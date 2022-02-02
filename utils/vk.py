import requests
import os
import json


def get_token_or_none():
    try:
        return os.environ['VKTOKEN']

    except:
        return None


def get_group_id_or_none():
    try:
        return os.environ['VKGROUPID']
    except:
        return None


def isMember(user_id, group_id=get_group_id_or_none(), token=get_token_or_none(), v='5.131'):
    url = f'https://api.vk.com/method/groups.isMember?group_id={group_id}&user_id={user_id}&access_token={token}&v={v}'
    result = requests.get(url).text
    print(url)
    if 'error' in result:
        print('Here')
        return False

    result = result.split(':')[-1][:-1]
    if '1' in result:
        return True
    else:
        return False


def get_info_or_none(data):
    data_dict = json.loads(data)
    first_name = None
    last_name = None
    try:
        vk_id = data_dict['id']
    except:
        return None

    try:
        first_name = data_dict['first_name']
        last_name = data_dict['last_name']
    except:
        pass

    return vk_id, first_name, last_name


token = 'a84f91cfa84f91cfa84f91cfc4a8348da0aa84fa84f91cfc9b6e840f9c891f5f317c6f9'
group_id = '190897798'
user_id = '504591770'
# print(isMember(user_id))
data = """{"id": 504591770, "first_name": "\u0415\u0432\u0433\u0435\u043d\u0438\u0439", "last_name": "\u0414\u0435\u0433\u0442\u044f\u0440\u0435\u0432", "can_access_closed": true, "is_closed": false, "sex": 2, "screen_name": "eugdeg", "online": 0, "nickname": "", "bdate": "19.2.1997", "city": {"id": 1, "title": "\u041c\u043e\u0441\u043a\u0432\u0430"}, "country": {"title": "\u0420\u043e\u0441\u0441\u0438\u044f", "id": 1}, "timezone": 3.0, "photo_max_orig": "https://sun1-28.userapi.com/s/v1/ig2/MUXGSGcNMptDMYhIx9wL0HOrgSLVsSDL9veWh7Fe9Cns7D4Wls9aUfMcMCMk2xlX7qAxyssfHkOQo0m3nLACqBg7.jpg?size=400x400&quality=96&crop=500,97,1538,1538&ava=1", "has_mobile": 1, "photo_medium": "https://sun1-28.userapi.com/s/v1/ig2/6hGyjsuQyFozu66jrFSBFZ9ziwF1nwjdBWsMiyl8BAF1rf4rA1nSsC7bN-snIOZ514hSuB0z8KsYg5yjOwGtM9Qi.jpg?size=100x100&quality=96&crop=569,97,1224,1224&ava=1", "photo": "https://sun1-28.userapi.com/s/v1/ig2/ECtK4Rc_aHu8SuroD5-E7gf3iHwq5JM3OcOs0takCf27Rnn3TnjjL3BPmILNQuo0k7RWIBggvvcvfAKbBg4yEPeN.jpg?size=50x50&quality=96&crop=569,97,1224,1224&ava=1", "photo_big": "https://sun1-28.userapi.com/s/v1/ig2/7cWJSgkXlJRMOw0RLZcuQucH1PC44B2oDwNBzEoVYGw3uDxAShChWAY4d3IFFSFBXCThe2gA0WCdabpzZfUtI5xT.jpg?size=200x200&quality=96&crop=500,97,1538,1538&ava=1", "activity": "Don't tread on me", "last_seen": {"platform": 4, "time": 1643749004}, "university": 0, "university_name": "", "faculty": 0, "faculty_name": "", "graduation": 0, "relation": 0, "universities": [], "counters": {"albums": 0, "audios": 143, "followers": 52, "friends": 110, "gifts": 71, "groups": 71, "online_friends": 18, "pages": 58, "photos": 5, "subscriptions": 1, "videos": 22, "new_photo_tags": 0, "new_recognition_tags": 0, "clips_followers": 162}}"""
print(get_info_or_none(data))
