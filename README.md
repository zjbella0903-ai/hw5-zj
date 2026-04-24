# HW5 - Reusable AI Skill

## Skill overview
This project implements a reusable skill called `csv-audit`. It checks CSV files for missing values, duplicate rows, unnamed columns, and other simple structural problems, then produces a short quality report.

## Why I chose this skill
I chose this skill because CSV validation is a narrow and realistic task where a Python script is genuinely necessary. A language model can explain results, but it should not be trusted to count missing values, detect duplicates, or parse file structure reliably on its own.

## How to use it
Place the skill in the standard `.agents/skills/` folder structure. When the user asks to inspect or audit a CSV file, the agent can activate this skill and run the Python script on the provided file.

## What the script does
The script reads a CSV file with pandas and produces a JSON report containing:
- row count
- column count
- column names
- missing value counts
- duplicate row count
- notes about unnamed or empty columns
- error messages if the file cannot be read

## What worked well
The skill is easy to trigger because the name and description are specific. The script handles the deterministic part of the workflow well and gives structured output that the agent can summarize clearly.

## Limitations
This skill only supports CSV files, not Excel files or databases. It also checks structural quality only, not domain-specific correctness. A readable CSV may still contain semantic errors that this skill cannot detect.

## Demo video
[Paste your video link here]