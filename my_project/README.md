


#### How to run

For reproduce this analysis, use the conda to create a environment.

- First, download the conda or miniconda: 

link conda: https://docs.conda.io/en/latest/miniconda.html

- So, on terminal line, navigate to the my_project folder and type:

```
conda env create -f environment.yml
```

- After the creating the environment, is necessary to activate it:

```
conda activate ifood-test
```

- After, put this new environment in the jupyter notebook (kernel)

```
python -m ipykernel install --user --name=ifood-test
```

- Open the notebook and select the ifood-test kernel on the up-right screen.


#### Folder structure
```

|------ ifood
|       |--- my_project                                     
|            |--- data                                      contains inputs and outputs data
|                 |--- ml_project1_data.csv
|                 |--- ml_project1_data_cleaned.csv
|                 |--- ml_project1_data_pre_processed.csv
|                 |--- customers_to_send_the_campaign.xlsx
|            |--- images
|            |--- notebooks                                 contains notebooks used in this analysis
|                 |--- data_cleaning
|                 |--- data_processing
|                 |--- eda                                  contains the exploratory data analysis about the marketing enfasis
|                      |--- 1_customers
|                      |--- 2_pilot_campaign
|                 |--- segmentation
|                 |--- predictive_model
|            |--- src                                       contains the Python packages created specially this analysis
|                 |--- data_clean.py
|                 |--- paths.py
|                 |--- data_visualization.py
|                 |--- eda.py
|            |--- environment.yml                           contains the Python libraries used in this analysis environment
|            |--- setup.py
|            |--- README.md

```

