#-*- coding:utf-8 -*-
from Tkinter import *
from tkMessageBox import *
import random

score = 0             #分数
root = Tk()           #创建窗口对象
root.wm_title('2048简易版')             #标题
root.resizable(width = False,height = False)     #窗口大小设为不可变

def init():
    arr = ([0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0])
    flag = 0
    while flag < 2:
        x = random.randint(0, 3)
        y = random.randint(0, 3)
        if arr[x][y] == 0:
            arr[x][y] = 2
            flag += 1
    return arr


def display(arr):
    for i in range(4):
        for j in range(4):
            if arr[i][j] == 0:
                Button(root,text = arr[i][j],width = 8,height = 3,bg = '#FFFFF0').grid(row = i,column = j)
            elif arr[i][j] == 2:
                Button(root,text = arr[i][j],width = 8,height = 3,bg = '#FFEC8B').grid(row = i,column = j)
            elif arr[i][j] == 4:
                Button(root,text = arr[i][j],width = 8,height = 3,bg = '#FFE7BA').grid(row = i,column = j)
            elif arr[i][j] == 8:
                Button(root,text = arr[i][j],width = 8,height = 3,bg = '#FFE1FF').grid(row = i,column  =j)
            elif arr[i][j] == 16:
                Button(root,text = arr[i][j],width = 8,height = 3,bg = '#FFD39B').grid(row = i,column  =j)
            elif arr[i][j] == 32:
                Button(root,text = arr[i][j],width = 8,height = 3,bg = '#FFBBFF').grid(row = i,column  =j)
            elif arr[i][j] == 64:
                Button(root,text = arr[i][j],width = 8,height = 3,bg = '#FFAEB9').grid(row = i,column  =j)
            elif arr[i][j] == 128:
                Button(root,text = arr[i][j],width = 8,height = 3,bg = '#FF8C69').grid(row = i,column  =j)
            elif arr[i][j] == 256:
                Button(root,text = arr[i][j],width = 8,height = 3,bg = '#FF8247').grid(row = i,column  =j)
            elif arr[i][j] == 512:
                Button(root,text = arr[i][j],width = 8,height = 3,bg = '#FF7256').grid(row = i,column  =j)
            elif arr[i][j] == 1024:
                Button(root,text = arr[i][j],width = 8,height = 3,bg = '#FF6347').grid(row = i,column  =j)
            else:
                Button(root,text = arr[i][j],width = 8,height = 3,bg = '#FF0000').grid(row = i,column  =j)

def add_random(arr):
    list = []
    for i in range(4):
        for j in range(4):
            if arr[i][j] == 0:
                list.append((i,j))
    #print list
    adress  = random.choice(list)
    #print adress
    arr[adress[0]][adress[1]] = 2
    display(arr)

def up(event,arr):
    global  score
    list = []
    for i in range(4):
        for j in range(3):
            for k in range(j+1,4):
                if arr[j][i] == 0:
                    arr[j][i],arr[k][i] = arr[k][i],arr[j][i]
                elif arr[j][i] == arr[k][i]:
                    arr[j][i] = 2*arr[j][i]
                    arr[k][i] = 0
                    score += arr[j][i]
    add_random(arr)
    return arr

def down(event,arr):
    global score
    for i in range(4):
        for j in range(3,0,-1):
            for k in range(j-1,-1,-1):
                if arr[j][i] == 0:
                    arr[j][i],arr[k][i] = arr[k][i],arr[j][i]
                elif arr[j][i] == arr[k][i]:
                    arr[j][i] = 2*arr[j][i]
                    arr[k][i] = 0
                    score += arr[j][i]
    add_random(arr)
    return arr

def right(event,arr):
    global score
    for j in range(4):
        for i in range(3, 0, -1):
            for k in range(i - 1, -1, -1):
                if arr[j][i] == 0:
                    arr[j][i], arr[j][k] = arr[j][k], arr[j][i]
                elif arr[j][i] == arr[j][k]:
                    arr[j][i] = 2 * arr[j][i]
                    arr[j][k] = 0
                    score += arr[j][i]
    add_random(arr)
    return arr

def left(event,arr):
    global score
    for j in range(4):
        for i in range(3):
            for k in range(i+1,4):
                if arr[j][i] == 0:
                    arr[j][i], arr[j][k] = arr[j][k], arr[j][i]
                elif arr[j][i] == arr[j][k]:
                    arr[j][i] = 2 * arr[j][i]
                    arr[j][k] = 0
                    score += arr[j][i]
    add_random(arr)
    return arr

def overCheck(arr):
    count = 0
    for i in range(4):
        for j in range(4):
            if arr[i][j] != 0:
                count+=1
    return count

def main():
    global score
    arr = init()
    display(arr)
    print arr
    root.bind('<Up>', lambda event: up(event, arr))  # 绑定事件，回调函数，这里要注意用lambda匿名函数来传参数，event是默认要传的
    root.bind('<Down>', lambda event: down(event, arr))
    root.bind('<Right>', lambda event: right(event, arr))
    root.bind('<Left>', lambda event: left(event, arr))
    # print arr
    # display(arr)
    root.mainloop()

if __name__ == '__main__':
    main()

