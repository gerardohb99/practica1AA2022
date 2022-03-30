from __future__ import print_function
# bustersAgents.py
# ----------------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


from builtins import range
from builtins import object
import util
from game import Agent
from game import Directions
from keyboardAgents import KeyboardAgent
import inference
import busters

from distanceCalculator import Distancer
from game import Actions
from game import Directions
import random, sys
# from wekaI import Weka


class NullGraphics(object):
    "Placeholder for graphics"

    def initialize(self, state, isBlue=False):
        pass

    def update(self, state):
        pass

    def pause(self):
        pass

    def draw(self, state):
        pass

    def updateDistributions(self, dist):
        pass

    def finish(self):
        pass


class KeyboardInference(inference.InferenceModule):
    """
    Basic inference module for use with the keyboard.
    """

    def initializeUniformly(self, gameState):
        "Begin with a uniform distribution over ghost positions."
        self.beliefs = util.Counter()
        for p in self.legalPositions: self.beliefs[p] = 1.0
        self.beliefs.normalize()

    def observe(self, observation, gameState):
        noisyDistance = observation
        emissionModel = busters.getObservationDistribution(noisyDistance)
        pacmanPosition = gameState.getPacmanPosition()
        allPossible = util.Counter()
        for p in self.legalPositions:
            trueDistance = util.manhattanDistance(p, pacmanPosition)
            if emissionModel[trueDistance] > 0:
                allPossible[p] = 1.0
        allPossible.normalize()
        self.beliefs = allPossible

    def elapseTime(self, gameState):
        pass

    def getBeliefDistribution(self):
        return self.beliefs


