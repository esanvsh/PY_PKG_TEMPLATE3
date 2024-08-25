echo [$(date)]: "START"
echo [$(date)]: "CREATING ENV with PYTHON3.11"
# WITHOUT CONDA
python3.11 -m venv venv
# WITH CONDA
#conda create --prefix ./env python=3.11 -y
echo [$(date)]: "ACTIVATE ENV"
# WITHOUT CONDA
/bin/bash -c "source ./venv/bin/activate"
# WITH CONDA
#source activate ./env
echo [$(date)]: "INSTALLING DEV requirements"
# WITHOUT CONDA
#python3.11 -m pip install -e .
# WITH CONDA
pip install -r requirements_dev.txt
#pip install -r requirements.txt
echo [$(date)]: "END"
