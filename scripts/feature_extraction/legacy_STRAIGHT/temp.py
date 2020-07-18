import codecs

fin = "863_wav.scp"

fp = codecs.open(fin, "r", encoding = "utf8")
data = fp.readlines()
fp.close()

fout = "863wav.scp"
prefix = "/home/pwj/863"
fp = codecs.open(fout, "w", encoding = "utf8")
for line in data:
    line = line.strip().split()
    gender = line[0][0]
    f = line[1].split("/")[-1]
    fdes = "{}/{}".format(prefix, f.replace("WAV", "pitch"))
    
    new_line = "{} {} {}\n".format(line[1], gender, fdes)
    fp.write(new_line)

fp.close()

