#Aluno: José Gabriel Gouveia dos Santos Silva
#Matricula: 002-021675
#Curso: Sistemas de Informação
import numpy as np
Atendente1=[]
Atendente2=[]
Atendente3=[]
Atendente4=[]
Tempo1=[]
Tempo2=[]
Tempo3=[]
Tempo4=[]

#Aqui botamos um randomizador do numero de clientes dentro de um periodo de 1 hora, chegam entre 3 e 11 clientes por minuto
ClienteEm1Hora= np.random.randint(3,12,60)

#Aqui calculamos o total de clientes que chegaram nessa uma hora
totalClientes=sum(ClienteEm1Hora)



#Mostramos na tela quantos clientes chegaram em uma hora
print("Total de Clientes:",totalClientes)

#Aqui dividimos os clientes em filas, são 4 atendentes para clientes dentro de uma hora após sua chegada
for i in ClienteEm1Hora:
  if len(Atendente1) < 15:
    Atendente1.append(i)

  elif len(Atendente2) < 15:
    Atendente2.append(i)

  elif len(Atendente3) < 15:
    Atendente3.append(i)

  elif len(Atendente4) < 15:
    Atendente4.append(i)

#Aqui calcularemos o tempo de espera de cada fila 
for tempo1 in Atendente1:
  Tempo1 = sum(np.random.randint(3,12,sum(Atendente1)))

for tempo2 in Atendente1:
  Tempo2 = sum(np.random.randint(3,12,sum(Atendente2)))

for tempo3 in Atendente1:
  Tempo3  =sum(np.random.randint(3,12,sum(Atendente3)))

for tempo4 in Atendente1:
  Tempo4=sum(np.random.randint(3,12,sum(Atendente4)))    
    
print("\nTempo de espera da primeira fila",round(Tempo1/60,1),"minutos")

print("\nTempo de espera da segunda fila",round(Tempo2/60,1),"minutos")

print("\nTempo de espera da terceira fila",round(Tempo3/60,1),"minutos")

print("\nTempo de espera da quarta fila",round(Tempo4/60,1),"minutos")

print("\nNumero de clientes que ficaram na fila 1:",Atendente1, "\n Soma total:", sum(Atendente1))
print("\nNumero de clientes que ficaram na fila 2:",Atendente2, "\n Soma total:", sum(Atendente2)) 
print("\nNumero de clientes que ficaram na fila 3:",Atendente3, "\n Soma total:", sum(Atendente3))
print("\nNumero de clientes que ficaram na fila 4:",Atendente4, "\n Soma total:", sum(Atendente4))