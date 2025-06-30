import os

lista_mercado = []

while True:

    menu = input('--Selecione uma opção--\n[A]dicionar [R]emover [V]er [S]air: ').upper()

    if menu == 'A':
        os.system('cls')
        adicionar_lista = input('O que deseja adicionar?: ')
        lista_mercado.append(adicionar_lista)
        os.system('cls')
        print(f'{adicionar_lista} foi adicionado a lista!\n')

    elif menu == 'R':
        if lista_mercado == []:
            os.system('cls')
            print('A lista está vazia!\n')
        else:
            os.system('cls')
            print('--Lista do mercado--')
            for indice, nome in enumerate(lista_mercado):
                print(f'{indice+1} - {nome}')
            print('')
            while True:
                try:
                    remover_lista = int(input('O que desejar remover?: '))
                    nome_removido = lista_mercado[remover_lista-1]
                    del lista_mercado[remover_lista-1]
                    os.system('cls')
                    print(f'{nome_removido} foi removido com sucesso!\n')
                    break
                except ValueError:
                    os.system('cls')
                    print('Por favor digite um número\n')
                except IndexError:
                    os.system('cls')
                    print('Não existe esse número na lista\n')
                except Exception:
                    print('Erro desconhecido')

    elif menu == 'V':
        if lista_mercado == []:
            os.system('cls')
            print('A lista está vazia!\n')
        else:
            os.system('cls')
            print('--Lista do mercado--')
            for indice, nome in enumerate(lista_mercado):
                print(f'{indice+1} - {nome}')
            print('')
    
    elif menu == 'S':
        os.system('cls')
        break

    else:
        os.system('cls')
        print('Essa opção não existe!\n')