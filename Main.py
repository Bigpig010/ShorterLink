import requests
import json
import sys
import time

commandLineArgs = sys.argv

# if len(commandLineArgs) > 1:
#     url = commandLineArgs[1]
# else:
#     print('Please enter the URL you want to shorten as a command line argument')
#     sys.exit()
url= input('Input your URL: ')
print('Generating shortened URL...')

access_token= '536ebe65fe8234a12eebb5f3af7aa33ef7224427'
endpoint= 'https://api-ssl.bitly.com/v4/shorten'

headers = {
    'Authorization': f'Bearer {access_token}',
    'Content-Type': 'application/json',
} 

max_retries= 3
retry_count= 0

while retry_count < max_retries:
    data= {
        'long_url': url,
    }
    response= requests.post(endpoint, headers=headers, data= json.dumps(data))
    if response.status_code== 200:
        shortened_url= json.loads(response.content)['link']
        print(f'Shortened URL: {shortened_url}' )
        break
    else:
        retry_count += 1
        
        if retry_count < max_retries:
            time.sleep(5)
else:
    print('URL shortening was not successful')   
