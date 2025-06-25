# Onnx Runtime - Prebuilt

A lightweight, modular set of prebuilt ONNX Runtime binaries for different platforms and configurations (CPU/GPU).  
This repository provides minimal, version-controlled branches of ONNX Runtime release builds for easy use in C/C++ and Python projects — without requiring you to clone or build the full upstream ONNX Runtime repo (~1GB+).

## 🎯 Purpose

Many users just need:
- The shared `.dll`/`.so` libraries
- Header files
- And adding a git submodule might be sufficient.

This repo offers just that — a clean setup with optional chunked binaries (to bypass GitHub size limits), along with simple `make` rules to initialise or reassemble large files.

---

## 📦 Structure

Each usable platform (only video game OS and linux because fuck mac) with release version available as individual branches:
```
onnxruntime-<platform>-<version>
```

Examples:
- `onnxruntime-win-x64-gpu-1.22.0`
- `onnxruntime-linux-x64-1.22.0`

The default branch (`main`) provides a `makefile` to switch branches and initialise the correct binaries.

---

## 🛠 Usage

### Clone the repo:
```bash
git clone https://github.com/Le-o-n/onnxruntime-prebuilt.git
cd onnxruntime-prebuilt
```

### Initialise a platform branch:
```bash
make init PLATFORM=win-x64-gpu
```

This:
- Checks out the branch `onnxruntime-win-x64-gpu-1.22.0`
- Unchunks large `.dll` files if needed

### Chunk/Unchunk manually:
```bash
make chunk    # Breaks large binaries into parts
make unchunk  # Reassembles them
```

---

## 🧩 Why chunking?

Some binaries (e.g. CUDA `.dll`s) exceed GitHub’s 100MB limit.  
I split them into `.partNN` chunks and reassemble them on initialisation.

---

## 🧰 Requirements

- `make`
- `python3.7+` (tested on 3.11)
- Works on Linux and Windows

---

## ✅ Example: Using in your C/C++ project

Simply copy the `include/` and `lib/` folders into your project and link as usual:

```c
#include <onnxruntime_c_api.h>
```

Use `onnxruntime.dll` or `.so` at runtime, as needed.

---


