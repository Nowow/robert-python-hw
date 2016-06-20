# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup
import re
import operator

jerome_klapka = open('/run/media/robert/1TB-1/linuxfolder/gitlair/robert-python-hw/disamb/jerome_parsed3', 'r')

soup = BeautifulSoup(jerome_klapka, 'lxml')

prep = [
        'без', 'безо', 
        'близ', 
        'в', 'во' ,
        'вместо', 'вне',
        'для',
        'до',
        'за', 
        'из', 'изо', 
        'из-за',
        'из-под' 
        'к' ,'ко', 
        'кроме',
        'между', 'меж',
        'на', 
        'над', 'надо', 
        'о', 'об', 'обо' 
        'от', 'ото', 
        'перед', 'передо'
        'пo' 
        'под', 'подо', 
        'при', 
        'про',
        'ради' 
        'с', 'со', 
        'сквозь', 
        'среди', 
        'у', 
        'через'
        ]


padeji = ['им',
          'род',	
          'дат',	
          'вин',	
          'твор',	
          'пр',	
          'парт',	
          'местн',	
          'зват' 
          ]


class Word(object):
    
    
        
    
    padej_list = {}
    def spisok_padej(self, prep, padej):
        if prep in list(self.padej_list.keys()):
            if padej in list(self.padej_list[prep].keys()):
                self.padej_list[str(prep)][str(padej)] += 1
            else:
                self.padej_list[str(prep)][str(padej)] = 1
        else:
            self.padej_list[str(prep)] = {str(padej) : 1}
            
    def __init__(self, prep, padej):
        self.spisok_padej(prep,padej)
            
    def return_pad_freq(self, padej):
        return self.padej_list[padej]
        
    def max_count_padej(self):
       return max(padej_list.iteritems(), key=operator.itemgetter(1))[0]
            
            
            
            
it_was_prep = True
it_is_prep = True
prep_was = ''
prep_is = ''
word_is = ''
word_was = ''
word_list = {}
counter = 0
for item in soup.find_all('ana'):
    
    it_was_prep = it_is_prep
    prep_was = prep_is
    word_was = word_is
    #print(item)
    lex = item.get('lex')
    print(lex)
    gr = item.get('gr')
    print(gr)
    pad = None
    for p in padeji:
        if len(re.findall('[=]' + p , gr)) > 0:
       #     print('DA BEJBI')
            pad = str(re.findall('[=]' + p , gr)[0][1:])
            type(pad)
    print('bil padej ' + str(pad))
    print('bil prep ' +prep_was)
    if lex in prep:
       
        print('ETO PRISTAVKA')
        it_is_prep = True
        prep_is = lex
        continue
 
    else:
        word_is = lex
        
        prep_is = ''
        if lex == word_was:
            if it_was_prep:
                counter += 1
                if lex in list(word_list.keys()):
                    word_list[lex].spisok_padej(prep_was, pad)
                else:
                    word_list[lex] = Word(prep_was, pad)
        else:
            it_is_prep = False

# CAN DO COOL THINGS! SOBIRAET, K KAKOMU SLOVU S PREDLOGOM SZADI KAKIE BILI PADEJI I IH 4ASTOTNOST'!