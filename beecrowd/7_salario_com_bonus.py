nomeVendedor = input()
salarioVendedor = float(input())
montanteVendasVendedor = float(input())

comissaoVendasVendedor = montanteVendasVendedor * 0.15
salarioFinalVendedor = salarioVendedor + comissaoVendasVendedor
print(f"TOTAL = R$ {salarioFinalVendedor:.2f}")