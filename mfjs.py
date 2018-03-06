import requests
from bs4 import BeautifulSoup
from mail import my_mail


def jhw(url, origin_price):
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'lxml')
    item_title = soup.find('h2', id='item_title').get_text()
    try:
        rmb_price = soup.find_all('span', color='orange')[1].get_text()
        text = '商品名{}\n原价是{}\n现价是{}\n便宜了{}'.format(item_title, origin_price, rmb_price, origin_price - int(rmb_price))
        if origin_price > int(rmb_price):
            mail_fyx = my_mail(text, '1101022351@qq.com')
            mail_fyx.run()
            
    except Exception:
        # print(Exception)
        mail_fyx = my_mail('有错误了', '1101022351@qq.com')
        mail_fyx.run()




if __name__ == '__main__':
    # jhw('http://surugaya.masadora.net/product/detail/602002954001', 88)
    jhw('http://surugaya.masadora.net/product/detail/120045357001', 23)
