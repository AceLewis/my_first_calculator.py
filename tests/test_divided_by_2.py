# test_divided_by_2.py
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


class TestDividedBy2(unittest.TestCase):

    def test_2_divided_by_0(self):
        self.assertEqual(run_calculator('2', '/', '0'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '2/0 = Inf',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_2_divided_by_1(self):
        self.assertEqual(run_calculator('2', '/', '1'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '2/1 = 2',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_2_divided_by_2(self):
        self.assertEqual(run_calculator('2', '/', '2'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '2/2 = 1',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_2_divided_by_3(self):
        self.assertEqual(run_calculator('2', '/', '3'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '2/3 = 0.6666666666666666666666666667',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_2_divided_by_4(self):
        self.assertEqual(run_calculator('2', '/', '4'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '2/4 = 0.5',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_2_divided_by_5(self):
        self.assertEqual(run_calculator('2', '/', '5'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '2/5 = 0.4',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_2_divided_by_6(self):
        self.assertEqual(run_calculator('2', '/', '6'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '2/6 = 0.3333333333333333333333333333',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_2_divided_by_7(self):
        self.assertEqual(run_calculator('2', '/', '7'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '2/7 = 0.2857142857142857142857142857',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_2_divided_by_8(self):
        self.assertEqual(run_calculator('2', '/', '8'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '2/8 = 0.25',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_2_divided_by_9(self):
        self.assertEqual(run_calculator('2', '/', '9'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '2/9 = 0.2222222222222222222222222222',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_2_divided_by_10(self):
        self.assertEqual(run_calculator('2', '/', '10'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '2/10 = 0.2',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_2_divided_by_11(self):
        self.assertEqual(run_calculator('2', '/', '11'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '2/11 = 0.1818181818181818181818181818',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_2_divided_by_12(self):
        self.assertEqual(run_calculator('2', '/', '12'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '2/12 = 0.1666666666666666666666666667',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_2_divided_by_13(self):
        self.assertEqual(run_calculator('2', '/', '13'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '2/13 = 0.1538461538461538461538461538',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_2_divided_by_14(self):
        self.assertEqual(run_calculator('2', '/', '14'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '2/14 = 0.1428571428571428571428571429',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_2_divided_by_15(self):
        self.assertEqual(run_calculator('2', '/', '15'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '2/15 = 0.1333333333333333333333333333',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_2_divided_by_16(self):
        self.assertEqual(run_calculator('2', '/', '16'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '2/16 = 0.125',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_2_divided_by_17(self):
        self.assertEqual(run_calculator('2', '/', '17'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '2/17 = 0.1176470588235294117647058824',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_2_divided_by_18(self):
        self.assertEqual(run_calculator('2', '/', '18'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '2/18 = 0.1111111111111111111111111111',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_2_divided_by_19(self):
        self.assertEqual(run_calculator('2', '/', '19'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '2/19 = 0.1052631578947368421052631579',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_2_divided_by_20(self):
        self.assertEqual(run_calculator('2', '/', '20'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '2/20 = 0.1',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_2_divided_by_21(self):
        self.assertEqual(run_calculator('2', '/', '21'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '2/21 = 0.09523809523809523809523809524',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_2_divided_by_22(self):
        self.assertEqual(run_calculator('2', '/', '22'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '2/22 = 0.09090909090909090909090909091',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_2_divided_by_23(self):
        self.assertEqual(run_calculator('2', '/', '23'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '2/23 = 0.08695652173913043478260869565',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_2_divided_by_24(self):
        self.assertEqual(run_calculator('2', '/', '24'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '2/24 = 0.08333333333333333333333333333',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_2_divided_by_25(self):
        self.assertEqual(run_calculator('2', '/', '25'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '2/25 = 0.08',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_2_divided_by_26(self):
        self.assertEqual(run_calculator('2', '/', '26'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '2/26 = 0.07692307692307692307692307692',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_2_divided_by_27(self):
        self.assertEqual(run_calculator('2', '/', '27'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '2/27 = 0.07407407407407407407407407407',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_2_divided_by_28(self):
        self.assertEqual(run_calculator('2', '/', '28'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '2/28 = 0.07142857142857142857142857143',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_2_divided_by_29(self):
        self.assertEqual(run_calculator('2', '/', '29'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '2/29 = 0.06896551724137931034482758621',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_2_divided_by_30(self):
        self.assertEqual(run_calculator('2', '/', '30'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '2/30 = 0.06666666666666666666666666667',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_2_divided_by_31(self):
        self.assertEqual(run_calculator('2', '/', '31'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '2/31 = 0.06451612903225806451612903226',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_2_divided_by_32(self):
        self.assertEqual(run_calculator('2', '/', '32'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '2/32 = 0.0625',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_2_divided_by_33(self):
        self.assertEqual(run_calculator('2', '/', '33'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '2/33 = 0.06060606060606060606060606061',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_2_divided_by_34(self):
        self.assertEqual(run_calculator('2', '/', '34'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '2/34 = 0.05882352941176470588235294118',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_2_divided_by_35(self):
        self.assertEqual(run_calculator('2', '/', '35'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '2/35 = 0.05714285714285714285714285714',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_2_divided_by_36(self):
        self.assertEqual(run_calculator('2', '/', '36'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '2/36 = 0.05555555555555555555555555556',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_2_divided_by_37(self):
        self.assertEqual(run_calculator('2', '/', '37'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '2/37 = 0.05405405405405405405405405405',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_2_divided_by_38(self):
        self.assertEqual(run_calculator('2', '/', '38'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '2/38 = 0.05263157894736842105263157895',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_2_divided_by_39(self):
        self.assertEqual(run_calculator('2', '/', '39'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '2/39 = 0.05128205128205128205128205128',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_2_divided_by_40(self):
        self.assertEqual(run_calculator('2', '/', '40'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '2/40 = 0.05',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_2_divided_by_41(self):
        self.assertEqual(run_calculator('2', '/', '41'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '2/41 = 0.04878048780487804878048780488',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_2_divided_by_42(self):
        self.assertEqual(run_calculator('2', '/', '42'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '2/42 = 0.04761904761904761904761904762',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_2_divided_by_43(self):
        self.assertEqual(run_calculator('2', '/', '43'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '2/43 = 0.04651162790697674418604651163',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_2_divided_by_44(self):
        self.assertEqual(run_calculator('2', '/', '44'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '2/44 = 0.04545454545454545454545454545',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_2_divided_by_45(self):
        self.assertEqual(run_calculator('2', '/', '45'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '2/45 = 0.04444444444444444444444444444',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_2_divided_by_46(self):
        self.assertEqual(run_calculator('2', '/', '46'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '2/46 = 0.04347826086956521739130434783',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_2_divided_by_47(self):
        self.assertEqual(run_calculator('2', '/', '47'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '2/47 = 0.04255319148936170212765957447',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_2_divided_by_48(self):
        self.assertEqual(run_calculator('2', '/', '48'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '2/48 = 0.04166666666666666666666666667',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_2_divided_by_49(self):
        self.assertEqual(run_calculator('2', '/', '49'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '2/49 = 0.04081632653061224489795918367',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_2_divided_by_50(self):
        self.assertEqual(run_calculator('2', '/', '50'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '2/50 = 0.04',
            'Thanks for using this calculator, goodbye :)',
        ])


if __name__ == '__main__':
    unittest.main()
