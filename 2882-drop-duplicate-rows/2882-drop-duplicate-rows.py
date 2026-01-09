import pandas as pd

def dropDuplicateEmails(customers: pd.DataFrame) -> pd.DataFrame:
    dropDuplicate = customers.drop_duplicates(subset=['email'])
    return dropDuplicate