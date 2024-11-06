from eht.utils import ProxyInfo
import json
import eht

url = 'https://e-hentai.org/g/792200/75054c9c21/'
directoryName = '123'
r18g = 1

e = eht.ehentai(url, directoryName, r18g = r18g, proxyinfo = ProxyInfo)
e.download
