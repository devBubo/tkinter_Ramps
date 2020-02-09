'''from tkinter import *
            root=Canvas()
            root.pack()
            winx=800
            winy=600
            root.config(width=winx,height=winy,bg='black')
            x=400
            y=400
            š=100
            v=100
            velx=10
            vely=10
            dx=velx
            dy=vely

            x1=300
            y1=200
            x2=450
            y2=350
            count=0
            fontsize=50

            text=root.create_text(winx - 50, winy - 20, fill='white', text=count,font=fontsize)

            while True:
                player=root.create_oval(x,y,x+š,y+v,fill='white')
                root.update()

                root.after(30)
                root.delete(player)
                x+=dx
                y+=dy
                if x >= winx-š:
                    dx=-velx
                elif x<=0:
                    dx=velx
                if y >=winy-v:
                    dy=-vely
                elif y <=0:
                    dy=vely
                if x==winx-š and y==winy-v:
                    count+=1
                    root.delete(text)
                    text=root.create_text(winx - 50, winy - 20, fill='white', text=count,font=fontsize)
                elif x==0 and y==0:
                    count += 1
                    root.delete(text)
                    text = root.create_text(winx - 50, winy - 20, fill='white', text=count,font=fontsize)
                elif x==winx-š and y==0:
                    count += 1
                    root.delete(text)
                    text = root.create_text(winx - 50, winy - 20, fill='white', text=count,font=fontsize)
                elif x==0 and y>=winy-v:
                    count += 1
                    root.delete(text)
                    text = root.create_text(winx - 50, winy - 20, fill='white', text=count,font=fontsize)
                    print(x,y)
                print('x', x,'y',y,count)

            root.mainloop()

            from tkinter import *
            def motion():
                  if var_pohyb==1:
                       root.move(player, 0, -10)
                  elif var_pohyb==3:
                       root.move(player, 0, 10)
                  elif var_pohyb==0:
                       root.move(player, 10, 0)
                  elif var_pohyb==2:
                       root.move(player, -10, 0)
                  elif var_pohyb==6:
                      print('Hi')
                  root.after (50, motion)
            def arrows (event):
                global var_pohyb
                if event.keysym=='Up':
                      var_pohyb=1
                elif event.keysym=='Down':
                      var_pohyb=3
                elif event.keysym=='Right':
                      var_pohyb=0
                elif event.keysym=='Left':
                      var_pohyb=2
                elif not(event.keysym):
                    var_pohyb=6
            root=Canvas (width=800, height=800)
            root.pack ()
            player=root.create_oval(100, 100, 150, 150)
            var_pohyb=5
            motion ()
            root.bind_all ('<Key>', arrows)

            root.mainloop()'''
from tkinter import *
import random
from tkinter import messagebox
winx=1000
winy=600
root = Canvas()
root.config(width=winx, height=winy,bg='#000040')
root.pack()


strela_x = 0
strela_y = 0
color = "#bcbcbc"
velx=15
score=0
vel_strela=10
sirka_rampy=100
vyska_rampy=50
r_strela=30
rampa_x = winx/2
rampa_y = winy-vyska_rampy

def rampa():
    global rectangle
    root.delete("all")
    rectangle=root.create_rectangle(rampa_x, rampa_y, rampa_x + sirka_rampy, rampa_y + vyska_rampy, fill=color, outline="")


def strela():
    strela=root.create_oval(strela_x, strela_y, strela_x + r_strela, strela_y + r_strela, fill="red")

def počítač_skóre():
    počítač_skóre=root.create_text(winx-30, 20, font="Times 20 italic bold", text=str(score),fill='#ffffff')

def vsetko():
    root.delete("all")
    rampa()
    počítač_skóre()
    #vymaže jestli se přešlo rampou
    if strela_y<winy-r_strela-vel_strela:
        strela()
    else:
        root.delete(strela)



def right(e):
    global rampa_x
    if rampa_x<winx-sirka_rampy:
        rampa_x = rampa_x + velx
    vsetko()


def left(e):
    global rampa_x
    if rampa_x>0:
        rampa_x = rampa_x - velx
    vsetko()

root.bind_all("<Right>", right)
root.bind_all("<Left>", left)
rampa()

while True:

    strela_x = random.randint(0, winx - r_strela)
    while strela_y < winy - r_strela:
        #pohybuje vertikalně střelu
        strela_y = strela_y + vel_strela

        #Jestli trefí rampu
        if rampa_x < strela_x + r_strela and rampa_x + sirka_rampy > strela_x and strela_y + r_strela > rampa_y:
            score+=1
            vel_strela+=0.1
            strela_x=random.randint(0,winx-r_strela)
            strela_y=0
        vsetko()
        root.update()
        root.after(50)
        if ((rampa_x > strela_x + r_strela and rampa_y < strela_y + r_strela) or (rampa_x + sirka_rampy < strela_x and rampa_y < strela_y + r_strela)):
            messagebox.showinfo("Game", "Prohra byla sladká")
            root.delete('all')
            root.create_text(winx/2,winy/2,font="Times 70 italic bold",text='Tvé skóre je '+str(score),fill='#ffffff')

        root.update()
        root.after(5)


