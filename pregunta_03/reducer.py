#
# >>> Escriba el codigo del reducer a partir de este punto <<<
#
import sys

if __name__ == "__main__":

    lista = []

    for line in sys.stdin:
        key, val = line.split("\t")
        val = int(val)

        lista.append((key, val))

        lista.sort(key=lambda i: i[1], reverse=False)

    for elemento in lista:
        sys.stdout.write("{},{}\n".format(elemento[0], elemento[1]))
