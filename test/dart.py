# reference: http://dart.fss.or.kr/dsap001/guide.do

import argparse
import requests


def company_search(params):
    '''
    http://dart.fss.or.kr/api/search.xml?auth=xxx     xml 응답
    http://dart.fss.or.kr/api/search.json?auth=xxx    json 응답
    '''
    URL = 'http://dart.fss.or.kr/api/search.json'
    res = requests.get(URL, params=params)

    print('status code: ' + str(res.status_code))
    print('json: ' + str(res.json()))


def company_condition(params):
    '''
    http://dart.fss.or.kr/api/company.xml?auth=xxx&crp_cd=xxx    xml 응답
    http://dart.fss.or.kr/api/company.json?auth=xxx&crp_cd=xxx   json 응답
    '''
    pass


def main(api_key):
    params = {'auth': api_key, 'page_set': 100}
    company_search(params)


if __name__ == '__main__':
    print('[' + __file__ + '] main invoked.')

    AP = argparse.ArgumentParser(description='arg parser')
    AP.add_argument('-api_key', action='store', required=True,
                    help='your API key for the DART service')
    ARGS = AP.parse_args()

    main(ARGS.api_key)
