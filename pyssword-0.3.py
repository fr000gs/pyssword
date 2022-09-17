import tkinter as tk
from tkinter import scrolledtext
from hashlib import sha512
from tkinter import Label
from tkinter import Entry
from tkinter import Checkbutton 
from tkinter import IntVar

master_password = 'foo'

# Creating tkinter window
win = tk.Tk()
win.title("PSWD")
win['background']='#aaffdd'
win.resizable(True, True)

def pswd():
    global pss
    pswd = master_pswd_area.get()
    site = username_area.get() + website_area.get()
    enc = sha512()
    enc.update(bytes(pswd + site, 'utf-8'))
    pss = enc.hexdigest()[::8] + '@A'
    display_area.delete('0', tk.END)
    display_area.insert(tk.INSERT, pss)
    show_toggle()

def ctoc():
    try: win.clipboard_clear()
    except tk.TclError: print('Clipboard Empty')
    win.clipboard_append(pss)

def show_toggle():
    if checkbutton_1_value.get():
        username_area.config(show='')
    else:
        username_area.config(show='*')
    if checkbutton_2_value.get():
        website_area.config(show='')
    else:
        website_area.config(show='*')
    if checkbutton_3_value.get():
        master_pswd_area.config(show='')
    else:
        master_pswd_area.config(show='*')
    if checkbutton_4_value.get():
        display_area.config(show='')
    else:
        display_area.config(show='*')

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
label_area_1.grid(row = 3, column = 0)

label_area_2 = Label(win, text='MasterPassword')
label_area_2.grid(row = 5, column = 0)

label_area_3 = Label(win, text='PassWord')
label_area_3.grid(row = 7, column = 0)

label_area_4 = Label(win, text='Show')
label_area_4.grid(row = 0, column = 3)

checkbutton_1_value = IntVar()
checkbutton_1 = Checkbutton(win, variable = checkbutton_1_value)
checkbutton_1.select()
checkbutton_1.grid(row = 1, column = 3)

checkbutton_2_value = IntVar()
checkbutton_2 = Checkbutton(win, variable = checkbutton_2_value)
checkbutton_2.select()
checkbutton_2.grid(row = 3, column = 3)

checkbutton_3_value = IntVar()
checkbutton_3 = Checkbutton(win, variable = checkbutton_3_value)
checkbutton_3.grid(row = 5, column = 3)

checkbutton_4_value = IntVar()
checkbutton_4 = Checkbutton(win, variable = checkbutton_4_value)
checkbutton_4.grid(row = 7, column = 3)

username_area = tk.Entry(win)
username_area.grid(row = 1, column=1, pady = 10)
username_area_scroll = tk.Scrollbar(orient='horizontal', width = 10, command = username_area.xview)
username_area.configure(xscrollcommand=username_area_scroll.set)
username_area_scroll.grid(row=2, column=1, sticky='ew', padx = 0)

website_area = tk.Entry(win)
website_area.grid(row = 3, column=1, pady = 10)
website_area_scroll = tk.Scrollbar(orient='horizontal', width = 10, command = website_area.xview)
website_area.configure(xscrollcommand=website_area_scroll.set)
website_area_scroll.grid(row=4, column=1, sticky='ew', padx = 0)

master_pswd_area = tk.Entry(win)
master_pswd_area.grid(row =5, column=1, pady = 10)
master_pswd_area_scroll = tk.Scrollbar(orient='horizontal', width = 10, command = master_pswd_area.xview)
master_pswd_area.configure(xscrollcommand=master_pswd_area_scroll.set)
master_pswd_area_scroll.grid(row=6, column=1, sticky='ew', padx = 0)
master_pswd_area.insert(tk.INSERT, master_password)

display_area = Entry(win)
display_area.grid(row = 7, column=1, padx = 10, pady = 10)

button_generate = tk.Button(win, text="OK", command=pswd)
button_generate.grid(row=1, column=4, padx = 10, pady = 10)
button_generate['background']='#33ff33'

C2CB = tk.Button(win, text = "Copy to clipboard", command = ctoc)
C2CB.grid(row=3, column=4, padx = 10, pady = 10)
C2CB['background']='#33ff77'

show_button = tk.Button(win, text = "Show/Hide", command = show_toggle)
show_button.grid(row=5, column=4, padx = 10, pady = 10)
show_button['background']='#33ff33'

show_toggle()
win.mainloop()
