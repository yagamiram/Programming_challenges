# GCD of two numbers using Euclid's algorithm
# Find remainder of the two numbers
# The divisor whose remainder is 0 is GCD

'''
How this works ?

Get the remainder of the two numbers (larger number % smaller number)
Now assign the smaller number to the larger number
and the remainder as the smaller number
do it recursively until the remainder becomes 0

int gcd(int a, int b) {
while(b){int r = a % b; a = b; b = r;}
return a;
}


complexity is : O(log(a+b))
'''

def GCD(k, m):
    # Base condition
    print k,m
    if m == 0:
        return k
    else:
        r = k % m
        k = m
        m = r
        return GCD(k,m)
    
    
if __name__ == "__main__":
    k = int(raw_input())
    m = int(raw_input())
    if k < m :
        temp = m
        k = m
        m = temp
    print GCD(k,m)
