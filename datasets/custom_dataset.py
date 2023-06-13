import os

from torch.utils.data import Dataset
from torchvision.io import read_image


class CustomDataset(Dataset):
    def __init__(self, img_dir, file_names, labels, transform=None, target_transform=None):
        self.img_dir = img_dir
        self.img_labels = labels
        self.file_names = file_names
        self.transform = transform
        self.target_transform = target_transform

    def __len__(self):
        return len(self.img_labels)

    def __getitem__(self, idx):
        img_path = os.path.join(self.img_dir, self.file_names.iloc[idx])
        image = read_image(img_path)
        label = self.img_labels.iloc[idx]
        if self.transform:
            image = self.transform(image)
        if self.target_transform:
            label = self.target_transform(label)
        return image, label
