import numpy as np
import numpy.matlib as npm
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import matplotlib as mp

pi = np.pi
DIMENSION = 300
NUMSOURCE = 7
WAVELENGTH = 10
FREQUENCY = 1/WAVELENGTH
SEPARATION = WAVELENGTH/2;
STARTINGLOC = 0.5*DIMENSION - np.round(NUMSOURCE/2)*SEPARATION
LOCATION = 0
PHASE = 2*pi
MPOS = np.zeros(shape=(2, NUMSOURCE))

a = range(DIMENSION)
x = npm.repmat(a, DIMENSION, 1)
canvasFull = np.ndarray(shape=(DIMENSION, DIMENSION, NUMSOURCE))

for i in range(NUMSOURCE):
    y = np.subtract(np.transpose(x), (STARTINGLOC + LOCATION))
    MPOS[1, i] = -(STARTINGLOC + LOCATION)
    LOCATION = LOCATION + SEPARATION
    local_R = np.sqrt(np.add(np.power(x, 2), np.power(y, 2)))
    canvasFull[:, :, i] = local_R


def generate_data(ANGLESHIFT):
    global PHASE
    SUMWAVE = np.zeros(shape=(DIMENSION, DIMENSION))
    for i in range(NUMSOURCE):
        PHASE = PHASE + ANGLESHIFT*pi
        WAVE = np.sin(np.subtract(np.multiply(2*pi*FREQUENCY, canvasFull[:, :, i]), PHASE))
        SUMWAVE = np.add(SUMWAVE, WAVE)

    return SUMWAVE


def update(data):
    mat.set_data(data)
    return mat

def data_gen():
    for ANGLESHIFT in np.arange(0, 10, 0.04):
        yield generate_data(ANGLESHIFT)
        print(ANGLESHIFT)

mp.rc('figure', figsize=(7, 7))
fig, ax = plt.subplots()
ax.scatter(MPOS[0, :], (-1*MPOS[1, :]), s=10, c='red')
ax.set_xlim([-10, DIMENSION])
ax.set_ylim([0, DIMENSION])
mat = ax.matshow(generate_data(0))
plt.colorbar(mat)
ani = animation.FuncAnimation(fig, update, data_gen, interval=10,
                              save_count=100)
plt.show()