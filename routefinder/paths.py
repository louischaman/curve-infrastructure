import dubins
import pyproj
from math import pi
wgs84=pyproj.Proj("+init=EPSG:4326")
osgb36=pyproj.Proj("+init=EPSG:27700")

def get_geo_dubins(q0, q1, turning_radius, step_size):
    # dubins on long and lat coords

    x0 = pyproj.transform(wgs84, osgb36, q0[1], q0[0]) + (pi - q0[2] ,)
    x1 = pyproj.transform(wgs84, osgb36, q1[1], q1[0]) + (pi - q1[2] ,)
    path = dubins.shortest_path(x0 , x1, turning_radius)
    configurations, _ = path.sample_many(step_size)
    ll_path = [pyproj.transform(osgb36, wgs84, coord[0], coord[1]) for coord in configurations]
    ll_path_switch = [ ( ele[1], ele[0]) for ele in ll_path]
    return( ll_path_switch )