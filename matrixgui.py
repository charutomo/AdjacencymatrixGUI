# -*- coding: utf-8 -*-
"""
Created on Thu Dec 22 17:42:11 2022

@author: Charissa
"""

import numpy as np
import tkinter as tk   # PEP8: `import *` is not preferred

# --- functions ---

def get_data():
    for r, row in enumerate(all_entries):
        for c, entry in enumerate(row):
            text = entry.get()
            demand[r,c] = float(text)  
    print(demand)
    window2.destroy()
    
# --- main ---

window = tk.Tk()
num =0

def getvert():
    global num
    num = entry.get()
    global rows
    global cols
    rows = int(num)
    cols = int(num)
    window.destroy()
    
label = tk.Label(text = "Please enter the number of vertices:")
label.grid()
entry = tk.Entry()
entry.grid()
button =  tk.Button(window, text='Enter', command=getvert)
button.grid()
window.mainloop() 

window2 = tk.Tk()
demand = np.zeros((rows, cols))

all_entries = []
for r in range(rows):
    entries_row = []
    for c in range(cols):
        e = tk.Entry(window2, width=5)  # 5 chars
        e.insert('end', 0)
        e.grid(row=r, column=c)
        entries_row.append(e)
    all_entries.append(entries_row)
    
b = tk.Button(window2, text='GET DATA', command=get_data)
b.grid(row=rows+1, column=0, columnspan=cols)
window2.mainloop() 



     