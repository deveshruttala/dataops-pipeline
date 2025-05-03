import pandas as pd
import logging

def merge_data(call_df, agent_df, dispo_df):
    logging.info("Merging datasets...")

    # Merge 1: Calls + Agent metadata
    merged = pd.merge(call_df, agent_df, on=['agent_id', 'org_id'], how='left', indicator=True)
    if (merged['_merge'] != 'both').any():
        mismatches = merged[merged['_merge'] != 'both']
        logging.warning(f"{len(mismatches)} call records did not match agent metadata.")
    merged.drop(columns=['_merge'], inplace=True)

    # Merge 2: Add disposition (login_time)
    merged = pd.merge(merged, dispo_df[['agent_id', 'org_id', 'call_date', 'login_time']],
                      on=['agent_id', 'org_id', 'call_date'], how='left', indicator=True)
    if (merged['_merge'] != 'both').any():
        logging.warning("Some call records have no matching login record.")
    merged.drop(columns=['_merge'], inplace=True)

    merged['login_time'] = merged['login_time'].fillna('')  # Presence field will use this

    return merged
