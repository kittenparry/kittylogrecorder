import tkinter as tk
import time

class Gui(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.x = 1
        self.row1 = tk.Frame(master)
        self.row2 = tk.Frame(master)
        self.row3 = tk.Frame(master)
        self.row1.grid(row=0, column=0)
        self.row2.grid(row=1, column=0)
        self.row3.grid(row=2, column=0)
        self.addElements()
        self.setTime()
    def addElements(self):
        self.label1 = tk.Label(self.row1, text="Directory:")
        self.text1 = tk.Entry(self.row1, width=50)
        self.text1.insert(tk.END, 'C:\\Users\\Public')
        self.text1.configure(state='readonly')
        self.label2 = tk.Label(self.row2, text="Filename:")
        self.text2 = tk.Entry(self.row2, width=10)
        self.text2.insert(tk.END, 'someFile')
        self.text2.configure(state='readonly')
        self.label3 = tk.Label(self.row2, text="Entry:")
        self.text3 = tk.Entry(self.row2, width=25)
        self.text3.bind("<Return>", self.logEntry2)
        #TODO: fix the cursor leaving the whole words behind using ctrl + right arrow to navigate
        #self.text3.configure(..)
        self.enterButton = tk.Button(self.row2, text="Enter", command=self.logEntry)
        self.time = tk.Label(self.row3, text="[time]")
        self.message = tk.Label(self.row3, text="")
        self.label1.pack(side="left")
        self.text1.pack(side="left")
        self.label2.pack(side="left")
        self.text2.pack(side="left")
        self.label3.pack(side="left")
        self.text3.pack(side="left")
        self.text3.focus()
        self.enterButton.pack(side="left")
        self.time.pack(side="left")
        self.message.pack(side="left")
    def logEntry2(self, event):
        self.logEntry()
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
        return time.strftime("%Y.%m.%d %H:%M:%S")
    def setTime(self):
        self.time.config(text=self.getTime())
        self.after(333, self.setTime)

if __name__ == '__main__':
    root = tk.Tk()
    root.title("Log Recorder")
    #edit below for window spawn position
    root.geometry("370x75+100+0")
    app = Gui(master=root)
    app.mainloop()
