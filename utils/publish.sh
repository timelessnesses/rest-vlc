sudo bash build.sh
python3 -m pip install twine
python3 -m twine upload dist/* -u $TWINE_USERNAME -p $TWINE_PASSWORD