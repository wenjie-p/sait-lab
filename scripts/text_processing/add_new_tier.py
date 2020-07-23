# This script add new tier to the current textgrid file
# Input:
# src: dir of src tgt files
# des: name of the output dir
# name: name of the new layer
import tgt
from tgt import IntervalTier
import os
import sys

def add_new_tier(src, des, name):

    if not os.path.exists(des):
        os.makedirs(des)

    for f in os.listdir(src):
        fin = "{}/{}".format(src, f)
        obj = tgt.io.read_textgrid(fin)
        end_time = obj.end_time
        new_tier = IntervalTier(start_time = 0.00, end_time = end_time, name = name, objects = None)
        obj.add_tier(new_tier)
        fout = "{}/{}".format(des, f)
        tgt.io.write_to_file(obj, fout)


if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: {} src des name".format(sys.argv[0]))
        exit(0)
    add_new_tier(sys.argv[1], sys.argv[2], sys.argv[3])
