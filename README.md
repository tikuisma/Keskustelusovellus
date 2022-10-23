# Keskustelusovellus

Sovellus [Herokussa](https://tsoha-visitors1.herokuapp.com/login)

Sovelluksen tarkoituksena on olla keskustelufoorumi, jossa on erilaisiin aiheisiin liittyviä viestiketjuja. Pääsivulla on ylläpitäjien luomat teemat, kuten mm. Harrastukset, Kulttuuri, Lemmikit, Ruoka ja juoma, Terveys ja Viihde. Käyttäjän valittua jonkin aihekokonaisuuksista, siirrytään tämän aihekokonaisuuden sisälle. Aihekokonaisuuden sisältä löytyy käyttäjien julkaisemat postaukset. Näitä postauksia/viestiketjuja käyttäjät pääsevät sitten kommentoimaan tai halutessaan luomaan itse uusia.
Sovellus on toteutettu englannin kielisenä.

## Käyttäjän luonti ja sisäänkirjautuminen
Ensin Herokussa tulee luoda käyttäjätunnus ja tälle salasana sekä valita missä roolissa ohjelmaa käytetään, käyttäjänä vai ylläpitäjänä.
Onnistuneen käyttäjätunnuksen luomisen jälkeen henkilö voi kirjautua sisään.
Mikäli käyttäjätunnus on varattu, tästä nousee käyttäjälle ilmoitus. Mikäli salasanan syötössä tulee virhe, tästä ilmoitetaan käyttäjälle.

## Käyttäjäroolit
### Käyttäjä
- Sisäänkirjautumisen jälkeen käyttäjällä on oikeus valita minkä aihekokonaisuuden viestiketjuja hän haluaa mennä katsomaan.
- Käyttäjällä on oikeus tehdä uusi postaus/viestiketju aihekokonaisuuden sisälle sekä myös vastata muiden käyttäjien aloittamiin viestiketjuihin.
- Käyttäjä näkee pääsivulla tekemiensä postauksien ja lähettämiensä kommenttien kokonaismäärän.
- Käyttäjä pystyy antamaan omille sekä muiden postauksille tykkäyksen.
- Käyttäjällä ei ole oikeutta poistaa omia viestejään tai muokata niitä.
- Pystyy kirjautumaan ulos.

### Ylläpitäjä
- Sisäänkirjautumisen jälkeen ylläpitäjä voi kirjoittaa samalla tavalla viestiketjuihin kuten käyttäjäkin. Myös tiedot omista postausten ja kommenttien määristä näkyvät pääsivulla.
- Ylläpitäjällä on oikeus luoda uusia aihekokonaisuuksia sekä luoda uusia viestiketjuja aihekokonaisuuksien sisälle.
- Ylläpitäjä voi poistaa sekä omia että muiden käyttäjien yksittäisiä kommentteja sekä kokonaisia postauksia/viestiketjuja.
- Ylläpitäjä pystyy antamaan tykkäyksen omille sekä muiden postauksille.
- Pystyy kirjautumaan ulos.

### Jatkokehitysideoita
- Käyttäjä pystyisi poistamaan tai muokkaamaan omia postauksia ja kommentteja.
- Palautekanava, johon käyttäjät voisivat laittaa ilmoituksen esimerkiksi kommentista. Tämän palautteen näkisivät sitten ylläpitäjät.
- Ylläpitäjän luominen niin, että kuka vaan ei voi luoda Admin-roolia.


Web-sovelluksen teko on osa Helsingin yliopiston Tietojenkäsittelytieteen Tietokantasovellus-harjoitustyötä.

