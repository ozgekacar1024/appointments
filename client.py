
{
    "admin": "ozge",
    "password": 123,
    
}
http = httpx.AsyncClient(base_url="http://127.0.0.1:8000")
class Client:
    async def post_json_data(self):
        url= "/process-json"
        
        try:
            response = await http.post(url, json=json_data)
            return response.json()
        except Exception as e :
            print(e)
        return {}
