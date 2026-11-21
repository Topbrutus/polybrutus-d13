# Exact certificate — Polybrutus 13D

## 1. Labelled distance preservation

Embed all 17 exact parent points `p_i` as `q_i=(p_i,0)` and adjoin `q18=e14` orthogonal to every old vector. All vectors have unit norm. Consequently each new squared distance equals
```
||q18-q_i||² = ||q18||²+||q_i||²-2<q18,q_i>=2.
```
The other 136 labelled distances are unchanged. There are `153=C(18,2)` pairs, eight normalized families with counts `{4:6,7:2,8:122,9:3,10:10,12:6,13:2,16:2}`, and the squared-distance sum is `1271/4` at R=1.

## 2. Proof of minimal Euclidean affine dimension

Let `X` be the 18-by-14 algebraic coordinate matrix, `D` its squared labelled Euclidean distance matrix and `H=I-11ᵀ/18` the centering matrix. The primary program proves exactly:
```
rank([q2-q1,...,q18-q1]) = 13
rank(B) = 13
B = -H D H/2 = (H X)(H X)^T
```
The right-hand factorization proves Gram positive semidefiniteness. Every Euclidean realization of this *same labelled metric* shares its centered Gram matrix, so its minimal affine embedding dimension is precisely thirteen. The storage representation has one exact constraint in its five-simplex coordinate block, explaining why 14 storage slots are not fourteen intrinsic affine dimensions.

## 3. Ideal oscillator weighted-Laplacian spectrum

Choose **a theoretical** equal-mass scalar-oscillator complete graph with weights `w_ij=1/d_ij²` for unit radius. For `L12`, the previous 17-point weighted Laplacian, a new point with 17 identical weight-1/2 edges yields

```
L13 = [ L12 + (1/2)I17  -(1/2)1 ]
      [ -(1/2)1ᵀ           17/2  ]
```

Thus the monic characteristic polynomial satisfies the rank-one-join identity

```
chi18(z)=z(z-9)chi17(z-1/2)/(z-1/2).
```

The parent has `chi17(z)=z(z-17/2)^6(z-8)^4 f6(z-5)` where `f6=chiP7/z` carries the original seven-point graph's six nonzero modes. Substitution gives

```
chi18(z)=z(z-9)^7(z-17/2)^4 f6(z-11/2).
```

The primary verifier calculates the **18-by-18 polynomial exactly**, proving direct equality to the recurrence and closed form. Evaluating `f6(7/2)` and `f6(3)` gives nonzero values; therefore the eigenvalue multiplicities are *exactly* 7 at 9, and 4 at 17/2.

The secondary verifier derives the 153 pairwise squared distances independently from rational structural rules, obtains the rank-13 centered Gram matrix, reconstructs the 18-by-18 Laplacian, and proves both multiplicities through derivatives of its characteristic polynomial.

## 4. Falsification and limitations

Four negative controls reject a tampered squared distance, an exact duplicate new point, an added point tilted toward the original core, and a permutation of labels preserving the unlabelled distance histogram.

All calculations are exact symbolic/rational mathematics. The orthogonal join and uniform graph spectral shift are known techniques. This case does not establish a new physical dimension, an independent experimental resonance, a new universal mathematical theorem, or the historical significance of the number 13.
