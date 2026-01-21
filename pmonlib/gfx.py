# Graphical functionality
#
# AUTHOR Sven Schrodt
# SINCE 2026-01-16

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import pandas as pd
from pmonlib.provider import Provider

class Gfx:
    '''
    Graphical functionalty for geometric Mondrian paintings
    '''
    fgsze=(3, 3)

    def __init__(self, file='dta/feature.csv'):
        '''
        Docstring für __init__
        
        :param self: Beschreibung
        :param file: Beschreibung
        '''
        self.features = pd.read_csv(file)
        self.provider = Provider()

    def get_pic(self, id):
        '''
        Docstring für get_pic
        
        :param self: Beschreibung
        :param id: Beschreibung
        '''

        rects = self.features.query('id == @id')
        total_width = rects.eval("x + w").max()
        total_height = rects.eval("y + h").max()
        
        fig, ax = plt.subplots(figsize=self.fgsze)
        #fig, ax = plt.subplots(figsize=(6,6))
        
        #print([fig, ax, type(fig), type(ax)])
        #exit()

        for (idx, row) in rects.iterrows():
            x, y, w, h, rgb = row[['x','y','w','h','rgb']]
            patch = mpatches.Rectangle((x, y), w, h, facecolor=rgb)
            ax.add_patch(patch)
        
        ax.axis([0, total_width, 0, total_height])
        ax.set_aspect('equal')
        ax.axis('off')
        title = self.provider.info_attr_by_id(id, 'title')
        fig.text(0.05, 0.05, f'» {title} « ({id})', ha="left", fontsize=12)
        #fig.text(0.5, 0.01, f'By Piet Mondrian', ha="center", fontsize=12)
        return fig


    def show_pic(self, id):
        #print(type(fig))
        fig = self.get_pic(id)
        plt.show()

if __name__ == '__main__':
    gfx = Gfx()
    fig = gfx.get_pic('b105')
    fig.savefig(fname='foo.svg', format='svg')
