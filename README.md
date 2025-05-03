# DPDzero DataOps Pipeline

## Project Overview

The DPDzero DataOps Pipeline is designed to handle daily call campaign data for loan collections. It reads, processes, merges, and generates performance metrics for agents based on call logs, agent rosters, and disposition summaries. The pipeline includes steps for data ingestion, validation, joining, feature engineering, and reporting. It is built to simulate a real-world data pipeline with a focus on improving loan collection processes through analysis of agent performance.


## Tech Stack

- **Python**: The primary language used for processing the data.
- **pandas**: For data manipulation and transformation.
- **argparse**: For accepting command-line arguments for file paths.
- **Logging**: For logging and debugging purposes throughout the pipeline.
- **CSV**: Used for input/output data files.

## Project Structure

```plaintext
dpdzero/
│
├── data/                    # Input CSV data files
│   ├── call_logs.csv        # Call log data
│   ├── agent_roster.csv     # Agent metadata
│   └── disposition_summary.csv # Disposition summary data
│
├── logs/                    # Log files for pipeline execution
│   └── pipeline.log         # Pipeline logs for debugging and tracking
│
├── src/                     # Source code
│   ├── main.py              # Main entry point for the pipeline
│   ├── data_ingestion.py    # Data ingestion and validation
│   ├── data_merge.py        # Data merging logic
│   ├── feature_engineering.py # Feature engineering to compute agent metrics
│   ├── reporting.py         # Report generation and summary creation
│   └── utils.py             # Utility functions like logging setup
│
├── agent_performance_summary.csv # Output report file
└── README.md                # Project documentation
```

## Inputs and Outputs

### Input Files

The pipeline expects the following CSV files as input:

1. **call_logs.csv**:
   - **Columns**: `call_id`, `agent_id`, `org_id`, `installment_id`, `status`, `duration`, `created_ts`, `call_date`
   - Represents a log of each call attempt, including the status and duration.

2. **agent_roster.csv**:
   - **Columns**: `agent_id`, `users_first_name`, `users_last_name`, `users_office_location`, `org_id`
   - Contains metadata for agents, such as their ID, name, and office location.

3. **disposition_summary.csv**:
   - **Columns**: `agent_id`, `org_id`, `call_date`, `login_time`
   - Provides information on when agents logged in, which helps calculate their presence.

### Output Files

1. **agent_performance_summary.csv**:
   - The main output of the pipeline containing agent performance metrics.
   - **Columns**: `agent_id`, `call_date`, `total_calls`, `unique_loans_contacted`, `connect_rate`, `avg_duration`, `presence`

2. **Slack-style Summary**:
   - A textual summary displayed in the console, showing the top performer, active agents, and average call duration for the latest date.

---

## How to Run

### Prerequisites

- Python 3.x installed
- Required Python packages:
  - `pandas`
  - `argparse`

### Steps to Run

1. **Install dependencies**:

   Run the following command to install the necessary dependencies:

   ```bash
   pip install pandas argparse
   ```

2. **Place the CSV files**:

Ensure the call_logs.csv, agent_roster.csv, and disposition_summary.csv files are placed in the data/ directory

3. **Run the Pipeline**:

   Execute the following command to run the pipeline:

   ```bash
   python src/main.py --calls data/call_logs.csv --agents data/agent_roster.csv --disposition data/disposition_summary.csv

   ```

4. **Check the outputs**:

After successful execution:
- A report `agent_performance_summary.csv` will be saved in the `output/` folder.
- A Slack-style summary will be displayed in the terminal.
- Logs will be available in `logs/pipeline.log`.


---

##  Real-Life Use Case

This project replicates a real-world scenario for a **loan collection campaign** where agents make outbound calls to borrowers. By analyzing the call logs and login data, the organization can measure:

- Agent productivity
- Call success rates
- Contact effectiveness
- Agent availability

###  Key Performance Indicators

- **Connect Rate**: Successful call percentage.
- **Average Call Duration**: Time spent per successful call.
- **Presence**: Whether the agent was logged in (available for work).

These insights enable:
- Improved agent training
- Efficient workload allocation
- Better business decision-making

---

##  Features

###  Data Ingestion & Validation

- Reads input from structured CSVs
- Checks for:
  - Required columns
  - Missing values
  - Duplicates
- Logs warnings and errors

###  Data Merging

- Joins all datasets by `agent_id`, `org_id`, and `call_date`
- Logs any mismatched entries or missing values

###  Feature Engineering

For each agent and date, the pipeline computes:
- Total number of calls made
- Unique loans contacted
- Connect rate (successful calls / total calls)
- Average duration of completed calls
- Presence (based on login time)

###  Reporting

- Generates a CSV with all metrics per agent per day
- Displays a human-readable summary in Slack-style format

###  Logging

- Logs pipeline steps and issues to `logs/pipeline.log`
- Captures:
  - Info messages for progress
  - Warnings for anomalies
  - Errors for fatal issues

---

##  Logs

Pipeline execution is logged in `logs/pipeline.log`. Includes:

- Info logs: Indicate normal operations (file read, merge success, etc.)
- Warnings: Highlight issues like missing or null data
- Errors: Report problems that prevent execution

---

##  Error Handling

- Performs strict validation on required columns
- Logs issues like:
  - Missing fields
  - Null values
  - Data mismatches
- Stops execution with clear error messages for fatal issues

---

##  Further Improvements

- Add more CLI options (e.g., filter by date range)
- Connect to databases instead of static CSVs
- Add unit tests for better maintainability
- Integrate Slack for real-time alerts and reporting
- Optimize for larger datasets using parallel processing

---


## Output ScreenShots

* Output File 

CSV file (agent_performance_summary.csv) having all the agent metrics

![agent_performance_summary](code_screenshots/csv%20output.png)


* Console Metrics Output

Displays agent metrics right within the console

![Console Metrics Output](code_screenshots/console%20output.png)



* Pipeline Logging Data

Displays a time series logging infortion with appropriate error highlights

![Pipeline Logging Data](code_screenshots/pipeline%20log.png)



---


##  Conclusion

This pipeline serves as a complete DataOps solution to automate the ingestion, validation, analysis, and reporting of agent performance in a call center environment. It helps organizations streamline their analytics, uncover agent performance patterns, and act quickly based on data insights.

It is extensible, robust, and suitable for real-time deployment in business environments requiring high accountability and performance tracking of human agents.

---

### Author and Developer
#### Devesh
