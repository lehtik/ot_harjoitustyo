# WatchDough

Sovelluksella voit seurata hapanjuuren leipomisvalmiutta. Kun juuri on valmis leivontaan, saat hälytyksen sovelluksesta. Voit myös tarkkailla kosteutta ja lämpötilaa, joilla on suuri vaikutus juuren toimintaan.

## Anturin valinta

Voit valita joko oikean anturin (R1, start_real) tai virtuaalianturin (DEV, start). Virtuaalinen anturi on aina käytettävissä, ja se tuottaa satunnaista mittausdatalta näyttävää dataa.

## Syklien testaus

Juuren kasvu on jaettu sykleihin (kalibrointi, alku, kasvuvaihe ja lopetus). Testimielessä voit säätää analyzer.py-tiedostossa olevaa CALIBRATION_TIME-attribuuttia mielesi mukaan lyhyemmäksi. Oikeaa käyttöä varten suositellaan 300 s (= 5 min) kalibrointiaikaa.

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

Ohjelman suorittaminen virtuaalianturilla `poetry run invoke start`

Ohjelman suorittaminen oikealla anturilla `poetry run invoke start_real`

### Testaus

`poetry run invoke test`

### Testikattavuus

`poetry run invoke coverage-report`

Raportti generoituu htmlcolv-hakemistoon.

### Pylint

Koodin laadun analyysin voi suorittaa komennolla

`poetry run invoke lint`

Analyysissa käytettävät laadun tarkistukset on määritetty tiedostossa .pylintrc
