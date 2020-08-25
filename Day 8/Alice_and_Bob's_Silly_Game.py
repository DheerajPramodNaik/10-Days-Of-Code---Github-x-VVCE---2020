def prime_check_fun(j):
    for i in range(2, int(j ** .5) + 1):
        if not j % i:
            return False
    return True
prime_list = [2]
def sillyGame(n):
    largest_prime_number = prime_list[-1]
    if n > largest_prime_number:
        for i in range(largest_prime_number + 1, n + 1):
            if prime_check_fun(i): 
                prime_list.append(i)
    return 'Alice' if sum(i <= n for i in prime_list) % 2 else 'Bob'

if __name__ == '__main__':

    g = int(input())

    for g_itr in range(g):
        n = int(input())

        result = sillyGame(n)
        print(result)