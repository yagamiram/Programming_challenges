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

How to find x and y values?
algorithm extended-gcd(x,y)
    if y = 0 then return(x, 1, 0)
    else
        (d, a, b) := extended-gcd(y, x mod y)
        return((d, b, a - (x div y) * b))
How it works?
d = gcd(y, x mod y)
so 
d = gcd(y, x mod y) = ay + (x mod y)b 

this become 

d = bx + (a-(x/y)b)y

what is modulo inverse?
modular multiplicative inverse of an integer a modulo m is an integer x such that

ax = 1 mod m (congruency)
Example:
Find modulo multiplcative inverse of 3 modulo 11.

x = 1/3 modulo 11

you have to find x here.
3x = 1 mod 11
if x = 4 then 3x = 12 
so 12 mod 11 = 1 = 1 mod 11

so x = 4

This can be found using extended euclid
If the extended euclid returns 1 then modulo inverse of an integer is x % m
Find the modulo inverse of 'a'

def modinv(a, m):
    gcd, x, y = egcd(a, m)
    if gcd != 1:
        return None  # modular inverse does not exist
    else:
        return x % m

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
