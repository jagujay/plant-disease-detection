import os

base_dir = "../data/plant-doc-dataset/test"

for subdir in os.listdir(base_dir):
    subdir_path = os.path.join(base_dir, subdir)

    if os.path.isdir(subdir_path):
        files = sorted(os.listdir(subdir_path))

        # Step 1: temp rename
        for i, f in enumerate(files):
            os.rename(
                os.path.join(subdir_path, f),
                os.path.join(subdir_path, f"temp_{i}.jpg")
            )

        # Step 2: final rename
        temp_files = sorted(os.listdir(subdir_path))
        for i, f in enumerate(temp_files, start=1):
            os.rename(
                os.path.join(subdir_path, f),
                os.path.join(subdir_path, f"{i}.jpg")
            )