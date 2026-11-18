# test_times_49.py
# Every single case gets its own test, to be true to the story

import io
import unittest
from contextlib import redirect_stdout
from pathlib import Path
from unittest import mock

SOURCE = Path(__file__).parent.parent / 'my_first_calculator.py'
CODE = compile(SOURCE.read_text(), str(SOURCE), 'exec')


def run_calculator(num1, sign, num2):
    answers = iter([num1, sign, num2])
    out = io.StringIO()
    with mock.patch('builtins.input', lambda prompt='': next(answers)), redirect_stdout(out):
        exec(CODE, {'__name__': '__main__'})
    return out.getvalue().splitlines()


class TestTimes49(unittest.TestCase):

    def test_49_times_0(self):
        self.assertEqual(run_calculator('49', '*', '0'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '49*0 = 0',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_49_times_1(self):
        self.assertEqual(run_calculator('49', '*', '1'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '49*1 = 49',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_49_times_2(self):
        self.assertEqual(run_calculator('49', '*', '2'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '49*2 = 98',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_49_times_3(self):
        self.assertEqual(run_calculator('49', '*', '3'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '49*3 = 147',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_49_times_4(self):
        self.assertEqual(run_calculator('49', '*', '4'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '49*4 = 196',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_49_times_5(self):
        self.assertEqual(run_calculator('49', '*', '5'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '49*5 = 245',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_49_times_6(self):
        self.assertEqual(run_calculator('49', '*', '6'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '49*6 = 294',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_49_times_7(self):
        self.assertEqual(run_calculator('49', '*', '7'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '49*7 = 343',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_49_times_8(self):
        self.assertEqual(run_calculator('49', '*', '8'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '49*8 = 392',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_49_times_9(self):
        self.assertEqual(run_calculator('49', '*', '9'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '49*9 = 441',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_49_times_10(self):
        self.assertEqual(run_calculator('49', '*', '10'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '49*10 = 490',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_49_times_11(self):
        self.assertEqual(run_calculator('49', '*', '11'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '49*11 = 539',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_49_times_12(self):
        self.assertEqual(run_calculator('49', '*', '12'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '49*12 = 588',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_49_times_13(self):
        self.assertEqual(run_calculator('49', '*', '13'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '49*13 = 637',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_49_times_14(self):
        self.assertEqual(run_calculator('49', '*', '14'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '49*14 = 686',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_49_times_15(self):
        self.assertEqual(run_calculator('49', '*', '15'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '49*15 = 735',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_49_times_16(self):
        self.assertEqual(run_calculator('49', '*', '16'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '49*16 = 784',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_49_times_17(self):
        self.assertEqual(run_calculator('49', '*', '17'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '49*17 = 833',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_49_times_18(self):
        self.assertEqual(run_calculator('49', '*', '18'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '49*18 = 882',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_49_times_19(self):
        self.assertEqual(run_calculator('49', '*', '19'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '49*19 = 931',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_49_times_20(self):
        self.assertEqual(run_calculator('49', '*', '20'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '49*20 = 980',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_49_times_21(self):
        self.assertEqual(run_calculator('49', '*', '21'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '49*21 = 1029',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_49_times_22(self):
        self.assertEqual(run_calculator('49', '*', '22'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '49*22 = 1078',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_49_times_23(self):
        self.assertEqual(run_calculator('49', '*', '23'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '49*23 = 1127',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_49_times_24(self):
        self.assertEqual(run_calculator('49', '*', '24'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '49*24 = 1176',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_49_times_25(self):
        self.assertEqual(run_calculator('49', '*', '25'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '49*25 = 1225',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_49_times_26(self):
        self.assertEqual(run_calculator('49', '*', '26'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '49*26 = 1274',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_49_times_27(self):
        self.assertEqual(run_calculator('49', '*', '27'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '49*27 = 1323',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_49_times_28(self):
        self.assertEqual(run_calculator('49', '*', '28'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '49*28 = 1372',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_49_times_29(self):
        self.assertEqual(run_calculator('49', '*', '29'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '49*29 = 1421',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_49_times_30(self):
        self.assertEqual(run_calculator('49', '*', '30'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '49*30 = 1470',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_49_times_31(self):
        self.assertEqual(run_calculator('49', '*', '31'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '49*31 = 1519',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_49_times_32(self):
        self.assertEqual(run_calculator('49', '*', '32'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '49*32 = 1568',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_49_times_33(self):
        self.assertEqual(run_calculator('49', '*', '33'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '49*33 = 1617',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_49_times_34(self):
        self.assertEqual(run_calculator('49', '*', '34'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '49*34 = 1666',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_49_times_35(self):
        self.assertEqual(run_calculator('49', '*', '35'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '49*35 = 1715',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_49_times_36(self):
        self.assertEqual(run_calculator('49', '*', '36'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '49*36 = 1764',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_49_times_37(self):
        self.assertEqual(run_calculator('49', '*', '37'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '49*37 = 1813',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_49_times_38(self):
        self.assertEqual(run_calculator('49', '*', '38'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '49*38 = 1862',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_49_times_39(self):
        self.assertEqual(run_calculator('49', '*', '39'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '49*39 = 1911',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_49_times_40(self):
        self.assertEqual(run_calculator('49', '*', '40'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '49*40 = 1960',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_49_times_41(self):
        self.assertEqual(run_calculator('49', '*', '41'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '49*41 = 2009',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_49_times_42(self):
        self.assertEqual(run_calculator('49', '*', '42'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '49*42 = 2058',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_49_times_43(self):
        self.assertEqual(run_calculator('49', '*', '43'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '49*43 = 2107',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_49_times_44(self):
        self.assertEqual(run_calculator('49', '*', '44'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '49*44 = 2156',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_49_times_45(self):
        self.assertEqual(run_calculator('49', '*', '45'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '49*45 = 2205',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_49_times_46(self):
        self.assertEqual(run_calculator('49', '*', '46'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '49*46 = 2254',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_49_times_47(self):
        self.assertEqual(run_calculator('49', '*', '47'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '49*47 = 2303',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_49_times_48(self):
        self.assertEqual(run_calculator('49', '*', '48'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '49*48 = 2352',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_49_times_49(self):
        self.assertEqual(run_calculator('49', '*', '49'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '49*49 = 2401',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_49_times_50(self):
        self.assertEqual(run_calculator('49', '*', '50'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '49*50 = 2450',
            'Thanks for using this calculator, goodbye :)',
        ])


if __name__ == '__main__':
    unittest.main()
