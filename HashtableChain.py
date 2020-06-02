from dataclasses import dataclass


@dataclass
class TInfo:
    name: str = ''
    family: str = ''
    phone: str = ''


@dataclass
class SubCell:
    info: TInfo = TInfo(name='', family='', phone='')


class Hash:

    def __init__(self, table_size = 100):
        self.table_size = table_size
        self.info = TInfo()
        self.hash_table = [[SubCell(self.info)] for _ in range(self.table_size)]
        self.step = 1

    def __hash_func(self, value):
        result = 0
        for i in value:
            result += ord(i)
            result %= self.table_size
        return result

    def add_cell(self, info:TInfo):
        adr = self.__hash_func(info.phone)
        i = len(self.hash_table[adr]) - 1
        self.hash_table[adr][i] = SubCell(info=info)
        self.hash_table[adr].append(SubCell(info=TInfo()))

    def del_cell(self, info):
        adr = self.__hash_func(info.phone)
        i = 0
        while self.hash_table[adr][i].info != info:
            i+=1
        del self.hash_table[adr][i]

    def find_cell(self, info):
        adr = self.__hash_func(info.phone)
        i = 0
        while self.hash_table[adr][i].info != info:
            i += 1
        return adr, i

    def out(self):
        out = "{:<6}{:<1}{:<6}{:<20}{:<20}{:<20}".format("N", "/", "N", "NAME", "FAMILY", "PHONE")
        for i in range(self.table_size):
            for j in range(len(self.hash_table[i])):
                name: str = self.hash_table[i][j].info.name
                family = self.hash_table[i][j].info.family
                phone = self.hash_table[i][j].info.phone
                out += "{:<6}{:<1}{:<6}{:<20}{:<20}{:<20}".format(i + 1, '.', j+1, name, family, phone)
        return out


print("Создание таблицы")

a = Hash(table_size=5)
Hash.add_cell(a, 'Yami', 'Tsukihiro', '79515955154')
Hash.add_cell(a, 'Jhon', 'Power', '79546488764')
Hash.add_cell(a, 'Martin', 'Weakness', '79516548927')
Hash.add_cell(a, 'Gerwant', 'Riviski', '7945657892')
Hash.add_cell(a, 'Rui', 'Fudzi', '79685213245')
b = Hash.out(a)
print(b)

print("Поиск по таблице номера 79516548927")

print(Hash.find_cell(a, '79516548927'))
print()

print("Удаление из таблицы номера 79515955154")

Hash.del_cell(a, '79515955154')
k = Hash.out(a)
print(k)
        