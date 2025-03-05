from tkinter import *
root=Tk()
root.title('Developed by MD.NAHIDUL ISLAM')
root.iconbitmap('cal.ico')
root.geometry('300x370')
root.resizable(False,False)
entry=Entry(root,font=('Arial',20),width=18,justify=RIGHT,borderwidth=12,bg='white',fg='blue')
entry.grid(row=0,column=0,columnspan=5)
entry.insert(0,0)
current_input=""
def update_input(value):
    global current_input
    current_input += str(value)
    entry.delete(0,END)
    entry.insert(0,current_input)
def clear_input():
    global current_input
    current_input=""
    entry.delete(0,END)
    entry.insert(0,0)
def undo_input():
    global current_input
    current_input = current_input[:-1]
    entry.delete(0,END)
    entry.insert(0,current_input)

def calculate_result():
    global current_input
    try:
        if '+' in current_input:
            output=current_input.split('+')
            result=float(output[0])+float(output[1])
        elif '-' in current_input:
            output=current_input.split('-')
            result=float(output[0])-float(output[1])
        elif '*' in current_input:
            output=current_input.split('*')
            result=float(output[0])*float(output[1])
        elif '/' in current_input:
            output=current_input.split('/')
            result=float(output[0])/float(output[1])
        elif '%' in current_input:
            output=current_input.split('%')
            result=float(output[0])%float(output[1])
        elif '^' in current_input:
            output=current_input.split('^')
            result=float(output[0])**float(output[1])
        elif 'r(' in current_input:
            output=current_input.split('r(')
            no=int(output[1]) # coll 1 index
            output=no**(1/2)
            result=output
        entry.delete(0,END)
        entry.insert(0,result)
        current_input=str(result)

    except:
        entry.delete(0,END)
        entry.insert(0,'Envalid syntax')



Button(root,text='C',font=('Arial',14),width=3,height=1,bg='red',fg='white',borderwidth=8,command=clear_input).grid(row=1,column=0,padx=4,pady=4)
Button(root,text='<<',font=('Arial',14),width=3,height=1,bg='red',fg='white',borderwidth=8,command=undo_input).grid(row=1,column=1,padx=4,pady=4)
Button(root,text='%',font=('Arial',14),width=3,height=1,bg='brown',fg='white',borderwidth=8,command=lambda:update_input('%')).grid(row=1,column=2,padx=4,pady=4)
Button(root,text='/',font=('Arial',14),width=3,height=1,bg='brown',fg='white',borderwidth=8,command=lambda:update_input('/')).grid(row=1,column=3,padx=4,pady=4)

Button(root,text='7',font=('Arial',14),width=3,height=1,bg='gray',fg='white',borderwidth=8,command=lambda:update_input(7)).grid(row=2,column=0,padx=4,pady=4)
Button(root,text='8',font=('Arial',14),width=3,height=1,bg='gray',fg='white',borderwidth=8,command=lambda:update_input(8)).grid(row=2,column=1,padx=4,pady=4)
Button(root,text='9',font=('Arial',14),width=3,height=1,bg='gray',fg='white',borderwidth=8,command=lambda:update_input(9)).grid(row=2,column=2,padx=4,pady=4)
Button(root,text='x',font=('Arial',14),width=3,height=1,bg='brown',fg='white',borderwidth=8,command=lambda:update_input('*')).grid(row=2,column=3,padx=4,pady=4)

Button(root,text='4',font=('Arial',14),width=3,height=1,bg='gray',fg='white',borderwidth=8,command=lambda:update_input(4)).grid(row=3,column=0,padx=4,pady=4)
Button(root,text='5',font=('Arial',14),width=3,height=1,bg='gray',fg='white',borderwidth=8,command=lambda:update_input(5)).grid(row=3,column=1,padx=4,pady=4)
Button(root,text='6',font=('Arial',14),width=3,height=1,bg='gray',fg='white',borderwidth=8,command=lambda:update_input(6)).grid(row=3,column=2,padx=4,pady=4)
Button(root,text='-',font=('Arial',14),width=3,height=1,bg='brown',fg='white',borderwidth=8,command=lambda:update_input('-')).grid(row=3,column=3,padx=4,pady=4)

Button(root,text='1',font=('Arial',14),width=3,height=1,bg='gray',fg='white',borderwidth=8,command=lambda:update_input(1)).grid(row=4,column=0,padx=4,pady=4)
Button(root,text='2',font=('Arial',14),width=3,height=1,bg='gray',fg='white',borderwidth=8,command=lambda:update_input(2)).grid(row=4,column=1,padx=4,pady=4)
Button(root,text='3',font=('Arial',14),width=3,height=1,bg='gray',fg='white',borderwidth=8,command=lambda:update_input(3)).grid(row=4,column=2,padx=4,pady=4)
Button(root,text='+',font=('Arial',14),width=3,height=1,bg='brown',fg='white',borderwidth=8,command=lambda:update_input('+')).grid(row=4,column=3,padx=4,pady=4)

Button(root,text='00',font=('Arial',14),width=3,height=1,bg='blue',fg='white',borderwidth=8,command=lambda:update_input('00')).grid(row=5,column=0,padx=4,pady=4)
Button(root,text='0',font=('Arial',14),width=3,height=1,bg='gray',fg='white',borderwidth=8,command=lambda:update_input(0)).grid(row=5,column=1,padx=4,pady=4)
Button(root,text='.',font=('Arial',14),width=3,height=1,bg='blue',fg='white',borderwidth=8,command=lambda:update_input('.')).grid(row=5,column=2,padx=4,pady=4)
Button(root,text='=',font=('Arial',14),width=3,height=1,bg='green',fg='white',borderwidth=8,command=calculate_result).grid(row=5,column=3,padx=4,pady=4)

root.mainloop()
