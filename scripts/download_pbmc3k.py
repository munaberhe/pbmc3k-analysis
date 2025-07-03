import scanpy as sc
import os

# Create the path if it doesn't exist
output_path = "data/raw"
os.makedirs(output_path, exist_ok=True)

# Load the PBMC 3k dataset
print("Downloading PBMC 3k dataset...")
adata = sc.datasets.pbmc3k()

# Save the dataset as .h5ad
save_path = os.path.join(output_path, "pbmc3k.h5ad")
adata.write(save_path)

print(f"Dataset saved to {save_path}")
