#
# >>> Escriba el codigo del reducer a partir de este punto <<<
#
import sys

if __name__ == "__main__":

    lista1 = []
    for line in sys.stdin:
        line = line.strip("\n")
        key, val = line.split(",")
        val = float(val)

        lista1.append((key, val))

    d = {}
    for x, y in lista1:
        d.setdefault(x, []).append(y)

    for x, y in d.items():
        sys.stdout.write("{}\t{}\t{}\n".format(x, max(y), min(y)))
