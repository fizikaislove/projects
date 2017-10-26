import matplotlib.pyplot as plt
import matplotlib.image as img
import numpy as np


x_left = list()
x_right = list()
left_or_right = True
tranform_coef=100

def plot_histogram(x):
    fig2=plt.figure(2)
    plt.hist(x)
    plt.show()
    fig2.savefig("histogramma.jpg")

def calculate(x1,x2):
    x1=np.asarray(x_left)
    x2=np.asarray(x_right)
    distance = [np.linalg.norm(x) for x in x1-x2]
    plot_histogram(distance)
    # plot_histogram(distance*tranform_coef)


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
    elif event.button==2:
        print("privet")
        calculate(x_left,x_right)

    else:
        print("This action doesn't do anything ")



fig = plt.figure(1)
Capture = img.imread("Image5.jpg")
picture = plt.imshow(Capture)
ax = fig.add_subplot(111)
line, = ax.plot([0], [0],'ro',lw=0.2)
picture.figure.canvas.mpl_connect('button_press_event', onclick)

# fig2= plt.figure(2)
# ax2 = fig2.add_subplot(111)
# line1,=ax2.plot([],[])

plt.show()
