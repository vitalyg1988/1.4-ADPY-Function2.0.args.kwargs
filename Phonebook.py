#! /usr/bin/env python3


def generation_str(string, max_len):
    start_index = 0
    end_index = max_len
    while end_index <= len(string):
        yield string[start_index: end_index]
        start_index = end_index
        end_index += max_len
    if end_index > len(string):
        yield string[start_index: len(string)]


def adv_print(*args, **kwarg):
    start = kwarg.get('start', '')
    max_line = kwarg.get('max_line', 0)
    in_file = kwarg.get('in_file', False)
    string = start + ','.join([str(arg) for arg in args])
    if max_line:
        temp_str = ''
        for item in generation_str(string, max_line):
            temp_str += f'{item}\n'
        string = temp_str
    if in_file:
        with open('output.txt', 'w', encoding='utf8') as file:
            file.write(string)
    print(string)


class Contact:
    def __init__(self, name, surname, phone_number, favorite=False, **kwargs):
        self.name = name
        self.surname = surname
        self.phone_number = phone_number
        self.favorite = favorite
        self.other_contacts = kwargs

    def __str__(self):
        other_contacts = ''
        for item in self.other_contacts:
            other_contacts += f'\t\t\t{item}: {self.other_contacts[item]}\n'
        favorite = 'нет'
        if self.favorite:
            favorite = 'да'
        return f'Имя: {self.name}\nФамилия: {self.surname}\nТелефон: {self.phone_number}\nВ избранных:{favorite}\n' \
               f'Дополнительная информация:\n' \
               f'{other_contacts}'


class Phonebook:
    def __init__(self, name):
        self.name = name
        self.contact_list = []

    def add_contact(self, *contact):
        for item in contact:
            if type(item) is not Contact:
                raise NotImplementedError('Можно добавлять только записи Contact')
            self.contact_list.append(item)

    def del_contact(self, phone_number):
        for index, contact in enumerate(self.contact_list):
            if phone_number == contact.phone_number:
                del self.contact_list[index]
            else:
                print('Такого номера телефона нет')

    def print_book(self):
        temp_str = ''
        for item in self.contact_list:
            temp_str += f'{item}'
        print(temp_str)

    def find_favorites(self):
        for item in filter(lambda item: item.favorite is True, self.contact_list):
            print(item)

    def find_contact(self, name, surname):
        temp_list = []
        for item in self.contact_list:
            if name == item.name and surname == item.surname:
                temp_list.append(item)
        if not temp_list:
            print('Контакта с таким именем и фамилией нет')
        else:
            for item in temp_list:
                print(item)


if __name__ == '__main__':
    # adv_print('This text is written to test the work advanced print', max_line=10, start='', in_file=True)
    # john = Contact('John', 'Smith', '+71234567809', telegram='@johny', email='johny@smith.com')
    # print(john)
    phone_book1 = Phonebook('phonebook')
    phone_book1.add_contact(Contact('John', 'Smith', '+71234567809', True, telegram='@johny', email='johny@smith.com'),
                            Contact('Steve', 'Smith', '+74585965233', telegram='@steve', email='steve@smith.com'),
                            Contact('Mike', 'Smith', '+7569845552', True, telegram='@mike', email='mike@smith.com'))
    phone_book1.find_favorites()
    # phone_book1.find_contact('Steve', 'Mike')
    # phone_book1.print_book()
