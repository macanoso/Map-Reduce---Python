#
# >>> Escriba el codigo del reducer a partir de este punto <<<
#
import sys
from collections import defaultdict
import operator

if __name__ == "__main__":

    diccionario = defaultdict(list)

    for line in sys.stdin:
        line = line.strip("\n")
        key, val = line.split("\t")
        val = val.split(",")
        key = int(key)

        for i in val:
            diccionario[i].append(key)

    dct = dict(diccionario)
    dct = dict(sorted(dct.items(), key=operator.itemgetter(0)))

    for x, y in dct.items():
        y = sorted(y, key=int)
        y = ",".join(str(x) for x in y)
        sys.stdout.write("{}\t{}\n".format(x, y))
