from config import token

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

url = "http://metroalmaty.kz/?q=ru/schedule-list"
a = requests.get(url)
soup = BeautifulSoup(a.text, "html.parser")
td = soup.find_all("td")
b = []
for t in td:
    b.append(t.text)


for c in range (len(b)):
    if c % 3 == 1:
        print (b[c], b[c + 1], b[c - 1])
