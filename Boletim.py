import sys

#Iserir notas dos alunos

def insere_nota():
	
	global aluno
	aluno = input("\nNome: ")
	global soma
	soma = int(input("\nPortuguês: "))
	soma = soma + int(input("Matematica: "))
	soma = soma + int(input("História: "))
	soma = soma + int(input("Geografia: "))
	soma = soma + int(input("Fisica: "))
	soma = soma + int(input("Quimica: "))
	soma = soma + int(input("Biologia: "))
	soma = soma + int(input("Artes: "))
	soma = soma + int(input("Ed. Fisica: "))
	soma = soma + int(input("Inglês: "))
	soma = soma + int(input("Filosofia: "))
	soma = soma + int(input("Sociologia: "))

#Soma notas e divide

def soma_nota():
	global nota
	nota = soma // 12

#Mostra nota final

def mostra_nota():
	print("\nA nota final do aluno {} foi {}.\n".format(aluno, nota))

	if nota >= 5:
		print("O aluno foi aprovado!\n")
	else:
		print("O aluno foi reprovado!\n")

def continua():
	insere_nota()
	soma_nota()
	mostra_nota()		

def final():
	resposta = input("Somar nota de mais algum aluno? Sim ou Nao: ")
	if resposta == 'sim':
		continua()
	else:
		print("Adeus")
		sys.exit(0)

insere_nota()
soma_nota()
mostra_nota()
final()



