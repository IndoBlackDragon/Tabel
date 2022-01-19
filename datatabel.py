from os import system as sy; sy("clear")
from inquirer import *
import re

nama = "nama"
kelas = "Kelas"
umur = "umur"

data_nama = []
data_kelas = []
data_umur = []

def main():

	pilihan =""
	while True:
		while pilihan != "0":
			print (15*"=","INPUT DATA",15*"=")
#			print ("1. ADD DATA")
#			print ("2. SHOW DATA")
#			print ("0. Exit")
			choc = ["1. ADD DATA",
				"2. SHOW DATA",
				"3. REMOVE DATA",
				"0. Exit"
				]
			pilihans = [List("choices",
					message="input ",
					choices=choc
					)
				]
			pilihan = prompt(pilihans)
			def hehe():
				global names,clas,ages,data_kelas,data_kelas,data_umur
				names = input("nama = ")
				clas = input("kelas = ")
				ages = input("umur = ")
				data_nama.append(names)
				data_kelas.append(clas)
				data_umur.append(ages)

			def okelah():
				global data_nama,data_kelas,data_umur
				data_nama = data_nama
				data_kelas = data_kelas
				data_umur = data_umur
			if re.findall(r'0',pilihan["choices"]): print ("\nbye byw\n");exit()
			elif re.findall(r"2",pilihan["choices"]): break
			elif re.findall(r"3",pilihan["choices"]):
				try:
					hapus = int(input('hapus data ke - '))
					data_nama.pop(hapus-1)
					data_kelas.pop(hapus-1)
					data_umur.pop(hapus-1)
				except ValueError:
					print ("\nmasukkan hanya angka\n")
				except IndexError:
					print ("\nData empty")
			elif re.findall(r'1',pilihan["choices"]): hehe();okelah()
			print ("")
#	nama = dict(zip(nama,[data_nama]))
#	kelas = dict(zip(nama,[data_kelas]))
#	umur = dict(zip(nama,[data_umur]))
		okelah()
		daftar = {}
		daftar[nama] = data_nama
		daftar[kelas] = data_kelas
		daftar[umur] = data_umur
		from tabulate import tabulate as tab
		table = tab(daftar,
			headers="keys",
			tablefmt="fancy_grid",
			showindex=range(1,len(data_nama)+1)
			)
		print (table,"\n")
#	while pilihan != "0":
#		print (15*"=","INPUT DATA",15*",")
#		print ("1. ADD DATA")
#		print ("2. SHOW DATA")
#		print ("0. Exit")
#		pilihan = input("\npilih >> ")
#		datas.append(pilihan)
#		names = input("nama = ")
#		data_nama.append(names)
#		clas = input("kelas = ")
#		data_kelas.append(clas)
#		ages = input("umur = ")
#		data_umur.append(ages)
#		if pilihan=="0": exit()
#		elif pilihan=="2": break
#	print (table)


main()
