#
# >>> Escriba el codigo del mapper a partir de este punto <<<
#
import sys

if __name__ == "__main__":

    for line in sys.stdin:
        lista = line.split("\t")
        sys.stdout.write("{}\t{}".format(lista[0], lista[1]))
