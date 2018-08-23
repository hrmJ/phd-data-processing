

# Yleistä

Tässä siis vanhat skriptit, joita tarvitaan, jotta voidaan käsitellä vanhaa
psql-tallennettua conll9-dataa

# Valmisteluja DO:ssa

HUOM! ks. install.sh


# Psql-valmistelu

synkkaa tietokantadumppi palvelimelle: `rsync --progress dumpfile.xx root@012321.123.123213:/tmp/`

JOS käytät valmista cluster backup -dumppia, palauta se ajamalla: `psql -f dumpin_nimi postgres`
(ei toimi: Tai jos käytössä vanhempi psql-versio, niin: `pg_restore -f dumpin_nimi`)

luo  käyttäjä `test_user`, `test_password`


```
CEATE USER test_user WITH PASSWORD 'test_password';
GRANT SELECT, INSERT, UPDATE, DELETE ON ALL TABLES IN SCHEMA public TO test_user;
GRANT ALL PRIVILEGES ON ALL TABLES IN SCHEMA public TO test_user;
GRANT ALL PRIVILEGES ON ALL SEQUENCES IN SCHEMA public TO test_user;
GRANT ALL PRIVILEGES ON ALL FUNCTIONS IN SCHEMA public TO test_user;
GRANT USAGE, SELECT ON SEQUENCE
```

# Syöttö tietokantaan

`python3 database_insertion/simple_insert.py <conllinput> <references> <dbname> <lang> <groupname> <corpus name>`
