from Modifier import Modifier
import tkinter as tk

class Application():
    erstellen = None
    g0Field = None
    g1Field = None
    xField = None
    yField = None
    zField = None
    xLabel= None
    yLabel=None
    zLabel=None
    v3_6=None
    v4_0=None
    versionControl=""
    version36 = "3.6"
    version40 = "4.0"



    def __init__(self, master):
        #super().__init__()

        #self.master = master
        #self.grid()
        self.fillView(master)

    def fillView(self, master):

        frame = tk.Frame(master)


        self.erstellen = tk.Button(frame, text = "Erstellen", command=self.createData)
        self.g0Field = tk.Entry(frame)
        self.g1Field = tk.Entry(frame)
        self.xField = tk.Entry(frame)
        self.yField = tk.Entry(frame)
        self.zField = tk.Entry(frame)

        self.xLabel = tk.Label(frame, text="00.000")
        self.yLabel = tk.Label(frame, text="00.000")
        self.zLabel = tk.Label(frame, text="00.000")

        #self.v3_6 = tk.Checkbutton(frame, test="Version 3.6", variable=self.version36)

        self.g0Field.insert("end", "G0")
        self.g1Field.insert(0, "G1")
        self.xField.insert(0, "X")
        self.yField.insert(0, "Y")
        self.zField.insert(0, "Z")

        frame.grid(padx=5, pady=5)
        self.g0Field.grid(row=0, column=0)
        self.g1Field.grid(row=3, column=0)
        self.xField.grid(row=2, column=1)
        self.xLabel.grid(row=2, column=2)
        self.yField.grid(row=2, column=3)
        self.yLabel.grid(row=2, column=4)
        self.zField.grid(row=2, column=5)
        self.zLabel.grid(row=2, column=6)
        tk.Label(frame, text ="SPOS=(00.00)").grid(row=2, column=7)
        #self.v3_6.grid(row=3, column = 2)
        self.erstellen.grid(row=3, column=5)

    def createData(self):
        print("Funst")
        g0 = self.g0Field.get()
        g1 = self.g1Field.get()
        x = self.xField.get()
        y = self.yField.get()
        z = self.zField.get()

        Modifier(g0, g1, x, y, z)




root = tk.Tk()
Application(root)
#app = Application(root)
root.mainloop()