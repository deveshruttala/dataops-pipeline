import argparse
from data_ingestion import read_and_validate
from data_merge import merge_data
from feature_engineering import compute_metrics
from reporting import save_report, generate_summary
from utils import setup_logging
import logging

def main(calls, agents, disposition):
    setup_logging()
    logging.info("Starting pipeline...")

    call_df, agent_df, dispo_df = read_and_validate(calls, agents, disposition)
    merged_df = merge_data(call_df, agent_df, dispo_df)
    summary_df = compute_metrics(merged_df)
    save_report(summary_df)

    summary_text = generate_summary(summary_df)
    print(summary_text)
    logging.info(f"\n{summary_text}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="DPDzero DataOps Pipeline")
    parser.add_argument("--calls", required=True, help="Path to call_logs.csv")
    parser.add_argument("--agents", required=True, help="Path to agent_roster.csv")
    parser.add_argument("--disposition", required=True, help="Path to disposition_summary.csv")
    args = parser.parse_args()

    main(args.calls, args.agents, args.disposition)
    logging.info("Pipeline completed successfully.")