#!/usr/bin/python3
# -*- coding: utf-8 -*-
import random
import tkinter as tk
from tkinter import messagebox


# 创建一个主窗口，用于容纳整个GUI程序
root = tk.Tk()
# 设置主窗口对象的标题栏
root.title("2048")
root.configure(background='#faf8ef')

#设置窗口大小
width = 325
height = 350
#获取屏幕尺寸以计算布局参数，使窗口居屏幕中央
screenwidth = root.winfo_screenwidth()
screenheight = root.winfo_screenheight()
alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth-width)/2, (screenheight-height)/2)
root.geometry(alignstr)
#设置窗口是否可变长、宽，True：可变，False：不可变
root.resizable(width=False, height=False)

#上部分内容
fm1=tk.Frame(root)
titleLabel=tk.Label(fm1, text='2048', font=('Arial', 25), bg='#faf8ef', fg='#776e65')
titleLabel2=tk.Label(fm1, text='', font=('Arial', 16), bg='#faf8ef')
scoreLabel=tk.Label(fm1, text='SCORE\n0', font=('Arial', 10), bg='#bbada0', fg='white')
titleLabel4=tk.Label(fm1, text='', font=('Arial', 16), bg='#faf8ef')
bestLabel=tk.Label(fm1, text='BEST\n0', font=('Arial', 10), bg='#bbada0', fg='white')
titleLabel.grid(column=0, row=0)
titleLabel2.grid(column=1, row=0)
scoreLabel.grid(column=2, row=0)
titleLabel4.grid(column=3, row=0)
bestLabel.grid(column=4, row=0)
fm1.configure(background='#faf8ef')
fm1.pack(pady=10, side=tk.TOP)

#2048核心内容
list = [[0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0],
    ]
init21, init22 = random.randint(0, 15), random.randint(0, 15)
while(init21 == init22):
    init22 = random.randint(0, 15)

cells = []
index=0
fm2=tk.Frame(root)
for i in range(4):
    for j in range(4):
        text = ''
        bg='#bbada0'
        relief = tk.RIDGE
        if (index == init21 or index == init22):
            text = 2
            bg='#eee4da'
            relief=tk.RAISED
            list[i][j] = 2
        cell=tk.Label(fm2, text=text, font=('Arial', 16), bg=bg, fg='#776e65', width=4, height=2, relief=relief)
        cell.grid(column=j, row=i, padx=2, pady=2)
        cells.append(cell)
        index += 1

fm2.configure(background='#bbada0')
fm2.pack(pady=15, side=tk.TOP)

#调试打印函数
def printList():
    for i in range(4):
        print(list[i])
    print("===========")

#右旋转矩阵
def turnRight(matrix):
    newMatrix=[]
    for column in range(len(matrix[0])):
        newRow = []
        for row in range(len(matrix)-1, -1, -1):
            newRow.append(matrix[row][column])
        newMatrix.append(newRow)
    return newMatrix

#左旋转矩阵
def turnLeft(matrix):
    newMatrix=[]
    for column in range(len(matrix[0])-1, -1, -1):
        newRow=[]
        for row in range(len(matrix)):
            newRow.append(matrix[row][column])
        newMatrix.append(newRow)
    return newMatrix

#随机出现2
def randomCell():
    while True:
        index = random.randint(0, 15)
        row = index // 4
        column = index % 4
        if list[row][column] == 0:
            list[row][column] = 2
            break

#判断矩阵是否已经不能挪动
def isFull(matrix):
    for column in range(len(matrix[0])):
        for row in range(len(matrix)):
            if matrix[row][column] == 0:
                return False
    for row in range(len(matrix) - 1):
        for column in range(len(matrix[0])):
            if matrix[row][column] == matrix[row+1][column]:
                return False
    for row in range(len(matrix)):
        for column in range(len(matrix[0]) - 1):
            if matrix[row][column] == matrix[row][column+1]:
                return False
    return True

