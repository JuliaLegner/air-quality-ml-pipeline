import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
REPORTS_DIR = os.path.join(BASE_DIR, "reports")


def save_results(results):
    os.makedirs(REPORTS_DIR, exist_ok=True)

    report_path = os.path.join(REPORTS_DIR, "results_summary.txt")

    with open(report_path, "w", encoding="utf-8") as file:
        file.write("Air Quality Classifier Results\n")
        file.write("=" * 40 + "\n")

        for name, accuracy in results.items():
            file.write(f"{name}: {accuracy * 100:.2f}%\n")

        best_model = max(results, key=results.get)
        file.write("\nBest model:\n")
        file.write(f"{best_model}: {results[best_model] * 100:.2f}%\n")

        print("\nBest model")
        print(f"{best_model}: {results[best_model] * 100:.2f}%")

    print(f"Results saved to {report_path}")
