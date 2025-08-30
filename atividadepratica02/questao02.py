nome_produto = "Camiseta"
preco_original = 50.00
porcentagem_desconto = 20


valor_desconto = preco_original * (porcentagem_desconto / 100)
preco_final = preco_original - valor_desconto

print(f"Nome do produto: {nome_produto}")
print(f"Preco original: R$ {preco_original}")
print(f"Porcentagem de desconto: {porcentagem_desconto}%")
print(f"Valor do desconto: R${round(valor_desconto,2)}")
print(f"Preco final: R${round(preco_final,2)}")