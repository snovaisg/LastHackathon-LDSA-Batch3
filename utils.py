import pandas as pd

def save_predictions(predictions: pd.DataFrame, output_path: str):
    """Save predictions to csv.
    Saves the predictions into a csv file with the format we need.
    We keep the index since it contains the user ids.
    Args:
        predictions (pd.DataFrame): DataFrame with user_id as index and ordered recommendations in the columns.
        output_path (str): Filepath for the predictions file.
    """
    
    predictions = predictions.copy()
    cols_to_drop = predictions.columns
    predictions['purchases'] = predictions.apply(lambda row: str([ str(row[column]) for column in predictions.columns]), axis=1)
    predictions = predictions.drop(columns=cols_to_drop)
    predictions.to_csv(output_path,index_label='user_id')
    print(f"Saved to csv in '{output_path}'.")