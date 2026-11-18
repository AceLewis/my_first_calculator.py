# test_times_1.py
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


class TestTimes1(unittest.TestCase):

    def test_1_times_0(self):
        self.assertEqual(run_calculator('1', '*', '0'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '1*0 = 0',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_1_times_1(self):
        self.assertEqual(run_calculator('1', '*', '1'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '1*1 = 1',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_1_times_2(self):
        self.assertEqual(run_calculator('1', '*', '2'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '1*2 = 2',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_1_times_3(self):
        self.assertEqual(run_calculator('1', '*', '3'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '1*3 = 3',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_1_times_4(self):
        self.assertEqual(run_calculator('1', '*', '4'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '1*4 = 4',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_1_times_5(self):
        self.assertEqual(run_calculator('1', '*', '5'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '1*5 = 5',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_1_times_6(self):
        self.assertEqual(run_calculator('1', '*', '6'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '1*6 = 6',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_1_times_7(self):
        self.assertEqual(run_calculator('1', '*', '7'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '1*7 = 7',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_1_times_8(self):
        self.assertEqual(run_calculator('1', '*', '8'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '1*8 = 8',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_1_times_9(self):
        self.assertEqual(run_calculator('1', '*', '9'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '1*9 = 9',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_1_times_10(self):
        self.assertEqual(run_calculator('1', '*', '10'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '1*10 = 10',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_1_times_11(self):
        self.assertEqual(run_calculator('1', '*', '11'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '1*11 = 11',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_1_times_12(self):
        self.assertEqual(run_calculator('1', '*', '12'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '1*12 = 12',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_1_times_13(self):
        self.assertEqual(run_calculator('1', '*', '13'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '1*13 = 13',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_1_times_14(self):
        self.assertEqual(run_calculator('1', '*', '14'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '1*14 = 14',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_1_times_15(self):
        self.assertEqual(run_calculator('1', '*', '15'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '1*15 = 15',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_1_times_16(self):
        self.assertEqual(run_calculator('1', '*', '16'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '1*16 = 16',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_1_times_17(self):
        self.assertEqual(run_calculator('1', '*', '17'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '1*17 = 17',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_1_times_18(self):
        self.assertEqual(run_calculator('1', '*', '18'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '1*18 = 18',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_1_times_19(self):
        self.assertEqual(run_calculator('1', '*', '19'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '1*19 = 19',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_1_times_20(self):
        self.assertEqual(run_calculator('1', '*', '20'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '1*20 = 20',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_1_times_21(self):
        self.assertEqual(run_calculator('1', '*', '21'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '1*21 = 21',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_1_times_22(self):
        self.assertEqual(run_calculator('1', '*', '22'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '1*22 = 22',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_1_times_23(self):
        self.assertEqual(run_calculator('1', '*', '23'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '1*23 = 23',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_1_times_24(self):
        self.assertEqual(run_calculator('1', '*', '24'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '1*24 = 24',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_1_times_25(self):
        self.assertEqual(run_calculator('1', '*', '25'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '1*25 = 25',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_1_times_26(self):
        self.assertEqual(run_calculator('1', '*', '26'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '1*26 = 26',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_1_times_27(self):
        self.assertEqual(run_calculator('1', '*', '27'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '1*27 = 27',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_1_times_28(self):
        self.assertEqual(run_calculator('1', '*', '28'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '1*28 = 28',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_1_times_29(self):
        self.assertEqual(run_calculator('1', '*', '29'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '1*29 = 29',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_1_times_30(self):
        self.assertEqual(run_calculator('1', '*', '30'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '1*30 = 30',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_1_times_31(self):
        self.assertEqual(run_calculator('1', '*', '31'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '1*31 = 31',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_1_times_32(self):
        self.assertEqual(run_calculator('1', '*', '32'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '1*32 = 32',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_1_times_33(self):
        self.assertEqual(run_calculator('1', '*', '33'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '1*33 = 33',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_1_times_34(self):
        self.assertEqual(run_calculator('1', '*', '34'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '1*34 = 34',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_1_times_35(self):
        self.assertEqual(run_calculator('1', '*', '35'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '1*35 = 35',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_1_times_36(self):
        self.assertEqual(run_calculator('1', '*', '36'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '1*36 = 36',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_1_times_37(self):
        self.assertEqual(run_calculator('1', '*', '37'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '1*37 = 37',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_1_times_38(self):
        self.assertEqual(run_calculator('1', '*', '38'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '1*38 = 38',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_1_times_39(self):
        self.assertEqual(run_calculator('1', '*', '39'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '1*39 = 39',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_1_times_40(self):
        self.assertEqual(run_calculator('1', '*', '40'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '1*40 = 40',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_1_times_41(self):
        self.assertEqual(run_calculator('1', '*', '41'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '1*41 = 41',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_1_times_42(self):
        self.assertEqual(run_calculator('1', '*', '42'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '1*42 = 42',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_1_times_43(self):
        self.assertEqual(run_calculator('1', '*', '43'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '1*43 = 43',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_1_times_44(self):
        self.assertEqual(run_calculator('1', '*', '44'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '1*44 = 44',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_1_times_45(self):
        self.assertEqual(run_calculator('1', '*', '45'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '1*45 = 45',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_1_times_46(self):
        self.assertEqual(run_calculator('1', '*', '46'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '1*46 = 46',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_1_times_47(self):
        self.assertEqual(run_calculator('1', '*', '47'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '1*47 = 47',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_1_times_48(self):
        self.assertEqual(run_calculator('1', '*', '48'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '1*48 = 48',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_1_times_49(self):
        self.assertEqual(run_calculator('1', '*', '49'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '1*49 = 49',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_1_times_50(self):
        self.assertEqual(run_calculator('1', '*', '50'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '1*50 = 50',
            'Thanks for using this calculator, goodbye :)',
        ])


if __name__ == '__main__':
    unittest.main()
