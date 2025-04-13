import httpx
import lxml

from bs4 import BeautifulSoup

headers = {
    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36",
}


async def get_response(link: str):
    async with httpx.AsyncClient(follow_redirects=True) as htx_client:
        result: httpx.Response = await htx_client.get(link)

        return await result.aread()


async def get_text_horoscope(zodiac: str):
    link = f"https://horo.mail.ru/prediction/{zodiac}/today/"
    response_result = await get_response(link=link)

    soup = BeautifulSoup(markup=response_result, features="lxml")
    horoscope = [x.text for x in soup.select('main[itemprop="articleBody"] p')]

    return "\n\n".join(horoscope)


async def get_text_compatibility(first_sign: str, second_sign: str):
    link = f"https://1001goroskop.ru/sovmestimost/?wom={first_sign}&man={second_sign}"
    try:
        response_result = await get_response(link=link)

        soup = BeautifulSoup(markup=response_result, features="lxml")

        relationship_type = soup.select_one('#maincenter > div:nth-child(2) > h1:last-child').text.split(':')[1]
        love_compatibility = (
            soup.select_one('#maincenter > p.sovm_percent.otbivka').text.replace('% С', '%\nС'))
        description = soup.select_one('#maincenter > p:nth-child(4)').text

        return relationship_type, love_compatibility, description
    except:
        return 'Некорректные знаки зодиака!'

