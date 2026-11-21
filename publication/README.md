# Polybrutus D13 archival release protocol

This is a computational mathematical preprint. Neither novelty of the general orthogonal completion nor a new physical spacetime dimension is claimed. The paper includes human author credit, AI disclosure and limitations.

1. Run `src/verify_d13.py` and `tests/independent_d13.py` with SymPy 1.14.0.
2. Publish a private GitHub candidate and a GitHub Actions workflow; get a successful run.
3. Freeze a verified source commit as `v0.1.0`. Create ZIP **from git archive at that tag**.
4. Record PDF, source ZIP and exact labelled-distance certificate SHA-256.
5. Stage a single Zenodo direct-API draft; check the author, source tag, AI disclosure, DOI ancestry, license and each of the three file checksums.
6. Make GitHub public, verify immutable tag publicly and publish the **existing** Zenodo draft.
7. Verify DOI and Zenodo file integrity through its public REST API; write DOI into README, citation, release manifest and central Memoria registry.

Avoid parallel GitHub/Zenodo automatic archive harvesting (duplicate records). Never publish API tokens, secrets or private conversational files.
