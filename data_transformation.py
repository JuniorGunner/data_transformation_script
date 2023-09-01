import pandas as pd
import os

def read_input_file(file_name: str) -> pd.DataFrame:
    """
    Read the Excel input file and return the dataframe.

    Parameters:
        - file_name (str): Name of the file to read.

    Returns:
        - pd.DataFrame: Dataframe containing the data.
    """
    file_path = os.path.join(os.getcwd(), "sample_input.xlsx")
    input_df = pd.read_excel(file_path, sheet_name="input_refresh_template", engine='openpyxl')
    return input_df


def transform_dataframe(input_df: pd.DataFrame) -> pd.DataFrame:
    """
    Transform the input dataframe to the desired format.

    Parameters:
        - input_df (pd.DataFrame): Dataframe to be transformed.

    Returns:
        - pd.DataFrame: Transformed dataframe.
    """
    input_df = input_df.dropna(how="all")
    dfs = [input_df.iloc[i:i+3] for i in range(0, len(input_df), 3)]

    result_df = pd.DataFrame()

    for df in dfs:
        site_id = df.iloc[2, 0]
        metric_names = df.iloc[0, 1:]
        dates = df.iloc[1, 1:]
        values = df.iloc[2, 1:]

        temp_df = pd.DataFrame({
            "Site ID": site_id,
            "Date": dates,
            "Metric": metric_names,
            "Value": values
        })

        temp_df = temp_df.pivot(index=["Date", "Site ID"], columns="Metric", values="Value").reset_index()
        result_df = pd.concat([result_df, temp_df], axis=0, ignore_index=True)

    result_df["Day of Month"] = pd.to_datetime(result_df["Date"]).dt.day
    result_df["Date"] = pd.to_datetime(result_df["Date"]).dt.strftime('%Y/%m/%d')
    result_df = result_df[['Day of Month', 'Date', 'Site ID', 'Page Views', 'Unique Visitors', 'Total Time Spent', 'Visits', 'Average Time Spent on Site']]
    
    return result_df

def save_to_excel(df: pd.DataFrame, output_name: str = "output.xlsx") -> None:
    """
    Save the dataframe to an Excel file.

    Parameters:
        - df (pd.DataFrame): Dataframe to be saved.
        - output_name (str): Name of the output file.

    Returns:
        - None
    """
    df.to_excel(output_name, index=False)


if __name__ == "__main__":
    df = read_input_file('input.xlsx')
    transformed_df = transform_dataframe(df)
    save_to_excel(transformed_df, "output.xlsx")
    print("Data transformation complete! Check output.xlsx for results.")
