# python template (UPDATE THIS WITH ORIGINAL DOCUMENTATION RELATED INFORMATION LATER)
## Instruction on how to use this template?

Documentation: `https://esanvsh.github.io/<repo-name>/<add project board link if any>`


######################################################################
## LOCAL SETUP
######################################################################

## STEPS - 

### STEP 01: GIT CLONE TEMPLATE & FIRST COMMIT 
# Create PROJECT FOLDER
git init
# From terminal go to path
code .
# Clone REPO
git clone <URL>
git commit -m "Commit after Clone"
# GIT REMOTE ADD
- We have LOCAL REPO
- We have REMOTE REPO at GITHUB 
git remote add origin https://<TOKEN_VALUE>@github.com/esanvsh/NewRepo.git
# GIT PUSH to REMOTE REPO
git push -u origin main
# Incase creating new File File1.txt
git add <file1.txt> or git add .
git commit -m "File1.txt Commit"

### STEP 02: ADD a `LICENSE` file

- Go to your github repository and click on `Add file` and then select `Create new file`.
- Now start typing the name of the file as `LICENSE` and then you'll see the option of selecting the desired template. 

NOTE: You can choose MIT License if you are not sure.

> This completes the basic skeleton of the project!!

### STEP 03: COMMIT the CHANGES
- We can commit the changes from VSCODE itself
- Use SOURCE CONTROL
### STEP 04: IMPORTANT: CREATE `.env` file in root dir

```ini
# update the following values as per your project
PROJECT_NAME=<PROJECT_NAME>
REPO_NAME=<REPO_NAME>
GITHUB_USER_NAME=<GITHUB_USER_NAME>
AUTHOR_NAME=<AUTHOR_NAME>
PACKAGE_NAME=<PACKAGE_NAME>
AUTHOR_EMAIL=<AUTHOR_EMAIL>
LICENCSE_NAME="MIT" # update as per your need, Here it is assumed that you choose MIT LICENSE
PYTHON_VERSION=3.11 # update as per your need, Here it is assumed that you choose version 3.8
YEAR=2024 # update as per your need
```

> **WARNING: if this step is skipped then exception will be raised**

### STEP 05: LOCAL SETUP - CREATE ENVIRONMENT without CONDA or with CONDA
> . /c/Users/sanve/anaconda3/etc/profile.d/conda.sh
- Run below command
> ./local_setup.sh
### LOCAL SETUP SCRIPT content
> #!/bin/bash
> . /c/Users/sanve/anaconda3/etc/profile.d/conda.sh
#### WITHOUT CONDA
> python3.11 -m venv venv
> /bin/bash -c "source ./venv/bin/activate"
> python3.11 -m pip install -e .
#### WITH CONDA
> conda create --prefix ./env python=3.11 -y
> conda activate ./env
> pip install -r requirements_dev.txt
> pip install -r requirements.txt


### STEP 06: UPDATE FILES
- Check if conda environment is created
pip install toml
pip install python-dotenv
python update_toml_py.py
> Here understanding of TOML file is critical
- Consider pyproject_temp.toml

### STEP 07: RUN template.py file
pip install python-dotenv
python template.py

### STEP 08: CREATE .py FILES in src/
- As per project requirement create .py files

### STEP 09: CREATE TEST FILES in tests/
 - tests/unit/test_unit.py
 - tests/integration/test_int.py

### STEP 10: RUN requirement_dev.txt
- In Local Environment
pip install -r requirements_dev.txt

### STEP 11: Uncomment github action workflows present in `.github/workflows` directory

### STEP 12: Create new release of the project
- After developement you can create release of your project to make this project available at `pypi.org`.
- For this you will need PYPI token, which can be created from your `pypi` profile section.
- And the above token should be added to the secret variables of the repository.


######################################################################
# DOCKERIZE in DEV ENVIRONMENT
######################################################################

### STEP 1
- Add files to .dockerignore
- Add files to .gitignore

### STEP 2: BUILD DOCKER IMAGE

docker build -t snakeapp .
docker run -d -it -p 8501:8501 -p 8002:8002 --name snakecontainer snakeapp
docker exec -it snakecontainer bash
> snakey
- On PORT 8002 FASTAPI will work
- ON PORT 8501 STREAMLIT will work
- PATH src/snakey/ --> RUN STREAMLIT on 8501
> streamlit run strmlt_ui.py


######################################################################
# DOCKERIZE in PROD ENVIRONMENT
######################################################################

### REMOVE UNECESSARY FILES
# Add files to .dockerignore
# Add files to .gitignore

### UPDATE requirements.txt
# UPDATE DockerFile with new requirements.txt

### CREATE PACKAGE
#

######################################################################
# ISSUES
######################################################################
# ^M ISSUE
 - vim filename
 - :e ++ff=unix
 - Now we will see all ^M
 - %s/^M//g
