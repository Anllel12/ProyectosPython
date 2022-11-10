import tkinter as tk
import math 

root = tk.Tk()
root.title('Calculadora')

i = 0
operation = ''
operation1 = 0
operation2 = 0
result = 0

display = tk.Entry(root, width = 40)
display.grid(row = 1 , columnspan = 6)

# Numeric Buttons

tk.Button(root, text='0', command = lambda: getNumber(0)).grid(padx=5, pady=5, row = 5, column = 0)
tk.Button(root, text='AC', command = lambda: clear()).grid(padx=5, pady=5, row = 5, column = 1)
tk.Button(root, text='=', command = lambda: equal()).grid(padx=5, pady=5, row = 5, column = 2)
tk.Button(root, text='+', command = lambda: getOperation('+')).grid(padx=5, pady=5, row = 5, column = 3)

tk.Button(root, text='1', command = lambda: getNumber(1)).grid(padx=5, pady=5, row = 4, column = 0)
tk.Button(root, text='2', command = lambda: getNumber(2)).grid(padx=5, pady=5, row = 4, column = 1)
tk.Button(root, text='3', command = lambda: getNumber(3)).grid(padx=5, pady=5, row = 4, column = 2)
tk.Button(root, text='-', command = lambda: getOperation('-')).grid(padx=5, pady=5, row = 4, column = 3)

tk.Button(root, text='4', command = lambda: getNumber(4)).grid(padx=5, pady=5, row = 3, column = 0)
tk.Button(root, text='5', command = lambda: getNumber(5)).grid(padx=5, pady=5, row = 3, column = 1)
tk.Button(root, text='6', command = lambda: getNumber(6)).grid(padx=5, pady=5, row = 3, column = 2)
tk.Button(root, text='*', command = lambda: getOperation('*')).grid(padx=5, pady=5, row = 3, column = 3)

tk.Button(root, text='7', command = lambda: getNumber(7)).grid(padx=5, pady=5, row = 2, column = 0)
tk.Button(root, text='8', command = lambda: getNumber(8)).grid(padx=5, pady=5, row = 2, column = 1)
tk.Button(root, text='9', command = lambda: getNumber(9)).grid(padx=5, pady=5, row = 2, column = 2)
tk.Button(root, text='/', command = lambda: getOperation('/')).grid(padx=5, pady=5, row = 2, column = 3)
# tk.Button(root, text='<-', command = lambda: undo()).grid(padx=5, pady=5, row = 2, column = 4)

def getNumber(n):
    global i
    display.insert(i, n)
    i += 1

def getOperation(operator):
    global operation
    global operation1
    operation1 = display.get()
    operation = operator
    clear()

def clear():
    global i
    global result
    display.delete(0, tk.END)
    i = 0
    result = 0

def equal():
    global i
    global result
    if operation == '/':
        result = operation1/operation2
    elif operation == '*':
        result = operation1*operation2
    elif operation == '-':
        result = operation1-operation2
    elif operation == '+':
        result = operation1+operation2
    clear()
    display.insert(i, result)

root.mainloop()

