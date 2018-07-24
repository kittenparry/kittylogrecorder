import tkinter as tk
#from tkinter import ttk
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
        self.strings()
        self.add_elements()
        self.set_time()
    def add_elements(self):
        self.label_dir = tk.Label(self.row3, text=self.str_dir)
        self.entry_dir = tk.Entry(self.row3, width=10)
        self.entry_dir.insert(tk.END, self.str_dir_path)
        self.entry_dir.configure(state='readonly')
        self.label_fname = tk.Label(self.row3, text=self.str_fname)
        self.entry_fname = tk.Entry(self.row3, width=10)
        self.entry_fname.insert(tk.END, self.str_fname_name)
        self.entry_fname.configure(state='readonly')
        #self.label3 = tk.Label(self.row3, text="Entry:")
        #OLD ENTRY
        #self.text3 = tk.Entry(self.row2, width=25)
        #self.text3.bind("<Return>", self.logEntry2)
        self.text_entry = tk.Text(self.row1, width=30, height=5, wrap='word')
        self.text_entry.bind("<Return>", self.log_entry_event)
        self.scrolly = tk.Scrollbar(self.row1, orient='vertical', command=self.text_entry.yview)
        self.text_entry.configure(yscrollcommand=self.scrolly.set)
        #TODO: fix the cursor leaving the whole words behind using ctrl + right arrow to navigate
        #self.text3.configure(..)
        #MONOSPACE TEST
        #self.text3.configure(style="Courier.TLabel")
        self.button_enter = tk.Button(self.row3, text=self.str_button_enter, command=self.log_entry)
        self.label_time = tk.Label(self.row2, text="")
        self.label_message = tk.Label(self.row2, text="")
        self.els = [self.label_dir, self.entry_dir, self.label_fname, self.entry_fname,
                    self.text_entry, self.button_enter]
        self.els2 = [self.label_time, self.label_message]
        for e in self.els:
            e.pack(side="left", padx=4, pady=5)
        for e in self.els2:
            e.pack(side="left")
        self.scrolly.pack(side="left", fill="y")
        self.text_entry.focus()
    def log_entry_event(self, event):
        self.log_entry()
        return 'break'
    def log_entry(self):
        try:
            path = str(self.entry_dir.get())
            file = str(self.entry_fname.get())
            if file[len(file)-4:len(file)] != '.txt':
                file += ".txt"
            if path[len(path)-1:len(path)] == '\\' or path[len(path)-1:len(path)] == '/':
                wp = path + file
            else:
                wp = path + "\\" + file
            #TODO C:\ folder fix
            if wp[0:3] == "C:\\" and file == wp[3:len(wp)]:
                self.label_message.config(text=self.str_err_cpath)
            else:
                fw = open(wp, 'a')
                #msg = self.getTime() + "| " + str(self.text3.get()) + "\n"
                msg = self.get_time() + "| " + str(self.text_entry.get('1.0', 'end'))# + "\n"
                fw.write(msg)
                if self.x > 1:
                    self.label_message.config(text=self.str_logged1)
                    self.x = 1
                else:
                    self.label_message.config(text=self.str_logged2)
                    self.x += 1
                fw.close()
                #self.text3.delete(0,'end')
                self.text_entry.delete('1.0', 'end')
        except IOError:
            self.label_message.config(text=self.str_err_io)
    def get_time(self):
        return time.strftime("%Y.%m.%d %H:%M:%S")
    def set_time(self):
        self.label_time.config(text=self.get_time())
        self.after(333, self.set_time)
    #FOCUS TEST
    #def focus_text3(self, event):
    #    if event.widget == root:
    #        self.text3.focus_set()
    def strings(self):
        self.str_dir = "Dir:"
        self.str_dir_path = "Other"
        self.str_fname = "Name:"
        self.str_fname_name = "myLogs"
        self.str_button_enter = "Enter"
        self.str_err_cpath = "|| Error. Can't write to C:\ alone.\n|| Put a folder or change the drive."
        self.str_logged1 = "|| Entry logged.."
        self.str_logged2 = "|| Entry logged."
        self.str_err_io = "|| Error. Directory doesn't exist."

if __name__ == '__main__':
    root = tk.Tk()
    root.title("Log Recorder")
    #edit below for window spawn position
    root.geometry("275x165+100+0")
    app = Gui(master=root)
    #FOCUS TEST
    #root.bind("<FocusIn>", Gui.focus_text3)
    #MONOSPACE TEST
    #style = ttk.Style()
    #style.configure("Courier.TButton", font=("Courier", 16))
    app.mainloop()
