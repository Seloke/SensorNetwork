
import datetime
import time
import random



def dataset(Cluster = 32, SensorinCluster = 16):

    "This is a function that generates simulated data type"

    #The order of the objects must be sequential, ( ie. 1,2,3...32. ) since each number references a different pipeline region.
    #Your generated dataset needs to return a single set of data, that has 32 entries, with each entry returning 16 floats.
    #The 16 floats returned will be between 0 and 1

    mySimulatedData = list()
    index = 0
    while index < Cluster:
      SensorReadings = list()
      index2 = 0
      while index2<SensorinCluster:
        SensorReadings.append(random.random()) #random.random()
        index2 = index2 + 1
      mySimulatedData.append(SensorReadings)
      index = index + 1
    return mySimulatedData

def writeDatatoFile(myData):

    #Problem 2:
    # Once you have your dataset to work with you will need to show that you can store this data with every iteration of the data set so no data is lost.
    # ACCEPTANCE CRITERIA
    # Every time your data set is generated the output should be stored and saved
    # For a challenge you could try to write the data to a file
    # New data should not overwrite historical data
    # For an extra challenge you can try to date and time stamp each interval of data collection


 ts = time.time()
 st = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')

 f = open('dataLog.txt', 'a')
 ind = 0

 logData = list()

 while ind <len(myData):
     dataLog = list()
     dataLog.append(st)
     dataLog.append('Cluster {0}'.format(ind +1))
     extractData = myData[ind]

     ind2 = 0
     while ind2<len(myData[ind]):
         dataLog.append(extractData[ind2])
         ind2 = ind2 +1
     f.write(str(dataLog))
     f.write('\n')

     logData.append(dataLog)
     ind = ind +1

 f.close()
 return logData

def errorGenerator(mydata, errorText = "Err"):
    # Create a copy of a "corrupted" data set containing at least one entry where the value is "err"

    #Gereate a ramdom number interger between 0 and 32

    ClustersWithErrs = int(round(len(mydata)*(random.random())))
    SensorWithErrs  = int(round(len(mydata[0])*(random.random())))
    # Convert the string to a numerical value that can be uniquely identified as the error

    if ClustersWithErrs > 1:
        ind = 0
        while ind < ClustersWithErrs:
            if SensorWithErrs > 1:
               ind2 = 0
               while  ind2 < SensorWithErrs:
                    ClustersErrs = int(round(len(mydata)*(random.random())))
                    SensorErrs  = int(round(len(mydata[0])*(random.random())))

                    if ClustersErrs <len(mydata):
                        if SensorErrs <len(mydata[0]):
                           tempdata = mydata[ClustersErrs]
                           tempdata[SensorErrs] = str(errorText)
                        else:
                            pass
                    else:
                        pass

                    ind2 = ind2+1
            else:
                pass
            ind = ind +1

    else:
        pass


    return mydata

def err2Num (errLog,errorText = "Err", errorValue = 999):
    ind = 0
    while ind < len(errLog):
        ind2 = 0
        while ind2 < len(errLog[ind]):
           if errLog[ind][ind2] == errorText:
               errLog[ind][ind2] = errorValue
           else:
             pass
           ind2 = ind2 + 1
        ind = ind +1

    return errLog

def writeErrorFile(str2Num,errorValue = 999):

    f = open('ErrorLog.txt', 'a')
    ind = 0
    while ind < len(str2Num):
        ind2 = 0
        while ind2 < len(str2Num[ind]):
           createErrorLog = list()
           if str2Num[ind][ind2] == errorValue:
               createErrorLog.append(str2Num[ind][0])
               createErrorLog.append(str2Num[ind][1])
               createErrorLog.append("Sensor {0}".format(ind +1))
               f.write(str(createErrorLog))
               f.write('\n')
           else:
             pass
           ind2 = ind2 + 1
        ind = ind + 1
    f.close()
    return

def programMain():

    mydata = dataset()                  # Create a data set
    errLog = errorGenerator(mydata)     # Generate random errors in that data set
    logData = writeDatatoFile(mydata)   # Write data set with possible errors to a text file
    str2Num = err2Num (logData)         # Convert the errors in the date to numeric values
    errLog = writeErrorFile(str2Num)    # Create a file with all the errors

    return

programMain()

