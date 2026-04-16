import os
import shutil
from pathlib import Path


def normalize_class_name(folder_name):
    """
    Normalizes folder names to lowercase to prevent case-sensitivity duplicates.
    """
    name = folder_name.lower().strip()

    # 1. Drop the "phantom" PlantDoc class that has no test data
    if name == "tomato two spotted spider mites leaf":
        return None

        # 2. Safety net for known internal dataset syntax quirks
    # (Just in case any were missed during the manual renaming)
    # mapping = {
    #     "apple rust leaf": "apple leaf rust",
    #     "tomato early blight leaf": "tomato leaf early blight",
    #     # Notice we do NOT map the potato blights here!
    # }

    return name


def merge_true_dataset(source_dirs, target_dir):
    """
    Merges all classes from both datasets into a single 29-class target directory.
    """
    target_path = Path(target_dir)
    splits = ['train', 'test']

    for split in splits:
        for source in source_dirs:
            source_split_path = Path(source) / split
            if not source_split_path.exists():
                print(f"Warning: {source_split_path} not found. Skipping.")
                continue

            for class_dir in source_split_path.iterdir():
                if class_dir.is_dir():
                    # Normalize the folder name
                    standardized_name = normalize_class_name(class_dir.name)

                    # If it's the phantom class, standardized_name is None, so we skip it
                    if not standardized_name:
                        continue

                    target_class_path = target_path / split / standardized_name
                    target_class_path.mkdir(parents=True, exist_ok=True)

                    # Copy all images, prefixing with the dataset name
                    for img_file in class_dir.iterdir():
                        if img_file.is_file():
                            new_file_name = f"{Path(source).name}_{img_file.name}"
                            shutil.copy2(img_file, target_class_path / new_file_name)

    print(f"\nTrue merge complete! 29-Class data saved to {target_dir}")


if __name__ == "__main__":
    sources = ["../data/plant-doc-dataset", "../data/web-sourced-dataset"]
    target = "../data/combined-dataset-true"

    merge_true_dataset(sources, target)