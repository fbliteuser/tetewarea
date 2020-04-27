import requests
from time import sleep
from getpass import getpass
import json
import sys
import os
import random
from threading import*

print("selamat datang anak kutu")

token = ("fc94ec35873bdb1d59568aa52dd3682047eb1da6","162fecd3594e170adc386b386048d61a81a9e764","e75e7d563f34ffc473185bec48e4c89aad7087df","a7b8f4b11b1927d31cbaabdd9c745c1f28b4a82e","423b0c22d5f92274861219e3591a451336179ec9",
         "e1200bf36d891c1f043702782cd2139e6fbbbc4e","5ca1a785be8b11fd24a06787e25e0388fd353ac2","08a955e9ab994ffaf6711d137dd779ec617522b1","8a3b5f63d65b03947e45fd217e4fc66e81b4467f","d1170f0fd6790fe5f2e8af6cd9ab72f753d8a459",
         "b8a6212fe95846b933cd8690b1448f427bf118bb","bc3ffc31e12de15a01d58bc3923beebc5dae8233","32f1508d1b08895fa6ecabe75ff55cd47378e3b7","61b390848a8acf70cc229e697e7d814a46118933","4cd91a6717e61b423eae075d4e2f4f438328aced",
         "35e8de7f130bc4522b6519e8687152760884d91b","a57833be7477056489a0c91f5189f4bd73c7d366","024a0dfe51e037393cd619469520bbdf40f84664","2943c1c24c1b61fddefcc64bb7756363c39f7287","71eb2b3baf6bb0d6421bf5bf04555423476bcbfa",
         "6ad8d46baf56a081c26d036223f644ca8ad30f03","9029a01e18ccfbbf0bbd4a64ba389e5137b0e365","a0cf3ad6aed20cc7d2d0af01c25076797b32ab00","4079aecf971eae5d67013df8abbfe20cacfcd780","8324fbb2059cee9dc3cd872c69089e5c00fce790",
         "1f94e25172cb0a143d2f585c95173bbe278f2828","26048caef3ea1517461bc38b950afdd0b7331a38","4182ed7cacfa23c15a2bf7f71fb667f695e59d4a","4e45b13746b76bf6e685be18a516a1cb5908aca8","6f5c937ea00a15c09b69116fa2226bffb8977b88",
         "995fd9315166fa8ab5865a9759a0382a93caaabf","53fc1f8280c52625ffa28f5abe8a2de02c00076d","1a818d3ae41ed6c91b449508663adc0078cc6689","9763b454f13f4c8b87267b33c25d6263800dbb70","26f7f1872800a2713e1ee3cbd337c814b924863e",
         "0721c6865430d79665bd85879540fcdc348b1653","078c6be4dbc347848c77d3b3e45147f29a47376f","78ad456a7c8fae25ea2f217184f7935671635c67","9c41e63a7128e163c04146d55e52d90e7cc9f034","988f5b455f8be188c4d4aaa2e6d49c26e872957b",
         "4810f8864550f6739030b70d221f950841736e14","9629a70030e2ecaa6e395a91aa441928cc51c612","7e2b83c688a64c7a60382bf86e05590fb6855110","8d07cb51614eb9de293574e8cba6d5699cd578cb","ff47e02a6d6375dbfdb8a537bcb6391ab0b106c0",
         "55b9b1c5ef9ccdf61ca201283e6e9be761c818ea","9503d938b03c3a917ef1e2fb5028a0487c0a9301","8a9e58b1beeeaf4cace5febbd170a8fce64f01c3","672fee0dd5e466cac28a989ae74fd25e11fc1d97","f9f9a4e1f1cc0ddbdbf5420a9db34dd87826fb5e",
         "a85dc1110c3328ae09ec0a90bba93a9717079274","f9093145b6a5570e4d76462253407a788e374abe","0c3ab8826f0df8c1db278f40c8c1528b131a2d8e","7563b6b94594b2b968ff6685b255783fbe7a4d74","1f6a624951422331aec4daef9984b5a7fbeb69fc",
         "da9487532c6254068fe38569b1146973a1d18fd2","0712de5e4ac786f2e70b084a7468146b4ccb594f","4a6762017b506de03cc238f5342186e052fde831","c84bf6c1bcf02d0a7b4b66c22ee3b636df065da9","0e139e14409f9304532d3b70039643d5633112af",
         "5383910421d6acb74073c2e1c1268d493ebd32fd","8039f0720b2f2143b5e8795eb08109b6a53e94a8","2a8a9c17e5e57b850d4ec9544e3237db125935fd","5da29ca6a4a6e4e4d13ed2f7153bb88e0c52be1d","bd5a9dad69cb631897e1e70e82f10e65cd2c022f",
         "4fd6c99f4a45dae2093c6a462f2777cdb4d04349","566ea11fb3cc461bb2e800a46f3d7166f602e4ef","a8a7337a7e3272f792a6f39628c0894f5fe80e3a","ae91f424698cea50c4b24a7180e42c2d6cad8dc2","d79547ad28ab44d47980f7f96e7f93d977a42fa9",
         "ee45b257d11aec5aa71643ca1fa24f896c3e1bc9","60fa25b073cb1322c267767797630f81d0d6b2bf","934f7c3526fc82c3cb1b2be0ba6aedf103e5c655","bb3db17252f78203402d54fe1edbfa563c03f38e","a1b4af076c9e9631c22794d39ef5f132ef9dda65",
         "70c6e005c53d494a5db32e64ddfc38fa1707fb14","ffe0204196f6e1273b526ca20f4cabf61fcaa2a1","2e8e7e06543159238d25bfdfc7d52d59af4642f7","38fde145276330617bc9c4ae7118dc6d855ffb72","8ac3b010b76a7d30ea96d7cac7536217b5664c31",
         "3ff71f06ef314945932e753d4bb03f179a8ff444","b615dfc5907c990260148f9d634588f7aee63d97","5f3584952ab51227e3b2f7e3654760bb531ceeff","2af79345fd9c706755114d5bad901ca076b0f4d3","3cd9b4b37a97a2c9e835e0b35bf022de2fa49d2d",
         "3baa957116c3fa6c8afc81088c55626ce267cef2","aa2e9e7f093552c177fa78f807a58b90dcbfd8ae","fc5fcc2a4998766a88375cde8a6cb7180ec52bae","85950fb3ff5089dc824c300abb1f86625234db34","6b04fa11149aa3ec3fb119cd2a8ccfa85e096509",
         "0e108c3bf7fa36a4635bab32bc67ea8259240daf","50280944ed134bf33b34f3170f55c85469b4d9fc","7a236a298a090a4f4f86f184cbf10d736d1ebe4b","8eb0bb1d577ceb14f6dd3fd9b794f7509ecbf884","eb086ab728a1fc49f2d03978b4e879effd1ec6d0",
         "937df8a8b8647949901d7809e5b2729e12d817c3","feb031be63cb4a60f41a3c6d0bfc357fae079ec5","34598b9116073d2821465438162c5a5924b41912","6f99e44fe124813eb422125711c492273a0d756a","c209e53fe1532484da891a9c055af1d04413e3b7",
         "86f89c12b15b8e882a330968651f5959d5085dff","9d4ff89153887b46af55e7a997facd576e2e142f","465dfdb08b262571092347ef4ea814cf77d2c4f3","d215b0e776b1bca421ddfb7d36b078c89e46af33","463f0aed2c2956bb9dddaf7898f597b9442461e8",
         "7a8ed27bdcd98b0499a294f6dc0f7696e08e7b69","af93bf3eb83c13d0fe5ece14509dfbabc790c967","a5b84c5e8754475c78dcb78259d828e87d967198","b1b8727e0f14001556e346f2b465e7dbe7799c43","b37bd13ef814218cdf61cb13b1f18753e1a36b24",
         "be162af81a0b18905754408f8735aa07da784f63","6fc90c02524b142a75495ebbafa2375c5daa6889","0a9b78cea4b371156729ce581ae2587d2da10b28","1e5480266e7a0b0afad22b92a11a9745977c2b52","b8919a8823ef98409ab33910104f535f2a910c4f",
         "63390702ccb9f0f94136959bc29e2afb50b2ff37","cae41df9d0a6a74cdb895aa29d1c95ec24b692b5","64b0405383b6e4cd8d5c91024edd25082ccaabdf","6f739ce20b81ea25b82d4ea957a2c4999c56315d","56e28d14bd3b2bb9b10add7586d905740438a323",
         "62014015377110da5af4666949b35f241937033d",")
def mengetik(s):
  for c in s + '\n':
    sys.stdout.write(c)
    sys.stdout.flush()
    sleep(random.random() * 0.1)
sleep(0.1)
uning = '\33[1;33m'
biru = '\33[36;1m'
hijau = '\033[1;32m'
merah ='\33[31;1m'
putih = '\33[37;1m'
merah2 = '\33[6;31m'

sleep(1)
os.system('clear')
print(biru+'                     -[✓] GUNAKAN DENGAN BIJAK\n')
print(biru+'                     -[✓] DIBUAT OLEH RAFLI-GANTENG\n')
API_BASE_URL = "https://id-api.spooncast.net/lives/"
API_CMD = "/join/"
sleep(1)
txtid = input(putih+"COPAS LINK SAUDARA DISINI :")
response = requests.get(txtid)
url = response.url
slink = url[34:-59]
print('\nID LIVE : ' +slink)
os.system('clear')
UAInput = open('UALIST.txt','r').read().splitlines()

DBTEST = list(dict.fromkeys(token))


def botlike():
    class like1(Thread):
        def run(self):
            for i in range(0, 50):
                paramex = {'cv':'heimdallr'}
                headers = {'Authorization': 'Token ' + str(token[i]),
		'accept':'text/html,application/xhtml+xml,application/xml;q=0.9,application/json,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
		'accept-encoding':'gzip, deflate, br',
		'accept-language':'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',
		'origin':'https://www.spooncast.net',
		'referer':'https://www.spooncast.net/',
		'content-type':'application/json',
		'user-agent':str(UAInput[i])}
                with requests.Session() as c:
                        r = c.post(API_BASE_URL + slink + API_CMD, headers = headers,params=paramex)
                        r2 = c.post(API_BASE_URL + slink + '/like/', headers = headers,params=paramex)
                        print(i+1,'Server Status', r.status_code)
                        #sleep(time)



    class like2(Thread):
        def run(self):
            for i in range(50, 100):
                paramex = {'cv':'heimdallr'}
                headers = {'Authorization': 'Token ' + str(token[i]),
		'accept':'text/html,application/xhtml+xml,application/xml;q=0.9,application/json,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
		'accept-encoding':'gzip, deflate, br',
		'accept-language':'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',
		'origin':'https://www.spooncast.net',
		'referer':'https://www.spooncast.net/',
		'content-type':'application/json',
		'user-agent':str(UAInput[i])}
                with requests.Session() as c:
                        r = c.post(API_BASE_URL + slink + API_CMD, headers = headers,params=paramex)
                        r2 = c.post(API_BASE_URL + slink + '/like/', headers = headers,params=paramex)
                        print(i+1,'Server Status', r.status_code)
                        #sleep(time)

    class like3(Thread):
        def run(self):
            for i in range(100, 150):
                paramex = {'cv':'heimdallr'}
                headers = {'Authorization': 'Token ' + str(token[i]),
		'accept':'text/html,application/xhtml+xml,application/xml;q=0.9,application/json,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
		'accept-encoding':'gzip, deflate, br',
		'accept-language':'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',
		'origin':'https://www.spooncast.net',
		'referer':'https://www.spooncast.net/',
		'content-type':'application/json',
		'user-agent':str(UAInput[i])}
                with requests.Session() as c:
                        r = c.post(API_BASE_URL + slink + API_CMD, headers = headers,params=paramex)
                        r2 = c.post(API_BASE_URL + slink + '/like/', headers = headers,params=paramex)
                        print(i+1,'Server Status', r.status_code)
                        #sleep(time)

    class like4(Thread):
        def run(self):
            for i in range(150, 200):
                paramex = {'cv':'heimdallr'}
                headers = {'Authorization': 'Token ' + str(token[i]),
		'accept':'text/html,application/xhtml+xml,application/xml;q=0.9,application/json,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
		'accept-encoding':'gzip, deflate, br',
		'accept-language':'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',
		'origin':'https://www.spooncast.net',
		'referer':'https://www.spooncast.net/',
		'content-type':'application/json',
		'user-agent':str(UAInput[i])}
                with requests.Session() as c:
                        r = c.post(API_BASE_URL + slink + API_CMD, headers = headers,params=paramex)
                        r2 = c.post(API_BASE_URL + slink + '/like/', headers = headers,params=paramex)
                        print(hijau,i+1,'Server Status', r.status_code)
                        #sleep(time)

    class like5(Thread):
        def run(self):
            for i in range(200, 250):
                paramex = {'cv':'heimdallr'}
                headers = {'Authorization': 'Token ' + str(token[i]),
		'accept':'text/html,application/xhtml+xml,application/xml;q=0.9,application/json,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
		'accept-encoding':'gzip, deflate, br',
		'accept-language':'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',
		'origin':'https://www.spooncast.net',
		'referer':'https://www.spooncast.net/',
		'content-type':'application/json',
		'user-agent':str(UAInput[i])}
                with requests.Session() as c:
                        r = c.post(API_BASE_URL + slink + API_CMD, headers = headers,params=paramex)
                        r2 = c.post(API_BASE_URL + slink + '/like/', headers = headers,params=paramex)
                        print(i+1,'Server Status', r.status_code)
                        #sleep(time)

    class like6(Thread):
        def run(self):
            for i in range(250, 300):
                paramex = {'cv':'heimdallr'}
                headers = {'Authorization': 'Token ' + str(token[i]),
		'accept':'text/html,application/xhtml+xml,application/xml;q=0.9,application/json,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
		'accept-encoding':'gzip, deflate, br',
		'accept-language':'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',
		'origin':'https://www.spooncast.net',
		'referer':'https://www.spooncast.net/',
		'content-type':'application/json',
		'user-agent':str(UAInput[i])}
                with requests.Session() as c:
                        r = c.post(API_BASE_URL + slink + API_CMD, headers = headers,params=paramex)
                        r2 = c.post(API_BASE_URL + slink + '/like/', headers = headers,params=paramex)
                        print(i+1,'Server Status', r.status_code)
                        #sleep(time)

    class like7(Thread):
        def run(self):
            for i in range(300, 350):
                paramex = {'cv':'heimdallr'}
                headers = {'Authorization': 'Token ' + str(token[i]),
		'accept':'text/html,application/xhtml+xml,application/xml;q=0.9,application/json,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
		'accept-encoding':'gzip, deflate, br',
		'accept-language':'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',
		'origin':'https://www.spooncast.net',
		'referer':'https://www.spooncast.net/',
		'content-type':'application/json',
		'user-agent':str(UAInput[i])}
                with requests.Session() as c:
                        r = c.post(API_BASE_URL + slink + API_CMD, headers = headers,params=paramex)
                        r2 = c.post(API_BASE_URL + slink + '/like/', headers = headers,params=paramex)
                        print(i+1,'Server Status', r.status_code)
                        #sleep(time)

    class like8(Thread):
        def run(self):
            for i in range(350, 400):
                paramex = {'cv':'heimdallr'}
                headers = {'Authorization': 'Token ' + str(token[i]),
		'accept':'text/html,application/xhtml+xml,application/xml;q=0.9,application/json,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
		'accept-encoding':'gzip, deflate, br',
		'accept-language':'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',
		'origin':'https://www.spooncast.net',
		'referer':'https://www.spooncast.net/',
		'content-type':'application/json',
		'user-agent':str(UAInput[i])}
                with requests.Session() as c:
                        r = c.post(API_BASE_URL + slink + API_CMD, headers = headers,params=paramex)
                        r2 = c.post(API_BASE_URL + slink + '/like/', headers = headers,params=paramex)
                        print(i+1,'Server Status', r.status_code)
                        #sleep(time)

    class like9(Thread):
        def run(self):
            for i in range(400, 450):
                paramex = {'cv':'heimdallr'}
                headers = {'Authorization': 'Token ' + str(token[i]),
		'accept':'text/html,application/xhtml+xml,application/xml;q=0.9,application/json,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
		'accept-encoding':'gzip, deflate, br',
		'accept-language':'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',
		'origin':'https://www.spooncast.net',
		'referer':'https://www.spooncast.net/',
		'content-type':'application/json',
		'user-agent':str(UAInput[i])}
                with requests.Session() as c:
                        r = c.post(API_BASE_URL + slink + API_CMD, headers = headers,params=paramex)
                        r2 = c.post(API_BASE_URL + slink + '/like/', headers = headers,params=paramex)
                        print(i+1,'Server Status', r.status_code)
                        #sleep(time)

    class like10(Thread):
        def run(self):
            for i in range(450, 500):
                paramex = {'cv':'heimdallr'}
                headers = {'Authorization': 'Token ' + str(token[i]),
		'accept':'text/html,application/xhtml+xml,application/xml;q=0.9,application/json,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
		'accept-encoding':'gzip, deflate, br',
		'accept-language':'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',
		'origin':'https://www.spooncast.net',
		'referer':'https://www.spooncast.net/',
		'content-type':'application/json',
		'user-agent':str(UAInput[i])}
                with requests.Session() as c:
                        r = c.post(API_BASE_URL + slink + API_CMD, headers = headers,params=paramex)
                        r2 = c.post(API_BASE_URL + slink + '/like/', headers = headers,params=paramex)
                        print(merah,i+1,'Server Status', r.status_code)
                        #sleep(time)

    class like11(Thread):
        def run(self):
            for i in range(500, 550):
                paramex = {'cv':'heimdallr'}
                headers = {'Authorization': 'Token ' + str(token[i]),
		'accept':'text/html,application/xhtml+xml,application/xml;q=0.9,application/json,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
		'accept-encoding':'gzip, deflate, br',
		'accept-language':'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',
		'origin':'https://www.spooncast.net',
		'referer':'https://www.spooncast.net/',
		'content-type':'application/json',
		'user-agent':str(UAInput[i])}
                with requests.Session() as c:
                        r = c.post(API_BASE_URL + slink + API_CMD, headers = headers,params=paramex)
                        r2 = c.post(API_BASE_URL + slink + '/like/', headers = headers,params=paramex)
                        print(biru,i+1,'Server Status', r.status_code)
                        #sleep(time)
                        
    class like12(Thread):
        def run(self):
            for i in range(550, 600):
                paramex = {'cv':'heimdallr'}
                headers = {'Authorization': 'Token ' + str(token[i]),
		'accept':'text/html,application/xhtml+xml,application/xml;q=0.9,application/json,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
		'accept-encoding':'gzip, deflate, br',
		'accept-language':'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',
		'origin':'https://www.spooncast.net',
		'referer':'https://www.spooncast.net/',
		'content-type':'application/json',
		'user-agent':str(UAInput[i])}
                with requests.Session() as c:
                        r = c.post(API_BASE_URL + slink + API_CMD, headers = headers,params=paramex)
                        r2 = c.post(API_BASE_URL + slink + '/like/', headers = headers,params=paramex)
                        print(putih,i+1,'Server Status', r.status_code)
                        #sleep(time)

    class like13(Thread):
        def run(self):
            for i in range(600, 650):
                paramex = {'cv':'heimdallr'}
                headers = {'Authorization': 'Token ' + str(token[i]),
		'accept':'text/html,application/xhtml+xml,application/xml;q=0.9,application/json,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
		'accept-encoding':'gzip, deflate, br',
		'accept-language':'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',
		'origin':'https://www.spooncast.net',
		'referer':'https://www.spooncast.net/',
		'content-type':'application/json',
		'user-agent':str(UAInput[i])}
                with requests.Session() as c:
                        r = c.post(API_BASE_URL + slink + API_CMD, headers = headers,params=paramex)
                        r2 = c.post(API_BASE_URL + slink + '/like/', headers = headers,params=paramex)
                        print(hijau,i+1,'Server Status', r.status_code)
                        #sleep(time)
                        
    
    class like14(Thread):
        def run(self):
            for i in range(650, 700):
                paramex = {'cv':'heimdallr'}
                headers = {'Authorization': 'Token ' + str(token[i]),
		'accept':'text/html,application/xhtml+xml,application/xml;q=0.9,application/json,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
		'accept-encoding':'gzip, deflate, br',
		'accept-language':'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',
		'origin':'https://www.spooncast.net',
		'referer':'https://www.spooncast.net/',
		'content-type':'application/json',
		'user-agent':str(UAInput[i])}
                with requests.Session() as c:
                        r = c.post(API_BASE_URL + slink + API_CMD, headers = headers,params=paramex)
                        r2 = c.post(API_BASE_URL + slink + '/like/', headers = headers,params=paramex)
                        print(hijau,i+1,'Server Status', r.status_code)
                        #sleep(time)
                        
    
    class like15(Thread):
        def run(self):
            for i in range(700, 750):
                paramex = {'cv':'heimdallr'}
                headers = {'Authorization': 'Token ' + str(token[i]),
		'accept':'text/html,application/xhtml+xml,application/xml;q=0.9,application/json,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
		'accept-encoding':'gzip, deflate, br',
		'accept-language':'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',
		'origin':'https://www.spooncast.net',
		'referer':'https://www.spooncast.net/',
		'content-type':'application/json',
		'user-agent':str(UAInput[i])}
                with requests.Session() as c:
                        r = c.post(API_BASE_URL + slink + API_CMD, headers = headers,params=paramex)
                        r2 = c.post(API_BASE_URL + slink + '/like/', headers = headers,params=paramex)
                        print(hijau,i+1,'Server Status', r.status_code)
                        #sleep(time)
                        
                                                                                    
    class like16(Thread):
        def run(self):
            for i in range(750, 800):
                paramex = {'cv':'heimdallr'}
                headers = {'Authorization': 'Token ' + str(token[i]),
		'accept':'text/html,application/xhtml+xml,application/xml;q=0.9,application/json,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
		'accept-encoding':'gzip, deflate, br',
		'accept-language':'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',
		'origin':'https://www.spooncast.net',
		'referer':'https://www.spooncast.net/',
		'content-type':'application/json',
		'user-agent':str(UAInput[i])}
                with requests.Session() as c:
                        r = c.post(API_BASE_URL + slink + API_CMD, headers = headers,params=paramex)
                        r2 = c.post(API_BASE_URL + slink + '/like/', headers = headers,params=paramex)
                        print(hijau,i+1,'Server Status', r.status_code)
                        #sleep(time)
                        
                                                                                    
    class like17(Thread):
        def run(self):
            for i in range(800, 850):
                paramex = {'cv':'heimdallr'}
                headers = {'Authorization': 'Token ' + str(token[i]),
		'accept':'text/html,application/xhtml+xml,application/xml;q=0.9,application/json,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
		'accept-encoding':'gzip, deflate, br',
		'accept-language':'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',
		'origin':'https://www.spooncast.net',
		'referer':'https://www.spooncast.net/',
		'content-type':'application/json',
		'user-agent':str(UAInput[i])}
                with requests.Session() as c:
                        r = c.post(API_BASE_URL + slink + API_CMD, headers = headers,params=paramex)
                        r2 = c.post(API_BASE_URL + slink + '/like/', headers = headers,params=paramex)
                        print(hijau,i+1,'Server Status', r.status_code)
                        #sleep(time)
                        
                                                                                    
    class like18(Thread):
        def run(self):
            for i in range(850, 900):
                paramex = {'cv':'heimdallr'}
                headers = {'Authorization': 'Token ' + str(token[i]),
		'accept':'text/html,application/xhtml+xml,application/xml;q=0.9,application/json,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
		'accept-encoding':'gzip, deflate, br',
		'accept-language':'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',
		'origin':'https://www.spooncast.net',
		'referer':'https://www.spooncast.net/',
		'content-type':'application/json',
		'user-agent':str(UAInput[i])}
                with requests.Session() as c:
                        r = c.post(API_BASE_URL + slink + API_CMD, headers = headers,params=paramex)
                        r2 = c.post(API_BASE_URL + slink + '/like/', headers = headers,params=paramex)
                        print(hijau,i+1,'Server Status', r.status_code)
                        #sleep(time)
                        
                                                                                    
    class like19(Thread):
        def run(self):
            for i in range(900, 950):
                paramex = {'cv':'heimdallr'}
                headers = {'Authorization': 'Token ' + str(token[i]),
		'accept':'text/html,application/xhtml+xml,application/xml;q=0.9,application/json,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
		'accept-encoding':'gzip, deflate, br',
		'accept-language':'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',
		'origin':'https://www.spooncast.net',
		'referer':'https://www.spooncast.net/',
		'content-type':'application/json',
		'user-agent':str(UAInput[i])}
                with requests.Session() as c:
                        r = c.post(API_BASE_URL + slink + API_CMD, headers = headers,params=paramex)
                        r2 = c.post(API_BASE_URL + slink + '/like/', headers = headers,params=paramex)
                        print(hijau,i+1,'Server Status', r.status_code)
                        #sleep(time)
                                                     

    class like20(Thread):
        def run(self):      
            for i in range(950, 1000):
                paramex = {'cv':'heimdallr'}
                headers = {'Authorization': 'Token ' + str(token[i]),
		'accept':'text/html,application/xhtml+xml,application/xml;q=0.9,application/json,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
		'accept-encoding':'gzip, deflate, br',
		'accept-language':'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',
		'origin':'https://www.spooncast.net',
		'referer':'https://www.spooncast.net/',
		'content-type':'application/json',
		'user-agent':str(UAInput[i])}
                with requests.Session() as c:
                        r = c.post(API_BASE_URL + slink + API_CMD, headers = headers,params=paramex)
                        r2 = c.post(API_BASE_URL + slink + '/like/', headers = headers,params=paramex)
                        print(hijau,i+1,'Server Status', r.status_code)
                        #sleep(time)
                        
    class like21(Thread):
        def run(self):
            for i in range(200, 210):
                paramex = {'cv':'heimdallr'}
                headers = {'Authorization': 'Token ' + str(token[i]),
		'accept':'text/html,application/xhtml+xml,application/xml;q=0.9,application/json,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
		'accept-encoding':'gzip, deflate, br',
		'accept-language':'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',
		'origin':'https://www.spooncast.net',
		'referer':'https://www.spooncast.net/',
		'content-type':'application/json',
		'user-agent':str(UAInput[i])}
                with requests.Session() as c:
                        r = c.post(API_BASE_URL + slink + API_CMD, headers = headers,params=paramex)
                        r2 = c.post(API_BASE_URL + slink + '/like/', headers = headers,params=paramex)
                        print(hijau,i+1,'Server Status', r.status_code)
                        #sleep(time)
                        
    class like22(Thread):
        def run(self):
            for i in range(210, 220):
                paramex = {'cv':'heimdallr'}
                headers = {'Authorization': 'Token ' + str(token[i]),
		'accept':'text/html,application/xhtml+xml,application/xml;q=0.9,application/json,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
		'accept-encoding':'gzip, deflate, br',
		'accept-language':'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',
		'origin':'https://www.spooncast.net',
		'referer':'https://www.spooncast.net/',
		'content-type':'application/json',
		'user-agent':str(UAInput[i])}
                with requests.Session() as c:
                        r = c.post(API_BASE_URL + slink + API_CMD, headers = headers,params=paramex)
                        r2 = c.post(API_BASE_URL + slink + '/like/', headers = headers,params=paramex)
                        print(hijau,i+1,'Server Status', r.status_code)
                        #sleep(time)
                        
    class like23(Thread):
        def run(self):
            for i in range(220, 230):
                paramex = {'cv':'heimdallr'}
                headers = {'Authorization': 'Token ' + str(token[i]),
		'accept':'text/html,application/xhtml+xml,application/xml;q=0.9,application/json,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
		'accept-encoding':'gzip, deflate, br',
		'accept-language':'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',
		'origin':'https://www.spooncast.net',
		'referer':'https://www.spooncast.net/',
		'content-type':'application/json',
		'user-agent':str(UAInput[i])}
                with requests.Session() as c:
                        r = c.post(API_BASE_URL + slink + API_CMD, headers = headers,params=paramex)
                        r2 = c.post(API_BASE_URL + slink + '/like/', headers = headers,params=paramex)
                        print(hijau,i+1,'Server Status', r.status_code)
                        #sleep(time)
                        
    class like24(Thread):
        def run(self):
            for i in range(230, 240):
                paramex = {'cv':'heimdallr'}
                headers = {'Authorization': 'Token ' + str(token[i]),
		'accept':'text/html,application/xhtml+xml,application/xml;q=0.9,application/json,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
		'accept-encoding':'gzip, deflate, br',
		'accept-language':'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',
		'origin':'https://www.spooncast.net',
		'referer':'https://www.spooncast.net/',
		'content-type':'application/json',
		'user-agent':str(UAInput[i])}
                with requests.Session() as c:
                        r = c.post(API_BASE_URL + slink + API_CMD, headers = headers,params=paramex)
                        r2 = c.post(API_BASE_URL + slink + '/like/', headers = headers,params=paramex)
                        print(hijau,i+1,'Server Status', r.status_code)
                        #sleep(time)
                        
    class like25(Thread):
        def run(self):
            for i in range(240, 250):
                paramex = {'cv':'heimdallr'}
                headers = {'Authorization': 'Token ' + str(token[i]),
		'accept':'text/html,application/xhtml+xml,application/xml;q=0.9,application/json,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
		'accept-encoding':'gzip, deflate, br',
		'accept-language':'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',
		'origin':'https://www.spooncast.net',
		'referer':'https://www.spooncast.net/',
		'content-type':'application/json',
		'user-agent':str(UAInput[i])}
                with requests.Session() as c:
                        r = c.post(API_BASE_URL + slink + API_CMD, headers = headers,params=paramex)
                        r2 = c.post(API_BASE_URL + slink + '/like/', headers = headers,params=paramex)
                        print(hijau,i+1,'Server Status', r.status_code)
                        #sleep(time)
                        
    class like26(Thread):
        def run(self):
            for i in range(250, 260):
                paramex = {'cv':'heimdallr'}
                headers = {'Authorization': 'Token ' + str(token[i]),
		'accept':'text/html,application/xhtml+xml,application/xml;q=0.9,application/json,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
		'accept-encoding':'gzip, deflate, br',
		'accept-language':'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',
		'origin':'https://www.spooncast.net',
		'referer':'https://www.spooncast.net/',
		'content-type':'application/json',
		'user-agent':str(UAInput[i])}
                with requests.Session() as c:
                        r = c.post(API_BASE_URL + slink + API_CMD, headers = headers,params=paramex)
                        r2 = c.post(API_BASE_URL + slink + '/like/', headers = headers,params=paramex)
                        print(hijau,i+1,'Server Status', r.status_code)
                        #sleep(time)
                        
    class like27(Thread):
        def run(self):
            for i in range(260, 270):
                paramex = {'cv':'heimdallr'}
                headers = {'Authorization': 'Token ' + str(token[i]),
		'accept':'text/html,application/xhtml+xml,application/xml;q=0.9,application/json,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
		'accept-encoding':'gzip, deflate, br',
		'accept-language':'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',
		'origin':'https://www.spooncast.net',
		'referer':'https://www.spooncast.net/',
		'content-type':'application/json',
		'user-agent':str(UAInput[i])}
                with requests.Session() as c:
                        r = c.post(API_BASE_URL + slink + API_CMD, headers = headers,params=paramex)
                        r2 = c.post(API_BASE_URL + slink + '/like/', headers = headers,params=paramex)
                        print(hijau,i+1,'Server Status', r.status_code)
                        #sleep(time)
                        
    class like28(Thread):
        def run(self):
            for i in range(270, 280):
                paramex = {'cv':'heimdallr'}
                headers = {'Authorization': 'Token ' + str(token[i]),
		'accept':'text/html,application/xhtml+xml,application/xml;q=0.9,application/json,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
		'accept-encoding':'gzip, deflate, br',
		'accept-language':'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',
		'origin':'https://www.spooncast.net',
		'referer':'https://www.spooncast.net/',
		'content-type':'application/json',
		'user-agent':str(UAInput[i])}
                with requests.Session() as c:
                        r = c.post(API_BASE_URL + slink + API_CMD, headers = headers,params=paramex)
                        r2 = c.post(API_BASE_URL + slink + '/like/', headers = headers,params=paramex)
                        print(hijau,i+1,'Server Status', r.status_code)
                        #sleep(time)
                        
    class like29(Thread):
        def run(self):
            for i in range(280, 290):
                paramex = {'cv':'heimdallr'}
                headers = {'Authorization': 'Token ' + str(token[i]),
		'accept':'text/html,application/xhtml+xml,application/xml;q=0.9,application/json,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
		'accept-encoding':'gzip, deflate, br',
		'accept-language':'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',
		'origin':'https://www.spooncast.net',
		'referer':'https://www.spooncast.net/',
		'content-type':'application/json',
		'user-agent':str(UAInput[i])}
                with requests.Session() as c:
                        r = c.post(API_BASE_URL + slink + API_CMD, headers = headers,params=paramex)
                        r2 = c.post(API_BASE_URL + slink + '/like/', headers = headers,params=paramex)
                        print(hijau,i+1,'Server Status', r.status_code)
                        #sleep(time)
                        
    class like30(Thread):
        def run(self):
            for i in range(290, 300):
                paramex = {'cv':'heimdallr'}
                headers = {'Authorization': 'Token ' + str(token[i]),
		'accept':'text/html,application/xhtml+xml,application/xml;q=0.9,application/json,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
		'accept-encoding':'gzip, deflate, br',
		'accept-language':'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',
		'origin':'https://www.spooncast.net',
		'referer':'https://www.spooncast.net/',
		'content-type':'application/json',
		'user-agent':str(UAInput[i])}
                with requests.Session() as c:
                        r = c.post(API_BASE_URL + slink + API_CMD, headers = headers,params=paramex)
                        r2 = c.post(API_BASE_URL + slink + '/like/', headers = headers,params=paramex)
                        print(hijau,i+1,'Server Status', r.status_code)
                        #sleep(time)
                        
    class like31(Thread):
        def run(self):
            for i in range(300, 310):
                paramex = {'cv':'heimdallr'}
                headers = {'Authorization': 'Token ' + str(token[i]),
		'accept':'text/html,application/xhtml+xml,application/xml;q=0.9,application/json,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
		'accept-encoding':'gzip, deflate, br',
		'accept-language':'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',
		'origin':'https://www.spooncast.net',
		'referer':'https://www.spooncast.net/',
		'content-type':'application/json',
		'user-agent':str(UAInput[i])}
                with requests.Session() as c:
                        r = c.post(API_BASE_URL + slink + API_CMD, headers = headers,params=paramex)
                        r2 = c.post(API_BASE_URL + slink + '/like/', headers = headers,params=paramex)
                        print(hijau,i+1,'Server Status', r.status_code)
                        #sleep(time)
                        
    class like32(Thread):
        def run(self):
            for i in range(310, 320):
                paramex = {'cv':'heimdallr'}
                headers = {'Authorization': 'Token ' + str(token[i]),
		'accept':'text/html,application/xhtml+xml,application/xml;q=0.9,application/json,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
		'accept-encoding':'gzip, deflate, br',
		'accept-language':'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',
		'origin':'https://www.spooncast.net',
		'referer':'https://www.spooncast.net/',
		'content-type':'application/json',
		'user-agent':str(UAInput[i])}
                with requests.Session() as c:
                        r = c.post(API_BASE_URL + slink + API_CMD, headers = headers,params=paramex)
                        r2 = c.post(API_BASE_URL + slink + '/like/', headers = headers,params=paramex)
                        print(hijau,i+1,'Server Status', r.status_code)
                        #sleep(time)
                        
    class like33(Thread):
        def run(self):
            for i in range(320, 330):
                paramex = {'cv':'heimdallr'}
                headers = {'Authorization': 'Token ' + str(token[i]),
		'accept':'text/html,application/xhtml+xml,application/xml;q=0.9,application/json,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
		'accept-encoding':'gzip, deflate, br',
		'accept-language':'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',
		'origin':'https://www.spooncast.net',
		'referer':'https://www.spooncast.net/',
		'content-type':'application/json',
		'user-agent':str(UAInput[i])}
                with requests.Session() as c:
                        r = c.post(API_BASE_URL + slink + API_CMD, headers = headers,params=paramex)
                        r2 = c.post(API_BASE_URL + slink + '/like/', headers = headers,params=paramex)
                        print(hijau,i+1,'Server Status', r.status_code)
                        #sleep(time)
                        
    class like34(Thread):
        def run(self):
            for i in range(330, 340):
                paramex = {'cv':'heimdallr'}
                headers = {'Authorization': 'Token ' + str(token[i]),
		'accept':'text/html,application/xhtml+xml,application/xml;q=0.9,application/json,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
		'accept-encoding':'gzip, deflate, br',
		'accept-language':'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',
		'origin':'https://www.spooncast.net',
		'referer':'https://www.spooncast.net/',
		'content-type':'application/json',
		'user-agent':str(UAInput[i])}
                with requests.Session() as c:
                        r = c.post(API_BASE_URL + slink + API_CMD, headers = headers,params=paramex)
                        r2 = c.post(API_BASE_URL + slink + '/like/', headers = headers,params=paramex)
                        print(hijau,i+1,'Server Status', r.status_code)
                        #sleep(time)
                        
    class like35(Thread):
        def run(self):
            for i in range(340, 350):
                paramex = {'cv':'heimdallr'}
                headers = {'Authorization': 'Token ' + str(token[i]),
		'accept':'text/html,application/xhtml+xml,application/xml;q=0.9,application/json,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
		'accept-encoding':'gzip, deflate, br',
		'accept-language':'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',
		'origin':'https://www.spooncast.net',
		'referer':'https://www.spooncast.net/',
		'content-type':'application/json',
		'user-agent':str(UAInput[i])}
                with requests.Session() as c:
                        r = c.post(API_BASE_URL + slink + API_CMD, headers = headers,params=paramex)
                        r2 = c.post(API_BASE_URL + slink + '/like/', headers = headers,params=paramex)
                        print(hijau,i+1,'Server Status', r.status_code)
                        #sleep(time)
                        
    class like36(Thread):
        def run(self):
            for i in range(350, 360):
                paramex = {'cv':'heimdallr'}
                headers = {'Authorization': 'Token ' + str(token[i]),
		'accept':'text/html,application/xhtml+xml,application/xml;q=0.9,application/json,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
		'accept-encoding':'gzip, deflate, br',
		'accept-language':'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',
		'origin':'https://www.spooncast.net',
		'referer':'https://www.spooncast.net/',
		'content-type':'application/json',
		'user-agent':str(UAInput[i])}
                with requests.Session() as c:
                        r = c.post(API_BASE_URL + slink + API_CMD, headers = headers,params=paramex)
                        r2 = c.post(API_BASE_URL + slink + '/like/', headers = headers,params=paramex)
                        print(hijau,i+1,'Server Status', r.status_code)
                        #sleep(time)
                        
    class like37(Thread):
        def run(self):
            for i in range(360, 370):
                paramex = {'cv':'heimdallr'}
                headers = {'Authorization': 'Token ' + str(token[i]),
		'accept':'text/html,application/xhtml+xml,application/xml;q=0.9,application/json,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
		'accept-encoding':'gzip, deflate, br',
		'accept-language':'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',
		'origin':'https://www.spooncast.net',
		'referer':'https://www.spooncast.net/',
		'content-type':'application/json',
		'user-agent':str(UAInput[i])}
                with requests.Session() as c:
                        r = c.post(API_BASE_URL + slink + API_CMD, headers = headers,params=paramex)
                        r2 = c.post(API_BASE_URL + slink + '/like/', headers = headers,params=paramex)
                        print(hijau,i+1,'Server Status', r.status_code)
                        #sleep(time)
                        
    class like38(Thread):
        def run(self):
            for i in range(370, 380):
                paramex = {'cv':'heimdallr'}
                headers = {'Authorization': 'Token ' + str(token[i]),
		'accept':'text/html,application/xhtml+xml,application/xml;q=0.9,application/json,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
		'accept-encoding':'gzip, deflate, br',
		'accept-language':'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',
		'origin':'https://www.spooncast.net',
		'referer':'https://www.spooncast.net/',
		'content-type':'application/json',
		'user-agent':str(UAInput[i])}
                with requests.Session() as c:
                        r = c.post(API_BASE_URL + slink + API_CMD, headers = headers,params=paramex)
                        r2 = c.post(API_BASE_URL + slink + '/like/', headers = headers,params=paramex)
                        print(hijau,i+1,'Server Status', r.status_code)
                        #sleep(time)
                        
    class like39(Thread):
        def run(self):
            for i in range(380, 390):
                paramex = {'cv':'heimdallr'}
                headers = {'Authorization': 'Token ' + str(token[i]),
		'accept':'text/html,application/xhtml+xml,application/xml;q=0.9,application/json,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
		'accept-encoding':'gzip, deflate, br',
		'accept-language':'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',
		'origin':'https://www.spooncast.net',
		'referer':'https://www.spooncast.net/',
		'content-type':'application/json',
		'user-agent':str(UAInput[i])}
                with requests.Session() as c:
                        r = c.post(API_BASE_URL + slink + API_CMD, headers = headers,params=paramex)
                        r2 = c.post(API_BASE_URL + slink + '/like/', headers = headers,params=paramex)
                        print(hijau,i+1,'Server Status', r.status_code)
                        #sleep(time)
                        
    class like40(Thread):
        def run(self):
            for i in range(390, 400):
                paramex = {'cv':'heimdallr'}
                headers = {'Authorization': 'Token ' + str(token[i]),
		'accept':'text/html,application/xhtml+xml,application/xml;q=0.9,application/json,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
		'accept-encoding':'gzip, deflate, br',
		'accept-language':'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',
		'origin':'https://www.spooncast.net',
		'referer':'https://www.spooncast.net/',
		'content-type':'application/json',
		'user-agent':str(UAInput[i])}
                with requests.Session() as c:
                        r = c.post(API_BASE_URL + slink + API_CMD, headers = headers,params=paramex)
                        r2 = c.post(API_BASE_URL + slink + '/like/', headers = headers,params=paramex)
                        print(hijau,i+1,'Server Status', r.status_code)
                        #sleep(time)
                        
    class like41(Thread):
        def run(self):
            for i in range(400, 410):
                paramex = {'cv':'heimdallr'}
                headers = {'Authorization': 'Token ' + str(token[i]),
		'accept':'text/html,application/xhtml+xml,application/xml;q=0.9,application/json,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
		'accept-encoding':'gzip, deflate, br',
		'accept-language':'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',
		'origin':'https://www.spooncast.net',
		'referer':'https://www.spooncast.net/',
		'content-type':'application/json',
		'user-agent':str(UAInput[i])}
                with requests.Session() as c:
                        r = c.post(API_BASE_URL + slink + API_CMD, headers = headers,params=paramex)
                        r2 = c.post(API_BASE_URL + slink + '/like/', headers = headers,params=paramex)
                        print(hijau,i+1,'Server Status', r.status_code)
                        #sleep(time)
                        
    class like42(Thread):
        def run(self):
            for i in range(410, 420):
                paramex = {'cv':'heimdallr'}
                headers = {'Authorization': 'Token ' + str(token[i]),
		'accept':'text/html,application/xhtml+xml,application/xml;q=0.9,application/json,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
		'accept-encoding':'gzip, deflate, br',
		'accept-language':'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',
		'origin':'https://www.spooncast.net',
		'referer':'https://www.spooncast.net/',
		'content-type':'application/json',
		'user-agent':str(UAInput[i])}
                with requests.Session() as c:
                        r = c.post(API_BASE_URL + slink + API_CMD, headers = headers,params=paramex)
                        r2 = c.post(API_BASE_URL + slink + '/like/', headers = headers,params=paramex)
                        print(hijau,i+1,'Server Status', r.status_code)
                        #sleep(time)
                        
    class like43(Thread):
        def run(self):
            for i in range(420, 430):
                paramex = {'cv':'heimdallr'}
                headers = {'Authorization': 'Token ' + str(token[i]),
		'accept':'text/html,application/xhtml+xml,application/xml;q=0.9,application/json,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
		'accept-encoding':'gzip, deflate, br',
		'accept-language':'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',
		'origin':'https://www.spooncast.net',
		'referer':'https://www.spooncast.net/',
		'content-type':'application/json',
		'user-agent':str(UAInput[i])}
                with requests.Session() as c:
                        r = c.post(API_BASE_URL + slink + API_CMD, headers = headers,params=paramex)
                        r2 = c.post(API_BASE_URL + slink + '/like/', headers = headers,params=paramex)
                        print(hijau,i+1,'Server Status', r.status_code)
                        #sleep(time)
                        
    class like44(Thread):
        def run(self):
            for i in range(430, 440):
                paramex = {'cv':'heimdallr'}
                headers = {'Authorization': 'Token ' + str(token[i]),
		'accept':'text/html,application/xhtml+xml,application/xml;q=0.9,application/json,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
		'accept-encoding':'gzip, deflate, br',
		'accept-language':'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',
		'origin':'https://www.spooncast.net',
		'referer':'https://www.spooncast.net/',
		'content-type':'application/json',
		'user-agent':str(UAInput[i])}
                with requests.Session() as c:
                        r = c.post(API_BASE_URL + slink + API_CMD, headers = headers,params=paramex)
                        r2 = c.post(API_BASE_URL + slink + '/like/', headers = headers,params=paramex)
                        print(hijau,i+1,'Server Status', r.status_code)
                        #sleep(time)
                        
    class like45(Thread):
        def run(self):
            for i in range(440, 450):
                paramex = {'cv':'heimdallr'}
                headers = {'Authorization': 'Token ' + str(token[i]),
		'accept':'text/html,application/xhtml+xml,application/xml;q=0.9,application/json,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
		'accept-encoding':'gzip, deflate, br',
		'accept-language':'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',
		'origin':'https://www.spooncast.net',
		'referer':'https://www.spooncast.net/',
		'content-type':'application/json',
		'user-agent':str(UAInput[i])}
                with requests.Session() as c:
                        r = c.post(API_BASE_URL + slink + API_CMD, headers = headers,params=paramex)
                        r2 = c.post(API_BASE_URL + slink + '/like/', headers = headers,params=paramex)
                        print(hijau,i+1,'Server Status', r.status_code)
                        #sleep(time)
                        
    class like46(Thread):
        def run(self):
            for i in range(450, 460):
                paramex = {'cv':'heimdallr'}
                headers = {'Authorization': 'Token ' + str(token[i]),
		'accept':'text/html,application/xhtml+xml,application/xml;q=0.9,application/json,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
		'accept-encoding':'gzip, deflate, br',
		'accept-language':'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',
		'origin':'https://www.spooncast.net',
		'referer':'https://www.spooncast.net/',
		'content-type':'application/json',
		'user-agent':str(UAInput[i])}
                with requests.Session() as c:
                        r = c.post(API_BASE_URL + slink + API_CMD, headers = headers,params=paramex)
                        r2 = c.post(API_BASE_URL + slink + '/like/', headers = headers,params=paramex)
                        print(hijau,i+1,'Server Status', r.status_code)
                        #sleep(time)
                        
    class like47(Thread):
        def run(self):
            for i in range(460, 470):
                paramex = {'cv':'heimdallr'}
                headers = {'Authorization': 'Token ' + str(token[i]),
		'accept':'text/html,application/xhtml+xml,application/xml;q=0.9,application/json,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
		'accept-encoding':'gzip, deflate, br',
		'accept-language':'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',
		'origin':'https://www.spooncast.net',
		'referer':'https://www.spooncast.net/',
		'content-type':'application/json',
		'user-agent':str(UAInput[i])}
                with requests.Session() as c:
                        r = c.post(API_BASE_URL + slink + API_CMD, headers = headers,params=paramex)
                        r2 = c.post(API_BASE_URL + slink + '/like/', headers = headers,params=paramex)
                        print(hijau,i+1,'Server Status', r.status_code)
                        #sleep(time)
                        
    class like48(Thread):
        def run(self):
            for i in range(470, 480):
                paramex = {'cv':'heimdallr'}
                headers = {'Authorization': 'Token ' + str(token[i]),
		'accept':'text/html,application/xhtml+xml,application/xml;q=0.9,application/json,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
		'accept-encoding':'gzip, deflate, br',
		'accept-language':'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',
		'origin':'https://www.spooncast.net',
		'referer':'https://www.spooncast.net/',
		'content-type':'application/json',
		'user-agent':str(UAInput[i])}
                with requests.Session() as c:
                        r = c.post(API_BASE_URL + slink + API_CMD, headers = headers,params=paramex)
                        r2 = c.post(API_BASE_URL + slink + '/like/', headers = headers,params=paramex)
                        print(hijau,i+1,'Server Status', r.status_code)
                        #sleep(time)
                        
    class like49(Thread):
        def run(self):
            for i in range(480, 490):
                paramex = {'cv':'heimdallr'}
                headers = {'Authorization': 'Token ' + str(token[i]),
		'accept':'text/html,application/xhtml+xml,application/xml;q=0.9,application/json,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
		'accept-encoding':'gzip, deflate, br',
		'accept-language':'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',
		'origin':'https://www.spooncast.net',
		'referer':'https://www.spooncast.net/',
		'content-type':'application/json',
		'user-agent':str(UAInput[i])}
                with requests.Session() as c:
                        r = c.post(API_BASE_URL + slink + API_CMD, headers = headers,params=paramex)
                        r2 = c.post(API_BASE_URL + slink + '/like/', headers = headers,params=paramex)
                        print(hijau,i+1,'Server Status', r.status_code)
                        #sleep(time)
                        
    class like50(Thread):
        def run(self):
            for i in range(490, 500):
                paramex = {'cv':'heimdallr'}
                headers = {'Authorization': 'Token ' + str(token[i]),
		'accept':'text/html,application/xhtml+xml,application/xml;q=0.9,application/json,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
		'accept-encoding':'gzip, deflate, br',
		'accept-language':'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',
		'origin':'https://www.spooncast.net',
		'referer':'https://www.spooncast.net/',
		'content-type':'application/json',
		'user-agent':str(UAInput[i])}
                with requests.Session() as c:
                        r = c.post(API_BASE_URL + slink + API_CMD, headers = headers,params=paramex)
                        r2 = c.post(API_BASE_URL + slink + '/like/', headers = headers,params=paramex)
                        print(hijau,i+1,'Server Status', r.status_code)
                        #sleep(time)                                                       

    t1 = like1()
    t2 = like2()
    t3 = like3()
    t4 = like4()
    t5 = like5()
    t6 = like6()
    t7 = like7()
    t8 = like8()
    t9 = like9()
    t10 = like10()
    t11 = like11()
    t12 = like12()
    t13 = like13()
    t14 = like14()
    t15 = like15()
    t16 = like16()
    t17 = like17()
    t18 = like18()
    t19 = like19()
    t20 = like20()
    t21 = like21()
    t22 = like22()
    t23 = like23()
    t24 = like24()
    t25 = like25()
    t26 = like26()
    t27 = like27()
    t28 = like28()
    t29 = like29()
    t30 = like30()
    t31 = like31()
    t32 = like32()
    t33 = like33()
    t34 = like34()
    t35 = like35()
    t36 = like36()
    t37 = like37()
    t38 = like38()
    t39 = like39()
    t40 = like40()
    t41 = like41()
    t42 = like42()
    t43 = like43()
    t44 = like44()
    t45 = like45()
    t46 = like46()
    t47 = like47()
    t48 = like48()
    t49 = like49()
    t50 = like50()

    t1.start()
    t2.start()
    t3.start()
    t4.start()
    t5.start()
    t6.start()
    t7.start()
    t8.start()
    t9.start()
    t10.start()
    t11.start()
    t12.start()
    t13.start()
    t14.start()
    t15.start()
    t16.start()
    t17.start()
    t18.start()
    t19.start()
    t20.start()
    t21.start()
    t22.start()
    t23.start()
    t24.start()
    t25.start()
    t26.start()
    t27.start()
    t28.start()
    t29.start()
    t30.start()
    t31.start()
    t32.start()
    t33.start()
    t34.start()
    t35.start()
    t36.start()
    t37.start()
    t38.start()
    t39.start()
    t40.start()
    t41.start()
    t42.start()
    t43.start()
    t44.start()
    t45.start()
    t46.start()
    t47.start()
    t48.start()
    t49.start()
    t50.start()
    
    t1.like()
    t2.like()
    t3.like()
    t4.like()
    t5.like()
    t6.like()
    t7.like()
    t8.like()
    t9.like()
    t10.like()
    t11.like()
    t12.like()
    t13.like()
    t14.like()
    t15.like()
    t16.like()
    t17.like()
    t18.like()
    t19.like()
    t20.like()
    t21.like()
    t22.like()
    t23.like()
    t24.like()
    t25.like()
    t26.like()
    t27.like()
    t28.like()
    t29.like()
    t30.like()
    t31.like()
    t32.like()
    t33.like()
    t34.like()
    t35.like()
    t36.like()
    t37.like()
    t38.like()
    t39.like()
    t40.like()
    t41.like()
    t42.like()
    t43.like()
    t44.like()
    t45.like()
    t46.like()
    t47.like()
    t48.like()
    t49.like()
    t50.like()
    print("\n============== JOIN INFINITY ==============\n")
while True:
    botlike()
