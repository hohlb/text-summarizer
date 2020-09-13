# Text Summarizer REST API
Creates text summaries, even for long texts. 

Two REST APIs are available:
* `POST /summaries/` takes a (long) text, create a summary using a background task, and immediately returns a `document_id` to retrieve the summary later using:
* `GET /summaries/{document_id}` returns the summary for the given `document_id`

Having two separate APIs is especially useful when the summarization runs a long time, e.g. for long texts or when no GPUs are available.

Built using [FastAPI](https://fastapi.tiangolo.com/) and [BERT Extractive Summarizer](https://github.com/dmmiller612/bert-extractive-summarizer).

## Installation

### Using Docker:
```bash
# run the REST API
#
# pulls the docker image from Docker Hub
# -p: binds our docker container's port of the REST API to the same port (8000) on the host machine
# --rm: automatically clean up the container and remove the file system when the container exits
docker run --rm -p 8000:8000 hohlb/text-summarizer

# (optional) use the Python environment, e.g. for executing scripts
# (recommendation: start this command in another shell and leave the REST API running via the above command)
#
# --it: opens an interactive terminal
docker run --rm -it hohlb/text-summarizer bash
```

### Install Python packages using pip or conda (alternatively):
<details>
  <summary>Click to expand</summary>

  #### Install packages using pip:
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

  # install the necessary Python packages
  #
  # first, we will install pytorch:
  # the following pytorch installation command worked for my platform, but it is highly recommended to
  # go to https://pytorch.org/ (you need to scroll a bit on that web page) to generate the correct "pip install" command for your platform
  python3 -m pip install torch==1.6.0+cpu torchvision==0.7.0+cpu -f https://download.pytorch.org/whl/torch_stable.html
  # now, we can install the remaining packages:
  python3 -m pip install -r requirements.txt
  ```

  #### Install packages using conda (alternatively):
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
  # (I opted to use the pip packages instead of the conda packages (see the following lines) because it worked better for me)
  python -m pip install torch==1.6.0+cpu torchvision==0.7.0+cpu -f https://download.pytorch.org/whl/torch_stable.html
  # now, we can install the remaining packages:
  python -m pip install -r requirements.txt
  ```

  #### Check if the packages were installated correctly
  ```bash
  python -c "import torch; import transformers; import summarizer; import fastapi; import uvicorn; import multipart; import requests"
  ```

  If you see no (error) messages, the installation went well.

  #### Build the database
  ```bash
  python ./scripts/create_database.py
  ```
  This SQLite database holds the summaries and their `document_id`. You can delete the database at any time and rebuild it using this script.
</details>

## Serve the REST API
If you used `pip` or `conda`, run
```bash
uvicorn main:app
```
(this will be done automatically in the Docker image).

Now, you can access the REST API. At http://localhost:8000/docs is the detailed documentation on how to use it, but you can also use these scripts:

## Use the REST API
Two scripts are provided which show how to use the REST API programmatically:

### Request a summary for a (long) text
```bash
python ./scripts/test/request_summary.py
```

This returns a `document_id` and starts the summarization of the (long) text (defined within the script) in a background task.

### Get the summary
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
