
import time
from twilio.rest import Client

text = '123'

auth_token = 'afe22d6e3df30b1aafc916adfbfff402'  # 去twilio.com注册账户获取token
account_sid = 'AC678c3d3ee76c8eda204e6a8ced57b765'

client = Client(account_sid, auth_token)


def sent_message(phone_number):
    mes = client.messages.create(
        from_='+8613083315903',  # 填写在active number处获得的号码
        body=text,
        to=phone_number
    )
    print("OK")


while 1:
    sent_message("13083315903")
    time.sleep(3600 * 24)