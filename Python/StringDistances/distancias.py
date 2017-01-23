#!/usr/bin/env python3

import sys
from multiprocessing import Process

class HammingMethodology:
    def __init__(self, pattern, secuence):
        self.pattern = pattern
        self.secuence = secuence
        self.secuenceLen = len(secuence)
        self.patternLen = len(pattern)
        self.threshold = 0.9

    '''
    Calculates the hamming distance of 2 given strings
    '''
    def hammingDistance(self, string1, string2):
        if(len(string1) != len(string2)):
            raise Exception("The strings have to be of the same size")

        hammingAcumulator = 0;
        for i in range(len(string1)):
            if string1[i] != string2[i]:
                hammingAcumulator += 1

        return hammingAcumulator

    '''
    Calculates the % of coincidence acording to a given string length and a
    Hamming distance.
    The calculation is due substracting the hamming distance to the string
    length. This is because a hamming distance of 0 means 100% coincidence and
    a hamming distance equal than the length of the string means 0% coincidence
    '''
    def hammingCoincidence(self, stringLength, hammingDistance):
        return (stringLength - hammingDistance)/stringLength

    def getCoincidenceArray(self):
        coincidenceArray = []
        lastCheckablePosition = self.secuenceLen - self.patternLen

        for windowStartPosition in range(lastStartPosition + 1):
            windowStopPosition = windowStartPosition + self.patternLen

            if(windowStopPosition <= self.secuenceLen):
                secuenceWindow = self.secuence[windowStartPosition:windowStopPosition]

                hd = self.hammingDistance(self.pattern, secuenceWindow)
                hc = self.hammingCoincidence(self.patternLen, hd)

                if hc > self.threshold:
                    coincidenceArray.append(windowStartPosition)

            sys.stdout.write("\rProcessing from %d to %d position" % (windowStartPosition, windowStopPosition))
            sys.stdout.flush()

        print("")

        return coincidenceArray;

    def getCoincidenceArrayWithJumps(self, start, jump):
        coincidenceArray = []
        lastStartPosition = self.secuenceLen - self.patternLen

        for windowStartPosition in range(start, lastStartPosition + 1, jump):
            windowStopPosition = windowStartPosition + self.patternLen

            if(windowStopPosition <= self.secuenceLen):
                secuenceWindow = self.secuence[windowStartPosition:windowStopPosition]

                hd = self.hammingDistance(self.pattern, secuenceWindow)
                hc = self.hammingCoincidence(self.patternLen, hd)

                if hc > self.threshold:
                    coincidenceArray.append(windowStartPosition)

        print(coincidenceArray)


    def getCoincidenceArrayMultiprocess(self, nProcesses):
        processList = []

        for i in range(nProcesses):
            processList.append(Process(target=self.getCoincidenceArrayWithJumps, args=(i, nProcesses)))
            processList[i].start()

        for process in processList:
            process.join()

    def getPatternLen(self):
        return self.patternLen

    def getSecuenceLen(self):
        return self.secuenceLen

    def getHammingDistance(self):
        return self.hammingDistance(self.pattern, self.secuence)

    def getHammingCoincidence(self):
        hm = self.getHammingDistance()
        patternDistance = len(self.pattern)
        return self.hammingCoincidence(patternDistance, hm)


def loadGenome(fileRoute):
    f = open(fileRoute, "r")
    pattern = ""

    for line in f:
        if line.startswith(">"):
            continue
        pattern += line.rstrip("\n")

    return pattern


if __name__ == '__main__':

    string1 = loadSinglePattern("patron.txt")
    string2 = loadSinglePattern("genomafragment.txt")

    hObject = HammingMethodology(string1, string2)

    print(hObject.getCoincidenceArray());

