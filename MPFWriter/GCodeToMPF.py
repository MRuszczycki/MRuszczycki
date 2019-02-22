#This is an easy Converter which is called after a GCode-File is written
#to use its output by splitting the lines and Convert it to a MPF

import io

from UM.Mesh.MeshWriter import MeshWriter
from UM.Logger import Logger
from UM.Application import Application
from UM.Settings.InstanceContainer import InstanceContainer
from UM.PluginRegistry import PluginRegistry

class GCodeToMPF():

    version = 1

    gCodeFile = None;

    path = ""#"C:\\Users\\Max\\Documents\\Dotos_programm"

    output =""

    verrechnungswert = 0.4497

    tempWinkel = 0.0

    counter = 10


    """def __init__(self):
        super.__init__()
        #self.openFile("C:/Users/Max/Desktop/a.gcode")"""

    @classmethod
    def openFile(self, pathSource, pathTarget, head, end):
        gCodeFile = open(pathSource, "r")


        gCodeLines = gCodeFile.readlines()

         #with open(path[:-5] + 'mpf', 'w+') as f:
        with io.open(pathTarget, "w+", encoding="utf8") as f:

            for line in (head.readlines()):
                f.write("N" + str(self.counter) + " " + line)
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
                f.write("N" + str(self.counter) + " " + line)
                self.counter += 10
            #f.writelines(end.readlines())
        self.counter = 10
        self.tempWinkel = 0.0

        return

    @classmethod
    def readLine(self, line):


        if (line[:2] != "G0" and line[:2] != "G1"):

            if line[:1] is not ';':
                if line[:3] == "G92":
                    self.tempWinkel = 0.0
                self.output += ";" + line
            else:
                self.output += line
            return
        else:

            containsXYZ = line.__contains__('X') or line.__contains__('Y') or line.__contains__('Z')

            elements = line.split(" ")
            checkEValue = elements[-1:].__str__()



            if (containsXYZ):
                self.output += "G1 "
            else:
                self.output += "G0 " + self.calculate(checkEValue[3:-4], containsXYZ)
                return

            self.roundXYZ(elements)


            if checkEValue[2:3] is 'E':
                self.output += " ".join(elements[1:-1]) + " " + (self.calculate(checkEValue[3:-4], containsXYZ))
                return
            else:
                self.output += " ".join(elements[1:])

    @classmethod
    def calculate(self, value, containsXYZ):
        #value = value.__getitem__(0)
        value = float(value)
        rEplace = value * self.verrechnungswert * 360.0 * 1.02 * 2

        temp = rEplace
        rEplace = rEplace - self.tempWinkel
        self.tempWinkel = temp


        if (containsXYZ):
            return ("SP1=IC(" + str(round(rEplace)) + ")\n")
        else:
            return ("SPOS=IC(" + str(round(rEplace)) + ")\n")


    @classmethod
    def roundXYZ(self, elem):
        newlineBoolean = None
        for i in range(len(elem)):

            temp = elem[i]
            if("\n" in temp):
                newlineBoolean = True
            if(self.hasNumbers(temp)):
                try:
                    number = float(temp[1:])

                    if(temp.__contains__('X')):
                        elem[i] = 'X'+ ('%.1f' % number)
                    elif(temp.__contains__('Y')):
                        elem[i] = 'Y' + ('%.1f' % number)
                    elif(temp.__contains__('Z')):
                        elem[i] = 'Z' + ('%.1f' % number)

                    if(newlineBoolean):
                        elem[i] += "\n"
                except ValueError:
                    pass
            newlineBoolean = False
        return

    @classmethod
    def hasNumbers(self, inputString):
        return any(char.isdigit() for char in inputString)