@echo Installing Plastimatch
setlocal 

mkdir backend\tools

set REL_PATH=backend\tools
set ABS_PATH=

pushd %REL_PATH%

set ABS_PATH=%CD%

popd

@echo %ABS_PATH%
msiexec /i scripts\Plastimatch-1.9.0-win64.msi TARGETDIR="%ABS_PATH%" INSTALL_ROOT="%ABS_PATH%" /qb