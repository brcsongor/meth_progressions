def n_term(n,first,difference):
    nterm = first+((n-1)*difference)
    print(nterm)
    return nterm
def sum_of_n(n,first,nterm):
    sum = (n*(first+nterm))/2
    print(sum)
    return sum
def pyramid(n,nterm):
    piramid = n*(first+nterm)
    print(piramid)
    return piramid
while True:
    first = int(input("What should be the first/starting component?\t"))
    difference = int(input("How much should the difference be?\t"))
    need = str(input("What do you need? (nterm, sum, or pyramid)\t"))
    if need == "nterm":
        n_term(int(input("Which element dou you need?\t")),first,difference)
    elif need == "sum":
        sum_of_n(int(input("How many elements you need summarised?\t")),first,n_term(int(input("Which element dou you need?\t")),first,difference))
    else:
        pyramid(int(input("How many levels shoud the prymaid have?\t")),n_term(int(input("Which element dou you need?\t")),first,difference))
