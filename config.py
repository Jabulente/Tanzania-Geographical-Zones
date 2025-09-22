import os

OUTPUT_PATH = "./outputs"
REGIONS_SHAPEFILE = "./datasets/Regions.shp"
DEFAULT_CMAP = "viridis"

# Create output folder if it doesn't exist
os.makedirs(OUTPUT_PATH, exist_ok=True)
