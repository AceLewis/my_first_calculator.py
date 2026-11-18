# test_times_31.py
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


class TestTimes31(unittest.TestCase):

    def test_31_times_0(self):
        self.assertEqual(run_calculator('31', '*', '0'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '31*0 = 0',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_31_times_1(self):
        self.assertEqual(run_calculator('31', '*', '1'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '31*1 = 31',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_31_times_2(self):
        self.assertEqual(run_calculator('31', '*', '2'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '31*2 = 62',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_31_times_3(self):
        self.assertEqual(run_calculator('31', '*', '3'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '31*3 = 93',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_31_times_4(self):
        self.assertEqual(run_calculator('31', '*', '4'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '31*4 = 124',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_31_times_5(self):
        self.assertEqual(run_calculator('31', '*', '5'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '31*5 = 155',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_31_times_6(self):
        self.assertEqual(run_calculator('31', '*', '6'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '31*6 = 186',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_31_times_7(self):
        self.assertEqual(run_calculator('31', '*', '7'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '31*7 = 217',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_31_times_8(self):
        self.assertEqual(run_calculator('31', '*', '8'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '31*8 = 248',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_31_times_9(self):
        self.assertEqual(run_calculator('31', '*', '9'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '31*9 = 279',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_31_times_10(self):
        self.assertEqual(run_calculator('31', '*', '10'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '31*10 = 310',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_31_times_11(self):
        self.assertEqual(run_calculator('31', '*', '11'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '31*11 = 341',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_31_times_12(self):
        self.assertEqual(run_calculator('31', '*', '12'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '31*12 = 372',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_31_times_13(self):
        self.assertEqual(run_calculator('31', '*', '13'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '31*13 = 403',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_31_times_14(self):
        self.assertEqual(run_calculator('31', '*', '14'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '31*14 = 434',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_31_times_15(self):
        self.assertEqual(run_calculator('31', '*', '15'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '31*15 = 465',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_31_times_16(self):
        self.assertEqual(run_calculator('31', '*', '16'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '31*16 = 496',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_31_times_17(self):
        self.assertEqual(run_calculator('31', '*', '17'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '31*17 = 527',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_31_times_18(self):
        self.assertEqual(run_calculator('31', '*', '18'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '31*18 = 558',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_31_times_19(self):
        self.assertEqual(run_calculator('31', '*', '19'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '31*19 = 589',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_31_times_20(self):
        self.assertEqual(run_calculator('31', '*', '20'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '31*20 = 620',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_31_times_21(self):
        self.assertEqual(run_calculator('31', '*', '21'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '31*21 = 651',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_31_times_22(self):
        self.assertEqual(run_calculator('31', '*', '22'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '31*22 = 682',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_31_times_23(self):
        self.assertEqual(run_calculator('31', '*', '23'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '31*23 = 713',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_31_times_24(self):
        self.assertEqual(run_calculator('31', '*', '24'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '31*24 = 744',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_31_times_25(self):
        self.assertEqual(run_calculator('31', '*', '25'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '31*25 = 775',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_31_times_26(self):
        self.assertEqual(run_calculator('31', '*', '26'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '31*26 = 806',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_31_times_27(self):
        self.assertEqual(run_calculator('31', '*', '27'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '31*27 = 837',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_31_times_28(self):
        self.assertEqual(run_calculator('31', '*', '28'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '31*28 = 868',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_31_times_29(self):
        self.assertEqual(run_calculator('31', '*', '29'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '31*29 = 899',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_31_times_30(self):
        self.assertEqual(run_calculator('31', '*', '30'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '31*30 = 930',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_31_times_31(self):
        self.assertEqual(run_calculator('31', '*', '31'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '31*31 = 961',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_31_times_32(self):
        self.assertEqual(run_calculator('31', '*', '32'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '31*32 = 992',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_31_times_33(self):
        self.assertEqual(run_calculator('31', '*', '33'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '31*33 = 1023',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_31_times_34(self):
        self.assertEqual(run_calculator('31', '*', '34'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '31*34 = 1054',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_31_times_35(self):
        self.assertEqual(run_calculator('31', '*', '35'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '31*35 = 1085',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_31_times_36(self):
        self.assertEqual(run_calculator('31', '*', '36'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '31*36 = 1116',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_31_times_37(self):
        self.assertEqual(run_calculator('31', '*', '37'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '31*37 = 1147',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_31_times_38(self):
        self.assertEqual(run_calculator('31', '*', '38'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '31*38 = 1178',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_31_times_39(self):
        self.assertEqual(run_calculator('31', '*', '39'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '31*39 = 1209',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_31_times_40(self):
        self.assertEqual(run_calculator('31', '*', '40'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '31*40 = 1240',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_31_times_41(self):
        self.assertEqual(run_calculator('31', '*', '41'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '31*41 = 1271',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_31_times_42(self):
        self.assertEqual(run_calculator('31', '*', '42'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '31*42 = 1302',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_31_times_43(self):
        self.assertEqual(run_calculator('31', '*', '43'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '31*43 = 1333',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_31_times_44(self):
        self.assertEqual(run_calculator('31', '*', '44'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '31*44 = 1364',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_31_times_45(self):
        self.assertEqual(run_calculator('31', '*', '45'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '31*45 = 1395',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_31_times_46(self):
        self.assertEqual(run_calculator('31', '*', '46'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '31*46 = 1426',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_31_times_47(self):
        self.assertEqual(run_calculator('31', '*', '47'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '31*47 = 1457',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_31_times_48(self):
        self.assertEqual(run_calculator('31', '*', '48'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '31*48 = 1488',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_31_times_49(self):
        self.assertEqual(run_calculator('31', '*', '49'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '31*49 = 1519',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_31_times_50(self):
        self.assertEqual(run_calculator('31', '*', '50'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '31*50 = 1550',
            'Thanks for using this calculator, goodbye :)',
        ])


if __name__ == '__main__':
    unittest.main()
