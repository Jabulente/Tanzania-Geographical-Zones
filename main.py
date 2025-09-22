from config import OUTPUT_PATH, REGIONS_SHAPEFILE
from data_loader import load_dataset
from plot_utils import visualize_regions
from tanzania_zones import TANZANIA_ZONES

if __name__ == "__main__":
    gdf = load_dataset(REGIONS_SHAPEFILE)
    visualize_regions(gdf, TANZANIA_ZONES, OUTPUT_PATH)
