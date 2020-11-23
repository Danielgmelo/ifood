#### How to run

To reproduce this analysis, use the Conda Terminal to create an environment.

- First, download conda or miniconda: 

Conda download page link: https://docs.conda.io/en/latest/miniconda.html

- On terminal, navigate to `my_project` folder and type:

```
conda env create -f environment.yml
```

- After creating the environment, it is necessary to activate it:

```
conda activate ifood-test
```

- Then, install this new environment in the jupyter notebook (kernel)

```
python -m ipykernel install --user --name=ifood-test
```

- Open the notebook and select the ifood-test kernel on the up-right screen.


#### Folder structure
```

|------ ifood
|       |--- my_project                                     
|            |--- data                                      contains data inputs and outputs
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
|            |--- src                                       contains the Python packages created specially for this analysis
|                 |--- data_cleaning.py
|                 |--- paths.py
|                 |--- data_visualization.py
|                 |--- eda.py
|            |--- environment.yml                           contains the Python libraries used in this analysis environment
|            |--- setup.py
|            |--- README.md

```
