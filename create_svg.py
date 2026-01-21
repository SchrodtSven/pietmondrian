from pmonlib.cache import Cache
from pmonlib.provider import Provider
from pmonlib.gfx import Gfx

provider = Provider()
gfx = Gfx()





print(Cache.path_by_id('b106'))


exit()

for idx in Cache.idc:
    '''
    /Users/svenschrodt/projx/pietmondrian/pmonlib/gfx.py:39: RuntimeWarning: More than 20 figures have been opened. 
    Figures created through the pyplot interface (`matplotlib.pyplot.figure`) are retained until explicitly closed and may consume too much memory. 
    
    (To control this warning, see the rcParam `figure.max_open_warning`). Consider using `matplotlib.pyplot.close()`.
    '''
    #idx = 'b288'
    idx = 'b194'
    fn = f'assets/img/{idx}.svg'
    print(fn)
    gfx.add_meta = False
    fig = gfx.get_pic(idx)
    fig.patch.set_linewidth(10)
    fig.patch.set_edgecolor('k')
    fig.savefig(fname=fn, format='svg')
    exit()