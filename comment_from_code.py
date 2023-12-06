import requests

def trigger_refresh(dataset_id, access_token):

    refresh_url = f"https://api.powerbi.com/v1.0/myorg/datasets/{dataset_id}/refreshes"
    headers = {
        "Authorization": f"Bearer {access_token}",
        "Content-Type": "application/json"
    }
    response = requests.post(refresh_url, headers=headers)
    
    if response.status_code == 202:
        print("Dataset refresh triggered successfully.")
    else:
        print("Failed to trigger dataset refresh.")


dataset_id = "your_dataset_id"
access_token = "your_access_token"
trigger_refresh(dataset_id, access_token)


