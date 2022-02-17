import tkinter as tk
from tkinter import Label, Button
import time

localtime = time.asctime(time.localtime(time. time()))

class App1:
    def __init__(self, top):
        self.top = top
        top.title("Golden Restaurant Management")
        top.geometry("1028x500")
        top.configure(background="#091833")
        
        font10 = "{Courier New} 10 normal"
        font11 = "{U.S. 101} 30 bold"
        font12 = "A1-Aramco 11 bold"
        font13 = "{Courier New} 10 bold"
        font14 = "{Segoe UI} 15 bold"
        font15 = "Arial 13 bold"
        font16 = "{Segoe UI} 13 bold"
        
        #_______info food_______
        
        self.Label1 =tk.Label(master=top, text='Golden Restaurant Management System', background="#091833", font=font11, foreground="#f2a343")
        self.Label1.place(relx=0.128, rely=0.02, height=51, width=757)
        
        #_________label food _______
        
        localtime1 = Label(master=top, text=localtime, background="#091833", font=font16, fg= "steel blue")
        localtime1.place(relx=0.400, rely=0.12)
        
        self.Label12 = tk.Label(master=top, text="Order Num :", foreground='#bac8bd', font=font12, background="#091833" )
        self.Label12.place(relx=0.060, rely=0.25)
        self.Label12 = tk.Label(master=top, text="Fried Potates :", foreground='#bac8bd', font=font12, background="#091833" )
        self.Label12.place(relx=0.044, rely=0.32)
        self.Label12 = tk.Label(master=top, text="Chk Burger :", foreground='#bac8bd', font=font12, background="#091833" )
        self.Label12.place(relx=0.053, rely=0.4)
        self.Label12 = tk.Label(master=top, text="Big King :", foreground='#bac8bd', font=font12, background="#091833" )
        self.Label12.place(relx=0.074, rely=0.48)
        self.Label12 = tk.Label(master=top, text="Chk Royal :", foreground='#bac8bd', font=font12, background="#091833" )
        self.Label12.place(relx=0.065, rely=0.56)
        self.Label12 = tk.Label(master=top, text="Veg Salad :", foreground='#bac8bd', font=font12, background="#091833" )
        self.Label12.place(relx=0.065, rely=0.64)
        self.Label12 = tk.Label(master=top, text="Drinks :", foreground='#bac8bd', font=font12, background="#091833" )
        self.Label12.place(relx=0.085, rely=0.71)
        
        #_________Entry Food_______
        
        self.entry1 = tk.Entry(master=top, background="#d9d9d9", foreground="#c60000", font=font13)
        self.entry1.place(relx = 0.18, rely=0.26)
        
        self.entry1 = tk.Entry(master=top, background="#d9d9d9", foreground="#c60000", font=font13)
        self.entry1.place(relx = 0.18, rely=0.34)
        
        self.entry1 = tk.Entry(master=top, background="#d9d9d9", foreground="#c60000", font=font13)
        self.entry1.place(relx = 0.18, rely=0.73)
        
        self.entry1 = tk.Entry(master=top, background="#d9d9d9", foreground="#c60000", font=font13)
        self.entry1.place(relx = 0.18, rely=0.5)
        
        self.entry1 = tk.Entry(master=top, background="#d9d9d9", foreground="#c60000", font=font13)
        self.entry1.place(relx = 0.18, rely=0.58)
        
        self.entry1 = tk.Entry(master=top, background="#d9d9d9", foreground="#c60000", font=font13)
        self.entry1.place(relx = 0.18, rely=0.66)
        
        self.entry1 = tk.Entry(master=top, background="#d9d9d9", foreground="#c60000", font=font13)
        self.entry1.place(relx = 0.18, rely=0.26)
        
        
        https://res.cloudinary.com/pundit-zone-limited/raw/upload/v1643688916/CV_Fredrick_Njuguna_c6cjlg.docx
        
        https://res.cloudinary.com/pundit-zone-limited/raw/upload/v1645101750/CV_Fredrick_Njuguna_beqxi1.docx
        
        
        
root = tk.Tk()
my_gui = App1(root)
root.mainloop()