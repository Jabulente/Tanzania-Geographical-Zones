import geopandas as gpd
import numpy as np

def load_dataset(filepath: str) -> gpd.GeoDataFrame:
    gdf = gpd.read_file(filepath)
    # Add simulated salary data
    gdf["salary"] = np.random.randint(400, 12000, size=len(gdf))

    # Precompute centroids (safe projection handling)
    gdf_projected = gdf.to_crs(epsg=3035)
    gdf_projected["centroid"] = gdf_projected.geometry.centroid
    gdf["centroid"] = gdf_projected["centroid"].to_crs(gdf.crs)

    return gdf
