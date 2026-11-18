# test_times_13.py
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


class TestTimes13(unittest.TestCase):

    def test_13_times_0(self):
        self.assertEqual(run_calculator('13', '*', '0'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '13*0 = 0',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_13_times_1(self):
        self.assertEqual(run_calculator('13', '*', '1'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '13*1 = 13',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_13_times_2(self):
        self.assertEqual(run_calculator('13', '*', '2'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '13*2 = 26',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_13_times_3(self):
        self.assertEqual(run_calculator('13', '*', '3'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '13*3 = 39',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_13_times_4(self):
        self.assertEqual(run_calculator('13', '*', '4'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '13*4 = 52',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_13_times_5(self):
        self.assertEqual(run_calculator('13', '*', '5'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '13*5 = 65',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_13_times_6(self):
        self.assertEqual(run_calculator('13', '*', '6'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '13*6 = 78',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_13_times_7(self):
        self.assertEqual(run_calculator('13', '*', '7'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '13*7 = 91',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_13_times_8(self):
        self.assertEqual(run_calculator('13', '*', '8'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '13*8 = 104',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_13_times_9(self):
        self.assertEqual(run_calculator('13', '*', '9'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '13*9 = 117',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_13_times_10(self):
        self.assertEqual(run_calculator('13', '*', '10'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '13*10 = 130',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_13_times_11(self):
        self.assertEqual(run_calculator('13', '*', '11'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '13*11 = 143',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_13_times_12(self):
        self.assertEqual(run_calculator('13', '*', '12'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '13*12 = 156',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_13_times_13(self):
        self.assertEqual(run_calculator('13', '*', '13'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '13*13 = 169',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_13_times_14(self):
        self.assertEqual(run_calculator('13', '*', '14'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '13*14 = 182',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_13_times_15(self):
        self.assertEqual(run_calculator('13', '*', '15'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '13*15 = 195',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_13_times_16(self):
        self.assertEqual(run_calculator('13', '*', '16'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '13*16 = 208',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_13_times_17(self):
        self.assertEqual(run_calculator('13', '*', '17'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '13*17 = 221',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_13_times_18(self):
        self.assertEqual(run_calculator('13', '*', '18'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '13*18 = 234',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_13_times_19(self):
        self.assertEqual(run_calculator('13', '*', '19'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '13*19 = 247',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_13_times_20(self):
        self.assertEqual(run_calculator('13', '*', '20'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '13*20 = 260',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_13_times_21(self):
        self.assertEqual(run_calculator('13', '*', '21'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '13*21 = 273',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_13_times_22(self):
        self.assertEqual(run_calculator('13', '*', '22'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '13*22 = 286',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_13_times_23(self):
        self.assertEqual(run_calculator('13', '*', '23'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '13*23 = 299',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_13_times_24(self):
        self.assertEqual(run_calculator('13', '*', '24'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '13*24 = 312',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_13_times_25(self):
        self.assertEqual(run_calculator('13', '*', '25'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '13*25 = 325',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_13_times_26(self):
        self.assertEqual(run_calculator('13', '*', '26'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '13*26 = 338',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_13_times_27(self):
        self.assertEqual(run_calculator('13', '*', '27'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '13*27 = 351',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_13_times_28(self):
        self.assertEqual(run_calculator('13', '*', '28'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '13*28 = 364',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_13_times_29(self):
        self.assertEqual(run_calculator('13', '*', '29'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '13*29 = 377',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_13_times_30(self):
        self.assertEqual(run_calculator('13', '*', '30'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '13*30 = 390',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_13_times_31(self):
        self.assertEqual(run_calculator('13', '*', '31'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '13*31 = 403',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_13_times_32(self):
        self.assertEqual(run_calculator('13', '*', '32'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '13*32 = 416',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_13_times_33(self):
        self.assertEqual(run_calculator('13', '*', '33'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '13*33 = 429',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_13_times_34(self):
        self.assertEqual(run_calculator('13', '*', '34'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '13*34 = 442',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_13_times_35(self):
        self.assertEqual(run_calculator('13', '*', '35'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '13*35 = 455',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_13_times_36(self):
        self.assertEqual(run_calculator('13', '*', '36'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '13*36 = 468',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_13_times_37(self):
        self.assertEqual(run_calculator('13', '*', '37'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '13*37 = 481',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_13_times_38(self):
        self.assertEqual(run_calculator('13', '*', '38'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '13*38 = 494',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_13_times_39(self):
        self.assertEqual(run_calculator('13', '*', '39'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '13*39 = 507',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_13_times_40(self):
        self.assertEqual(run_calculator('13', '*', '40'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '13*40 = 520',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_13_times_41(self):
        self.assertEqual(run_calculator('13', '*', '41'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '13*41 = 533',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_13_times_42(self):
        self.assertEqual(run_calculator('13', '*', '42'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '13*42 = 546',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_13_times_43(self):
        self.assertEqual(run_calculator('13', '*', '43'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '13*43 = 559',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_13_times_44(self):
        self.assertEqual(run_calculator('13', '*', '44'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '13*44 = 572',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_13_times_45(self):
        self.assertEqual(run_calculator('13', '*', '45'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '13*45 = 585',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_13_times_46(self):
        self.assertEqual(run_calculator('13', '*', '46'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '13*46 = 598',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_13_times_47(self):
        self.assertEqual(run_calculator('13', '*', '47'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '13*47 = 611',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_13_times_48(self):
        self.assertEqual(run_calculator('13', '*', '48'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '13*48 = 624',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_13_times_49(self):
        self.assertEqual(run_calculator('13', '*', '49'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '13*49 = 637',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_13_times_50(self):
        self.assertEqual(run_calculator('13', '*', '50'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '13*50 = 650',
            'Thanks for using this calculator, goodbye :)',
        ])


if __name__ == '__main__':
    unittest.main()
