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

Luokkakaavio tulossa.

## Tietokantataso

Sekvenssikaavio tulossa.

## Päätoiminnallisuudet

Tämänhetkisten tietojen katselu sekä tallennus. Myöhemmin tulossa hälytys kun pinnamittaus on korkeimmillaan.

## Ohjelman rakenteen heikkoudet

Vaikeaa toteuttaa käytännössä pinnanmittauksen korkeinta kohtaa.
