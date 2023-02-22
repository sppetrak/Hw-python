eng = 'qwertyuiopasdfghjklzxcvbnm'
rus = 'ёйцукенгшщзхъфывапролджэячсмитьбю'

eng_dict = {1: 'AEIOULNSTR',
            2: 'DG',
            3: 'BCMP',
            4: 'FHVWY',
            5: 'K',
            8: 'JX',
            10: 'QZ'}
rus_dict = {1: 'АВЕИНОРСТ',
            2: 'ДКЛМПУ',
            3: 'БГЁЬЯ',
            4: 'ЙЫ',
            5: 'ЖЗХЦЧ',
            8: 'ШЭЮ',
            10: 'ФЩЪ'}

word = input('Введите слово на Русском или Английском языке: ')

def count_points(lang_dict: dict, word: str):
    summa = 0
    for letter in word:
        for key, value in lang_dict.items():
            if letter.upper() in value:
                summa += key
    print(f'Сумма баллов за слово {word} - {summa}')

if word[0].lower() in eng:
    count_points(eng_dict, word)
else:
    count_points(rus_dict, word)