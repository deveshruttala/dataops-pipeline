import pandas as pd
import logging

def save_report(df, output_file="agent_performance_summary.csv"):
    df.to_csv(output_file, index=False)
    logging.info(f"Summary report saved to {output_file}")

def generate_summary(df):
    logging.info("Generating Slack-style summary...")

    if df.empty:
        logging.warning("Empty dataframe for summary.")
        return "No data available for summary."

    latest_date = df['call_date'].max()
    daily_df = df[df['call_date'] == latest_date]

    top_agent_row = daily_df.loc[daily_df['connect_rate'].idxmax()]
    top_agent_name = f"{top_agent_row['users_first_name']} {top_agent_row['users_last_name']}"
    top_connect_rate = int(top_agent_row['connect_rate'] * 100)

    total_agents = daily_df.shape[0]
    avg_duration = round(daily_df['avg_duration'].mean(), 2)

    summary = (
        f"Agent Summary for {latest_date.date()}\n"
        f"Top Performer: {top_agent_name} ({top_connect_rate}% connect rate)\n"
        f"Total Active Agents: {total_agents}\n"
        f"Average Duration: {avg_duration} min"
    )

    logging.info("Summary generated.")
    return summary
