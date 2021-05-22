# 1. Write a Python program which accepts the radius of a circle from the user and compute the area.
# Developed by : Yamini Rathod C0796390
# Date : 16-05-2021

# Method 3 : Using Python tkinter feature

from tkinter import *
from tkinter import messagebox

class myCalculator:
    def __init__(self):
        self.window = Tk()
        self.window.title("My Calculator")
        self.window.geometry("500x400")

        self.top_frame = Frame()
        self.bottom_frame = Frame()
        self.result_frame = Frame()

        self.welcome_label1 = Label(self.top_frame, text="Welcome to Reverse Name Program")
        self.welcome_label2 = Label(self.top_frame, text="Designed By: Yamini Rathod C0796390")

        self.prompt_label1 = Label(self.top_frame, text="Please enter the first name : ")
        self.fname = Entry(self.top_frame)

        self.prompt_label2 = Label(self.top_frame, text="Please enter the last name : ")
        self.lname = Entry(self.top_frame)

        self.calc_buttom1 = Button(self.bottom_frame, text="Get Reverse", padx=10, command=self.rev)
        self.cancel_button = Button(self.bottom_frame, text="Exit", padx=10, command=self.window.destroy)

        self.result = StringVar()
        self.result.set("Result: N/A")
        self.result_label = Label(self.result_frame, textvariable=self.result, bg="yellow", fg="green")

        self.welcome_label1.pack(padx=10, pady=10)
        self.welcome_label2.pack(padx=10, pady=10)
        self.prompt_label1.pack(padx=10, pady=10)
        self.fname.pack(padx=10, pady=10)
        self.prompt_label2.pack(padx=10, pady=10)
        self.lname.pack(padx=10, pady=10)

        self.calc_buttom1.pack(side="left", padx=10, pady=10)
        self.cancel_button.pack(side="left", padx=10, pady=10)
        self.result_label.pack(side="left", padx=10, pady=10)

        self.top_frame.pack()
        self.bottom_frame.pack()
        self.result_frame.pack()

        mainloop()

    def rev(self):
        try:
            firstname = self.fname.get()
            lastname = self.lname.get()

            self.result.set(f'The reverse output is : {lastname} {firstname}')
        except:
            messagebox.showerror("Input Error", "The input is invalid! Please try again!")

myWindow = myCalculator()