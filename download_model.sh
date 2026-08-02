#!/usr/bin/env bash
# Download the Baarali Edge model weights.
#
# Contract imposed by the ADTC template:
#   - idempotent (safe to run twice),
#   - no credentials (public URL only),
#   - output path identical to `_runtime.model_path` in metadata.json.
#
# Two things this script does beyond the letter of that contract, because the
# profiler is unforgiving about both:
#
#   1. The download lands in a `.partial` file and is renamed only on success.
#      An interrupted run must not leave a truncated .gguf that looks complete —
#      llama.cpp would fail deep inside the profiler with a confusing error.
#   2. The finished file is checked against a published SHA-256. A silently
#      corrupted download would be scored as a bad model rather than as a bad
#      download, and we would never know which one we were looking at.

set -euo pipefail

HERE="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
MODEL_DIR="$HERE/model"

MODEL_NAME="Qwen3.5-2B-IQ4_XS.gguf"
MODEL_FILE="$MODEL_DIR/$MODEL_NAME"
MODEL_URL="https://huggingface.co/Benewende-dev/baarali-edge-2b/resolve/main/$MODEL_NAME?download=true"
MODEL_SHA256="3639f34b5ca22aa1c51f3616566eae8c355111554f6924ad97ee2652ed11c1cd"
MODEL_BYTES="1172996352"

verifier() {
  local fichier="$1"
  local somme
  if command -v sha256sum > /dev/null 2>&1; then
    somme="$(sha256sum "$fichier" | cut -d' ' -f1)"
  elif command -v shasum > /dev/null 2>&1; then
    somme="$(shasum -a 256 "$fichier" | cut -d' ' -f1)"
  else
    echo "warning: no sha256 tool found — skipping integrity check" >&2
    return 0
  fi
  if [[ "$somme" != "$MODEL_SHA256" ]]; then
    echo "error: checksum mismatch for $fichier" >&2
    echo "  expected $MODEL_SHA256" >&2
    echo "  got      $somme" >&2
    return 1
  fi
}

mkdir -p "$MODEL_DIR"

if [[ -f "$MODEL_FILE" ]]; then
  if verifier "$MODEL_FILE"; then
    echo "model already present and verified: $MODEL_FILE"
    exit 0
  fi
  echo "existing file failed verification — re-downloading" >&2
  rm -f "$MODEL_FILE"
fi

echo "downloading $MODEL_NAME (~1.1 GiB)…"

if command -v curl > /dev/null 2>&1; then
  # -C - resumes a partial file: on a metered or unstable link, restarting a
  # gigabyte from zero is not an acceptable failure mode.
  curl -L --fail --progress-bar -C - -o "$MODEL_FILE.partial" "$MODEL_URL"
elif command -v wget > /dev/null 2>&1; then
  wget --continue --show-progress -O "$MODEL_FILE.partial" "$MODEL_URL"
else
  echo "error: neither curl nor wget found" >&2
  exit 1
fi

taille="$(wc -c < "$MODEL_FILE.partial" | tr -d ' ')"
if [[ "$taille" != "$MODEL_BYTES" ]]; then
  echo "error: expected $MODEL_BYTES bytes, got $taille — download incomplete" >&2
  exit 1
fi

verifier "$MODEL_FILE.partial"
mv "$MODEL_FILE.partial" "$MODEL_FILE"
echo "done: $MODEL_FILE"
