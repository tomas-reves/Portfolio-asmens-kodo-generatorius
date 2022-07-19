from random import randrange
from datetime import datetime
import logging

logging.basicConfig(filename='personal_codes.log', level=logging.INFO, format='%(asctime)s:%(levelname)s:%(message)s')



class AsmensKodas:
    def __init__(self, gimimo_data: str, lytis: str):
        self.gimimo_data = gimimo_data
        self.lytis = lytis

    def generatorius(self):
        asmens_kodas = []
        if str(self.gimimo_data[0:2]) == "19" and self.lytis == 'vyras':
            asmens_kodas.append("3")
        elif str(self.gimimo_data[0:2]) == "19" and self.lytis == 'moteris':
            asmens_kodas.append('4')
        elif str(self.gimimo_data[0:2]) == "20" and self.lytis == 'vyras':
            asmens_kodas.append('5')
        else:
            asmens_kodas.append('6')
        asmens_kodas.append(self.gimimo_data[2:4])
        asmens_kodas.append(self.gimimo_data[5:7])
        asmens_kodas.append(self.gimimo_data[8:])
        asmens_kodas.append(str(randrange(100, 999)))  # tolesni trys skaiciai: tą dieną gimusių eilės numeris;
        semi_final_variantas = "".join(asmens_kodas)
        kontrolinis_skaicius_1 = int(semi_final_variantas[0] * 1 + semi_final_variantas[1] * 2 + semi_final_variantas[2]
                                     * 3 + semi_final_variantas[3] * 4 + semi_final_variantas[4] * 5 +
                                     semi_final_variantas[5]
                                     * 6 + semi_final_variantas[6] * 7 + semi_final_variantas[7] * 8 +
                                     semi_final_variantas[8] *
                                     9 + semi_final_variantas[9] * 1) % 11
        kontrolinis_skaicius_2 = int(semi_final_variantas[0] * 3 + semi_final_variantas[1] * 4 + semi_final_variantas[2]
                                     * 5 + semi_final_variantas[3] * 6 + semi_final_variantas[4] * 7 +
                                     semi_final_variantas[5]
                                     * 8 + semi_final_variantas[6] * 9 + semi_final_variantas[7] * 1 +
                                     semi_final_variantas[8] *
                                     2 + semi_final_variantas[9] * 3) % 11
        if kontrolinis_skaicius_1 != 10:
            asmens_kodas.append(str(kontrolinis_skaicius_1))
        elif kontrolinis_skaicius_2 != 10:
            asmens_kodas.append(str(kontrolinis_skaicius_2))
        else:
            asmens_kodas.append("0")

        final_asmens_kodas = "".join(asmens_kodas)
        logging.info(f"Ivesta: {self.gimimo_data}, {self.lytis}; sugeneruotas asmens kodas: {final_asmens_kodas} ")
        return final_asmens_kodas

class AsmensKodoInterface:

    def gauti_duomenis(self) -> AsmensKodas:

        print("Sveiki, ši programa sugeneruos Jūsų asmens kodą.")
        while True:
            date_of_birth = input("Iveskite savo gimimo datą formatu pvz. 1999/10/23: ")
            try:
                ivesta_data = datetime.strptime(date_of_birth, "%Y/%m/%d")
                break
            except ValueError:
                print("Klaida įvedant gimimo datą. Įveskite validžią gimimo datą nurodytu formatu pvz. 1999/10/23")
                continue
        while True:

            gender = int(input("Jūsų lytis. Įveskite skaičių: 1 -- vyras | 2 -- moteris "))
            if gender == 1 or gender == 2:
                print("Jūsų sugeneruotas asmens kodas yra:")
            else:
                print("Klaida įvedant lytį. Įveskitę tik skaičius 1 -- vyras, 2 -- moteris.")
                continue
            if gender == 1:
                gender = 'vyras'
            else:
                gender = 'moteris'

            return AsmensKodas(date_of_birth, gender)

# interface_instance = AsmensKodoInterface()
# a = interface_instance.gauti_duomenis()
# print(a.generatorius())

if __name__ == '__main__':
    interface_instance = AsmensKodoInterface()
    a = interface_instance.gauti_duomenis()
    print(a.generatorius())