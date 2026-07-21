import pandas as pd
from datetime import date

file = "data/raw/impact_links.csv"

df = pd.read_csv(file)


new_link = {
    "record_id": "IMP_NEW_001",
    "parent_id": "EVT_NEW_001",
    "pillar": "access",
    "related_indicator": "ACCOUNT_OWNERSHIP",
    "impact_direction": "positive",
    "impact_magnitude": "medium",
    "lag_months": 12,
    "evidence_basis": "Digital financial inclusion policies can increase account ownership",
    "collected_by": "Hawinet Zewde",
    "collection_date": str(date.today()),
    "notes": "Added relationship between digital policy and financial inclusion access"
}


new_df = pd.DataFrame([new_link])


# keep same columns as original
new_df = new_df.reindex(columns=df.columns)


enriched = pd.concat(
    [df, new_df],
    ignore_index=True
)


enriched.to_csv(
    "data/processed/impact_links_enriched.csv",
    index=False
)


print("New impact links shape:", enriched.shape)