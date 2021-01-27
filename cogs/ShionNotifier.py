from discord.ext import commands, tasks
import discord
from replit import db
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import asyncio
from asgiref.sync import sync_to_async


class ShionNotifier(commands.Cog):
    def __init__(self, client):
        self.client = client
        self.twitter_notifier.start()
        self.yt_notifier.start()

    #Twitter Notifier
    @tasks.loop(seconds=10)
    async def twitter_notifier(self):
        if db['receive_webhook'] != db['prev_webhook']:
            data = db['receive_webhook']

            notifChannel = self.client.get_channel(802466656605306921) #NanodaBot Notif Channel
            await notifChannel.send(data["content"])
            db['prev_webhook'] = db['receive_webhook']

    @twitter_notifier.before_loop
    async def before_twitsend(self):
        await self.client.wait_until_ready()
        return
    
    #Youtube Notifier
    @tasks.loop(seconds=65)
    async def yt_notifier(self):
        print("yt execute")
        soup = await sync_to_async(get_soup)()

        live = soup.find("ytd-thumbnail-overlay-time-status-renderer", attrs={"class" : "style-scope ytd-thumbnail", "overlay-style" : "LIVE"})
        print("soup done")
        if live is not None:
            print("Shion is Live!!!")
            link = soup.find("a", href=True, attrs={"id" : "thumbnail"})
            stream_link = "https://www.youtube.com" + link["href"]
            msg = "@everyone" + " Shion-sama is now live! Come Watch! " + stream_link
            notifChannel = self.client.get_channel(799237354828726313) #NanodaBot Notif Channel

            await notifChannel.send(msg)
            await asyncio.sleep(43200) #Sleep for 12 hours
            
        else:
            print("Not live, big oof")
    
    @yt_notifier.before_loop
    async def before_ytsend(self):
        await self.client.wait_until_ready()
        return
    
def get_soup():
        print("get soup run")
        chrome_options = Options()
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--disable-dev-shm-usage')

        
        driver = webdriver.Chrome(options=chrome_options)
        print("driver run")
        
        driver.get("https://www.youtube.com/channel/UCri7Aft0jr2Jd0wIdTft84A") #Shion-Sama's YT
        print("driver executed")
        asyncio.sleep(3)

        html = driver.page_source
        data = BeautifulSoup(html, 'html.parser')
        print("soup retrieved")
        driver.quit()

        return data

def setup(client):
    client.add_cog(ShionNotifier(client))
