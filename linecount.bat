@echo off

SET PYTHONFILE=linecount.py
SET PYTHONPATH=%~dp0\..\scripts\linecount
SET CALLDIR=%CD%

pushd %PYTHONPATH%
%PYTHONFILE% %CALLDIR% %*
popd