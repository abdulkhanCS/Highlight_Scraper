#Importing Package
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from instabot import Bot
import praw
import json
import os
import glob
import time

client_id = "UeYjQwM9QtoBCg"
client_secret_key = "mncZbtXIqg8zv0n0y6pw2v_qVymO2A"

user_agent = "highlight_scraper"
username = "dIoading"
password = "khan0121"

chromedriver_path = "./chromedriver.exe"
chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("download.default_directory=C:/Users/akhan/Desktop")
driver = webdriver.Chrome(executable_path=chromedriver_path, options = chrome_options)

reddit = praw.Reddit(client_id = client_id, client_secret = client_secret_key, 
user_agent = user_agent, username = username, password = password)
subreddit = reddit.subreddit("nba")
hot_posts = subreddit.new(limit = 15)

bot = Bot()
bot.login(username="ballphase",password="khan01210")

for post in hot_posts:
    if(post.link_flair_text == "Highlight"):
        caption = post.title
        link = "https://streamabledl" + post.url[18:len(post.url)]
        driver.get(link)
        driver.implicitly_wait(10)
        download = driver.find_elements_by_xpath("//*[@id='root']/main/div/div/div[2]/div[2]/button")
        download[0].click()
        score = post.score
        time.sleep(5)
        latest_file = max(glob.iglob("C:/Users/akhan/Downloads/*mp4"),key=os.path.getctime)
        bot.upload_video(latest_file, caption=caption + "\n\n #basketball #bball #highlights")




driver.quit()
#To use methods of login and upload_photo of Bot
#bot = Bot()
#Login Using your instagram Credentials
#bot.login(username="ballphase",password="khan01210")

#Upload Photo to your accunt
#bot.upload_video("media/vid.mp4",caption="Caris Levert is back")