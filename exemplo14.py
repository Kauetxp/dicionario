students = {
    "João":{
        'idade':18,
        'cidade':"Sao Paulo",
        'notas':[7.5,8.0,9.0]
    },
    "Maria":{
        'idade':20,
        'cidade':"Rio de Janeiro",
        'notas':[7.5,10.0,5.0]
    },
    "Pedro":{
        'idade':19,
        'cidade':"Belo Horizonte",
        'notas':[7.5,9.0,9.5]
    }
}
#Imprimir a idade do joão

print("A Idade de João é:"+str(students["João"]["idade"]))

#Adicionar uma nota para Maria

students["Maria"]["notas"].append(9.0)

#Imprimir todas as informações dos alunos

for student, info in students.items():
    print(student + ":")
    print("Idade: "+ str(info['idade']))
    print("Cidade: "+ str(info['cidade']))
    print("Notas: "+ str(info['notas']))
    print("Média: "+ str(sum(info['notas'])/len(info['notas'])))
    
    