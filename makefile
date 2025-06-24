.PHONY: chunk unchunk init

init: unchunk
	@echo " [INFO] Done Initialisation"
chunk: 
	python3 scripts/chunker.py chunk ./lib/libonnxruntime_providers_cuda.so --output ./lib/ 

unchunk:
	python3 scripts/chunker.py unchunk "./lib/libonnxruntime_providers_cuda.so.part*" --output ./lib/libonnxruntime_providers_cuda.so --clean


