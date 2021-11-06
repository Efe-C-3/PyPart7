from typing import Dict

lang_dict = {1: 'English',
             2: 'Spanish',
             }

modes_to_select = {1: 'User',
                   2: 'Admin'
                   }

support_to_select = {1: 'Add new language',
                     2: 'Update existing greeting'
                     }


def print_language_options(lang_options: Dict[int, str]) -> None:
    print('Please choose a language: ')
    for key in sorted(lang_options):
        print('{0}: {1}'.format(key, lang_options[key]))


def language_input() -> int:
    return int(input())


def language_choice_is_valid(lang_options: Dict[int, str], lang_choice: int) -> bool:
    validation = lang_choice in lang_options
    return validation


"""================================================================================"""


def set_user_mode_with_input(mode_options):
    print("Choose one: Admin or User")
    for key in sorted(mode_options):
        print('{0}: {1}'.format(key, mode_options[key]))


def mode_input():
    return int(input())


def mode_choice_is_valid(mode_options: Dict[int, str], mode_choice: int) -> bool:
    validation = mode_choice in mode_options
    return validation


"""================================================================================"""


def set_support_option(support_options):
    print("Choose one: Add language or Update language")
    for key in sorted(support_options):
        print('{0}: {1}'.format(key, support_options[key]))


def support_input():
    return int(input())


def support_choice_is_valid(support_options: Dict[int, str], support_choice: int) -> bool:
    validation = support_choice in support_options
    return validation


"""================================================================================"""

def get_additional_language_input():
    return 'What is the new language you want to add?'


def additional_language_input(name_prompt):
    response = input(name_prompt)
    return response


def greeting_for_additional_language(response):
    print(f'{response} is added')


"""================================================================================"""


def updated_language_prompt():
    return 'What language do you want to update?'


def updated_language_input(update_language):
    response_for_language = input(update_language)
    return response_for_language


def updated_prompt():
    return 'What is the new greeting?'


def updated_greeting(response_for_greeting):
    updated_response_for_greeting = input(response_for_greeting)
    print(f'The greeting is updated as "{updated_response_for_greeting}"')


if __name__ == '__main__':
    set_user_mode_with_input(modes_to_select)
    chosen_mode = mode_input()
    while mode_choice_is_valid(modes_to_select, chosen_mode) is False:
        print("Invalid selection. Try again.")
        chosen_mode = mode_input()

    set_support_option(support_to_select)
    chosen_support = support_input()
    while support_choice_is_valid(support_to_select, chosen_support) is False:
        print("Invalid selection. Try again.")
        chosen_support = support_input()

    if chosen_support == 1:
        selected_additional_language_prompt = f"{get_additional_language_input()} \n"
        chosen_additional_language= additional_language_input(selected_additional_language_prompt)
        greeting_for_additional_language(chosen_additional_language)

    elif chosen_support ==2:
        selected_update_language_prompt = f"{updated_language_prompt()} \n"
        chosen_update_language = updated_language_input(selected_update_language_prompt)
        selected_greeting = f"{updated_prompt()} \n"
        updated_greeting(selected_greeting)

    else:
        print("Invalid selection.")

