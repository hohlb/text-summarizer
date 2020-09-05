# Text Summarizer REST API
Creates text summaries, even for long texts. 

Two REST APIs are available:
* `POST /summaries/` takes a (long) text, create a summary using a background task, and immediately returns a `document_id` to retrieve the summary later using:
* `GET /summaries/{document_id}` returns the summary for the given `document_id`

Built using [FastAPI](https://fastapi.tiangolo.com/) and [BERT Extractive Summarizer](https://github.com/dmmiller612/bert-extractive-summarizer).

## Installation
Python 3.6 or higher is supported.

### Install packages using pip:
```bash
# change the working directory to our codebase
cd text-summarizer

# create a virtual Python environment in current directory (optional, but recommended)
python3 -m venv .venv

# activate the virtual Python environment we just created
source .venv/bin/activate
# if you are not using the bash shell, you can take the right command from the table
# "Command to activate virtual environment" at https://docs.python.org/3/library/venv.html

# update the virtual environment's package manager
python3 -m pip install --upgrade pip

# install the necessary Python packages
#
# first, we will install pytorch:
# the following pytorch installation command worked for my platform, but it is highly recommended to
# go to https://pytorch.org/ (you need to scroll a bit on that web page) to generate the correct "pip install" command for your platform
python3 -m pip install torch==1.6.0+cpu torchvision==0.7.0+cpu -f https://download.pytorch.org/whl/torch_stable.html
# now, we can install the remaining packages:
python3 -m pip install -r requirements.txt
```

### Install packages using conda (alternatively):
```bash
# change the working directory to our codebase
cd text-summarizer

# update the package (and environment) manager
conda update conda

# create a new conda environment in the current directory
conda create --prefix ./.venv
conda activate .venv/

# search for packages on the better maintained "conda-forge" channel before using the default channel
conda config --env --add channels conda-forge

# use Python 3.8
conda install python=3.8

# install the necessary Python packages
#
# first, we will install pytorch:
# the following pytorch installation command worked for my platform, but it is highly recommended to
# go to https://pytorch.org/ (you need to scroll a bit on that web page) to generate the correct "pip install" command for your platform
# (I opted to use the pip packages of pytorch instead of the conda packages (see the following line) because it worked better for my setup)
python -m pip install torch==1.6.0+cpu torchvision==0.7.0+cpu -f https://download.pytorch.org/whl/torch_stable.html
# now, we can install the remaining packages:
python -m pip install -r requirements.txt
```

### Check if the packages were installated correctly
```bash
python -c "import torch; import transformers; import summarizer; import fastapi; import uvicorn; import multipart; import requests"
```

If you see no (error) messages, the installation went well.

### Rebuild the database (optional)
You can delete the existing SQLite database `summaries.db` at any time and rebuild it using:
```bash
python ./src/create_database.py
```

## Serve the REST API
Run
```bash
uvicorn main:app
```
Now, you can access the REST API. At http://127.0.0.1:8000/docs is the detailed documentation on how to use it, but you can also use the test scripts:

## Test the REST API
Two scripts are provided which show how to use the REST API programmatically:

### Request a summary for a (long) text
```bash
python ./tests/request_summary.py
```

This returns a `document_id` and starts the summarization of the (long) text (defined within the script) in a background task.

### Get the summary
```bash
python ./tests/get_summary.py 1
```

Replace `1` in this example with the actual `document_id` you got in the previous step.

```bash
# output if the summary is still being created:
python ./tests/get_summary.py 1
{'document_id': 1, 'summary': None}

# output once the summarization is done:
python ./tests/get_summary.py 1
{'document_id': 1,
 'summary': 'Tree squirrel\n'
            '\n'
            'Tree squirrels are the members of the squirrel family ...'}

```
