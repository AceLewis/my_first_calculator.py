# test_times_39.py
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


class TestTimes39(unittest.TestCase):

    def test_39_times_0(self):
        self.assertEqual(run_calculator('39', '*', '0'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '39*0 = 0',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_39_times_1(self):
        self.assertEqual(run_calculator('39', '*', '1'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '39*1 = 39',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_39_times_2(self):
        self.assertEqual(run_calculator('39', '*', '2'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '39*2 = 78',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_39_times_3(self):
        self.assertEqual(run_calculator('39', '*', '3'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '39*3 = 117',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_39_times_4(self):
        self.assertEqual(run_calculator('39', '*', '4'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '39*4 = 156',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_39_times_5(self):
        self.assertEqual(run_calculator('39', '*', '5'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '39*5 = 195',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_39_times_6(self):
        self.assertEqual(run_calculator('39', '*', '6'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '39*6 = 234',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_39_times_7(self):
        self.assertEqual(run_calculator('39', '*', '7'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '39*7 = 273',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_39_times_8(self):
        self.assertEqual(run_calculator('39', '*', '8'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '39*8 = 312',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_39_times_9(self):
        self.assertEqual(run_calculator('39', '*', '9'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '39*9 = 351',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_39_times_10(self):
        self.assertEqual(run_calculator('39', '*', '10'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '39*10 = 390',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_39_times_11(self):
        self.assertEqual(run_calculator('39', '*', '11'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '39*11 = 429',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_39_times_12(self):
        self.assertEqual(run_calculator('39', '*', '12'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '39*12 = 468',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_39_times_13(self):
        self.assertEqual(run_calculator('39', '*', '13'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '39*13 = 507',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_39_times_14(self):
        self.assertEqual(run_calculator('39', '*', '14'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '39*14 = 546',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_39_times_15(self):
        self.assertEqual(run_calculator('39', '*', '15'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '39*15 = 585',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_39_times_16(self):
        self.assertEqual(run_calculator('39', '*', '16'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '39*16 = 624',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_39_times_17(self):
        self.assertEqual(run_calculator('39', '*', '17'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '39*17 = 663',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_39_times_18(self):
        self.assertEqual(run_calculator('39', '*', '18'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '39*18 = 702',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_39_times_19(self):
        self.assertEqual(run_calculator('39', '*', '19'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '39*19 = 741',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_39_times_20(self):
        self.assertEqual(run_calculator('39', '*', '20'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '39*20 = 780',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_39_times_21(self):
        self.assertEqual(run_calculator('39', '*', '21'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '39*21 = 819',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_39_times_22(self):
        self.assertEqual(run_calculator('39', '*', '22'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '39*22 = 858',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_39_times_23(self):
        self.assertEqual(run_calculator('39', '*', '23'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '39*23 = 897',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_39_times_24(self):
        self.assertEqual(run_calculator('39', '*', '24'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '39*24 = 936',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_39_times_25(self):
        self.assertEqual(run_calculator('39', '*', '25'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '39*25 = 975',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_39_times_26(self):
        self.assertEqual(run_calculator('39', '*', '26'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '39*26 = 1014',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_39_times_27(self):
        self.assertEqual(run_calculator('39', '*', '27'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '39*27 = 1053',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_39_times_28(self):
        self.assertEqual(run_calculator('39', '*', '28'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '39*28 = 1092',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_39_times_29(self):
        self.assertEqual(run_calculator('39', '*', '29'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '39*29 = 1131',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_39_times_30(self):
        self.assertEqual(run_calculator('39', '*', '30'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '39*30 = 1170',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_39_times_31(self):
        self.assertEqual(run_calculator('39', '*', '31'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '39*31 = 1209',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_39_times_32(self):
        self.assertEqual(run_calculator('39', '*', '32'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '39*32 = 1248',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_39_times_33(self):
        self.assertEqual(run_calculator('39', '*', '33'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '39*33 = 1287',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_39_times_34(self):
        self.assertEqual(run_calculator('39', '*', '34'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '39*34 = 1326',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_39_times_35(self):
        self.assertEqual(run_calculator('39', '*', '35'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '39*35 = 1365',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_39_times_36(self):
        self.assertEqual(run_calculator('39', '*', '36'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '39*36 = 1404',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_39_times_37(self):
        self.assertEqual(run_calculator('39', '*', '37'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '39*37 = 1443',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_39_times_38(self):
        self.assertEqual(run_calculator('39', '*', '38'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '39*38 = 1482',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_39_times_39(self):
        self.assertEqual(run_calculator('39', '*', '39'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '39*39 = 1521',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_39_times_40(self):
        self.assertEqual(run_calculator('39', '*', '40'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '39*40 = 1560',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_39_times_41(self):
        self.assertEqual(run_calculator('39', '*', '41'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '39*41 = 1599',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_39_times_42(self):
        self.assertEqual(run_calculator('39', '*', '42'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '39*42 = 1638',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_39_times_43(self):
        self.assertEqual(run_calculator('39', '*', '43'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '39*43 = 1677',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_39_times_44(self):
        self.assertEqual(run_calculator('39', '*', '44'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '39*44 = 1716',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_39_times_45(self):
        self.assertEqual(run_calculator('39', '*', '45'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '39*45 = 1755',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_39_times_46(self):
        self.assertEqual(run_calculator('39', '*', '46'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '39*46 = 1794',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_39_times_47(self):
        self.assertEqual(run_calculator('39', '*', '47'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '39*47 = 1833',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_39_times_48(self):
        self.assertEqual(run_calculator('39', '*', '48'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '39*48 = 1872',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_39_times_49(self):
        self.assertEqual(run_calculator('39', '*', '49'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '39*49 = 1911',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_39_times_50(self):
        self.assertEqual(run_calculator('39', '*', '50'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '39*50 = 1950',
            'Thanks for using this calculator, goodbye :)',
        ])


if __name__ == '__main__':
    unittest.main()
