# Text Summarizer REST API
Creates text summaries, even for long texts. 

Two REST APIs are available:
* `POST /summaries/` takes a (long) text, create a summary using a background task, and immediately returns a `document_id` to retrieve the summary later using:
* `GET /summaries/{document_id}` returns the summary for the given `document_id`

Having two separate APIs is especially useful when the summarization runs a long time, e.g. for long texts or when no GPUs are available.

Built using [FastAPI](https://fastapi.tiangolo.com/) and [BERT Extractive Summarizer](https://github.com/dmmiller612/bert-extractive-summarizer).

## Setup

### Using Docker:
```bash
# serve the REST APIs
docker run --rm -p 8000:8000 hohlb/text-summarizer

# (optional) use the Python environment, e.g. for executing scripts
# (start this command in another shell and leave the REST APIs running via the above command)
docker run --rm -it hohlb/text-summarizer bash
```

The Docker image gets pulled from [Docker Hub](https://hub.docker.com/r/hohlb/text-summarizer) automatically. (The image gets put on Docker Hub via [my GitHub Action workflow](https://github.com/hohlb/text-summarizer/blob/master/.github/workflows/dockerhub.yml).)

### Setup using pip or conda (alternatively):
<details>
  <summary>Click to expand</summary>

  #### Create a virtual environment for pip:
  Python 3.6 or higher is supported.

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
  ```

  #### Create a virtual environment using conda (alternatively):
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
  ```

  #### Install the necessary Python packages:
  ```bash
  python -m pip install -r requirements.txt
  ```
  This also works if you are using a `conda` environment.
    
  Check if the packages were installated correctly
  ```bash
  python -c "import torch; import transformers; import summarizer; import fastapi; import uvicorn; import multipart; import requests"
  ```
  If you see no (error) messages, the installation went well.

  #### Build the database
  ```bash
  python -m scripts.create_database
  ```
  This SQLite database holds the summaries and their `document_id`. You can delete the database at any time and rebuild it using this script.

  #### Serve the REST APIs
  ```bash
  uvicorn main:app
  ```
</details>

## Use the REST APIs
Now, you can access the REST APIs. At http://localhost:8000/docs and http://localhost:8000/redoc are the detailed documentations on how to use the REST APIs, but you can also use these scripts:

### Use the REST APIs programmatically
Two scripts are provided which show how to use the REST APIs programmatically:

#### Request a summary for a (long) text
```bash
python ./scripts/test/request_summary.py
```

This returns a `document_id` and starts the summarization of the (long) text (defined within the script) in a background task.

#### Get the summary
```bash
python ./scripts/test/get_summary.py 1
```

Replace `1` in this example with the actual `document_id` you got in the previous step.

```bash
# output if the summary is still being created:
python ./scripts/test/get_summary.py 1
{'document_id': 1, 'summary': None}

# output once the summarization is done:
python ./scripts/test/get_summary.py 1
{'document_id': 1,
 'summary': 'Tree squirrel\n'
            '\n'
            'Tree squirrels are the members of the squirrel family ...'}

```
