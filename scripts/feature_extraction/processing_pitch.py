import codecs
import os
import numpy as np


src = "../../data/Luojieqiong_Pitch"
des = "../../data/Luojieqiong_Res"

dic = {}
sen = ["sent", "sent2"]

def load_f0(fin):
    fp = codecs.open(fin, "r", encoding = "utf8")
    data = fp.readlines()
    fp.close()
    f0s = [float(ele.strip()) for ele in data if float(ele.strip()) > 0]
    pts = [ np.log2(f0) for f0 in f0s]
    return pts

for country in os.listdir(src):
    dc = "{}/{}".format(src, country)
    dic[country] = {}
    for spk in os.listdir(dc):
        dspk = "{}/{}".format(dc, spk)
        dic[country][spk] = []
        for s in sen:
            dsen = "{}/{}".format(dspk, s)
            for f in os.listdir(dsen):
                fin = "{}/{}".format(dsen, f)
                f0s = load_f0(fin)
                dic[country][spk].extend(f0s)
            

for country in dic:
    for spk in dic[country]:
        fout = "{}/{}_{}.pitch".format(des, country, spk)
        data = dic[country][spk]
        data = [str(ele) for ele in data]
        with codecs.open(fout, "w", encoding = "utf8") as fp:
            fp.write(" ".join(data))
