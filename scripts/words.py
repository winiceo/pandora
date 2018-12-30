#!/usr/bin/env python
# -*- coding: utf-8 -*-

import utils
import api

words = [
    {
        'text@en': 'house',
        'text@ru': 'дом',
        'transcription@en': 'hause',
        'transcription@ru': "'хаус",
        'pronunciation@en': 'https://howjsay.com/mp3/house.mp3',
        'images': [
            'http://epicpix.com/wp-content/uploads/2016/04/ff_3280.jpg',
        ],
    },
    {
        'text@en': 'lake',
        'text@ru': 'озеро',
        'transcription@en': 'leik',
        'transcription@ru': "'лэйк",
        'pronunciation@en': 'https://howjsay.com/mp3/lake.mp3',
        'images': [
            'https://github.com/flutter/website/blob/master/src/_includes/code/layout/lakes/images/lake.jpg?raw=true',
        ],
    },
    {
        "text@en": "gum",
        "text@ru": "жвачка",
        "transcription@ru": "гам",
        'pronunciation@en': 'https://howjsay.com/mp3/gum.mp3',
        "images": [
            "https://i.pinimg.com/originals/39/10/30/3910305670e1fb3f0584e998e30f1b71.jpg",
            "https://images-na.ssl-images-amazon.com/images/I/81F-d7PAZQL._SL1500_.jpg",
            "https://cdn.shopify.com/s/files/1/0004/8132/9204/products/double-mint-gum_1024x1024.jpg?v=1522355731",
        ],
    },
    {
        "text@en": "recreation",
        "text@ru": "отдых",
        "transcription@ru": "рикри`эйшен",
        'pronunciation@en': 'https://howjsay.com/mp3/recreation.mp3',
        "images": [
            "http://www.bridgewaternj.gov/wp-content/uploads/Images/recphoto.jpg",
            "https://vmcdn.ca/f/files/halifaxtoday/images/sports/071818-sports-equipment-recreation-gym-fitness-adobestock_190038155.jpeg;w=630",
            "http://www.worldwar-collectibles.com/wp-content/uploads/2017/03/recreation.jpg",
        ],
    },
    {
        "text@en": "apple",
        "text@ru": "яблоко",
        "transcription@ru": "эпл",
        'pronunciation@en': 'https://howjsay.com/mp3/apple.mp3',
        "images": [
            "http://static1.squarespace.com/static/5849b12a2e69cf47aecece6b/584ebb9646c3c416aac4f2b5/5b830f4dcd8366d1f2d15de9/1535382024204/apple.jpg?format=1500w",
        ],
    },
    {
        "text@en": "table",
        "text@ru": "стол",
        "transcription@ru": "тэйбл",
        'pronunciation@en': 'https://howjsay.com/mp3/table.mp3',
        "images": [
            "https://cdn.shopify.com/s/files/1/2660/5106/products/wisz8mrpd67l6pss3crw_2b63262e-9b7a-4bbb-8f4f-d2da5d3cc57f_800x.jpg?v=1539039199",
        ],
    },
    {
        "text@en": "spoon",
        "text@ru": "ложка",
        "transcription@ru": "спун",
        'pronunciation@en': 'https://howjsay.com/mp3/spoon.mp3',
        "images": [
            "https://coubsecure-s.akamaihd.net/get/b45/p/coub/simple/cw_timeline_pic/f357228b51f/972920dc0d51d3ed34e9d/big_1409081702_1382451563_att-migration20121219-1328-1jpmbyq.jpg",
        ],
    },
    {
        'text@en': 'girl',
        'text@ru': 'девушка',
        'transcription@en': 'gerl',
        'transcription@ru': "'гёл",
        'pronunciation@en': 'https://howjsay.com/mp3/girl.mp3',
        'images': [
            'https://i.ytimg.com/vi/ktlQrO2Sifg/maxresdefault.jpg',
        ],
    },
    {
        'text@en': 'bed',
        'text@ru': 'кровать',
        'transcription@en': 'bed',
        'transcription@ru': "'бэд",
        'pronunciation@en': 'https://howjsay.com/mp3/bed.mp3',
        'images': [
            'https://hoff.ru//upload/iblock/9be/9be0921f96cf2f30b4e5136c4eccd7d8.jpg',
        ],
    },
    {
        'text@en': 'boy',
        'text@ru': 'мальчик',
        'transcription@en': 'bOI',
        'transcription@ru': "'бой",
        'pronunciation@en': 'https://howjsay.com/mp3/boy.mp3',
        'images': [
            'https://www.paparazzi.ru/upload/wysiwyg_files/img/1472483485.jpg',
        ],
    },
    {
        'text@en': 'body',
        'text@ru': 'тело',
        'transcription@en': 'bOdI',
        'transcription@ru': "'боди",
        'pronunciation@en': 'https://howjsay.com/mp3/body.mp3',
        'images': [
            'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRKLUYuJGon1owJX__Y7Ov3uzLVPwMzK7dXDS375I5DRRP3ISprGA',
        ],
    },
    {
        'text@en': 'car',
        'text@ru': 'автомобиль',
        'transcription@en': 'kɑːr',
        'transcription@ru': "'кар",
        'pronunciation@en': 'https://howjsay.com/mp3/car.mp3',
        'images': [
            'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRmIGgC7NLbTyrby1pTLhexemP0apw-H_zJ0at2BdJhPuHdhqiu',
        ],
    },
    {
        'text@en': 'door',
        'text@ru': 'дверь',
        'transcription@en': 'dɔːr',
        'transcription@ru': "'дор",
        'pronunciation@en': 'https://howjsay.com/mp3/door.mp3',
        'images': [
            'https://images.obi.ru/product/RU/800x600/400211_1.jpg',
        ],
    },
]


