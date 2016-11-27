import requests
import re

__author__ = 'Stan'


def get_suitcase_size():
    r = requests.get('http://pkit.wopr.c2x.io:8000/suitcases/rolly')
    return r.json()['volume']


def get_parts():
    r = requests.get('http://pkit.wopr.c2x.io:8000/robots/hey-you/parts')
    return r.json()


def sort_parts(array):
    convert = lambda text: int(text) if text.isdigit() else text
    alphanum_key = lambda key: [convert(c) for c in re.split('([0-9]+)', key)]
    return sorted(array, key=alphanum_key)


def pack_the_stuff():
    suitcase = get_suitcase_size()
    parts = sorted(get_parts(), key=lambda k: k['value'])[::-1]
    ids = []
    total_value = 0
    result = {}
    for part in parts:
        suitcase -= part['volume']
        if suitcase <= 0:
            break
        ids.append(str(part['id']))
        total_value += part['value']
    result['part_ids'] = sort_parts(ids)
    result['value'] = total_value
    print result
    return result

pack_the_stuff()
