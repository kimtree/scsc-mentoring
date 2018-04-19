import pa01
import string

# quadgram 관련 정보 생성
fp = open('english_quadgrams.txt', 'r')
quadgram_dict = pa01.log_probability_dictionary(fp)
print(quadgram_dict)

value = pa01.fitness_calculator('PRANSHU', quadgram_dict)
print(value)

# 찾을 수 없는 키: 48
pa01.chosen_plaintext_attack('0123456789qwertyuiopasdfghjklzxcvbnm., ', '02030405060708090A0B1C22101D1F2420141A1B0C1E0F11121315161725230E210D19184243', 2, '131017171A48221A1D170F')

# now you know it
pa01.chosen_plaintext_attack('0123456789qwertyuiopasdfghjklzxcvbnm., ', 'F2F3F4F5F6F7F8F9FAFB0D13010E101511050B0CFC0F000203040607081614FE12FD0A09333439', 2, '0A0B1339150B1139070A0B13390510')

# ITISPARADOXICALYETTRUETOSAYTHATTHEMOREWEKNOWTHEMOREIGNORANTWEBECOMEINTHEABSOLUTE ..
cipher_text = 'Uf ue bmdmpajuomx, kqf fdgq, fa emk, ftmf ftq yadq iq wzai, ftq yadq uszadmzf iq nqoayq uz ftq mneaxgfq eqzeq, rad uf ue azxk ftdagst qzxustfqzyqzf ftmf iq nqoayq oazeouage ar agd xuyufmfuaze. Bdqoueqxk azq ar ftq yaef sdmfurkuzs dqegxfe ar uzfqxxqofgmx qhaxgfuaz ue ftq oazfuzgage abqzuzs gb ar zqi mzp sdqmfqd bdaebqofe - Zuwaxm Fqexm'
cipher_text = cipher_text.replace(' ', '').translate(str.maketrans({key: None for key in string.punctuation}))
pa01.bruteforce_shift_cipher(cipher_text, quadgram_dict)