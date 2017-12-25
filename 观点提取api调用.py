import requests
import json,re,time


def send_request(text,type):
    # Request
    # POST https://aip.baidubce.com/rpc/2.0/nlp/v2/comment_tag

    try:
        response = requests.post(
            url="https://aip.baidubce.com/rpc/2.0/nlp/v2/comment_tag",
            params={
                "access_token": "24.692a7079623b2ea4e1a6db9c99f85aaa.2592000.1516172362.282335-10525908",
            },
            headers={
                "Cookie": "BAIDUID=0F4BD41B1D4168198362C68C03F5B005:FG=1",
                "Content-Type": "application/json; charset=utf-8",
            },
            data=json.dumps({
                "type": type,
                "text": text
            })
        )
        # print('Response HTTP Status Code: {status_code}'.format(
        #     status_code=response.status_code))
        # print('Response HTTP Response Body: {content}'.format(
        #     content=response.text))
        # time.sleep(2)
        p = re.findall(r"<span>(.*?)</span>", response.text, re.M | re.I)
        if p:
            return p[0]
    except requests.exceptions.RequestException:
        print('HTTP Request failed')

with open(r'path','r',encoding='utf-8') as file:
    with open(r'path',"w",encoding="utf-8") as f:
        title = "ID"+"\t"+"客服"+"\t"+"sentence"+"\t"+"客服平均浓度"+"\t"+"客服情绪占比"+"\t"+"斜率"+"\t"+"平均应答时长"+"\t"+"分类"+"\t"+"观点"+"\n"
        f.write(title)
        next(file)
        for line in file.readlines():
            comment = line.split('\t')[2].strip().replace(r"\s+","")
            result = str(send_request(comment,12))
            sentence = line.strip("\n") + "\t" + result + "\n"
            f.write(sentence)