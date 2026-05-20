
def merge_two_sorted_list(A,B):

    i=0
    j=0
    sorted_list=[]

    while i < len(A) and j < len(B):
        if A[i]<B[j]:
            sorted_list.append(A[i])
            i+=1
        elif A[i]==B[j]:
            sorted_list.append((A[i]))
            i+=1
            j+=1
        else:
            sorted_list.append((B[j]))
            j+=1

    while i<len(A):
        sorted_list.append(A[i])
        i+=1
    while j<len(B):
        sorted_list.append(B[j])
        j+=1

    print(sorted_list)

A=[1,2,3,4,5,23]
B=[3,4,5,6,7]
merge_two_sorted_list(A,B)