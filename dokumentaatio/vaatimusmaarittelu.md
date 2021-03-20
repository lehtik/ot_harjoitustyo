<body style=text-align:justify>

# Vaatimusmäärittely
<font face="Arial">Tämä vaatimusmäärittely koskee WatchDough-sovellusta.

## Sovelluksen tarkoitus

---

WatchDough on hapanjuuren leipomisvalmiutta tarkkaileva sovellus.

Hapanjuuren leipomisvalmiutta voi olla hankala määrittää silmämääräisesti, mutta jatkuvasti mitattavalla ultraäänianturilla saadaan suhteellisen tarkkaa tietoa siitä, milloin juuri on valmiina käyttöön eli on kasvattanut tilavuuttaan noin kaksinkertaiseksi ja saavuttaa korkeimman kohtansa. 

Juurenkohotuksessa hapanjuurta kasvatetaan leivontavalmiiksi n. 6 tuntia kestävässä nostatuksessa purkissa. Oikealla ajoituksella on suuri merkitys leipomisen lopputulokseen.

Sovelluksella käyttäjä voi tarkkailla juuren leipomisvalmiutta, lämpötilaa ja ilmankosteutta graafien avulla ja saada ilmoitus juuren ollessa valmis. Sovelluksen käyttäminen juurenkohotuksen tarkkailuun vaatii luonnollisesti fyysisen laitteiston, mutta tarkoituksena on lisätä mukaan simulaattori, jolla voidaan testata mahdollista lopputulosta tietyillä lähtöparametreilla.

## Käyttäjäroolit:
---
Lopullisessa sovelluksessa on ainoastaan normaali käyttäjä. Myöhemmin lisätään mahdollisuus valita suuremmilla oikeuksilla varustettu kehittäjän rooli.

<br>

## Käyttöliittymäluonnos
---
Sovelluksen näkymä on lähes samanlainen kaikille käyttäjille. Kehittäjä-statuksella olevat käyttäjät näkevät lisäksi pääsyn statistiikkaan.

<font color=red>Tähän kuva</font>

Sovellus aukeaa kirjautumisnäkymään, jossa voi joko kirjautua olemassa olevilla kredentiaaleilla (käyttäjänimi ja salasana) sisään tai vaihtoehtoisesti luoda uusi tunnus. Ohjelman käyttöä varten on kirjauduttava sisään.

Sisäänkirjautumisen jälkeen normaali käyttäjä näkee valikon, josta voi valita uuden juurenkohotuksen aloittamisen tai uloskirjautumisen. Myöhemmin valikkoon lisätään myös juurihistoriatietojen katsominen sekä simulaattori. Kehittäjä-statuksella olevat käyttäjät näkevät myöhemmin tässä painikkeen statistiikan katsomiseen.

## Perusversion toiminnallisuudet
---
### Normaalien käyttäjien toiminnallisuudet

#### **Ennen kirjautumista**

- Käyttäjä voi luoda henkilökohtaisen käyttäjätunnuksen järjestelmään, jolla hän voi kirjautua salasanan avulla sisään.
    - Ohjelman käyttämistä varten on kirjauduttava sisään.
    - Käyttäjätunnuksen on oltava uniikki ja vähintään 3 kirjainta tai numeroa pitkä.
    - Salasanan on oltava vähintään 8 merkkiä pitkä ja sen on sisällytettävä vähintään yksi numero ja yksi kirjain.
- Jos kirjautumisessa yritetty käyttäjätunnus tai salasana on väärä, tulee tästä ilmoitus.

#### **Kirjautumisen jälkeen**

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

</font>
</body>