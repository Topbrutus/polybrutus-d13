# Polybrutus 13D: Exact Conservative Euclidean Completion and a Sevenfold Weighted-Graph Mode

**Research author:** Gabriel St-Pierre  
**Affiliation:** Independent researcher  
**Project:** Polybrutus-X72  
**Date:** 20 November 2026  
**Version:** 0.1.0  
**Publication status:** Reproducible mathematical preprint; not independently peer reviewed  
**Parent record:** Polybrutus 12D, DOI 10.5281/zenodo.24408720  
**Frozen source:** https://github.com/Topbrutus/polybrutus-d13/tree/v0.1.0 (once published)

## Abstract

An exact **18-point labelled Euclidean distance configuration** of **minimal affine embedding dimension 13** is constructed by conservatively extending the archived Polybrutus 12D metric. The seventeen old points and **all 136 old pairwise squared distances** are preserved exactly. One new orthogonal unit vector adds **17 squared distances of value 2R²**, yielding **153 distinct labelled pair distances** distributed among eight exact normalized classes. The minimal affine rank 13 is certified both from the exact coordinate difference matrix and from the exact rank of the centered squared-distance Gram matrix, with an explicit positive-semidefinite factorization.

A separately implemented rational verifier reconstructs all **153 labelled** squared distances without importing the geometric source and confirms the centered Gram rank. For a **deliberately chosen ideal weighted-graph scalar-oscillator model**, the exact characteristic polynomial has an eigenvalue at **9 of multiplicity 7** and at **17/2 of multiplicity 4**, both checked independently. This is a case study in known orthogonal-completion and graph-spectral techniques. It is not a newly demonstrated physical spacetime dimension, a universal theorem of novel mathematics, or a measurement of a physical apparatus.

## 1. Provenance and research scope

The canonical Polybrutus construction consists of **seven analytically defined points** on a sphere in three-dimensional Euclidean space. A previously published seven-dimensional completion adjoined five vertices of a regular four-dimensional simplex in an orthogonal subspace, preserving the seven-point distances exactly while reaching twelve vertices and sixty-six labelled pairs (DOI **10.5281/zenodo.24407952**).

The extension lineage subsequently archived separate, reproducible metric cases: Polybrutus **8D**, 13 vertices and 78 pairs (DOI **10.5281/zenodo.24408344**); **9D**, 14 and 91 pairs (DOI **10.5281/zenodo.24408448**); **10D**, 15 and 105 pairs (DOI **10.5281/zenodo.24408569**); **11D**, 16 and 120 pairs (DOI **10.5281/zenodo.24408650**); and **12D**, 17 and 136 pairs (DOI **10.5281/zenodo.24408720**).

The present computation **reuses the immutable source tag** `Topbrutus/polybrutus-d12@v0.1.0`, commit `e6ea0d1d174bcd9580e4d1d1c5c5dd2355cc935e`. That exact source and all required ancestor code and certificates are carried unchanged in `prior/` of the 13D code archive. The parent geometry is not silently reconstructed from an approximation or modified.

## 2. Exact eighteen-point Euclidean metric

Normalize the radius to `R=1`. Let `p1,...,p17` be the seventeen previously verified D12 vectors stored in thirteen coordinate slots. Their effective affine rank is twelve because the five-simplex storage block has one fixed linear relation.

Embed every parent point into fourteen storage coordinates as:

```
q_i = (p_i,0)       for i=1,...,17.
```

Append a unit basis vector in the new fourteenth storage coordinate:

```
q18 = e14 = (0,0,0,0,0,0,0,0,0,0,0,0,0,1).
```

The new vector is orthogonal to every old vector. All eighteen points lie on the unit sphere, and all 136 original pair distances are identical. For every old index `i`:

```
||q18 - q_i||² = ||q18||²+||q_i||²-2<q18,q_i> = 2.
```

Thus the new metric has `136 + 17 = C(18,2) = 153` unordered labelled pairs. For an arbitrary radius `R>0`, scaling every coordinate by `R` gives each new squared distance exactly `2R²`.

The exact normalized squared-distance classes `k=4d²/R²` and multiplicities are:

| k | 4 | 7 | 8 | 9 | 10 | 12 | 13 | 16 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| Multiplicity | 6 | 2 | **122** | 3 | 10 | 6 | 2 | 2 |

The total of these eight counts is **153**. The full squared-distance sum is **1271R²/4**. At normalized radius the exact centroid of the eighteen points in the fourteen storage coordinates is:

```
G = (0,0,1/36,0,0,0,0,0,1/18,1/18,1/18,1/18,1/18,1/18).
```

The thirteen-dimensional claim concerns the **minimal affine embedding dimension of the labelled Euclidean metric**. Fourteen coordinate storage slots do not imply fourteen independent affine directions.

## 3. Exact certificate of minimum affine dimension

Write `D` for the **18-by-18** matrix whose entry `D[i,j]` is the **squared** Euclidean distance between labelled vertices `q_i` and `q_j`. Let `X` be the exact **18-by-14** coordinate array and `H=I-11ᵀ/18` be the symmetric centering matrix.

The centered Euclidean distance Gram matrix is defined from the labelled metric by:

```
B = -1/2 H D H.
```

The main symbolic program independently proves the following three exact identities:

```
rank([q2-q1,...,q18-q1]) = 13
rank(B) = 13
B = (H X)(H X)^T
```

