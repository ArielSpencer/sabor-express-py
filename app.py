import os

def display_logo():
    print('*************')
    print('⟆Ꭿᑲ𝖮ᖇ ᕮⲭᕈᖇ∈⟆⟆')
    print('*************')

def display_options_menu():
    print('1. Cadastrar Restaurante')
    print('2. Listar Restaurantes')
    print('3. Ativar Restaurante')
    print('4. Sair\n')

def register_restaurant():
    os.system('clear')
    print('Cadastrar Restaurante')

def list_restaurants():
    os.system('clear')
    print('Listar Restaurantes')

def activate_restaurant():
    os.system('clear')
    print('Ativar Restaurante')

def exit_program():
    os.system('clear')
    print('\nPrograma finalizado!')

def chosen_menu_option():
    chosen_option = int(input('\nEscolha uma opção: '))

    if chosen_option == 1:
        register_restaurant()
    elif chosen_option == 2:
        list_restaurants()
    elif chosen_option == 3:
        activate_restaurant()
    elif chosen_option == 4:
        exit_program()
    else:
        os.system('clear')
        print(f'{chosen_option} é uma opção inválida! Digite um número entre 1 e 4.')
        display_options_menu()
        chosen_menu_option()

def main():
    os.system('clear')
    display_logo()
    display_options_menu()
    chosen_menu_option()

if __name__ == '__main__':
    main()
    