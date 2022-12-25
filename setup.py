import os
import sys
import time
import requests
import argparse
import subprocess


parse = argparse.ArgumentParser();
parse.add_argument("-d", '--direccion', help="direccion example: http://127.0.0.1")
parse.add_argument("-w", "--wordlist", help="ruta del wordlist")
args = parse.parse_args()


def funtion_presentation():
	try:
		subprocess.run(["cat", "./banner/banner.txt"])
	except OSError:
		print("error al cargar banner")
#res.status_code
def funtion_connect():
	try:
		while True:
			archivo = open(f"{args.wordlist}", "r")
			mainread = archivo.readlines()
			for x in mainread:
				more = x.strip()
				res = requests.get(args.direccion+more)
				if(res.status_code != 404):
					print(f"{res.status_code} <- response << {more}")
					file = open("./log.txt", "a")
					file.write(f"\n{args.direccion+more}")
					file.close()
				else:
					pass
	except OSError:
		print("error de conexion o al cargar wordlist")


def funtion_verificar():
	try:
		palabra=args.direccion
		palabra=list(palabra)
		verificador1=palabra[0]+palabra[1]+palabra[2]+palabra[3]; # http
		verificador2=palabra[0]+palabra[1]+palabra[2]+palabra[3]+palabra[4]; #https
		if(verificador1=="http" or verificador2=="https"):
			funtion_presentation()
			funtion_connect()
	except OSError:
		print("URL INVALIDA");
def funtion_borrar():
	try:
		subprocess.run(["rm", "-rf", "./log.txt"])
	except OSError:
		print("error al borrar fichero")
while True:
	funtion_borrar()
	funtion_verificar()