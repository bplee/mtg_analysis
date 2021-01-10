import os
import pandas as pd
import json

class DataLoader:
    def __init__(self):
        self.card_rankings = DataLoader.load_17_lands()
        print(" Loaded 17 lands card Ranking in 'self.card_rankings'")
        self.set_data_df, self._all_set_data = DataLoader.load_set()
        print(" Loaded ZNR set in 'self.set_data_df'")


    @staticmethod
    def load_17_lands(filepath="../data/17_lands.csv"):
        """
        loads 17 lands csv file

        Parameters
        ----------
        filepath : str
            (default is "../data/17_lands.csv") expected filepath of csv file with expected format

        Returns
        -------
        pandas df
            filled with 17 lands ranking statistics
            data and column name legend found here : https://www.17lands.com/card_ratings

        """
        return pd.read_csv(filepath, index_col=0)


    @staticmethod
    def load_set(filepath="../data/ZNR.json", remove_0_info_cols=True, draftable_cards=265):
        """
        loads json set from mtgjson into a pandas df

        Parameters
        ----------
        filepath : str
            (default is "../data/ZNR.json")

        remove_0_info_cols : bool
            (default is True) boolean to remove columns that contain data orthogonal to value of a card (e.g. artist, flavortext)

        draftable_cards : int
            (default is 265) max card number of cards seen in a draft pool (not considering basic lands) default set for ZNR set

        Returns
        -------
        pandas df
            each row is a card (MDFC's have two rows, one for each side)

        """
        with open(filepath) as f:
            set_data = json.load(f)

        rtn = pd.DataFrame(set_data['data']['cards'])

        if remove_0_info_cols:
            rtn = rtn.drop(['artist',
                            'availability',
                            'borderColor',
                            'edhrecRank',
                            'flavorText',
                            'foreignData',
                            'frameVersion',
                            'hasFoil',
                            'hasNonFoil',
                            'identifiers',
                            'legalities',
                            'originalText',
                            'originalType',
                            'purchaseUrls',
                            'printings',
                            'rulings',
                            'setCode',
                            'type',
                            'uuid',
                            'variations',
                            'isReprint',
                            'otherFaceIds',
                            'isStorySpotlight',
                            'frameEffects',
                            'leadershipSkills',
                            'isFullArt',
                            'isStarter',
                            'isPromo',
                            'watermark',
                            'promoTypes'], axis=1)

        rtn.number = pd.to_numeric(rtn.number, errors='coerce', downcast='integer')
        rtn = rtn[rtn.number <= draftable_cards]
        rtn.number = rtn.number.astype(int)

        return rtn, set_data


if __name__ == "__main__()":

    data_obj = DataLoader()
