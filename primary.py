import math
liczba = 1
licznik = 0
cel = 1000000
plik = 'lista.txt'
plik_wyjsciowy = None
bufor = None
dzielniki = []

def start():
    sprawdz()

def sprawdz():
    global plik_wyjsciowy
    try:
        plik_wyjsciowy = open(plik, 'r')
    except FileNotFoundError:
        plik_wyjsciowy = open(plik, 'w')
        print('Plik nie istnieje. Tworzę plik: ' + plik)
        plik_wyjsciowy.close()
        licz()
    else:
        print('Plik ' + plik + ' istnieje. Rozpoczynam dopisywanie.')
        odczytaj()


def odczytaj():
    global plik_wyjsciowy, bufor, licznik, liczba
    plik_wyjsciowy = open(plik, 'r')
    for linia in plik_wyjsciowy:
        if linia != '' and linia != None:
            try:
                liczba = int(linia)
            except ValueError:
                pass
    # pozycja = bufor.find('. ')
    # licznik = int(bufor[:pozycja])
    # liczba = int(bufor[pozycja + 2:])

    plik_wyjsciowy.close()
    licz()

def odczytaj_dzielniki(max):
    global dzielniki
    max_int = int(max)
    x = 0
    plik_wyjsciowy.seek(0)
    for linia in plik_wyjsciowy:
        # pozycja_liczby = linia.find('. ')
        # pozycja_nowej_linii = linia.find('\n')
        # ls = list(linia)
        # print(ls)
        # if len(ls) < 1:
        #     continue
        # else:
        #     del ls[ls.index('\n')]

        # if len(ls) == 0:
        #     continue
        # else:
        #     try:
        #         del ls[0:ls.index(' ') + 1]
        #     except ValueError:
        #         pass
        # #
        #     del ls[ls.index('\n')]
        #     s = ''.join(ls)
        #     print(ls)
        #     x = int(s)

        # s = linia[linia.find('. ') + 2:linia.find('\n')]

        try:
            x = int(linia)
        except ValueError:
            continue
        else:
            if x <= max_int and x != 1 and x != 2:
                if dzielniki.count(x) == 0:
                    dzielniki.append(x)
                else:
                    continue
            else:
                break
    # print(dzielniki)
    # return dzielniki

def licz():
    global licznik, liczba, plik_wyjsciowy, dzielniki
    plik_wyjsciowy = open(plik, 'r+')

    while True:
        liczba += 1
        pierwsza = True
        if liczba % 2 == 0 or liczba == 2:
            continue
        else:
            pierwiastek_liczby = math.sqrt(liczba)
            odczytaj_dzielniki(pierwiastek_liczby)
            for dzielnik in dzielniki:
                if liczba % dzielnik == 0:
                    pierwsza = False
                    break

            # while dzielnik > 1:
            #     if liczba % dzielnik == 0:
            #         pierwsza = False
            #         break
            #     dzielnik -= 1
        if pierwsza == True:
            licznik += 1
            print(str(licznik) + ': ' + str(liczba))
            plik_wyjsciowy.seek(0, 2)
            plik_wyjsciowy.write(str(liczba) + '\n')

                # bufor = str(licznik) + '. ' + str(liczba)

                # plik_wyjsciowy.write(bufor + '\n')



start()
