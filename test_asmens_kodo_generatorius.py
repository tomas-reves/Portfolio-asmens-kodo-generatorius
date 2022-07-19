import unittest
from asmens_kodo_generatorius import AsmensKodas

class TestKodas(unittest.TestCase):

    def test_first_7_personal_code(self):
        lytis_vyras = 'vyras'
        lytis_moteris = 'moteris'
        gimimo_data_20_amzius = '1995/05/15'
        gimimo_data_21_amzius = '2005/12/25'
        pirmas_testas = AsmensKodas(gimimo_data_20_amzius, lytis_vyras)
        antras_testas = AsmensKodas(gimimo_data_20_amzius, lytis_moteris)
        trecias_testas = AsmensKodas(gimimo_data_21_amzius, lytis_vyras)
        ketvirtas_testas = AsmensKodas(gimimo_data_21_amzius, lytis_moteris)

        self.assertEqual(pirmas_testas.generatorius()[:7], '3950515')
        self.assertEqual(antras_testas.generatorius()[:7], '4950515')
        self.assertEqual(trecias_testas.generatorius()[:7], '5051225')
        self.assertEqual(ketvirtas_testas.generatorius()[:7], '6051225')

if __name__ == '__main__':
    unittest.main()