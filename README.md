# Data-Analysis-and-ML
```python
# Inspect the Slovakian data to accurately describe fig_SVK.png
svk = df[df['Country'] == 'SVK']
print(svk.groupby(['Sport', 'Medal']).size())


```

```text
Traceback (most recent call last):
  File "<xbox-string>", line 2, in <module>
    svk = df[df['Country'] == 'SVK']
NameError: name 'df' is not defined


```

```python
import pandas as pd
df = pd.read_csv('Olympics-Data.csv')
svk = df[df['Country'] == 'SVK']
print(svk.groupby(['Sport', 'Medal']).size())


```

```text
Sport          Medal 
Aquatics       Silver     2
Canoe          Bronze     3
Canoe / Kayak  Bronze     5
               Gold      10
               Silver     7
Judo           Silver     1
Shooting       Bronze     3
               Silver     2
Wrestling      Bronze     1
dtype: int64


```

# Olympic Games Historical Data Analysis & Visualizations

An exploratory data analysis (EDA) of historical Olympic Games medal records, exploring gender participation over time, all-time nation rankings, and discipline-level performance breakdowns.

---

## Visualizations & Key Findings

### 1. Gender Participation & Medal Trajectory (`fig_gen.png`)

* **Focus:** Historical distribution of medals won by male vs. female athletes from 1896 to modern editions.


* **Insight:** Highlights the disparity in early modern Olympic Games alongside the steady, accelerated rise in women's medal counts beginning in the 1970s and 1980s.



---

### 2. All-Time Gold Medal Dominance (`fig_top10.png`)

* **Focus:** Top 10 countries by cumulative Olympic gold medal count.


* **Insight:** Highlights the United States (USA) as the dominant historical leader with over 2,000 gold medals, followed by the Soviet Union (URS), Great Britain (GBR), Italy (ITA), and Germany (GER).



---

### 3. National Discipline & Medal Breakdown: Slovakia (`fig_SVK.png`)

* **Focus:** Sunburst / nested donut chart displaying Olympic medals won by Slovakia (SVK) categorized by sport and medal tier.


* **Insight:** Shows clear historical specialization in white-water events, with **Canoe / Kayak** capturing the vast majority of Slovak gold and total medals, complemented by podium finishes in Shooting, Canoe, Aquatics, Judo, and Wrestling.



---

## Dataset Overview

The dataset (`Olympics-Data.csv`) records Olympic medalists with the following attributes:

| Field | Description |
| --- | --- |
| `Year` | Olympic edition year (1896 onwards)

 |
| `City` | Host city (e.g., Athens, London, Beijing)

 |
| `Sport` | Core Olympic sport category (e.g., Aquatics, Canoeing)

 |
| `Discipline` | Specific sporting discipline (e.g., Swimming, Diving)

 |
| `Athlete` | Competitor name

 |
| `Country` | Three-letter IOC country code (e.g., USA, HUN, SVK)

 |
| `Gender` | Athlete gender (`Men` / `Women`)

 |
| `Event` | Specific competitive event

 |
| `Medal` | Result achieved (`Gold`, `Silver`, `Bronze`)

 |

---

## Tech Stack & Setup

* **Language:** Python
* **Data Manipulation:** `pandas`, `numpy`
* **Plotting & Styling:** `matplotlib`, `seaborn`

```bash
# Clone the repository
git clone https://github.com/your-username/olympic-data-analysis.git
cd olympic-data-analysis

# Install dependencies
pip install pandas matplotlib seaborn

```
