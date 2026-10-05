def calcular_desconto(valor_compra, tipo_cliente):
    if valor_compra < 0:
        raise ValueError("Valor da compra não pode ser negativo")

    desconto = 0


    if valor_compra >= 100 and valor_compra < 500:
        desconto = 0.10
    elif valor_compra >= 500:
        desconto = 0.20

    
    if tipo_cliente.upper() == "VIP":
        desconto += 0.05

    valor_desconto = valor_compra * desconto

  
    if valor_desconto > 200:
        valor_desconto = 200

    return round(valor_desconto, 2)