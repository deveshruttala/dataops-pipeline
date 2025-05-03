import pandas as pd
import numpy as np
import logging

def compute_metrics(df):
    logging.info("Computing agent performance metrics...")

    df['duration'] = pd.to_numeric(df['duration'], errors='coerce')
    df['completed'] = df['status'].str.lower().eq('completed').astype(int)
    df['loan_contact'] = df['installment_id'].notnull().astype(int)
    df['presence'] = (df['login_time'] != '').astype(int)

    summary = df.groupby(['call_date', 'agent_id', 'users_first_name', 'users_last_name'], dropna=False).agg(
        total_calls=('call_id', 'count'),
        unique_loans=('installment_id', pd.Series.nunique),
        completed_calls=('completed', 'sum'),
        avg_duration=('duration', lambda x: round(np.nanmean(x) / 60, 2)),
        presence=('presence', 'max')
    ).reset_index()

    summary['connect_rate'] = (summary['completed_calls'] / summary['total_calls']).round(2)

    logging.info("Metrics computed.")
    return summary
