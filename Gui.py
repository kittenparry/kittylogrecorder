from tkinter import *
from threading import *
from time import strftime, sleep

class Gui(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.x = 1
        self.row1 = Frame(master)
        self.row2 = Frame(master)
        self.row3 = Frame(master)
        self.row1.grid(row=0, column=0)
        self.row2.grid(row=1, column=0)
        self.row3.grid(row=2, column=0)
        self.addElements()
        self.setTime()
        #self.t = Timer()
        #self.t.start()
    def addElements(self):
        self.label1 = Label(self.row1, text="Directory:")
        self.text1 = Entry(self.row1, width=50)
        self.text1.insert(END, 'C:\\')
        self.label2 = Label(self.row2, text="Filename:")
        self.text2 = Entry(self.row2, width=10)
        self.text2.insert(END, 'logs')
        self.label3 = Label(self.row2, text="Entry:")
        self.text3 = Entry(self.row2, width=25)
        self.enterButton = Button(self.row2, text="Enter", command=self.logEntry)
        self.time = Label(self.row3, text="[time]")
        self.message = Label(self.row3, text="[message]")
        self.label1.pack(side="left")
        self.text1.pack(side="left")
        self.label2.pack(side="left")
        self.text2.pack(side="left")
        self.label3.pack(side="left")
        self.text3.pack(side="left")
        self.enterButton.pack(side="left")
        self.time.pack(side="left")
        self.message.pack(side="left")
    def logEntry(self):
        try:
            path = str(self.text1.get())
            file = str(self.text2.get())
            if file[len(file)-4:len(file)] != '.txt':
                file += ".txt"
            if path[len(path)-1:len(path)] == '\\' or path[len(path)-1:len(path)] == '/':
                wp = path + file
            else:
                wp = path + "\\" + file
            #TODO C:\ folder fix
            if wp[0:3] == "C:\\" and file == wp[3:len(wp)]:
                self.message.config(text="|| Error. Can't write to C:\ alone.\n|| Put a folder or change the drive.")
            else:
                fw = open(wp, 'a')
                msg = self.getTime() + "| " + str(self.text3.get()) + "\n"
                fw.write(msg)
                if self.x > 1:
                    self.message.config(text="|| Entry logged..")
                    self.x = 1
                else:
                    self.message.config(text="|| Entry logged.")
                    self.x += 1
                fw.close()
                self.text3.delete(0,'end')
        except IOError:
            self.message.config(text="|| Error. Directory doesn't exist.")
    def getTime(self):
        return strftime("%Y.%m.%d %H:%M:%S")
    def setTime(self):
        self.time.config(text=self.getTime())

#TODO timer
class Timer(Thread):
    def run(self):
        for _ in range(999999999999):
            Gui.setTime(Gui)
            sleep(0.5)
root = Tk()
root.title("Log Recorder")
app = Gui(master=root)
root.geometry("370x85+0+100")
app.mainloop()