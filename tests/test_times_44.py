# test_times_44.py
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


class TestTimes44(unittest.TestCase):

    def test_44_times_0(self):
        self.assertEqual(run_calculator('44', '*', '0'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '44*0 = 0',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_44_times_1(self):
        self.assertEqual(run_calculator('44', '*', '1'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '44*1 = 44',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_44_times_2(self):
        self.assertEqual(run_calculator('44', '*', '2'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '44*2 = 88',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_44_times_3(self):
        self.assertEqual(run_calculator('44', '*', '3'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '44*3 = 132',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_44_times_4(self):
        self.assertEqual(run_calculator('44', '*', '4'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '44*4 = 176',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_44_times_5(self):
        self.assertEqual(run_calculator('44', '*', '5'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '44*5 = 220',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_44_times_6(self):
        self.assertEqual(run_calculator('44', '*', '6'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '44*6 = 264',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_44_times_7(self):
        self.assertEqual(run_calculator('44', '*', '7'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '44*7 = 308',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_44_times_8(self):
        self.assertEqual(run_calculator('44', '*', '8'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '44*8 = 352',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_44_times_9(self):
        self.assertEqual(run_calculator('44', '*', '9'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '44*9 = 396',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_44_times_10(self):
        self.assertEqual(run_calculator('44', '*', '10'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '44*10 = 440',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_44_times_11(self):
        self.assertEqual(run_calculator('44', '*', '11'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '44*11 = 484',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_44_times_12(self):
        self.assertEqual(run_calculator('44', '*', '12'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '44*12 = 528',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_44_times_13(self):
        self.assertEqual(run_calculator('44', '*', '13'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '44*13 = 572',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_44_times_14(self):
        self.assertEqual(run_calculator('44', '*', '14'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '44*14 = 616',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_44_times_15(self):
        self.assertEqual(run_calculator('44', '*', '15'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '44*15 = 660',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_44_times_16(self):
        self.assertEqual(run_calculator('44', '*', '16'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '44*16 = 704',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_44_times_17(self):
        self.assertEqual(run_calculator('44', '*', '17'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '44*17 = 748',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_44_times_18(self):
        self.assertEqual(run_calculator('44', '*', '18'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '44*18 = 792',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_44_times_19(self):
        self.assertEqual(run_calculator('44', '*', '19'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '44*19 = 836',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_44_times_20(self):
        self.assertEqual(run_calculator('44', '*', '20'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '44*20 = 880',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_44_times_21(self):
        self.assertEqual(run_calculator('44', '*', '21'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '44*21 = 924',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_44_times_22(self):
        self.assertEqual(run_calculator('44', '*', '22'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '44*22 = 968',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_44_times_23(self):
        self.assertEqual(run_calculator('44', '*', '23'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '44*23 = 1012',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_44_times_24(self):
        self.assertEqual(run_calculator('44', '*', '24'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '44*24 = 1056',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_44_times_25(self):
        self.assertEqual(run_calculator('44', '*', '25'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '44*25 = 1100',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_44_times_26(self):
        self.assertEqual(run_calculator('44', '*', '26'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '44*26 = 1144',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_44_times_27(self):
        self.assertEqual(run_calculator('44', '*', '27'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '44*27 = 1188',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_44_times_28(self):
        self.assertEqual(run_calculator('44', '*', '28'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '44*28 = 1232',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_44_times_29(self):
        self.assertEqual(run_calculator('44', '*', '29'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '44*29 = 1276',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_44_times_30(self):
        self.assertEqual(run_calculator('44', '*', '30'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '44*30 = 1320',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_44_times_31(self):
        self.assertEqual(run_calculator('44', '*', '31'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '44*31 = 1364',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_44_times_32(self):
        self.assertEqual(run_calculator('44', '*', '32'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '44*32 = 1408',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_44_times_33(self):
        self.assertEqual(run_calculator('44', '*', '33'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '44*33 = 1452',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_44_times_34(self):
        self.assertEqual(run_calculator('44', '*', '34'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '44*34 = 1496',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_44_times_35(self):
        self.assertEqual(run_calculator('44', '*', '35'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '44*35 = 1540',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_44_times_36(self):
        self.assertEqual(run_calculator('44', '*', '36'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '44*36 = 1584',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_44_times_37(self):
        self.assertEqual(run_calculator('44', '*', '37'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '44*37 = 1628',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_44_times_38(self):
        self.assertEqual(run_calculator('44', '*', '38'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '44*38 = 1672',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_44_times_39(self):
        self.assertEqual(run_calculator('44', '*', '39'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '44*39 = 1716',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_44_times_40(self):
        self.assertEqual(run_calculator('44', '*', '40'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '44*40 = 1760',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_44_times_41(self):
        self.assertEqual(run_calculator('44', '*', '41'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '44*41 = 1804',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_44_times_42(self):
        self.assertEqual(run_calculator('44', '*', '42'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '44*42 = 1848',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_44_times_43(self):
        self.assertEqual(run_calculator('44', '*', '43'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '44*43 = 1892',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_44_times_44(self):
        self.assertEqual(run_calculator('44', '*', '44'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '44*44 = 1936',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_44_times_45(self):
        self.assertEqual(run_calculator('44', '*', '45'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '44*45 = 1980',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_44_times_46(self):
        self.assertEqual(run_calculator('44', '*', '46'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '44*46 = 2024',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_44_times_47(self):
        self.assertEqual(run_calculator('44', '*', '47'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '44*47 = 2068',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_44_times_48(self):
        self.assertEqual(run_calculator('44', '*', '48'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '44*48 = 2112',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_44_times_49(self):
        self.assertEqual(run_calculator('44', '*', '49'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '44*49 = 2156',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_44_times_50(self):
        self.assertEqual(run_calculator('44', '*', '50'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '44*50 = 2200',
            'Thanks for using this calculator, goodbye :)',
        ])


if __name__ == '__main__':
    unittest.main()
