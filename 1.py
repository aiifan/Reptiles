import requests
import json

class BaiduTranslate():

    HEADERS = {'user-agent' :'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36'}

    def baidu_translate_sug(self, obj):
        """
        英译中
        """
        __url = 'https://fanyi.baidu.com/sug'
        __data = {
            'kw' : obj
        }
        response = requests.post(__url, data=__data, headers=self.HEADERS)
        dict_obj = json.dumps(response.json(), ensure_ascii=False)
        with open(obj + '.json', 'w', encoding='utf8') as f:
            f.write(dict_obj)
        return 'ok'
if __name__ == "__main__":


    x = BaiduTranslate()
    x.baidu_translate_sug('你好')