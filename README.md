# WatchDough

Sovelluksella voit seurata hapanjuuren leipomisvalmiutta. Kun juuri on valmis leivontaan, saat hälytyksen sovelluksesta. Voit myös tarkkailla kosteutta ja lämpötilaa, joilla on suuri vaikutus juuren toimintaan.

## Anturin valinta

Voit valita joko oikean anturin (R1) tai virtuaalianturin (DEV). Virtuaalinen anturi on aina käytettävissä, ja se tuottaa satunnaista mittausdatalta näyttävää dataa.

## Python-versio

Käytä vähintään `Python 3.6`.

## Dokumentaatio

[Vaatimusmäärittely](dokumentaatio/vaatimusmaarittely.md)

[Tyoaikakirjanpito](dokumentaatio/tyoaikakirjanpito.txt)

... lisää tulossa ...

## Asennus

Asenna riippuvuudet komennolla `poetry install`.

Suorita alustustoimenpiteet: `poetry run invoke build`

Käynnistä sovellus `poetry run invoke start`

## Komentorivitoiminnot

### Ohjelman suorittaminen

Ohjelman suorittaminen `poetry run invoke start`

### Testaus

`poetry run invoke test`

### Testikattavuus

`poetry run invoke coverage-report`

Raportti generoituu htmlcolv-hakemistoon.
