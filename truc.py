import http.client

conn = http.client.HTTPSConnection("http-first-steps.challenges.pro.root-me.org")

headers = {
    "0": "pineapple",
    "1": "1",
    "2": "2",
    "3": "3",
    "4": "4",
    "5": "5",
    "6": "6",
    "7": "7",
    "8": "pizza"
}

conn.request("GET", "/", headers=headers)

response = conn.getresponse()
print(response.status, response.read().decode())
conn.close()
