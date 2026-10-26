import glob
import json
import os
import pandas as pd


def transform_weather_data():
    raw_files = glob.glob("data/raw/*.json")

    if not raw_files:
        print("No raw data files found to transform!")
        return

    print(f"Found {len(raw_files)} raw weather file(s). Processing...")

    records = []

    # Read and parse raw JSON files
    for file_path in raw_files:
        with open(file_path, "r") as f:
            item = json.load(f)

            record = {
                "city": item.get("name"),
                "temperature": item.get("main", {}).get("temp"),
                "feels_like": item.get("main", {}).get("feels_like"),
                "humidity": item.get("main", {}).get("humidity"),
                "weather_condition": (
                    item["weather"][0].get("description")
                    if item.get("weather")
                    else None
                ),
                "timestamp": item.get("dt"),
            }
            records.append(record)

    # Clean DataFrame and format timestamps
    df = pd.DataFrame(records)
    df = df.dropna(subset=["city", "temperature"])
    df["timestamp"] = pd.to_datetime(df["timestamp"], unit="s")
    df = df.drop_duplicates(subset=["city", "timestamp"])

    os.makedirs("data/processed", exist_ok=True)

    # Export cleaned dataset to CSV
    output_path = "data/processed/weather_cleaned.csv"
    df.to_csv(output_path, index=False)

    print(f"Success! Transformed data saved to {output_path}")
    print("\nPreview of cleaned data:")
    print(df)


if __name__ == "__main__":
    transform_weather_data()