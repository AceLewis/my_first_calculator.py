# test_times_10.py
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


class TestTimes10(unittest.TestCase):

    def test_10_times_0(self):
        self.assertEqual(run_calculator('10', '*', '0'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '10*0 = 0',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_10_times_1(self):
        self.assertEqual(run_calculator('10', '*', '1'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '10*1 = 10',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_10_times_2(self):
        self.assertEqual(run_calculator('10', '*', '2'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '10*2 = 20',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_10_times_3(self):
        self.assertEqual(run_calculator('10', '*', '3'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '10*3 = 30',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_10_times_4(self):
        self.assertEqual(run_calculator('10', '*', '4'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '10*4 = 40',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_10_times_5(self):
        self.assertEqual(run_calculator('10', '*', '5'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '10*5 = 50',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_10_times_6(self):
        self.assertEqual(run_calculator('10', '*', '6'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '10*6 = 60',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_10_times_7(self):
        self.assertEqual(run_calculator('10', '*', '7'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '10*7 = 70',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_10_times_8(self):
        self.assertEqual(run_calculator('10', '*', '8'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '10*8 = 80',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_10_times_9(self):
        self.assertEqual(run_calculator('10', '*', '9'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '10*9 = 90',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_10_times_10(self):
        self.assertEqual(run_calculator('10', '*', '10'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '10*10 = 100',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_10_times_11(self):
        self.assertEqual(run_calculator('10', '*', '11'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '10*11 = 110',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_10_times_12(self):
        self.assertEqual(run_calculator('10', '*', '12'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '10*12 = 120',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_10_times_13(self):
        self.assertEqual(run_calculator('10', '*', '13'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '10*13 = 130',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_10_times_14(self):
        self.assertEqual(run_calculator('10', '*', '14'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '10*14 = 140',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_10_times_15(self):
        self.assertEqual(run_calculator('10', '*', '15'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '10*15 = 150',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_10_times_16(self):
        self.assertEqual(run_calculator('10', '*', '16'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '10*16 = 160',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_10_times_17(self):
        self.assertEqual(run_calculator('10', '*', '17'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '10*17 = 170',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_10_times_18(self):
        self.assertEqual(run_calculator('10', '*', '18'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '10*18 = 180',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_10_times_19(self):
        self.assertEqual(run_calculator('10', '*', '19'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '10*19 = 190',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_10_times_20(self):
        self.assertEqual(run_calculator('10', '*', '20'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '10*20 = 200',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_10_times_21(self):
        self.assertEqual(run_calculator('10', '*', '21'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '10*21 = 210',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_10_times_22(self):
        self.assertEqual(run_calculator('10', '*', '22'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '10*22 = 220',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_10_times_23(self):
        self.assertEqual(run_calculator('10', '*', '23'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '10*23 = 230',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_10_times_24(self):
        self.assertEqual(run_calculator('10', '*', '24'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '10*24 = 240',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_10_times_25(self):
        self.assertEqual(run_calculator('10', '*', '25'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '10*25 = 250',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_10_times_26(self):
        self.assertEqual(run_calculator('10', '*', '26'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '10*26 = 260',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_10_times_27(self):
        self.assertEqual(run_calculator('10', '*', '27'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '10*27 = 270',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_10_times_28(self):
        self.assertEqual(run_calculator('10', '*', '28'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '10*28 = 280',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_10_times_29(self):
        self.assertEqual(run_calculator('10', '*', '29'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '10*29 = 290',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_10_times_30(self):
        self.assertEqual(run_calculator('10', '*', '30'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '10*30 = 300',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_10_times_31(self):
        self.assertEqual(run_calculator('10', '*', '31'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '10*31 = 310',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_10_times_32(self):
        self.assertEqual(run_calculator('10', '*', '32'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '10*32 = 320',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_10_times_33(self):
        self.assertEqual(run_calculator('10', '*', '33'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '10*33 = 330',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_10_times_34(self):
        self.assertEqual(run_calculator('10', '*', '34'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '10*34 = 340',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_10_times_35(self):
        self.assertEqual(run_calculator('10', '*', '35'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '10*35 = 350',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_10_times_36(self):
        self.assertEqual(run_calculator('10', '*', '36'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '10*36 = 360',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_10_times_37(self):
        self.assertEqual(run_calculator('10', '*', '37'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '10*37 = 370',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_10_times_38(self):
        self.assertEqual(run_calculator('10', '*', '38'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '10*38 = 380',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_10_times_39(self):
        self.assertEqual(run_calculator('10', '*', '39'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '10*39 = 390',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_10_times_40(self):
        self.assertEqual(run_calculator('10', '*', '40'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '10*40 = 400',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_10_times_41(self):
        self.assertEqual(run_calculator('10', '*', '41'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '10*41 = 410',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_10_times_42(self):
        self.assertEqual(run_calculator('10', '*', '42'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '10*42 = 420',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_10_times_43(self):
        self.assertEqual(run_calculator('10', '*', '43'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '10*43 = 430',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_10_times_44(self):
        self.assertEqual(run_calculator('10', '*', '44'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '10*44 = 440',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_10_times_45(self):
        self.assertEqual(run_calculator('10', '*', '45'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '10*45 = 450',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_10_times_46(self):
        self.assertEqual(run_calculator('10', '*', '46'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '10*46 = 460',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_10_times_47(self):
        self.assertEqual(run_calculator('10', '*', '47'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '10*47 = 470',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_10_times_48(self):
        self.assertEqual(run_calculator('10', '*', '48'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '10*48 = 480',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_10_times_49(self):
        self.assertEqual(run_calculator('10', '*', '49'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '10*49 = 490',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_10_times_50(self):
        self.assertEqual(run_calculator('10', '*', '50'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '10*50 = 500',
            'Thanks for using this calculator, goodbye :)',
        ])


if __name__ == '__main__':
    unittest.main()
