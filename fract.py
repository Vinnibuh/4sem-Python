#!/usr/bin/env python3
     
def simplify(p, q):
    n, d = abs(p), abs(q)
    while d != n:
        if d > n:
            d = d - n
        else:
            n = n - d
    p, q = p // d, q // d
    return (p, q)
       
class Fraction:
    def __init__(self, p = 1, q = 1):
        if q == 0:
            raise ZeroDivisionError
        elif p == 0:
            self.p, self.q = 0, 1
        else:
            self.p, self.q = simplify(p, q)
    def add(self, other):
        return Fraction(self.p*other.q + self.q*other.p,self.q*other.q)
    def mply(self, other):
        return Fraction(self.p*other.p, self.q*other.q)
    def div(self, other):
        if other.p == 0:
            raise ZeroDivisionError
        return Fraction(self.p*other*q, self.q*other.p)
    def isint(self):
        if self.q == 1:
            return True 
        else:
            return False

