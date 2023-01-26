from tectonic import Helpers
from tectonic import Valuation
import math

def test_band_of_investing():
    r = round(Valuation.band_of_investing(0.07, 15,0.50,0.10,950000),2)
    assert r == 9_056_476.08