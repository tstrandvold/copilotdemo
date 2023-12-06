import datetime
import requests


def Import_FromRESTAPI_NOBB (apiname):

        Filename = 'F:\\NOBB\\' 
        if apiname == "items":
            NumberOfDaysBack = 4
            endDate = datetime.datetime.now() + datetime.timedelta(days= -1)
            startDate = endDate + datetime.timedelta(NumberOfDaysBack * -1)
            fromdate = startDate.strftime("%Y-%m-%d")
            todate = endDate.strftime("%Y-%m-%d")
            apiname = apiname + "?from={}&to={}".format(fromdate, todate)
            Filename = 'F:\\NOBB\\items\\' + apiname.replace("=","").replace("&","").replace("?","") + ".json"    
        else:
            Filename = 'F:\\NOBB\\' + apiname + "\\" + apiname + datetime.datetime.now().strftime("%Y-%m-%d") + ".json"    
        url = "https://export.byggtjeneste.no/api/v1/" + apiname
        print(url, flush=True)
        headers = {
            'Authorization': 'Basic c2thbnNrYV9hcGk6MTltMjA4Z2E='
            }
        payload = {}
        response = requests.request("GET", url, headers=headers, data=payload)
        
        
        # print (Filename, flush=True)
        with open(Filename, mode='w', encoding='UTF8') as localfile:
            localfile.write(response.text)
    

