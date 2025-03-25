# Origin-Destination Transportation Centrality

## Setup
### Cloning the Repository

```sh
git https://github.com/omzkiii/thesis.git
cd thesis
```

---

### Environment Setup

1. **Create a virtual environment**:
   ```bash
   python -m venv env
   ```

2. **Activate the virtual environment**:

- On Windows:
```sh
.\env\Scripts\activate
```

- On macOS/Linux:
```sh
source env/bin/activate
```

3. **Install the required packages**:
```sh
pip install -r requirements.txt
```

---

## ODTC Runtime Analysis

### 1. Run Simulation (Generate 500 ODTC & TC Runtimes)

```bash
python controllers/main.py
```

This will simulate **500 iterations** of ODTC and TC across a given area.

####  Usage:
- If you have a **place name**:
```python
evaluation("Quiapo, Manila", None, ["school", "college", "institute", "university"])
```
- If you have **coordinates**:
```python
evaluation(
    coordinates,  # e.g., (14.5995, 120.9842)
    distance_meters,  # e.g., 1000
    ["school", "college", "institute", "university"]
)
```

> [!NOTE]
> Be sure to set the `graph_type` variable manually to label the output as **Grid**, **Scale-Free**, or **Ring**.


---

### 2. Analyze Runtime Statistics

```bash
python controllers/analyze_runtime.py
```

Performs:
- Normality tests using D'Agostino and Pearson
- Paired t-test or Wilcoxon signed-rank test
- Prints means, statistical test results, and normality conclusions

---

### 3. Launch the GUI (Graphical Analysis + Visualization)

```bash
python gui/main_window.py
```

This opens a full GUI for:
- Viewing statistical test results
- Exploring bar charts and by graph type
- Viewing normality test visualizations (Q-Q and histograms)

---

### 4. Display Central Nodes from Any Location

```bash
python displayCentralNodes.py
```


> [!IMPORTANT]
> - Make sure `execution_times.csv` exists before running the GUI or analyzer.
> - If you're modifying the simulation or GUI, keep your virtual environment activated.


---

## ODTD/Steiner Network Route Construction

To run the main gui:
```sh
python ./main.py
```

The program will output an HTML file.

Since the algorthim takes a long time to process the program will used the generated HTML if there is any.

To generate a new one simply delete the HTML file of the desired location.

The HTML files are named as "app/{location} - {amenities}.html"



