#Classroom Print
#By Kevin Papenhausen
# A GUI Application that allows for the printing of many documents at once by simple highlighting the
# documents you wish to print

import os, subprocess, time, shutil, getpass, smtplib, email

from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
from pathlib import Path
from shutil import copyfile
from os import listdir
from os.path import isfile, join
from email.mime.text import MIMEText

root = Tk()
root.title("Classroom Print")


def intro():
    answer = messagebox.askquestion('Classroom Print', '    Welcome to Classroom Print!\n\n Would you like to see directions?')

    if answer == 'yes':
        instruction()

    


def donothing():
    print("Nothing being done")
def instruction():
    os.startfile(r'Classroom Print Instructions.pdf')
def pastprints():
    os.startfile(r'C:/Users/Public/Desktop/Printed')
def openPath():
    os.startfile(r'explorer.exe')
def openPath1():
    os.startfile(r'shell:::{A8A91A66-3A7D-4424-8D24-04E180695C7A}')
def openPath2():
    filename =  filedialog.askopenfilenames(parent = root,title = "choose your file")
    #print(filename)
    filename = root.tk.splitlist(filename)
    
    file = list(filename) #creates list
    
    if file != []:  
        running =  True
        while running:
            for path in file:
                
                dst = r'To_Print/'
                print(dst)
                thispath = path
                print(thispath)
                
                file.remove(thispath)
                
                shutil.copy(thispath, dst) # copys path
                if file ==[]:
                    running = False
                else:
                    continue
    else:
        exit
        
def printloc():
    os.startfile(r'To_Print')


#Removes Printed Files

def remove():
    
    path = r'To_Print/'
    printer = "print"

    t = os.path.abspath(r'To_Print/')

    onlyfiles = [f for f in listdir(path) if isfile(join(path, f))]
    running = True
    if onlyfiles == []:
        running = False
    else:
        while running:
            for elem in onlyfiles:
                
                path_tpl =r'C:\Users\{}\Downloads'
                dst = path_tpl.format(getpass.getuser())
    
                thiselem = elem
                onlyfiles.remove(thiselem)
                aPath= "To_Print/" + thiselem
                print(aPath)
                os.remove(aPath)
               
                    
                if onlyfiles == []:
                    running = False
def remove1():
    
    path = r'To_Print/'
    printer = "print"

    t = os.path.abspath(r'To_Print/')

    onlyfiles = [f for f in listdir(path) if isfile(join(path, f))]
    running = True
    if onlyfiles == []:
        messagebox.showinfo('Cleared',"Documents Cleared from printer queue")
        running = False
    else:
        while running:
            for elem in onlyfiles:
                
                path_tpl =r'C:\Users\{}\Downloads'
                dst = path_tpl.format(getpass.getuser())
                thiselem = elem
                onlyfiles.remove(thiselem)
                aPath= "To_Print/" + thiselem
                print(aPath)
                os.remove(aPath)
              
                    
                if onlyfiles == []:
                    messagebox.showinfo('Cleared',"Documents cleared from printer queue")
                    running = False


                
#Function to print files                  

def printing():

    cname=os.environ['COMPUTERNAME']
    print(cname)
    path = r'To_Print/'
    printer = "print"

    t = os.path.abspath(r'To_Print/')

    onlyfiles = [f for f in listdir(path) if isfile(join(path, f))]
   
    print(onlyfiles)
    index = 0
    if onlyfiles != []:    
        running = True
        while running:
            for elem in onlyfiles:
            
                thiselem = elem
                onlyfiles.remove(thiselem)
                aPath= "To_Print\\" + thiselem
                print(aPath)
                os.startfile(aPath, printer) #This send doc to printer
                
                time.sleep(0.2)
                if onlyfiles == []:
                    usage()
                    #time.sleep(1)
                    messagebox.showinfo('Print Status',"Print Job Complete!.... To print another copy, simply click 'Print'.  To print different documents, click 'Clear' and perform Step 1 again.")
                    
                    running = False
    
    else:
        messagebox.showinfo('ERROR', "Printer Queue is Empty.  Please Add Files")
        print("nothing to print")

"""Main Menu"""

def window():
    width_of_window = 700
    height_of_window = 800

    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    x_coordinate = (screen_width/2) - (width_of_window/2)
    y_coordinate = (screen_height/2) - (height_of_window/2)

    root.geometry("%dx%d+%d+%d" % (width_of_window, height_of_window, x_coordinate, y_coordinate))

    

    menu()
    
