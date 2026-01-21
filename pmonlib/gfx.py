# Graphical functionality
#
# AUTHOR Sven Schrodt
# SINCE 2026-01-16

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import pandas as pd
from pmonlib.provider import Provider
from pmonlib.cache import Cache


class Gfx:
    """
    Graphical functionalty for geometric Mondrian paintings
    """

    fgsze = (3, 3)
    ftsize = 12
    frame_width = 10
    frame_color = "k"
    format = "svg"
    add_meta = True
    diable_axes = True

    # FIXME
    _cfg = {
        "fgsze": (3, 3),
        "ftsize": 12,
        "frame_width": 10,
        "frame_color": "k",
        "format": "svg",
        "add_meta": True,
        "disable_axes": True,
        # ....
    }

    def __init__(self, file="dta/feature.csv"):
        """
        Initialize (meta) data

        :param self:
        :param file: origin of feature data
        """
        self.features = pd.read_csv(file)
        self.provider = Provider()

    def get_pic(self, id):
        """
        Drawing dynamically created painting with current configuration

        :param self:
        :param id: index of painting
        """

        rects = self.features.query("id == @id")
        full_width = rects.eval("x + w").max()
        full_height = rects.eval("y + h").max()

        fig, ax = plt.subplots(figsize=self.fgsze)

        for idx, row in rects.iterrows():
            x, y, w, h, rgb = row[["x", "y", "w", "h", "rgb"]]
            patch = mpatches.Rectangle((x, y), w, h, facecolor=rgb)
            ax.add_patch(patch)

        ax.axis([0, full_width, 0, full_height])
        ax.set_aspect("auto")
        if self.diable_axes:
            ax.axis("off")

        if self.add_meta:
            title = self.provider.info_attr_by_id(id, "title")
            fig.text(0.05, 0.05, f"» {title} « ({id})", ha="left", fontsize=self.ftsize)

        return fig

    def show_pic(self, idx):
        """
        Show painting

        :param self:
        :param id: ID of painting
        """
        fig = self.get_pic(idx)
        plt.show()

    def save_pic(self, idx):
        """
        Save dynamically created picture

        :param self:
        :param idx: ID of painting
        """
        fig = self.get_pic(idx)
        fig.patch.set_linewidth(self.frame_width)
        fig.patch.set_edgecolor(self.frame_color)
        fig.savefig(fname=Cache.path_by_id(idx), format=self.format)
        plt.close()


        
    def inject(self, cfg):
        '''
        Injecting configuration data -> will be merged with existing config
        
        :param self: 
        :param cfg: dict with (new) configuration attributes
        '''

        self._cfg = self._cfg | cfg
        return self

    def __str__(self):
        return f"""width: {self.frame_width} color: {self.frame_color}"""


if __name__ == "__main__":
    gfx = Gfx()
    fig = gfx.get_pic("b105")
    fig.savefig(fname="foo.svg", format="svg")
