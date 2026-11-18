# test_minus_19.py
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


class TestMinus19(unittest.TestCase):

    def test_19_minus_0(self):
        self.assertEqual(run_calculator('19', '-', '0'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '19-0 = 19',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_19_minus_1(self):
        self.assertEqual(run_calculator('19', '-', '1'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '19-1 = 18',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_19_minus_2(self):
        self.assertEqual(run_calculator('19', '-', '2'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '19-2 = 17',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_19_minus_3(self):
        self.assertEqual(run_calculator('19', '-', '3'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '19-3 = 16',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_19_minus_4(self):
        self.assertEqual(run_calculator('19', '-', '4'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '19-4 = 15',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_19_minus_5(self):
        self.assertEqual(run_calculator('19', '-', '5'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '19-5 = 14',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_19_minus_6(self):
        self.assertEqual(run_calculator('19', '-', '6'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '19-6 = 13',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_19_minus_7(self):
        self.assertEqual(run_calculator('19', '-', '7'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '19-7 = 12',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_19_minus_8(self):
        self.assertEqual(run_calculator('19', '-', '8'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '19-8 = 11',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_19_minus_9(self):
        self.assertEqual(run_calculator('19', '-', '9'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '19-9 = 10',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_19_minus_10(self):
        self.assertEqual(run_calculator('19', '-', '10'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '19-10 = 9',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_19_minus_11(self):
        self.assertEqual(run_calculator('19', '-', '11'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '19-11 = 8',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_19_minus_12(self):
        self.assertEqual(run_calculator('19', '-', '12'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '19-12 = 7',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_19_minus_13(self):
        self.assertEqual(run_calculator('19', '-', '13'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '19-13 = 6',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_19_minus_14(self):
        self.assertEqual(run_calculator('19', '-', '14'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '19-14 = 5',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_19_minus_15(self):
        self.assertEqual(run_calculator('19', '-', '15'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '19-15 = 4',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_19_minus_16(self):
        self.assertEqual(run_calculator('19', '-', '16'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '19-16 = 3',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_19_minus_17(self):
        self.assertEqual(run_calculator('19', '-', '17'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '19-17 = 2',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_19_minus_18(self):
        self.assertEqual(run_calculator('19', '-', '18'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '19-18 = 1',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_19_minus_19(self):
        self.assertEqual(run_calculator('19', '-', '19'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '19-19 = 0',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_19_minus_20(self):
        self.assertEqual(run_calculator('19', '-', '20'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '19-20 = -1',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_19_minus_21(self):
        self.assertEqual(run_calculator('19', '-', '21'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '19-21 = -2',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_19_minus_22(self):
        self.assertEqual(run_calculator('19', '-', '22'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '19-22 = -3',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_19_minus_23(self):
        self.assertEqual(run_calculator('19', '-', '23'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '19-23 = -4',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_19_minus_24(self):
        self.assertEqual(run_calculator('19', '-', '24'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '19-24 = -5',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_19_minus_25(self):
        self.assertEqual(run_calculator('19', '-', '25'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '19-25 = -6',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_19_minus_26(self):
        self.assertEqual(run_calculator('19', '-', '26'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '19-26 = -7',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_19_minus_27(self):
        self.assertEqual(run_calculator('19', '-', '27'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '19-27 = -8',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_19_minus_28(self):
        self.assertEqual(run_calculator('19', '-', '28'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '19-28 = -9',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_19_minus_29(self):
        self.assertEqual(run_calculator('19', '-', '29'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '19-29 = -10',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_19_minus_30(self):
        self.assertEqual(run_calculator('19', '-', '30'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '19-30 = -11',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_19_minus_31(self):
        self.assertEqual(run_calculator('19', '-', '31'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '19-31 = -12',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_19_minus_32(self):
        self.assertEqual(run_calculator('19', '-', '32'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '19-32 = -13',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_19_minus_33(self):
        self.assertEqual(run_calculator('19', '-', '33'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '19-33 = -14',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_19_minus_34(self):
        self.assertEqual(run_calculator('19', '-', '34'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '19-34 = -15',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_19_minus_35(self):
        self.assertEqual(run_calculator('19', '-', '35'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '19-35 = -16',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_19_minus_36(self):
        self.assertEqual(run_calculator('19', '-', '36'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '19-36 = -17',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_19_minus_37(self):
        self.assertEqual(run_calculator('19', '-', '37'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '19-37 = -18',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_19_minus_38(self):
        self.assertEqual(run_calculator('19', '-', '38'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '19-38 = -19',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_19_minus_39(self):
        self.assertEqual(run_calculator('19', '-', '39'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '19-39 = -20',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_19_minus_40(self):
        self.assertEqual(run_calculator('19', '-', '40'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '19-40 = -21',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_19_minus_41(self):
        self.assertEqual(run_calculator('19', '-', '41'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '19-41 = -22',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_19_minus_42(self):
        self.assertEqual(run_calculator('19', '-', '42'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '19-42 = -23',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_19_minus_43(self):
        self.assertEqual(run_calculator('19', '-', '43'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '19-43 = -24',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_19_minus_44(self):
        self.assertEqual(run_calculator('19', '-', '44'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '19-44 = -25',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_19_minus_45(self):
        self.assertEqual(run_calculator('19', '-', '45'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '19-45 = -26',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_19_minus_46(self):
        self.assertEqual(run_calculator('19', '-', '46'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '19-46 = -27',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_19_minus_47(self):
        self.assertEqual(run_calculator('19', '-', '47'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '19-47 = -28',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_19_minus_48(self):
        self.assertEqual(run_calculator('19', '-', '48'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '19-48 = -29',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_19_minus_49(self):
        self.assertEqual(run_calculator('19', '-', '49'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '19-49 = -30',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_19_minus_50(self):
        self.assertEqual(run_calculator('19', '-', '50'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '19-50 = -31',
            'Thanks for using this calculator, goodbye :)',
        ])


if __name__ == '__main__':
    unittest.main()
