def calculadora():
    while True:
        try:
            primeiro_digito = float(input("Insira um número: "))
            segundo_digito = float(input("Insira outro número: "))
            tipo_operacao = input("Insira o tipo de operação (+, -, x, /): ").strip()

            if tipo_operacao == "+":
                print(f"Resultado: {primeiro_digito + segundo_digito}")
            elif tipo_operacao == "-":
                print(f"Resultado: {primeiro_digito - segundo_digito}")
            elif tipo_operacao == "x":
                print(f"Resultado: {primeiro_digito * segundo_digito}")
            elif tipo_operacao == "/":
                if segundo_digito == 0:
                    print("Erro: Divisão por zero não é permitida.")
                else:
                    print(f"Resultado: {primeiro_digito / segundo_digito}")
            else:
                print("Operação inválida. Tente novamente.")
                continue

            escolha = input("Deseja realizar outra operação? (S/N): ").strip().upper()
            if escolha == "N":
                print("Encerrando a calculadora. Até logo!")
                break
            else:
                print("Digite S ou N: ")
        except ValueError:
            print("Entrada inválida. Certifique-se de digitar números corretamente.")
        except Exception as e:
            print(f"Ocorreu um erro inesperado: {e}. Tente novamente.")

calculadora()
