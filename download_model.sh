#!/usr/bin/env bash
# Download the Baarali Edge model weights.
#
# Contract imposed by the ADTC template:
#   - idempotent (safe to run twice),
#   - no credentials (public URL only),
#   - output path identical to `_runtime.model_path` in metadata.json.
#
# The download lands in a `.partial` file and is renamed only on success: an
# interrupted run must not leave a truncated .gguf that looks complete to the
# profiler.

set -euo pipefail

HERE="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
MODEL_DIR="$HERE/model"

# ── À renseigner à l'étape 4, une fois les poids publiés sur Hugging Face ──────
MODEL_FILE="$MODEL_DIR/TODO-MODEL-NAME-Q4_K_M.gguf"
MODEL_URL="TODO-PUBLIC-HUGGINGFACE-URL"
# ──────────────────────────────────────────────────────────────────────────────

if [[ "$MODEL_URL" == TODO-* ]]; then
  echo "error: model URL not set yet — see PLAN.md, étape 4" >&2
  exit 1
fi

mkdir -p "$MODEL_DIR"

if [[ -f "$MODEL_FILE" ]]; then
  echo "model already present at $MODEL_FILE — skipping download"
  exit 0
fi

echo "downloading $MODEL_URL → $MODEL_FILE…"

if command -v curl > /dev/null 2>&1; then
  curl -L --fail --progress-bar -o "$MODEL_FILE.partial" "$MODEL_URL"
elif command -v wget > /dev/null 2>&1; then
  wget --show-progress -O "$MODEL_FILE.partial" "$MODEL_URL"
else
  echo "error: neither curl nor wget found" >&2
  exit 1
fi

mv "$MODEL_FILE.partial" "$MODEL_FILE"
echo "done: $MODEL_FILE"
