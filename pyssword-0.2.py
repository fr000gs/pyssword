import tkinter as tk
from tkinter import scrolledtext
from hashlib import sha512
from tkinter import Label

master_password = 'foo'
separator = '@'

# Creating tkinter window
win = tk.Tk()
win.title("PSWD")
win['background']='#aaffdd'
win.resizable(True, True)

def pswd():
    global pss
    pswd = master_pswd_area.get('1.0', tk.END)[:-1]
    site = username_area.get('1.0', tk.END)[:-1] + separator + website_area.get('1.0' , tk.END)[:-1]
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
label_title = Label(win,
         text = "Password Manager",
         font = ("FixedSys", 10),
         background = 'white',
         foreground = "black")
label_title.grid(column = 1, row = 0)

label_area_0 = Label(win, text='UserName')
label_area_0.grid(row = 1, column = 0)

label_area_1 = Label(win, text='WebSite')
label_area_1.grid(row = 2, column = 0)

label_area_2 = Label(win, text='MasterPassword')
label_area_2.grid(row = 3, column = 0)

label_area_3 = Label(win, text='PassWord')
label_area_3.grid(row = 4, column = 0)

username_area = scrolledtext.ScrolledText(win, width = 20, height = 2)
username_area.grid(row = 1, column=1, padx = 10, pady = 10)

website_area = scrolledtext.ScrolledText(win, width = 20, height = 2)
website_area.grid(row = 2, column=1, padx = 10, pady = 10)

master_pswd_area = scrolledtext.ScrolledText(win, width = 20, height = 2)
master_pswd_area.grid(row = 3, column=1, padx = 10, pady = 10)
master_pswd_area.insert(tk.INSERT, master_password)

display_area = scrolledtext.ScrolledText(win, width = 20, height = 2)
display_area.grid(row = 4, column=1, padx = 10, pady = 10)

button_generate = tk.Button(win, text="OK", command=pswd)
button_generate.grid(row=1, column=2, padx = 10, pady = 10)
button_generate['background']='#33ff33'

C2CB = tk.Button(win, text = "Copy to clipboard", command = ctoc)
C2CB.grid(row=2, column=2, padx = 10, pady = 10)
C2CB['background']='#33ff77'

win.mainloop()
