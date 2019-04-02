teplota_vody = float(input ('Zadejte teplotu vody:'))
cislo_je_spravne = teplota_vody > 0

if teplota_vody < 0:
        print ('Voda je zmrzlá!')
elif teplota_vody == 0:
        print ('Voda je skoro zmrzlá!') 
elif teplota_vody < 20:
        print ('Voda je studená! Nekoupal bych se!')      
elif teplota_vody <=35:
        print ('Voda není moc tepla, ale můžete se vykoupat') 
elif teplota_vody <= 40:
        print ('Voda je dostatečně teplá.')
elif teplota_vody > 40:
        print ('Pozor! Může pálit!')
