@echo off

REM This file should be used to call the nav python file

SET PYTHONFILE=linecount.py
SET PYTHONPATH=%~dp0\..\scripts\linecount
SET CALLDIR=%CD%

pushd %PYTHONPATH%
%PYTHONFILE% %CALLDIR% %*
popd