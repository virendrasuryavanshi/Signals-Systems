import matplotlib.pyplot as plt
import numpy as np
import math
import pylab

def unit_step(t):
    y = []
    for x in t:
        if (x >= 0 and x <= 2):
            y.append(1)
        else:
            y.append(0)
    return np.array(y)

def q1():
    t = np.arange(-5,5,0.001)
    y = np.sin(t)
    plt.figure()
    plt.title("Sinusoidal")
    plt.plot(t,y)
    plt.show()

    y = unit_step(t)
    plt.figure()
    plt.title("Unit Step function")
    plt.plot(t,y)
    plt.show()

    y = np.exp(t)
    plt.figure()
    plt.title("Exponential")
    plt.plot(t,y)
    plt.show()

def part1():
    t = np.arange(-5,5,0.001)
    y = np.array(-unit_step(t))
    y2 = 2*np.exp(-unit_step(t))
    y3 = 3*np.exp(-unit_step(t))
    y4 = np.exp(-(2*unit_step(t) + 3*unit_step(t)))
    plt.figure()
    plt.title("Linearity of y = exp(-x(t))")
    plt.plot( t,y4,label='y(t) = T(x3(t))')
    plt.plot(t,(y2+y3),"r--",label='ay1(t)+by2(t)')
    plt.legend(loc='upper left')
    plt.show()

    x = unit_step(t-0.3)
    y = np.exp(-x)
    y1 = np.exp(-unit_step(t-0.3))
    plt.figure()
    plt.title("Time invariance of y = exp(-x(t))")
    plt.plot( t,y1,label='y = T(x(arg(x(t))-t0))')
    plt.plot(t,y,"r--" , label='y(t-t0)')
    plt.legend(loc='upper left')
    plt.show()

def part2():
    t = np.arange(-5,5,0.001)
    y2 = 2*unit_step(2*t)
    y3 = 3*unit_step(2*t)
    y4 = (2*unit_step(2*t) + 3*unit_step(2*t))
    plt.figure()
    plt.title("Linearity of y = x(2t)")
    plt.plot( t,y4,label='y(t) = T(x3(t))')
    plt.plot(t,(y2+y3),"r--",label='ay1(t)+by2(t)')
    plt.legend(loc='upper left')
    plt.show()

    y = unit_step(2*(t-0.3))
    y1 = unit_step(2*t-0.3)
    plt.figure()
    plt.plot( t,y1,label='y = T(x(t-t0))')
    plt.plot(t,y,"r--" , label='y = T(x(arg(x(t))-t0))')
    plt.legend(loc='upper left')
    plt.show()

def part3():
    t = np.arange(-5,5,0.001)
    y2 = 2* ( unit_step(t-1) + unit_step(-t-1) )
    y3 = 3* ( unit_step(t-1) + unit_step(-t-1) )
    y4 = 2*unit_step(t-1) + 3*unit_step(t-1) + 2*unit_step(-t-1) + 3*unit_step(-t-1)
    plt.figure()
    plt.title("Linearity of y = x(t-1) + x(-t-1)")
    plt.plot( t,y4,label='y(t) = T(x3(t))')
    plt.plot(t,(y2+y3),"r--",label='ay1(t)+by2(t)')
    plt.legend(loc='upper left')
    plt.show()

    y = unit_step(t-1-0.3) + unit_step(-(t-0.3)-1)
    y1 = unit_step(t-1-0.3) + unit_step(-t-1-0.3)
    plt.figure()
    plt.title("Time invariance of y = x(t-1) + x(-t-1)")
    plt.plot( t,y1,label='y = T(x(arg(t)-t0))')
    plt.plot(t,y,"r--" , label='y(t-t0)')
    plt.legend(loc='upper left')
    plt.show()

q1()
part1()
part2()
part3()
