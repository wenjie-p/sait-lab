from postprocessing_per_spk import *

conf = "./focus.conf"
pitch_dir = "wav"
#tone_nucleus_dir = "nucleiTI"
tgt_dir = "New_TG"


stages = ["前测", "中测", "后测"]

import sys
src = sys.argv[1]
import xlsxwriter
fout = sys.argv[2]

wb = xlsxwriter.Workbook(fout)

for stage in stages:
    sheet = wb.add_worksheet(stage)
    sdir = "{}/{}".format(src, stage)
    col_beg = 0
    for spk in os.listdir(sdir):
        if not spk.startswith("F001"):
            continue
        spkdir = "{}/{}".format(sdir, spk)
        if not os.path.isdir(spkdir):
            continue
        
#        ftn = "{}/{}".format(spkdir, tone_nucleus_dir)
        fpt = "{}/{}".format(spkdir, pitch_dir)
        ftgt = "{}/{}".format(spkdir, tgt_dir)
    
        spk_data = postprocessing(conf, fpt, ftgt, "")
        sheet.write(0, col_beg, spk)
        for i in range(len(spk_data)):
            for j in range(len(spk_data[0])):
                sheet.write(i, col_beg + j + 1, spk_data[i][j])
        col_beg += (1 + len(spk_data[0]))

wb.close()
