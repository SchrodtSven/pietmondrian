import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import pandas as pd

class Gfx:
    '''
    Graphical functionalty for geometric Mondrian painting 
    '''
    fgsze=(4, 4)

    def __init__(self, file='dta/mondrian-painting-features.csv'):
        self.features = pd.read_csv(file)

    def show_pic(self, id):


        rects = self.features.query('painting_id == @id')
        total_width = rects.eval("x + width").max()
        total_height = rects.eval("y + height").max()
        
        fig, ax = plt.subplots(figsize=self.fgsze)
        #fig, ax = plt.subplots(figsize=(3, 3))
        
        for (idx, row) in rects.iterrows():
            x, y, w, h, rgb = row[['x','y','width','height','rgb']]
            patch = mpatches.Rectangle((x, y), w, h, facecolor=rgb)
            ax.add_patch(patch)
        
        ax.axis([0, total_width, 0, total_height])
        ax.set_aspect('equal')
        ax.axis('off')
        fig.text(0.5, 0.01, id, ha="center", fontsize=14)
        plt.show()

if __name__ == '__main__':
    gfx = Gfx()
    gfx.show_pic('b105')
