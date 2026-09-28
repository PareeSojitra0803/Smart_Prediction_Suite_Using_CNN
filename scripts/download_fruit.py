from datasets import load_dataset
import os

# Load RAW dataset
ds = load_dataset(
    "Project-AgML/fresh_rotten_fruit_classification",
    "raw",
    split="train"
)

# Create folders
os.makedirs("../Data/fruit_dataset/Fresh", exist_ok=True)
os.makedirs("../Data/fruit_dataset/Rotten", exist_ok=True)

fresh_count = 0
rotten_count = 0

for i, item in enumerate(ds):

    label = item["label"]
    image = item["image"]

    if label == 0 and fresh_count < 1000:
        image.save(f"../Data/fruit_dataset/Fresh/fresh_{fresh_count}.jpg")
        fresh_count += 1

    elif label == 1 and rotten_count < 1000:
        image.save(f"../Data/fruit_dataset/Rotten/rotten_{rotten_count}.jpg")
        rotten_count += 1

    if fresh_count == 1000 and rotten_count == 1000:
        break

print("Done!")
print("Fresh:", fresh_count)
print("Rotten:", rotten_count)