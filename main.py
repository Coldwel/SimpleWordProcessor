import tkinter as tk
from tkinter import filedialog, messagebox
from tkinter.font import families

class WordProcessor:
    def __init__(self, master):
        self.master = master
        self.master.title("Word Processor")

        # Set up the menu bar
        menubar = tk.Menu(self.master)
        filemenu = tk.Menu(menubar, tearoff=0)
        filemenu.add_command(label="New", command=self.new_file)
        filemenu.add_command(label="Open", command=self.open_file)
        filemenu.add_command(label="Save", command=self.save_file)
        filemenu.add_command(label="Save As", command=self.save_file_as)
        filemenu.add_separator()
        filemenu.add_command(label="Exit", command=self.quit_program)
        menubar.add_cascade(label="File", menu=filemenu)

        fontmenu = tk.Menu(menubar, tearoff=1)
        self.font_family = tk.StringVar()
        self.font_family.set("Arial")
        for family in sorted(families()):
            fontmenu.add_radiobutton(label=family, variable=self.font_family, command=self.change_font_family)
        menubar.add_cascade(label="Font", menu=fontmenu)
        self.master.config(menu=menubar)

        # Set up the text area
        self.textarea = tk.Text(self.master, undo=True)
        self.textarea.pack(fill=tk.BOTH, expand=True)

    def new_file(self):
        self.textarea.delete('1.0', tk.END)
        self.master.title("Word Processor")

    def open_file(self):
        filepath = filedialog.askopenfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
        if filepath:
            try:
                with open(filepath, "r") as file:
                    self.textarea.delete('1.0', tk.END)
                    self.textarea.insert(tk.END, file.read())
                self.master.title("Word Processor - " + filepath)
            except Exception as e:
                messagebox.showerror("Error", str(e))

    def save_file(self):
        try:
            with open(self.filepath, "w") as file:
                file.write(self.textarea.get('1.0', tk.END))
        except:
            self.save_file_as()

    def save_file_as(self):
        filepath = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
        if filepath:
            self.filepath = filepath
            self.save_file()
            self.master.title("Word Processor - " + filepath)

    def quit_program(self):
        if messagebox.askokcancel("Quit", "Are you sure you want to quit?"):
            self.master.destroy()

    def change_font_family(self):
        font_family = self.font_family.get()
        current_font = self.textarea['font']
        font_size = ''.join(filter(str.isdigit, current_font))
        if font_size == '':
            font_size = '12'
        self.textarea.configure(font=(font_family, int(font_size)))


root = tk.Tk()
app = WordProcessor(root)
root.mainloop()
