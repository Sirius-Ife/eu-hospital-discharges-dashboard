# EU Hospital Discharge Analysis

This project explores **hospital discharge rates across European countries (2017–2021)** using Eurostat data.  
It combines Python (Google Colab) for cleaning and analysis, and Power BI for interactive visualizations.  

## Project Goals
- Compare inpatient hospital discharge trends across Europe.
- Highlight cross-country differences in the latest available year (2021).
- Provide policy-relevant insights into healthcare demand and system capacity.

## Data
- Source: [Eurostat – Hospital discharges and length of stay](https://ec.europa.eu/eurostat)
- Cleaned datasets:
  - `hospital-discharge-cleaned.csv` → Multi-year data (2017–2021)
  - `hospital-discharge-latest.csv` → Latest snapshot (2021)

## Tools Used
- **Python (Colab):** Data download, cleaning, descriptive analysis
- **Power BI:** Dashboards and comparative visualizations
- **GitHub:** Version control and reproducibility

## How to Reproduce
1. Open the Colab notebook: `hospital_discharge_analysis.ipynb`
2. Run all cells to download and clean data.
3. Export cleaned CSVs.
4. Open `hospital_discharge.pbix` in Power BI to explore dashboards.

## Key Findings
- Discharge rates vary significantly across Europe (from <10,000 to >35,000 per 100k).
- COVID-19 disruptions (2020–2021) caused visible shifts in several countries.
- Western and Northern Europe generally show lower inpatient discharge rates compared to Eastern Europe.

---
