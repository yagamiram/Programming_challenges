'''
Find the power m^n
source:
https://web.stanford.edu/class/cs97si/02-mathematics.pdf

Base case:
1.If n == 0 return 1
2. If n == 1 return m

Recursive case:
1. If the power is even then divide by 2 and
     call recursively
2. Else # odd case
    divide n-1/2 and call recursively and
    at the end multiply m*rec_call*rec_call
    
complexity is O(log n)

More elegant approach (C++):
double pow(double a, int n) {
     if(n == 0) return 1;
     if(n == 1) return a;
     double t = pow(a, n/2);
     return t * t * pow(a, n%2);
}

'''

def power(m, n):
    if n == 0:
        return 1
    elif n == 1:
        return m
    else:
        # check if m is odd or even
        if n % 2  == 0:
            # even
            value =  power(m, n/2)
            return value * value
        else:
            # odd
            value = power(m, (n-1)/2)
            return m*value*value
        
print power(-15,6)
