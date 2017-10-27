import matplotlib.pyplot as plt
import matplotlib.image as img
import numpy as np


x_left = list()
x_right = list()
left_or_right = True
tranform_coef=10
def plot_histogram(x):
    fig2=plt.figure(2)
    plt.hist(x)
    plt.show()
    fig2.savefig("histogramma.jpg")

def calculate(x1,x2):
    x1=np.asarray(x_left)
    x2=np.asarray(x_right)
    distance = [np.linalg.norm(x)/tranform_coef for x in x1-x2]
    plot_histogram(distance)
    words = [str(y)+'\n' for y in distance]
    data = open("data_for_histogram.txt",'w')
    data.writelines(words)
    data.close()


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
            left_or_right = False
            x_left.append([event.xdata,event.ydata])
        else:
            left_or_right = True
            x_right.append([event.xdata,event.ydata])
            draw_line(x_left,x_right)
    elif event.button==2:
        calculate(x_left,x_right)
    else:
        print("This action doesn't do anything ")



fig = plt.figure(1)
Capture = img.imread("Image5.jpg")
picture = plt.imshow(Capture)
ax = fig.add_subplot(111)
line, = ax.plot([], [],'ro',lw=0.2)
picture.figure.canvas.mpl_connect('button_press_event', onclick)

plt.show()
