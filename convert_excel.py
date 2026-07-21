import pandas as pd

# Main dataset
file = "data/raw/ethiopia_fi_unified_data.xlsx"

# Read first sheet
data = pd.read_excel(
    file,
    sheet_name="ethiopia_fi_unified_data"
)

# Read impact sheet
impact = pd.read_excel(
    file,
    sheet_name="Impact_sheet"
)

# Save CSV versions
data.to_csv(
    "data/raw/ethiopia_fi_unified_data.csv",
    index=False
)

impact.to_csv(
    "data/raw/impact_links.csv",
    index=False
)


# Reference codes
reference = pd.read_excel(
    "data/raw/reference_codes.xlsx"
)

reference.to_csv(
    "data/raw/reference_codes.csv",
    index=False
)

print("Conversion completed!")
print("Data:", data.shape)
print("Impact:", impact.shape)
print("Reference:", reference.shape)