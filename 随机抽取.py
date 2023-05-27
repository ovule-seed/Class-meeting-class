import tkinter as tk
import random as rd
import time
root = tk.Tk()
root.title("随机抽取")
root.geometry('600x700')
root.resizable(False, False)
root.configure(bg='#FFFFFF')

n = 0 

def atmosphere(s):
    if s == 'group':
        ending = 8
    else:
        ending = 44
    for i in range(20):
        final_label.config(text=rd.randint(1,ending))
        final_label.update()
        time.sleep(0.05)


def rand(s):
    global n
    t = 0
    if s == 'group':
        if n == 0:
            atmosphere(s)
            final_label.config(text=1)
            n += 1
        else:
            atmosphere(s)
            final_label.config(text=rd.randint(1, 8))
    else:
        atmosphere(s)
        final_label.config(text=rd.randint(1, 44))

            

title_label = tk.Label(root, text='随机抽取', font=('微软雅黑', 20), bg='#FFFFFF')
title_label.pack(pady=50)

final_label = tk.Label(root, text='waiting……', font=(
    '微软雅黑', 50), foreground='white', background='red')
final_label.pack(pady=20)

group_btn = tk.Button(root, text="抽取小组", font=(
    '微软雅黑', 16), bg='#63B8FF', fg='#FFFFFF', command=lambda: rand('group'))
group_btn.place(relx=0.5, rely=0.5, anchor='center')
group_btn.bind("<Enter>", lambda event: group_btn.config(bg='#4D7DAA'))
group_btn.bind("<Leave>", lambda event: group_btn.config(bg='#63B8FF'))

person_btn = tk.Button(root, text="抽取个人", font=(
    '微软雅黑', 16), bg='#63B8FF', fg='#FFFFFF', command=lambda: rand('student'))
person_btn.place(relx=0.5, rely=0.6, anchor='center')
person_btn.bind("<Enter>", lambda event: person_btn.config(bg='#4D7DAA'))
person_btn.bind("<Leave>", lambda event: person_btn.config(bg='#63B8FF'))


root.mainloop()
