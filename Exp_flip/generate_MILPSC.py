import os
from os.path import join, exists

src = "../ElectricRepulsion"
dst = "../ElectricRepulsion_MILPSC"

for i in range(10, 260, 10):
    f = "Elec{:0>3}.txt".format(i)
    if exists(join(dst, f)):
        continue
    os.system(
        f"python -m qspace_direction.direction_flip --input {join(src, f)} --output {join(dst, f)} -c DISTANCE"
    )
