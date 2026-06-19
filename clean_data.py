import pandas as pd

# Load Dataset
df = pd.read_csv("data/raw/hotel_bookings.csv")

print("Dataset Loaded")
print(df.shape)

# Remove duplicates
df.drop_duplicates(inplace=True)

print("Duplicates Removed")

# Fill missing values

if "agent" in df.columns:
    df["agent"] = df["agent"].fillna(0)

if "company" in df.columns:
    df["company"] = df["company"].fillna(0)

if "country" in df.columns:
    df["country"] = df["country"].fillna("Unknown")

if "children" in df.columns:
    df["children"] = df["children"].fillna(0)

# Create feature

df["total_stay"] = (
    df["stays_in_weekend_nights"]
    +
    df["stays_in_week_nights"]
)

# Missing Values

print("\nMissing Values:")
print(df.isnull().sum())

# Basic Summary

print("\nCancellation Rate:")
print(df["is_canceled"].mean())

print("\nAverage ADR:")
print(df["adr"].mean())

# Export

df.to_csv(
"data/cleaned/clean_hotel.csv",
index=False
)

print("\nWeek 1 Completed!")