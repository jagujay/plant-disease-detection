import os

base_dir = "../data/combined-dataset-true/train"

image_exts = ('.jpg', '.jpeg', '.png', '.bmp', '.gif')

total_subdirs = 0
report_lines = []

for subdir in sorted(os.listdir(base_dir)):
    subdir_path = os.path.join(base_dir, subdir)

    if os.path.isdir(subdir_path):
        total_subdirs += 1

        images = [
            f for f in os.listdir(subdir_path)
            if f.lower().endswith(image_exts)
        ]

        count = len(images)
        line = f"{subdir}: {count} images"
        report_lines.append(line)

# Print results
print(f"Total subdirectories: {total_subdirs}\n")
for line in report_lines:
    print(line)

# Save to file
with open("../data/combined-dataset-true/train/report.txt", "w") as f:
    f.write(f"Total subdirectories: {total_subdirs}\n\n")
    f.write("\n".join(report_lines))

print("\nReport saved to report.txt")