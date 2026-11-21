# Polybrutus D13 — Formal configuration

**Parent source:** `Topbrutus/polybrutus-d12@v0.1.0`, commit `e6ea0d1d174bcd9580e4d1d1c5c5dd2355cc935e`, DOI `10.5281/zenodo.24408720`.

Let `P={p1,...,p17}` denote the previous 12D configuration of unit-radius vectors, represented in **13 storage coordinates** with one regular-simplex hyperplane relation. Embed `q_i=(p_i,0)` in 14 storage-coordinate slots for i=1..17. Append `q18=e14=(0,...,0,1)`.

Exactly 18 points have norm `R=1`. The new unit point is orthogonal to each old vector:

```
d(q_i,q18)^2 = 2,    i=1,...,17.
```

All **136** predecessor labelled squared distances are preserved; precisely **17** new squared distances are 2. For general `R>0`, multiply all coordinates by `R`, making the new squared distances `2R²`.

- Intrinsic affine dimension **13**, although storage uses 14 coordinate slots.
- Vertices **18**; unordered pairs **153**.
- Normalized histogram for `k=4d²/R²`: `4:6,7:2,8:122,9:3,10:10,12:6,13:2,16:2`.
- Exact sum of pairwise squared distances: `1271 R²/4`.
- Centroid, R=1, storage coordinates: `(0,0,1/36,0,0,0,0,0,1/18,1/18,1/18,1/18,1/18,1/18)`.

**Ideal graph-Laplacian model:** With `w_ij=R²/d_ij²` and equal scalar unit masses, all new couplings are 1/2. The spectrum satisfies

```
chi18(z) = z(z-9)chi17(z-1/2)/(z-1/2)
         = z(z-9)^7(z-17/2)^4 f6(z-11/2),
 f6(z) = chiP7(z)/z.
```

Eigenvalue 9 has multiplicity exactly 7; eigenvalue 17/2 has multiplicity exactly 4. This is a selected mathematical model, not experimental physics.
