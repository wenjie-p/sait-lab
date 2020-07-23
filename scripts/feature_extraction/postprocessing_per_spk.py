import codecs
import numpy as np
import os
import sys
import tgt

def extract_focus_dur(fin, ith):

    obj = tgt.io.read_textgrid(fin)
    tier = obj.get_tier_by_name("Pinyin")
    items = tier.intervals
    durs = []
    for item in items:
        text = item.text
        if text == "sil":
            continue
        dur = float(item.end_time) - float(item.start_time)
        durs.append(dur)
    f_dur = durs[ith]/sum(durs)

    tier = obj.get_tier_by_name("Tone_Nucleus")
    items = tier.intervals
    segs = []
    for item in items:
        text = item.text
        if text == "tn":
            beg = item.start_time
            end = item.end_time
            beg = int(beg*1000)
            end = int(end*1000)
            segs.append([beg, end])
    return f_dur, segs

def extract_segment_info(fpt, ftgt, ith):
    data = []
    f_dur, segs = extract_focus_dur(ftgt, ith)
    p_data = load_data(fpt)
    pre_max = ""
    s_max = -1000
    s_min = 1000
    deltas = []
    for (beg, end) in segs:
        f0s = [ float(ele.strip()) for ele in p_data[beg: end]]
        sts = [12*np.log2(p/100) for p in f0s]
        p_max = np.max(sts)
        p_min = np.min(sts)
        
        if p_max > s_max:
            s_max = p_max
        if p_min < s_min:
            s_min = p_min
        p_mean = np.mean(sts)
        p_range = p_max - p_min
        line = [p_max, p_min, p_mean, p_range]
        data.append(line)

        if pre_max != "":
            deltas.append(pre_max - p_max)
        pre_max = p_max
    
    if len(data) == 0:
        return [None] * 8
    sen_range = s_max - s_min
    f_max = data[ith][0]
    f_min = data[ith][1]
    f_range = data[ith][-1]
    f_mean = data[ith][2]
    if len(deltas) == 1:
        deltas.append(0.00)

    return f_max, f_min, f_range, f_mean, sen_range, f_dur, deltas[0], deltas[-1]

def load_data(fin):
    fp = codecs.open(fin, "r")
    data = fp.readlines()
    fp.close()
    return data

def load_conf(fin):
    
    data = load_data(fin)
    dic = {}
    for i in range(len(data)):
        ith = data[i].strip()
        dic[i+1] = int(ith)
    return dic

def postprocessing(fin, pd, tgt, fout):

    conf = load_conf(fin)
    data = []
    line = ["filename","focus_max","focus_min","focus_range","focus_mean","sen_range","focus_dur","delta1","delta2"]
    data.append(line)
    for f in os.listdir(pd):
        fid = f.split(".")[0]
        fpt = "{}/{}".format(pd, f)
        ftgt = "{}/{}.TextGrid".format(tgt, fid)
        if not os.path.exists(fpt) or not os.path.exists(ftgt):
            continue
        fid_ = int(fid)
        if fid_ > 63:
            continue
        ith = conf[fid_] - 1
        if ith < 0:
            continue
        #print("processing file: {}".format(fpt))
        f_max, f_min, f_range, f_mean, sen_range, f_dur, delta1, delta2 = extract_segment_info(fpt, ftgt, ith)
        if f_max == None:
            print("file {} not processed.".format(ftgt))
            continue

        line = "{}\t{:.3f}\t{:.3f}\t{:.3f}\t{:.3f}\t{:.3f}\t{:.3f}\t{:.3f}\t{:.3f}\n".format(fid, f_max, f_min, f_range, f_mean, sen_range, f_dur, delta1, delta2)
        line = [fid, f_max, f_min, f_range, f_mean, sen_range, f_dur, delta1, delta2]
        
        data.append(line)
    
    return data


if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("Usage: {} conf pitch_dir textgrid_dir output_file".format(sys.argv[0]))
        exit(0)

    postprocessing(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])

