#!/usr/bin/env bash
set -e

echo "=== Project root ==="
cd "$(dirname "$0")/../.."
pwd

BUILD_DIR="cmake-build-wsl"

echo "=== Checking dependencies ==="

# Python
if ! command -v python3 &> /dev/null; then
    echo "ERROR: Python3 not found"
    exit 1
fi

# Conan
if ! command -v conan &> /dev/null; then
    echo "ERROR: Conan not found (install via pipx)"
    exit 1
fi

# Compiler
if ! command -v g++ &> /dev/null; then
    echo "ERROR: g++ not found (install build-essential)"
    exit 1
fi

# Build tool (ninja or make)
if ! command -v ninja &> /dev/null && ! command -v make &> /dev/null; then
    echo "ERROR: No build tool found (install ninja-build or make)"
    exit 1
fi

echo "=== Conan profile detect ==="
conan profile detect --force

echo "=== Cleaning old build (if exists) ==="
rm -rf "$BUILD_DIR"

echo "=== Installing dependencies (Conan) ==="
conan install . \
    -of "$BUILD_DIR" \
    --build=missing \
    -s build_type=Debug

# Проверка что toolchain реально появился
if [ ! -f "$BUILD_DIR/conan_toolchain.cmake" ]; then
    echo "ERROR: conan_toolchain.cmake not generated"
    exit 1
fi

echo "=== Conan toolchain generated ==="
ls "$BUILD_DIR" | grep conan

echo "=== Setup completed successfully ==="