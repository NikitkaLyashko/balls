import random

import wrap
import wrap_py
from wrap import  sprite

@wrap.always(delay=1000)
def balls():
    global  p,ball
    # wrap.sprite_text.set_text(balls_on_face_1, "столько создается в секунду:" + str(m))
    for n in range(m):
        x = random.randint(0, 500)
        y = random.randint(0, 500)
        speed_x = random.randint(-5, 5)
        speed_y = random.randint(1, 5)
        size = random.randint(5, 16)
        costume_in_list = random.choice(costume)
        ball=sprite.add("balls__2",x,y,costume_in_list)
        sprite.set_size(ball,size,size)

        a={"id":ball,"size":size,"speed_x":speed_x,"speed_y":speed_y,"g":0}
        a_lot_of_ball.append(a)

        wrap.sprite.move_left_to(balls_on_face, 0)
        wrap.sprite.move_left_to(balls_on_face_1, 0)

    wrap.sprite_text.set_text(balls_on_face, "на экране столько шариков:" + str(len(a_lot_of_ball)))




@wrap.on_key_down(wrap.K_1)
def stop():
    global mode
    mode="stop"
    
@wrap.on_key_down(wrap.K_3)
def next_fly():
    global mode
    mode="fly"

@wrap.on_key_down(wrap.K_2)
def drops():
    global mode
    mode="fall"









calculator=0
@wrap.on_key_down(wrap.K_e)
def e_title():
    global calculator
    calculator += 1
    for in_list_drow in list_drow:
        wrap.sprite.hide(in_list_drow)
        if calculator%2==0:
            wrap.sprite.show(in_list_drow)



@wrap.on_key_down(wrap.K_UP)
def key_up():
    global m
    m+=1
    wrap.sprite_text.set_text(balls_on_face_1, "столько создается в секунду:"+ str(m))



@wrap.on_key_down(wrap.K_DOWN)
def key_down():
    global m
    m-=1
    if m<=0:
        m=0
    wrap.sprite_text.set_text(balls_on_face_1, "столько создается в секунду:" + str(m))

@wrap.on_key_down(wrap.K_DELETE)
def key_delete():
    global m
    for sprits in a_lot_of_ball:
        wrap.sprite.remove(sprits["id"])
    a_lot_of_ball.clear()
    wrap.sprite_text.set_text(balls_on_face, "на экране столько шариков:" + str(0))

def drow(costum):
    global y
    y += 15
    balls_on_face=wrap.sprite.add_text(costum, 1, y, text_color=[110, 255, 32])
    wrap.sprite.move_left_to(balls_on_face, 0)
    list_drow.append(balls_on_face)


    return balls_on_face





wrap.world.create_world(500,500)
wrap.add_sprite_dir("balls")
a_lot_of_ball=[]
list_drow = []
costume =["blue","red","green"]
m=0
y=0

mode="fly"

drow("E: скрыть показать детали:" )
balls_on_face=drow("на экране столько шариков:" + str(len(a_lot_of_ball)))
balls_on_face_1=drow("столько создается в секунду"+str(m))
drow("Del: удалить элементы с экрана" )
drow("1 - это остановка")
drow("2- это падение")
drow("3- это свободный полет")



@wrap.always(delay=10)
def fly():
    global speed_x
    if mode=="fly":
        for clov_in_lict in a_lot_of_ball:


            sprite.move(clov_in_lict["id"],clov_in_lict["speed_x"],clov_in_lict["speed_y"])

            right_ball=sprite.get_right(clov_in_lict["id"])
            if right_ball>=500:
                clov_in_lict["speed_x"]=-clov_in_lict["speed_x"]

            left_ball=sprite.get_left(clov_in_lict["id"])
            if left_ball<=0:
                clov_in_lict["speed_x"]=-clov_in_lict["speed_x"]

            top_ball=sprite.get_top(clov_in_lict["id"])
            if top_ball<0:
                clov_in_lict["speed_y"]=-clov_in_lict["speed_y"]

            bottom_ball=wrap.sprite.get_bottom(clov_in_lict["id"])
            if bottom_ball>500:
                clov_in_lict["speed_y"]=-clov_in_lict["speed_y"]


@wrap.always(delay=10)
def dropping():
    if mode=="fall":
        print(a_lot_of_ball[0]["g"])
        for abc in a_lot_of_ball:
            bot_id=wrap.sprite.get_bottom(abc["id"])

            if bot_id>=500:
                wrap.sprite.move_bottom_to(abc["id"],500)
                if abc["g"]<0.5:
                    abc["g"]=0
                else:
                    abc["g"]=-abc["g"]*0.8
            else:

                abc["g"]+=0.1
            wrap.sprite.move(abc["id"], 0, abc["g"])

























import wrap_py
wrap_py.app.start()