
import datetime
import time
import random
def dataset():
    "This is a function that generates simulated data type"
    #The order of the objects must be sequential, ( ie. 1,2,3...32. ) since each number references a different pipeline region.
    #Your generated dataset needs to return a single set of data, that has 32 entries, with each entry returning 16 floats.
    #The 16 floats returned will be between 0 and 1

    mySimulatedData = list()

    index = 0

    while index <32:
      SensorReadings = list()
      index2 = 0
      while index2<16:
        SensorReadings.append(index2)
        index2 = index2 + 1
      mySimulatedData.append(SensorReadings)
      index = index + 1
    return mySimulatedData



def writeDatatoFile(myData):
 ts = time.time()
 st = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')


 dataLog = myData
 # Open for 'w'riting
 f = open('dataLog.txt', 'w')
 # Write text to file
 f.write(str(dataLog))
 # Close the file
 f.close()
 return

mydata = dataset()
writeDatatoFile(mydata)

