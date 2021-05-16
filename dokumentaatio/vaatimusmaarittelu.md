# Vaatimusmäärittely
Tämä vaatimusmäärittely koskee WatchDough-sovellusta.

## Sovelluksen tarkoitus

WatchDough on hapanjuuren leipomisvalmiutta tarkkaileva sovellus.

Hapanjuuren leipomisvalmiutta voi olla hankala määrittää silmämääräisesti, mutta jatkuvasti mitattavalla ultraäänianturilla saadaan suhteellisen tarkkaa tietoa siitä, milloin juuri on valmiina käyttöön eli on kasvattanut tilavuuttaan noin kaksinkertaiseksi ja saavuttaa korkeimman kohtansa. 

Juurenkohotuksessa hapanjuurta kasvatetaan leivontavalmiiksi n. 6 tuntia kestävässä nostatuksessa purkissa. Oikealla ajoituksella on suuri merkitys leipomisen lopputulokseen.

Sovelluksella käyttäjä voi tarkkailla juuren leipomisvalmiutta, lämpötilaa ja ilmankosteutta graafien avulla ja saada ilmoitus juuren ollessa valmis. Sovelluksen käyttäminen juurenkohotuksen tarkkailuun vaatii luonnollisesti fyysisen laitteiston, mutta testausta varten mukaan on lisätty simulaattori, jolla voidaan testata mahdollista lopputulosta satunnaisilla parametreilla.

## Käyttäjäroolit:

 Sovelluksessa on vain normaali käyttäjä.

## Käyttöliittymäluonnos

Sovelluksen näkymä on samanlainen kaikille käyttäjille.

![image](https://user-images.githubusercontent.com/80920371/113039769-b9077280-91a0-11eb-81e3-e99f24eadb49.png)

Sovellus aukeaa suoraan "juuri-dashboardille", josta käyttäjä näkee heti anturin tilanteen. Myöhemmin näkymään lisätään myös painikkeet kohtuksen aloittamiselle ja edellisten kohotustietojen katsomiseen. Juuren kohotuksen aloittamisen jälkeen tähän näkymään avautuu myös graafit (lämpötila, kosteus ja pinnankorkeus).

## Perusversion toiminnallisuudet

### Normaalien käyttäjien toiminnallisuudet

- Käyttäjä voi aloittaa uuden juurenkohotuksen tarkkailun. // TEHTY
    - Juurenkohotuksen käynnistyessä aloitetaan ilmankosteuden, lämpötilan ja juuren korkeuden tarkkailu. // TEHTY
    - Mittaus toteutetaan fyysisellä laitteistolla, kuva alla // TEHTY
- Käyttäjä saa ilmoituksen, kun juuren korkeus saavuttaa huippupisteensä. // TEHTY
- Käyttäjä voi pysäyttää juurenkohotuksen tarkkailun sovelluksessa. // TEHTY

#### **Jatkokehitysideoita**

Tarkoituksena on lisätä ainakin seuraavat toiminnallisuudet kehityksen myötä:

- Käyttäjä voi asettaa ilmoituksen, kun lämpötila ylittää tai alittaa vapaavalintaisen arvon
- Käyttäjä voi asettaa ilmoituksen, kun ilmankosteus ylittää tai alittaa vapaavalintaisen arvon
- Käyttäjä voi halutessaan tallentaa kohotuksen lopuksi tiedot juurihistoriaansa. // TEHTY
- Käyttäjä voi tarkastella juurihistoriaansa.
    - Historiatietoihin kuuluu päivämäärä sekä ilmankosteus-, lämpötila- ja korkeuskuvaajat.
- Käyttäjä voi simuloida kohotusta ja saada tietoja arvioidusta kohotusajasta antamalla lähtöparametriksi lämpötilan. Simulaatio on summittainen ja se olettaa juuren olevan ruokittu tietyllä suhteella ja ilmankosteuden olevan jokin tietty arvo. // Osittain TEHTY, ei lähtöparametreilla.

### Toimintaympäristön rajoitteet
- Ohjelmiston tulee toimia Linux- ja OSX-käyttöjärjestelmillä varustetuissa koneissa.
- Käyttäjien ja todojen tiedot talletetaan paikallisen koneen levylle.
