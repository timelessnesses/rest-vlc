@echo off
./build.cmd
python -m twine
python -m twine upload dist/* -u %TWINE_USERNAME% -p %TWINE_PASSWORD%