def merge_arrays(A, B):
    a = len(A)
    b = len(B)
    i = 0
    j = 0
    C = []

    while i < a and j < b:
        if A[i] < B[j]:
            C.append(A[i])
            i += 1
        else:
            C.append(B[j])
            j += 1

    while i < a:
        C.append(A[i])
        i += 1

    while j < b:
        C.append(B[j])
        j += 1

    return C

if __name__ == "__main__":
    size_A = int(input())
    arr1 = list(map(int, input().split()))

    size_B = int(input())
    arr2 = list(map(int, input().split()))

    merged_array = merge_arrays(arr1, arr2)
    for num in merged_array:
        print(num, end=" ")
