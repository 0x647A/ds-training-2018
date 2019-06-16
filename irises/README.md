# Zadanie rekrutacyjne - roche_c4l (Junior Data Science)
(To do this report I use polish language, because the ask was written in this language)

---

### Zadania 1

Twój klient zajmuje się importem kwiatów (irysów) z Chin. Sprowadza zawsze te same 3 gatunki: Virginica, Versicolor oraz Setosa. Niestety wraz z ostatnią dostawą kwiaty wymieszały się i nie wiadomo, który jest który (co zaskakujące, nawet eksperci z kwiaciarni nie potrafią odpowiedzieć na to pytanie!). Na szczęście zostało jeszcze 150 sztuk z poprzedniej dostawy, które są dobrze oznaczone. Klient polecił zmierzyć długości i szerokości płatków, aby spróbować na tej podstawie poprawnie przyporządkować nowe kwiaty do odpowiednich kategorii.

**Cel**: Na podstawie dostarczonych danych opracuj model klasyfikacyjny do jednego z 3 gatunków irysów. Przygotuj raport, w którym opiszesz swój tok myślenia oraz podjęte działania. W razie wątpliwości pojawiających się w trakcie realizacji zadania opisz je w taki sposób jakbyś zwracał/a się do klienta z prośbą o odpowiedzi (mimo wszystko jednak oczekiwany jest na końcu model z oszacowaną jakością klasyfikacji). Celem tego zadania nie jest wyśrubowanie modelu, ale ukazanie procesu twórczego.

---

### Kontakt z klientem:

**Klient**: O nie! Daria! Straszne rzeczy! Moje kwiaty ukochane, które sprowadzam od lat, wymieszały się! O nie! ;-(

**Ja**: Jak to się wymieszały? A to aż taki problem? Sam mówisz, że sprowadzasz je od lat, więc pewnie z zamkniętymi oczami je rozpoznasz! :-) 

**Klient**: Właśnie nie! Jestem amatorem tych kwiatów, a nie znawcą... Co ja teraz zrobię... Virginica... Versicolor... Setosa... Znam tylko nazwy, ale nie umiem ich odróżnić... Jej...

**Ja**: Bardzo mi przykro... a może wiesz chociaż, co odróżnia jednego Irysa od drugiego? Może jest coś takiego po czym będzie wiadomo, że są inne?

**Klient**: Hmmmm.... Nie wiem :-( Ale! Zaraz, zaraz! Jest coś takiego! Długość i szerokość płatków oraz kielicha. Niestety nie wiem, jakie wymiary ma dana odmiana. Czy to może być pomocne?

**Ja**: Jasne! Zobacz, jak będziemy mieli tą cechę to możemy dane kwiaty sklasteryzować!

**Klient**: Co masz na myśli?

**Ja**: Podzielimy je na trzy grupy. W każdej grupie będą odmiany kwiatów, które mają podobne wymiary płatków!

**Klient**: Aaaaa to ma sens! Ale nawet, jak je podzielimy w grupy to nie będziemy wiedzieli, które to które... Więc to jest jakby bez sensu.

**Ja**: Wcale nie! Może masz jeszcze w magazynie jakieś oznaczone odmianą kwiaty?

**Klient**: Tak, mam. Zostało mi jeszcze 150 sztuk z poprzedniej dostawy.

**Ja**: No własnie! Spójrz będziemy mieli podzielone na grupy trzy odmiany pod względem szerokości i długości płatka. Później porównamy to z przedstawicielami oznaczonych odmian z magazynu i już! Po problemie!

**Klient**: Faktycznie! I damy radę to zrobić?

**Ja**: Oczywiście! Zrobię, co w mojej mocy. Nie martw się!

**Klient**: Kamień z serca! Dziękuję! W takim razie czekam na Twoje wyniki :-) 

---

### Rozwiązanie zadania

1. Podstawowe informacje o zadaniu:
    * Tytuł: Podział pomieszanych irysów na trzy gatunki: Virginica, Versicolor, Setosa;
    * Zbiór ma 4 atrybuty i 150 wierszy - mały, łatwo mieści się w pamięci;
    * Rodzaj zadania: klasyfikacja (multiclass);
    * Zbiór danych: /data/C4L Academy - Data Science Graduate - IRISES dataset (2019-06).csv;
    * Język programowania wykorzystany do wykonania zadania: Python; 
    * Środowisko: Jupiter Notebook;
    * System kontroli wersji: git;
    * Platforma, gdzie będzie umieszczony kod: GitHub;
    

2. Plan działania:
    * Poznanie i zrozumienie danych danych:
            - załaduje dane do dataframe (skorzystam z Pandas - Python Data Analysis Library);
            
            - wyekstraktowanie podstawowych informacji o danych: 
            
                - .info(): podstawowe informacje o zbiorze danych,
                
                - .shape: metoda opisująca kształt danych,
                
                - .describe(): liczy podstawowe statystyki dla danych,
                
                - .nunique(): liczba unikatowych elementów,
                
                - .isnull(): szuka pustych wartości,
                
                - .sample(n): zwraca n wylosowanych wierszy,
                
                - .columns: wypisuje nazwy kolumn,
                
                - .corr() oblicza korelacje między kolumnami w zbirze danych;
               
               
3. Przygotowanie danych                
4. Wizualizacja danych (wykorzystana bibliotekę matplotlib);
5. Zbudowanie modelu: 
      * do tego problemu wybrałam algorytm "K najbliższych sąsiadów" - jest to algorytm klasyfikacji i regresji. Pobiera dane wejściowe i wybiera grupę, z której pochodzą dane.
      
      
6. Optymalizacja - próba polepszenia wyników.
7. Wizualizacja wyników.
___

[**Link do kodu źródłowego**](https://github.com/dczerniawko/portfolio/blob/master/irises/roche_c4l.ipynb) 

___

### Wnioski

Zadanie udało się wykonać. Model osiągnął dokładność na pozomie 93%.