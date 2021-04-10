from char_map import get_all_pixels, get_coords

import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np


def getFrequencies(contents):
    """Get the frequencies of certain keypresses in dictionary."""
    heatmapData = np.asarray([[0] * 57] * 21)

    for char in contents:
        coords = get_coords(char)
        if coords:
            for coord in coords:
                x, y = coord
                heatmapData[x][y] += contents[char]

    total = np.sum(heatmapData)
    if total != 0:
        heatmapData = heatmapData / total

    for pixel in get_all_pixels(((18, 18), (19, 34))):
        x, y = pixel
        heatmapData[x][y] *= 0.3

    return heatmapData[::-1]


def blendAndShow(contents):
    """Plot a heatmap, upscale it to the keyboard and show a blended image."""
    heatmapData = getFrequencies(contents)
    img = mpimg.imread('keyboard.png')

    plt.clf()
    plt.xticks([])
    plt.yticks([])
    plt.axis('off')

    plt.imshow(heatmapData, interpolation='lanczos', zorder=1,
               cmap='viridis', alpha=0.8)
    plt.imshow(img, extent=(0, 57, 0, 21))
    plt.show()
