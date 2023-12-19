# lag en csv fil som ineholder adresse og postnummer, gjerne 3-4 rader
# les inn csv filen
# for hver adresse i csv filen
#    kall geonorge api
#    hent ut koordinater
#    skriv koordinater til csv fil
# last opp csv fil til blob storage


connection_string = "DefaultEndpointsProtocol=https;AccountName=clausedemo;AccountKey=ooQFU1aU2ymE7rq2HsZ23LxpmBw6dKCiTJI2/gEwHHOt6n1xXjcVXuNgnGwQI8m3pouJfOS3fXZ+AStjK7UQA==;EndpointSuffix=core.windows.net"
 


        ADRESSE = row["ADRESSE"]
        POSTNUMMER = row["POSTNUMMER"]
        headers = {
        'accept': 'application/json'
        }
        params=[('adressetekst',ADRESSE), ('postnummer',POSTNUMMER), ('side','0'), ('sokemodus','AND'), ('treffPerSide','1')]
        url = "https://ws.geonorge.no/adresser/v1/sok"
        response = requests.request("GET", url, params=params, headers=headers)
        # print(response.text)
        data = json.loads(response.text)
