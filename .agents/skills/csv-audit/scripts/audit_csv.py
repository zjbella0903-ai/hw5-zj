import sys
import json
import pandas as pd


def audit_csv(file_path: str):
    report = {
        "file_path": file_path,
        "status": "success",
        "rows": 0,
        "columns": 0,
        "column_names": [],
        "missing_values": {},
        "duplicate_rows": 0,
        "notes": []
    }

    try:
        df = pd.read_csv(file_path)
    except Exception as e:
        return {
            "file_path": file_path,
            "status": "error",
            "message": f"Could not read CSV file: {str(e)}"
        }

    report["rows"] = int(df.shape[0])
    report["columns"] = int(df.shape[1])
    report["column_names"] = [str(col) for col in df.columns]

    if df.empty:
        report["notes"].append("The CSV file contains no data rows.")

    if len(df.columns) == 0:
        report["notes"].append("The CSV file has no columns.")

    report["missing_values"] = {
        str(col): int(df[col].isna().sum()) for col in df.columns
    }

    report["duplicate_rows"] = int(df.duplicated().sum())

    unnamed_cols = [str(col) for col in df.columns if str(col).startswith("Unnamed")]
    if unnamed_cols:
        report["notes"].append(
            f"Found unnamed columns: {', '.join(unnamed_cols)}"
        )

    completely_empty_cols = [
        str(col) for col in df.columns if df[col].isna().all()
    ]
    if completely_empty_cols:
        report["notes"].append(
            f"Completely empty columns: {', '.join(completely_empty_cols)}"
        )

    return report


def main():
    if len(sys.argv) < 2:
        print(json.dumps({
            "status": "error",
            "message": "Usage: python audit_csv.py <csv_file_path>"
        }, indent=2))
        sys.exit(1)

    file_path = sys.argv[1]
    result = audit_csv(file_path)
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()