# Keskustelusovellus

Sovelluksen tarkoituksena on olla keskustelufoorumi, jossa on erilaisiin aiheisiin liittyviä viestiketjuja. Pääsivulla olisi tarkoitus olla ennalta annetut aihekokonaisuudet, kuten mm. Harrastukset, Kulttuuri, Lemmikit, Ruoka ja juoma, Terveys ja Viihde. Käyttäjän valittua jokin aihekokonaisuuksista, siirrytään tämän aihekokonaisuuden sisälle, jossa ovat käyttäjien luomat viestiketjut. Näitä viestiketjuja käyttäjät pääsevät sitten kommentoimaan tai halutessaan luomaan uusia.

## Sovelluksen nykystatus
Sovellus on edelleen kesken, projekti toimii paikallisesti. Herokussa se ei jostain syystä pyöri oikein ja tunnista muita sivuja. Herokussa tulee jostain syystä jokin tietokantavirhe.

## Käyttäjän luonti ja sisäänkirjautuminen
Ensin tulee luoda tunnus ja tälle salasana sekä valita missä roolissa ohjelmaa käytetään, käyttäjänä vai ylläpitäjänä.
Onnistuneen käyttäjätunnuksen luomisen jälkeen henkilö voi kirjautua sisään.
Mikäli käyttäjätunnus on varattu, tästä nousee käyttäjälle ilmoitus.

## Käyttäjäroolit
### Käyttäjä
- Sisäänkirjautumisen jälkeen käyttäjällä on oikeus valita minkä aihekokonaisuuden viestiketjuja haluaa mennä katsomaan ja kirjoittamaan. Mikäli ylläpitäjä on antanut erityisen oikeuden käyttäjälle tiettyyn ns. salaiseen aihekokonaisuuteen, näkyy tämä aihekokonaisuus myös käyttäjällä ja tällöin käyttäjällä on oikeus kommentoida ja luoda uusia viestiketjuja.
- Käyttäjä voi muokata omia viestejään tai poistaa näitä. Käyttäjällä on myös oikeus poistaa luomansa viestiketju.
- Käyttäjällä on oikeus aloittaa uusi keskustelu aihekokonaisuuden sisällä sekä myös vastata muiden käyttäjien aloittamiin viestiketjuihin.
- Käyttäjä näkee jokaisen aihekokonaisuuden sivulta omat lähetettyjen viestien määrän sekä viimeisimmän viestin lähetysajankohdan. Ns. pääsivulla käyttäjä näkee lähettämiensä viestien kokonaismäärän ja viimeisimmän viestin lähetysajankohdan.
- Pystyy kirjautumaan ulos.

### Ylläpitäjä
- Sisäänkirjautumisen jälkeen ylläpitäjä voi kirjoittaa samalla tavalla viestiketjuihin kuten käyttäjäkin. Myös tiedot lähetetyistä viesteistä ja viimeisimmän viestin lähetysajankohdasta ovat kuten käyttäjälläkin.
- Ylläpitäjällä on oikeus luoda uusia aihekokonaisuuksia sekä luoda uusia viestiketjuja aihekokonaisuuksien sisälle.
- Ylläpitäjä voi poistaa sekä omia että muiden käyttäjien viestiketjuja.
- Ylläpitäjä voi luoda salaisen aihekokonaisuuden, joka näkyy kaikille ylläpitäjille sekä niille käyttäjille, joille on annettu oikeus tähän.
- Pystyy kirjautumaan ulos.


Web-sovelluksen teko on osa Helsingin yliopiston Tietojenkäsittelytieteen Tietokantasovellus-harjoitustyötä.

