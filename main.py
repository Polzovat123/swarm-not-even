import json

import matplotlib.pyplot as plt
import numpy as np

import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
import numpy as np

def visualize_matrix(matrix):
    colors = ['blue', 'green', 'brown', 'red', 'grey', 'black']
    tick_ship_description = ['water', 'island', 'ship', 'enemy', 'water old', 'island map']
    cmap = ListedColormap(colors)
    bounds = [-0.5, 0.5, 1.5, 2.5, 3.5, 4.5, 5.5]  # Extend bounds for new colors
    norm = plt.Normalize(bounds[0], bounds[-1])

    fig, ax = plt.subplots()
    plt.figure(figsize=(100, 100))
    im = ax.imshow(matrix, cmap=cmap, norm=norm)

    cbar = plt.colorbar(im, ticks=[0, 1, 2, 3, 4, 5], orientation='vertical', fraction=0.046, pad=0.04)
    cbar.set_ticklabels(tick_ship_description)

    ax.grid(which='both', linestyle='-', linewidth=2, color='k', zorder=10)
    ax.set_xticks(np.arange(-0.5, len(matrix[0]), 1))
    ax.set_yticks(np.arange(-0.5, len(matrix), 1))
    ax.set_xticklabels([])
    ax.set_yticklabels([])

    # fig_manager = plt.get_current_fig_manager()
    # fig_manager.full_screen_toggle()

    plt.show()


with open('map.json', 'r') as file:
    json_content = file.read()
    json_map = json.loads(json_content)

height, width = json_map['height'], json_map['width']

matrix = np.zeros((height, width))
visualize_matrix(matrix)
