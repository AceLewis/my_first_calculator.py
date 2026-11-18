# test_minus_49.py
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


class TestMinus49(unittest.TestCase):

    def test_49_minus_0(self):
        self.assertEqual(run_calculator('49', '-', '0'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '49-0 = 49',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_49_minus_1(self):
        self.assertEqual(run_calculator('49', '-', '1'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '49-1 = 48',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_49_minus_2(self):
        self.assertEqual(run_calculator('49', '-', '2'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '49-2 = 47',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_49_minus_3(self):
        self.assertEqual(run_calculator('49', '-', '3'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '49-3 = 46',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_49_minus_4(self):
        self.assertEqual(run_calculator('49', '-', '4'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '49-4 = 45',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_49_minus_5(self):
        self.assertEqual(run_calculator('49', '-', '5'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '49-5 = 44',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_49_minus_6(self):
        self.assertEqual(run_calculator('49', '-', '6'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '49-6 = 43',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_49_minus_7(self):
        self.assertEqual(run_calculator('49', '-', '7'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '49-7 = 42',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_49_minus_8(self):
        self.assertEqual(run_calculator('49', '-', '8'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '49-8 = 41',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_49_minus_9(self):
        self.assertEqual(run_calculator('49', '-', '9'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '49-9 = 40',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_49_minus_10(self):
        self.assertEqual(run_calculator('49', '-', '10'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '49-10 = 39',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_49_minus_11(self):
        self.assertEqual(run_calculator('49', '-', '11'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '49-11 = 38',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_49_minus_12(self):
        self.assertEqual(run_calculator('49', '-', '12'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '49-12 = 37',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_49_minus_13(self):
        self.assertEqual(run_calculator('49', '-', '13'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '49-13 = 36',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_49_minus_14(self):
        self.assertEqual(run_calculator('49', '-', '14'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '49-14 = 35',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_49_minus_15(self):
        self.assertEqual(run_calculator('49', '-', '15'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '49-15 = 34',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_49_minus_16(self):
        self.assertEqual(run_calculator('49', '-', '16'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '49-16 = 33',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_49_minus_17(self):
        self.assertEqual(run_calculator('49', '-', '17'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '49-17 = 32',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_49_minus_18(self):
        self.assertEqual(run_calculator('49', '-', '18'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '49-18 = 31',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_49_minus_19(self):
        self.assertEqual(run_calculator('49', '-', '19'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '49-19 = 30',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_49_minus_20(self):
        self.assertEqual(run_calculator('49', '-', '20'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '49-20 = 29',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_49_minus_21(self):
        self.assertEqual(run_calculator('49', '-', '21'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '49-21 = 28',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_49_minus_22(self):
        self.assertEqual(run_calculator('49', '-', '22'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '49-22 = 27',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_49_minus_23(self):
        self.assertEqual(run_calculator('49', '-', '23'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '49-23 = 26',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_49_minus_24(self):
        self.assertEqual(run_calculator('49', '-', '24'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '49-24 = 25',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_49_minus_25(self):
        self.assertEqual(run_calculator('49', '-', '25'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '49-25 = 24',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_49_minus_26(self):
        self.assertEqual(run_calculator('49', '-', '26'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '49-26 = 23',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_49_minus_27(self):
        self.assertEqual(run_calculator('49', '-', '27'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '49-27 = 22',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_49_minus_28(self):
        self.assertEqual(run_calculator('49', '-', '28'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '49-28 = 21',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_49_minus_29(self):
        self.assertEqual(run_calculator('49', '-', '29'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '49-29 = 20',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_49_minus_30(self):
        self.assertEqual(run_calculator('49', '-', '30'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '49-30 = 19',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_49_minus_31(self):
        self.assertEqual(run_calculator('49', '-', '31'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '49-31 = 18',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_49_minus_32(self):
        self.assertEqual(run_calculator('49', '-', '32'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '49-32 = 17',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_49_minus_33(self):
        self.assertEqual(run_calculator('49', '-', '33'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '49-33 = 16',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_49_minus_34(self):
        self.assertEqual(run_calculator('49', '-', '34'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '49-34 = 15',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_49_minus_35(self):
        self.assertEqual(run_calculator('49', '-', '35'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '49-35 = 14',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_49_minus_36(self):
        self.assertEqual(run_calculator('49', '-', '36'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '49-36 = 13',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_49_minus_37(self):
        self.assertEqual(run_calculator('49', '-', '37'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '49-37 = 12',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_49_minus_38(self):
        self.assertEqual(run_calculator('49', '-', '38'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '49-38 = 11',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_49_minus_39(self):
        self.assertEqual(run_calculator('49', '-', '39'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '49-39 = 10',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_49_minus_40(self):
        self.assertEqual(run_calculator('49', '-', '40'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '49-40 = 9',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_49_minus_41(self):
        self.assertEqual(run_calculator('49', '-', '41'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '49-41 = 8',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_49_minus_42(self):
        self.assertEqual(run_calculator('49', '-', '42'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '49-42 = 7',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_49_minus_43(self):
        self.assertEqual(run_calculator('49', '-', '43'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '49-43 = 6',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_49_minus_44(self):
        self.assertEqual(run_calculator('49', '-', '44'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '49-44 = 5',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_49_minus_45(self):
        self.assertEqual(run_calculator('49', '-', '45'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '49-45 = 4',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_49_minus_46(self):
        self.assertEqual(run_calculator('49', '-', '46'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '49-46 = 3',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_49_minus_47(self):
        self.assertEqual(run_calculator('49', '-', '47'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '49-47 = 2',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_49_minus_48(self):
        self.assertEqual(run_calculator('49', '-', '48'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '49-48 = 1',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_49_minus_49(self):
        self.assertEqual(run_calculator('49', '-', '49'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '49-49 = 0',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_49_minus_50(self):
        self.assertEqual(run_calculator('49', '-', '50'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '49-50 = -1',
            'Thanks for using this calculator, goodbye :)',
        ])


if __name__ == '__main__':
    unittest.main()
