# test_divided_by_38.py
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


class TestDividedBy38(unittest.TestCase):

    def test_38_divided_by_0(self):
        self.assertEqual(run_calculator('38', '/', '0'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '38/0 = Inf',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_38_divided_by_1(self):
        self.assertEqual(run_calculator('38', '/', '1'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '38/1 = 38',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_38_divided_by_2(self):
        self.assertEqual(run_calculator('38', '/', '2'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '38/2 = 19',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_38_divided_by_3(self):
        self.assertEqual(run_calculator('38', '/', '3'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '38/3 = 12.66666666666666666666666667',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_38_divided_by_4(self):
        self.assertEqual(run_calculator('38', '/', '4'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '38/4 = 9.5',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_38_divided_by_5(self):
        self.assertEqual(run_calculator('38', '/', '5'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '38/5 = 7.6',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_38_divided_by_6(self):
        self.assertEqual(run_calculator('38', '/', '6'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '38/6 = 6.333333333333333333333333333',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_38_divided_by_7(self):
        self.assertEqual(run_calculator('38', '/', '7'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '38/7 = 5.428571428571428571428571429',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_38_divided_by_8(self):
        self.assertEqual(run_calculator('38', '/', '8'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '38/8 = 4.75',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_38_divided_by_9(self):
        self.assertEqual(run_calculator('38', '/', '9'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '38/9 = 4.222222222222222222222222222',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_38_divided_by_10(self):
        self.assertEqual(run_calculator('38', '/', '10'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '38/10 = 3.8',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_38_divided_by_11(self):
        self.assertEqual(run_calculator('38', '/', '11'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '38/11 = 3.454545454545454545454545455',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_38_divided_by_12(self):
        self.assertEqual(run_calculator('38', '/', '12'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '38/12 = 3.166666666666666666666666667',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_38_divided_by_13(self):
        self.assertEqual(run_calculator('38', '/', '13'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '38/13 = 2.923076923076923076923076923',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_38_divided_by_14(self):
        self.assertEqual(run_calculator('38', '/', '14'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '38/14 = 2.714285714285714285714285714',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_38_divided_by_15(self):
        self.assertEqual(run_calculator('38', '/', '15'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '38/15 = 2.533333333333333333333333333',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_38_divided_by_16(self):
        self.assertEqual(run_calculator('38', '/', '16'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '38/16 = 2.375',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_38_divided_by_17(self):
        self.assertEqual(run_calculator('38', '/', '17'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '38/17 = 2.235294117647058823529411765',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_38_divided_by_18(self):
        self.assertEqual(run_calculator('38', '/', '18'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '38/18 = 2.111111111111111111111111111',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_38_divided_by_19(self):
        self.assertEqual(run_calculator('38', '/', '19'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '38/19 = 2',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_38_divided_by_20(self):
        self.assertEqual(run_calculator('38', '/', '20'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '38/20 = 1.9',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_38_divided_by_21(self):
        self.assertEqual(run_calculator('38', '/', '21'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '38/21 = 1.809523809523809523809523810',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_38_divided_by_22(self):
        self.assertEqual(run_calculator('38', '/', '22'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '38/22 = 1.727272727272727272727272727',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_38_divided_by_23(self):
        self.assertEqual(run_calculator('38', '/', '23'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '38/23 = 1.652173913043478260869565217',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_38_divided_by_24(self):
        self.assertEqual(run_calculator('38', '/', '24'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '38/24 = 1.583333333333333333333333333',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_38_divided_by_25(self):
        self.assertEqual(run_calculator('38', '/', '25'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '38/25 = 1.52',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_38_divided_by_26(self):
        self.assertEqual(run_calculator('38', '/', '26'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '38/26 = 1.461538461538461538461538462',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_38_divided_by_27(self):
        self.assertEqual(run_calculator('38', '/', '27'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '38/27 = 1.407407407407407407407407407',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_38_divided_by_28(self):
        self.assertEqual(run_calculator('38', '/', '28'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '38/28 = 1.357142857142857142857142857',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_38_divided_by_29(self):
        self.assertEqual(run_calculator('38', '/', '29'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '38/29 = 1.310344827586206896551724138',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_38_divided_by_30(self):
        self.assertEqual(run_calculator('38', '/', '30'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '38/30 = 1.266666666666666666666666667',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_38_divided_by_31(self):
        self.assertEqual(run_calculator('38', '/', '31'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '38/31 = 1.225806451612903225806451613',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_38_divided_by_32(self):
        self.assertEqual(run_calculator('38', '/', '32'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '38/32 = 1.1875',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_38_divided_by_33(self):
        self.assertEqual(run_calculator('38', '/', '33'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '38/33 = 1.151515151515151515151515152',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_38_divided_by_34(self):
        self.assertEqual(run_calculator('38', '/', '34'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '38/34 = 1.117647058823529411764705882',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_38_divided_by_35(self):
        self.assertEqual(run_calculator('38', '/', '35'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '38/35 = 1.085714285714285714285714286',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_38_divided_by_36(self):
        self.assertEqual(run_calculator('38', '/', '36'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '38/36 = 1.055555555555555555555555556',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_38_divided_by_37(self):
        self.assertEqual(run_calculator('38', '/', '37'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '38/37 = 1.027027027027027027027027027',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_38_divided_by_38(self):
        self.assertEqual(run_calculator('38', '/', '38'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '38/38 = 1',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_38_divided_by_39(self):
        self.assertEqual(run_calculator('38', '/', '39'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '38/39 = 0.9743589743589743589743589744',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_38_divided_by_40(self):
        self.assertEqual(run_calculator('38', '/', '40'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '38/40 = 0.95',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_38_divided_by_41(self):
        self.assertEqual(run_calculator('38', '/', '41'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '38/41 = 0.9268292682926829268292682927',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_38_divided_by_42(self):
        self.assertEqual(run_calculator('38', '/', '42'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '38/42 = 0.9047619047619047619047619048',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_38_divided_by_43(self):
        self.assertEqual(run_calculator('38', '/', '43'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '38/43 = 0.8837209302325581395348837209',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_38_divided_by_44(self):
        self.assertEqual(run_calculator('38', '/', '44'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '38/44 = 0.8636363636363636363636363636',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_38_divided_by_45(self):
        self.assertEqual(run_calculator('38', '/', '45'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '38/45 = 0.8444444444444444444444444444',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_38_divided_by_46(self):
        self.assertEqual(run_calculator('38', '/', '46'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '38/46 = 0.8260869565217391304347826087',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_38_divided_by_47(self):
        self.assertEqual(run_calculator('38', '/', '47'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '38/47 = 0.8085106382978723404255319149',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_38_divided_by_48(self):
        self.assertEqual(run_calculator('38', '/', '48'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '38/48 = 0.7916666666666666666666666667',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_38_divided_by_49(self):
        self.assertEqual(run_calculator('38', '/', '49'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '38/49 = 0.7755102040816326530612244898',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_38_divided_by_50(self):
        self.assertEqual(run_calculator('38', '/', '50'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '38/50 = 0.76',
            'Thanks for using this calculator, goodbye :)',
        ])


if __name__ == '__main__':
    unittest.main()
