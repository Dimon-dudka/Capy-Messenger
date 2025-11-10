@echo off
cd /d "%~dp0"
setlocal enabledelayedexpansion

echo === Checking Python version ===
python --version >nul 2>&1
if errorlevel 1 (
    py --version >nul 2>&1
    if errorlevel 1 (
        echo === ERROR: Python is not installed or not in PATH ===
        exit /b 1
    )
    set "py_cmd=py"
) else (
    set "py_cmd=python"
)

for /f "tokens=2" %%v in ('!py_cmd! --version 2^>^&1') do (
    set "python_version=%%v"
    goto check_version
)

:check_version
for /f "tokens=1,2 delims=." %%a in ("!python_version!") do (
    set "major=%%a"
    set "minor=%%b"
)

for /f "delims=" %%i in ("!major!") do set "major=%%i"
set "major=!major:~-1!"

if !major! lss 3 (
    echo === ERROR: Python version !python_version! is less than 3.0 ===
    exit /b 1
)
echo === Found Python !python_version! ===

echo === Checking Conan ===
conan --version >nul 2>&1
if errorlevel 1 (
    echo === ERROR: Conan is not installed or not in PATH ===
    exit /b 1
)

for /f "tokens=*" %%c in ('conan --version 2^>^&1') do set conan_version=%%c
echo === Found !conan_version! ===

echo === Installing dependencies ===
conan install . --build=missing
conan install . -s build_type=Debug --build=missing

echo === Configuring CMake ===
cmake -S . -B build -DCMAKE_TOOLCHAIN_FILE=Third-Party/conan_toolchain.cmake -DCMAKE_C_COMPILER=cl -DCMAKE_CXX_COMPILER=cl

echo === Building project ===
cmake --build build

echo === Successfully installed ===
pause
