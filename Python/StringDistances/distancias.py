#!/usr/bin/env python3


class HammingMethodology:
    def __init__(self, pattern, secuence):
        self.pattern = pattern
        self.secuence = secuence

    def hammingDistance(self, string1, string2):
        if(len(string1) != len(string2)):
            raise Exception("The strings have to be of the same size")

        hammingAcumulator = 0;
        for i in range(len(string1)):
            if string1[i] != string2[i]:
                hammingAcumulator += 1

        return hammingAcumulator

    def hammingCoincidence(self, stringLength, hammingDistance):
        return (stringLength - hammingDistance)/stringLength

    def getHammingDistance(self):
        return self.hammingDistance(self.pattern, self.secuence)

    def getHammingCoincidence(self):
        hm = self.getHammingDistance()
        patternDistance = len(self.pattern)
        return self.hammingCoincidence(patternDistance, hm)


if __name__ == '__main__':
    string1 = 'ACGGACACAGA'
    string2 = 'ACAGACCAAAT'

    hObject = HammingMethodology(string1, string2)

    hDistance = hObject.getHammingDistance()
    hCoincidence = hObject.getHammingCoincidence()

    print("Comparition between: " + string1 + " " + string2)

    print("Hamming distance: " + str(hDistance))
    print("Fragment coincidence: " + str(hCoincidence))