class BustersAgent(object):
    "An agent that tracks and displays its beliefs about ghost positions."

    def __init__(self, index=0, inference="ExactInference", ghostAgents=None, observeEnable=True,
                 elapseTimeEnable=True):
        inferenceType = util.lookup(inference, globals())
        self.inferenceModules = [inferenceType(a) for a in ghostAgents]
        self.observeEnable = observeEnable
        self.elapseTimeEnable = elapseTimeEnable
        # self.weka = Weka()
        # self.weka.start_jvm()

    def registerInitialState(self, gameState):
        "Initializes beliefs and inference modules"
        import __main__
        self.display = __main__._display
        for inference in self.inferenceModules:
            inference.initialize(gameState)
        self.ghostBeliefs = [inf.getBeliefDistribution() for inf in self.inferenceModules]
        self.firstMove = True

    def observationFunction(self, gameState):
        "Removes the ghost states from the gameState"
        agents = gameState.data.agentStates
        gameState.data.agentStates = [agents[0]] + [None for i in range(1, len(agents))]
        return gameState

    def getAction(self, gameState):
        "Updates beliefs, then chooses an action based on updated beliefs."
        # for index, inf in enumerate(self.inferenceModules):
        #    if not self.firstMove and self.elapseTimeEnable:
        #        inf.elapseTime(gameState)
        #    self.firstMove = False
        #    if self.observeEnable:
        #        inf.observeState(gameState)
        #    self.ghostBeliefs[index] = inf.getBeliefDistribution()
        # self.display.updateDistributions(self.ghostBeliefs)
        return self.chooseAction(gameState)

    def chooseAction(self, gameState):
        "By default, a BustersAgent just stops.  This should be overridden."
        return Directions.STOP
    
    def printMiniMap(self, entireMap, pacmanPos, ghostPos, size=2):
        miniMap = ""
        x,y = pacmanPos

        for i in range(y-size,y+size+1):
            for j in range(x-size,x+size+1):
                if i < 0 or i > (entireMap.height-1) or j < 0 or j > (entireMap.width-1) or entireMap[j][i] == True:
                    miniMap+="W,"
                elif entireMap[j][i] == False:
                    isGhost = False
                    for (ghostX,ghostY) in ghostPos:
                        if(ghostX == j and ghostY == i):
                            isGhost = True
                    if isGhost:
                        miniMap+="G,"
                    else:
                        miniMap+="E,"
        miniMap = miniMap[0:len(miniMap)-1]
        return miniMap
    
    def printHeader(self):
        data = ""
        data += "@relation " + self.__class__.__name__ + "training-data\n\n"
        data += "@attribute score NUMERIC\n"
        # Minimap para size=2
        for i in range(1,26):
            data += "@attribute minimap"+ str(i) +" {W,E,G}\n"

        data += "@attribute isGhostNorth {True, False}\n"
        data += "@attribute isGhostSouth {True, False}\n"
        data += "@attribute isGhostEast  {True, False}\n"
        data += "@attribute isGhostWest  {True, False}\n"
        data += "@attribute isFoodNorth  {True, False}\n"
        data += "@attribute isFoodSouth  {True, False}\n"
        data += "@attribute isFoodEast   {True, False}\n"
        data += "@attribute isFoodWest   {True, False}\n"

        data += "@attribute action{Stop,South,North,West,East}\n"
        data += "@attribute nextScore NUMERIC\n\n"
        data += "@data\n"
        return data

    def is_food (self, gameState, direction):
        _directions = {Directions.NORTH: (0, 1),
                   Directions.SOUTH: (0, -1),
                   Directions.EAST:  (1, 0),
                   Directions.WEST:  (-1, 0),
                   Directions.STOP:  (0, 0)}
        x, y = gameState.getPacmanPosition()

        xd, yd = _directions[direction]
        x += xd
        y += yd

        return gameState.data.food[x][y]

    def is_ghost (self, gameState, direction):
        _directions = {Directions.NORTH: (0, 1),
                   Directions.SOUTH: (0, -1),
                   Directions.EAST:  (1, 0),
                   Directions.WEST:  (-1, 0),
                   Directions.STOP:  (0, 0)}
        x, y = gameState.getPacmanPosition()

        xd, yd = _directions[direction]
        x += xd
        y += yd
        
        for i, ghost_position in enumerate(gameState.getGhostPositions()):          
            if ghost_position == (x,y) and gameState.getLivingGhosts()[i+1] == True:
                return True          

        return False

    def printLineDataV2(self, gameState, data=""):
        direction = 0
        alive_ghost = 0
        pacmanPos = gameState.getPacmanPosition()

        # # Ghosts vector center in pacman 
        # for i, ghostPos in enumerate(gameState.getGhostPositions()):
        #     if gameState.getLivingGhosts()[i+1] is True:
        #         data += str(ghostPos[0] - pacmanPos[0]) + ","
        #         data += str(ghostPos[1] - pacmanPos[1]) + ","
        #     else:
        #         found = False
        #         for i, ghostPos in enumerate(gameState.getGhostPositions()):
        #             if gameState.getLivingGhosts()[i+1] is True and found is False:
        #                 data += str(ghostPos[0] - pacmanPos[0]) + ","
        #                 data += str(ghostPos[1] - pacmanPos[1]) + ","
        #                 found = True


        # # Alive ghosts (index 0 corresponds to Pacman and is always false)
        # for i in range(1, len(gameState.getLivingGhosts())):
        #     if i == 1 and gameState.getLivingGhosts()[i] is False:
        #         alive_ghost += 1000

        #     elif i == 2 and gameState.getLivingGhosts()[i] is False:
        #         alive_ghost += 100

        #     elif i == 3 and gameState.getLivingGhosts()[i] is False:
        #         alive_ghost += 10

        #     elif i == 4 and gameState.getLivingGhosts()[i] is False:
        #         alive_ghost += 1

        # data += str(alive_ghost) + ","

        # Score
        data += str(gameState.getScore()) + ","

        # MiniMap
        data += self.printMiniMap(gameState.getWalls(), gameState.getPacmanPosition(), gameState.getGhostPositions()) + ","

        #Is ghost in directions
        # North
        data += str(self.is_ghost(gameState, Directions.NORTH)) + ","
        # South
        data += str(self.is_ghost(gameState, Directions.SOUTH)) + ","
        # East
        data += str(self.is_ghost(gameState, Directions.EAST)) + ","
        # West
        data += str(self.is_ghost(gameState, Directions.WEST)) + ","

        #Is food in directions
        # North
        data += str(self.is_food(gameState, Directions.NORTH)) + ","
        # South
        data += str(self.is_food(gameState, Directions.SOUTH)) + ","
        # East
        data += str(self.is_food(gameState, Directions.EAST)) + ","
        # West
        data += str(self.is_food(gameState, Directions.WEST)) + ","


        return data



