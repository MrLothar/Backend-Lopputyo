# PelaajaAPI

## Yleistä

Tämä on PelaajaAPI, joka on suunniteltu pelaajan edistymisen seurantaan. API tarjoaa rajattuja toiminnallisuuksia erilaisten tietojen hakemiseen ja muokkaamiseen. Sovellus on testattu käyttäen Python versiota 3.12.2.

## Mahdolliset tietopyynnöt:

- Saat kaikkien pelaajien nimet ja id:t.
- Voit hakea yksittäisen pelaajan kaikki tiedot.
- Pääset käsiksi yksittäisen pelaajan kaikkiin tapahtumiin.
- Voit etsiä yksittäisen pelaajan tietyn tyyppiset tapahtumat.
- Saat kaikki järjestelmässä olevat tapahtumat.
- Voit etsiä kaikki järjestelmässä olevat tietyn tyyppiset tapahtumat.
- Voit luoda uuden pelaajan.
- Voit tallentaa pelaajalle uusia tapahtumia.

## Käynnistysohjeet/Virtuaaliympäristön asennus:

Avaa kansio (APP) Visual Studio Codessa ja avaa Command Palette (Ctrl+Shift+P). Kirjoita hakukenttään "Venv" ja valitse (viimeisin ehdotus) asennettu Python versio.

### Ympäristön asennus

#### Asenna tarvittavat kirjastot ajamalla seuraavat komennot terminaalissa:

pip install fastapi

pip install "uvicorn[standard]"

cd app

### Käynnistä sovellus seuraavalla komennolla:

uvicorn main:app --reload

## Nauti!



