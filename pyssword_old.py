import tkinter as tk
from tkinter import scrolledtext
from hashlib import sha512

master_password = 'foo'

# Creating tkinter window
win = tk.Tk()
win.title("PSWD")
win['background']='#aaffdd'
win.resizable(True, True)

def pswd():
    global pss
    pswd = pswd_area.get('1.0', tk.END)[:-1]
    site = input_area.get('1.0', tk.END)[:-1]
    enc = sha512()
    enc.update(bytes(pswd + site, 'utf-8'))
    pss = enc.hexdigest()[::8] + '@A'
    display_area.delete('1.0', tk.END)
    display_area.insert(tk.INSERT, pss)

def ctoc():
    try: win.clipboard_clear()
    except tk.TclError: print('Clipboard Empty')
    win.clipboard_append(pss)

# Title Label
tk.Label(win,
         text = "Password Manager",
         font = ("FixedSys", 10),
         background = 'white',
         foreground = "black").grid(column = 0, row = 0)

input_area = scrolledtext.ScrolledText(win, width = 20, height = 2)
input_area.grid(row = 1, column=0, padx = 10, pady = 10)

display_area = scrolledtext.ScrolledText(win, width = 20, height = 2)
display_area.grid(row = 2, column=0, padx = 10, pady = 10)

pswd_area = scrolledtext.ScrolledText(win, width = 20, height = 2)
pswd_area.grid(row = 3, column=0, padx = 10, pady = 10)
pswd_area.insert(tk.INSERT, master_password)

button1 = tk.Button(win, text="OK", command=pswd)
button1.grid(row=1, column=1, padx = 10, pady = 10)
button1['background']='#33ff33'

C2CB = tk.Button(win, text = "Copy to clipboard", command = ctoc)
C2CB.grid(row=2, column=1, padx = 10, pady = 10)
C2CB['background']='#33ff77'

input_area.delete('1.0', tk.END)
input_area.insert(tk.INSERT, '')
win.mainloop()
