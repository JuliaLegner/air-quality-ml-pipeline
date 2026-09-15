# pytest test suite for COMP1878
#test Task 1(API Class), Task 2(data handling), Task 3 (classifiers)

import pytest
import pandas as pd
from unittest.mock import MagicMock, patch
from COMP1878_advancedprogramming.api import OpenWeatherAirPollution
from COMP1878_advancedprogramming.dataset import (load_data, get_locations, summarise_data, location_s)
from COMP1878_advancedprogramming.modeling.train import apply_model
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score


# Test for Task 1: API Class
def test_api_stores_key():
    api = OpenWeatherAirPollution("testkey")
    assert api.api_key == "testkey"


def test_api_base_url():
    assert "air_pollution" in OpenWeatherAirPollution.url

def test_api_invalid_key_empty():
    with pytest.raises(ValueError):
        OpenWeatherAirPollution("")


def test_api_invalid_key_not_string():
    with pytest.raises(ValueError):
        OpenWeatherAirPollution(12345)


def test_air_pollution_returns_dict():
    mock_response = MagicMock()
    mock_response.status_code = 200
    mock_response.text = ('{"list": [{"main": {"aqi": 2},"components": {"co": 100.0, "no": 0.0, "no2": 2.94}}]}')
    with patch("COMP1878_advancedprogramming.api.requests.get", return_value=mock_response):
        api = OpenWeatherAirPollution("test_key")
        result = api.get_air_pollution_data(51.5, -0.1)
        assert isinstance(result, dict)
        assert "list" in result


def test_air_pollution_bad_status_returns_none():
    mock_response = MagicMock()
    mock_response.status_code = 401
    with patch("COMP1878_advancedprogramming.api.requests.get", return_value=mock_response):
        api = OpenWeatherAirPollution("bad_key")
        result = api.get_air_pollution_data(51.5, -0.1)
        assert result is None


@pytest.mark.parametrize("aqi, expected", [
    (1, "Good"),
    (2, "Fair"),
    (3, "Moderate"),
    (4, "Poor"),
    (5, "Very Poor"),
    (99, "Unknown"),
])
def test_aqi_description(aqi, expected):
    api = OpenWeatherAirPollution("test_key")
    assert api.get_aqi_description(aqi) == expected



# Test for Task 2: Data Handling
def test_data_returns_dataframe(tmp_path):
    csv_file = tmp_path / "test.csv"
    csv_file.write_text("name,latitude,longitude\nLondon,51.5,-0.1\n")
    df = load_data(str(csv_file))
    assert isinstance(df, pd.DataFrame)
    assert len(df) == 1


def test_load_data_expected_columns(tmp_path):
    csv_file = tmp_path / "test.csv"
    csv_file.write_text("name,latitude,longitude\nParis,48.8,2.3\n")
    df = load_data(str(csv_file))
    assert "name" in df.columns
    assert "latitude" in df.columns


def test_get_locations_filters():
    df = pd.DataFrame({
        "name": ["Baghdad", "London", "Paris"],
        "latitude": [33.3, 51.5, 48.8],
        "longitude": [44.4, -0.1, 2.3],
    })
    result = get_locations(df)
    assert "Baghdad" in result["name"].values
    assert "Paris" in result["name"].values
    assert "London" not in result["name"].values


def test_selected_locations_count():
    assert len(location_s) >= 30


def test_summarise_data_prints_output(capsys):
    df = pd.DataFrame({ "aqi": [1, 2, 3, 4, 5], "co": [100, 200, 300, 400, 500],    })
    summarise_data(df)
    captured = capsys.readouterr()
    assert "Total number locations" in captured.out
    assert "Average AQI" in captured.out


# Test for  Task 3: Classifier
def _sample_df():
    return pd.DataFrame({"co":[100, 200, 300, 400, 500, 600, 700, 800],
        "no":    [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8],
        "no2":   [1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0],
        "o3":    [80, 70, 60, 50, 40, 30, 20, 10],
        "so2":   [1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0],
        "pm2_5": [5.0, 10.0, 15.0, 20.0, 25.0, 30.0, 35.0, 40.0],
        "pm10":  [10, 20, 30, 40, 50, 60, 70, 80],
        "nh3":   [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8],
        "aqi":   [1, 2, 3, 4, 5, 1, 2, 3]})


def test_model_returns_three_values():
    df = _sample_df()
    X = df.drop(columns=["aqi"])
    y = df["aqi"]
    model = RandomForestClassifier(n_estimators=10, random_state=42)
    result = apply_model(model, X, y)
    assert len(result) == 3


def test_model_predictions_matches_test_length():
    df = _sample_df()
    X = df.drop(columns=["aqi"])
    y = df["aqi"]
    model = RandomForestClassifier(n_estimators=10, random_state=42)
    _, y_test, predictions = apply_model(model, X, y)
    assert len(predictions) == len(y_test)


def test_model_accuracy_valid_range():
    df = _sample_df()
    x = df.drop(columns=["aqi"])
    y = df["aqi"]
    model = RandomForestClassifier(n_estimators=10, random_state=42)
    _, y_test, predictions = apply_model(model, x, y)
    accuracy = accuracy_score(y_test, predictions)
    assert 0.0 <= accuracy <= 1.0