# test_times_0.py
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


class TestTimes0(unittest.TestCase):

    def test_0_times_0(self):
        self.assertEqual(run_calculator('0', '*', '0'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '0*0 = 0',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_0_times_1(self):
        self.assertEqual(run_calculator('0', '*', '1'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '0*1 = 0',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_0_times_2(self):
        self.assertEqual(run_calculator('0', '*', '2'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '0*2 = 0',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_0_times_3(self):
        self.assertEqual(run_calculator('0', '*', '3'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '0*3 = 0',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_0_times_4(self):
        self.assertEqual(run_calculator('0', '*', '4'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '0*4 = 0',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_0_times_5(self):
        self.assertEqual(run_calculator('0', '*', '5'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '0*5 = 0',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_0_times_6(self):
        self.assertEqual(run_calculator('0', '*', '6'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '0*6 = 0',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_0_times_7(self):
        self.assertEqual(run_calculator('0', '*', '7'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '0*7 = 0',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_0_times_8(self):
        self.assertEqual(run_calculator('0', '*', '8'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '0*8 = 0',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_0_times_9(self):
        self.assertEqual(run_calculator('0', '*', '9'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '0*9 = 0',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_0_times_10(self):
        self.assertEqual(run_calculator('0', '*', '10'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '0*10 = 0',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_0_times_11(self):
        self.assertEqual(run_calculator('0', '*', '11'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '0*11 = 0',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_0_times_12(self):
        self.assertEqual(run_calculator('0', '*', '12'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '0*12 = 0',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_0_times_13(self):
        self.assertEqual(run_calculator('0', '*', '13'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '0*13 = 0',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_0_times_14(self):
        self.assertEqual(run_calculator('0', '*', '14'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '0*14 = 0',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_0_times_15(self):
        self.assertEqual(run_calculator('0', '*', '15'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '0*15 = 0',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_0_times_16(self):
        self.assertEqual(run_calculator('0', '*', '16'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '0*16 = 0',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_0_times_17(self):
        self.assertEqual(run_calculator('0', '*', '17'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '0*17 = 0',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_0_times_18(self):
        self.assertEqual(run_calculator('0', '*', '18'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '0*18 = 0',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_0_times_19(self):
        self.assertEqual(run_calculator('0', '*', '19'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '0*19 = 0',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_0_times_20(self):
        self.assertEqual(run_calculator('0', '*', '20'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '0*20 = 0',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_0_times_21(self):
        self.assertEqual(run_calculator('0', '*', '21'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '0*21 = 0',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_0_times_22(self):
        self.assertEqual(run_calculator('0', '*', '22'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '0*22 = 0',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_0_times_23(self):
        self.assertEqual(run_calculator('0', '*', '23'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '0*23 = 0',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_0_times_24(self):
        self.assertEqual(run_calculator('0', '*', '24'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '0*24 = 0',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_0_times_25(self):
        self.assertEqual(run_calculator('0', '*', '25'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '0*25 = 0',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_0_times_26(self):
        self.assertEqual(run_calculator('0', '*', '26'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '0*26 = 0',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_0_times_27(self):
        self.assertEqual(run_calculator('0', '*', '27'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '0*27 = 0',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_0_times_28(self):
        self.assertEqual(run_calculator('0', '*', '28'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '0*28 = 0',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_0_times_29(self):
        self.assertEqual(run_calculator('0', '*', '29'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '0*29 = 0',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_0_times_30(self):
        self.assertEqual(run_calculator('0', '*', '30'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '0*30 = 0',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_0_times_31(self):
        self.assertEqual(run_calculator('0', '*', '31'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '0*31 = 0',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_0_times_32(self):
        self.assertEqual(run_calculator('0', '*', '32'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '0*32 = 0',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_0_times_33(self):
        self.assertEqual(run_calculator('0', '*', '33'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '0*33 = 0',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_0_times_34(self):
        self.assertEqual(run_calculator('0', '*', '34'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '0*34 = 0',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_0_times_35(self):
        self.assertEqual(run_calculator('0', '*', '35'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '0*35 = 0',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_0_times_36(self):
        self.assertEqual(run_calculator('0', '*', '36'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '0*36 = 0',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_0_times_37(self):
        self.assertEqual(run_calculator('0', '*', '37'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '0*37 = 0',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_0_times_38(self):
        self.assertEqual(run_calculator('0', '*', '38'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '0*38 = 0',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_0_times_39(self):
        self.assertEqual(run_calculator('0', '*', '39'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '0*39 = 0',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_0_times_40(self):
        self.assertEqual(run_calculator('0', '*', '40'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '0*40 = 0',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_0_times_41(self):
        self.assertEqual(run_calculator('0', '*', '41'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '0*41 = 0',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_0_times_42(self):
        self.assertEqual(run_calculator('0', '*', '42'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '0*42 = 0',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_0_times_43(self):
        self.assertEqual(run_calculator('0', '*', '43'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '0*43 = 0',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_0_times_44(self):
        self.assertEqual(run_calculator('0', '*', '44'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '0*44 = 0',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_0_times_45(self):
        self.assertEqual(run_calculator('0', '*', '45'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '0*45 = 0',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_0_times_46(self):
        self.assertEqual(run_calculator('0', '*', '46'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '0*46 = 0',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_0_times_47(self):
        self.assertEqual(run_calculator('0', '*', '47'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '0*47 = 0',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_0_times_48(self):
        self.assertEqual(run_calculator('0', '*', '48'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '0*48 = 0',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_0_times_49(self):
        self.assertEqual(run_calculator('0', '*', '49'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '0*49 = 0',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_0_times_50(self):
        self.assertEqual(run_calculator('0', '*', '50'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '0*50 = 0',
            'Thanks for using this calculator, goodbye :)',
        ])


if __name__ == '__main__':
    unittest.main()
