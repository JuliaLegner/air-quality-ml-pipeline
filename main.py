#Main python file -connecting all
#Entry point  Air Quality Classifier project
#running full pipeline: API set up > data collection > data processing > classifier training > results/outcomes

import os
from dotenv import load_dotenv, find_dotenv
from COMP1878_advancedprogramming.api import OpenWeatherAirPollution
from COMP1878_advancedprogramming.dataset import (load_data, get_locations, fetch_and_save_raw_data, load_raw_data_dataframe, summarise_data, process_and_save)
from COMP1878_advancedprogramming.modeling.train import train_and_evaluate

dotenv_path = find_dotenv()
load_dotenv(dotenv_path)
API_KEY = os.environ.get("API_KEY")

if API_KEY is None:
    raise EnvironmentError(
        "API_KEY not found. Make sure your .env file exists "
        "and contains: API_KEY=your_key_here"
    )


base_dir = os.path.dirname(os.path.abspath(__file__))
CSV_PATH = os.path.join(base_dir, "data", "worldwide_locations.csv")


def main():
    print("=" * 60)
    print("COMP1878 Air Quality Classifier Project")
    print("=" * 60)

    #task 1: intialising the API key
    print("\n[Task 1] Initialising API client...")
    api = OpenWeatherAirPollution(API_KEY)
    print("API client ready.")

    #task 2: loading and filtering locations
    print("\n[Task 2] Loading locations from CSV...")
    df_locations = load_data(CSV_PATH)
    locations = get_locations(df_locations)
    print(f"Selected {len(locations)} locations.")

    #task 2: fetching and saving raw data
    print("\n[Task 2] Fetching raw air pollution data...")
    fetch_and_save_raw_data(api, locations)

    #task 2: loading raw data into DataFrame
    print("\n[Task 2] Loading raw data into DataFrame...")
    df_raw = load_raw_data_dataframe()
    summarise_data(df_raw)

    #task 2: processing and saving
    print("\n[Task 2] Processing and saving data...")
    process_and_save(df_raw)

    #task 3: training and evaluating classifiers
    print("\n[Task 3] Training classifiers...")
    results = train_and_evaluate()

    print("\n" + "=" * 60)
    print("Final Results:")
    for name, acc in results.items():
        print(f"  {name}: {acc * 100:.2f}%")
    print("=" * 60)


if __name__ == "__main__":
    main()
