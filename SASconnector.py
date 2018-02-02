import swat

host = 'https://Flightplanner-forefront.saasnow.com:8443'
port_number = "5570"
user = "stefan.ekstrom"
password = "Forefront_1"

conn = swat.CAS(host, username=user, password=password)
print(conn.serverstatus())
conn.close()
print(conn.serverstatus())
# SKAPA EN REQUEST MOT REST ISTÄLLET!!!
