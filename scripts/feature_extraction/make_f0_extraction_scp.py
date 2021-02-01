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


def make_scp(src, suffix):
    data = []
    for stage in os.listdir(src):
        ds = "{}/{}".format(src, stage)
        if not os.path.isdir(ds):
            continue
        for spk in os.listdir(ds):
            gender = spk[0]
            dwav = "{}/{}/{}".format(ds, spk, suffix)
            for wav in os.listdir(dwav):
                if not wav.endswith(".wav"):
                    continue
                fwav = "{}/{}".format(dwav, wav)
                fpit = fwav.replace(".wav", ".pitch")
                fwav = os.path.abspath(fwav)
                fpit = os.path.abspath(fpit)
                line = "{}\t{}\t{}\n".format(fwav, gender, fpit)
                data.append(line)
    if len(data) == 0:
        print(src)
        exit(0)
    return data


def make_scp3(src):
    data = []
    for spk in os.listdir(src):
        dspk = "{}/{}".format(src, spk)
        if not os.path.isdir(dspk):
            continue
        for f in os.listdir(dspk):
            if not f.endswith(".wav"):
                continue
            fwav = "{}/{}".format(dspk, f)
            fpit = fwav.replace(".wav", ".pitch")
            fwav = os.path.abspath(fwav)
            fpit = os.path.abspath(fpit)
            gender = spk[0]
            line = "{}\t{}\t{}\n".format(fwav, gender, fpit)
            data.append(line)
    if len(data) == 0:
        print(src)
        exit(0)
    return data

src1 = "../../data/YaYa/TextGrid_Wav/First_Batch_Data/First_Batch_Data"
src2 = "../../data/YaYa/TextGrid_Wav/Second_Batch_Data/Second_Batch_Data"
src3 = "../../data/YaYa/TextGrid_Wav/Third_Batch_Data/"
src4 = "../../data/YaYa/TextGrid_Wav/Five_Batch_Data/"

op = "New_TG"
data1 = make_scp(src1, op)
data2 = make_scp(src2, op)
data4 = make_scp(src4, "")
data3 = make_scp3(src3)

data = data1 + data2 + data3 + data4

fout = "./all_wav.scp"
write2file(fout, data)
