<h2 align='center'> Visualization of Tanzania Geographical Zones and Its Regions</h1>

## 📌 Project Overview

This project provides a geospatial visualization of **Tanzania's geographical zones and regions**. It uses geospatial data to map each zone, display regions, and annotate them for easy identification. The visualizations include simulated data (e.g., salary distribution) to demonstrate thematic mapping techniques.

The project is built with **Python** using `geopandas`, `matplotlib`, and other supporting libraries.

---

## 🗂️ Project Structure

```text
Tanzania Geographical Zones/
├── datasets/
│   └── Regions.shp           # Shapefile of Tanzania regions
├── outputs/                  # Folder where generated maps are saved
├── config.py                 # Global settings, paths, and defaults
├── data_loader.py            # Functions for loading and preprocessing geospatial data
├── plot_utils.py             # Functions for plotting, annotating, and saving maps
├── tanzania_zones.py         # Definition of Tanzania zones and their regions
├── main.py                   # Main script to run visualizations
├── requirements.txt          # Python dependencies
└── README.md                 # Project documentation
```

---

## ⚙️ Features

* Loads and preprocesses **Tanzania regions shapefile** using GeoPandas.
* Annotates regions with safe centroid calculations.
* Generates **maps for each geographical zone**:

  * Lake Zone, Northern Zone, Central Zone, Southern Zone, Southern Highlands, Western Zone, Pemba, Unguja.
* Supports **custom colormaps** for thematic visualization.
* Adds **footer and credits** with timestamps and data source.
* Saves high-resolution PNG maps to an output folder.

---

## 🛠️ Installation

1. Clone the repository:

```bash
git clone https://github.com/Jabulente/Tanzania-Geographical-Zones.git
cd Tanzania-Geographical-Zones
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Make sure the dataset is available:

```
./datasets/Regions.shp
```

---

## 🚀 Usage

Run the main script to generate visualizations:

```bash
python main.py
```

* Output maps are saved to the folder defined in `config.py` (`outputs/` by default).
* Each zone map will show regions, annotated names, and a simulated thematic variable (salary).

---

## 🖼️ Example Output

* **Lake Zone Map** – regions annotated with names and salary distribution.
* **Northern Zone Map** – clear distinction of regions with color-coded salary values.

*(You can insert example PNGs here for visual reference.)*

---

## 🔧 Customization

* Change colormap by editing `cmap` parameter in `visualize_regions()` in `main.py`.
* Adjust font size, figure size, and other plotting parameters in `plot_utils.py`.
* Add real data instead of simulated salary for thematic mapping.

---

## 📚 Dependencies

* Python ≥ 3.9
* geopandas
* matplotlib
* numpy
* pandas
* pypalettes

Install all dependencies using:

```bash
pip install geopandas matplotlib numpy pandas pypalettes
```

---

## 📄 License

This project is open for personal, educational, and research purposes. Please credit the author when using the visualizations.
