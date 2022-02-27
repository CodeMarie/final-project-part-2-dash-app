# Dash Data Dashboard for Retail Project 
## _Repository Part Two of Two_

## Installation requirements

Installations required if not already installed and at current level of Pip: 
At the time of developing pip was used rather than pip3 for the upgrade and further information about Pip use this link [here](https://pip.pypa.io/en/stable/installation/)
 
The requirements for this dash application includes jupyter notebooks which uses the extension ipynb and Pandas.
If not already globally installed the terminal use the command (if using the first cell of the data.ipynb file precede the command with an exclamation mark and a space e.g. ! pip install pandas)

```sh
pip install notebook
pip install pandas
# pip install dash-bootstrap-components
```
Setting up the environment 

A Jupyter Notebook in a file called data.ipybn was created for testing of the implemented csv files. 

To work with Python in Jupyter Notebooks, you must activate a Python or Anaconda environment in VS Code which you've installed the Jupyter package. Using the shortcut Command Palette (Ctrl+Shift+P) and from dropdown Select Interpreter. For this project select the Python environment from Select Interpreter was used.

Within the file you can select a kernel from the top right of the workbook. Selecting code or markdown for notes will produce new cells.
These cells which can be ran all at the same time or can run independently for speed in data assessments.

Installation requirements in the app.py file 

- Setting up the virtual environment 
For current version of software and bash shell use the term
py -m venv env 
command in the terminal, if python3 is used this will be python3 venv env 
This should create the env folder 
Next if using Windows use the command 
env\Scripts\activate
If using Mac or Unix this will be 
Source env/bin/activate

This allows for pip install Dash.

Using standard convention

```sh
import plotly.express as px
import pandas as pd
```

Note within the ipynb file pandas and plotly.express is imported.Click on Run All to begin executing these cells

Within app.py 
```sh
import dash
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output
from dash import dcc, html 
```

## Data Files 
Please refer to Dash-Project Part-One which informs further about the data cleansing of the original raw data. 
The files imported from this process are csv files utilised by the Dashboard Application. 

## Development Diary 

- For styling there is the option of Dash Bootstrap Components which can be installed with pip install dash-bootstrap-components to be imported

## Deployment
A runtime.txt file needs to hold the version of Python used which is needed for the Heroku server 
Gunicorn 'Green Unicorn' is a Python WSGI production grade HTTP Server for UNIX
A ProcFile is used for Heroku deployment with web: gunicorn app:server 
A requirements.txt file is created with pip freeze > requirements.txt

References 


- Jupyter Notebooks in Visual Code https://code.visualstudio.com/docs/datascience/jupyter-notebooks

- Runtimes supported by Heroku https://devcenter.heroku.com/articles/python-runtimes

- Dash core components https://dash.plotly.com/dash-core-components