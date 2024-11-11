ponto = [0, 0]
print("Endereço original:", id(ponto))  # Mostra o endereço de memória original

ponto[0] = 10
print("Após modificar conteúdo:", id(ponto))  # O endereço é o mesmo, pois só mudamos o conteúdo

ponto = [69, 72]
print("Após reatribuição:", id(ponto))  # O endereço é diferente, pois criamos um novo objeto


ponto2 = [0,0]
print("Endereço do ponto2: ", id(ponto2))

ponto2.append(3)

print("Endereço do ponnto 2 após modificação: ", id(ponto2))