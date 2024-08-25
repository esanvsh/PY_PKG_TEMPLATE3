#!/bin/bash
. /c/Users/sanve/anaconda3/etc/profile.d/conda.sh
echo [$(date)]: "START"
echo [$(date)]: "Creating env with PYTHON3.11"
# WITHOUT CONDA
#python3.11 -m venv venv
# WITH CONDA
conda create --prefix ./env python=3.11 -y
echo [$(date)]: "activate env"
# WITHOUT CONDA
#/bin/bash -c "source ./venv/bin/activate"
# WITH CONDA
conda activate ./env
#echo [$(date)]: "Intalling dev requirements"
# WITHOUT CONDA
#python3.11 -m pip install -e .
# WITH CONDA
#pip install -r requirements_dev.txt
#pip install -r requirements.txt
echo [$(date)]: "END"
