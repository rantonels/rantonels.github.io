import mpmath

mpmath.cplot( lambda z: mpmath.cot(z)*mpmath.cot(z/1j)/z, re=[-5,5],im=[-5,5], points=50000, verbose=True)


