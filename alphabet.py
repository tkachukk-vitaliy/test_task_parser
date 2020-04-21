import itertools

##a = ord('а')
##alph_ru = ''.join([chr(i) for i in range(a,a+6)] + [chr(a+33)] + [chr(i) for i in range(a+6,a+32)])
##print(alph_ru)
##print(''.join([chr(i) for i in range(a,a+6)] + [chr(a+33)] + [chr(i) for i in range(a+6,a+32)]))
##
##print(string.ascii_lowercase)
alph_ru = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
alph_uk = 'абвгґдеєжзиіїйклмнопрстуфхцчшщьюя'
alph_en = 'abcdefghijklmnopqrstuvwxyz'
alph_test = 'abcdefg'

ALPH_LIST = [alph_test]

proxies = ['159.224.166.129:51020',
         '212.90.168.150:52589',
         '93.78.238.94:41258',
         '194.79.20.30:8080',
         '212.115.224.71:53281',
         '94.244.28.246:31280',
         '188.163.170.130:41209',
         '176.104.52.46:47578',
         '91.193.253.188:23500',
         '37.57.15.43:33761']

userag = ['Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 10.0; Trident/8.0; .NET4.0C; .NET4.0E; .NET CLR 2.0.50727; .NET CLR 3.0.30729; .NET CLR 3.5.30729)' ,
          'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 10.0; WOW64; Trident/7.0; .NET4.0C; .NET4.0E; .NET CLR 2.0.50727; .NET CLR 3.0.30729; .NET CLR 3.5.30729; ms-office; MSOffice 16)',
          'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.1; Trident/7.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; InfoPath.3; Tablet PC 2.0; .NET4.0E; Shuame; GWX:DOWNLOADED; GWX:RESERVED)',
          'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E; InfoPath.3; ms-office; MSOffice 15)',
          'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.2; Win64; x64; Trident/7.0; .NET4.0E; .NET4.0C; .NET CLR 3.5.30729; .NET CLR 2.0.50727; .NET CLR 3.0.30729; CMNTDFJS)',
          'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.2; Win64; x64; Trident/7.0; .NET4.0E; .NET4.0C; .NET CLR 3.5.30729; .NET CLR 2.0.50727; .NET CLR 3.0.30729; CMNTDFJS; ms-office; MSOffice 15)',
          'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.3; Win64; x64; Trident/7.0; .NET4.0E; .NET4.0C; .NET CLR 3.5.30729; .NET CLR 2.0.50727; .NET CLR 3.0.30729; GWX:RED; GWX:RESERVED; LCJB)',
          'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0; .NET CLR 1.1.4322; .NET CLR 2.0.50727; .NET CLR 3.0.04506.30; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729)',
          'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0; .NET CLR 2.0.50727; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729; .NET CLR 1.1.4322; .NET4.0C)',
          'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0)',]


def combinate(alph, n):
    list_cwr = []
    for combos in itertools.combinations_with_replacement(alph,n):
        list_cwr.append(''.join(combos))
    return list_cwr

def list_input(n):
    F = [combinate(ALPH_LIST[j], i+1) for i in range(n) for j in range(len(ALPH_LIST))]
    list_input = [x for xs in F for x in xs]
    return list_input




##print(len(list_input(2)))


##all_links =[]
##for _ in range(len(list_input(2))):
##    all_links.append([{'q':list_input(2)[i], 'isAJax': 1} for i in range(len(list_input(2)))])
###all_links = [{'q':alphabet.list_input(2)[i], 'isAJax': 1} for i in range(len(alphabet.list_input(2)))]
##print(len(all_links))




