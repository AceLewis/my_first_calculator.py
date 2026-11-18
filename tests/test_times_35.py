# test_times_35.py
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


class TestTimes35(unittest.TestCase):

    def test_35_times_0(self):
        self.assertEqual(run_calculator('35', '*', '0'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '35*0 = 0',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_35_times_1(self):
        self.assertEqual(run_calculator('35', '*', '1'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '35*1 = 35',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_35_times_2(self):
        self.assertEqual(run_calculator('35', '*', '2'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '35*2 = 70',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_35_times_3(self):
        self.assertEqual(run_calculator('35', '*', '3'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '35*3 = 105',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_35_times_4(self):
        self.assertEqual(run_calculator('35', '*', '4'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '35*4 = 140',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_35_times_5(self):
        self.assertEqual(run_calculator('35', '*', '5'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '35*5 = 175',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_35_times_6(self):
        self.assertEqual(run_calculator('35', '*', '6'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '35*6 = 210',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_35_times_7(self):
        self.assertEqual(run_calculator('35', '*', '7'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '35*7 = 245',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_35_times_8(self):
        self.assertEqual(run_calculator('35', '*', '8'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '35*8 = 280',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_35_times_9(self):
        self.assertEqual(run_calculator('35', '*', '9'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '35*9 = 315',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_35_times_10(self):
        self.assertEqual(run_calculator('35', '*', '10'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '35*10 = 350',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_35_times_11(self):
        self.assertEqual(run_calculator('35', '*', '11'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '35*11 = 385',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_35_times_12(self):
        self.assertEqual(run_calculator('35', '*', '12'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '35*12 = 420',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_35_times_13(self):
        self.assertEqual(run_calculator('35', '*', '13'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '35*13 = 455',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_35_times_14(self):
        self.assertEqual(run_calculator('35', '*', '14'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '35*14 = 490',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_35_times_15(self):
        self.assertEqual(run_calculator('35', '*', '15'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '35*15 = 525',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_35_times_16(self):
        self.assertEqual(run_calculator('35', '*', '16'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '35*16 = 560',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_35_times_17(self):
        self.assertEqual(run_calculator('35', '*', '17'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '35*17 = 595',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_35_times_18(self):
        self.assertEqual(run_calculator('35', '*', '18'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '35*18 = 630',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_35_times_19(self):
        self.assertEqual(run_calculator('35', '*', '19'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '35*19 = 665',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_35_times_20(self):
        self.assertEqual(run_calculator('35', '*', '20'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '35*20 = 700',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_35_times_21(self):
        self.assertEqual(run_calculator('35', '*', '21'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '35*21 = 735',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_35_times_22(self):
        self.assertEqual(run_calculator('35', '*', '22'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '35*22 = 770',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_35_times_23(self):
        self.assertEqual(run_calculator('35', '*', '23'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '35*23 = 805',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_35_times_24(self):
        self.assertEqual(run_calculator('35', '*', '24'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '35*24 = 840',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_35_times_25(self):
        self.assertEqual(run_calculator('35', '*', '25'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '35*25 = 875',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_35_times_26(self):
        self.assertEqual(run_calculator('35', '*', '26'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '35*26 = 910',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_35_times_27(self):
        self.assertEqual(run_calculator('35', '*', '27'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '35*27 = 945',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_35_times_28(self):
        self.assertEqual(run_calculator('35', '*', '28'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '35*28 = 980',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_35_times_29(self):
        self.assertEqual(run_calculator('35', '*', '29'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '35*29 = 1015',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_35_times_30(self):
        self.assertEqual(run_calculator('35', '*', '30'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '35*30 = 1050',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_35_times_31(self):
        self.assertEqual(run_calculator('35', '*', '31'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '35*31 = 1085',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_35_times_32(self):
        self.assertEqual(run_calculator('35', '*', '32'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '35*32 = 1120',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_35_times_33(self):
        self.assertEqual(run_calculator('35', '*', '33'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '35*33 = 1155',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_35_times_34(self):
        self.assertEqual(run_calculator('35', '*', '34'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '35*34 = 1190',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_35_times_35(self):
        self.assertEqual(run_calculator('35', '*', '35'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '35*35 = 1225',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_35_times_36(self):
        self.assertEqual(run_calculator('35', '*', '36'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '35*36 = 1260',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_35_times_37(self):
        self.assertEqual(run_calculator('35', '*', '37'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '35*37 = 1295',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_35_times_38(self):
        self.assertEqual(run_calculator('35', '*', '38'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '35*38 = 1330',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_35_times_39(self):
        self.assertEqual(run_calculator('35', '*', '39'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '35*39 = 1365',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_35_times_40(self):
        self.assertEqual(run_calculator('35', '*', '40'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '35*40 = 1400',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_35_times_41(self):
        self.assertEqual(run_calculator('35', '*', '41'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '35*41 = 1435',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_35_times_42(self):
        self.assertEqual(run_calculator('35', '*', '42'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '35*42 = 1470',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_35_times_43(self):
        self.assertEqual(run_calculator('35', '*', '43'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '35*43 = 1505',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_35_times_44(self):
        self.assertEqual(run_calculator('35', '*', '44'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '35*44 = 1540',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_35_times_45(self):
        self.assertEqual(run_calculator('35', '*', '45'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '35*45 = 1575',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_35_times_46(self):
        self.assertEqual(run_calculator('35', '*', '46'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '35*46 = 1610',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_35_times_47(self):
        self.assertEqual(run_calculator('35', '*', '47'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '35*47 = 1645',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_35_times_48(self):
        self.assertEqual(run_calculator('35', '*', '48'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '35*48 = 1680',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_35_times_49(self):
        self.assertEqual(run_calculator('35', '*', '49'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '35*49 = 1715',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_35_times_50(self):
        self.assertEqual(run_calculator('35', '*', '50'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '35*50 = 1750',
            'Thanks for using this calculator, goodbye :)',
        ])


if __name__ == '__main__':
    unittest.main()
