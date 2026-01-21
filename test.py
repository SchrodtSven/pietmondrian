from pmonlib.cache import Cache
from pmonlib.provider import Provider
from pmonlib.gfx import Gfx

provider = Provider()
gfx = Gfx()


print(gfx._cfg)


print(gfx.inject({'frame_color': 'pinkk', 'format': 'png', 'foo': 23})._cfg)


gfx.cfg()