import time, os
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
# options.add_experimental_option('excludeSwitches', ['enable-logging'])
options.add_argument("--log-level=3")
options.add_argument("--user-data-dir=C:\\Users\\Administrator\\AppData\\Local\\Google\\Chrome Beta\\User Data")
options.binary_location = "C:\\Program Files\\Google\\Chrome Beta\\Application\\chrome.exe"


# print(
#     "\033[1;31;40m IMPORTANT: Put one or more videos in the *videos* folder in the bot directory. Please make sure to name the video files like this --> Ex: vid1.mp4 vid2.mp4 vid3.mp4 etc..")
# time.sleep(6)
# answer = input(
#     "\033[1;32;40m Press 1 if you want to spam same video or Press 2 if you want to upload multiple videos: ")
def upload_youtube():
    dir_path = '.\\videos'
    count = 0

    for path in os.listdir(dir_path):
        if os.path.isfile(os.path.join(dir_path, path)):
            count += 1
    print("   ", count, " Videos found in the videos folder, ready to upload...")
    time.sleep(1)
    i=0
    for i in range(count):
        try:
            bot = webdriver.Chrome(executable_path=ChromeDriverManager().install(), chrome_options=options)
            bot.get("https://studio.youtube.com")
            time.sleep(3)
            upload_button = bot.find_element(By.XPATH, '//*[@id="upload-icon"]')
            upload_button.click()
            time.sleep(5)

            file_input = bot.find_element(By.XPATH, '//*[@id="content"]/input')
            simp_path = 'videos/vid{}.mp4'.format(str(i + 1))
            abs_path = os.path.abspath(simp_path)

            file_input.send_keys(abs_path)

            time.sleep(7)

            next_button = bot.find_element(By.XPATH, '//*[@id="next-button"]')
            for i in range(3):
                next_button.click()
                time.sleep(5)

            done_button = bot.find_element(By.XPATH, '//*[@id="done-button"]')
            done_button.click()
            time.sleep(5)
            i+=1
            print("done : {}".format(i))
            bot.quit()
        except:
            bot.quit()
            continue


if __name__ == "__main__":
    upload_youtube()
