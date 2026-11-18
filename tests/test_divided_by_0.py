# test_divided_by_0.py
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


class TestDividedBy0(unittest.TestCase):

    def test_0_divided_by_0(self):
        self.assertEqual(run_calculator('0', '/', '0'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '0/0 = Undefined',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_0_divided_by_1(self):
        self.assertEqual(run_calculator('0', '/', '1'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '0/1 = 0',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_0_divided_by_2(self):
        self.assertEqual(run_calculator('0', '/', '2'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '0/2 = 0',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_0_divided_by_3(self):
        self.assertEqual(run_calculator('0', '/', '3'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '0/3 = 0',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_0_divided_by_4(self):
        self.assertEqual(run_calculator('0', '/', '4'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '0/4 = 0',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_0_divided_by_5(self):
        self.assertEqual(run_calculator('0', '/', '5'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '0/5 = 0',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_0_divided_by_6(self):
        self.assertEqual(run_calculator('0', '/', '6'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '0/6 = 0',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_0_divided_by_7(self):
        self.assertEqual(run_calculator('0', '/', '7'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '0/7 = 0',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_0_divided_by_8(self):
        self.assertEqual(run_calculator('0', '/', '8'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '0/8 = 0',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_0_divided_by_9(self):
        self.assertEqual(run_calculator('0', '/', '9'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '0/9 = 0',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_0_divided_by_10(self):
        self.assertEqual(run_calculator('0', '/', '10'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '0/10 = 0',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_0_divided_by_11(self):
        self.assertEqual(run_calculator('0', '/', '11'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '0/11 = 0',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_0_divided_by_12(self):
        self.assertEqual(run_calculator('0', '/', '12'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '0/12 = 0',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_0_divided_by_13(self):
        self.assertEqual(run_calculator('0', '/', '13'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '0/13 = 0',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_0_divided_by_14(self):
        self.assertEqual(run_calculator('0', '/', '14'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '0/14 = 0',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_0_divided_by_15(self):
        self.assertEqual(run_calculator('0', '/', '15'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '0/15 = 0',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_0_divided_by_16(self):
        self.assertEqual(run_calculator('0', '/', '16'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '0/16 = 0',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_0_divided_by_17(self):
        self.assertEqual(run_calculator('0', '/', '17'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '0/17 = 0',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_0_divided_by_18(self):
        self.assertEqual(run_calculator('0', '/', '18'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '0/18 = 0',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_0_divided_by_19(self):
        self.assertEqual(run_calculator('0', '/', '19'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '0/19 = 0',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_0_divided_by_20(self):
        self.assertEqual(run_calculator('0', '/', '20'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '0/20 = 0',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_0_divided_by_21(self):
        self.assertEqual(run_calculator('0', '/', '21'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '0/21 = 0',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_0_divided_by_22(self):
        self.assertEqual(run_calculator('0', '/', '22'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '0/22 = 0',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_0_divided_by_23(self):
        self.assertEqual(run_calculator('0', '/', '23'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '0/23 = 0',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_0_divided_by_24(self):
        self.assertEqual(run_calculator('0', '/', '24'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '0/24 = 0',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_0_divided_by_25(self):
        self.assertEqual(run_calculator('0', '/', '25'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '0/25 = 0',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_0_divided_by_26(self):
        self.assertEqual(run_calculator('0', '/', '26'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '0/26 = 0',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_0_divided_by_27(self):
        self.assertEqual(run_calculator('0', '/', '27'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '0/27 = 0',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_0_divided_by_28(self):
        self.assertEqual(run_calculator('0', '/', '28'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '0/28 = 0',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_0_divided_by_29(self):
        self.assertEqual(run_calculator('0', '/', '29'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '0/29 = 0',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_0_divided_by_30(self):
        self.assertEqual(run_calculator('0', '/', '30'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '0/30 = 0',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_0_divided_by_31(self):
        self.assertEqual(run_calculator('0', '/', '31'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '0/31 = 0',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_0_divided_by_32(self):
        self.assertEqual(run_calculator('0', '/', '32'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '0/32 = 0',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_0_divided_by_33(self):
        self.assertEqual(run_calculator('0', '/', '33'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '0/33 = 0',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_0_divided_by_34(self):
        self.assertEqual(run_calculator('0', '/', '34'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '0/34 = 0',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_0_divided_by_35(self):
        self.assertEqual(run_calculator('0', '/', '35'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '0/35 = 0',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_0_divided_by_36(self):
        self.assertEqual(run_calculator('0', '/', '36'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '0/36 = 0',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_0_divided_by_37(self):
        self.assertEqual(run_calculator('0', '/', '37'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '0/37 = 0',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_0_divided_by_38(self):
        self.assertEqual(run_calculator('0', '/', '38'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '0/38 = 0',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_0_divided_by_39(self):
        self.assertEqual(run_calculator('0', '/', '39'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '0/39 = 0',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_0_divided_by_40(self):
        self.assertEqual(run_calculator('0', '/', '40'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '0/40 = 0',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_0_divided_by_41(self):
        self.assertEqual(run_calculator('0', '/', '41'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '0/41 = 0',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_0_divided_by_42(self):
        self.assertEqual(run_calculator('0', '/', '42'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '0/42 = 0',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_0_divided_by_43(self):
        self.assertEqual(run_calculator('0', '/', '43'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '0/43 = 0',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_0_divided_by_44(self):
        self.assertEqual(run_calculator('0', '/', '44'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '0/44 = 0',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_0_divided_by_45(self):
        self.assertEqual(run_calculator('0', '/', '45'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '0/45 = 0',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_0_divided_by_46(self):
        self.assertEqual(run_calculator('0', '/', '46'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '0/46 = 0',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_0_divided_by_47(self):
        self.assertEqual(run_calculator('0', '/', '47'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '0/47 = 0',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_0_divided_by_48(self):
        self.assertEqual(run_calculator('0', '/', '48'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '0/48 = 0',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_0_divided_by_49(self):
        self.assertEqual(run_calculator('0', '/', '49'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '0/49 = 0',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_0_divided_by_50(self):
        self.assertEqual(run_calculator('0', '/', '50'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '0/50 = 0',
            'Thanks for using this calculator, goodbye :)',
        ])


if __name__ == '__main__':
    unittest.main()