class BustersKeyboardAgent(BustersAgent, KeyboardAgent):
    "An agent controlled by the keyboard that displays beliefs about ghost positions."

    def __init__(self, index=0, inference="KeyboardInference", ghostAgents=None):
        KeyboardAgent.__init__(self, index)
        BustersAgent.__init__(self, index, inference, ghostAgents)

    def getAction(self, gameState):
        return BustersAgent.getAction(self, gameState)

    def chooseAction(self, gameState):
        # print(self.printMiniMap(gameState.getWalls(), gameState.getPacmanPosition(), gameState.getGhostPositions()))
        return KeyboardAgent.getAction(self, gameState)

'''Random PacMan Agent'''


class RandomPAgent(BustersAgent):

    def registerInitialState(self, gameState):
        BustersAgent.registerInitialState(self, gameState)
        self.distancer = Distancer(gameState.data.layout, False)

    ''' Example of counting something'''

    def countFood(self, gameState):
        food = 0
        for width in gameState.data.food:
            for height in width:
                if (height == True):
                    food = food + 1
        return food

    ''' Print the layout'''

    def printGrid(self, gameState):
        table = ""
        ##print(gameState.data.layout) ## Print by terminal
        for x in range(gameState.data.layout.width):
            for y in range(gameState.data.layout.height):
                food, walls = gameState.data.food, gameState.data.layout.walls
                table = table + gameState.data._foodWallStr(food[x][y], walls[x][y]) + ","
        table = table[:-1]
        return table

    def chooseAction(self, gameState):
        move = Directions.STOP
        legal = gameState.getLegalActions(0)  ##Legal position from the pacman
        move_random = random.randint(0, 3)
        if (move_random == 0) and Directions.WEST in legal:  move = Directions.WEST
        if (move_random == 1) and Directions.EAST in legal: move = Directions.EAST
        if (move_random == 2) and Directions.NORTH in legal:   move = Directions.NORTH
        if (move_random == 3) and Directions.SOUTH in legal: move = Directions.SOUTH
        return move


class GreedyBustersAgent(BustersAgent):
    "An agent that charges the closest ghost."

    def registerInitialState(self, gameState):
        "Pre-computes the distance between every two points."
        BustersAgent.registerInitialState(self, gameState)
        self.distancer = Distancer(gameState.data.layout, False)

    def chooseAction(self, gameState):
        """
        First computes the most likely position of each ghost that has
        not yet been captured, then chooses an action that brings
        Pacman closer to the closest ghost (according to mazeDistance!).

        To find the mazeDistance between any two positions, use:
          self.distancer.getDistance(pos1, pos2)

        To find the successor position of a position after an action:
          successorPosition = Actions.getSuccessor(position, action)

        livingGhostPositionDistributions, defined below, is a list of
        util.Counter objects equal to the position belief
        distributions for each of the ghosts that are still alive.  It
        is defined based on (these are implementation details about
        which you need not be concerned):

          1) gameState.getLivingGhosts(), a list of booleans, one for each
             agent, indicating whether or not the agent is alive.  Note
             that pacman is always agent 0, so the ghosts are agents 1,
             onwards (just as before).

          2) self.ghostBeliefs, the list of belief distributions for each
             of the ghosts (including ghosts that are not alive).  The
             indices into this list should be 1 less than indices into the
             gameState.getLivingGhosts() list.
        """
        pacmanPosition = gameState.getPacmanPosition()
        legal = [a for a in gameState.getLegalPacmanActions()]
        livingGhosts = gameState.getLivingGhosts()
        livingGhostPositionDistributions = \
            [beliefs for i, beliefs in enumerate(self.ghostBeliefs)
             if livingGhosts[i + 1]]
        return Directions.EAST


