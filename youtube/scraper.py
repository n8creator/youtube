from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

###
# https://stackoverflow.com/questions/66902404/selenium-python-click-agree-to-youtube-cookie/
###

def bypass_consent(driver):
    try:
        consent = driver.find_element_by_css_selector(
                'button.VfPpkd-LgbsSe.VfPpkd-LgbsSe-OWXEXe-k8QpJ.VfPpkd-LgbsSe-OWXEXe-dgl2Hf.nCP5yc.AjY5Oe.DuMIQc.IIdkle')
        consent.click()
    except:
        try:
            consent = WebDriverWait(driver, 5).until(EC.element_to_be_clickable(
                (By.XPATH, "//input[@type='submit' and @value='I agree']")))
            consent.submit()
        except:
            pass


def parse_channel_id(url):
    options = Options()
    options.headless = False

    driver = webdriver.Firefox(options=options)
    driver.get(url)

    bypass_consent(driver=driver)

    channelId = driver.find_element_by_xpath("//meta[@itemprop='channelId']").get_attribute("content")

    driver.quit()

    return channelId


if __name__ == "__main__":
    print(parse_channel_id('https://www.youtube.com/channel/UCXYLIFmTDW94hu70G_dRkOQ'))
