#CLIPPING EXAMPLE

#Name of the Book
#- Data for the clipping position page, position, time
#
#clipping text
#==========

import csv

inputFile = "clip.txt"
outputFile = "sal.csv"

fr = open(inputFile, 'r')
fw = open(outputFile, 'w')
writer = csv.writer(fw, delimiter=",")
writer.writerow(["Hash","Book","Location","Text"])
auxList = []
count = 0
for i in fr:
    if count == 0:
        auxList.append(i)
    if count == 1:
        auxList.append(i)
    if count == 3:
        auxList.append(i)
    if count == 4:
        #Generate Hash from List
        auxList.insert(0,hash(str(auxList)))
        writer.writerow(auxList)
        auxList = []
        count = 0
        continue
    count+=1

fr.close()
fw.close()
