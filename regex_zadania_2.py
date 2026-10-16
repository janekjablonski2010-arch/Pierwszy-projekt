import re
Zadanie_1="Zadanie 1"
print(f"{Zadanie_1}")

tekst="Paczka z Warszawy ma kod 02-123, a przesyłka do Krakowa leci na 31-009. Błędny kod to 123-45."
wzorzec=r"\d{2}[-\s]\d{3}"
wynik=re.findall(wzorzec,tekst)
print(f"Wynik: {wynik}")

Zadanie_2="Zadanie 2"
print(f"{Zadanie_2}")

tekst_2="Pies pije sok, lis bije w tok, a kot myje bok. Ten rok jest super!"
wzorzec_2=r"[stb]ok"
wynik_2=re.findall(wzorzec_2,tekst_2)
print(f"Wynik: {wynik_2}")

Zadanie_3="Zadanie 3"
print(f"{Zadanie_3}")

tekst_3="Z1, X2, Y3, Q9, Z8, M4"
wzorzec_3=r"[^z]\d"
wynik_3=re.findall(wzorzec_3,tekst_3)
print(f"Wynik: {wynik_3}")

Zadanie_4="Zadanie 4"
print(f"{Zadanie_4}")

tekst_4="Pierwsza lekcja jest o 08:00, długa przerwa o 11:30, a powrót do domu o 15:45. Fałszywy czas to 8:0."
wzorzec_4=r"\d{2}[:\s]\d{2}"
wynik_4=re.findall(wzorzec_4,tekst_4)
print(f"Wynik: {wynik_4}")

Zadanie_5="Zadanie 5"
print(f"{Zadanie_5}")

tekst_5="Moje urodziny to 15-08-2010. Mój brat urodził się 05.04.2015. Błędna data to 1-2-12."
wzorzec_5=r"\d{2}[-.\s]\d{2}[-.\s]\d{4}[-.\s]"
wynik_5=re.findall(wzorzec_5,tekst_5)
print(f"Wynik: {wynik_5}")

Zadanie_6="Zadanie 6"
print(f"{Zadanie_6}")

tekst_6="Wrzucam fotkę na Insta: #wakacje #morze2026 i #chill. Błędne to po prostu # (brak słowa) albo samo słowo plaza."
wzorzec_6=r"#\w+"
wynik_6=re.findall(wzorzec_6,tekst_6)
print(f"Wynik: {wynik_6}")

Zadanie_7="Zadanie 7"
print(f"{Zadanie_7}")

tekst_7="Sprawdź te linki: https://youtube.com oraz http://stara-gra.pl. Zignoruj zepsuty link htp://blad.com."
wzorzec_7=r"https?://"
wynik_7=re.findall(wzorzec_7,tekst_7)
print(f"Wynik: {wynik_7}")

Zadanie_8="Zadanie 8"
print(f"{Zadanie_8}")

tekst_8="Znalazłem pliki: mem.jpg, tapeta.png, smieszny_kot.gif. Nie klikaj w wirus.exe ani notatka.txt!"
wzorzec_8=r"\w+\.(?:jpg|png|gif)"
wynik_8=re.findall(wzorzec_8,tekst_8)
print(f"Wynik: {wynik_8}")


Zadanie_9="Zadanie 9"
print(f"{Zadanie_9}")

tekst_9="Nowa gra kosztuje 250 PLN, używana 99 PLN, a naklejka 5 PLN. Zignoruj zapis 50PLN (brak spacji) oraz tanio PLN."
wzorzec_9=r"\d+\sPLN"
wynik_9=re.findall(wzorzec_9,tekst_9)
print(f"Wynik: {wynik_9}")

Zadanie_10="Zadanie 10"
print(f"{Zadanie_10}")

tekst_10="Ten bot to świetny robot. Czy widziałeś moje nowe botki? Pamiętaj, bot to tylko bot."
wzorzec_10=r"\bbot\b"
wynik_10=re.findall(wzorzec_10,tekst_10)
print(f"Wynik: {wynik_10}")
