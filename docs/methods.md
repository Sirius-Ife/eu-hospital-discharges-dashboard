# Methods Note: Hospital Discharge Analysis

## Data
- **Source:** Eurostat (public, aggregated datasets).
- **Indicators:** Inpatient hospital discharges (ICD10: A–T_Z), per 100,000 inhabitants.
- **Years:** 2017–2021.
- **Coverage:** EU Member States + selected non-EU countries (e.g., CH, NO).

## Processing
1. Download raw Eurostat TSV data via Python in Google Colab.
2. Clean:
   - Filtered for indicator = `INPAT`, unit = `P_HTHAB`, age = `TOTAL`.
   - Kept only years 2017–2021.
   - Removed empty/missing values.
3. Saved two datasets:
   - `hospital-discharge-cleaned.csv` → 20,837 rows (2017–2021).
   - `hospital-discharge-latest.csv` → 4,103 rows (2021 only).

## Analysis
- **Trends (multi-year):** Line plots of discharge rates by country.
- **Cross-sectional (latest year):** Bar charts + distribution plots (2021 snapshot).
- **Comparative stats:** Regional grouping (West/North/South/East).
- **Dashboard:** Power BI visuals for interactive exploration.

## Limitations
- Discharge data may not be directly comparable (coding/reporting differences).
- Rates reflect **system organization**, not necessarily quality or health outcomes.
- COVID-19 disruptions complicate year-on-year comparisons.

## Reproducibility
- Entire pipeline in `hospital_discharge_analysis.ipynb` (Colab).
- Outputs stored in `/data/cleaned`.
- Dashboards stored as `.pbix` files for Power BI.
