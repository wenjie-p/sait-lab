from add_new_tier import add_new_tier


tier_name = "Tone_Nucleus"

import os

tgt_dir = "TG"
root = "/Users/wenjie/workspace/projects/sait-lab/data/YaYa/First_Second_Batch_Data/"
vs = ["First_Batch_Data", "Second_Batch_Data"]
des = "New_TG"

droot = "/Users/wenjie/workspace/projects/sait-lab/data/YaYa/Data"
for v in vs:
    src = "{}/{}".format(root, v)
    for stage in os.listdir(src):
        ds = "{}/{}".format(src, stage)
        if not os.path.isdir(ds):
            continue
        for spk in os.listdir(ds):
            dspk = "{}/{}/{}".format(ds, spk, tgt_dir)
            if not os.path.isdir(dspk):
                continue
            ddes = "{}/{}/{}/{}/{}".format(droot, v, stage, spk, des)
            if not os.path.exists(ddes):
                os.makedirs(ddes)
            add_new_tier(dspk, ddes, tier_name)
