# This script implemets the process of pitch extraction
# There are two steps for this job:
# 1) make scp and,
# 2) run the STRAIGHT algorithm.

#import codecs
import os
import sys
#sys.path.append("/disk2/pwj/workspace/projects/sait-lab/toolkits/legacy_STRAIGHT/src")

#from f0_extraction import f0_extraction
from utils import write2file


def make_scp(src, des, fout):
    data = []
    for stage in os.listdir(src):
        ds = "{}/{}".format(src, stage)
        if not os.path.isdir(ds):
            continue
        for spk in os.listdir(ds):
            gender = spk[0]
            dwav = "{}/{}/New_TG".format(ds, spk)
            if not os.path.isdir(dwav):
                continue
            des_dir = "{}/{}/{}".format(des, stage, spk)
            if not os.path.exists(des_dir):
                os.makedirs(des_dir)
            for wav in os.listdir(dwav):
                if not wav.endswith(".wav"):
                    continue
                fwav = "{}/{}".format(dwav, wav)
                fpit = "{}/{}.pitch".format(des_dir, wav.split(".")[0])
                fwav = os.path.abspath(fwav)
                fpit = os.path.abspath(fpit)
                line = "{}\t{}\t{}\n".format(fwav, gender, fpit)
                data.append(line)

    write2file(fout, data)


if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: {} /path/to/data/[pre:mid:post] pitch_dir fout[scp]".format(sys.argv[0]))
        exit(0)

    scp = sys.argv[3]
    make_scp(sys.argv[1], sys.argv[2], scp)
    #scp = os.path.abspath(scp)
    #f0_extraction(scp)
