def cautare_secventiala_neordonata(l, element):
    """
    Complexitatea apartine lui O(n)
    """
    poz = -1
    for i in range(0, len(l)):
        if element == l[i]:
            poz = i
    return poz


def cautare_secventiala_neordonata_faster(l, element):
    """
    Best case is O(1)
    Worst case is O(n)
    Avearage case is O(n)
    """
    
    i = 0
    while i< len(l) and element!=l[i]:
        i+=1
    
    if i < len(l):
        return i
    return -1


def cautare_secventiala_ordonata(l, element):
    """
    Complexitatea O(n)
    """
    if len(l) == 0:
        return 0
    
    if element < l[0]:
        return 0
    if element > l[len(l)-1]:
        return len(l)

    
    poz = -1
    for i in range(0, len(l)):
        if element>=l[i]:
            poz = i
    if poz == -1:
        return len(l)

    return poz

def cautare_secventiala_ordonata_faster(l, element):
    """
    Best complexity O(1)
    Worst O(n)
    Average O(n)
    """
    if len(l) == 0:
        return 0
    
    if element < l[0]:
        return 0
    if element > l[len(l)-1]:
        return len(l)

    i = 0
    while i<len(l) and element >l[i]:
        i+=1
    return i
def cautare_binara_iterativ(l, element):
    """
    Best case is O(1)
    Worst is O(logn)
    Average is O(logn)
    """
    if len(l) ==0:
        return 0
    if element<=l[0]:
        return 0
    if element>l[len(l)-1]:
        return len(l)
    stanga = 0
    dreapta = len(l)
    while dreapta - stanga>1:
        m = (stanga+dreapta)//2
        if element <= l[m]:
            dreapta = m
        else: stanga = m
    return dreapta
def cautare_binara_recursiv(l, element):
    """
    Best case is O(1)
    Worst is O(logn)
    Average is O(logn)
    """
    if len(l) ==0:
        return 0
    if element<=l[0]:
        return 0
    if element>l[len(l)-1]:
        return len(l)
    return algoritm_cautare_binara(l, element, 0, len(l))

def algoritm_cautare_binara(l, element, stanga, dreapta):
    if stanga>=dreapta-1:
        return dreapta
    mijloc = (stanga+dreapta)//2

    if element <= l[mijloc]:
        return algoritm_cautare_binara(l, element, stanga, mijloc)
    else:
        return algoritm_cautare_binara(l, element, mijloc, dreapta)

def selection_sort(l):
    """
    Time complexity is O(n^2)
    In place algorithm
    """
    for i in range(0, len(l)-1):
        pozitie = i
        for j in range(i+1, len(l)):
            if l[j]< l[pozitie]:
                pozitie = j
        if i<pozitie:
            l[i],l[pozitie] = l[pozitie], l[i]

def direct_selection_sort(l):
    """
    Time complexity is O(n^2)
    In place algorithm
    """
    for i in range(0, len(l)-1):
        for j in range(i+1, len(l)):
            if l[j]<l[i]:
                l[i],l[j] = l[j], l[i]


def insertion_sort(l):
    """
    Caz defavorabil: O(n^2)
    Caz faborabil: O(n)
    Caz mediu: O(n^2)
    In place
    """
    for i in range(1, len(l)):
        ind = i-1
        a = l[i]
        while ind>=0 and a<l[ind]:
            l[ind+1] = l[ind]
            ind -=1
        l[ind+1] = a

def bubbleSort(l):
    """
    Favorabil O(n)
    Nevaforabil O(n^2)
    Mediu O(n^2)
    In place
    """
    sorted = False
    while not sorted:
        sorted = True # assume the list is already sorted
        for i in range(len(l)-1):
            if l[i+1]<l[i]:
                l[i], l[i + 1] = l[i + 1], l[i]
                sorted = False
def bubbleSort2(l):
    """
    Favorabil O(n)
    Nevaforabil O(n^2)
    Mediu O(n^2)
    In place
    """
    for j in range(1, len(l)):
        for i in range(0, len(l)-j):
            if l[i+1]<l[i]:
                l[i], l[i + 1] = l[i + 1], l[i]

