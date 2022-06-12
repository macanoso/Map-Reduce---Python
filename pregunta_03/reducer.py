#
# >>> Escriba el codigo del reducer a partir de este punto <<<
#
import sys

if __name__ == "__main__":

    lista1 = []

    for line in sys.stdin:
        key, val = line.split(",")
        val = int(val)

        lista1.append((key, val))

        lista1.sort(key=lambda i: i[1], reverse=False)

    for elemento in lista1:
        sys.stdout.write("{},{}\n".format(elemento[0], elemento[1]))
