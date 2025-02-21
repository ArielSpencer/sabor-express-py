import os

restaurants = []

def display_logo():
    print('*************')
    print('⟆Ꭿᑲ𝖮ᖇ ᕮⲭᕈᖇ∈⟆⟆')
    print('*************\n')

def display_options_menu():
    print('1. Cadastrar Restaurante')
    print('2. Listar Restaurantes')
    print('3. Alterar Status do Restaurante')
    print('4. Sair')

def display_subtitle(text):
    os.system('clear')
    print(f'{text}\n')

def back_to_menu():
    input('\nDigite "Enter" para voltar ao menu principal. ')
    main()

def register_restaurant():
    display_subtitle('Cadastrar Restaurante')

    restaurant_name = input('Digite o nome do restaurante: ')
    category_restaurant = input('Digite a categoria do restaurante: ')

    data_restaurant = {'nome': restaurant_name, 'categoria': category_restaurant, 'ativo': False}
    restaurants.append(data_restaurant)

    print(f'Restaurante {restaurant_name} cadastrado com sucesso!')

    back_to_menu()

def list_restaurants():
    display_subtitle('Listar Restaurantes')

    for restaurant in restaurants:
        name_restaurant = restaurant['nome']
        category_restaurant = restaurant['categoria']
        status_restaurant = 'Ativo' if restaurant['ativo'] else 'Inativo'
        print(f'- Restaurante: {name_restaurant} | Categoria: {category_restaurant} | Status: {status_restaurant}')
    
    back_to_menu()

def change_status_restaurant():
    display_subtitle('Alterar Status do Restaurante')

    restaurant_name = input('Digite o nome do restaurante que deseja alterar o status: ')
    restaurant_found = False

    for restaurant in restaurants:
        if restaurant_name == restaurant['nome']:
            restaurant_found = True
            restaurant['ativo'] = not restaurant['ativo']
            status_message = f'O restaurante {restaurant_name} foi ativado com sucesso.' if restaurant['ativo'] else f'O restaurante {restaurant_name} foi desativado com sucesso.'
            print(status_message)

    if not restaurant_found:
        print(f'Restaurante {restaurant_name} não encontrado.')

    back_to_menu()

def exit_program():
    display_subtitle('Programa finalizado!')

def invalid_option():
    print('Opção inválida!')
    back_to_menu()

def chosen_menu_option():
    try:
        chosen_option = int(input('\nEscolha uma opção: '))

        if chosen_option == 1:
            register_restaurant()
        elif chosen_option == 2:
            list_restaurants()
        elif chosen_option == 3:
            change_status_restaurant()
        elif chosen_option == 4:
            exit_program()
        else:
            invalid_option()      
    except:
        invalid_option() 

def main():
    os.system('clear')
    display_logo()
    display_options_menu()
    chosen_menu_option()

if __name__ == '__main__':
    main()
