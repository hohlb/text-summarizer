Start
    start "Anaconda Prompt (miniconda3)"
    
    cd C:\projects\text-summarizer && conda activate .venv/
    
    uvicorn main:app --reload
    
    #python run_summarization.py --documents_dir ./data --summaries_output_dir ./summaries --no_cuda false --batch_size 4 --min_length 50 --max_length 200 --beam_size 5 --alpha 0.95 --block_trigram true
    
    
Cache
    C:\Users\Beni/.cache\torch\transformers\
    
    first run of "python summarize.py" downloads 1.43 GB

    
Installation
    start "Anaconda Prompt (miniconda3)"

    conda update conda


    ## create a new environment inside a project folder

    cd C:\projects\text-summarizer && conda create --prefix ./.venv -y && conda activate .venv/

    # shorten the displayed name inside the CLI
    conda config --env --set env_prompt '({name})'

    # search for packages on channel "conda-forge" before using the default channel
    conda config --env --add channels conda-forge

    # install packages
    #
    # we install ipykernel to use this environment from JupyterLab
    #
    # we install scrapy via pip to avoid DLL errors for the etree dependency (no need for this under linux)
    
    
    conda install python=3.8
    
    # go to https://pytorch.org/ (scroll a bit) to generate the correct "pip install" command for your platform
    python -m pip install torch==1.6.0+cpu torchvision==0.7.0+cpu -f https://download.pytorch.org/whl/torch_stable.html
    python -m pip install -r requirements.txt


    
    # test the installation
    #python -c "import torch; import transformers; import fastapi"
    python -c "import torch; import transformers; import summarizer; import fastapi; import uvicorn; import multipart; import requests"

    # make kernel (environment) available to JupyterLab (restart JupyterLab afterwards)
    #jupyter kernelspec uninstall text-summarizer
    python -m ipykernel install --user --name=text-summarizer
    
    
    python ./src/create_database.py
    
    uvicorn main:app
    
    python ./tests/request_summary.py
    python ./tests/get_summary.py 1
