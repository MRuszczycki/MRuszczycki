
import os
import py_compile

class Modifier:
    # Variablen
    xVar = ''
    yVar = ''
    zVar = ''
    g1Var = ''
    g0Var = ''

    modifyIt = False

    # /Variablen
    def modifyCode(self):
        # placeholder für FileImput
        file = open("J_Do_It_2.py", 'r')
        codeLines = file.read().split("\n")
        file.close()

        modifyIt = False
        counter = 0

        for line in codeLines:


            if "#Variablen" in line:
                modifyIt = True
            elif "#/Variablen" in line:
                modifyIt = False
                break

            if modifyIt:
                lineSplitted = line.split('\'')

                if "xVar" in lineSplitted[0]:
                    lineSplitted[1] = self.xVar
                elif "yVar" in lineSplitted[0]:
                    lineSplitted[1] = self.yVar
                elif "zVar" in lineSplitted[0]:
                    lineSplitted[1] = self.zVar
                elif "g0Var" in lineSplitted[0]:
                    lineSplitted[1] = self.g0Var
                elif "g1Var" in lineSplitted[0]:
                    lineSplitted[1] = self.g1Var

                newLine = '\''.join(lineSplitted)
                codeLines[counter] = newLine

            counter += 1






        file = open("./Output/J_Do_It_2.py", 'w+')
        code = "\n".join(codeLines)
        file.write(code)
        file.close()
        py_compile.compile("./Output/J_Do_It_2.py")


        # os.system('start cmd /k "python compile.py build_ext --inplace"')
        #os.system("start python compile.py build_ext --inplace")

        return

    def setVariables(self, x, y, z, g0, g1):
        self.xVar = x
        self.yVar = y
        self.zVar = z
        self.g0Var = g0
        self.g1Var = g1
        return

    def __init__(self, g0, g1, x, y, z):
        self.setVariables(x, y, z, g0, g1)
        self.modifyCode()




