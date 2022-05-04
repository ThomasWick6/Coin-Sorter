#######
##GUI##

from tkinter import *

import serial
import time

global dval,pval,nval,qval
dval = 2.27
pval = 2.5
nval = 5.0
qval = 5.67


WIDTH = 1200  #width/hight          #sets width, hight, and name for person who it's for
HEIGHT = 800
name = "Tommy"

arduino = serial.Serial(port='COM3', baudrate=57600, timeout=.1)


time.sleep(20)
def ar_read():
    while True:
        val = 'p'
        arduino.write(bytes(val,'utf-8'))
    
        time.sleep(0.05)
    
        listdata = []
        for n in range(1000):
        
            data = arduino.readline()
            print (data)
            try:
                fdata = float(data)
            
                listdata.append(fdata)

                if (len(listdata)==4):
                    break
            
            except:
                pass
        if (len(listdata)==4):
            break
    ndata = len(listdata)   
    d1 = float(listdata[ndata-4])
    p1 = float(listdata[ndata-3])
    n1 = float(listdata[ndata-2])
    q1 = float(listdata[ndata-1])
            
    d2 = d1/dval
    p2 = p1/pval
    n2 = n1/nval
    q2 = q1/qval
            
    #print (p2,n2,d2,q2)   
    return round(d2),round(p2),round(n2),round(q2)




#Main GUI class
class main(Frame): 
    def __init__(self, master):               #Main class in order to set up GUI
        Frame.__init__(self, master)
        self.master = master

    
    def GUI(self):

        
        welcome = Label(self.master, text = "Welcome, {}!".format(name), font = ("Arial", 20),).place(x = 470, y = 50)
    
        dimes,pennys,nickles,quarters = ar_read()
             
        balance = pennys*0.01 + nickles*0.05 + dimes*0.1 + quarters*0.25
        balance = round(balance,2)

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

        
def runbank():
    
    U.GUI()
    window.after(1000,runbank)
    

window = Tk()
window.geometry("{}x{}".format(WIDTH, HEIGHT))
window.title("Smart Piggy Bank")
U = main(window)
U.GUI()
runbank()
window.mainloop()





