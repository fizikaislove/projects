import matplotlib.pyplot as plt
import matplotlib.image as img
from PIL import Image, ImageDraw
import numpy as np

fig = plt.figure(1)
Capture = img.imread("Image5.jpg")



x_left = list()
x_right = list()

x_c1=list()
x_c2=list()
left_or_right = True
def calculate(x1,x2):
    x1=np.asarray(x_left)
    x2=np.asarray(x_right)
    distance = [np.linalg.norm(x) for x in x1-x2]
    q=np.linspace(0,100,1000)
    # line.set_data(q,2*q+1)


def draw_line(x1,x2):
    w=list()
    y=list()
    for n in range(len(x1)):
        w.append(np.linspace(x2[n][0],x1[n][0],100))
        y.append((-1)*((x1[n][1]-x2[n][1])*w[n]+x1[n][0]*x2[n][1]
                -x2[n][0]*x1[n][1])/(x2[n][0]-x1[n][0]))
    line.set_data(w,y)
    line.figure.canvas.draw()


def onclick(event):
    global left_or_right,x_left,x_right
    print(event.button)
    if event.button==3:
        if left_or_right is True:
            print("levo")
            left_or_right = False
            x_left.append([event.xdata,event.ydata])
        else:
            print("pravo")
            left_or_right = True
            x_right.append([event.xdata,event.ydata])
            draw_line(x_left,x_right)
            # calculate(x_left,x_right)
    elif event.button==2:
        print("privet")
    else:
        print("This action  ")

picture = plt.imshow(Capture)
ax = fig.add_subplot(111)
line, = ax.plot([0], [0],'ro',lw=0.2)
picture.figure.canvas.mpl_connect('button_press_event', onclick)
plt.show()
