# test_times_25.py
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


class TestTimes25(unittest.TestCase):

    def test_25_times_0(self):
        self.assertEqual(run_calculator('25', '*', '0'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '25*0 = 0',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_25_times_1(self):
        self.assertEqual(run_calculator('25', '*', '1'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '25*1 = 25',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_25_times_2(self):
        self.assertEqual(run_calculator('25', '*', '2'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '25*2 = 50',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_25_times_3(self):
        self.assertEqual(run_calculator('25', '*', '3'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '25*3 = 75',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_25_times_4(self):
        self.assertEqual(run_calculator('25', '*', '4'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '25*4 = 100',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_25_times_5(self):
        self.assertEqual(run_calculator('25', '*', '5'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '25*5 = 125',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_25_times_6(self):
        self.assertEqual(run_calculator('25', '*', '6'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '25*6 = 150',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_25_times_7(self):
        self.assertEqual(run_calculator('25', '*', '7'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '25*7 = 175',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_25_times_8(self):
        self.assertEqual(run_calculator('25', '*', '8'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '25*8 = 200',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_25_times_9(self):
        self.assertEqual(run_calculator('25', '*', '9'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '25*9 = 225',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_25_times_10(self):
        self.assertEqual(run_calculator('25', '*', '10'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '25*10 = 250',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_25_times_11(self):
        self.assertEqual(run_calculator('25', '*', '11'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '25*11 = 275',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_25_times_12(self):
        self.assertEqual(run_calculator('25', '*', '12'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '25*12 = 300',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_25_times_13(self):
        self.assertEqual(run_calculator('25', '*', '13'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '25*13 = 325',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_25_times_14(self):
        self.assertEqual(run_calculator('25', '*', '14'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '25*14 = 350',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_25_times_15(self):
        self.assertEqual(run_calculator('25', '*', '15'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '25*15 = 375',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_25_times_16(self):
        self.assertEqual(run_calculator('25', '*', '16'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '25*16 = 400',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_25_times_17(self):
        self.assertEqual(run_calculator('25', '*', '17'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '25*17 = 425',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_25_times_18(self):
        self.assertEqual(run_calculator('25', '*', '18'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '25*18 = 450',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_25_times_19(self):
        self.assertEqual(run_calculator('25', '*', '19'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '25*19 = 475',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_25_times_20(self):
        self.assertEqual(run_calculator('25', '*', '20'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '25*20 = 500',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_25_times_21(self):
        self.assertEqual(run_calculator('25', '*', '21'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '25*21 = 525',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_25_times_22(self):
        self.assertEqual(run_calculator('25', '*', '22'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '25*22 = 550',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_25_times_23(self):
        self.assertEqual(run_calculator('25', '*', '23'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '25*23 = 575',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_25_times_24(self):
        self.assertEqual(run_calculator('25', '*', '24'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '25*24 = 600',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_25_times_25(self):
        self.assertEqual(run_calculator('25', '*', '25'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '25*25 = 625',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_25_times_26(self):
        self.assertEqual(run_calculator('25', '*', '26'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '25*26 = 650',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_25_times_27(self):
        self.assertEqual(run_calculator('25', '*', '27'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '25*27 = 675',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_25_times_28(self):
        self.assertEqual(run_calculator('25', '*', '28'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '25*28 = 700',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_25_times_29(self):
        self.assertEqual(run_calculator('25', '*', '29'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '25*29 = 725',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_25_times_30(self):
        self.assertEqual(run_calculator('25', '*', '30'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '25*30 = 750',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_25_times_31(self):
        self.assertEqual(run_calculator('25', '*', '31'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '25*31 = 775',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_25_times_32(self):
        self.assertEqual(run_calculator('25', '*', '32'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '25*32 = 800',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_25_times_33(self):
        self.assertEqual(run_calculator('25', '*', '33'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '25*33 = 825',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_25_times_34(self):
        self.assertEqual(run_calculator('25', '*', '34'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '25*34 = 850',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_25_times_35(self):
        self.assertEqual(run_calculator('25', '*', '35'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '25*35 = 875',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_25_times_36(self):
        self.assertEqual(run_calculator('25', '*', '36'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '25*36 = 900',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_25_times_37(self):
        self.assertEqual(run_calculator('25', '*', '37'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '25*37 = 925',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_25_times_38(self):
        self.assertEqual(run_calculator('25', '*', '38'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '25*38 = 950',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_25_times_39(self):
        self.assertEqual(run_calculator('25', '*', '39'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '25*39 = 975',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_25_times_40(self):
        self.assertEqual(run_calculator('25', '*', '40'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '25*40 = 1000',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_25_times_41(self):
        self.assertEqual(run_calculator('25', '*', '41'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '25*41 = 1025',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_25_times_42(self):
        self.assertEqual(run_calculator('25', '*', '42'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '25*42 = 1050',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_25_times_43(self):
        self.assertEqual(run_calculator('25', '*', '43'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '25*43 = 1075',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_25_times_44(self):
        self.assertEqual(run_calculator('25', '*', '44'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '25*44 = 1100',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_25_times_45(self):
        self.assertEqual(run_calculator('25', '*', '45'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '25*45 = 1125',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_25_times_46(self):
        self.assertEqual(run_calculator('25', '*', '46'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '25*46 = 1150',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_25_times_47(self):
        self.assertEqual(run_calculator('25', '*', '47'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '25*47 = 1175',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_25_times_48(self):
        self.assertEqual(run_calculator('25', '*', '48'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '25*48 = 1200',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_25_times_49(self):
        self.assertEqual(run_calculator('25', '*', '49'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '25*49 = 1225',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_25_times_50(self):
        self.assertEqual(run_calculator('25', '*', '50'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '25*50 = 1250',
            'Thanks for using this calculator, goodbye :)',
        ])


if __name__ == '__main__':
    unittest.main()
