def get_mps_and_keys2(api_url):
    response = requests.get(api_url) 
    response_json = response.json()
    mpd = response_json.get('mpd_url')
    keys = response_json.get('keys')
    return mpd, keys
    
def get_mps_and_keys3(api_url):
    response = requests.get(api_url)   
    response_json = response.json()
    mpd = response_json.get('url')
    return mpd