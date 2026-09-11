# COMP1878 Coursework
#Task 3 - Training an Air Quality Classifier

#importing libraries
import os
import pandas as pd
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split

base_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
csv_file = os.path.join(base_dir, "data", "processed", "air_pollution_processed.csv")
processed_directory = os.path.join(base_dir, "reports")

#loading the csv file into pandas dataframe
#file_name= path to csv file. returns dataframe to containing file content, raises file not error is no existing file at path
def load_data(file_name):
    try:
        return pd.read_csv(file_name)
    except FileNotFoundError:
        print("Processed CSV file not found.")
        raise

#splitting data, training classifier and returning the predictions
#perfoming a 75/25 train/test split model using randomforest
def apply_model(model, x, y):
    x_train, x_test, y_train, y_test = train_test_split(
        x, y, test_size=0.25, random_state=42
    )

    model.fit(x_train, y_train)
    predictions = model.predict(x_test)

    return model, y_test, predictions

#printing out the feature importance of trained tree based model:
def show_feature_importance(model, feature_names):
    importance = pd.Series(
        model.feature_importances_,
        index=feature_names
    ).sort_values(ascending=False)

    print("\nFeature importance:")
    print(importance)

#saving classifier accuracy results to text file in reports
def save_results(results):
    os.makedirs(processed_directory, exist_ok=True)

    report_path = os.path.join(processed_directory, "results_summary.txt")
    with open(report_path, "w", encoding="utf-8") as file:
        file.write("Air Quality Classifier Results\n")
        file.write("=" * 60 + "\n")

        for name, accuracy in results.items():
            file.write(f"{name}: {accuracy * 100:.2f}%\n")

    print(f"\nResults saved to {report_path}")

#running full training model and evaluation pipeline for both classifiers
def train_and_evaluate():
    df = load_data(csv_file)

    # remove location if it exists, because it is not numeric
    if "location" in df.columns:
        x = df.drop(columns=["location", "aqi"])
    else:
        x = df.drop(columns=["aqi"])

    y = df["aqi"]

    classifiers = {
        "RandomForestClassifier": RandomForestClassifier(
            n_estimators=100,
            random_state=42
        ),
        "GradientBoostingClassifier": GradientBoostingClassifier(
            n_estimators=100,
            random_state=42
        )
    }

    results = {}

    for name, model in classifiers.items():
        trained_model, y_test, predictions = apply_model(model, x, y)
        accuracy = accuracy_score(y_test, predictions)
        results[name] = accuracy

        print(f"\n{name}")
        print(f"Accuracy: {accuracy * 100:.2f}%")

        if hasattr(trained_model, "feature_importances_"):
            show_feature_importance(trained_model, x.columns)

    save_results(results)
    return results


if __name__ == "__main__":
    if os.path.exists(csv_file):
        results = train_and_evaluate()

        print("\nFinal results:")
        for name, accuracy in results.items():
            print(f"{name}: {accuracy * 100:.2f}%")
    else:
        print("No processed data found.")
        print("Please run main.py first.")