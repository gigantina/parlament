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

