import torch
from torch.utils.data import Dataset

class ChunkingDataset(Dataset):
    def __init__(self, datasetLoader):
        self.loader = datasetLoader
        self.sequences = self.loader.get_all()

    def __len__(self):
        return len(self.sequences)

    def __getitem__(self, idx):
        tuple = self.sequences[idx]
        x = torch.tensor(tuple[0], dtype=torch.float)
        y = torch.tensor(tuple[1], dtype=torch.float)
        return x, y