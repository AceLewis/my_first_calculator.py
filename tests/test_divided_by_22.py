# test_divided_by_22.py
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


class TestDividedBy22(unittest.TestCase):

    def test_22_divided_by_0(self):
        self.assertEqual(run_calculator('22', '/', '0'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '22/0 = Inf',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_22_divided_by_1(self):
        self.assertEqual(run_calculator('22', '/', '1'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '22/1 = 22',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_22_divided_by_2(self):
        self.assertEqual(run_calculator('22', '/', '2'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '22/2 = 11',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_22_divided_by_3(self):
        self.assertEqual(run_calculator('22', '/', '3'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '22/3 = 7.333333333333333333333333333',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_22_divided_by_4(self):
        self.assertEqual(run_calculator('22', '/', '4'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '22/4 = 5.5',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_22_divided_by_5(self):
        self.assertEqual(run_calculator('22', '/', '5'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '22/5 = 4.4',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_22_divided_by_6(self):
        self.assertEqual(run_calculator('22', '/', '6'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '22/6 = 3.666666666666666666666666667',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_22_divided_by_7(self):
        self.assertEqual(run_calculator('22', '/', '7'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '22/7 = 3.142857142857142857142857143',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_22_divided_by_8(self):
        self.assertEqual(run_calculator('22', '/', '8'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '22/8 = 2.75',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_22_divided_by_9(self):
        self.assertEqual(run_calculator('22', '/', '9'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '22/9 = 2.444444444444444444444444444',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_22_divided_by_10(self):
        self.assertEqual(run_calculator('22', '/', '10'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '22/10 = 2.2',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_22_divided_by_11(self):
        self.assertEqual(run_calculator('22', '/', '11'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '22/11 = 2',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_22_divided_by_12(self):
        self.assertEqual(run_calculator('22', '/', '12'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '22/12 = 1.833333333333333333333333333',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_22_divided_by_13(self):
        self.assertEqual(run_calculator('22', '/', '13'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '22/13 = 1.692307692307692307692307692',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_22_divided_by_14(self):
        self.assertEqual(run_calculator('22', '/', '14'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '22/14 = 1.571428571428571428571428571',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_22_divided_by_15(self):
        self.assertEqual(run_calculator('22', '/', '15'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '22/15 = 1.466666666666666666666666667',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_22_divided_by_16(self):
        self.assertEqual(run_calculator('22', '/', '16'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '22/16 = 1.375',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_22_divided_by_17(self):
        self.assertEqual(run_calculator('22', '/', '17'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '22/17 = 1.294117647058823529411764706',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_22_divided_by_18(self):
        self.assertEqual(run_calculator('22', '/', '18'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '22/18 = 1.222222222222222222222222222',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_22_divided_by_19(self):
        self.assertEqual(run_calculator('22', '/', '19'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '22/19 = 1.157894736842105263157894737',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_22_divided_by_20(self):
        self.assertEqual(run_calculator('22', '/', '20'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '22/20 = 1.1',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_22_divided_by_21(self):
        self.assertEqual(run_calculator('22', '/', '21'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '22/21 = 1.047619047619047619047619048',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_22_divided_by_22(self):
        self.assertEqual(run_calculator('22', '/', '22'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '22/22 = 1',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_22_divided_by_23(self):
        self.assertEqual(run_calculator('22', '/', '23'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '22/23 = 0.9565217391304347826086956522',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_22_divided_by_24(self):
        self.assertEqual(run_calculator('22', '/', '24'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '22/24 = 0.9166666666666666666666666667',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_22_divided_by_25(self):
        self.assertEqual(run_calculator('22', '/', '25'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '22/25 = 0.88',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_22_divided_by_26(self):
        self.assertEqual(run_calculator('22', '/', '26'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '22/26 = 0.8461538461538461538461538462',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_22_divided_by_27(self):
        self.assertEqual(run_calculator('22', '/', '27'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '22/27 = 0.8148148148148148148148148148',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_22_divided_by_28(self):
        self.assertEqual(run_calculator('22', '/', '28'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '22/28 = 0.7857142857142857142857142857',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_22_divided_by_29(self):
        self.assertEqual(run_calculator('22', '/', '29'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '22/29 = 0.7586206896551724137931034483',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_22_divided_by_30(self):
        self.assertEqual(run_calculator('22', '/', '30'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '22/30 = 0.7333333333333333333333333333',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_22_divided_by_31(self):
        self.assertEqual(run_calculator('22', '/', '31'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '22/31 = 0.7096774193548387096774193548',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_22_divided_by_32(self):
        self.assertEqual(run_calculator('22', '/', '32'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '22/32 = 0.6875',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_22_divided_by_33(self):
        self.assertEqual(run_calculator('22', '/', '33'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '22/33 = 0.6666666666666666666666666667',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_22_divided_by_34(self):
        self.assertEqual(run_calculator('22', '/', '34'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '22/34 = 0.6470588235294117647058823529',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_22_divided_by_35(self):
        self.assertEqual(run_calculator('22', '/', '35'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '22/35 = 0.6285714285714285714285714286',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_22_divided_by_36(self):
        self.assertEqual(run_calculator('22', '/', '36'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '22/36 = 0.6111111111111111111111111111',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_22_divided_by_37(self):
        self.assertEqual(run_calculator('22', '/', '37'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '22/37 = 0.5945945945945945945945945946',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_22_divided_by_38(self):
        self.assertEqual(run_calculator('22', '/', '38'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '22/38 = 0.5789473684210526315789473684',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_22_divided_by_39(self):
        self.assertEqual(run_calculator('22', '/', '39'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '22/39 = 0.5641025641025641025641025641',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_22_divided_by_40(self):
        self.assertEqual(run_calculator('22', '/', '40'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '22/40 = 0.55',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_22_divided_by_41(self):
        self.assertEqual(run_calculator('22', '/', '41'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '22/41 = 0.5365853658536585365853658537',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_22_divided_by_42(self):
        self.assertEqual(run_calculator('22', '/', '42'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '22/42 = 0.5238095238095238095238095238',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_22_divided_by_43(self):
        self.assertEqual(run_calculator('22', '/', '43'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '22/43 = 0.5116279069767441860465116279',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_22_divided_by_44(self):
        self.assertEqual(run_calculator('22', '/', '44'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '22/44 = 0.5',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_22_divided_by_45(self):
        self.assertEqual(run_calculator('22', '/', '45'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '22/45 = 0.4888888888888888888888888889',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_22_divided_by_46(self):
        self.assertEqual(run_calculator('22', '/', '46'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '22/46 = 0.4782608695652173913043478261',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_22_divided_by_47(self):
        self.assertEqual(run_calculator('22', '/', '47'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '22/47 = 0.4680851063829787234042553191',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_22_divided_by_48(self):
        self.assertEqual(run_calculator('22', '/', '48'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '22/48 = 0.4583333333333333333333333333',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_22_divided_by_49(self):
        self.assertEqual(run_calculator('22', '/', '49'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '22/49 = 0.4489795918367346938775510204',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_22_divided_by_50(self):
        self.assertEqual(run_calculator('22', '/', '50'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '22/50 = 0.44',
            'Thanks for using this calculator, goodbye :)',
        ])


if __name__ == '__main__':
    unittest.main()
