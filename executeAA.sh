
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
