# test_times_47.py
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


class TestTimes47(unittest.TestCase):

    def test_47_times_0(self):
        self.assertEqual(run_calculator('47', '*', '0'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '47*0 = 0',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_47_times_1(self):
        self.assertEqual(run_calculator('47', '*', '1'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '47*1 = 47',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_47_times_2(self):
        self.assertEqual(run_calculator('47', '*', '2'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '47*2 = 94',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_47_times_3(self):
        self.assertEqual(run_calculator('47', '*', '3'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '47*3 = 141',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_47_times_4(self):
        self.assertEqual(run_calculator('47', '*', '4'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '47*4 = 188',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_47_times_5(self):
        self.assertEqual(run_calculator('47', '*', '5'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '47*5 = 235',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_47_times_6(self):
        self.assertEqual(run_calculator('47', '*', '6'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '47*6 = 282',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_47_times_7(self):
        self.assertEqual(run_calculator('47', '*', '7'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '47*7 = 329',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_47_times_8(self):
        self.assertEqual(run_calculator('47', '*', '8'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '47*8 = 376',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_47_times_9(self):
        self.assertEqual(run_calculator('47', '*', '9'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '47*9 = 423',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_47_times_10(self):
        self.assertEqual(run_calculator('47', '*', '10'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '47*10 = 470',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_47_times_11(self):
        self.assertEqual(run_calculator('47', '*', '11'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '47*11 = 517',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_47_times_12(self):
        self.assertEqual(run_calculator('47', '*', '12'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '47*12 = 564',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_47_times_13(self):
        self.assertEqual(run_calculator('47', '*', '13'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '47*13 = 611',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_47_times_14(self):
        self.assertEqual(run_calculator('47', '*', '14'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '47*14 = 658',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_47_times_15(self):
        self.assertEqual(run_calculator('47', '*', '15'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '47*15 = 705',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_47_times_16(self):
        self.assertEqual(run_calculator('47', '*', '16'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '47*16 = 752',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_47_times_17(self):
        self.assertEqual(run_calculator('47', '*', '17'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '47*17 = 799',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_47_times_18(self):
        self.assertEqual(run_calculator('47', '*', '18'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '47*18 = 846',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_47_times_19(self):
        self.assertEqual(run_calculator('47', '*', '19'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '47*19 = 893',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_47_times_20(self):
        self.assertEqual(run_calculator('47', '*', '20'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '47*20 = 940',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_47_times_21(self):
        self.assertEqual(run_calculator('47', '*', '21'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '47*21 = 987',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_47_times_22(self):
        self.assertEqual(run_calculator('47', '*', '22'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '47*22 = 1034',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_47_times_23(self):
        self.assertEqual(run_calculator('47', '*', '23'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '47*23 = 1081',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_47_times_24(self):
        self.assertEqual(run_calculator('47', '*', '24'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '47*24 = 1128',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_47_times_25(self):
        self.assertEqual(run_calculator('47', '*', '25'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '47*25 = 1175',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_47_times_26(self):
        self.assertEqual(run_calculator('47', '*', '26'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '47*26 = 1222',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_47_times_27(self):
        self.assertEqual(run_calculator('47', '*', '27'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '47*27 = 1269',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_47_times_28(self):
        self.assertEqual(run_calculator('47', '*', '28'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '47*28 = 1316',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_47_times_29(self):
        self.assertEqual(run_calculator('47', '*', '29'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '47*29 = 1363',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_47_times_30(self):
        self.assertEqual(run_calculator('47', '*', '30'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '47*30 = 1410',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_47_times_31(self):
        self.assertEqual(run_calculator('47', '*', '31'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '47*31 = 1457',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_47_times_32(self):
        self.assertEqual(run_calculator('47', '*', '32'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '47*32 = 1504',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_47_times_33(self):
        self.assertEqual(run_calculator('47', '*', '33'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '47*33 = 1551',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_47_times_34(self):
        self.assertEqual(run_calculator('47', '*', '34'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '47*34 = 1598',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_47_times_35(self):
        self.assertEqual(run_calculator('47', '*', '35'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '47*35 = 1645',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_47_times_36(self):
        self.assertEqual(run_calculator('47', '*', '36'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '47*36 = 1692',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_47_times_37(self):
        self.assertEqual(run_calculator('47', '*', '37'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '47*37 = 1739',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_47_times_38(self):
        self.assertEqual(run_calculator('47', '*', '38'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '47*38 = 1786',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_47_times_39(self):
        self.assertEqual(run_calculator('47', '*', '39'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '47*39 = 1833',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_47_times_40(self):
        self.assertEqual(run_calculator('47', '*', '40'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '47*40 = 1880',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_47_times_41(self):
        self.assertEqual(run_calculator('47', '*', '41'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '47*41 = 1927',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_47_times_42(self):
        self.assertEqual(run_calculator('47', '*', '42'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '47*42 = 1974',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_47_times_43(self):
        self.assertEqual(run_calculator('47', '*', '43'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '47*43 = 2021',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_47_times_44(self):
        self.assertEqual(run_calculator('47', '*', '44'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '47*44 = 2068',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_47_times_45(self):
        self.assertEqual(run_calculator('47', '*', '45'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '47*45 = 2115',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_47_times_46(self):
        self.assertEqual(run_calculator('47', '*', '46'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '47*46 = 2162',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_47_times_47(self):
        self.assertEqual(run_calculator('47', '*', '47'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '47*47 = 2209',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_47_times_48(self):
        self.assertEqual(run_calculator('47', '*', '48'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '47*48 = 2256',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_47_times_49(self):
        self.assertEqual(run_calculator('47', '*', '49'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '47*49 = 2303',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_47_times_50(self):
        self.assertEqual(run_calculator('47', '*', '50'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '47*50 = 2350',
            'Thanks for using this calculator, goodbye :)',
        ])


if __name__ == '__main__':
    unittest.main()
