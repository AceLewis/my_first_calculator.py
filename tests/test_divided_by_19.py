# test_divided_by_19.py
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


class TestDividedBy19(unittest.TestCase):

    def test_19_divided_by_0(self):
        self.assertEqual(run_calculator('19', '/', '0'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '19/0 = Inf',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_19_divided_by_1(self):
        self.assertEqual(run_calculator('19', '/', '1'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '19/1 = 19',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_19_divided_by_2(self):
        self.assertEqual(run_calculator('19', '/', '2'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '19/2 = 9.5',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_19_divided_by_3(self):
        self.assertEqual(run_calculator('19', '/', '3'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '19/3 = 6.333333333333333333333333333',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_19_divided_by_4(self):
        self.assertEqual(run_calculator('19', '/', '4'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '19/4 = 4.75',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_19_divided_by_5(self):
        self.assertEqual(run_calculator('19', '/', '5'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '19/5 = 3.8',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_19_divided_by_6(self):
        self.assertEqual(run_calculator('19', '/', '6'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '19/6 = 3.166666666666666666666666667',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_19_divided_by_7(self):
        self.assertEqual(run_calculator('19', '/', '7'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '19/7 = 2.714285714285714285714285714',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_19_divided_by_8(self):
        self.assertEqual(run_calculator('19', '/', '8'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '19/8 = 2.375',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_19_divided_by_9(self):
        self.assertEqual(run_calculator('19', '/', '9'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '19/9 = 2.111111111111111111111111111',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_19_divided_by_10(self):
        self.assertEqual(run_calculator('19', '/', '10'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '19/10 = 1.9',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_19_divided_by_11(self):
        self.assertEqual(run_calculator('19', '/', '11'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '19/11 = 1.727272727272727272727272727',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_19_divided_by_12(self):
        self.assertEqual(run_calculator('19', '/', '12'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '19/12 = 1.583333333333333333333333333',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_19_divided_by_13(self):
        self.assertEqual(run_calculator('19', '/', '13'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '19/13 = 1.461538461538461538461538462',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_19_divided_by_14(self):
        self.assertEqual(run_calculator('19', '/', '14'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '19/14 = 1.357142857142857142857142857',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_19_divided_by_15(self):
        self.assertEqual(run_calculator('19', '/', '15'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '19/15 = 1.266666666666666666666666667',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_19_divided_by_16(self):
        self.assertEqual(run_calculator('19', '/', '16'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '19/16 = 1.1875',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_19_divided_by_17(self):
        self.assertEqual(run_calculator('19', '/', '17'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '19/17 = 1.117647058823529411764705882',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_19_divided_by_18(self):
        self.assertEqual(run_calculator('19', '/', '18'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '19/18 = 1.055555555555555555555555556',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_19_divided_by_19(self):
        self.assertEqual(run_calculator('19', '/', '19'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '19/19 = 1',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_19_divided_by_20(self):
        self.assertEqual(run_calculator('19', '/', '20'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '19/20 = 0.95',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_19_divided_by_21(self):
        self.assertEqual(run_calculator('19', '/', '21'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '19/21 = 0.9047619047619047619047619048',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_19_divided_by_22(self):
        self.assertEqual(run_calculator('19', '/', '22'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '19/22 = 0.8636363636363636363636363636',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_19_divided_by_23(self):
        self.assertEqual(run_calculator('19', '/', '23'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '19/23 = 0.8260869565217391304347826087',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_19_divided_by_24(self):
        self.assertEqual(run_calculator('19', '/', '24'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '19/24 = 0.7916666666666666666666666667',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_19_divided_by_25(self):
        self.assertEqual(run_calculator('19', '/', '25'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '19/25 = 0.76',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_19_divided_by_26(self):
        self.assertEqual(run_calculator('19', '/', '26'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '19/26 = 0.7307692307692307692307692308',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_19_divided_by_27(self):
        self.assertEqual(run_calculator('19', '/', '27'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '19/27 = 0.7037037037037037037037037037',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_19_divided_by_28(self):
        self.assertEqual(run_calculator('19', '/', '28'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '19/28 = 0.6785714285714285714285714286',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_19_divided_by_29(self):
        self.assertEqual(run_calculator('19', '/', '29'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '19/29 = 0.6551724137931034482758620690',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_19_divided_by_30(self):
        self.assertEqual(run_calculator('19', '/', '30'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '19/30 = 0.6333333333333333333333333333',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_19_divided_by_31(self):
        self.assertEqual(run_calculator('19', '/', '31'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '19/31 = 0.6129032258064516129032258065',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_19_divided_by_32(self):
        self.assertEqual(run_calculator('19', '/', '32'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '19/32 = 0.59375',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_19_divided_by_33(self):
        self.assertEqual(run_calculator('19', '/', '33'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '19/33 = 0.5757575757575757575757575758',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_19_divided_by_34(self):
        self.assertEqual(run_calculator('19', '/', '34'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '19/34 = 0.5588235294117647058823529412',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_19_divided_by_35(self):
        self.assertEqual(run_calculator('19', '/', '35'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '19/35 = 0.5428571428571428571428571429',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_19_divided_by_36(self):
        self.assertEqual(run_calculator('19', '/', '36'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '19/36 = 0.5277777777777777777777777778',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_19_divided_by_37(self):
        self.assertEqual(run_calculator('19', '/', '37'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '19/37 = 0.5135135135135135135135135135',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_19_divided_by_38(self):
        self.assertEqual(run_calculator('19', '/', '38'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '19/38 = 0.5',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_19_divided_by_39(self):
        self.assertEqual(run_calculator('19', '/', '39'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '19/39 = 0.4871794871794871794871794872',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_19_divided_by_40(self):
        self.assertEqual(run_calculator('19', '/', '40'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '19/40 = 0.475',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_19_divided_by_41(self):
        self.assertEqual(run_calculator('19', '/', '41'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '19/41 = 0.4634146341463414634146341463',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_19_divided_by_42(self):
        self.assertEqual(run_calculator('19', '/', '42'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '19/42 = 0.4523809523809523809523809524',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_19_divided_by_43(self):
        self.assertEqual(run_calculator('19', '/', '43'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '19/43 = 0.4418604651162790697674418605',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_19_divided_by_44(self):
        self.assertEqual(run_calculator('19', '/', '44'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '19/44 = 0.4318181818181818181818181818',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_19_divided_by_45(self):
        self.assertEqual(run_calculator('19', '/', '45'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '19/45 = 0.4222222222222222222222222222',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_19_divided_by_46(self):
        self.assertEqual(run_calculator('19', '/', '46'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '19/46 = 0.4130434782608695652173913043',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_19_divided_by_47(self):
        self.assertEqual(run_calculator('19', '/', '47'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '19/47 = 0.4042553191489361702127659574',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_19_divided_by_48(self):
        self.assertEqual(run_calculator('19', '/', '48'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '19/48 = 0.3958333333333333333333333333',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_19_divided_by_49(self):
        self.assertEqual(run_calculator('19', '/', '49'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '19/49 = 0.3877551020408163265306122449',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_19_divided_by_50(self):
        self.assertEqual(run_calculator('19', '/', '50'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '19/50 = 0.38',
            'Thanks for using this calculator, goodbye :)',
        ])


if __name__ == '__main__':
    unittest.main()
