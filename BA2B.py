#BA2B
#Find a Median string

def rosalindprint(res, newline=False):
    text=""
    sep=" "
    if newline:
        sep="\n"
    for i in res:
        text=text+str(i)+sep
    return text.strip()

def kmer(text, i ,k):
    #substring of text from i-th position for the next k letters
    return text[i:(i+k)]

def kmerindicies(text,k):
    #find indicies of all k-mers in text
    D=dict()
    for i in range(0, len(text)-k+1):
        tmp=kmer(text,i,k)
        try:
            D[tmp].append(i)
        except KeyError:
            D[tmp]=[i]
    return D

def kmersfrequency(text,k):
    #find the number of occurences of all k-mers in text
    D=kmerindicies(text,k)
    for k,v in D.items():
        D[k]=len(v)
    return D

def HammingDistance(p,q):
    #computes the hamming distance between strings p and q
    if len(p)!=len(q):
        return -1
    dist=0
    for first, second in zip(p,q):
        if first!=second:
            dist=dist+1
    return dist

def minhamm(text,pattern):
    #find the minimum Hamming distance between Pattern and any k-mer in Text
    #where k=len(pattern)
    D=kmersfrequency(text,len(pattern))
    return min([HammingDistance(pattern,x) for x in D.keys()])

def subsets(n,k):
    #return all k-sized subsets (as indices) of an n-sized set
    if k==0:
        return[[0]*n]
    def helper(l,lastn):
        if sum(l)<lastn or lastn<1:
            return[]
        for i in range(len(l)-1,-1,-1):
            if l[i]==1:
                lastind=i
                break
        head=l[:(lastind-lastn+1)]
        N=len(l)-len(head)
        res=[
            head+[0]*i+[1]*lastn+[0]*(N-i-lastn)
            for i in range(0,N-lastn+1)
        ]
        return res
    def recursion(l,lastn):
        tmp=helper(l,lastn)
        if lastn==1:
            return tmp
        L=[]
        for x in tmp:
            L.extend(recursion(x,lastn-1))
        return L
    startlist=[1]*k+[0]*(n-k)
    return recursion(startlist,k)

def mutations(pattern,errorind):
    #generate all mutations for a pattern at indices given in errorind
    #such that Hamming distance is equal to the sum(errorind)
    def f(base, start=""):
        if base=="A":
            return [start + "C", start + "G", start + "T"]
        if base=="C":
            return [start + "A", start + "G", start + "T"]
        if base=="G":
            return [start + "A", start + "C", start + "T"]
        if base=="T":
            return [start + "A", start + "C", start + "G"]
    L=[""]
    for base, error in zip(pattern, errorind):
        if error==0:
            L=[x+base for x in L]
        else:
            tmp=[f(base,x) for x in L]
            L=[]
            [[L.append(x) for x in x1] for x1 in tmp]
    return L

def kmersNeighbours(text,k):
    """
    find all k-mers (words) and their Neighbours in a string text
    together with a minimal hamming distance between neighbours
    """
    D = kmersfrequency(text, k)

    errors = []
    for d in range(1, k + 1):
        errors.extend(subsets(k, d))

    L = []
    for x in D.keys():
        for errorind in errors:
            L.extend(mutations(x, errorind))
    L = list(set(L))

    RES = dict()
    for pattern in L:
        RES[pattern] = min([HammingDistance(pattern, x) for x in D.keys()])
    return RES


def MedianStrings(dnalist, k):
    """
    Find a k-mer Pattern that minimizes d(Pattern, DnaList)=sum(d(Pattern,Dna))
    over all k-mers Pattern and Dna in DnaList where d = minhamm
    """
    L = []
    for dna in dnalist:
        L.append(kmersNeighbours(dna, k))

    s = set()
    for x in L:
        s = s.union(x.keys())

    RES = dict()
    for key in s:
        RES[key] = 0

    for D in L:
        for key, value in D.items():
            RES[key] = RES[key] + value

    mincount = min(RES.values())

    return [key for key, value in RES.items() if mincount == value]


if __name__ == "__main__":
    with open("./rosalind_ba2b.txt") as myfile:
        inlines = [x.strip("\n") for x in myfile.readlines()]
        k = int(inlines[0])
        L = inlines[1:]
    print(rosalindprint(MedianStrings(L,k)))