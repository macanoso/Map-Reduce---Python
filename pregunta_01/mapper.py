#
# >>> Escriba el codigo del mapper a partir de este punto <<<
#
import sys

if __name__ == "__main__":

    for line in sys.stdin:
        sys.stdout.write("{}\t{}\n".format(line.split(",")[0], line.split(",")[1]))
