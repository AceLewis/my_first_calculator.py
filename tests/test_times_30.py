# test_times_30.py
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


class TestTimes30(unittest.TestCase):

    def test_30_times_0(self):
        self.assertEqual(run_calculator('30', '*', '0'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '30*0 = 0',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_30_times_1(self):
        self.assertEqual(run_calculator('30', '*', '1'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '30*1 = 30',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_30_times_2(self):
        self.assertEqual(run_calculator('30', '*', '2'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '30*2 = 60',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_30_times_3(self):
        self.assertEqual(run_calculator('30', '*', '3'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '30*3 = 90',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_30_times_4(self):
        self.assertEqual(run_calculator('30', '*', '4'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '30*4 = 120',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_30_times_5(self):
        self.assertEqual(run_calculator('30', '*', '5'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '30*5 = 150',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_30_times_6(self):
        self.assertEqual(run_calculator('30', '*', '6'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '30*6 = 180',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_30_times_7(self):
        self.assertEqual(run_calculator('30', '*', '7'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '30*7 = 210',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_30_times_8(self):
        self.assertEqual(run_calculator('30', '*', '8'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '30*8 = 240',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_30_times_9(self):
        self.assertEqual(run_calculator('30', '*', '9'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '30*9 = 270',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_30_times_10(self):
        self.assertEqual(run_calculator('30', '*', '10'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '30*10 = 300',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_30_times_11(self):
        self.assertEqual(run_calculator('30', '*', '11'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '30*11 = 330',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_30_times_12(self):
        self.assertEqual(run_calculator('30', '*', '12'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '30*12 = 360',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_30_times_13(self):
        self.assertEqual(run_calculator('30', '*', '13'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '30*13 = 390',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_30_times_14(self):
        self.assertEqual(run_calculator('30', '*', '14'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '30*14 = 420',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_30_times_15(self):
        self.assertEqual(run_calculator('30', '*', '15'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '30*15 = 450',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_30_times_16(self):
        self.assertEqual(run_calculator('30', '*', '16'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '30*16 = 480',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_30_times_17(self):
        self.assertEqual(run_calculator('30', '*', '17'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '30*17 = 510',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_30_times_18(self):
        self.assertEqual(run_calculator('30', '*', '18'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '30*18 = 540',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_30_times_19(self):
        self.assertEqual(run_calculator('30', '*', '19'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '30*19 = 570',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_30_times_20(self):
        self.assertEqual(run_calculator('30', '*', '20'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '30*20 = 600',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_30_times_21(self):
        self.assertEqual(run_calculator('30', '*', '21'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '30*21 = 630',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_30_times_22(self):
        self.assertEqual(run_calculator('30', '*', '22'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '30*22 = 660',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_30_times_23(self):
        self.assertEqual(run_calculator('30', '*', '23'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '30*23 = 690',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_30_times_24(self):
        self.assertEqual(run_calculator('30', '*', '24'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '30*24 = 720',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_30_times_25(self):
        self.assertEqual(run_calculator('30', '*', '25'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '30*25 = 750',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_30_times_26(self):
        self.assertEqual(run_calculator('30', '*', '26'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '30*26 = 780',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_30_times_27(self):
        self.assertEqual(run_calculator('30', '*', '27'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '30*27 = 810',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_30_times_28(self):
        self.assertEqual(run_calculator('30', '*', '28'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '30*28 = 840',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_30_times_29(self):
        self.assertEqual(run_calculator('30', '*', '29'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '30*29 = 870',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_30_times_30(self):
        self.assertEqual(run_calculator('30', '*', '30'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '30*30 = 900',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_30_times_31(self):
        self.assertEqual(run_calculator('30', '*', '31'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '30*31 = 930',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_30_times_32(self):
        self.assertEqual(run_calculator('30', '*', '32'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '30*32 = 960',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_30_times_33(self):
        self.assertEqual(run_calculator('30', '*', '33'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '30*33 = 990',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_30_times_34(self):
        self.assertEqual(run_calculator('30', '*', '34'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '30*34 = 1020',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_30_times_35(self):
        self.assertEqual(run_calculator('30', '*', '35'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '30*35 = 1050',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_30_times_36(self):
        self.assertEqual(run_calculator('30', '*', '36'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '30*36 = 1080',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_30_times_37(self):
        self.assertEqual(run_calculator('30', '*', '37'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '30*37 = 1110',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_30_times_38(self):
        self.assertEqual(run_calculator('30', '*', '38'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '30*38 = 1140',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_30_times_39(self):
        self.assertEqual(run_calculator('30', '*', '39'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '30*39 = 1170',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_30_times_40(self):
        self.assertEqual(run_calculator('30', '*', '40'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '30*40 = 1200',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_30_times_41(self):
        self.assertEqual(run_calculator('30', '*', '41'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '30*41 = 1230',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_30_times_42(self):
        self.assertEqual(run_calculator('30', '*', '42'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '30*42 = 1260',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_30_times_43(self):
        self.assertEqual(run_calculator('30', '*', '43'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '30*43 = 1290',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_30_times_44(self):
        self.assertEqual(run_calculator('30', '*', '44'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '30*44 = 1320',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_30_times_45(self):
        self.assertEqual(run_calculator('30', '*', '45'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '30*45 = 1350',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_30_times_46(self):
        self.assertEqual(run_calculator('30', '*', '46'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '30*46 = 1380',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_30_times_47(self):
        self.assertEqual(run_calculator('30', '*', '47'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '30*47 = 1410',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_30_times_48(self):
        self.assertEqual(run_calculator('30', '*', '48'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '30*48 = 1440',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_30_times_49(self):
        self.assertEqual(run_calculator('30', '*', '49'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '30*49 = 1470',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_30_times_50(self):
        self.assertEqual(run_calculator('30', '*', '50'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '30*50 = 1500',
            'Thanks for using this calculator, goodbye :)',
        ])


if __name__ == '__main__':
    unittest.main()
