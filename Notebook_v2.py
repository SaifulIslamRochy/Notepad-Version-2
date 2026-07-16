# -*- coding: utf-8 -*-
"""
Created on Sat Jan  2 11:45:15 2021

@author: Rochy
"""
import tkinter as tk
from tkinter import *
import pyttsx3
import qrcode
from PIL import Image, ImageTk
from tkinter import messagebox 
from tkinter.filedialog import asksaveasfilename
import os
from tkinter import ttk
from ttkthemes import ThemedTk

splash_root=Tk()
splash_width=413
splash_height=214
screen_width=splash_root.winfo_screenwidth()
screen_height=splash_root.winfo_screenheight()
x=(screen_width/2)-(splash_width/2)
y=(screen_height/2)-(splash_height/2)
splash_root.geometry(f'{splash_width}x{splash_height}+{int(x)}+{int(y)}')

splash_root.overrideredirect(True)

splash_root.config(bg="#1982BE")
splashlabel1=ttk.Label(splash_root, text="Notebook", font="montserrat 30 ", background="#1982BE",foreground='#FFFFFD')
splashlabel1.place(x=110,y=85)
splashlabel2=ttk.Label(splash_root, text="Version..2v", font="montserrat 10 ", background="#1982BE",foreground='#FFFFFD')
splashlabel2.place(x=175,y=130)

