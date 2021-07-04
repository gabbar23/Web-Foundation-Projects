import requests
from bs4 import BeautifulSoup
import lxml
import smtplib
from dotenv import dotenv_values

config = dotenv_values(".env")

MY_EMAIL="
MY_PASSWORD=""
PRODUCT_LINK=""
HEADER=config["HEADERS"]

TARGET_PRICE=200.00

#getting_soup
response=requests.get(PRODUCT_LINK,headers=HEADER)
data=response.text
print(response)
soup=BeautifulSoup(data,"lxml")


#getting_price
price=soup.find(name="span",class_="a-size-medium a-color-price inlineBlock-display offer-price a-text-normal price3P")
price_=price.getText()
price = price_.replace('₹\xa0', '')
price = price.replace('.00', '')
price = float(price.replace(',', ''))
product_name=(soup.find(name="span",id="productTitle")).getText()


#comparing_price

if TARGET_PRICE<=price:
    connection = smtplib.SMTP("smtp.gmail.com")
    connection.starttls()
    connection.login(MY_EMAIL, MY_PASSWORD)
    connection.sendmail(
        from_addr=MY_EMAIL,
        to_addrs="",
        msg=f"Subject:Price Alert!\n\n {product_name} is availabe on your Target price i.e Rs.{price} on Amazon! "
        
    )
    