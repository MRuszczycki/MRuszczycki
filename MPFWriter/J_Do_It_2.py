#This is an easy Converter which is called after a GCode-File is written
#to use its output by splitting the lines and Convert it to a MPF

import io

class DoIt():

    version = 2
    gCodeFile = None
    path = ""
    output =""
    tempWinkel = 0.0
    counter = 10

    #Variablen
    verrechnungswert = 0.4497
    xVar = 'X'
    yVar = 'Y'
    zVar = 'Z'
    g1Var = 'G1'
    g0Var = 'G0'
    #/Variablen

    @classmethod
    def openFile(self, pathSource, pathTarget, head, end):
        gCodeFile = open(pathSource, "r")


        gCodeLines = gCodeFile.readlines()

         #with open(path[:-5] + 'mpf', 'w+') as f:
        with io.open(pathTarget, "w+", encoding="utf8") as f:

            for line in (head.readlines()):
                f.write("N" + self.counter.__str__() + " " + line)
                self.counter += 10
            #f.writelines(head.readlines())
            f.write("\n\n\n")

            for line in gCodeLines:
                self.output += "N" + self.counter.__str__() + " "
                self.readLine(line)
                self.counter += 10
                f.write(self.output)
                self.output = ""

            f.write("\n\n\n")

            for line in (end.readlines()):
                f.write("N" + self.counter.__str__() + " " + line)
                self.counter += 10
            #f.writelines(end.readlines())
        self.counter = 10
        self.tempWinkel = 0.0

        return

    @classmethod
    def readLine(self, line):

        elements = line.split(" ")

        if(elements[0] != "G0" and elements[0] != "G1"):
            if ";" not in elements[0]:
                if elements[0] == "G92":
                    self.tempWinkel = 0.0
                self.output += ";" + line
            else:
                self.output += line
            return
        else:
            containsXYZ = line.__contains__('X') or line.__contains__('Y') or line.__contains__('Z')
            checkEValue = elements[-1:].__str__()

            if containsXYZ:
                self.output += self.g1Var + " "
            else:
                self.output += self.g0Var + " " + self.calculate(checkEValue[3:-4], containsXYZ)
                return

            if checkEValue[2:3] is 'E':
                self.output += self.replaceVars(elements[1:-1]) + (self.calculate(checkEValue[3:-4], containsXYZ))
                return
            else:
                self.output += " ".join(elements[1:])

    @classmethod
    def replaceVars(self, elements):
        moddedLine = ''

        for strValue in elements:
            if 'X' in strValue:
                moddedLine += self.xVar + strValue[1:] + " "
            elif 'Y' in strValue:
                moddedLine += self.yVar + strValue[1:] + " "
            elif 'Z' in strValue:
                moddedLine += self.zVar + strValue[1:] + " "
            else:
                moddedLine += strValue

        return moddedLine



    @classmethod
    def calculate(self, value, containsXYZ):
        # value = value.__getitem__(0)
        value = float(value)
        rEplace = value * self.verrechnungswert * 360.0 * 1.02 * 2

        temp = rEplace
        rEplace = rEplace - self.tempWinkel
        self.tempWinkel = temp

        if (containsXYZ):
            return ("SP1=IC(" + ('%.3f' % rEplace) + ")\n")
        else:
            return ("SPOS=IC(" + ('%.3f' % rEplace) + ")\n")