class BasicAgentAA(BustersAgent):

    def registerInitialState(self, gameState):
        BustersAgent.registerInitialState(self, gameState)
        self.distancer = Distancer(gameState.data.layout, False)
        self.countActions = 0

    ''' Example of counting something'''

    def countFood(self, gameState):
        food = 0
        for width in gameState.data.food:
            for height in width:
                if (height == True):
                    food = food + 1
        return food

    ''' Print the layout'''

    def printGrid(self, gameState):
        table = ""
        # print(gameState.data.layout) ## Print by terminal
        for x in range(gameState.data.layout.width):
            for y in range(gameState.data.layout.height):
                food, walls = gameState.data.food, gameState.data.layout.walls
                table = table + gameState.data._foodWallStr(food[x][y], walls[x][y]) + ","
        table = table[:-1]
        return table

    def printInfo(self, gameState):
        print("---------------- TICK ", self.countActions, " --------------------------")
        # Map size
        width, height = gameState.data.layout.width, gameState.data.layout.height
        print("Width: ", width, " Height: ", height)
        # Pacman position
        print("Pacman position: ", gameState.getPacmanPosition())
        # Legal actions for Pacman in current position
        print("Legal actions: ", gameState.getLegalPacmanActions())
        # Pacman direction
        print("Pacman direction: ", gameState.data.agentStates[0].getDirection())
        # Number of ghosts
        print("Number of ghosts: ", gameState.getNumAgents() - 1)
        # Alive ghosts (index 0 corresponds to Pacman and is always false)
        print("Living ghosts: ", gameState.getLivingGhosts())
        # Ghosts positions
        print("Ghosts positions: ", gameState.getGhostPositions())
        # Ghosts directions
        print("Ghosts directions: ",
              [gameState.getGhostDirections().get(i) for i in range(0, gameState.getNumAgents() - 1)])
        # Manhattan distance to ghosts
        print("Ghosts distances: ", gameState.data.ghostDistances)
        # Pending pac dots
        print("Pac dots: ", gameState.getNumFood())
        # Manhattan distance to the closest pac dot
        print("Distance nearest pac dots: ", gameState.getDistanceNearestFood())
        # Map walls
        print("Map:")
        print(gameState.getWalls())
        # Score
        print("Score: ", gameState.getScore())

    def vectorToAction(self, vector, legal, lastAction):
        dx, dy = vector
        max_d = max(dx, dy)

        # Dar prioridad al diferencial mas grande
        if max_d == dy:
            if dy > 0 and Directions.NORTH in legal and Directions.SOUTH is not lastAction:
                return Directions.NORTH
            if dy < 0 and Directions.SOUTH in legal and Directions.NORTH is not lastAction:
                return Directions.SOUTH
            if dx < 0 and Directions.WEST in legal and Directions.EAST is not lastAction:
                return Directions.WEST
            if dx > 0 and Directions.EAST in legal and Directions.WEST is not lastAction:
                return Directions.EAST
        else:
            if dx < 0 and Directions.WEST in legal and Directions.EAST is not lastAction:
                return Directions.WEST
            if dx > 0 and Directions.EAST in legal and Directions.WEST is not lastAction:
                return Directions.EAST
            if dy > 0 and Directions.NORTH in legal and Directions.SOUTH is not lastAction:
                return Directions.NORTH
            if dy < 0 and Directions.SOUTH in legal and Directions.NORTH is not lastAction:
                return Directions.SOUTH

        # Cuando se queda sin acciones legales hacemos uso de un random action
        direction = Directions.STOP
        legal.remove(Directions.STOP)
        while direction is Directions.STOP:
            move_random = random.randint(0, 3)
            if (move_random == 0) and Directions.WEST in legal and (
                    Directions.EAST is not lastAction or len(legal) == 1):
                direction = Directions.WEST
            elif (move_random == 1) and Directions.EAST in legal and (
                    Directions.WEST is not lastAction or len(legal) == 1):
                direction = Directions.EAST
            elif (move_random == 2) and Directions.NORTH in legal and (
                    Directions.SOUTH is not lastAction or len(legal) == 1):
                direction = Directions.NORTH
            elif (move_random == 3) and Directions.SOUTH in legal and (
                    Directions.NORTH is not lastAction or len(legal) == 1):
                direction = Directions.SOUTH
        return direction


    def chooseAction(self, gameState):
        self.countActions = self.countActions + 1
        self.printInfo(gameState)
        move = Directions.STOP
        legal = gameState.getLegalActions(0)  ##Legal position from the pacman
        minDistance = 10 ** 10
        livingGhosts = gameState.getLivingGhosts()
        lastAction = gameState.data.agentStates[0].getDirection()
        vec = (1, 1)

        for i in range(1, len(livingGhosts)):
            if livingGhosts[i]:

                distance = (gameState.data.ghostDistances[i - 1], 10 ** 10)[
                    gameState.data.ghostDistances[i - 1] is None]
                if distance < minDistance:
                    minDistance = distance
                    vecx = gameState.getGhostPositions()[i - 1][0] - gameState.getPacmanPosition()[0]
                    vecy = gameState.getGhostPositions()[i - 1][1] - gameState.getPacmanPosition()[1]
                    vec = (vecx, vecy)


        move = self.vectorToAction(vec, legal, lastAction)
      
        return move

    def printLineData(self, gameState):
        data = ""
        # Pacman position
        data = str(gameState.getPacmanPosition()[0]) + ", " + str(gameState.getPacmanPosition()[1]) + ", "

        # Ghosts positions
        for i in gameState.getGhostPositions():
            data += str(i[0]) + ", "
            data += str(i[1]) + ", "

        # Ghosts distances (recordar que cuando el fantasma esta muerto la distancia es 1)
        for i in gameState.data.ghostDistances:
            data += str(i) + ", "

        # Legal actions for Pacman in current position
        if "North" in gameState.getLegalPacmanActions():
            data += "True, "
        else:
            data += "False, "

        if "South" in gameState.getLegalPacmanActions():
            data += "True, "
        else:
            data += "False, "

        if "East" in gameState.getLegalPacmanActions():
            data += "True, "
        else:
            data += "False, "

        if "West" in gameState.getLegalPacmanActions():
            data += "True, "
        else:
            data += "False, "

        # Pacman direction (last action)
        data += str(gameState.data.agentStates[0].getDirection()) + ", "

        # Alive ghosts (index 0 corresponds to Pacman and is always false)
        for i in range(1, len(gameState.getLivingGhosts())):
            data += str(gameState.getLivingGhosts()[i]) + ", "

            # Score
        data += str(gameState.getScore()) + "\n"
        return data

    # Para ver los puntos conflictivos seria bueno crearse un array en el que vamos evaluando puntos conflictivos para leugo consultar dicha lista antes
    # realizar cualquier tipo de movimiento 

