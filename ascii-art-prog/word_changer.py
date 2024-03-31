import re

out = []
with open("flash.txt", "rb") as x:
    for line in x:
        m = re.match(rb"(.+?)\[(.+?)\]\t(.+?)\t([^\s]+)", line)
        groups = list(m.groups())
        if groups[-1].isdigit():
            groups[-1] = b"other"
        out.append(b"\t".join(groups))

with open("flash-thing.txt", "wb") as x:
    x.write(b"\n".join(out))
