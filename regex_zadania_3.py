import re
Zadanie_11="Zadanie 11"
print(f"{Zadanie_11}")

text_11="Mój stary adres to 02-123 Warszawa, a nowy to 34-500 Zakopane. Zignoruj błędne kody jak 123-45, 12-3456 czy a1-123."
wzór_11=r"\d{2}-\d{3}"
wynik_11=re.findall(wzór_11, text_11)
print(f"{wynik_11}")

Zadanie_12="Zadanie 12"
print(f"{Zadanie_12}")

text_12="Wczoraj Adam i Kasia poszli do kina. Zabrał się z nimi też mały piesek reksio. Jutro dołączy do nich Piotr i zapominalski tomek."
wzór_12=r"\b[A-Z]\w+"
wynik_12=re.findall(wzór_12, text_12)
print(f"{wynik_12}")

Zadanie_13="Zadanie 13"
print(f"{Zadanie_13}")

text_13="Na parkingu stały auta o numerach: KR12345, WX98765, a także rower i auto z zagranicy (zły format: AB12C). Znalazłem też PO55555."
wzór_13=r"[A-Z]{2}\d{5}"
wynik_13=re.findall(wzór_13, text_13)
print(f"{wynik_13}")