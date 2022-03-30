
rm output.arff
python busters.py -l freeHunt.lay -p BasicAgentAA  -t 0 -g RandomGhost
python busters.py -l freeHunt5.lay -p BasicAgentAA -t 0 -g RandomGhost
wc -l output.arff > salida-sameMaps-freeHunt.txt

rm output.arff
python busters.py -l sandClockHunt.lay -p BasicAgentAA  -t 0 -g RandomGhost
python busters.py -l sandClockHunt5.lay -p BasicAgentAA -t 0 -g RandomGhost
wc -l output.arff > salida-sameMaps-sandClockHunt.txt

rm output.arff
python busters.py -l theLMap.lay -p BasicAgentAA  -t 0 -g RandomGhost
python busters.py -l theLMap5.lay -p BasicAgentAA -t 0 -g RandomGhost
wc -l output.arff > salida-sameMaps-theLMap.txt

rm output.arff
python busters.py -l dotHunt.lay -p BasicAgentAA  -t 0 -g RandomGhost
python busters.py -l dotHunt5.lay -p BasicAgentAA -t 0 -g RandomGhost
wc -l output.arff > salida-sameMaps-dotHunt.txt

rm output.arff
python busters.py -l maziMaze.lay -p BasicAgentAA  -t 0 -g RandomGhost
python busters.py -l maziMaze6.lay -p BasicAgentAA -t 0 -g RandomGhost
wc -l output.arff > salida-sameMaps-maziMaze.txt

# OtherMaps
rm output.arff
python busters.py -l testTube.lay -p BasicAgentAA  -t 0 -g RandomGhost
python busters.py -l testTube.lay -p BasicAgentAA -t 0 -g RandomGhost
wc -l output.arff > salida-otherMaps-testTube.txt

rm output.arff
python busters.py -l 20Hunt.lay -p BasicAgentAA  -t 0 -g RandomGhost
python busters.py -l 20Hunt.lay -p BasicAgentAA -t 0 -g RandomGhost
wc -l output.arff > salida-otherMaps-20Hunt.txt

rm output.arff
python busters.py -l newmap.lay -p BasicAgentAA  -t 0 -g RandomGhost
python busters.py -l newmap.lay -p BasicAgentAA -t 0 -g RandomGhost
wc -l output.arff > salida-otherMaps-newmap.txt

rm output.arff
python busters.py -l extra.lay -p BasicAgentAA  -t 0 -g RandomGhost
python busters.py -l extra.lay -p BasicAgentAA -t 0 -g RandomGhost
wc -l output.arff > salida-otherMaps-extra.txt

rm output.arff
python busters.py -l capsuleClassic.lay -p BasicAgentAA  -t 0 -g RandomGhost
python busters.py -l capsuleClassic.lay -p BasicAgentAA -t 0 -g RandomGhost
wc -l output.arff > salida-otherMaps-capsuleClassic.txt
