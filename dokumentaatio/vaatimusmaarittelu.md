# Vaatimusmäärittely
Tämä vaatimusmäärittely koskee WatchDough-sovellusta.

## Sovelluksen tarkoitus

WatchDough on hapanjuuren leipomisvalmiutta tarkkaileva sovellus.

Hapanjuuren leipomisvalmiutta voi olla hankala määrittää silmämääräisesti, mutta jatkuvasti mitattavalla ultraäänianturilla saadaan suhteellisen tarkkaa tietoa siitä, milloin juuri on valmiina käyttöön eli on kasvattanut tilavuuttaan noin kaksinkertaiseksi ja saavuttaa korkeimman kohtansa. 

Juurenkohotuksessa hapanjuurta kasvatetaan leivontavalmiiksi n. 6 tuntia kestävässä nostatuksessa purkissa. Oikealla ajoituksella on suuri merkitys leipomisen lopputulokseen.

Sovelluksella käyttäjä voi tarkkailla juuren leipomisvalmiutta, lämpötilaa ja ilmankosteutta graafien avulla ja saada ilmoitus juuren ollessa valmis. Sovelluksen käyttäminen juurenkohotuksen tarkkailuun vaatii luonnollisesti fyysisen laitteiston, mutta tarkoituksena on lisätä mukaan simulaattori, jolla voidaan testata mahdollista lopputulosta tietyillä lähtöparametreilla.

## Käyttäjäroolit:

Lopullisessa sovelluksessa on ainoastaan normaali käyttäjä.

<br>

## Käyttöliittymäluonnos

Sovelluksen näkymä on lähes samanlainen kaikille käyttäjille.

<font color=red>Tähän kuva</font>

Sovellus aukeaa suoraan valikkoon, josta voi valita uuden juurenkohotuksen aloittamisen tai uloskirjautumisen. Myöhemmin valikkoon lisätään myös juurihistoriatietojen katsominen sekä simulaattori. Kehittäjä-statuksella olevat käyttäjät näkevät myöhemmin tässä painikkeen statistiikan katsomiseen.

## Perusversion toiminnallisuudet

### Normaalien käyttäjien toiminnallisuudet

- Käyttäjä voi aloittaa uuden juurenkohotuksen tarkkailun.
    - Juurenkohotuksen käynnistyessä aloitetaan ilmankosteuden, lämpötilan ja juuren korkeuden tarkkailu.
    - Mittaus toteutetaan fyysisellä laitteistolla, joka on kuvattu erillisessä <font color="red">dokumentissa (linkitetään myöhemmin)</font>.
- Käyttäjä saa ilmoituksen, kun juuren korkeus saavuttaa huippupisteensä.
- Käyttäjä voi pysäyttää juurenkohotuksen tarkkailun sovelluksessa.

#### **Jatkokehitysideoita**

Tarkoituksena on lisätä ainakin seuraavat toiminnallisuudet kehityksen myötä:

- Käyttäjä voi asettaa ilmoituksen, kun lämpötila ylittää tai alittaa vapaavalintaisen arvon
- Käyttäjä voi asettaa ilmoituksen, kun ilmankosteus ylittää tai alittaa vapaavalintaisen arvon
- Käyttäjä voi halutessaan tallentaa kohotuksen lopuksi tiedot juurihistoriaansa.
- Käyttäjä voi tarkastella juurihistoriaansa.
    - Historiatietoihin kuuluu päivämäärä sekä ilmankosteus-, lämpötila- ja korkeuskuvaajat.
- Käyttäjä voi simuloida kohotusta ja saada tietoja arvioidusta kohotusajasta antamalla lähtöparametriksi lämpötilan. Simulaatio on summittainen ja se olettaa juuren olevan ruokittu tietyllä suhteella ja ilmankosteuden olevan jokin tietty arvo.

### Toimintaympäristön rajoitteet
- Ohjelmiston tulee toimia Linux- ja OSX-käyttöjärjestelmillä varustetuissa koneissa.
- Käyttäjien ja todojen tiedot talletetaan paikallisen koneen levylle.