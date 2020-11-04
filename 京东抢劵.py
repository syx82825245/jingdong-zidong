import requests
import time
import json

# 1. 请求网页
def geturl():
    url = 'https://api.m.jd.com/client.action?functionId=newBabelAwardCollection'
    headers = {
        'cookie': '__jdc=122270672; __jdv=122270672|direct|-|none|-|1602568778510; __jdu=1602568778508762049783; shshshfp=ba65f1396e9580b154a1bba824f3e9e3; shshshfpa=45aa1bb0-e1f9-8fde-b46f-18a73212c1a6-1602568779; shshshfpb=nowgnMappyHef4oOBwTKicg%3D%3D; areaId=18; ipLoc-djd=18-1544-29465-0; 3AB9D23F7A4B3C9B=YG6ZLMD633GAW35XHLWIK7MD5BI3IPH3KP56I6FTW4BMD7X3AC4VPPHRALPJ5NNWXRE2HNAQX6HHE2QJ72HCASHGUU; wlfstk_smdl=yxhbflmsa6gbw2n8kewyss0viulveclc; TrackID=1zieHVwEF2l9m3TBqyq18tRHs_v7lkL3OoeG_pyiCyQ7xC5yICj5mtiZy7oMTnB24AOSQPSf4LKAjKDKZwyKBS06cqhgr1enY0OAPmbSQxvM; pinId=Oc3JID567qU; pin=wend-12; unick=wend-12; ceshi3.com=000; _tp=2PhllUq1yx%2BLrr%2BzXT0WOQ%3D%3D; _pst=wend-12; __jda=122270672.1602568778508762049783.1602568778.1602574509.1602582751.3; __jdb=122270672.1.1602568778508762049783|3.1602582751; shshshsID=f16b5119444ea5361f5eef3475072f8c_1_1602582751905; thor=87AEEC639FACE77A00645E815159D0D0E38D2DEECD53C73E75FCB39E517F858B8068111D4B15B6CF94A7CBDAE3B13066AACC401A412A0EB59CB95E0C7660148BC31C64EC4202C91AA18C3608CA77FE90696567A59EDA57CCCFE653AE5EA9777AAAFCD6045146417D3FE3393A3612A29566F301E71BA372920D9366150A791C0CE2F838D615CE7E097435DB8CC54540A7',
        'origin': 'https://pro.m.jd.com',
        'referer': 'https://pro.jd.com/mall/active/TT9s9JigEyqGXyn8VUN9sSzzLq8/index.html',
        'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36'
    }
    data = {
        'body': '{"activityId":"TT9s9JigEyqGXyn8VUN9sSzzLq8","scene":"1","args":"key=60380964227D971E6B766F652EF4FE5F7950D59C3F2507F4F993F3E042208C5ED234A7E882347522B56957883295D239_babel,roleId=CC4F462FF17611DD74637C66C334FB31_babel","platform":"3","orgType":"2","openId":"-1","pageClickKey":"-1","eid":"YG6ZLMD633GAW35XHLWIK7MD5BI3IPH3KP56I6FTW4BMD7X3AC4VPPHRALPJ5NNWXRE2HNAQX6HHE2QJ72HCASHGUU","fp":"093a3e2112064094088a57d5f26707f2","shshshfp":"28a151259dc99494fecf5ea56854a5fa","shshshfpa":"058d1b75-2baa-b4a9-4c7b-da07f9020eea-1602123419","shshshfpb":"wX0r7CY/sIUZopDpnTGJZrw==","childActivityUrl":"https://pro.m.jd.com/mall/active/TT9s9JigEyqGXyn8VUN9sSzzLq8/index.html","pageClick":"Babel_Coupon","mitemAddrId":"","geo":{"lng":"","lat":""},"addressId":"","posLng":"","posLat":"","focus":"","innerAnchor":"","cv":"2.0"}',
        'screen': '750*1334',
        'client': 'wh5',
        'clientVersion': '1.0.0',
        'sid': '',
        'uuid': '16021234195141801139854',
        'area': ''
    }
    

    response = requests.post(url=url, headers=headers, data=data)
    print(response.content.decode())

if __name__ == '__main__':
    geturl()
