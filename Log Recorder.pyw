import tkinter as tk
import time

class Gui(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.x = 1
        self.row1 = tk.Frame(master)
        self.row2 = tk.Frame(master)
        self.row1.grid(row=0, column=0)
        self.row2.grid(row=1, column=0, sticky="ew", padx=(10,0))
        self.add_elements()
        self.set_time()
    def add_elements(self):
        self.label_dir = tk.Label(self.row1, text=strings("label_dir"), state='disabled')
        self.entry_dir = tk.Entry(self.row1, width=10)
        self.entry_dir.insert(tk.END, strings("path_dir"))
        self.entry_dir.configure(state='disabled')
        self.label_fname = tk.Label(self.row1, text=strings("label_fname"), state='disabled')
        self.entry_fname = tk.Entry(self.row1, width=10)
        self.entry_fname.insert(tk.END, strings("name_fname"))
        self.entry_fname.configure(state='disabled')
        self.text_entry = tk.Text(self.row2, width=50, height=4, wrap='word')
        self.text_entry.bind("<Return>", self.log_entry_event)
        self.scrolly = tk.Scrollbar(self.row2, orient='vertical', command=self.text_entry.yview)
        self.text_entry.configure(yscrollcommand=self.scrolly.set)
        self.button_enter = tk.Button(self.row1, text=strings("button_enter"), command=self.log_entry)
        self.label_time = tk.Label(self.row1, text="")
        self.label_message = tk.Label(self.row1, text="")
        self.els = [self.label_time, self.label_message, self.label_dir, self.entry_dir,
                    self.label_fname, self.entry_fname, self.text_entry, self.button_enter]
        for e in self.els:
            e.pack(side="left", pady=2, padx=1)
        self.scrolly.pack(side="left", fill="y")
        self.text_entry.focus()
    def log_entry_event(self, event):
        self.log_entry()
        return 'break'
    #TODO:
    #if not os.path.exists(path):
    #   os.makedirs(path)
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
                self.label_message.config(text=strings("err_c_path"))
            else:
                fw = open(wp, 'a')
                msg = self.get_time() + "| " + str(self.text_entry.get('1.0', 'end'))
                fw.write(msg)
                if self.x > 1:
                    self.label_message.config(text=strings("logged1"))
                    self.x = 1
                else:
                    self.label_message.config(text=strings("logged2"))
                    self.x += 1
                fw.close()
                self.text_entry.delete('1.0', 'end')
        except IOError:
            self.label_message.config(text=strings("err_io"))
    def get_time(self):
        return time.strftime("%Y.%m.%d %H:%M:%S")
    def set_time(self):
        self.label_time.config(text=self.get_time())
        self.after(333, self.set_time)

def strings(s):
    str = {
        "label_dir": "Dir:",
        "path_dir": "Other",
        "label_fname": "Name:",
        "name_fname": "myLogs",
        "button_enter": "Enter",
        "err_c_path": "|| Error. Can't write to C:\ alone.\n|| Put a folder or change the drive.",
        "err_io": "|| Error. Directory doesn't exist.",
        "logged1": "|| Logged!!",
        "logged2": "|| Logged..",
    }
    return str.get(s)

if __name__ == '__main__':
    root = tk.Tk()
    root.title("Log Recorder")
    root.geometry("435x115+94+0")
    app = Gui(master=root)
    app.mainloop()
