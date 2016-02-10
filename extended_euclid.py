# Extended euclid's algorithm

'''
How this works ?
https://web.stanford.edu/~dntse/classes/cs70_fall09/cs70_fall09_5.pdf

to  find modular inverse:
https://en.wikibooks.org/wiki/Algorithm_Implementation/Mathematics/Extended_Euclidean_algorithm#Modular_inverse

What is extended euclid's algorithm?
Extended Euclidean algorithm is an extension to the Euclidean algorithm, which computes, 
besides the greatest common divisor of integers a and b, the coefficients of Bézout's identity, that is integers x and y such that

ax + by = gcd(a, b).
'''

def GCD(k, m):
    # Base condition
    print k,m
    if m == 0:
        return k, 1, 0
    else:
        gcd, a, b = GCD(m,k%m)
        return gcd, b, a-(k/m)*b
    
    
if __name__ == "__main__":
    k = int(raw_input())
    m = int(raw_input())
    if k < m :
        temp = m
        k = m
        m = temp
    print GCD(k,m)
