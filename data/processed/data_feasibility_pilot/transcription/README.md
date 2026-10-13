# Verified passage layer

`verified_passages.jsonl` separates three layers:

1. `raw_ocr_excerpt`: uncorrected text copied from the downloaded OCR/text layer;
2. `verified_transcription`: a short passage visually compared once against the page image;
3. `normalized_text`: an interpretive research paraphrase, never a replacement for the source text.

The verification is a single research-agent pass, not double-keyed diplomatic transcription or expert adjudication. Punctuation, ligatures and table values were checked for the selected passage only; the rest of each page retains provider OCR status. The `caution` field must travel with any benchmark item derived from the passage.
