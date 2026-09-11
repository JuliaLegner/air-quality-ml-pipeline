# COMP 1878 Coursework
# Task 2 - Data Handling

#importing libraries
import json
import os
import pandas as pd
from sklearn.preprocessing import MinMaxScaler

base_direction = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
rawd = os.path.join(base_direction,"data", "raw")
processedd = os.path.join(base_direction, "data", "processed")



#loading worldwide locations CSV
#file_name= path to CSV, return DataFrame from CSV
def load_data(file_name):
    df = pd.read_csv(file_name)
    return df

# selecting locations from the CSV
location_s = ["Agra", "Baghdad", "Bamenda", "Banff", "Bangkok", "Belgrade", "Bucharest",
                      "Buenos Aires", "California", "Cape Town", "Chicago", "Delhi", "Denver",
                      "Dhaka", "Faisalabad", "Gaya", "Incheon", "Istanbul", "Jakarta", "Jodhpur",
                      "Johannesburg", "Kanpur", "Kathmandu", "Katowice", "Kemerovo", "Kuala Lumpur",
                      "Lanzhou", "Lima", "Lisbon", "Los Angeles", "Madrid", "Marseille", "Mexico City",
                      "Mumbai", "New Delhi", "Norilsk", "Omsk", "Paris", "Patna", "Piacenza", "Prague",
                      "Rawalpindi", "Riyadh", "Santiago", "Shenyang", "Shijiazhuang", "Slavonski Brod",
                      "Sofia", "Stockholm", "Sydney", "Tehran", "Tianjin", "Toluca", "Turin", "Ulan-Ude",
                      "Vancouver", "Vicenza", "Warsaw", "Wellington", "Xi'an"]

# filtering the DataFrame to only keep selected locations
def get_locations(df):
    locations = df[df["name"].isin(location_s)]
    return locations


# fetching data from API for each location and save as JSON
def fetch_and_save_raw_data(api, locations):
    os.makedirs(rawd, exist_ok=True)
    for _, row in locations.iterrows():
        name = row["name"].replace(" ", "_").replace("'", "")
        lat = row["latitude"]
        lon = row["longitude"]
        print(f"Fetching data for {row['name']}...")
        data = api.get_air_pollution_data(lat, lon)

        if data is None:
            print(f"  Skipping {row['name']} — no data returned.")
            continue

        filepath = os.path.join(rawd, f"{name}.json")
        with open(filepath, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4)


    print(f"\nRaw data for {len(locations)} locations saved to '{rawd}/'.")


#reading all JSON files and combining them into one DataFrame
def load_raw_data_dataframe():
    records = []

    for filename in sorted(os.listdir(rawd)):
        if not filename.endswith(".json"):
            continue
        filepath = os.path.join(rawd, filename)
        with open(filepath, "r", encoding="utf-8") as f:
            data = json.load(f)

        item = data["list"][0]
        record = {"aqi": item["main"]["aqi"],
            "co": item["components"].get("co"),
            "no": item["components"].get("no"),
            "no2": item["components"].get("no2"),
            "o3": item["components"].get("o3"),
            "so2": item["components"].get("so2"),
            "pm2_5": item["components"].get("pm2_5"),
            "pm10": item["components"].get("pm10"),
            "nh3": item["components"].get("nh3")}

        records.append(record)

    df = pd.DataFrame(records)
    print(f"Loaded {len(df)} records from '{rawd}/'.")
    return df


# summarising data of raw air data quality to console
def summarise_data(df):
    print("\nData Summary:")
    print("----------------")
    print(f"Total number locations: {len(df)}")
    print(f"Average AQI: {df['aqi'].mean():.2f}")
    print(f"Most common AQI: {df['aqi'].mode()[0]}")
    print(f"Worst recorded AQI: {df['aqi'].max()}")
    print(f"Best recorded AQI: {df['aqi'].min()}")
    print("\n")


# filling missing values, normalise columns and save to CSV
def process_and_save(df):
    os.makedirs(processedd, exist_ok=True)
    # Fill missing values with column mean
    df = df.fillna(df.mean(numeric_only=True))


    #normalising all feature columns except aqi
    feature_cols = [col for col in df.columns if col != "aqi"]
    scaler = MinMaxScaler()
    df[feature_cols] = scaler.fit_transform(df[feature_cols])

    processed_path = os.path.join(processedd, "air_pollution_processed.csv")
    df.to_csv(processed_path, index=False)
    print(f" processed data saved to '{processed_path}'.")
    return df


if __name__ =="__main__":
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    csv_path = os.path.join(base_dir, "data", "worldwide_locations.csv")

    df_locations = load_data(csv_path)
    locations = get_locations(df_locations)
    print(f"Selected {len(locations)} locations:")
    print(locations)

    # Load raw data and print summary
    if os.path.exists(rawd) and len(os.listdir(rawd)) > 0:
        df_raw = load_raw_data_dataframe()
        summarise_data(df_raw)
    else:
        print("\n No raw data yet - run main.py first to fetch data.")