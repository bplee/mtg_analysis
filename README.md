# mtg_analysis
Repo for analyzing mtg cards and drafts

## Data
All the following contents of data are no longer currently pertinent to the project. Instead data stores public datasets from 17lands (through `/code/data_walkthrough.ipynb`). This python notebook downloads compressed data to /data/sets/stx/

Contains the following: 
- `ZNR.json` from [MTGjson](https://mtgjson.com/downloads/all-sets/). All initial analyses performed on the ZNR set
- `17_lands.xlsx` copy pasta from (17 land's website)[https://www.17lands.com/card_ratings] was formatted into following `csv` file
- `17_lands.csv` csv of refined table

## Code
The only relevent file in `/code/` right now is `data_walkthrough.ipynb`, as it downloads data and does some introduction to some of the data.

Contains data loader object to read 17 lands ranking data and all relevent ZNR card data into pandas df's. 