#绘制矩阵表格
def draw():
    for i in range(4):
        for j in range(4):
            index = i * 4 + j
            text = list[i][j]
            fg='#776e65'
            relief=tk.RAISED
            if text == 0:
                bg='#bbada0'
                relief = tk.RIDGE
                text = ''
            if text ==  2:
                bg='#eee4da'
            elif text == 4:
                bg='#ede0c8'
            elif text == 8:
                bg='#f2b179'
                fg='#f9f6f2'
            elif text == 16:
                bg='#f59563'
                fg='#f9f6f2'
            elif text == 32:
                bg='#f67c5f'
                fg='#f9f6f2'
            elif text == 64:
                bg='#f65e3b'
                fg='#f9f6f2'
            elif text == 128:
                bg='#edcf72'
                fg='#f9f6f2'
            elif text == 256:
                bg='#edcc61'
                fg='#f9f6f2'
            elif text == 512:
                bg='#edc850'
                fg='#f9f6f2'
            elif text == 1024:
                bg='#edc53f'
                fg='#f9f6f2'
            elif text == 2048:
                bg='#edc22e'
                fg='f9f6f2'
            cells[index].config(text=text, relief=relief, bg=bg, fg=fg)

#处理向上的按键
def keyUp():
    mov,score = False, 0
    for i in range(3):
        for j in range(4):
            if list[i][j] != 0:
                r,b = 1,False
                while (i + r < 4):
                    if list[i+r][j] != 0:
                        b = True
                        break
                    r += 1
                #print("i:%d, j:%d, b:%s %s" % (i,j,b, list[i]))
                if b and list[i][j] == list[i+r][j]:
                    list[i][j] += list[i+r][j]
                    list[i+r][j] = 0
                    score += list[i][j]
                    mov = True
    for i in range(3):
        for j in range(4):
            if list[i][j] == 0:
                r = 1
                while i + r < 4 and list[i][j] == 0:
                    #print('-> %d, %d, %d, %d' % (i, j, r, list[i+r][j]))
                    list[i][j], list[i+r][j] = list[i+r][j], 0
                    r += 1
                if list[i][j] != 0:
                    mov = True
    return (mov, score)

#处理向下的按键
def keyDown():
    mov,score = False, 0
    for i in range(3, 0, -1):
        #print(">>>> row:%d %s" % (i, list[i]))
        for j in range(4):
            if list[i][j] != 0:
                r,b = 1,False
                while (i - r >= 0):
                    #print("process i:%d, j:%d, r:%d %s" % (i,j,r, list[i-r]))
                    if list[i-r][j] != 0:
                        b = True
                        break
                    r += 1
                #print("i:%d, j:%d, b:%s" % (i,j,b))
                if b and list[i][j] == list[i-r][j]:
                    list[i][j] += list[i-r][j]
                    list[i-r][j] = 0
                    score += list[i][j]
                    mov = True
    for i in range(3, 0, -1):
        for j in range(4):
            if list[i][j] == 0:
                r = 1
                while (i - r >= 0 and list[i][j] == 0):
                    #print('-> %d, %d, %d, %d' % (i, j, r, list[i][j]))
                    list[i][j], list[i-r][j] = list[i-r][j], 0
                    r += 1
                if list[i][j] != 0:
                    mov = True
    return (mov, score)

#处理向左的按键
def keyLeft():
    global  list
    list=turnRight(list)
    r = keyUp()
    list=turnLeft(list)
    return r

#处理向右的按键
def keyRight():
    global  list
    list=turnRight(list)
    r = keyDown()
    list=turnLeft(list)
    return r

#按键处理函数
globalScore = 0
def onKeyDown(event):
    global globalScore
    mov,score =  False, 0
    if event.keysym == 'Up':
        mov,score = keyUp()
    elif event.keysym == 'Down':
        mov,score = keyDown()
    elif event.keysym == 'Left':
        mov,score = keyLeft()
    elif event.keysym == 'Right':
        mov,score = keyRight()
    if mov:
        randomCell()
    if (not mov) and isFull(list):
        r = messagebox.askokcancel('提示', 'Game Over :(，Play Again^_^？')
        print('choice:', r)
        if r:
            pass
        else:
            return
    printList()
    draw()
    globalScore+=score
    scoreLabel.config(text='SCORE\n%d'%globalScore)

    

root.bind('<Left>', onKeyDown)
root.bind('<Up>', onKeyDown)
root.bind('<Right>', onKeyDown)
root.bind('<Down>', onKeyDown)
printList()

# 注意，这时候窗口还是不会显示的...
# 除非执行下面的这条代码！！！！！
root.mainloop()
