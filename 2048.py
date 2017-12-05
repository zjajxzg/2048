#-*- coding:utf-8 -*-
import random

score = 0

def display(arr):
    for i in range(len(arr)):
        print arr[i]
    return arr

def init():
    arr = ([0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0])
    flag = 0
    while flag < 2:
        x = random.randint(0, 3)
        y = random.randint(0, 3)
        if arr[x][y] == 0:
            arr[x][y] =2
            flag += 1
    return arr


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

def up(key,arr):
    global  score
    if key == 'w':
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

def down(key,arr):
    global score
    if key == 's':
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

def left(key,arr):
    global score
    if key == 'd':
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

def right(key,arr):
    global score
    if key == 'a':
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
    flag = True
    while flag:
        arr = display(arr)
        print 'your score now :%d' %(score)
        key = raw_input('please input a direction ,w=up,a=left,s=down,d=right:')
        if 'q' == key:
            flag = False
        elif overCheck(arr) == 16:
            flag = False
            print 'game over!'
        else:
            arr = up(key,arr)
            arr = down(key,arr)
            arr = left(key,arr)
            arr = right(key,arr)


if __name__ == '__main__':
    main()
