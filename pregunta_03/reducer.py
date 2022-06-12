#
# >>> Escriba el codigo del reducer a partir de este punto <<<
#
from email import header
import sys
import pandas as pd

if __name__ == "__main__":

    lista = []

    for line in sys.stdin:
        key, val = line.split("\t")
        val = int(val)
        lista.append((key, val))
    lista.sort(key=lambda i: i[1], reverse=False)

    data_output = pd.DataFrame(
        lista,
    )
    print(data_output.to_csv(index=False, header=None, sep=",").rstrip("\n"))
