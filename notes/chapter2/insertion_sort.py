

A = [5,2,4,6,1,3]

def insertion_sort(list):
    # Only changes the number in front of the number. Same sorting algorithm
    for j in range(1,len(list)):
        key = list[j]
        i = j-1

        while (i >= 0 and list[i] > key):
            list[i+1] = list[i]
            i=i-1


        list[i+1] = key

    return


insertion_sort(A)
