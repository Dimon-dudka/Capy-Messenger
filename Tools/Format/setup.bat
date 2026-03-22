@echo off
pushd %~dp0..\..

py -m Tools.Format.setup %*
pause
popd