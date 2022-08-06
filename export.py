import mysql.connector
import tkinter as tk
import os
import json

connection = mysql.connector.connect(host="127.0.0.1",
                                    database="project",
                                    user="root",
                                    password="")

cursor=connection.cursor()
w = tk.Tk()

w.geometry("500x600")

label = tk.Label(
    text="Push",
    bg="white", 
    fg="black"
)
label.pack()


def send_inf():
    cursor.execute("select * from users")
    data=cursor.fetchall()
    with open('export.json', 'w') as f:
        json.dump(data, f)

frm_buttons = tk.Frame()
frm_buttons.pack(fill=tk.X, ipadx=5, ipady=5)

btn_submit = tk.Button(master=frm_buttons, text="Export", command=send_inf)
btn_submit.pack(padx=10, ipadx=10)

w.mainloop()
cursor.close()