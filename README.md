# Learning_log
 
 Learning log - application for taking notes on topics of interest. User can create topics and take notes on them. Only a registered user can take notes.

## Project start: ##

### 1. Clone the repository: ###
    git clone https://github.com/konevyar/Learning_log.git

### 2. Go to project directory: ###
    cd Learning_log

### 3. Create and activate a virtual environment: ###
    python3 -m venv venv

###### on Windows
    source venv/Scripts/activate

###### on Mac/Linux
    source venv/bin/activate

### 4. Install dependencies from the requirements.txt file: ###
    pip install -r requirements.txt
  
### Make migration: ###
    python3 manage.py migrate

### Start project: ###
    python3 manage.py runserver
