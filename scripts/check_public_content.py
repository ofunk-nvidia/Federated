#!/usr/bin/env python3
"""Conservative publication gate for this documentation-only repository."""

from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SELF = Path(__file__).resolve()
MAX_TEXT_BYTES = 2 * 1024 * 1024
MAX_IMAGE_BYTES = 5 * 1024 * 1024
IMAGE_SUFFIXES = {".png", ".jpg", ".jpeg", ".gif", ".webp"}
PROHIBITED_SUFFIXES = {
    ".7z", ".bin", ".ckpt", ".db", ".dmp", ".dump", ".env", ".fmb",
    ".gz", ".jks", ".keystore", ".onnx", ".p12", ".parquet", ".pem",
    ".pfx", ".pt", ".pth", ".rdf", ".safetensors", ".sqlite", ".tar", ".zip",
}
PROHIBITED_PARTS = {
    "adapters", "checkpoints", "client-data", "customer-data", "customer-projects",
    "datasets", "model-weights", "raw-data",
}
PATTERNS = {
    "private key": re.compile(r"-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----"),
    "GitHub token": re.compile(r"\b(?:ghp|github_pat)_[A-Za-z0-9_]{20,}\b"),
    "AWS access key": re.compile(r"\b(?:AKIA|ASIA)[A-Z0-9]{16}\b"),
    "credential assignment": re.compile(
        r"(?i)\b(?:password|passwd|pwd|secret|api[_-]?key|access[_-]?token)\s*[:=]\s*['\"]?[^\s'\"<{]{8,}"
    ),
    "restricted marking": re.compile(
        r"\b(?:NVIDIA CONFIDENTIAL|CLIENT CONFIDENTIAL|INTERNAL USE ONLY|DO NOT DISTRIBUTE)\b"
    ),
}


def main() -> int:
    failures: list[str] = []
    for path in sorted(p for p in ROOT.rglob("*") if p.is_file()):
        if ".git" in path.parts:
            continue
        rel = path.relative_to(ROOT)
        lowered_parts = {part.lower() for part in rel.parts}
        suffix = path.suffix.lower()
        size = path.stat().st_size

        if lowered_parts & PROHIBITED_PARTS:
            failures.append(f"{rel}: prohibited path")
            continue
        if suffix in PROHIBITED_SUFFIXES:
            failures.append(f"{rel}: prohibited file type")
            continue
        if suffix in IMAGE_SUFFIXES:
            if size > MAX_IMAGE_BYTES:
                failures.append(f"{rel}: image exceeds {MAX_IMAGE_BYTES} bytes")
            continue
        if size > MAX_TEXT_BYTES:
            failures.append(f"{rel}: file exceeds {MAX_TEXT_BYTES} bytes")
            continue
        try:
            content = path.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            failures.append(f"{rel}: unapproved binary file")
            continue
        if path.resolve() == SELF:
            continue
        for label, pattern in PATTERNS.items():
            if pattern.search(content):
                failures.append(f"{rel}: possible {label}")

    if failures:
        print("Publication gate failed:")
        for failure in failures:
            print(f"- {failure}")
        print("Human provenance and confidentiality review is required even after fixing these findings.")
        return 1

    print("Automated publication gate passed.")
    print("This does not replace human provenance, licence, confidentiality, and privacy review.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
