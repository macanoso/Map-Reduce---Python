#
# >>> Escriba el codigo del mapper a partir de este punto <<<
#
import sys
import re

if __name__ == "__main__":

    for line in sys.stdin:
        lista = line.split("   ")[1]
        lista1 = line.split("-")[1]
        sys.stdout.write("{},1\n".format(lista1))
