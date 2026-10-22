from tkinter import *

first_num=second_num=operator=None

def get_digit(digit):
    current = result_label['text']                       #7                   
    new = current + str(digit)                           #78
    result_label.config(text=new)                        #78

def clear():
    result_label.config(text='')                         #C

def get_operator(op):
    global first_num,operator                            #Global number access kiya  

    first_num = int(result_label['text'])                #Convert to intger
    operator = op                                        
    result_label.config(text='')                         #''

def get_result():
    global first_num,second_num,operator
    second_num = int(result_label['text'])

    if operator == '+':
        result_label.config(text=str(first_num + second_num))        #Add
    elif operator == '-':
        result_label.config(text=str(first_num - second_num))        #Sub
    elif operator == '*':
        result_label.config(text=str(first_num * second_num))        #Multi
    else:
        if second_num == 0:
            result_label.config(text='Error')                        #Infinte
        else:
            result_label.config(text=str(first_num / second_num))    #Div

root = Tk()                          
root.title('Calculator')                         #title
root.geometry('280x400')                         #Structure
root.resizable(0,0)                              #Fixed Size
root.configure(background='black')               #bg='black'

result_label = Label(root,text='',fg='white',bg='black')                    #kya likha hoga
result_label.grid(row=0,column=0,columnspan=10,pady=(50,25),sticky='w')     #rows or columns bnane k liye
result_label.configure(font=('verdana',30,'bold'))                          #kis font me?

btn7 = Button(root,text='7',bg="#0056a6",fg='white',width=5,height=2,command=lambda :get_digit(7))
btn7.grid(row=1,column=0)                  #1st row,0th col me 7
btn7.config(font=('verdana',14))           #command se function call hota h

btn8 = Button(root,text='8',bg="#0056a6",fg='white',width=5,height=2,command=lambda :get_digit(8))
btn8.grid(row=1,column=1)                  #1st row, 1st col me 8
btn8.config(font=('verdana',14))

btn9 = Button(root,text='9',bg="#0056a6",fg='white',width=5,height=2,command=lambda :get_digit(9))
btn9.grid(row=1,column=2)
btn9.config(font=('verdana',14))

btn_add = Button(root,text='+',bg="#0056a6",fg='white',width=5,height=2,command=lambda :get_operator('+'))
btn_add.grid(row=1,column=3)
btn_add.config(font=('verdana',14))

btn4 = Button(root,text='4',bg="#0056a6",fg='white',width=5,height=2,command=lambda :get_digit(4))
btn4.grid(row=2,column=0)
btn4.config(font=('verdana',14))

btn5 = Button(root,text='5',bg="#0056a6",fg='white',width=5,height=2,command=lambda :get_digit(5))
btn5.grid(row=2,column=1)
btn5.config(font=('verdana',14))

btn6 = Button(root,text='6',bg="#0056a6",fg='white',width=5,height=2,command=lambda :get_digit(6))
btn6.grid(row=2,column=2)
btn6.config(font=('verdana',14))

btn_sub = Button(root,text='-',bg="#0056a6",fg='white',width=5,height=2,command=lambda :get_operator('-'))
btn_sub.grid(row=2,column=3)
btn_sub.config(font=('verdana',14))

btn1 = Button(root,text='1',bg="#0056a6",fg='white',width=5,height=2,command=lambda :get_digit(1))
btn1.grid(row=3,column=0)
btn1.config(font=('verdana',14))

btn2 = Button(root,text='2',bg="#0056a6",fg='white',width=5,height=2,command=lambda :get_digit(2))
btn2.grid(row=3,column=1)
btn2.config(font=('verdana',14))

btn3 = Button(root,text='3',bg="#0056a6",fg='white',width=5,height=2,command=lambda :get_digit(3))
btn3.grid(row=3,column=2)
btn3.config(font=('verdana',14))

btn_multi = Button(root,text='*',bg="#0056a6",fg='white',width=5,height=2,command=lambda :get_operator('*'))
btn_multi.grid(row=3,column=3)
btn_multi.config(font=('verdana',14))

btn_clr = Button(root,text='C',bg="#0056a6",fg='white',width=5,height=2,command=lambda :clear())
btn_clr.grid(row=4,column=0)
btn_clr.config(font=('verdana',14))

btn0 = Button(root,text='0',bg="#0056a6",fg='white',width=5,height=2,command=lambda :get_digit(0))
btn0.grid(row=4,column=1)
btn0.config(font=('verdana',14))

btn_equal = Button(root,text='=',bg="#0056a6",fg='white',width=5,height=2,command=get_result)
btn_equal.grid(row=4,column=2)
btn_equal.config(font=('verdana',14))

btn_div = Button(root,text='/',bg="#0056a6",fg='white',width=5,height=2,command=lambda :get_operator('/'))
btn_div.grid(row=4,column=3)
btn_div.config(font=('verdana',14))

root.mainloop()