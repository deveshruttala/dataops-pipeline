import pandas as pd
import logging

def read_and_validate(call_file, agent_file, dispo_file):
    logging.info("Reading input files...")

    call_df = pd.read_csv(call_file)
    agent_df = pd.read_csv(agent_file)
    dispo_df = pd.read_csv(dispo_file)

    # Required columns by file
    required_columns = {
        'Calls': ['call_date', 'agent_id', 'org_id'],
        'Agents': ['agent_id', 'org_id'],
        'Disposition': ['call_date', 'agent_id', 'org_id']
    }

    # Column presence check
    for df_name, df, cols in [('Calls', call_df, required_columns['Calls']),
                              ('Agents', agent_df, required_columns['Agents']),
                              ('Disposition', dispo_df, required_columns['Disposition'])]:
        for col in cols:
            if col not in df.columns:
                logging.error(f"Missing column '{col}' in {df_name} data.")
                raise ValueError(f"{df_name} file must contain '{col}' column.")

    # Convert call_date to datetime where applicable
    for df_name, df in [('Calls', call_df), ('Disposition', dispo_df)]:
        try:
            df['call_date'] = pd.to_datetime(df['call_date'], errors='coerce')
        except Exception as e:
            logging.error(f"Error converting call_date in {df_name}: {e}")
            raise

    # Check for missing values
    for name, df in [('Calls', call_df), ('Agents', agent_df), ('Disposition', dispo_df)]:
        null_counts = df.isnull().sum()
        if null_counts.any():
            logging.warning(f"{name} data has missing values:\n{null_counts[null_counts > 0]}")

    # Check for duplicates
    for name, df in [('Calls', call_df), ('Agents', agent_df), ('Disposition', dispo_df)]:
        dup_count = df.duplicated().sum()
        if dup_count:
            logging.warning(f"{name} data has {dup_count} duplicate rows.")

    return call_df, agent_df, dispo_df