The last equation is a factorization proving **positive semidefiniteness** without relying on floating-point eigenvalues. Every Euclidean realization of these **same 153 labelled squared distances** yields this unique centered Gram matrix, so no Euclidean realization of this exact metric can have affine rank different from thirteen. This is a metric-rank certificate, not a statement about dimensionality of physical spacetime.

A second verifier independently reconstructs the 153 squared distances using rational arithmetic for the seven canonical original positions; squared distance `5/2` between five regular-simplex vertices; and squared distance `2` for all appropriate pairs involving the six additional orthogonal unit points or orthogonal groups. It reproduces the table **153/153**, confirms the 136 parent entries, and independently recomputes the centered Gram rank 13.

## 4. Sevenfold ideal weighted-graph mode

As a **chosen theoretical model**, place equal-mass scalar displacements on all eighteen vertices, with complete-graph couplings of normalized strength `w_ij = R²/d_ij²`. No physical oscillator is claimed to have been constructed; the assigned weights are a mathematical modelling rule.

For normalized unit radius, every coupling involving the newly added vertex is `1/2`. Let `L12` be the prior **17-by-17** graph Laplacian. The full 18-by-18 Laplacian is:

```
L13 = [ L12+(1/2)I17       -(1/2)1 ]
      [ -(1/2)1ᵀ              17/2 ]
```

Writing `chi17(z)=det(z I-L12)` and `chi18(z)=det(z I-L13)`, a decomposition into uniform, intergroup and old zero-sum modes yields the exact recurrence:

```
chi18(z) = z(z-9)chi17(z-1/2)/(z-1/2).
```

The published 12D source established an exact factorization:

```
chi17(z) = z(z-17/2)^6(z-8)^4 f6(z-5),
f6(z) = chiP7(z)/z,
```

where `chiP7(z)` is the polynomial of the original seven-point complete weighted Laplacian and `f6` carries its six nonzero modes. Substitution gives:

```
chi18(z) = z(z-9)^7(z-17/2)^4 f6(z-11/2).
```

The primary program computes the **complete exact 18-by-18 characteristic polynomial** and verifies both this expression and the recurrence. To rule out additional hidden multiplicities, it evaluates `f6(7/2)` and `f6(3)` and verifies both are nonzero.

Consequently the model has **exactly seven modes at eigenvalue 9**, and **exactly four modes at eigenvalue 17/2**. The independent rational-distance program constructs the full weighted graph by its own route and confirms these multiplicities using derivatives of the exact characteristic polynomial.

These eigenvalues are **dimensionless** under the chosen normalization. They are not frequencies in hertz and do not determine any physical particle mass, Higgs coupling or measurement.

## 5. Reproducibility, negative controls and falsifiability

The frozen public source archive contains the full source chain in `prior/`, the main program `src/verify_d13.py`, the independent program `tests/independent_d13.py`, the exact JSON certificate `results/certificate_d13.json` with all **153 labelled distances**, the formal geometry specification, provenance, SHA-256 integrity index and continuous GitHub Actions verification.

Run:

```sh
python -m pip install sympy==1.14.0
python src/verify_d13.py
python tests/independent_d13.py
```

Both programs must report PASS and the same SHA-256 for the JSON certificate. Four deliberate invalid variants are separately rejected: a changed squared distance, a duplicated new vertex, a nonorthogonal proposed vertex and a point-label permutation that preserves the unlabelled multiset of distances but changes the labelled metric.

A Git archive produced directly from the frozen scientific source tag, the complete PDF note and the JSON certificate are the three Zenodo archival files. Their file hashes identify what was actually deposited.

## 6. Novelty, limitations, and relation to the number thirteen

The orthogonal metric-completion mechanism is standard Euclidean distance geometry. A uniform half-weight graph join and its spectral shift are established graph-matrix facts. This particular **13D case**, its exact complete metric and the specific sevenfold eigenvalue are a reproducible computation within the Polybrutus programme; they do **not** prove a novel universal mathematical law.

The repeated number **13** may invite comparisons with the Polybrutus research vocabulary of base-13, 13R cycles and earlier physical conjectures. No such relation has been mathematically deduced from the present labelled metric. There is **no** demonstrated new physical spacetime dimension, no physical experiment, no measured resonance frequency and no claim of independent peer review.

## 7. Human responsibility, AI disclosure, licensing

**Research author and responsible investigator:** Gabriel St-Pierre (independent researcher). The original Polybrutus geometry, the research programme and authorization to deposit each dimensional case originate with him.

**Generative AI disclosure:** OpenAI ChatGPT (Astra) substantially assisted in source inspection, symbolic geometry and rank proof, implementing the main and independently coded rational checkers, modelling ideal weighted-graph spectra, provenance verification, drafting this note and organizing the archived release. AI is **not listed as an author**. Human scientific peer review has not yet occurred.

**Licenses:** scientific note and prose CC BY 4.0; source programs MIT.

**Source references:** original Polybrutus seven-point geometry, https://github.com/Topbrutus/polybrutus/blob/main/SPECIFICATION.md ; D07 DOI https://doi.org/10.5281/zenodo.24407952 ; D08 https://doi.org/10.5281/zenodo.24408344 ; D09 https://doi.org/10.5281/zenodo.24408448 ; D10 https://doi.org/10.5281/zenodo.24408569 ; D11 https://doi.org/10.5281/zenodo.24408650 ; D12 https://doi.org/10.5281/zenodo.24408720 ; frozen source https://github.com/Topbrutus/polybrutus-d12/tree/v0.1.0 .
