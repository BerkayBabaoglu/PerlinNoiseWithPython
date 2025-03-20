import numpy as np
import matplotlib.pyplot as plt
from noise import snoise2

width,height = 100,100 #size of the noise map
scale = 10.0 #scale of the noise
octaves = 6 #number of octaves
persistence = 0.5  # persistence
lacunarity = 2.0  #lacunarity

noise_array = np.zeros((width,height))

#generate
for y in range(height):
    for x in range(width):
        noise_array[y][x] = snoise2(x / scale,
                                    y/ scale,
                                    octaves=octaves,
                                    persistence=persistence,
                                    lacunarity=lacunarity)



plt.imshow(noise_array, cmap='gray')
plt.colorbar()
plt.title("2d perlin noise")
plt.show()

