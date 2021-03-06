rm output.arff

python busters.py -l freeHunt.lay -p BasicAgentAA  -t 0
python busters.py -l freeHunt2.lay -p BasicAgentAA -t 0
python busters.py -l freeHunt3.lay -p BasicAgentAA -t 0 -g RandomGhost
python busters.py -l freeHunt4.lay -p BasicAgentAA -t 0 -g RandomGhost
python busters.py -l freeHunt5.lay -p BasicAgentAA -t 0 -g RandomGhost

python busters.py -l sandClockHunt.lay -p BasicAgentAA  -t 0
python busters.py -l sandClockHunt2.lay -p BasicAgentAA -t 0
python busters.py -l sandClockHunt3.lay -p BasicAgentAA -t 0 -g RandomGhost
python busters.py -l sandClockHunt4.lay -p BasicAgentAA -t 0 -g RandomGhost
python busters.py -l sandClockHunt5.lay -p BasicAgentAA -t 0 -g RandomGhost

python busters.py -l theLMap.lay -p BasicAgentAA  -t 0
python busters.py -l theLMap2.lay -p BasicAgentAA -t 0
python busters.py -l theLMap3.lay -p BasicAgentAA -t 0 -g RandomGhost
python busters.py -l theLMap4.lay -p BasicAgentAA -t 0 -g RandomGhost
python busters.py -l theLMap5.lay -p BasicAgentAA -t 0 -g RandomGhost

python busters.py -l dotHunt.lay -p BasicAgentAA  -t 0
python busters.py -l dotHunt2.lay -p BasicAgentAA -t 0
python busters.py -l dotHunt3.lay -p BasicAgentAA -t 0 -g RandomGhost
python busters.py -l dotHunt4.lay -p BasicAgentAA -t 0 -g RandomGhost
python busters.py -l dotHunt5.lay -p BasicAgentAA -t 0 -g RandomGhost

python busters.py -l maziMaze.lay -p BasicAgentAA  -t 0
python busters.py -l maziMaze2.lay -p BasicAgentAA -t 0
python busters.py -l maziMaze4.lay -p BasicAgentAA -t 0 -g RandomGhost
python busters.py -l maziMaze5.lay -p BasicAgentAA -t 0 -g RandomGhost
python busters.py -l maziMaze6.lay -p BasicAgentAA -t 0 -g RandomGhost

mv output.arff t1_training_allData.arff

rm output.arff

python busters.py -l freeHunt.lay -p BasicAgentAA  -t 0
python busters.py -l freeHunt5.lay -p BasicAgentAA -t 0 -g RandomGhost

python busters.py -l sandClockHunt.lay -p BasicAgentAA  -t 0
python busters.py -l sandClockHunt5.lay -p BasicAgentAA -t 0 -g RandomGhost

python busters.py -l theLMap.lay -p BasicAgentAA  -t 0
python busters.py -l theLMap5.lay -p BasicAgentAA -t 0 -g RandomGhost

python busters.py -l dotHunt.lay -p BasicAgentAA  -t 0
python busters.py -l dotHunt5.lay -p BasicAgentAA -t 0 -g RandomGhost

python busters.py -l maziMaze.lay -p BasicAgentAA  -t 0
python busters.py -l maziMaze6.lay -p BasicAgentAA -t 0 -g RandomGhost

mv output.arff t1_test_sameMaps_allData.arff

rm output.arff

python busters.py -l testTube.lay -p BasicAgentAA  -t 0
python busters.py -l testTube.lay -p BasicAgentAA -t 0 -g RandomGhost

python busters.py -l 20Hunt.lay -p BasicAgentAA  -t 0
python busters.py -l 20Hunt.lay -p BasicAgentAA -t 0 -g RandomGhost

python busters.py -l newmap.lay -p BasicAgentAA  -t 0
python busters.py -l newmap.lay -p BasicAgentAA -t 0 -g RandomGhost

python busters.py -l extra.lay -p BasicAgentAA  -t 0
python busters.py -l extra.lay -p BasicAgentAA -t 0 -g RandomGhost

python busters.py -l capsuleClassic.lay -p BasicAgentAA  -t 0
python busters.py -l capsuleClassic.lay -p BasicAgentAA -t 0 -g RandomGhost

mv output.arff t1_test_otherMaps_allData.arff
