---
name: csv-audit
description: Validates CSV files, identifies missing values, duplicate rows, and basic schema problems, and produces a short quality report. Use when the user asks to inspect, clean, or audit tabular CSV data.
---

# CSV Audit

## When to use this skill
Use this skill when the user provides a CSV file or asks to inspect, validate, clean, or audit tabular CSV data. This skill is especially useful when the task requires deterministic checks such as counting missing values, detecting duplicate rows, reviewing column names, and identifying simple schema problems.

## When not to use this skill
Do not use this skill for general writing tasks, spreadsheet visualization, Excel-only workflows, or advanced statistical analysis. Do not use it when the user wants speculative interpretation instead of concrete file validation. If the file is not CSV, explain the limitation instead of forcing the workflow.

## Expected inputs
- A CSV file path
- Optional user request about what to inspect, such as missing values, duplicates, or schema consistency

## Step-by-step instructions
1. Confirm that the input is a CSV file.
2. Run the Python audit script on the file.
3. Read the script output carefully.
4. Summarize the results for the user in plain language.
5. Highlight the most important issues first, such as empty columns, many missing values, duplicate rows, or malformed structure.
6. If the file cannot be read, explain the error clearly and avoid guessing.
7. If the user asks for cleaning or fixes, only suggest safe next steps unless explicitly asked to transform the file.

## Expected output format
Provide a short quality report that includes:
- total rows
- total columns
- column names
- missing value counts by column
- duplicate row count
- any detected structural or parsing issues
- a brief conclusion about whether the CSV looks usable

## Important limitations and checks
- This skill only supports CSV input.
- This skill performs deterministic checks, not domain-specific interpretation.
- A readable CSV can still contain semantic problems the script cannot detect.
- If the CSV is empty, malformed, or uses an unexpected delimiter, report that limitation clearly.