def quickSort(l):
    """
    Returns AN ORDERED LIST
    Caz favorabil: nlogn
    Caz mediu: nlogn
    Caz worst: n^2
    NOT In place
    """
    if len(l)<=1:
        return l
    pivot = l.pop()
    lesser  = quickSort([x for x in l if x<pivot])
    greater = quickSort([x for x in l if x>=pivot])
    return lesser + [pivot] + greater

def partition(l, stanga, dreapta):
    pivot = l[stanga]     
    i = stanga
    j = dreapta
    while i!=j:
        while l[j]>=pivot and i<j:
            j = j-1
        l[i] = l[j]
        while l[i]<=pivot and i<j:
            i = i+1
        l[j] = l[i]
    l[i] = pivot
    return i

"""
pivot = l[stanga]
i = stanga
j = dreapta

while i!=j:
    while l[j]>=pivot and i<j:
        j-=1
    l[i] =l[j]

    while l[i]<=pivot and i<j:
        i+=1
    l[j] = l[i]
l[i] = pivot
return i

"""

def quickSort2(l, stanga, dreapta):
    """
    Caz favorabil: nlogn
    Caz mediu: nlogn
    Caz worst: n^2
    In place
    """
    pos = partition(l, stanga, dreapta)
    if stanga<pos-1:
        quickSort2(l, stanga, pos-1)
    if pos+1<dreapta:
        quickSort2(l, pos+1, dreapta)


def mergeSort(l, start, end):
    """
    Returns AN ORDERED LIST
    Cazuri identice, complexitate = O(nlogn)
    NOT IN PLACE, O(n)
    """
    if end>start:
            
        m = (end+start)//2
        mergeSort(l, start, m)
        mergeSort(l, m+1, end)
        merge(l, start, m, end)

"""INVATA SORTARI"""
def merge(arr, l, m, r):
    n1 = m - l + 1
    n2 = r - m
 
    # create temp arrays
    L = [0] * n1
    R = [0] * n2
 
    # Copy data to temp arrays L[] and R[]
    for i in range(0, n1):
        L[i] = arr[l + i]
 
    for j in range(0, n2):
        R[j] = arr[m + 1 + j]
 
    # Merge the temp arrays back into arr[l..r]
    i = 0     # Initial index of first subarray
    j = 0     # Initial index of second subarray
    k = l     # Initial index of merged subarray
 
    while i < n1 and j < n2:
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1
 
    # Copy the remaining elements of L[], if there
    # are any
    while i < n1:
        arr[k] = L[i]
        i += 1
        k += 1
 
    # Copy the remaining elements of R[], if there
    # are any
    while j < n2:
        arr[k] = R[j]
        j += 1
        k += 1

def main():
    lista =  [3,56,2,5,6,1,12,4,6,1,5,78]
    #[3,1,4,10,8,5,3,2]
    #[3,56,2,5,6,1,12,4,6,1,5,78]
    mergeSort(lista,0,len(lista)-1)
    print(lista)

main()
"""
def longest_even_desc_subseq(vector):
    lungime = len(vector)
    #vectori l - lungimea 
    #p - elementul ce urmeaza
    l = [0]*lungime
    p = [0]*lungime
    l[lungime-1] = 1
    p[lungime -1] = -1
    
    for k in range(lungime-2, -1, -1):
        l[k]=1
        p[k]=-1
        
        for i in range(k+1, lungime):
            if (vector[i]%2==0 and vector[i]<=vector[k] ) and l[k]< l[i]+1:
                l[k] = l[i]+1
                p[k] = i
                
    j = 0
    for i in range(0, lungime):
        if l[i]>l[j]:
            j=i
    rez = []
    while j!=-1:
     rez = rez+[vector[j]]
     j = p[j]
    return rez



lista = longest_even_desc_subseq([2,12,3,6,14,3,4,7,2])
print(lista)
"""