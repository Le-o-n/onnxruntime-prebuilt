.PHONY: init help
.DEFAULT_GOAL := help

PLATFORM ?=
BRANCH := onnxruntime-$(PLATFORM)

help:
	@echo "Usage: make init PLATFORM=<platform>"
	@echo "Example platforms:"
	@echo "  linux-x64"
	@echo "  win-x64-gpu"
	@echo "  osx-arm64"

init:
ifeq ($(strip $(PLATFORM)),)
	@$(MAKE) help
	@echo "[ERROR] PLATFORM not specified."
	exit 1
endif
	@echo "[INFO] Switching to branch: $(BRANCH)"
	@git fetch origin $(BRANCH)
	@git checkout $(BRANCH)
	@echo "[INFO] Running 'make init' on branch: $(BRANCH)"
	@$(MAKE) init
