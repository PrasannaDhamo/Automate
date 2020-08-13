import requests
from bs4 import BeautifulSoup


def horoscope():
    print("Daily Horoscope. \n")
    print(
        "Enter your Zodiac sign number:\n",
        "1. Aries\n",
        "2. Taurus\n",
        "3. Gemini\n",
        "4. Cancer\n",
        "5. Leo\n",
        "6. Virgo\n",
        "7. Libra\n",
        "8. Scorpio\n",
        "9. Sagittarius\n",
        "10. Capricorn\n",
        "11. Aquarius\n",
        "12. Pisces\n",
    )
    zodiac_sign = int(input("Number> ").strip())
    print("choose some day:\n", "yesterday\n", "today\n", "tomorrow\n", "monthly\n", "weekly\n")
    day = input("enter the day> ")
    if day == ("today" or "yesterday" or "tomorrow"):
        day = "daily-" + day
        
    url = (
        "https://www.horoscope.com/us/horoscopes/general/"
        f"horoscope-general-{day}.aspx?sign={zodiac_sign}"
    )
    print(url)
    soup = BeautifulSoup(requests.get(url).content, "html.parser")
    print(soup.find("div", class_="main-horoscope").p.text)


if __name__ == "__main__":
    horoscope()
