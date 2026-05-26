# ☁️ Meteorological Data Analysis with the Hadoop Ecosystem

> **A Big Data pipeline built on Apache Hadoop MapReduce for large-scale meteorological data analysis. Implements 4 independent analytical jobs in Java to compute average temperatures, extreme temperatures, precipitation totals, and seasonal patterns from distributed weather datasets stored on HDFS.**

---

## 📋 Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Architecture](#architecture)
- [Project Structure](#project-structure)
- [The 4 MapReduce Analyses](#the-4-mapreduce-analyses)
- [MapReduce Pattern](#mapreduce-pattern)
- [Data Pipeline](#data-pipeline)
- [Getting Started](#getting-started)
- [Running the Jobs](#running-the-jobs)
- [Visualization](#visualization)
- [Dependencies](#dependencies)
- [Report](#report)
- [Author](#author)

---

## Overview

This project applies the **Apache Hadoop MapReduce** paradigm to process and analyze large-scale meteorological datasets. Weather data is ingested from a structured CSV file (`weather.csv`), stored on **HDFS** (Hadoop Distributed File System), and processed by 4 independent MapReduce jobs written in **Java**.

Each job follows the canonical Hadoop pattern of **Mapper → Shuffle & Sort → Reducer**, orchestrated by a **Driver** class. Results are written back to HDFS output directories and visualized using **Python (Matplotlib/Seaborn)**.

---

## Features

- **4 Independent MapReduce Jobs** — Each targeting a specific meteorological analysis
- **Full Hadoop MapReduce Stack** — Custom Mapper, Reducer, and Driver per job
- **HDFS Integration** — Input data loaded from and output written to HDFS paths
- **CSV Parsing in Mapper** — Handles quoted CSV fields, skips header rows
- **Error-Tolerant Parsing** — Silently skips malformed or incomplete records
- **Python Visualization** — Charts generated from MapReduce output using Matplotlib
- **Architecture Diagram** — Auto-generated system diagram (`architecture_diagram.py`)
- **Full Project Report** — PDF documentation included

---

## Architecture

```
                        ┌─────────────────────┐
                        │   weather.csv (raw)  │
                        │   (local filesystem) │
                        └──────────┬──────────┘
                                   │
                              hdfs dfs -put
                                   │
                                   ▼
                        ┌─────────────────────┐
                        │        HDFS          │
                        │  /user/hadoop/meteo  │
                        │  /input/weather.csv  │
                        └──────────┬──────────┘
                                   │
                    ┌──────────────┼──────────────┐
                    │              │              │              │
                    ▼              ▼              ▼              ▼
             ┌──────────┐  ┌──────────┐  ┌──────────┐  ┌──────────┐
             │ Job 1    │  │ Job 2    │  │ Job 3    │  │ Job 4    │
             │ Average  │  │ Extreme  │  │ Precipi- │  │ Seasonal │
             │ Temp     │  │ Temp     │  │ tations  │  │ Analysis │
             └────┬─────┘  └────┬─────┘  └────┬─────┘  └────┬─────┘
                  │              │              │              │
            ┌─────▼──────────────▼──────────────▼──────────────▼─────┐
            │                  MapReduce Engine                        │
            │                                                          │
            │   [Mapper]  →  [Shuffle & Sort]  →  [Reducer]          │
            │                                                          │
            │   Parse CSV        Group by key      Aggregate           │
            │   Emit (K, V)      Sort by key       Emit result         │
            └──────────────────────────┬───────────────────────────────┘
                                       │
                                       ▼
                        ┌─────────────────────┐
                        │        HDFS          │
                        │  /output/analyse1    │
                        │  /output/analyse2    │
                        │  /output/analyse3    │
                        │  /output/analyse4    │
                        └──────────┬──────────┘
                                   │
                                   ▼
                        ┌─────────────────────┐
                        │  visualisation.py    │
                        │  (Python + Matplotlib)│
                        │  Charts & Graphs     │
                        └─────────────────────┘
```

---

## Project Structure

```
Analyse-Donnees-Meteorologiques-Hadoop/
│
├── Mappeur(analyse1-temp-moyenne).java      # Mapper  — Average temperature per state
├── Reducteur(analyse1-temp-moyenne).java    # Reducer — Average temperature per state
├── Driver(analyse1-temp-moyenne).java       # Driver  — Job 1 configuration
│
├── Mappeur(analyse2-temp-extremes).java     # Mapper  — Min/Max temperatures
├── Reducteur(analyse2-temp-extremes).java   # Reducer — Min/Max temperatures
├── Driver(analyse2-temp-extremes).java      # Driver  — Job 2 configuration
│
├── Mappeur(analyse3-precipitations).java    # Mapper  — Precipitation totals
├── Reducteur(analyse3-precipitations).java  # Reducer — Precipitation totals
├── Driver(analyse3-precipitations).java     # Driver  — Job 3 configuration
│
├── Mappeur(analyse4-saisons).java           # Mapper  — Seasonal temperature patterns
├── Reducteur(analyse4-saisons).java         # Reducer — Seasonal temperature patterns
├── Driver(analyse4-saisons).java            # Driver  — Job 4 configuration
│
├── visualisation.py                         # Python charts from MapReduce results
├── architecture_diagram.py                  # Auto-generated system architecture diagram
├── Nidali-Hicham_Mini-Projet-BigData.pdf   # Full project report
└── README.md                                # Project documentation
```

---

## The 4 MapReduce Analyses

### Analysis 1 — Average Temperature per State
**Goal:** Compute the mean temperature for each U.S. state across all records.

| Component | Role |
|---|---|
| **Mapper** | Parses CSV, emits `(state_name, temperature)` |
| **Reducer** | Accumulates values, computes average per state |
| **Output** | `state → avg_temperature (°F)` |

---

### Analysis 2 — Extreme Temperatures (Min / Max)
**Goal:** Identify the highest and lowest temperatures ever recorded per state.

| Component | Role |
|---|---|
| **Mapper** | Emits `(state_name, temperature)` pairs |
| **Reducer** | Tracks minimum and maximum across all values per state |
| **Output** | `state → min_temp, max_temp` |

---

### Analysis 3 — Precipitation Totals
**Goal:** Aggregate total precipitation per state to identify the wettest regions.

| Component | Role |
|---|---|
| **Mapper** | Emits `(state_name, precipitation_value)` |
| **Reducer** | Sums all precipitation values per state |
| **Output** | `state → total_precipitation (inches)` |

---

### Analysis 4 — Seasonal Analysis
**Goal:** Compute average temperature per season per state to detect seasonal patterns.

| Component | Role |
|---|---|
| **Mapper** | Extracts month, maps to season, emits `(state_season, temperature)` |
| **Reducer** | Averages temperature per state-season combination |
| **Output** | `state_season → avg_temperature` |

---

## MapReduce Pattern

Every analysis follows the same **3-class structure**:

```
┌─────────────────────────────────────────────────────────────┐
│  Driver.java                                                 │
│  ─────────────────────────────────────────────────────────  │
│  - Configures the Hadoop Job                                 │
│  - Sets Mapper, Reducer, Output key/value types             │
│  - Defines HDFS input/output paths                           │
│  - Submits job and waits for completion                      │
└─────────────────────────────────────────────────────────────┘
          │
          ▼
┌─────────────────────────────────────────────────────────────┐
│  Mappeur.java  extends Mapper<LongWritable, Text, Text, IntWritable>
│  ─────────────────────────────────────────────────────────  │
│  Input:  (line_offset, raw_csv_line)                         │
│  Logic:  - Skips header (key == 0)                           │
│           - Splits line on `","` delimiter                   │
│           - Extracts state name (col 8) and temperature (col 9)│
│           - Emits: (state_name, temperature_int)             │
│  Output: (Text key, IntWritable value)                       │
└─────────────────────────────────────────────────────────────┘
          │
     [Hadoop Shuffle & Sort]
     Groups all values by key, sorted alphabetically
          │
          ▼
┌─────────────────────────────────────────────────────────────┐
│  Reducteur.java  extends Reducer<Text, IntWritable, Text, ...>
│  ─────────────────────────────────────────────────────────  │
│  Input:  (state_name, [temp1, temp2, temp3, ...])            │
│  Logic:  Aggregates the list of values (sum, min, max, avg)  │
│  Output: (state_name, result_value)                          │
└─────────────────────────────────────────────────────────────┘
```

---

## Data Pipeline

### Input Data Format
CSV file (`weather.csv`) stored on HDFS, with columns including:

| Column Index | Field | Example |
|---|---|---|
| 8 | State name | `"California"` |
| 9 | Average temperature (°F) | `"72"` |
| 10 | Precipitation | `"0.45"` |

### HDFS Paths

| Purpose | Path |
|---|---|
| Input data | `/user/hadoop/meteo/input/weather.csv` |
| Analysis 1 output | `/user/hadoop/meteo/output/analyse1` |
| Analysis 2 output | `/user/hadoop/meteo/output/analyse2` |
| Analysis 3 output | `/user/hadoop/meteo/output/analyse3` |
| Analysis 4 output | `/user/hadoop/meteo/output/analyse4` |

---

## Getting Started

### Prerequisites

- **Java JDK** 8+
- **Apache Hadoop** 2.x or 3.x (configured in pseudo-distributed or fully distributed mode)
- **Python** 3.8+ with `matplotlib`, `pandas`, `seaborn`
- `$HADOOP_CLASSPATH` environment variable set

### 1. Upload Data to HDFS

```bash
# Create HDFS directory structure
hdfs dfs -mkdir -p /user/hadoop/meteo/input

# Upload the dataset
hdfs dfs -put weather.csv /user/hadoop/meteo/input/
```

### 2. Compile & Package

```bash
# Compile all Java files for a given analysis
javac -classpath $HADOOP_CLASSPATH *.java

# Package into a JAR
jar -cvf analyse1.jar *.class
```

### 3. Install Python Dependencies

```bash
pip install matplotlib pandas seaborn
```

---

## Running the Jobs

### Analysis 1 — Average Temperature

```bash
hdfs dfs -rm -r /user/hadoop/meteo/output/analyse1

hadoop jar analyse1.jar Driver \
  /user/hadoop/meteo/input/weather.csv \
  /user/hadoop/meteo/output/analyse1
```

### Analysis 2 — Extreme Temperatures

```bash
hdfs dfs -rm -r /user/hadoop/meteo/output/analyse2

hadoop jar analyse2.jar Driver \
  /user/hadoop/meteo/input/weather.csv \
  /user/hadoop/meteo/output/analyse2
```

### Analysis 3 — Precipitation

```bash
hdfs dfs -rm -r /user/hadoop/meteo/output/analyse3

hadoop jar analyse3.jar Driver \
  /user/hadoop/meteo/input/weather.csv \
  /user/hadoop/meteo/output/analyse3
```

### Analysis 4 — Seasonal Patterns

```bash
hdfs dfs -rm -r /user/hadoop/meteo/output/analyse4

hadoop jar analyse4.jar Driver \
  /user/hadoop/meteo/input/weather.csv \
  /user/hadoop/meteo/output/analyse4
```

### Retrieve Results from HDFS

```bash
hdfs dfs -cat /user/hadoop/meteo/output/analyse1/part-r-00000
```

---

## Visualization

After all jobs complete, run the Python visualization script to generate charts from the MapReduce output:

```bash
python visualisation.py
```

This generates bar charts, heatmaps, and seasonal trend plots from the HDFS result files.

To regenerate the system architecture diagram:

```bash
python architecture_diagram.py
```

---

## Dependencies

| Technology | Version | Purpose |
|---|---|---|
| **Apache Hadoop** | 2.x / 3.x | Distributed processing framework |
| **Java JDK** | 8+ | MapReduce job implementation |
| **HDFS** | Built-in | Distributed file storage |
| **Python** | 3.8+ | Results visualization |
| `matplotlib` | Latest | Chart generation |
| `pandas` | Latest | HDFS output parsing |
| `seaborn` | Latest | Styled statistical charts |

---

## Report

The full project report (methodology, results, analysis, and conclusions) is available as a PDF:

📄 [`Nidali-Hicham_Mini-Projet-BigData.pdf`](./Nidali-Hicham_Mini-Projet-BigData.pdf)

---

## Author

**Hicham Nidali**
- GitHub: [@Hicham-nidali](https://github.com/Hicham-nidali)

---

*This project was developed as part of a Big Data engineering curriculum, applying distributed computing principles to real-world meteorological datasets using the Apache Hadoop ecosystem.*
