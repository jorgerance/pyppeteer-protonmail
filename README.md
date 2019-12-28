# pyppeteer - Log in to Protonmail with 2fa


## Description

Using [pyppeteer](https://pypi.org/project/pyppeteer/), an uofficial Python port of [puppeteer](https://github.com/GoogleChrome/puppeteer) JavaScript (headless) chrome/chromium browser automation library, to log into [Protonmail](https://protonmail.com/)

---

## Requirements

### Packages

| Package   | Version | Description                                                                |
| --------- | ------- | -------------------------------------------------------------------------- |
| pyppeteer | 0.0.25  | Headless chrome/chromium automation library (unofficial port of puppeteer) |
| mintotp   | 0.2.0   | Minimal TOTP Generator                                                     |


### .secrets.cfg

Enter your login credentials in a **.secrets.cfg** file following an **.ini format**, which will be parsed by [configparser](https://pypi.org/project/configparser/), as in the example below:

```ini
[credentials]
username = user@protonmail.com
password = user_password
otp_seed = 1234567890QWERTYUIOPASDFGHJKLZXCV
```

## Running [main.py](main.py)

```shell
0 ✓ steve@hal9000 ~/repos/pyppeteer-protonmail $ ./main.py
 > Screenshot 1: ./screenshots/1-protonmail.png
 > OTP: 123456
 > Screenshot 2: ./screenshots/2-protonmail.png
 > Screenshot 3: ./screenshots/3-protonmail.png
 > Browser closed
0 ✓ steve@hal9000 ~/repos/pyppeteer-protonmail $
```

### Expected output files

```shell
0 ✓ steve@hal9000 ~/repos/pyppeteer-protonmail/screenshots $ ls -l
total 1234
-rw-r--r--  1 steve  bluejeans  123456 Jun 28 11:11 1-protonmail.png
-rw-r--r--  1 steve  bluejeans  123456 Jun 28 11:11 2-protonmail.png
-rw-r--r--  1 steve  bluejeans   12345 Jun 28 11:11 3-protonmail.png
0 ✓ steve@hal9000 ~/repos/pyppeteer-protonmail/screenshots $
```

#### Screenshot: 1-protonmail.png

![1-protonmail.png](/.github/1-protonmail.png)

#### Screenshot: 2-protonmail.png

![2-protonmail.png](/.github/2-protonmail.png)

#### Screenshot: 3-protonmail.png

![3-protonmail.png](/.github/3-protonmail.png)
