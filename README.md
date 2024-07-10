Instructions for setup:

python3 -m venv env
source env/bin/activate
pip install -r requirements.txt

python3 data_management/pre_processing.py

mkdir objdir
g++ src/simulator.cpp -o objdir/simulator.out

./objdir/simulator.out
