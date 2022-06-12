#
# >>> Escriba el codigo del mapper a partir de este punto <<<
#
import sys

if __name__ == "__main__":

    for line in sys.stdin:
        a, b = line.split(",")
        sys.stdout.write("{}\t{}".format(a, b))
