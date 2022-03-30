rm output.arff

python busters.py -l freeHunt.lay 
python busters.py -l freeHunt2.lay
python busters.py -l freeHunt3.lay -g RandomGhost
python busters.py -l freeHunt4.lay -g RandomGhost
python busters.py -l freeHunt5.lay -g RandomGhost

python busters.py -l sandClockHunt.lay 
python busters.py -l sandClockHunt2.lay
python busters.py -l sandClockHunt3.lay -g RandomGhost
python busters.py -l sandClockHunt4.lay -g RandomGhost
python busters.py -l sandClockHunt5.lay -g RandomGhost

python busters.py -l theLMap.lay 
python busters.py -l theLMap2.lay
python busters.py -l theLMap3.lay -g RandomGhost
python busters.py -l theLMap4.lay -g RandomGhost
python busters.py -l theLMap5.lay -g RandomGhost

python busters.py -l dotHunt.lay 
python busters.py -l dotHunt2.lay
python busters.py -l dotHunt3.lay -g RandomGhost
python busters.py -l dotHunt4.lay -g RandomGhost
python busters.py -l dotHunt5.lay -g RandomGhost

python busters.py -l maziMaze.lay 
python busters.py -l maziMaze2.lay
python busters.py -l maziMaze4.lay -g RandomGhost
python busters.py -l maziMaze5.lay -g RandomGhost
python busters.py -l maziMaze6.lay -g RandomGhost

mv output.arff t1_training_allData.arff

rm output.arff

python busters.py -l freeHunt.lay 
python busters.py -l freeHunt5.lay -g RandomGhost

python busters.py -l sandClockHunt.lay 
python busters.py -l sandClockHunt5.lay -g RandomGhost

python busters.py -l theLMap.lay 
python busters.py -l theLMap5.lay -g RandomGhost

python busters.py -l dotHunt.lay 
python busters.py -l dotHunt5.lay -g RandomGhost

python busters.py -l maziMaze.lay 
python busters.py -l maziMaze6.lay -g RandomGhost

mv output.arff t1_test_sameMaps_allData.arff

rm output.arff

python busters.py -l testTube.lay 
python busters.py -l testTube.lay -g RandomGhost

python busters.py -l 20Hunt.lay 
python busters.py -l 20Hunt.lay -g RandomGhost

python busters.py -l newmap.lay 
python busters.py -l newmap.lay -g RandomGhost

python busters.py -l extra.lay 
python busters.py -l extra.lay -g RandomGhost

python busters.py -l capsuleClassic.lay 
python busters.py -l capsuleClassic.lay -g RandomGhost

mv output.arff t1_test_otherMaps_allData.arff
