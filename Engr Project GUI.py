#######
##GUI##
from tkinter import *

WIDTH = 1200  #width/hight          #sets width, hight, and name for person who it's for
HEIGHT = 800
name = "Tommy"



#Main GUI class
class main(Frame): 
    def __init__(self, master):               #Main class in order to set up GUI
        Frame.__init__(self, master)
        self.master = master

    
    def GUI(self):

        welcome = Label(self.master, text = "Welcome, {}!".format(name), font = ("Arial", 20),).place(x = 470, y = 50)
        

        totallabel = Label(self.master, text = "Your total balance", font = ("Arial", 18)).place(x = 490, y = 80)
        total = Label(self.master, text = "${}".format(balance), font = ("Arial", 18), fg = "red").place(x = 500, y = 120)      #The 

        pennylabel = Label(self.master, text = "Number of pennies", font = ("Arial", 18)).place(x = 100, y = 200)
        penny = Label(self.master, text = "{}".format(pennys), font = ("Arial", 18), fg = "red").place(x = 180, y = 260)
        
        
        nicklelabel = Label(self.master, text = "Number of nickles", font = ("Arial", 18)).place(x = 350, y = 200)
        nickle = Label(self.master, text = "{}".format(nickles), font = ("Arial", 18), fg = "red").place(x = 380, y = 260)
        
        
        dimelabel = Label(self.master, text = "Number of dimes", font = ("Arial", 18)).place(x = 600, y = 200)
        dime = Label(self.master, text = "{}".format(dimes), font = ("Arial", 18), fg = "red").place(x = 680, y = 260)
        
        
        quarterlabel = Label(self.master, text = "Number of quarters", font = ("Arial", 18)).place(x = 850, y = 200)
        quarter = Label(self.master, text = "{}".format(quarters), font = ("Arial", 18), fg = "red").place(x = 880, y = 260)        
        






def findbal(): #future command to calculate total balance in bank
    balance = 9.83
    return balance
balance = findbal()
def penny():
    pennys = 12
    return pennys
pennys = penny()


def nickle():
    nickles = 11
    return nickles 
nickles = nickle()


def dime():
    dimes = 9
    return dimes
dimes = dime()


def quarter():
    quarters = 14
    return quarters
quarters = quarter()










window = Tk()
window.geometry("{}x{}".format(WIDTH, HEIGHT))
window.title("Smart Piggy Bank")
U = main(window)
U.GUI()
window.mainloop()
