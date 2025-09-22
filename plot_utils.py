import matplotlib.pyplot as plt
from datetime import datetime
from typing import Dict, List, Optional
import random

def annotate_regions(zone_gdf, ax, color="black", fontsize=12):
    for _, row in zone_gdf.iterrows():
        try:
            point = row.geometry.representative_point()
            ax.text(
                point.x,
                point.y,
                row.get("Region_Nam", "Unknown"),
                fontsize=fontsize,
                ha="center",
                va="center",
                weight="bold",
                color=color,
            )
        except Exception as e:
            print(f"Skipping region due to geometry issue: {e}")


def add_footer_and_credits(fig, created_by="Jabulente"):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M")
    fig.text(
        0.5, 0.02,
        f"Data Source: World Bank | Created by: {created_by} | Generated: {timestamp}",
        ha="center", va="center", fontsize=10, weight="bold", color="black", style="italic"
    )


def visualize_regions(
    gdf,
    zones: Dict[str, List[str]],
    output_path: Optional[str] = None,
    cmap: str = "Oranges"
):
    plt.rcParams.update({"font.family": "Arial", "font.size": 18})

    for zone_name, regions in zones.items():
        zone_gdf = gdf[gdf["Region_Nam"].isin(regions)]
        fig, ax = plt.subplots(figsize=(10, 10), facecolor="white")
        
        cmap_name = random.choice(plt.colormaps())
        zone_gdf.plot(ax=ax, column="salary", cmap=cmap, edgecolor="black", linewidth=0.5, legend=False)
        annotate_regions(zone_gdf, ax, fontsize=14)

        fig.text(0.5, 0.95, f"Tanzania {zone_name} and Its Regions".upper(), color="black", fontweight="bold", ha="center", size=16)
        add_footer_and_credits(fig)

        ax.axis("off")
        fig.tight_layout()

        if output_path:
            filename = f"{output_path}/{zone_name}.png"
            plt.savefig(filename, dpi=300, bbox_inches="tight")
            print(f"Saved map: {filename}")

        plt.close()
