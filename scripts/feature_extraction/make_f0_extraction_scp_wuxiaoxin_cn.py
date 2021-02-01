import os
import codecs



src = "../../data/JP_韵律上不自然的双音节_基频提取_wxx"
des = "../../data/Wuxiaoxin_Pitch"
src = "../../data/CN"
des = "../../data/CN_Wuxiaoxin_Pitch"
data = []

for spk in os.listdir(src):
    dspk = f"{src}/{spk}"
    if not os.path.isdir(dspk):
        continue
    gender = spk[0]
    for f in os.listdir(dspk):
        if not f.endswith(".wav"):
            continue
        fsrc = f"{dspk}/{f}"
        fdes = f"{des}/{spk}/"
        if not os.path.exists(fdes):
            os.makedirs(fdes)
        fdes = f"{fdes}/{f.replace('wav', 'pitch')}"
        fsrc = os.path.abspath(fsrc)
        fdes = os.path.abspath(fdes)
        line = f"{fsrc}\t{gender}\t{fdes}\n"
        data.append(line)


fout = "./wuxiaoxin_cn.scp"
fp = codecs.open(fout, "w", encoding = "utf8")
for line in data:
    fp.write(line)
fp.close()
        
