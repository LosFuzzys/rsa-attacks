'''
Created on Sep 07, 2016

@author: verr
    
'''

import ContinuedFractions, Arithmetic

def hack_RSA(e,n):
    '''
    Finds d knowing (e,n)
    applying the Wiener continued fraction attack
    '''
    frac = ContinuedFractions.rational_to_contfrac(e, n)
    convergents = ContinuedFractions.convergents_from_contfrac(frac)
    
    for (k,d) in convergents:
        
        #check if d is actually the key
        if k!=0 and (e*d-1)%k == 0:
            phi = (e*d-1)//k
            s = n - phi + 1
            # check if the equation x^2 - s*x + n = 0
            # has integer roots
            discr = s*s - 4*n
            if(discr>=0):
                t = Arithmetic.is_perfect_square(discr)
                if t!=-1 and (s+t)%2==0:
                    print("Hacked!")
                    return d
    return None
    

if __name__ == "__main__":
    e = None
    n = None
    c = None

    # calculate d from e and n
    if e is not None and n is not None:
        d = hack_RSA(e, n)
        print 'd = %d' % d

    # decrypt c using d and n
    if c is not None and d is not None:
        p = pow(c, d, n)
        print 'p = %d' % p

