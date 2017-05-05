import mpmath

tpij = 2*mpmath.pi*1j

def eta(t):
    q124 = mpmath.exp(tpij * t / 24)
    q = mpmath.exp(tpij * t)
    return q124*mpmath.qp(q,q)

mpmath.cplot( eta, re=[-1.1,1.1],im=[0.00001,0.5], points=1000000, verbose=True)


