# Data Protection Impact Assessment (DPIA) – EU Hospital Discharges Project

## Purpose
This project analyzes **aggregated Eurostat hospital discharge data** to compare healthcare system trends across European countries.

## Data Governance
- **Source:** Eurostat (open, aggregated, non-personal data).
- **Identifiers:** Only country/region codes (e.g., BE, DE, FR). No individual-level data is used.
- **Personal Data:** None. Dataset is fully anonymized and aggregated.

## Risks
- No GDPR risk since no personal, sensitive, or identifiable data is processed.
- Low risk of misinterpretation if results are presented without context (policy and healthcare differences must be considered).

## Safeguards
- Transparent workflow: all scripts, cleaned datasets, and dashboards are open-source.
- Reproducibility: analysis can be rerun from scratch using the provided Colab notebook.
- Responsible reporting: results framed in policy context, not as judgments on healthcare quality.

## Conclusion
The project complies with GDPR and FAIR principles (Findable, Accessible, Interoperable, Reusable).  
No further DPIA steps required.
