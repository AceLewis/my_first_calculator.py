# test_times_36.py
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


class TestTimes36(unittest.TestCase):

    def test_36_times_0(self):
        self.assertEqual(run_calculator('36', '*', '0'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '36*0 = 0',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_36_times_1(self):
        self.assertEqual(run_calculator('36', '*', '1'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '36*1 = 36',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_36_times_2(self):
        self.assertEqual(run_calculator('36', '*', '2'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '36*2 = 72',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_36_times_3(self):
        self.assertEqual(run_calculator('36', '*', '3'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '36*3 = 108',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_36_times_4(self):
        self.assertEqual(run_calculator('36', '*', '4'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '36*4 = 144',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_36_times_5(self):
        self.assertEqual(run_calculator('36', '*', '5'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '36*5 = 180',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_36_times_6(self):
        self.assertEqual(run_calculator('36', '*', '6'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '36*6 = 216',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_36_times_7(self):
        self.assertEqual(run_calculator('36', '*', '7'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '36*7 = 252',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_36_times_8(self):
        self.assertEqual(run_calculator('36', '*', '8'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '36*8 = 288',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_36_times_9(self):
        self.assertEqual(run_calculator('36', '*', '9'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '36*9 = 324',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_36_times_10(self):
        self.assertEqual(run_calculator('36', '*', '10'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '36*10 = 360',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_36_times_11(self):
        self.assertEqual(run_calculator('36', '*', '11'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '36*11 = 396',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_36_times_12(self):
        self.assertEqual(run_calculator('36', '*', '12'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '36*12 = 432',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_36_times_13(self):
        self.assertEqual(run_calculator('36', '*', '13'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '36*13 = 468',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_36_times_14(self):
        self.assertEqual(run_calculator('36', '*', '14'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '36*14 = 504',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_36_times_15(self):
        self.assertEqual(run_calculator('36', '*', '15'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '36*15 = 540',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_36_times_16(self):
        self.assertEqual(run_calculator('36', '*', '16'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '36*16 = 576',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_36_times_17(self):
        self.assertEqual(run_calculator('36', '*', '17'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '36*17 = 612',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_36_times_18(self):
        self.assertEqual(run_calculator('36', '*', '18'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '36*18 = 648',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_36_times_19(self):
        self.assertEqual(run_calculator('36', '*', '19'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '36*19 = 684',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_36_times_20(self):
        self.assertEqual(run_calculator('36', '*', '20'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '36*20 = 720',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_36_times_21(self):
        self.assertEqual(run_calculator('36', '*', '21'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '36*21 = 756',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_36_times_22(self):
        self.assertEqual(run_calculator('36', '*', '22'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '36*22 = 792',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_36_times_23(self):
        self.assertEqual(run_calculator('36', '*', '23'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '36*23 = 828',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_36_times_24(self):
        self.assertEqual(run_calculator('36', '*', '24'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '36*24 = 864',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_36_times_25(self):
        self.assertEqual(run_calculator('36', '*', '25'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '36*25 = 900',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_36_times_26(self):
        self.assertEqual(run_calculator('36', '*', '26'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '36*26 = 936',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_36_times_27(self):
        self.assertEqual(run_calculator('36', '*', '27'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '36*27 = 972',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_36_times_28(self):
        self.assertEqual(run_calculator('36', '*', '28'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '36*28 = 1008',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_36_times_29(self):
        self.assertEqual(run_calculator('36', '*', '29'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '36*29 = 1044',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_36_times_30(self):
        self.assertEqual(run_calculator('36', '*', '30'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '36*30 = 1080',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_36_times_31(self):
        self.assertEqual(run_calculator('36', '*', '31'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '36*31 = 1116',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_36_times_32(self):
        self.assertEqual(run_calculator('36', '*', '32'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '36*32 = 1152',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_36_times_33(self):
        self.assertEqual(run_calculator('36', '*', '33'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '36*33 = 1188',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_36_times_34(self):
        self.assertEqual(run_calculator('36', '*', '34'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '36*34 = 1224',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_36_times_35(self):
        self.assertEqual(run_calculator('36', '*', '35'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '36*35 = 1260',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_36_times_36(self):
        self.assertEqual(run_calculator('36', '*', '36'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '36*36 = 1296',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_36_times_37(self):
        self.assertEqual(run_calculator('36', '*', '37'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '36*37 = 1332',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_36_times_38(self):
        self.assertEqual(run_calculator('36', '*', '38'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '36*38 = 1368',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_36_times_39(self):
        self.assertEqual(run_calculator('36', '*', '39'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '36*39 = 1404',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_36_times_40(self):
        self.assertEqual(run_calculator('36', '*', '40'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '36*40 = 1440',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_36_times_41(self):
        self.assertEqual(run_calculator('36', '*', '41'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '36*41 = 1476',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_36_times_42(self):
        self.assertEqual(run_calculator('36', '*', '42'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '36*42 = 1512',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_36_times_43(self):
        self.assertEqual(run_calculator('36', '*', '43'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '36*43 = 1548',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_36_times_44(self):
        self.assertEqual(run_calculator('36', '*', '44'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '36*44 = 1584',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_36_times_45(self):
        self.assertEqual(run_calculator('36', '*', '45'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '36*45 = 1620',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_36_times_46(self):
        self.assertEqual(run_calculator('36', '*', '46'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '36*46 = 1656',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_36_times_47(self):
        self.assertEqual(run_calculator('36', '*', '47'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '36*47 = 1692',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_36_times_48(self):
        self.assertEqual(run_calculator('36', '*', '48'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '36*48 = 1728',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_36_times_49(self):
        self.assertEqual(run_calculator('36', '*', '49'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '36*49 = 1764',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_36_times_50(self):
        self.assertEqual(run_calculator('36', '*', '50'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '36*50 = 1800',
            'Thanks for using this calculator, goodbye :)',
        ])


if __name__ == '__main__':
    unittest.main()