"""Top Menu for file and exit"""
def menu():
    menu = Menu(root)
    root.config(menu=menu)

    subMenu = Menu(menu)
    menu.add_cascade(label="File", menu=subMenu)
    subMenu.add_command(label="Open", command= lambda : openPath2())
    subMenu.add_separator() #adds line in 
    #subMenu.add_command(label="Exit", command=quit)

    editmenu = Menu(menu)
    menu.add_cascade(label="View", menu=editmenu)
    editmenu.add_command(label="Print Queue", command= lambda : printloc())

    editmenu = Menu(menu)
    menu.add_cascade(label="Select", menu=editmenu)
    editmenu.add_command(label="Printer", command= lambda : openPath1())

    editmenu = Menu(menu)
    menu.add_cascade(label="Help", menu=editmenu)
    editmenu.add_command(label="Directions", command= lambda : instruction())

    


    toolbar()
    
"""Toolbar"""
def toolbar():

   
    toolbar = Label(root,text='Classroom Print', bg="#001489", fg='White',bd=8,relief="groove", font='Helvetica 32 bold')
    toolbar.pack(side=TOP, fill=X)

    C1 = Canvas(root, bg="red", height=1, width=800)
    C1.pack(side=TOP, fill=X)

  
    
    
    statusBar()
    
"""Status Bar"""
def statusBar():
    status = Label(root, text= "Waiting to Print...", bd=1, relief=SUNKEN, anchor=W)
    status.pack(sid=BOTTOM, fill=X)
    

    
def button():

    rightFrame = Frame(root, width=610, height = 515, relief = 'groove',bd=8, bg="#001489", highlightthickness=2, highlightbackground="#B22222")
    rightFrame.place(x = 40, y = 85)

    Print = Button(root, text="Print",relief = 'groove', bd=4, width=5, height=0, font='Helvetica 17 bold', command=lambda : printing(), bg ='#4876FF', foreground='white')
    Clear = Button(root, text="Clear",relief = 'groove', bd=4, width=5, height=0, font='Helvetica 17 bold', command=lambda : remove1(), bg ='#4876FF', foreground='white')
    openPath = Button(root, text="Open",relief = 'groove',bd=4, width=5, height=0, font='Helvetica 17 bold', bg ='#4876FF', foreground='white',command= lambda : openPath2())
    

    
    openPath.place(x = 530, y = 150)
    
 
    Print.place(x = 530, y = 280)
    Clear.place(x = 530, y = 500)
    
  
    
    directions()
def directions():
    
    direction1 = Label(root,text='Step 1: ', bg="#001489", fg='White', font='Helvetica 24 bold')
    direction3 = Label(root,text='Step 2:', bg="#001489", fg='White', font='Helvetica 24 bold')
    direction4 = Label(root,text='Clear Print Queue:', bg="#001489", fg='White', font='Helvetica 24 bold')
    
    
    direction1.place(x = 275, y = 150)
    direction3.place(x = 275, y = 280)
    direction4.place(x = 100, y = 500)
    
def usage():

    msg = MIMEText('Classroom Print Usage')
    msg['Subject'] = os.environ['COMPUTERNAME']


    sender ="classroomprint@saratogaschools.org"
    receiver= "classroomprint@saratogaschools.org"
    #print(content)
    try:
        mailserver = smtplib.SMTP('smtp.office365.com',587)
        mailserver.ehlo()
        mailserver.starttls()
        mailserver.login(sender, 'Printcl@ssroom!')
        mailserver.sendmail(sender, receiver, msg.as_string())
        mailserver.quit()  
    except:
        print("unable to send")


window()



filename = PhotoImage(file = "images1.PNG")
background_label = Label(root, image=filename)
background_label.pack(side=BOTTOM, fill= X)

C = Canvas(root, bg="#333399", height=1, width=800)
C.pack(side=BOTTOM, fill=X)



backgroundImage = PhotoImage(file = "background.png")
panel1 = Label(root, image=backgroundImage)
panel1.pack(side=LEFT)

remove()
button()

printer = PhotoImage(file = "printer.PNG")
printer_label = Label(root, image=printer)
printer_label.place(x = 60, y = 155)
intro()





root.mainloop()

