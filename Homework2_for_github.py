#имеется список с почтами клиентов
crm = [[510266, 'b0198ff4@mail.ru'],
 [882968, '5bda448e2@mail.ru'],
 [1446917, 'e860d3c@yandex.ru'],
 [237601, '17f1f367@mail.ru'],
 [79304, 'f408b395d@gmail.com'],
 [535956, '15fcf41fe@i-free.com'],
 [1657538, 'e13cbd939@mail.ru'],
 [43966, 'd4e8b4@mail.ru'],
 [2112521, '1763b7@mail.ru'],
 [1038965, '21b786@mail.ru'],]
#достанем из списка только почты клиентов
only_mail = list() 
count = 0
for data in crm:
    only_mail.append((crm[count][1]))
    count += 1
print(only_mail)

# создадим список, в котором будут только домены почт после символа «@»
domains = list()
count = 0
for data in only_mail:
    
    dom = data[data.find('@')+1:]
    #print(dom)
    domains.append(dom)
    count += 1
  # напиши здесь свой код
print(domains)

#допустим нам нужно удалить все домены mail.ru

copy_domains_number4 = domains.copy() # копируем список доменов , чтобы последующие изменения не коснулись исходного списка
while copy_domains_number4.count('mail.ru') != 0:
    copy_domains_number4.remove('mail.ru')
print(copy_domains_number4)
print(copy_domains_number4.count('mail.ru')) #проверяем результат


#допустим теперь нужно создать список уникальных доменов
unic_domain = set(copy_domains_number4)
print(unic_domain)

#  а теперь узнать количество уникальных доменов
new_copy_domains = domains.copy() #создали копию всех доменов

new_unic_domain = unic_domain.copy() #создали копию списка уникальных доменов
new_dict_domains = {} #создали пустой словарь
for i in new_unic_domain:
    new_dict_domains[i] = new_copy_domains.count(i)
print(new_dict_domains)
