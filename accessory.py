import requests

def get_pudgy_penguin_head_accessory(token_id, api_key):
    url = f"https://api.opensea.io/api/v2/metadata/ethereum//{token_id}"
    headers = {
        "X-API-KEY": api_key
    }
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        data = response.json()
        attributes = data.get('traits', [])
        
        for attribute in attributes:
            if attribute['trait_type'] == 'Head':
                return attribute['value']
        return "No Head Accessory found"
    elif response.status_code == 403:
        return "Error: Access forbidden. Check your API key and permissions."
    elif response.status_code == 404:
        return "Error: Resource not found. Check the token ID and contract address."
    else:
        return f"Error: {response.status_code}"

token_id = 3233
api_key = ""
head_accessory = get_pudgy_penguin_head_accessory(token_id, api_key)
print(f"Head Accessory of Pudgy Penguin #{token_id}: {head_accessory}")
