## 📥 Cloning the Repository

Make sure to clone the `geo2` branch:

```bash
git clone -b geo2 https://github.com/yourusername/yourrepo.git
cd yourrepo
```

---

## 🔧 Environment Setup

1. **Create a virtual environment** (recommended):
   ```bash
   python -m venv env
   ```

2. **Activate the virtual environment**:

   - On Windows:
     ```bash
     .\env\Scripts\activate
     ```

   - On macOS/Linux:
     ```bash
     source env/bin/activate
     ```

3. **Install the required packages**:
   ```bash
   pip install -r requirements.txt
   ```

---

## 🚀 How to Use

### 1️⃣ Run Simulation (Generate 500 ODTC & TC Runtimes)

```bash
python controllers/main.py
```

This will simulate **500 iterations** of ODTC and TC across a given area.

#### 🔹 Usage:
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

✅ Be sure to set the `graph_type` variable manually to label the output as **Grid**, **Scale-Free**, or **Ring**.

---

### 2️⃣ Analyze Runtime Statistics

```bash
python controllers/analyze_runtime.py
```

Performs:
- Normality tests using D'Agostino and Pearson
- Paired t-test or Wilcoxon signed-rank test
- Prints means, statistical test results, and normality conclusions

---

### 3️⃣ Launch the GUI (Graphical Analysis + Visualization)

```bash
python gui/main_window.py
```

This opens a full GUI for:
- Viewing statistical test results
- Exploring bar charts and by graph type
- Viewing normality test visualizations (Q-Q and histograms)

---

### 4️⃣ Display Central Nodes from Any Location

```bash
python displayCentralNodes.py
```

Checks if a location (e.g., city or neighborhood) has **strong node connection**,

---

## 📁 Project Structure

```
.
├── controllers/
│   ├── main.py                # Main simulation logic (ODTC vs TC)
│   └── analyze_runtime.py     # Performs statistical tests
│
├── gui/
│   ├── main_window.py         # Launch GUI
│   └── handlers/              # GUI graph handlers (bar, box, normality)
│
├── displayCentralNodes.py     # CLI tool for analyzing centrality of a location
├── execution_times.csv        # Output file for simulation results
├── requirements.txt           # Python package dependencies
└── README.md                  # You’re here!
```

---

## 📌 Notes

- Make sure `execution_times.csv` exists before running the GUI or analyzer.
- If you're modifying the simulation or GUI, keep your virtual environment activated.

---
