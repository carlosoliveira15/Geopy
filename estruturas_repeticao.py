import pandas as pd

option = -1
saldo_atual = 1800.

index = ["0", "1", "2", "3"]

data = pd.Series(dict(zip(index, ["01-05-2024", "02-05-2024", "02-05-2024", "03-05-2024"])))
nr_doc = pd.Series(dict(zip(index, ["000000", "950900", "422566", "837249"])))
desc = pd.Series(dict(zip(index, ["Saldo anterior", "Transf. recebida", "Pagamento impostos", "Transf. enviada"])))
valor = pd.Series(dict(zip(index, ["", 500.00, -1200.00, -1000.00])))
saldo = pd.Series(dict(zip(index, [3500.00, 4000.00, 2800.00, 1800.00])))

extract = pd.DataFrame({"Data":data,
                        "Número de Doc.":nr_doc,
                        "Descrição":desc,
                        "Valor":valor,
                        "Saldo":saldo
                        })

while option != 0:
    option = int(input("[1] Sacar\n [2] Extrato\n [3] Depositar\n [0] Sair\n"))

    if option == 1:
        saque = float(input(f"Informe o valor do saque: "))
        if saque <= saldo_atual:
            print("Sucesso!")
        else:
            print("Saldo insuficiente!")
    elif option == 2:
        print(extract)
    elif option == 3:
        input("Informe o valor do deposito: ")
    else:
        print("Atendimento Concluído!")