# reference: http://dart.fss.or.kr/dsap001/guide.do

import argparse
import requests


def main(api_key):
    URL = 'http://dart.fss.or.kr/api/search.json'
    params = {'auth': api_key, 'page_set': 100}
    res = requests.get(URL, params=params)

    print('status code: ' + str(res.status_code))
    print('json: ' + str(res.json()))


if __name__ == '__main__':
    print('[' + __file__ + '] main invoked.')

    AP = argparse.ArgumentParser(description='arg parser')
    AP.add_argument('-api_key', action='store', required=True,
                    help='your API key for the DART service')
    ARGS = AP.parse_args()

    main(ARGS.api_key)
