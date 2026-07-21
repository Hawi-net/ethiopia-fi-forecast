import pandas as pd

# Load datasets
data = pd.read_csv(
    "data/raw/ethiopia_fi_unified_data.csv"
)

impact = pd.read_csv(
    "data/raw/impact_links.csv"
)

reference = pd.read_csv(
    "data/raw/reference_codes.csv"
)


print("DATA")
print(data.head())

print("\nShape:")
print(data.shape)


print("\nIMPACT LINKS")
print(impact.head())

print("\nShape:")
print(impact.shape)


print("\nREFERENCE CODES")
print(reference.head())

print("\nShape:")
print(reference.shape)
print("\n==============================")
print("RECORD TYPE COUNT")
print("==============================")

print(data["record_type"].value_counts())


print("\n==============================")
print("PILLAR COUNT")
print("==============================")

print(data["pillar"].value_counts())


print("\n==============================")
print("SOURCE TYPE COUNT")
print("==============================")

print(data["source_type"].value_counts())


print("\n==============================")
print("CONFIDENCE COUNT")
print("==============================")

print(data["confidence"].value_counts())


print("\n==============================")
print("DATE RANGE")
print("==============================")

data["observation_date"] = pd.to_datetime(
    data["observation_date"],
    errors="coerce"
)

print("Start:", data["observation_date"].min())
print("End:", data["observation_date"].max())


print("\n==============================")
print("UNIQUE INDICATORS")
print("==============================")

print(data["indicator_code"].unique())


print("\nNumber of indicators:")
print(data["indicator_code"].nunique())

print(data.columns.tolist())
print("\n==============================")
print("EVENTS")
print("==============================")

events = data[data["record_type"]=="event"]

print(events[[
    "record_id",
    "category",
]])


print("\n==============================")
print("IMPACT LINKS")
print("==============================")

print(
    impact[
        [
        "parent_id",
        "related_indicator",
        "impact_direction",
        "lag_months"
        ]
    ]
)