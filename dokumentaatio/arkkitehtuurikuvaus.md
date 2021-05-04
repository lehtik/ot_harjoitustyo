# Arkkitehtuurikuvaus

## Rakenne

Ohjelmassa on tällä hetkellä kaksi tasoa:

- Käyttöliittymätaso, joka vastaa käyttöliittymälogiikasta ja käyttäjän syötteisiin reagoimisesta
- Palvelutaso, jossa on ohjelman sovelluslogiikka
- Tietokantataso, joka vastaa tallennetusta tiedosta

Lisäksi on olemassa vielä fyysinen taso, jossa sijaitsee mittauslaitteisto. Tätä voidaan kuitenkin simuloida testejä varten sovellustasolla.

## Käyttöliittymä

Käyttöliittymä on tehty tkinterillä ja se sisältää tällä hetkellä vain yhden näkymän, jossa voidaan nähdä tämänhetkinen mittausdata ja mennyt data grafisesti.

Myöhemmin tätä tietoa voidaan myös tallentaa ja sitä varten toteutetaan painike.

## Palvelutaso

Alla on kuvattuna luokkakaavio, josta näkyy sovelluslogiikan sijoittuminen ohjelmassa.

![image](https://user-images.githubusercontent.com/80920371/117047015-0b94fb00-ad1a-11eb-81b5-dd43eb2816bc.png)

## Tietokantataso

Titokantatasolle päästään Saverista, jossa tallennetaan tiedot .jsonlines-tiedostoksi.

<img width="499" alt="image" src="https://user-images.githubusercontent.com/80920371/117047883-08e6d580-ad1b-11eb-94a9-a22b7216fc1a.png">

## Päätoiminnallisuudet

Tämänhetkisten tietojen katselu sekä tallennus. Myöhemmin tulossa hälytys kun pinnamittaus on korkeimmillaan.

## Ohjelman rakenteen heikkoudet

Vaikeaa toteuttaa käytännössä pinnanmittauksen korkeinta kohtaa.
