# POLYBRUTUS 13D — Exact Euclidean metric and sevenfold ideal graph mode

**Human author and scientific responsibility:** Gabriel St-Pierre (Topbrutus), independent researcher.  
**Scientific status:** exact reproducible computational case study, no human peer review.  
**AI-use disclosure:** OpenAI ChatGPT (Astra) substantially assisted symbolic computation, rational independent checking, research note drafting and GitHub/Zenodo publication operations. AI is not an author.

## Exact results at radius R=1

- **18 labelled vertices**, **153** unordered pairwise squared distances, minimal Euclidean affine embedding dimension exactly **13**.
- Exact preservation of all **136/136** labelled squared distances from immutable Polybrutus 12D release.
- Exactly **17** new squared distances, all **2**, arising from one orthogonal unit vector.
- Eight normalized squared-distance families for `k=4d²/R²`: `{4:6,7:2,8:122,9:3,10:10,12:6,13:2,16:2}`.
- Squared-distance sum `1271 R²/4`.
- Exact symbolic certificate: coordinate-difference rank=13; centered squared-distance Gram rank=13; `B=(HX)(HX)^T`, proving positive semidefiniteness.
- **Chosen ideal graph model:** equal-mass scalar oscillators with complete-graph couplings `w_ij=R²/d²`. The model's weighted-Laplacian eigenvalue **9** has exact multiplicity **7**, and eigenvalue **17/2** has exact multiplicity **4**.
- Independent rational-distance verifier checks **153/153** labelled metric entries and both spectral multiplicities, without importing the generator; four deliberately invalid cases are rejected.

## Reproduce

```sh
python -m pip install sympy==1.14.0
python src/verify_d13.py
python tests/independent_d13.py
```

The `prior/` directory preserves the exact source chain and certificates of D08-D12 from the immutable parent tag `Topbrutus/polybrutus-d12@v0.1.0`, commit `e6ea0d1d174bcd9580e4d1d1c5c5dd2355cc935e`.

## Archive

`src/verify_d13.py` — exact symbolic construction, rank, PSD, spectral polynomial and four negative controls.  
`tests/independent_d13.py` — independent rational pairwise distances, centered Gram and direct multiplicity derivatives.  
`results/certificate_d13.json` — complete table of 153 labelled squared distances, exact invariants and proven model spectrum.  
`SPECIFICATION_D13.md`, `PREUVE_D13.md`, `PROVENANCE.md` — mathematical proof chain.  
`publication/POLYBRUTUS_13D_NOTE.pdf`, `.md` — unreviewed scientific note CC BY 4.0.  
`SHA256SUMS.txt` — tagged Git blob checksums. Source code MIT.

## Previous records

- Canonical seven-point geometry: https://github.com/Topbrutus/polybrutus/blob/main/SPECIFICATION.md
- 7D: https://doi.org/10.5281/zenodo.24407952
- 8D: https://doi.org/10.5281/zenodo.24408344
- 9D: https://doi.org/10.5281/zenodo.24408448
- 10D: https://doi.org/10.5281/zenodo.24408569
- 11D: https://doi.org/10.5281/zenodo.24408650
- 12D: https://doi.org/10.5281/zenodo.24408720

**Limits:** This is a *particular* affine metric extension. Orthogonal join and spectral shifts are established mathematics. The number 13 does not establish a new spacetime dimension, the historical 13R/base-13 hypothesis, or a new universal theorem.
