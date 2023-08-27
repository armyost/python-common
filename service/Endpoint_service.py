import requests

class EndpointService:
    def __init__(self, EndpointDao):
        self.EndpointDao = EndpointDao

    def endpointList(self):
        return self.EndpointDao.selectEndpointAll()

    def endpointInfoDetail(self, group_id, device_id):
        return self.EndpointDao.selectEndpointInfo(group_id, device_id)
        
    def endpointUrlFind(self, group_id):
        return self.EndpointDao.selectEndpointUrl(group_id)
    
    def endpointInfoApiDetail(self, endpoint_url):
        API_HOST = endpoint_url
        url = API_HOST+"/getInfo"
        method="GET"

        headers = {
            'Content-Type': 'application/json',
            'charset': 'UTF-8',
            'Accept': '*/*'
            } 
        try: 
            if method == 'GET': 
                responseJson = requests.get(url, headers=headers) 
            elif method == 'POST': 
                responseJson = requests.post(url, headers=headers) 
            print("response status %r" % responseJson.status_code) 
            print("response text %r" % responseJson.text) 
        except Exception as ex: 
            print(ex)
        return responseJson
    
    def endpointInfoModify(self, group_id, endpoint_response):
        return self.EndpointDao.updateEndpointLocation(group_id, endpoint_response)