def notebook():
    splash_root.destroy()
    notebook_root=Tk()
    notebook_root_width=800
    notebook_root_height=465
    screen_width=notebook_root.winfo_screenwidth()
    screen_height=notebook_root.winfo_screenheight()
    x=(screen_width/2)-(notebook_root_width/2)
    y=(screen_height/2)-(notebook_root_height/2)
    notebook_root.geometry(f'{notebook_root_width}x{notebook_root_height}+{int(x)}+{int(y)}')
    notebook_root.iconbitmap('notepad.ico')
    notebook_root.title(f'Notepad')
    
        
    def newfile():
        global file
        notebook_root.title("Untitled-notepad")
        file= None
        textbox.delete(1.0, END)
        
    def openfile():
        global file
        file= askopenfilename(defaultextension=".txt", filetypes=[("All Files", "*.*"),("Text Document", "*.txt")])
        if file=="":
            file=None
        else:
            notebook_root.title(os.path.basename(file)+" -notepad")
            textbox.delete(1.0, END)
            f=open(file, "r")
            textbox.insert(1.0, f.read())
            f.close()
        
    def savefile():
        global file
        if file==None:
            file= asksaveasfilename(initialfile="Untitled.txt", defaultextension=".txt", filetypes=[("All Files", "*.*"),("Text Document", "*.txt")])
        
            if file=="":
                file=None
            else:
                f=open(file, "w")
                f.write(textbox.get(1.0, END))
                f.close()
                notebook_root.title(os.path.basename(file)+" -notepad")
        else:
            f=open(file, "w")
            f.write(textbox.get(1.0, END))
            f.close()
            
    def about():
        messagebox.showinfo("About",'''Smart Notepad
                            \nProject: Notepad\nDeveloper: Saiful Islam Rochy\nVersion: 2v\nDeveloped year: 2021(1v)\nUpdated: 2023(2v)''')
                    
    def close():
        notebook_root.destroy()
        
    def cut():
        textbox.event_generate(("<<Cut>>"))
        
    def copy():
        textbox.event_generate(("<<Copy>>"))
        
    def paste():
        textbox.event_generate(("<<Paste>>"))
    
        
    def speak_in_male_voice():
        if len(textbox.get(1.0, END))<2:
            speech= pyttsx3.init()
            speech.setProperty("rate",150)
            speech.say("Please insert some text to convert it into speak. Thank you.")
            speech.runAndWait()
        else:
            speech= pyttsx3.init()
            speech.setProperty("rate",150)
            speech.say(textbox.get(1.0, END))
            speech.runAndWait()
            
    def speak_in_female_voice():
        if len(textbox.get(1.0, END))<2:
            speech= pyttsx3.init()
            voice=speech.getProperty('voices')
            speech.setProperty("rate",150)
            speech.setProperty('voice', voice[1].id)
            speech.say("Please insert some text to convert it into speak. Thank you.")
            speech.runAndWait()
        else:
            speech= pyttsx3.init()
            voice=speech.getProperty('voices')
            speech.setProperty("rate",150)
            speech.setProperty('voice', voice[1].id)
            speech.say(textbox.get(1.0, END))
            speech.runAndWait()
    
    
    def make_a_list():
        text=textbox.get(1.0, END)
        text=text.split()
        count=0 
        textbox.delete(1.0, END)
        for i in text:
            count=count+1
            list_created=f"{count}. {i.title()}\n"
            textbox.insert(INSERT, list_created)
            


            
    def Remove():
        REMOVE=ThemedTk(theme='radiance')
        REMOVE_width=350
        REMOVE_height=150
        screen_width=REMOVE.winfo_screenwidth()
        screen_height=REMOVE.winfo_screenheight()
        x=(screen_width/2)-(REMOVE_width/2)
        y=(screen_height/2)-(REMOVE_height/2)
        REMOVE.geometry(f'{REMOVE_width}x{REMOVE_height}+{int(x)}+{int(y)}')
        REMOVE.iconbitmap('remove.ico')
        REMOVE.title("REMOVE")
        REMOVE.resizable(0,0)
        remove_entry=ttk.Entry(REMOVE, width=30)
        remove_entry.place(x=85,y=80)
        remove_label=ttk.Label(REMOVE, text='Type a single word', font="montserrat 8", background='#F0F0F0')
        remove_label.place(x=85, y=55)
        def remove_text():
            c=textbox.get(1.0, END).split()
            text=remove_entry.get()
            d=[]
            Upper=text.upper()
            Lower=text.lower()
            Title=text.title()
            
            for i in c:
                d.append(i)
                if Upper in i:
                    d.remove(Upper)
                elif Lower in i:
                    d.remove(Lower)
                elif Title in i:
                    d.remove(Title)
                    
            value_2=' '.join(d)
            textbox.delete(1.0, END)
            for i in value_2:
                textbox.insert(INSERT, i)
            
        
        remove_button=ttk.Button(REMOVE, text="Remove", width=7, command=remove_text)
        remove_button.place(x=130,y=105)
        
    
    def Remove_Case_Sensitive():
        REMOVE_CASE_SENSITIVE=ThemedTk(theme='radiance')
        REMOVE_CASE_SENSITIVE_width=350
        REMOVE_CASE_SENSITIVE_height=150
        screen_width=REMOVE_CASE_SENSITIVE.winfo_screenwidth()
        screen_height=REMOVE_CASE_SENSITIVE.winfo_screenheight()
        x=(screen_width/2)-(REMOVE_CASE_SENSITIVE_width/2)
        y=(screen_height/2)-(REMOVE_CASE_SENSITIVE_height/2)
        REMOVE_CASE_SENSITIVE.geometry(f'{REMOVE_CASE_SENSITIVE_width}x{REMOVE_CASE_SENSITIVE_height}+{int(x)}+{int(y)}')
        REMOVE_CASE_SENSITIVE.iconbitmap('remove.ico')
        REMOVE_CASE_SENSITIVE.title("REMOVE_CASE_SENSITIVE")
        REMOVE_CASE_SENSITIVE.resizable(0,0)
        remove_case_sensitive_entry=ttk.Entry(REMOVE_CASE_SENSITIVE, width=30)
        remove_case_sensitive_entry.place(x=85,y=80)
        remove_case_sensitive_label=ttk.Label(REMOVE_CASE_SENSITIVE, text='Type a single word', font="montserrat 8", background='#F0F0F0')
        remove_case_sensitive_label.place(x=85, y=55)

        
        def remove_case_sensitive_text():    
            c=textbox.get(1.0, END).split()
            text=remove_case_sensitive_entry.get()
            for i in c:
                if i==text:
                    c.remove(text)
            value_1=' '.join(c)
            textbox.delete(1.0, END)
            for i in value_1:
                textbox.insert(INSERT, i)
            
        remove_case_sensitive_button=ttk.Button(REMOVE_CASE_SENSITIVE, text="Remove", width=7, command=remove_case_sensitive_text)
        remove_case_sensitive_button.place(x=130,y=105)
        
        
        
        
    
    def Replace_Case_Sensitive():
        REPLACE_CASE_SENSITIVE=ThemedTk(theme='radiance')
        REPLACE_CASE_SENSITIVE_width=350
        REPLACE_CASE_SENSITIVE_height=150
        screen_width=REPLACE_CASE_SENSITIVE.winfo_screenwidth()
        screen_height=REPLACE_CASE_SENSITIVE.winfo_screenheight()
        x=(screen_width/2)-(REPLACE_CASE_SENSITIVE_width/2)
        y=(screen_height/2)-(REPLACE_CASE_SENSITIVE_height/2)
        REPLACE_CASE_SENSITIVE.geometry(f'{REPLACE_CASE_SENSITIVE_width}x{REPLACE_CASE_SENSITIVE_height}+{int(x)}+{int(y)}')
        REPLACE_CASE_SENSITIVE.iconbitmap('replace.ico')
        REPLACE_CASE_SENSITIVE.title("REPLACE_CASE_SENSITIVE")
        REPLACE_CASE_SENSITIVE.resizable(0,0)
        replace_case_sensitive_entry1=ttk.Entry(REPLACE_CASE_SENSITIVE, width=25)
        replace_case_sensitive_entry1.place(x=15,y=80)
        replace_case_sensitive_entry2=ttk.Entry(REPLACE_CASE_SENSITIVE, width=25)
        replace_case_sensitive_entry2.place(x=180,y=80)
        replace_case_sensitive_label1=ttk.Label(REPLACE_CASE_SENSITIVE, text='Previous', font="montserrat 8", background='#F0F0F0')
        replace_case_sensitive_label1.place(x=15, y=55)
        replace_case_sensitive_label2=ttk.Label(REPLACE_CASE_SENSITIVE, text='New', font="montserrat 8", background='#F0F0F0')
        replace_case_sensitive_label2.place(x=180, y=55)
        replace_case_sensitive_label3=ttk.Label(REPLACE_CASE_SENSITIVE, text='Type a single word', font="montserrat 10", background='#F0F0F0')
        replace_case_sensitive_label3.place(x=115, y=15)

        
        def replace_case_sensitive_text():
            a=textbox.get(1.0, END)
            text1=replace_case_sensitive_entry1.get()
            text2=replace_case_sensitive_entry2.get()
            value_3=a.replace(text1, text2)
            textbox.delete(1.0, END)
            textbox.insert(INSERT, value_3)

        replace_case_sensitive_button=ttk.Button(REPLACE_CASE_SENSITIVE, text="Replace", width=7, command=replace_case_sensitive_text)
        replace_case_sensitive_button.place(x=130,y=105)
    
    def Replace():
        REPLACE=ThemedTk(theme='radiance')
        REPLACE_width=350
        REPLACE_height=150
        screen_width=REPLACE.winfo_screenwidth()
        screen_height=REPLACE.winfo_screenheight()
        x=(screen_width/2)-(REPLACE_width/2)
        y=(screen_height/2)-(REPLACE_height/2)
        REPLACE.geometry(f'{REPLACE_width}x{REPLACE_height}+{int(x)}+{int(y)}')
        REPLACE.iconbitmap('replace.ico')
        REPLACE.title("REPLACE")
        REPLACE.resizable(0,0)
        replace_entry1=ttk.Entry(REPLACE, width=25)
        replace_entry1.place(x=15,y=80)
        replace_entry2=ttk.Entry(REPLACE, width=25)
        replace_entry2.place(x=180,y=80)
        replace_label1=ttk.Label(REPLACE, text='Previous', font="montserrat 8", background='#F0F0F0')
        replace_label1.place(x=15, y=55)
        replace_label2=ttk.Label(REPLACE, text='New', font="montserrat 8", background='#F0F0F0')
        replace_label2.place(x=180, y=55)
        replace_label3=ttk.Label(REPLACE, text='Type a single word', font="montserrat 10", background='#F0F0F0')
        replace_label3.place(x=115, y=15)
        replace_label4=ttk.Label(REPLACE, text='(Press the button 3 times)', font="montserrat 7 bold", background='#F0F0F0', foreground='#EE4B2B')
        replace_label4.place(x=118, y=35)
        
        
        def replace_text():
            global value_3
            a=textbox.get(1.0, END)
            text1=replace_entry1.get()
            text2=replace_entry2.get()
            Upper=text1.upper()
            Lower=text1.lower()
            Title=text1.title()
            if Upper in a:
                value_3=a.replace(Upper, text2)
            if Lower in a:
                value_3=a.replace(Lower, text2)
            if Title in a:
                value_3=a.replace(Title, text2)
            textbox.delete(1.0, END)
            textbox.insert(INSERT, value_3)


                
        replace_button=ttk.Button(REPLACE, text="Replace", width=7, command=replace_text)
        replace_button.place(x=130,y=105)

   
            
    '''Text Field'''
    textbox= Text(notebook_root, font="montserrat 12", selectbackground="#F0936A", undo=True)
    file=None
    textbox.pack(expand=True, fill=BOTH)
    scrollbar1= Scrollbar(textbox, orient=VERTICAL)
    scrollbar1.config(command=textbox.yview)
    scrollbar1.pack(side=RIGHT, fill=Y)
        
    scrollbar2= Scrollbar(textbox, orient=HORIZONTAL)
    scrollbar2.config(command=textbox.xview)
    scrollbar2.pack(side=BOTTOM, fill=X)
    textbox.config(yscrollcommand=scrollbar1.set, wrap="none", xscrollcommand=scrollbar2.set)
        
    '''MenuPanel of notebook'''
    menupanel= Menu(notebook_root)
        
    filemenu=Menu(menupanel, tearoff=0, activebackground="#F0936A")
    filemenu.add_command(label="New", command=newfile)
    filemenu.add_command(label="Open", command=openfile)
    filemenu.add_command(label="Save", command=savefile)
    filemenu.add_command(label="About", command=about)
    filemenu.add_separator()
    filemenu.add_command(label="Exit", command=close)
    menupanel.add_cascade(label="File", menu= filemenu)
        
    editmenu=Menu(menupanel, tearoff=0, activebackground="#F0936A")
    editmenu.add_command(label="Cut    Ctrl+x", command=cut)
    editmenu.add_command(label="Copy   Ctrl+c", command=copy)
    editmenu.add_command(label="Paste  Ctrl+v", command=paste)
    editmenu.add_command(label="Undo   Ctrl+z", command=textbox.edit_undo)
    editmenu.add_command(label="Redo   Ctrl+y", command=textbox.edit_redo)
    editmenu.add_separator()
    editmenu.add_command(label="Remove(case Sensitive)", command=Remove_Case_Sensitive)
    editmenu.add_command(label="Remove", command=Remove)
    editmenu.add_command(label="Replace(case Sensitive)", command=Replace_Case_Sensitive)
    editmenu.add_command(label="Replace", command=Replace)
    editmenu.add_command(label="Make a List", command=make_a_list)
    menupanel.add_cascade(label="Edit", menu= editmenu)
        
    speakmenu=Menu(menupanel, tearoff=0, activebackground="#F0936A")
    speakmenu.add_command(label="🔊...Text to Speak<Male voice>(English*)", command=speak_in_male_voice)
    menupanel.add_cascade(label="Speak", menu=speakmenu)
    speakmenu.add_command(label="🔊...Text to Speak<Female voice>(English*)", command=speak_in_female_voice)
    
    

    notebook_root.config(menu= menupanel)


splash_root.after(3500, notebook)
mainloop()
    
'''///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////'''


