
usage:
	@echo USAGE FIXME

recalculate-locked-dependencies:
	pip-compile --generate-hashes requirements.in

vendor/feather-icons@4.29.0.tar.gz:
	wget $$(npm view feather-icons@4.29.0 dist.tarball) -O $@

vendor/bootstrap@5.2.3.tar.gz:
	wget $$(npm view bootstrap@5.2.3 dist.tarball) -O $@

vendor/slim-js@5.0.10.tar.gz:
	wget $$(npm view slim-js@5.0.10 dist.tarball) -O $@
