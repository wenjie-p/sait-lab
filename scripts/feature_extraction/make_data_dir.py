import os
import shutil
import sys

def make_data_dir(src, des):

    for stage in os.listdir(src):
        ds = f"{src}/{stage}"
        if not os.path.isdir(ds):
            continue
        for spk in os.listdir(ds):
            dr = f"{ds}/{spk}/Pitch_Dir"
            if not os.path.isdir(dr):
                continue
            for f in os.listdir(dr):
                fsrc = f"{dr}/{f}"
                if not os.path.isfile(fsrc):
                    continue
                des_dir = f"{des}/{stage}/{spk}/Pitch_Dir"
                if not os.path.isdir(des_dir):
                    os.makedirs(des_dir)
                fdes = f"{des_dir}/{f}"
                shutil.copyfile(fsrc, fdes)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print(f"Usage: {sys.argv[0]} src_batch des_dir")
        exit(0)

    make_data_dir(sys.argv[1], sys.argv[2])
