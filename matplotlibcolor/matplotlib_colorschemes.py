# matplotlib_colorschemes.py

import yaml
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap

def register_schemes(scheme_path):
    with open(scheme_path) as f:
        schemes = yaml.safe_load(f)

    for scheme in schemes:
        name = scheme['name']
        colors = scheme['colors']
        plt.register_cmap(name=name, cmap=ListedColormap(colors))
