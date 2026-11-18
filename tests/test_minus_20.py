# test_minus_20.py
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


class TestMinus20(unittest.TestCase):

    def test_20_minus_0(self):
        self.assertEqual(run_calculator('20', '-', '0'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '20-0 = 20',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_20_minus_1(self):
        self.assertEqual(run_calculator('20', '-', '1'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '20-1 = 19',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_20_minus_2(self):
        self.assertEqual(run_calculator('20', '-', '2'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '20-2 = 18',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_20_minus_3(self):
        self.assertEqual(run_calculator('20', '-', '3'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '20-3 = 17',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_20_minus_4(self):
        self.assertEqual(run_calculator('20', '-', '4'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '20-4 = 16',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_20_minus_5(self):
        self.assertEqual(run_calculator('20', '-', '5'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '20-5 = 15',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_20_minus_6(self):
        self.assertEqual(run_calculator('20', '-', '6'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '20-6 = 14',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_20_minus_7(self):
        self.assertEqual(run_calculator('20', '-', '7'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '20-7 = 13',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_20_minus_8(self):
        self.assertEqual(run_calculator('20', '-', '8'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '20-8 = 12',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_20_minus_9(self):
        self.assertEqual(run_calculator('20', '-', '9'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '20-9 = 11',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_20_minus_10(self):
        self.assertEqual(run_calculator('20', '-', '10'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '20-10 = 10',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_20_minus_11(self):
        self.assertEqual(run_calculator('20', '-', '11'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '20-11 = 9',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_20_minus_12(self):
        self.assertEqual(run_calculator('20', '-', '12'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '20-12 = 8',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_20_minus_13(self):
        self.assertEqual(run_calculator('20', '-', '13'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '20-13 = 7',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_20_minus_14(self):
        self.assertEqual(run_calculator('20', '-', '14'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '20-14 = 6',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_20_minus_15(self):
        self.assertEqual(run_calculator('20', '-', '15'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '20-15 = 5',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_20_minus_16(self):
        self.assertEqual(run_calculator('20', '-', '16'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '20-16 = 4',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_20_minus_17(self):
        self.assertEqual(run_calculator('20', '-', '17'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '20-17 = 3',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_20_minus_18(self):
        self.assertEqual(run_calculator('20', '-', '18'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '20-18 = 2',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_20_minus_19(self):
        self.assertEqual(run_calculator('20', '-', '19'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '20-19 = 1',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_20_minus_20(self):
        self.assertEqual(run_calculator('20', '-', '20'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '20-20 = 0',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_20_minus_21(self):
        self.assertEqual(run_calculator('20', '-', '21'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '20-21 = -1',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_20_minus_22(self):
        self.assertEqual(run_calculator('20', '-', '22'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '20-22 = -2',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_20_minus_23(self):
        self.assertEqual(run_calculator('20', '-', '23'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '20-23 = -3',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_20_minus_24(self):
        self.assertEqual(run_calculator('20', '-', '24'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '20-24 = -4',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_20_minus_25(self):
        self.assertEqual(run_calculator('20', '-', '25'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '20-25 = -5',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_20_minus_26(self):
        self.assertEqual(run_calculator('20', '-', '26'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '20-26 = -6',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_20_minus_27(self):
        self.assertEqual(run_calculator('20', '-', '27'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '20-27 = -7',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_20_minus_28(self):
        self.assertEqual(run_calculator('20', '-', '28'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '20-28 = -8',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_20_minus_29(self):
        self.assertEqual(run_calculator('20', '-', '29'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '20-29 = -9',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_20_minus_30(self):
        self.assertEqual(run_calculator('20', '-', '30'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '20-30 = -10',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_20_minus_31(self):
        self.assertEqual(run_calculator('20', '-', '31'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '20-31 = -11',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_20_minus_32(self):
        self.assertEqual(run_calculator('20', '-', '32'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '20-32 = -12',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_20_minus_33(self):
        self.assertEqual(run_calculator('20', '-', '33'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '20-33 = -13',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_20_minus_34(self):
        self.assertEqual(run_calculator('20', '-', '34'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '20-34 = -14',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_20_minus_35(self):
        self.assertEqual(run_calculator('20', '-', '35'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '20-35 = -15',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_20_minus_36(self):
        self.assertEqual(run_calculator('20', '-', '36'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '20-36 = -16',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_20_minus_37(self):
        self.assertEqual(run_calculator('20', '-', '37'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '20-37 = -17',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_20_minus_38(self):
        self.assertEqual(run_calculator('20', '-', '38'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '20-38 = -18',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_20_minus_39(self):
        self.assertEqual(run_calculator('20', '-', '39'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '20-39 = -19',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_20_minus_40(self):
        self.assertEqual(run_calculator('20', '-', '40'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '20-40 = -20',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_20_minus_41(self):
        self.assertEqual(run_calculator('20', '-', '41'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '20-41 = -21',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_20_minus_42(self):
        self.assertEqual(run_calculator('20', '-', '42'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '20-42 = -22',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_20_minus_43(self):
        self.assertEqual(run_calculator('20', '-', '43'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '20-43 = -23',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_20_minus_44(self):
        self.assertEqual(run_calculator('20', '-', '44'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '20-44 = -24',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_20_minus_45(self):
        self.assertEqual(run_calculator('20', '-', '45'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '20-45 = -25',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_20_minus_46(self):
        self.assertEqual(run_calculator('20', '-', '46'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '20-46 = -26',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_20_minus_47(self):
        self.assertEqual(run_calculator('20', '-', '47'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '20-47 = -27',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_20_minus_48(self):
        self.assertEqual(run_calculator('20', '-', '48'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '20-48 = -28',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_20_minus_49(self):
        self.assertEqual(run_calculator('20', '-', '49'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '20-49 = -29',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_20_minus_50(self):
        self.assertEqual(run_calculator('20', '-', '50'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '20-50 = -30',
            'Thanks for using this calculator, goodbye :)',
        ])


if __name__ == '__main__':
    unittest.main()
