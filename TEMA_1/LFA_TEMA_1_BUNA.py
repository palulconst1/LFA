fin = set()


def dfs(cuvant, nod, ok,s=fin):
    vecini=[]
    if ok == 1:
        cuvant = cuvant[1:len(cuvant)]
    ok=0
    if cuvant == '':
        s.add(nod)
        return 0
    for z in range(nr_st):
        if matrix[nod][z] == '$':
            vecini.append(z)
            dfs(cuvant, z, 0)
        if cuvant[0] in matrix[nod][z]:
            vecini.append(z)
            ok=1
            dfs(cuvant, z, ok)
    if not vecini:
        return 0


def verificare(sir):
    fin.clear()
    if sir == '':
        return 1
    for t in sir:
        if t not in alfabet:
            return 0
    dfs(sir, 0, 0)
    for j in fin:
        if j in st_fin:
            return 1


f = open("date.txt")
nr_st = int(f.readline())
nr_carac = int(f.readline())
alfabet = [x for x in f.readline().split()]
q0 = int(f.readline())
nr_st_fin = int(f.readline())
st_fin = [int(x) for x in (f.readline().split())]
nr_tr = int(f.readline())
x = len(alfabet)

matrix = []
for i in range(nr_st):
    row = []
    for j in range(nr_st):
        row.append('0')
    matrix.append(row)

for i in range(nr_tr):
    tr_cr = f.readline().split()
    m = int(tr_cr[0])
    n = int(tr_cr[2])
    if  matrix[m][n] == '0':
         matrix[m][n] = tr_cr[1]
    else:
        matrix[m][n] = matrix[m][n] + tr_cr[1]


# Am citit toate datele de intrare, construind o matrice de adiacenta ce reprezinta automatul dat.

nr_teste = int(f.readline())
for i in range(nr_teste):
    test = f.readline()
    test = test[0:len(test)-1]
    test1 = test
    if verificare(test1) == 1:
        print(test, "~ DA")
    else:
        print(test, "~ NU")