class AgentAA(BustersAgent):

    def registerInitialState(self, gameState):
        BustersAgent.registerInitialState(self, gameState)
        self.distancer = Distancer(gameState.data.layout, False)
        self.countActions = 0


    def countFood(self, gameState):
        food = 0
        for width in gameState.data.food:
            for height in width:
                if (height == True):
                    food = food + 1
        return food

    ''' Print the layout'''

    def printGrid(self, gameState):
        table = ""
        # print(gameState.data.layout) ## Print by terminal
        for x in range(gameState.data.layout.width):
            for y in range(gameState.data.layout.height):
                food, walls = gameState.data.food, gameState.data.layout.walls
                table = table + gameState.data._foodWallStr(food[x][y], walls[x][y]) + ","
        table = table[:-1]
        return table

    def chooseAction(self, gameState):
        self.countActions = self.countActions + 1
        move = Directions.STOP
        legal = gameState.getLegalActions(0)  ##Legal position from the pacman

        rawX = self.printLineDataV2(gameState).split(",")
        rawX.pop()
        x = []
        for i,val in enumerate(rawX):
            try:
                if i == 8:
                    raise Exception
                val = int(val)
                x.append(val)
            except:
                x.append(val)

        move = self.weka.predict("./Weka_data/aprox_2/t1_LMT_2_2.model", x, "./Weka_data/aprox_2/t1_training_2_2.arff")
        while move not in legal:
            move_random = random.randint(0, 3)
            if (move_random == 0) and Directions.WEST in legal:  move = Directions.WEST
            if (move_random == 1) and Directions.EAST in legal: move = Directions.EAST
            if (move_random == 2) and Directions.NORTH in legal:   move = Directions.NORTH
            if (move_random == 3) and Directions.SOUTH in legal: move = Directions.SOUTH
        return move

    