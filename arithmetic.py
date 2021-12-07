def n_term():
    n = int(input("Which element do you need?\t"))
    nterm = first + ((n - 1) * difference)
    return nterm
def sum_of_n():
    n = int(input("How many elements do you need summarised?\t"))
    sum = (n*(first + nterm()))/2
    return sum
def pyramid():
    n = int(input("How many levels should the pyramid have?\t"))
    piramid = n*(first + nterm())
while True:
    first = int(input("What should be the first/starting component?\t"))
    difference = int(input("How much should the difference be?\t"))
    need = str(input("What do you need? (nterm, sum, or pyramid)\t"))
    nterm = 0
    sum = 0
    piramid = 0
    if need == "nterm":
        n_term()
        print(nterm)
    elif need == "sum":
        sum_of_n()
        print(sum)
    else:
        pyramid()
        print(piramid)
