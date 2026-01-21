# Graphical functionality
#
# AUTHOR Sven Schrodt
# SINCE 2026-01-16

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import pandas as pd

class Gfx:
    '''
    Graphical functionalty for geometric Mondrian paintings
    '''
    fgsze=(4, 4)

    def __init__(self, file='dta/feature.csv'):
        self.features = pd.read_csv(file)

    def show_pic(self, id):


        rects = self.features.query('id == @id')
        total_width = rects.eval("x + w").max()
        total_height = rects.eval("y + h").max()
        
        fig, ax = plt.subplots(figsize=self.fgsze)
        #fig, ax = plt.subplots(figsize=(3, 3))
        
        for (idx, row) in rects.iterrows():
            x, y, w, h, rgb = row[['x','y','w','h','rgb']]
            patch = mpatches.Rectangle((x, y), w, h, facecolor=rgb)
            ax.add_patch(patch)
        
        ax.axis([0, total_width, 0, total_height])
        ax.set_aspect('equal')
        ax.axis('off')
        fig.text(0.5, 0.01, id, ha="center", fontsize=14)
        print(type(fig))
        plt.show()

if __name__ == '__main__':
    gfx = Gfx()
    gfx.show_pic('b105')
