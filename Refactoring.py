import datetime
import requests


def import_from_rest_api_nobb(apiname):
    filename = 'F:\\NOBB\\'
    
    if apiname == "items":
        number_of_days_back = 4
        end_date = datetime.datetime.now() + datetime.timedelta(days=-1)
        start_date = end_date + datetime.timedelta(number_of_days_back * -1)
        from_date = start_date.strftime("%Y-%m-%d")
        to_date = end_date.strftime("%Y-%m-%d")
        apiname = f"{apiname}?from={from_date}&to={to_date}"
        filename = f'F:\\NOBB\\items\\{apiname.replace("=", "").replace("&", "").replace("?", "")}.json'
    else:
        filename = f'F:\\NOBB\\{apiname}\\{apiname}{datetime.datetime.now().strftime("%Y-%m-%d")}.json'
    
    url = f"https://export.byggtjeneste.no/api/v1/{apiname}"
    print(url, flush=True)
    
    headers = {
        'Authorization': 'Basic c2thbnNrYV9hcGk6MTltMjA4Z2E='
    }
    
    payload = {}
    response = requests.request("GET", url, headers=headers, data=payload)
    
    with open(filename, mode='w', encoding='UTF8') as localfile:
        localfile.write(response.text)
