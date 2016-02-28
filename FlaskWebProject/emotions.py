import httplib, urllib, base64, binascii, json, sys
#Get JSON of emotions
def getEmotions(image):
    headers = {
	    # Request headers
	    'Content-Type': 'application/octet-stream',
	    'Ocp-Apim-Subscription-Key': '9230cf9cbda44ab8a063f96855f3e4d4'
	}

#	try:
    conn = httplib.HTTPSConnection('api.projectoxford.ai')
    conn.request("POST", "/emotion/v1.0/recognize?", str(image), headers)
    response = conn.getresponse()
    data = response.read()
    conn.close()
    a = json.loads(data[1:-1])
    return a 
#	except Exception as e:
#	    print("[Errno {0}] {1}".format(e.errno, e.strerror))
#Get JSON of emotions
def getEmotions_fn(file_name):
	headers = {
	    # Request headers
	    'Content-Type': 'application/octet-stream',
	    'Ocp-Apim-Subscription-Key': '9230cf9cbda44ab8a063f96855f3e4d4'
	}

	file = open(file_name, "rb")
	body = file.read()
	file.close()

	try:
		conn = httplib.HTTPSConnection('api.projectoxford.ai')
		conn.request("POST", "/emotion/v1.0/recognize?", str(body), headers)
		response = conn.getresponse()
		data = response.read()
		conn.close()
		return json.loads(data)[0]
	except Exception as e:
	    print("[Errno {0}] {1}".format(e.errno, e.strerror))
