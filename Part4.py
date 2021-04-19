import serial
import matplotlib.pyplot as plt
from drawnow import *

Data1 = []


def PlotSignal():
    plt.ylim(0, 1200)
    plt.title('Plotting in Streaming AD0 from Arduino')
    plt.grid(True)
    plt.ylabel('Analog Signal AD0')
    plt.plot(Data1, 'r', label='Digital Signal')
    plt.legend(loc='upper right')


if __name__ == '__main__':

    ser = serial.Serial('COM4', 9600)
    plt.ion()
    dCounter = 0
    ser.flush()

    while True:
        while ser.inWaiting() == 0:
            pass  # do nothing if no incoming data

        ardData = ser.readline().decode('utf-8')
        InputData = ardData.split(',')
        temp = float(InputData[0])
        Data1.append(temp)

        drawnow(PlotSignal)
        plt.pause(0.000001)
        dCounter = dCounter + 1
        if dCounter > 60:
            dCounter = 0
        Data1.pop(0)

    ser.close()
