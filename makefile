.PHONY: chunk unchunk init

init: unchunk

chunk: 
	python scripts/chunker.py chunk ./lib/onnxruntime_providers_cuda.dll --output ./lib/ 

unchunk:
	python scripts/chunker.py unchunk "./lib/onnxruntime_providers_cuda.dll.part*" --output ./lib/onnxruntime_providers_cuda.dll --clean


