import os
from os.path import join, exists

src = "../ElectricRepulsion"
dst = "../ElectricRepulsion_camino"

for i in range(10, 260, 10):
    f = "Elec{:0>3}.txt".format(i)
    if exists(join(dst, f)):
        continue
    os.system(f"dirorder {join(src, f)} {join(dst, f)} -cartesian -nthreads $(nproc)")
