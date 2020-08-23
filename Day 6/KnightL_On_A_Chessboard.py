import math
import os
import random
import re
import sys

def knightlOnAChessboard(n):
    answer = [[0]*(n-1) for _ in range(n-1)]
    for i in range(1, n):
        for j in range(1, n):
            if j <= i:
                answer[i-1][j-1] = newknightlOnAChessboard(n, i, j)
    for i in range(1, n):
        for j in range(1, n):
            if j > i:
                answer[i-1][j-1] = answer[j-1][i-1]
    return answer

def newknightlOnAChessboard(n, a, b):
    if n < a or n < b:
        return False
    else:
        hash_ = {}
        for i in range(n):
            for j in range(n):
                hash_[(i,j)] = set()
                for u in [(i-a, j-b), (i+a, j-b), (i-a, j+b), (i+a, j+b), (i-b, j+a), (i-b, j-a), (i+b, j+a),(i+b, j-a)]:
                    if u[0]>=0 and u[0]<=n-1 and u[1]>=0 and u[1]<=n-1:
                        hash_[(i,j)].add((u[0],u[1]))
        stack_ = []
        shortest_distance = {}
        
        stack_.append((0,0))
        point = stack_[0]
        shortest_distance[(0,0)] = (0, None)
        
        def destination(s, stack_, hash_):
            if s == stack_[-1]:
                for item in hash_[s]:
                    if item not in stack_:
                        return False
                return True
        
        while point != stack_[-1] or (not destination(point, stack_, hash_)):
            if point != stack_[-1]:
                for v in hash_[point]:
                    if v not in stack_:
                        stack_.append(v)
                        shortest_distance[v] = (shortest_distance[point][0]+1, point)
                    else:
                        if shortest_distance[v][0] > shortest_distance[point][0]:
                            shortest_distance[v] = (shortest_distance[point][0]+1, point)
                
                point = stack_[stack_.index(point)+1]
            else:
                for v in hash_[point]:
                    if v not in stack_:
                        stack_.append(v)
                        shortest_distance[v] = (shortest_distance[point][0]+1, point)
                        
                point = stack_[stack_.index(point)+1]
        if (n-1, n-1) in shortest_distance:
            return shortest_distance[(n-1, n-1)][0]
        else:
            return -1




if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    result = knightlOnAChessboard(n)

    fptr.write('\n'.join([' '.join(map(str, x)) for x in result]))
    fptr.write('\n')

    fptr.close()