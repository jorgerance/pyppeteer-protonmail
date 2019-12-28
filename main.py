#!/usr/bin/env python3

import asyncio
import configparser
import random

import mintotp
from pyppeteer import launch

# protonmail login site url
url = 'https://mail.protonmail.com/login'

# parsing values from secrets.cfg file
config = configparser.ConfigParser()
config.read('.secrets.cfg')
username = config.get("credentials", "username")
password = config.get("credentials", "password")

# otp_seet = None if no value has been set on secrets.cfg
try:
    otp_seed = config.get("credentials", "otp_seed")
except Exception:
    otp_seed = None

# css selectors definition
username_selector = '#username'
password_selector = '#password'
otp_selector = '#twoFactorCode'
loginBtn_selector = '#login_btn'
loginBtn2fa_selector = '#login_btn_2fa'
firstMessage_selector = 'div.conversation:nth-child(1) > \
    div:nth-child(5) > h4:nth-child(1)'

# screenshot file name settings
screenshotName = 'protonmail'
screenshotPath = "./screenshots/"
screenshotFileName = None
screenshotCount = 1

# pyppeteer settings
windowWidth = 1768
windowHeigth = 1024
minClickTime = 700     # Min click delay (ms)
maxClickTime = 2000    # Max click delay (ms)


def randomNum(minTime, maxTime):
    clickDelayMs = random.randrange(minClickTime, maxClickTime, 1)
    return clickDelayMs


def takeScreenshot():
    global screenshotCount
    global screenshotFileName
    screenshotFileName = screenshotPath + str(screenshotCount) + \
        '-' + screenshotName + '.png'
    print(' > Screenshot ' + str(screenshotCount) +
          ': ' + screenshotFileName)
    screenshotCount = screenshotCount + 1
    return


async def main():
    browser = await launch(headless=True)
    page = await browser.newPage()
    await page.setViewport({'width': windowWidth, 'height': windowHeigth})
    await page.emulateMedia('screen')

    # Open login site
    await page.goto(url)
    takeScreenshot()
    await page.screenshot({'path': screenshotFileName,
                           'fullPage': False,
                           'webkit-print-color-adjust': True})

    # Enter username
    await page.click(username_selector,
                     delay=randomNum(minClickTime, maxClickTime))
    await page.keyboard.type(username)

    # Enter password
    await page.click(password_selector,
                     delay=randomNum(minClickTime, maxClickTime))
    await page.keyboard.type(password)

    # Click login button
    await page.click(loginBtn_selector,
                     delay=randomNum(minClickTime, maxClickTime))

    # Enters otp if opt_seed properly configured
    if otp_seed is not None:
        await page.waitForSelector(otp_selector)
        await page.click(otp_selector,
                         delay=randomNum(minClickTime, maxClickTime))

        currentOtp = mintotp.totp(otp_seed)
        await page.keyboard.type(currentOtp)
        print(" > OTP: " + currentOtp)
        takeScreenshot()
        await page.screenshot({'path': screenshotFileName,
                               'fullPage': False,
                               'webkit-print-color-adjust': True})
        await page.click(loginBtn2fa_selector,
                         delay=randomNum(minClickTime, maxClickTime))
    else:
        print(" > No otp_seed found")

    # Opening inbox
    await page.waitForSelector(firstMessage_selector)
    takeScreenshot()
    await page.screenshot({'path': screenshotFileName,
                           'fullPage': False,
                           'webkit-print-color-adjust': True})
    await browser.close()
    print(" > Browser closed")

asyncio.get_event_loop().run_until_complete(main())
