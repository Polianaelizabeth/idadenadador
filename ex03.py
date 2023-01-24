idade = int(input("Qual a idade do nadador? "))

if idade < 5:
    print("Infelizmente, não temos categoria para essa idade.")
elif 5 <= idade <= 7:
    print("Categoria infantil.")
elif 8 <= idade <= 10:
    print("Categoria juvenil.")
elif 11 <= idade <= 15:
    print("Categoria adolescente.")
elif 16 <= idade <= 30:
    print("Categoria adulto.")
else:
    print("categoria sênior")