#Youtube Notifier
    @tasks.loop(seconds=65)
    async def yt_notifier(self):
        chrome_options = Options()
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--disable-dev-shm-usage')

        driver = await webdriver.Chrome(options=chrome_options)

        driver.get("https://www.youtube.com/channel/UCri7Aft0jr2Jd0wIdTft84A") #Shion-Sama's YT
        await asyncio.sleep(2)

        html = await driver.page_source
        soup = await BeautifulSoup(html, 'html.parser')
        live = await soup.find("ytd-thumbnail-overlay-time-status-renderer", attrs={"class" : "style-scope ytd-thumbnail", "overlay-style" : "LIVE"})

        if live is not None:
            print("Shion is Live!!!")
            link = soup.find("a", href=True, attrs={"id" : "thumbnail"})
            stream_link = "https://www.youtube.com" + link["href"]
            msg = "@everyone" + " Shion-sama is now live! Come Watch! " + stream_link
            await driver.quit()
            await asyncio.sleep(43200) #Sleep for 12 hours
            
        else:
            print("Not live, big oof")
            await driver.quit()

    
    @yt_notifier.before_loop
    async def before_ytsend(self):
        await self.client.wait_until_ready()
        return