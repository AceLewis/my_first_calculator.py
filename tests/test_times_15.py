# test_times_15.py
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


class TestTimes15(unittest.TestCase):

    def test_15_times_0(self):
        self.assertEqual(run_calculator('15', '*', '0'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '15*0 = 0',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_15_times_1(self):
        self.assertEqual(run_calculator('15', '*', '1'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '15*1 = 15',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_15_times_2(self):
        self.assertEqual(run_calculator('15', '*', '2'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '15*2 = 30',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_15_times_3(self):
        self.assertEqual(run_calculator('15', '*', '3'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '15*3 = 45',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_15_times_4(self):
        self.assertEqual(run_calculator('15', '*', '4'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '15*4 = 60',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_15_times_5(self):
        self.assertEqual(run_calculator('15', '*', '5'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '15*5 = 75',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_15_times_6(self):
        self.assertEqual(run_calculator('15', '*', '6'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '15*6 = 90',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_15_times_7(self):
        self.assertEqual(run_calculator('15', '*', '7'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '15*7 = 105',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_15_times_8(self):
        self.assertEqual(run_calculator('15', '*', '8'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '15*8 = 120',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_15_times_9(self):
        self.assertEqual(run_calculator('15', '*', '9'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '15*9 = 135',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_15_times_10(self):
        self.assertEqual(run_calculator('15', '*', '10'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '15*10 = 150',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_15_times_11(self):
        self.assertEqual(run_calculator('15', '*', '11'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '15*11 = 165',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_15_times_12(self):
        self.assertEqual(run_calculator('15', '*', '12'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '15*12 = 180',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_15_times_13(self):
        self.assertEqual(run_calculator('15', '*', '13'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '15*13 = 195',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_15_times_14(self):
        self.assertEqual(run_calculator('15', '*', '14'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '15*14 = 210',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_15_times_15(self):
        self.assertEqual(run_calculator('15', '*', '15'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '15*15 = 225',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_15_times_16(self):
        self.assertEqual(run_calculator('15', '*', '16'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '15*16 = 240',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_15_times_17(self):
        self.assertEqual(run_calculator('15', '*', '17'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '15*17 = 255',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_15_times_18(self):
        self.assertEqual(run_calculator('15', '*', '18'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '15*18 = 270',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_15_times_19(self):
        self.assertEqual(run_calculator('15', '*', '19'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '15*19 = 285',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_15_times_20(self):
        self.assertEqual(run_calculator('15', '*', '20'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '15*20 = 300',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_15_times_21(self):
        self.assertEqual(run_calculator('15', '*', '21'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '15*21 = 315',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_15_times_22(self):
        self.assertEqual(run_calculator('15', '*', '22'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '15*22 = 330',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_15_times_23(self):
        self.assertEqual(run_calculator('15', '*', '23'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '15*23 = 345',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_15_times_24(self):
        self.assertEqual(run_calculator('15', '*', '24'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '15*24 = 360',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_15_times_25(self):
        self.assertEqual(run_calculator('15', '*', '25'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '15*25 = 375',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_15_times_26(self):
        self.assertEqual(run_calculator('15', '*', '26'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '15*26 = 390',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_15_times_27(self):
        self.assertEqual(run_calculator('15', '*', '27'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '15*27 = 405',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_15_times_28(self):
        self.assertEqual(run_calculator('15', '*', '28'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '15*28 = 420',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_15_times_29(self):
        self.assertEqual(run_calculator('15', '*', '29'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '15*29 = 435',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_15_times_30(self):
        self.assertEqual(run_calculator('15', '*', '30'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '15*30 = 450',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_15_times_31(self):
        self.assertEqual(run_calculator('15', '*', '31'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '15*31 = 465',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_15_times_32(self):
        self.assertEqual(run_calculator('15', '*', '32'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '15*32 = 480',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_15_times_33(self):
        self.assertEqual(run_calculator('15', '*', '33'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '15*33 = 495',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_15_times_34(self):
        self.assertEqual(run_calculator('15', '*', '34'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '15*34 = 510',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_15_times_35(self):
        self.assertEqual(run_calculator('15', '*', '35'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '15*35 = 525',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_15_times_36(self):
        self.assertEqual(run_calculator('15', '*', '36'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '15*36 = 540',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_15_times_37(self):
        self.assertEqual(run_calculator('15', '*', '37'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '15*37 = 555',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_15_times_38(self):
        self.assertEqual(run_calculator('15', '*', '38'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '15*38 = 570',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_15_times_39(self):
        self.assertEqual(run_calculator('15', '*', '39'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '15*39 = 585',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_15_times_40(self):
        self.assertEqual(run_calculator('15', '*', '40'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '15*40 = 600',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_15_times_41(self):
        self.assertEqual(run_calculator('15', '*', '41'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '15*41 = 615',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_15_times_42(self):
        self.assertEqual(run_calculator('15', '*', '42'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '15*42 = 630',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_15_times_43(self):
        self.assertEqual(run_calculator('15', '*', '43'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '15*43 = 645',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_15_times_44(self):
        self.assertEqual(run_calculator('15', '*', '44'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '15*44 = 660',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_15_times_45(self):
        self.assertEqual(run_calculator('15', '*', '45'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '15*45 = 675',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_15_times_46(self):
        self.assertEqual(run_calculator('15', '*', '46'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '15*46 = 690',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_15_times_47(self):
        self.assertEqual(run_calculator('15', '*', '47'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '15*47 = 705',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_15_times_48(self):
        self.assertEqual(run_calculator('15', '*', '48'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '15*48 = 720',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_15_times_49(self):
        self.assertEqual(run_calculator('15', '*', '49'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '15*49 = 735',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_15_times_50(self):
        self.assertEqual(run_calculator('15', '*', '50'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '15*50 = 750',
            'Thanks for using this calculator, goodbye :)',
        ])


if __name__ == '__main__':
    unittest.main()
