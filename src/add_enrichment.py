import pandas as pd
from datetime import date


file = "data/raw/ethiopia_fi_unified_data.csv"

df = pd.read_csv(file)


new_records = [

# New observation
{
"record_id": "REC_NEW_001",
"record_type": "observation",
"category": "",
"pillar": "access",
"indicator": "Financial account ownership",
"indicator_code": "ACCOUNT_OWNERSHIP",
"indicator_direction": "increase",
"value_numeric": 46,
"value_text": "46% of adults own an account",
"value_type": "percentage",
"unit": "%",
"observation_date": "2024-01-01",
"source_name": "World Bank Global Findex",
"source_type": "survey",
"source_url": "https://www.worldbank.org/en/publication/globalfindex",
"confidence": "high",
"collected_by": "Hawinet Zewde",
"collection_date": str(date.today()),
"original_text": "Financial account ownership data from Global Findex",
"notes": "Added because account ownership is a key financial inclusion forecasting indicator"
},


# New event
{
"record_id": "EVT_NEW_001",
"record_type": "event",
"category": "policy",
"pillar": "",
"indicator": "",
"indicator_code": "",
"indicator_direction": "",
"value_numeric": "",
"value_text": "",
"value_type": "",
"unit": "",
"observation_date": "2021-01-01",
"source_name": "National Bank of Ethiopia",
"source_type": "policy",
"source_url": "",
"confidence": "medium",
"collected_by": "Hawinet Zewde",
"collection_date": str(date.today()),
"original_text": "National digital payment initiatives",
"notes": "Policy event that may influence digital financial inclusion"
}

]


new_df = pd.DataFrame(new_records)

# Keep same column order
new_df = new_df.reindex(columns=df.columns)

# Combine
enriched = pd.concat(
    [df, new_df],
    ignore_index=True
)


# Save processed dataset
enriched.to_csv(
    "data/processed/ethiopia_fi_unified_data_enriched.csv",
    index=False
)


print("New shape:", enriched.shape)