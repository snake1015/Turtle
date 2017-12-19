'''
   作者：SNAKE
   功能：用递归绘制分形树
   版本：1.0
   日期：17/12/2017
'''

import turtle

def draw_fractaltree(brach_lenth):
    '''
    绘制分形树方法
    '''
    if brach_lenth >= 5:
        #print(brach_lenth)
        if brach_lenth - 10 < 5:
            turtle.color('green')
        else:
            turtle.color('brown')
        #向前绘制树枝
        turtle.forward(brach_lenth)
        #向右绘制树权
        turtle.right(20)
        draw_fractaltree(brach_lenth - 10)

        #向左绘制树枝
        turtle.left(40)
        draw_fractaltree(brach_lenth - 10)

        #回到前一个节点
        turtle.right(20)
        turtle.penup()
        turtle.backward(brach_lenth)
        turtle.pendown()

def main():
    '''
    主函数
    :return:
    '''

    turtle.left(90)
    turtle.penup()
    turtle.backward(100)
    turtle.pendown()
    #turtle.color('brown')
    draw_fractaltree(80)
    turtle.exitonclick()

if __name__ == '__main__':
    main()