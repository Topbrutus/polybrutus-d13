#!/usr/bin/env python3
"""Independent D13 rational metric and graph-spectrum verification.

No import of any source generator. The 18-labelled-point metric uses the
seven original points (x=a*sqrt3, y,z), five 4-simplex vertices, and six
successive orthogonal unit vectors. Rebuilds all 153 squared distances.
"""
from pathlib import Path
from collections import Counter
from fractions import Fraction as F
from itertools import combinations
import hashlib,json
import sympy as s

ROOT=Path(__file__).resolve().parents[1]
report=json.loads((ROOT/"results"/"certificate_d13.json").read_text(encoding="utf8"))
parent=json.loads((ROOT/"prior"/"certificate_d12.json").read_text(encoding="utf8"))
core=[
 (F(0),F(0),F(1)),(F(1,2),F(0),F(1,2)),
 (F(-1,4),F(3,4),F(1,2)),(F(-1,4),F(-3,4),F(1,2)),
 (F(0),F(0),F(-1)),(F(1,2),F(0),F(-1,2)),
 (F(-1,2),F(0),F(-1,2))
]
def sqdist(i,j):
    if i==j:return F(0)
    if i<7 and j<7:
        a,b,c=(core[i][k]-core[j][k] for k in range(3))
        return 3*a*a+b*b+c*c
    if 7<=i<12 and 7<=j<12:return F(5,2)
    return F(2)

pairs=list(combinations(range(18),2))
expected={(i+1,j+1):sqdist(i,j) for i,j in pairs}
observed={(int(x["i"]),int(x["j"])):F(x["d2"])
          for x in report["labelled_squared_distances"]}
assert len(expected)==153 and expected==observed
old={(int(x["i"]),int(x["j"])):F(x["d2"])
     for x in parent["labelled_squared_distances"]}
assert len(old)==136 and all(expected[k]==v for k,v in old.items())
assert all(sqdist(i,17)==F(2) for i in range(17))
hist=Counter(4*sqdist(i,j) for i,j in pairs)
assert hist==Counter({F(4):6,F(7):2,F(8):122,F(9):3,F(10):10,F(12):6,F(13):2,F(16):2})
assert sum(expected.values(),F(0))==F(1271,4)
D=s.Matrix(18,18,lambda i,j:s.Rational(sqdist(i,j).numerator,sqdist(i,j).denominator))
H=s.eye(18)-s.ones(18)/18
B=-H*D*H/2
assert B.rank()==13
D12=D[:17,:17];H12=s.eye(17)-s.ones(17)/17
assert (-H12*D12*H12/2).rank()==12

L=s.zeros(18)
for i,j in pairs:
    w=1/D[i,j]
    L[i,i]+=w;L[j,j]+=w
    L[i,j]-=w;L[j,i]-=w
z=s.Symbol("z");poly=L.charpoly(z).as_expr()
for value,multiplicity in [(s.Integer(9),7),(s.Rational(17,2),4)]:
    assert all(s.simplify(s.diff(poly,z,k).subs(z,value))==0 for k in range(multiplicity))
    assert s.simplify(s.diff(poly,z,multiplicity).subs(z,value))!=0
assert report["affine_rank"]==report["centered_gram_rank"]==13
assert report["parent_distances_preserved"]==136 and report["new_distances"]==17
p=ROOT/"results"/"certificate_d13.json"
print("INDEPENDENT D13 PASS: 153 exact rational labelled distances, parent 136/136, Gram rank 13")
print("INDEPENDENT IDEAL GRAPH PASS: eigenvalue 9 x7, eigenvalue 17/2 x4")
print("CERTIFICATE_SHA256="+hashlib.sha256(p.read_bytes()).hexdigest())
