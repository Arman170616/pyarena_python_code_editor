from tkinter import *
from tkinter.filedialog import asksaveasfilename, askopenfilename

compiler = Tk()
compiler.title('pyarena')
file_path = ''


def set_file_path(path):
    global file_path
    file_path = path

def open_file():
    path = askopenfilename(filetypes=[('python files', '*.py')])
    with open(path, 'r') as file:
        code = file.read()
        editor.delete('1.0', END)
        editor.insert('1.0', code)
        set_file_path(path)
        


def save_as():
    if file_path == '':

        path = asksaveasfilename(filetypes=[('python files', '*.py')])
    else:
        path = file_path    
    with open(path, 'w') as file:
        code = editor.get('1.0', END)
        file.write(code)
        set_file_path(path)

def run():
    code = editor.get('1.0', END)
    exec(code)



menu_bar = Menu(compiler)

file_menu = Menu(menu_bar, tearoff=0)
file_menu.add_command(label='Open', command=open_file)
file_menu.add_command(label='Save', command=save_as)
file_menu.add_command(label='Save As', command=save_as)
file_menu.add_command(label='Exit', command=exit)
menu_bar.add_cascade(label='File', menu = file_menu)  #file

run_bar = Menu(menu_bar, tearoff=0)
run_bar.add_command(label='Run', command=run)
menu_bar.add_cascade(label='Run', menu = run_bar)  #run




compiler.config(menu=menu_bar)

editor = Text()
editor.pack()

compiler.mainloop()
