import argparse
import os
import glob
from pathlib import Path

CHUNK_SIZE_MB = 20
CHUNK_SIZE = CHUNK_SIZE_MB * 1024 * 1024


def verbose_print(msg):
    print(f"[INFO] {msg}")


def chunk_file(file_path, output_dir):
    file_path = Path(file_path)
    output_dir = Path(output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    verbose_print(f"Starting chunking of: {file_path}")
    verbose_print(f"Chunk size: {CHUNK_SIZE_MB} MB")
    verbose_print(f"Output directory: {output_dir}")

    with open(file_path, 'rb') as infile:
        i = 1
        while chunk := infile.read(CHUNK_SIZE):
            part_filename = output_dir / f"{file_path.name}.part{i:02}"
            with open(part_filename, 'wb') as outfile:
                outfile.write(chunk)
            verbose_print(f"Written chunk: {part_filename} ({len(chunk)} bytes)")
            i += 1

    verbose_print("✅ Chunking completed.")


def unchunk_files(input_glob, output_file, clean=False):
    files = sorted(glob.glob(input_glob))
    if not files:
        print(f"[ERROR] No files found matching pattern: {input_glob}")
        return

    output_file = Path(output_file)
    output_file.parent.mkdir(parents=True, exist_ok=True)

    verbose_print(f"Found {len(files)} chunks to join:")
    for f in files:
        verbose_print(f" - {f}")

    expected_total_size = sum(os.path.getsize(f) for f in files)
    verbose_print(f"Expected total output size: {expected_total_size} bytes")

    written_bytes = 0

    with open(output_file, 'wb') as outfile:
        for chunk_file in files:
            with open(chunk_file, 'rb') as infile:
                chunk_data = infile.read()
                outfile.write(chunk_data)
                written_bytes += len(chunk_data)
                verbose_print(f"Appended {chunk_file} ({len(chunk_data)} bytes)")

    verbose_print(f"✅ Unchunking complete: {output_file}")
    verbose_print(f"Total bytes written: {written_bytes} bytes")

    if written_bytes == expected_total_size:
        verbose_print("✅ Output file size matches total input size.")
        if clean:
            verbose_print("🧹 Cleaning up chunk parts...")
            for f in files:
                try:
                    os.remove(f)
                    verbose_print(f"Deleted: {f}")
                except Exception as e:
                    print(f"[WARN] Failed to delete {f}: {e}")
    else:
        print("❌ Byte mismatch! Not cleaning up parts.")
        print(f"Expected: {expected_total_size}, Written: {written_bytes}")


def main():
    parser = argparse.ArgumentParser(description="Chunk or unchunk large binary files")
    parser.add_argument("mode", choices=["chunk", "unchunk"], help="Operation mode")
    parser.add_argument("input", help="Input file path (chunk) or wildcard path (unchunk)")
    parser.add_argument("--output", required=True, help="Output directory (chunk) or output file path (unchunk)")
    parser.add_argument("--clean", action="store_true", help="Delete chunk files after unchunking")

    args = parser.parse_args()

    if args.mode == "chunk":
        chunk_file(args.input, args.output)
    elif args.mode == "unchunk":
        unchunk_files(args.input, args.output, clean=args.clean)


if __name__ == "__main__":
    main()
