# Enter your code here. Read input from STDIN. Print output to STDOUT
import numpy as np

for i in range(int(input())):
    n = input()
    gpa = list(map(float, input().split()))
    max_coef = -2
    for j in range(0, 5):
        test_marks = list(map(float, input().split()))
        coef = np.corrcoef(gpa, test_marks)[0, 1]
        if coef > max_coef:
            max_coef = coef
            max_j = j
    print(max_j + 1)