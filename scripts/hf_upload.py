from huggingface_hub import HfApi

api = HfApi()
USERNAME = "your-username"

print("Uploading 16-Class Dataset in safe batches...")
api.upload_large_folder(
    folder_path="../data/combined-dataset-16-class",
    repo_id=f"{USERNAME}/plant-disease-16-class",
    repo_type="dataset",
)

print("Uploading True Dataset in safe batches...")
api.upload_large_folder(
    folder_path="../data/combined-dataset-true",
    repo_id=f"{USERNAME}/plant-disease-true",
    repo_type="dataset",
)

print("Uploading All Model Weights...")
api.upload_large_folder(
    folder_path="../models",
    repo_id=f"{USERNAME}/plant-disease-architectures",
    repo_type="model",
)