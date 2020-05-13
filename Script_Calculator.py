from tkinter import *

class Action_Display_Calculator:
    def __init__(self,root,nilai):
        self.nilai = nilai
        self.root = root
    def button_click(self,number):
        self.nilai.insert(END,number)

    def button_hapus_satu(self):
        strings = str(self.nilai.get())
        if len(strings) == 1:
            kosong = ""
            self.nilai.delete(0,END)
        else:
            self.nilai.delete(len(strings)-1)
    def button_hapus(self):
        strings = self.nilai.get()
        self.nilai.delete(0,END)
  
    def button_enter(self):
        operator = str(self.nilai.get()).replace("x","*")
        sumup = eval(operator)
        self.nilai.delete(0,END)
        self.nilai.insert(0,sumup)
       
    def display(self):
        #number button
        button_1=  Button(self.root, text="1", bg="#00BFFF",padx=16, bd=8, fg='black',font=('arial',20, 'bold'), activebackground="#FFC0CB",command=lambda : self.button_click(1))
        button_2=  Button(self.root, text="2",   bg="#00BFFF",padx=16, bd=8, fg='black',font=('arial',20, 'bold'), activebackground="#FFC0CB",command=lambda : self.button_click(2))
        button_3=  Button(self.root, text="3",  bg="#00BFFF",padx=16, bd=8, fg='black',font=('arial',20, 'bold'), activebackground="#FFC0CB",command=lambda : self.button_click(3))
        button_4=  Button(self.root, text="4", bg="#00BFFF",padx=16, bd=8, fg='black',font=('arial',20, 'bold'), activebackground="#FFC0CB",command=lambda : self.button_click(4))
        button_5=  Button(self.root, text="5",  bg="#00BFFF",padx=16, bd=8, fg='black',font=('arial',20, 'bold'), activebackground="#FFC0CB",command=lambda : self.button_click(5))
        button_6=  Button(self.root, text="6",  bg="#00BFFF",padx=16, bd=8, fg='black',font=('arial',20, 'bold'), activebackground="#FFC0CB",command=lambda : self.button_click(6))
        button_7=  Button(self.root, text="7",  bg="#00BFFF",padx=16, bd=8, fg='black',font=('arial',20, 'bold'), activebackground="#FFC0CB",command=lambda : self.button_click(7))
        button_8=  Button(self.root, text="8", bg="#00BFFF",padx=16, bd=8, fg='black',font=('arial',20, 'bold'), activebackground="#FFC0CB",command=lambda : self.button_click(8))
        button_9=  Button(self.root, text="9",bg="#00BFFF",padx=16, bd=8, fg='black',font=('arial',20, 'bold'), activebackground="#FFC0CB",command=lambda : self.button_click(9))
        button_0=  Button(self.root, text="0",bg="#00BFFF",padx=16, bd=8, fg='black',font=('arial',20, 'bold'), activebackground="#FFC0CB",command=lambda : self.button_click(0))
        #special or option
        button_koma=  Button(self.root, text=".",bg="#00BFFF",padx=19, bd=8, fg='black',font=('arial',20, 'bold'), activebackground="#FFC0CB",command=lambda : self.button_click("."))
        button_tambah=  Button(self.root, text="+",bg="#00BFFF",padx=16, bd=8, fg='black',font=('arial',20, 'bold'), activebackground="#FFC0CB",command=lambda : self.button_click("+"))
        button_kali=  Button(self.root, text="x",bg="#00BFFF",padx=25, bd=8, fg='black',font=('arial',20, 'bold'), activebackground="#FFC0CB",command=lambda :self.button_click("x"))
        button_kurang=  Button(self.root, text="-",bg="#00BFFF",padx=28, bd=8, fg='black',font=('arial',20, 'bold'), activebackground="#FFC0CB",command=lambda :self.button_click("-"))
        button_bagi=  Button(self.root, text="/",bg="#00BFFF",padx=29, bd=8, fg='black',font=('arial',20, 'bold'), activebackground="#FFC0CB",command=lambda : self.button_click("/"))
        button_hapus_satu=  Button(self.root, text="<<",bg="#00BFFF",padx=16, bd=8, fg='black',font=('arial',20, 'bold'), activebackground="#FFC0CB",command= self.button_hapus_satu)
        button_hapus=  Button(self.root, text="C",bg="#00BFFF",padx=55, pady=16 ,bd=8, fg='black',font=('arial',20, 'bold'), activebackground="#FFC0CB",command= self.button_hapus)
        enter = Button(self.root,text="Enter",borderwidth=2 ,padx=40, pady=16, bg="#00BFFF", bd=8, fg='black',font=('arial',20, 'bold'), activebackground="#FFC0CB",command= self.button_enter )
        
        button_7.grid(row=1, column=0)
        button_8.grid(row=1, column=1)
        button_9.grid(row=1, column=2)
        button_hapus_satu.grid(row=1, column=3)

        button_4.grid(row=2, column=0)
        button_5.grid(row=2, column=1)
        button_6.grid(row=2, column=2)
        button_kurang.grid(row=2, column=3)
        
        button_1.grid(row=3, column=0)
        button_2.grid(row=3, column=1)
        button_3.grid(row=3, column=2)
        button_kali.grid(row=3, column=3)

        button_0.grid(row=4, column=0)
        button_koma.grid(row=4, column=1)
        button_tambah.grid(row=4, column=2)
        button_bagi.grid(row=4, column=3)
        
        enter.grid(row=5,column=2, columnspan=2)
        button_hapus.grid(row=5, column=0,columnspan=2)


class Calculator:
    def __init__(self):
        root = Tk()
        root.title('Calculator')
        root.iconbitmap('e:/Python3.8 tutorial/calculator_icon.ico')
        nilai = Entry(root,font=('arial', 20 , 'bold'), bd=25, insertwidth=5, bg="#00BFFF", justify='left')
        # nilai.grid(row=0,column=0,columnspan=3,ipady=10)
        nilai.grid(columnspan=4,ipady=20)
        action = Action_Display_Calculator(root,nilai)
        action.display()
        root.mainloop()
calculator = Calculator()