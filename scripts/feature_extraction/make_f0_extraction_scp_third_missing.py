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
    for spk in os.listdir(src):
        gender = spk[0]
        dspk = "{}/{}".format(src, spk)
        if not os.path.isdir(dspk):
            continue
        for f in os.listdir(dspk):
            if f.endswith(".wav"):
                fwav = "{}/{}".format(dspk, f)
                fpit = "{}/{}/{}.pitch".format(des, spk, f.split(".")[0])
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
