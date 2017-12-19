'''
作者：snake
功能：五角星绘制
日期：12/16/2017
'''

import turtle

def onepentagram(lenth):
    for count in range(5):
        turtle.forward(lenth)
        turtle.right(144)

def main():
    '''
    主函数
    :return:
    '''
    lenth = 50
    while lenth <= 150:
        onepentagram(lenth)
        lenth += 20
    turtle.penup()
    onepentagram(lenth)
    turtle.exitonclick()

if __name__ == '__main__':
    main()