class NameCard:
    def print_info(self, name):
        print(name)

    def __enter__(self):
        print('enter')
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('exit')
        return self

    def __del__(self):
        print('del')
        return self

with NameCard() as name_card:
    name_card.print_info('한동석')