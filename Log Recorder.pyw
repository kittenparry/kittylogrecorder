import tkinter as tk
import time
import platform

class Gui(tk.Frame):
	def __init__(self, master=None):
		tk.Frame.__init__(self, master)
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
		# self.entry_dir.configure(state='disabled')
		self.label_fname = tk.Label(self.row1, text=strings("label_fname"), state='disabled')
		self.entry_fname = tk.Entry(self.row1, width=10)
		self.entry_fname.insert(tk.END, strings("name_fname"))
		# self.entry_fname.configure(state='disabled')
		self.text_entry = tk.Text(self.row2, width=50, height=4, wrap='word')
		self.text_entry.bind("<Return>", self.log_entry_event)
		self.scrolly = tk.Scrollbar(self.row2, orient='vertical', command=self.text_entry.yview)
		self.text_entry.configure(yscrollcommand=self.scrolly.set)
		self.button_enter = tk.Button(self.row1, text=strings("button_enter"), command=self.log_entry)
		self.label_time = tk.Label(self.row1, text="")
		self.label_message = tk.Label(self.row1, text="")
		self.els = [self.label_time, self.label_message, self.text_entry, self.button_enter]
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
				wp = path + "/" + file

			fw = open(wp, 'a')
			msg = self.get_time() + "| " + str(self.text_entry.get('1.0', 'end'))
			fw.write(msg)
			fw.close()
			self.text_entry.delete('1.0', 'end')
		except IOError:
			self.label_message.config(text=strings("err_io"))
	def get_time(self):
		return time.strftime("%Y.%m.%d %H:%M:%S")
	def set_time(self):
		self.label_time.config(text=self.get_time())
		self.after(333, self.set_time)

dict_strings = {
	"title": "Log Recorder",
	"label_dir": "Dir:",
	"path_dir": "Other",
	"label_fname": "Name:",
	"name_fname": "myLogs",
	"button_enter": "Enter",
	"err_c_path": "|| Error. Can't write to C:\ alone.\n|| Put a folder or change the drive.",
	"err_io": "|| Error. Directory doesn't exist.",
}
def strings(s):
	return dict_strings.get(s)

def get_geometry():
	os = platform.system()
	if os == 'Windows':
		return "435x115+94+0"
	# elif os == 'Linux', might as well use else to include OS X
	else:
		screen_width = 1920
		program_width = 390
		x_position = (screen_width - program_width) / 2
		return ("%dx115+%d+30" % (program_width, x_position))


if __name__ == '__main__':
	root = tk.Tk()
	root.tk.call('tk', 'scaling', 1.3)
	root.title(strings("title"))
	root.geometry(get_geometry())
	app = Gui(master=root)
	app.mainloop()
