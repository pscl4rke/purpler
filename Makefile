
recalculate-locked-dependencies:
	pip-compile --generate-hashes requirements.in

vendor/feather-icons@4.29.0.tar.gz:
	wget $$(npm view feather-icons@4.29.0 dist.tarball) -O $@
