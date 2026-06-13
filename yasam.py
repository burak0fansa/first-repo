#MATRİS = SÜTUN VE SATIRDAN OLUŞAN TABLO

#EĞER Bİ YERDE MATRİS VARSA NUMPY

#IZGARA= GRİD >> ARKAPLANIN KARESEL OLMASI

#0 ölü hücre, 1 canlı hücre

import numpy as np
import matplotlib.pyplot as plt

import matplotlib.animation as animation



N= 50

ON= 255
OFF= 0

#[255,0]  p[0.2, 0.8] >>>> N*N

grid= np.random.choice([ON, OFF], N*N, p= [0.2,0.8]).reshape(N,N)


def update(frameNum, img, grid, N):
    new_grid= grid.copy()

    for i in range (N):  #SATIR- SÜTUN OLAYINI ÇÖZERİZ.
        for j in range(N):
            total = int((grid[i, (j - 1) % N] + grid[i, (j + 1) % N] +

                         grid[(i - 1) % N, j] + grid[(i + 1) % N, j] +

                         grid[(i - 1) % N, (j - 1) % N] +

                         grid[(i - 1) % N, (j + 1) % N] +

                         grid[(i + 1) % N, (j - 1) % N] + grid[(i + 1) % N, (j + 1) % N]) / 255)

            if grid[i,j]== ON:
                if (total<2) or (total>3):
                    new_grid[i,j]=OFF

            else:
                if total==3:
                    new_grid[i,j]= ON



    img.set_data(new_grid)
    grid[:] = new_grid[:]
    return img

fig, ax= plt.subplots()
img= ax.imshow(grid, interpolation= 'nearest', cmap='magma')

ani= animation.FuncAnimation (fig, update, fargs=(img,grid,N), frames=10, interval=10, save_count=50)

plt.show()












































