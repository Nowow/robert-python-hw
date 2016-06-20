# -*- coding: utf-8 -*-

from xml.etree import ElementTree
import re
from lxml import etree




china_dict_source = open('cedict_ts.u8', 'r', encoding = 'utf-8')

china_dict = {}

for line in china_dict_source:
    if line[0] == '#':
        continue
    line = line.split()
    china_dict[line[1]] = {'lex' : line[0]}
    ind = 3
    for i in line[2:]:
        if i.endswith(']'):
            break
        else:
            ind += 1
    trans = ''
    for i in range(2,ind):
        trans += line[i]
    china_dict[line[1]].update({'transcr' : trans,
                                'sem' : ' '.join(line[ind:])})
                
china_dict_source.close()


china_source = ElementTree.parse('/run/media/robert/1TB-1/linuxfolder/gitlair/robert-python-hw/china/stal.xml')


root = etree.Element('se')
for node in china_source.iter():
    print('new one')
    
    linecash = node.text
    linecash = linecash.lower()
    linecash = re.sub(r'\W+', '', linecash)
    linecash = re.sub('ａ', '', linecash)
    
#    linecash = linecash.replace('！','')
#    linecash = linecash.replace('“','')
#    
#    linecash = linecash.replace('？','')
#    linecash = linecash.replace('：','')
#    linecash = linecash.replace('。','')
#    linecash = linecash.replace('、','')
    
    
#    linecash = linecash.encode()
#    linecash = linecash.decode()
    for i in range(len(linecash)):
        if len(linecash) < 2:
            continue
        key_cash = []
        try:
            if node.attrib['lang'] == 'ru':
#                print('ETO RUSSKAY')
                continue
        except:
            pass
        
        print(linecash)
        
      #  print(linecash == g)
        for item in list(china_dict.keys()):        
            if str(linecash).startswith(item):
    #            print('HEL RUBICK')
                key_cash.append(item)
        print(key_cash)
        maxkey = max(key_cash)
        w = etree.Element('w')
        ana = etree.Element('ana')
        ana.attrib['lex'] = china_dict[maxkey]['lex']
        ana.attrib['transcr'] = china_dict[maxkey]['transcr']
        ana.attrib['sem'] = china_dict[maxkey]['sem']
        ana.text = maxkey
        w.append(ana)
        root.append(w)
        linecash = linecash[len(maxkey):]
        
dump = open('dump.xml', 'bw')
tr = etree.ElementTree(root)
tr.write(z, encoding = 'utf-8', pretty_print = True )

    #node.text
    
        
    