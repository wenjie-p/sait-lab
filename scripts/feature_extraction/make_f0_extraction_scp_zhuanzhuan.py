import os
import codecs



src = "../../data/Zhuanzhuan/KZ"
des = "../../data/Zhuanzhuan/KZ_Pitch"
data = []

for spk in os.listdir(src):
    dspk = f"{src}/{spk}"
    if not os.path.isdir(dspk):
        continue
    gender = spk[0]
    for t in os.listdir(dspk):
        dt = f"{dspk}/{t}"
        if not os.path.isdir(dt):
            continue
        for f in os.listdir(dt):
            if not f.endswith(".wav"):
                continue
            fsrc = f"{dt}/{f}"
            fdes = f"{des}/{spk}/{t}"
            if not os.path.exists(fdes):
                os.makedirs(fdes)
            fdes = f"{fdes}/{f.replace('wav', 'pitch')}"
            fsrc = os.path.abspath(fsrc)
            fdes = os.path.abspath(fdes)
            line = f"{fsrc}\t{gender}\t{fdes}\n"
            data.append(line)


fout = "./zhuanzhuan.scp"
fp = codecs.open(fout, "w", encoding = "utf8")
for line in data:
    fp.write(line)
fp.close()
        
