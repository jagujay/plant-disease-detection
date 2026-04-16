import os
import shutil
from pathlib import Path


def get_target_classes(web_dataset_path):
    train_path = Path(web_dataset_path) / 'train'
    return {d.name.lower(): d.name for d in train_path.iterdir() if d.is_dir()}


def merge_16_class_dataset(plantdoc_dir, web_dir, target_dir):
    plantdoc_path = Path(plantdoc_dir)
    web_path = Path(web_dir)
    target_path = Path(target_dir)

    allowed_classes = get_target_classes(web_dir)
    print(f"Targeting {len(allowed_classes)} classes based on web-sourced data...")

    splits = ['train', 'test']

    for split in splits:
        # --- Process Web Dataset ---
        web_split_path = web_path / split
        if web_split_path.exists():
            for class_dir in web_split_path.iterdir():
                if class_dir.is_dir():
                    dest_class_dir = target_path / split / class_dir.name
                    dest_class_dir.mkdir(parents=True, exist_ok=True)
                    for img in class_dir.iterdir():
                        if img.is_file():
                            # Include the original class name in the prefix to guarantee uniqueness
                            unique_name = f"web_{class_dir.name}_{img.name}"
                            shutil.copy2(img, dest_class_dir / unique_name)

        # --- Process PlantDoc Dataset ---
        plantdoc_split_path = plantdoc_path / split
        if plantdoc_split_path.exists():
            for class_dir in plantdoc_split_path.iterdir():
                if class_dir.is_dir():
                    class_name_lower = class_dir.name.lower()

                    # Robust substring matching for ANY potato blight
                    if "potato" in class_name_lower and "blight" in class_name_lower:
                        search_name = "potato leaf blight"
                    else:
                        search_name = class_name_lower

                    # Filter: Only copy if the name exists in our allowed 16 classes
                    if search_name in allowed_classes:
                        final_dest_name = allowed_classes[search_name]
                        dest_class_dir = target_path / split / final_dest_name
                        dest_class_dir.mkdir(parents=True, exist_ok=True)

                        for img in class_dir.iterdir():
                            if img.is_file():
                                # Include the original PlantDoc class name to prevent early/late overwrites!
                                unique_name = f"plantdoc_{class_dir.name}_{img.name}"
                                shutil.copy2(img, dest_class_dir / unique_name)
                    else:
                        pass

    print(f"\n16-class merge complete! Data saved to {target_dir}")


if __name__ == "__main__":
    sources_plantdoc = "../data/plant-doc-dataset"
    sources_web = "../data/web-sourced-dataset"
    target_directory = "../data/combined-dataset-16class-change"

    merge_16_class_dataset(sources_plantdoc, sources_web, target_directory)