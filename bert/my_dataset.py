import pandas as pd
import torch
from torch.utils.data import Dataset


class My_Dataset(Dataset):
    # CITATION: https://androidkt.com/load-pandas-dataframe-using-dataset-and-dataloader-in-pytorch/
    def __init__(self, df: pd.DataFrame):
        self.df = df

    def __len__(self):
        return len(self.df)

    def __getitem__(self, idx: int):
        item = {
            "labels": torch.tensor(self.df.iloc[idx]['labels'], dtype=torch.int64),
            "input_ids": torch.tensor(self.df.iloc[idx]['input_ids']),
            "token_type_ids": torch.tensor(self.df.iloc[idx]['token_type_ids']),
            "attention_mask": torch.tensor(self.df.iloc[idx]['attention_mask']),
        }
        return item


class My_Dataset_Test(Dataset):
    # CITATION: https://androidkt.com/load-pandas-dataframe-using-dataset-and-dataloader-in-pytorch/
    def __init__(self, df: pd.DataFrame):
        self.df = df

    def __len__(self):
        return len(self.df)

    def __getitem__(self, idx: int):
        item = {
            "company": self.df.iloc[idx]["company"],
            "date": self.df.iloc[idx]["date"],
            "labels": torch.tensor(1, dtype=torch.int64),
            "input_ids": torch.tensor(self.df.iloc[idx]['input_ids']),
            "token_type_ids": torch.tensor(self.df.iloc[idx]['token_type_ids']),
            "attention_mask": torch.tensor(self.df.iloc[idx]['attention_mask']),
        }
        return item
