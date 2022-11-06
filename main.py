import requests
from bs4 import BeautifulSoup as soup
from urllib.parse import urlencode

regId = "INPUT_REG_HERE"
regPost = "INPUT_POSTCODE_HERE"
eventId = "INPUT_EVENT_ID_HERE"
eventURL = "INPUT_EVENT_URL_HERE"

url = "https://glastonbury.seetickets.com/gfl/addregistrations"

headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
    'Connection': 'keep-alive',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Host': 'glastonbury.seetickets.com',
    'Origin': 'https://glastonbury.seetickets.com',
    'Referer': eventURL,
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36'
}

payload = {
    'GlastonburyEventId': f'DF-{eventId}',
    'registrations[0].RegistrationId': regId,
    'registrations[0].PostCode': regPost,
    'registrations[1].RegistrationId': '',
    'registrations[1].PostCode': '',
    'registrations[2].RegistrationId': '',
    'registrations[2].PostCode': '',
    'registrations[3].RegistrationId': '',
    'registrations[3].PostCode': '',
    'registrations[4].RegistrationId': '',
    'registrations[4].PostCode': '',
    'registrations[5].RegistrationId': '',
    'registrations[5].PostCode': ''
}

session = requests.Session()
payload = urlencode(payload)
ticketLoad = False
while ticketLoad == False:
    try:
        data = session.post(url, headers=headers, data=payload, timeout=5)
        htmlPage = soup(data.text, "lxml")
        if "You will be held at this page until there is a free space on the booking site" in str(htmlPage):
            print("You will be held at this page until there is a free space on the booking site")
            ticketLoad = False
        else:
            ticketLoad = True
    except Exception as e:
        print("Haven't carted")
print(data.url)
print(session.cookies.get_dict())
