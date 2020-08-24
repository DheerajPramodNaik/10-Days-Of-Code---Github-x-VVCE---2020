def countSort(arr):
    for i in arr:
        i[0] = int(i[0])    
    for i in range(len(arr)//2):
        arr[i][1] = "-"
    answer = [[] for j in range(len(arr))]
    for i in arr:
        answer[i[0]].append(i[1])
    for i in answer:
        for j in i:
            print(j,end=" ")


if __name__ == '__main__':
    n = int(input().strip())
    arr = []
    for _ in range(n):
        arr.append(input().rstrip().split())
    countSort(arr)