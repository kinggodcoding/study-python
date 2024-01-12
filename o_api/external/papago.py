# IdnQHHDEbNfO1iraY1Hj
# CKkplev9_8
# https://openapi.naver.com/v1/papago/n2mt
import urllib.request
import json

client_id = "IdnQHHDEbNfO1iraY1Hj"
client_secret = "CKkplev9_8"
encoding_text = urllib.parse.quote("보고싶어, 사랑해")
data = f"source=ko&target=en&text={encoding_text}"
url = "https://openapi.naver.com/v1/papago/n2mt"
request = urllib.request.Request(url)

# -H
request.add_header("X-Naver-Client-Id", client_id)
request.add_header("X-Naver-Client-Secret", client_secret)
response = urllib.request.urlopen(request, data=data.encode("utf-8"))
rescode = response.getcode()

if rescode == 200:
    response = json.loads(response.read().decode("utf-8"))
    print(response['message']['result']['translatedText'])