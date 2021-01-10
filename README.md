# mtg_analysis
Repo for analyzing mtg cards and drafts

## Data
Contains the following: 
- `ZNR.json` from [MTGjson](https://mtgjson.com/downloads/all-sets/). All initial analyses performed on the ZNR set
- `17_lands.xlsx` copy pasta from (17 land's website)[https://www.17lands.com/card_ratings] was formatted into following `csv` file
- `17_lands.csv` csv of refined table

## Code
Contains data loader object to read 17 lands ranking data and all relevent ZNR card data into pandas df's. 

Not all card names in the `17_lands.csv` and `ZNR.json` files are the same
