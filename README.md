# tutorial_project
for details look here : [click me you,yeah you](https://github.com/avnyadav/machine_learning_project)

## Creating conda environment
* this "-p" is prefix which means create your environment in the same folder as your project existing folder 
* the "-y" means YES it will ask once you trying to install conda for confirmation 
we are bruteforcing the answer as yes :)

* "pip freeze > requirements.txt" - it's for installing the required libraries but if we are using the virtual environment then use this kind of syntax 

**Code**

`conda create -p myvenv python==3.9.15 -y`

`conda activate myvenv/`

`pip freeze > requirements.txt`
