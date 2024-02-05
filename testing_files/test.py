import tkinter as tk

class Window1:
    def __init__(self, master):
        self.master = master
        self.master.geometry("1366x768")
        
        self.frame = tk.Frame(self.master)
        self.button1 = tk.Button(self.frame, text = 'Go to Window 2', width = 25, command = self.new_window)
        self.button1.pack()
        self.frame.pack()

    def new_window(self):
        self.master.withdraw()
        self.newWindow = tk.Toplevel(self.master)
        Window2(self.newWindow)

class Window2:
    def __init__(self, master):
        self.master = master
        self.master.geometry("1366x768")
        self.frame = tk.Frame(self.master)
        self.quitButton = tk.Button(self.frame, text = 'Go to Window 3', width = 25, command = self.close_windows)
        self.quitButton.pack()
        self.frame.pack()

    def close_windows(self):
        self.master.withdraw()
        self.newWindow = tk.Toplevel(self.master)
        Window3(self.master, self.newWindow)

class Window3:
    def __init__(self, master, prev_window):
        self.master = master
        self.master.geometry("1366x768")
        self.prev_window = prev_window
        self.frame = tk.Frame(self.prev_window)
        self.quitButton = tk.Button(self.frame, text = 'Go to Window 2', width = 25, command = self.close_windows)
        self.quitButton.pack()
        self.frame.pack()

    def close_windows(self):
        self.prev_window.destroy()
        self.master.deiconify()

def main(): 
    root = tk.Tk()
    app = Window1(root)
    root.mainloop()

if __name__ == '__main__':
    main()
