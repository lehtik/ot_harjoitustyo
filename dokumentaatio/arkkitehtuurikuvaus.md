# Arkkitehtuurikuvaus

## Rakenne

Ohjelmassa on tällä hetkellä kaksi tasoa:

- Käyttöliittymätaso, joka vastaa käyttöliittymälogiikasta ja käyttäjän syötteisiin reagoimisesta
- Palvelutaso, jossa on ohjelman sovelluslogiikka
- Tietokantataso, joka vastaa tallennetusta tiedosta

Lisäksi on olemassa vielä fyysinen taso, jossa sijaitsee mittauslaitteisto. Tätä voidaan kuitenkin simuloida testejä varten sovellustasolla.

## Käyttöliittymä

Käyttöliittymä on tehty tkinterillä ja se sisältää tällä hetkellä vain yhden näkymän, jossa voidaan nähdä tämänhetkinen mittausdata ja mennyt data graafisesti.

Tallennus aloitetaan painamalla Aloita tallennus -painiketta. Tämä avaa uuden .jsonlines-tiedoston. Painamalla Lopeta tallennus -painiketta tallennus päättyy.

## Palvelutaso

Alla on kuvattuna luokkakaavio, josta näkyy sovelluslogiikan sijoittuminen ohjelmassa.

![image](https://yuml.me/79ccc140.jpg)

## Tietokantataso

Titokantatasolle päästään Saverista, jossa tallennetaan tiedot .jsonlines-tiedostoksi. Tallennuksen aloittaminen aloittaa tallennuksen tiedostoon, josta tiedot on myöhemmin haettavissa.

<img width="499" alt="tallennus" src="https://user-images.githubusercontent.com/80920371/117047883-08e6d580-ad1b-11eb-94a9-a22b7216fc1a.png">

Juuren valmistumista analysoidaan analyser.py-tiedoston tilakoneessa (StateMachine), joka kyselee keskihajontaa, keskiarvoa ja kulmakerrointa luokilta.

<img width="1022" alt="analysointi" src="https://user-images.githubusercontent.com/80920371/118409260-3116f280-b692-11eb-875c-3613cebdca29.png">


## Päätoiminnallisuudet

Tämänhetkisten tietojen katselu sekä tallennus. Hälytyksen saaminen, kun juuri on saavuttanut huippupisteensä.

## Ohjelman rakenteen heikkoudet

Analysointi ei ole välttämättä sataprosenttisen varma, mikäli olosuhteet ovat hyvin vaihtelevat.
