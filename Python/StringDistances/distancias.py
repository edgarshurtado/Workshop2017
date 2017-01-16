#!/usr/bin/env python3


class HammingMethodology:
    def __init__(self, pattern, secuence):
        self.pattern = pattern
        self.secuence = secuence
        self.secuenceLen = len(secuence)
        self.patternLen = len(pattern)

    def hammingDistance(self, string1, string2):
        if(len(string1) != len(string2)):
            raise Exception("The strings have to be of the same size")

        hammingAcumulator = 0;
        for i in range(len(string1)):
            if string1[i] != string2[i]:
                hammingAcumulator += 1

        return hammingAcumulator

    def getPatternLen(self):
        return self.patternLen

    def getSecuenceLen(self):
        return self.secuenceLen

    def hammingCoincidence(self, stringLength, hammingDistance):
        return (stringLength - hammingDistance)/stringLength

    def getHammingDistance(self):
        return self.hammingDistance(self.pattern, self.secuence)

    def getHammingCoincidence(self):
        hm = self.getHammingDistance()
        patternDistance = len(self.pattern)
        return self.hammingCoincidence(patternDistance, hm)

    def getCoincidenceArray(self):
        coincidenceArray = []
        lastCheckablePosition = self.secuenceLen - self.patternLen

        for windowStartPosition in range(lastCheckablePosition):
            windowStopPosition = windowStartPosition + self.patternLen

            if(windowStopPosition < self.secuenceLen):
                secuenceWindow = self.secuence[windowStartPosition:windowStopPosition]

                hd = self.hammingDistance(self.pattern, secuenceWindow)
                hc = self.hammingCoincidence(self.patternLen, hd)

                coincidenceArray.append(hc)

        return coincidenceArray;



def loadSinglePattern(fileRoute):
    f = open(fileRoute, "r")
    f.readline()

    pattern = ""

    for line in f:
        pattern += line.rstrip("\n")

    return pattern


if __name__ == '__main__':

    string1 = loadSinglePattern("patron.txt")
    string2 = loadSinglePattern("genomafragment.txt")

    hObject = HammingMethodology(string1, string2)

    print(hObject.getCoincidenceArray());

