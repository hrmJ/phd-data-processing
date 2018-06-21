# Yleistä

Tässä siis vanhat skriptit, joita tarvitaan, jotta voidaan käsitellä vanhaa
psql-tallennettua conll9-dataa

# Riippuvuuksia


```
#Universe-repo käyttöön
sudo apt-get install software-properties-common
sudo apt-add-repository universe
sudo apt-get update
```

apt install python3-psycopg2
apt install python3-lxml
apt install python3-sqlalchemy

pip3 install progress
pip3 install termcolor
pip3 install bs4

# Psql-valmistelu

```
CREATE USER test_user WITH PASSWORD 'test_password';
GRANT SELECT, INSERT, UPDATE, DELETE ON ALL TABLES IN SCHEMA public TO test_user;
GRANT ALL PRIVILEGES ON ALL TABLES IN SCHEMA public TO test_user;
GRANT ALL PRIVILEGES ON ALL SEQUENCES IN SCHEMA public TO test_user;
GRANT ALL PRIVILEGES ON ALL FUNCTIONS IN SCHEMA public TO test_user;
```
