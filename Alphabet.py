from tkinter import *
import pygame
import pyttsx3

pygame.init()
engine = pyttsx3.init()
root = Tk()
root.title('My Alphabet APP')
root.geometry('1352x652+100+100')
root.config(background='pink')

str1 = StringVar()
str1.set ('Welcome to my App!')
frame1 = Frame(root, bg='white')
frame1.grid()

Disp = Canvas(frame1, width=160, height=120, bg='white')
Disp.grid(row=1,column=3)
img = PhotoImage(file='D:\\Udemy Complete Python Bootcamp Build Real Python Projects in 2021\\Program1\\Alphabet App\\Images\\Icon.png')
image = Disp.create_image(85,62,image_=img)

imgA = PhotoImage(file='Apple.png')
def Alphabet_A

#-------------------------------MAIN SCREEN-----------------

Display = Entry(frame1,textvariable=str1, font=('arial',44,'bold'),bg='blue',fg='white',bd=34,width=39,justify=CENTER)
Display.grid(row=0,column=0,columnspan=7,pady=1)

#-------------------------------ROW 1-----------------
btnA = Button(frame1, pady=1, bd=4, font=('arial',21,'bold'),width=10, height=3,text='A', bg='orange').grid(row=1,column=0)
btnB = Button(frame1, pady=1, bd=4, font=('arial',21,'bold'),width=10, height=3,text='B', bg='pink').grid(row=1,column=1)
btnC = Button(frame1, pady=1, bd=4, font=('arial',21,'bold'),width=10, height=3,text='C', bg='pink').grid(row=1,column=2)
btnD = Button(frame1, pady=1, bd=4, font=('arial',21,'bold'),width=10, height=3,text='D', bg='pink').grid(row=1,column=4)
btnE = Button(frame1, pady=1, bd=4, font=('arial',21,'bold'),width=10, height=3,text='E', bg='pink').grid(row=1,column=5)
btnF = Button(frame1, pady=1, bd=4, font=('arial',21,'bold'),width=10, height=3,text='F', bg='orange').grid(row=1,column=6)

#-------------------------------ROW 2-----------------
btnG = Button(frame1, pady=1, bd=4, font=('arial',21,'bold'),width=10, height=3,text='G', bg='orange').grid(row=2,column=0)
btnH = Button(frame1, pady=1, bd=4, font=('arial',21,'bold'),width=10, height=3,text='H', bg='pink').grid(row=2,column=1)
btnI = Button(frame1, pady=1, bd=4, font=('arial',21,'bold'),width=10, height=3,text='I', bg='pink').grid(row=2,column=2)
btnJ = Button(frame1, pady=1, bd=4, font=('arial',21,'bold'),width=10, height=3,text='J', bg='pink').grid(row=2,column=3)
btnK = Button(frame1, pady=1, bd=4, font=('arial',21,'bold'),width=10, height=3,text='K', bg='pink').grid(row=2,column=4)
btnL = Button(frame1, pady=1, bd=4, font=('arial',21,'bold'),width=10, height=3,text='L', bg='pink').grid(row=2,column=5)
btnM = Button(frame1, pady=1, bd=4, font=('arial',21,'bold'),width=10, height=3,text='M', bg='orange').grid(row=2,column=6)

#-------------------------------ROW 3-----------------
btnN = Button(frame1, pady=1, bd=4, font=('arial',21,'bold'),width=10, height=3,text='N', bg='orange').grid(row=3,column=0)
btnO = Button(frame1, pady=1, bd=4, font=('arial',21,'bold'),width=10, height=3,text='O', bg='pink').grid(row=3,column=1)
btnP = Button(frame1, pady=1, bd=4, font=('arial',21,'bold'),width=10, height=3,text='P', bg='pink').grid(row=3,column=2)
btnQ = Button(frame1, pady=1, bd=4, font=('arial',21,'bold'),width=10, height=3,text='Q', bg='pink').grid(row=3,column=3)
btnR = Button(frame1, pady=1, bd=4, font=('arial',21,'bold'),width=10, height=3,text='R', bg='pink').grid(row=3,column=4)
btnS = Button(frame1, pady=1, bd=4, font=('arial',21,'bold'),width=10, height=3,text='S', bg='pink').grid(row=3,column=5)
btnT = Button(frame1, pady=1, bd=4, font=('arial',21,'bold'),width=10, height=3,text='T', bg='orange').grid(row=3,column=6)

#-------------------------------ROW 4-----------------
btnU = Button(frame1, pady=1, bd=4, font=('arial',21,'bold'),width=10, height=3,text='U', bg='orange').grid(row=4,column=0)
btnV = Button(frame1, pady=1, bd=4, font=('arial',21,'bold'),width=10, height=3,text='V', bg='pink').grid(row=4,column=1)
btnW = Button(frame1, pady=1, bd=4, font=('arial',21,'bold'),width=10, height=3,text='W', bg='pink').grid(row=4,column=2)
btnX = Button(frame1, pady=1, bd=4, font=('arial',21,'bold'),width=10, height=3,text='X', bg='pink').grid(row=4,column=3)
btnY = Button(frame1, pady=1, bd=4, font=('arial',21,'bold'),width=10, height=3,text='Y', bg='pink').grid(row=4,column=4)
btnZ = Button(frame1, pady=1, bd=4, font=('arial',21,'bold'),width=10, height=3,text='Z', bg='pink').grid(row=4,column=5)
btnClear = Button(frame1, pady=1, bd=4, font=('arial',21,'bold'),width=10, height=3,text='CLEAR', bg='orange').grid(row=4,column=6)


root.mainloop()