def rdf_repr(v):
    if isinstance(v, str):
        return '"{0}"'.format(v)
    return v


def nquad(id, k, v):
    a = k.split('@')
    p = a[0]
    lang = a[1] if len(a) == 2 else ''
    s = rdf_repr(v)
    if len(lang) > 0:
        s += "@{0}".format(lang)
    return "_:{0} <{1}> {2} .\n".format(id, p, s)


def nquads(d, id='x'):
    result = ''
    for k, v in d.iteritems():
        result += nquad(id, k, v)
    return result


def get_id(resp, id='x'):
    return resp['data']['uids'][id]


def pairs(list):
    for x in list:
        for y in list:
            yield (x, y)


# TODO find existing words and update their transcriptions, pronunciations, images
# TODO port this script to golang and provide an API endpoint
for word in words:
    # insert word nodes for all languages
    nodes = {}
    word_ids = []
    for key in word:
        if key.startswith('text@'):
            text = word[key]
            lang = key[key.index('@')+1:]
            props = {
                '_word': '',
                'text': text,
                'lang': lang,
            }
            trans_key = 'transcription@' + lang
            if trans_key in word:
                props['transcription'] = word[trans_key]
            data = nquads(props)
            resp = api.set_nquads(data)
            wid = get_id(resp)
            nodes[lang] = wid
            word_ids.append(wid)

    # link words together with translated_as predicate
    proc = {}
    for (w1, w2) in pairs(word_ids):
        if w1 == w2:
            continue
        k1 = "{0}-{1}".format(w1, w2)
        k2 = "{0}-{1}".format(w2, w1)
        if k1 in proc:
            continue
        data = "<{0}> <translated_as> <{1}> .\n".format(w1, w2)
        api.set_nquads(data)
        proc[k1] = 1
        proc[k2] = 1

    # todo upload images to S3 store
    # insert images
    image_nodes = []
    for url in word['images']:
        data = nquads({
            '_image': '',
            'url': url,
            'source': 'google',
        })
        resp = api.set_nquads(data)
        obj_id = get_id(resp)
        # link with connected words
        for lang in nodes:
            wid = nodes[lang]
            data = "<{0}> <relevant> <{1}> .\n".format(wid, obj_id)
            api.set_nquads(data)

    # todo upload sounds to S3 store
    for key in word:
        if key.startswith('pronunciation@'):
            lang = key[key.index('@')+1:]
            data = nquads({
                '_sound': '',
                'url': word[key],
                'source': 'https://howjsay.com',
            })
            resp = api.set_nquads(data)
            obj_id = get_id(resp)
            # link with word
            wid = nodes[lang]
            data = "<{0}> <pronounced_as> <{1}> .\n".format(wid, obj_id)
            api.set_nquads(data)
