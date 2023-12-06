import pandas as pd
import io

def read_and_group_data_by_year(blob_service_client, container_name, blob_name, date_column):
    blob_client = blob_service_client.get_blob_client(container_name, blob_name)

    blob_data = blob_client.download_blob().readall()
    data = pd.read_csv(io.BytesIO(blob_data))

    data[date_column] = pd.to_datetime(data[date_column])
    data['Year'] = data[date_column].dt.year

    grouped_data = data.groupby('Year').sum()

    return grouped_data