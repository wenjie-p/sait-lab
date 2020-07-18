import codecs


def write2file(fout, data):
    fp = codecs.open(fout, "w")
    for line in data:
        fp.write(line)
    fp.close()
