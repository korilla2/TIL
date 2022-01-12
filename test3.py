from urllib import parse
import pandas as pd


def get_fnguide(code):
    get_param = {
        'pGB': 1,
        'gicode': 'A%s' % (code),
        'cID': '',
        'MenuYn': 'Y',
        'ReportGB': '',
        'NewMenuID': 101,
        'stkGb': 701,
    }
    get_param = parse.urlencode(get_param)
    url = "http://comp.fnguide.com/SVO2/ASP/SVD_Main.asp?%s" % (get_param)
    tables = pd.read_html(url, header=0)
    return(tables)


print(get_fnguide('036570')[11])  # 삼성전자
