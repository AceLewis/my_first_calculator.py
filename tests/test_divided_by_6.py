# test_divided_by_6.py
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


class TestDividedBy6(unittest.TestCase):

    def test_6_divided_by_0(self):
        self.assertEqual(run_calculator('6', '/', '0'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '6/0 = Inf',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_6_divided_by_1(self):
        self.assertEqual(run_calculator('6', '/', '1'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '6/1 = 6',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_6_divided_by_2(self):
        self.assertEqual(run_calculator('6', '/', '2'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '6/2 = 3',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_6_divided_by_3(self):
        self.assertEqual(run_calculator('6', '/', '3'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '6/3 = 2',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_6_divided_by_4(self):
        self.assertEqual(run_calculator('6', '/', '4'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '6/4 = 1.5',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_6_divided_by_5(self):
        self.assertEqual(run_calculator('6', '/', '5'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '6/5 = 1.2',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_6_divided_by_6(self):
        self.assertEqual(run_calculator('6', '/', '6'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '6/6 = 1',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_6_divided_by_7(self):
        self.assertEqual(run_calculator('6', '/', '7'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '6/7 = 0.8571428571428571428571428571',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_6_divided_by_8(self):
        self.assertEqual(run_calculator('6', '/', '8'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '6/8 = 0.75',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_6_divided_by_9(self):
        self.assertEqual(run_calculator('6', '/', '9'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '6/9 = 0.6666666666666666666666666667',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_6_divided_by_10(self):
        self.assertEqual(run_calculator('6', '/', '10'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '6/10 = 0.6',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_6_divided_by_11(self):
        self.assertEqual(run_calculator('6', '/', '11'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '6/11 = 0.5454545454545454545454545455',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_6_divided_by_12(self):
        self.assertEqual(run_calculator('6', '/', '12'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '6/12 = 0.5',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_6_divided_by_13(self):
        self.assertEqual(run_calculator('6', '/', '13'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '6/13 = 0.4615384615384615384615384615',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_6_divided_by_14(self):
        self.assertEqual(run_calculator('6', '/', '14'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '6/14 = 0.4285714285714285714285714286',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_6_divided_by_15(self):
        self.assertEqual(run_calculator('6', '/', '15'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '6/15 = 0.4',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_6_divided_by_16(self):
        self.assertEqual(run_calculator('6', '/', '16'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '6/16 = 0.375',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_6_divided_by_17(self):
        self.assertEqual(run_calculator('6', '/', '17'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '6/17 = 0.3529411764705882352941176471',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_6_divided_by_18(self):
        self.assertEqual(run_calculator('6', '/', '18'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '6/18 = 0.3333333333333333333333333333',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_6_divided_by_19(self):
        self.assertEqual(run_calculator('6', '/', '19'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '6/19 = 0.3157894736842105263157894737',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_6_divided_by_20(self):
        self.assertEqual(run_calculator('6', '/', '20'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '6/20 = 0.3',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_6_divided_by_21(self):
        self.assertEqual(run_calculator('6', '/', '21'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '6/21 = 0.2857142857142857142857142857',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_6_divided_by_22(self):
        self.assertEqual(run_calculator('6', '/', '22'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '6/22 = 0.2727272727272727272727272727',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_6_divided_by_23(self):
        self.assertEqual(run_calculator('6', '/', '23'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '6/23 = 0.2608695652173913043478260870',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_6_divided_by_24(self):
        self.assertEqual(run_calculator('6', '/', '24'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '6/24 = 0.25',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_6_divided_by_25(self):
        self.assertEqual(run_calculator('6', '/', '25'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '6/25 = 0.24',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_6_divided_by_26(self):
        self.assertEqual(run_calculator('6', '/', '26'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '6/26 = 0.2307692307692307692307692308',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_6_divided_by_27(self):
        self.assertEqual(run_calculator('6', '/', '27'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '6/27 = 0.2222222222222222222222222222',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_6_divided_by_28(self):
        self.assertEqual(run_calculator('6', '/', '28'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '6/28 = 0.2142857142857142857142857143',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_6_divided_by_29(self):
        self.assertEqual(run_calculator('6', '/', '29'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '6/29 = 0.2068965517241379310344827586',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_6_divided_by_30(self):
        self.assertEqual(run_calculator('6', '/', '30'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '6/30 = 0.2',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_6_divided_by_31(self):
        self.assertEqual(run_calculator('6', '/', '31'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '6/31 = 0.1935483870967741935483870968',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_6_divided_by_32(self):
        self.assertEqual(run_calculator('6', '/', '32'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '6/32 = 0.1875',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_6_divided_by_33(self):
        self.assertEqual(run_calculator('6', '/', '33'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '6/33 = 0.1818181818181818181818181818',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_6_divided_by_34(self):
        self.assertEqual(run_calculator('6', '/', '34'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '6/34 = 0.1764705882352941176470588235',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_6_divided_by_35(self):
        self.assertEqual(run_calculator('6', '/', '35'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '6/35 = 0.1714285714285714285714285714',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_6_divided_by_36(self):
        self.assertEqual(run_calculator('6', '/', '36'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '6/36 = 0.1666666666666666666666666667',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_6_divided_by_37(self):
        self.assertEqual(run_calculator('6', '/', '37'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '6/37 = 0.1621621621621621621621621622',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_6_divided_by_38(self):
        self.assertEqual(run_calculator('6', '/', '38'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '6/38 = 0.1578947368421052631578947368',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_6_divided_by_39(self):
        self.assertEqual(run_calculator('6', '/', '39'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '6/39 = 0.1538461538461538461538461538',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_6_divided_by_40(self):
        self.assertEqual(run_calculator('6', '/', '40'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '6/40 = 0.15',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_6_divided_by_41(self):
        self.assertEqual(run_calculator('6', '/', '41'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '6/41 = 0.1463414634146341463414634146',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_6_divided_by_42(self):
        self.assertEqual(run_calculator('6', '/', '42'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '6/42 = 0.1428571428571428571428571429',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_6_divided_by_43(self):
        self.assertEqual(run_calculator('6', '/', '43'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '6/43 = 0.1395348837209302325581395349',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_6_divided_by_44(self):
        self.assertEqual(run_calculator('6', '/', '44'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '6/44 = 0.1363636363636363636363636364',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_6_divided_by_45(self):
        self.assertEqual(run_calculator('6', '/', '45'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '6/45 = 0.1333333333333333333333333333',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_6_divided_by_46(self):
        self.assertEqual(run_calculator('6', '/', '46'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '6/46 = 0.1304347826086956521739130435',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_6_divided_by_47(self):
        self.assertEqual(run_calculator('6', '/', '47'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '6/47 = 0.1276595744680851063829787234',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_6_divided_by_48(self):
        self.assertEqual(run_calculator('6', '/', '48'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '6/48 = 0.125',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_6_divided_by_49(self):
        self.assertEqual(run_calculator('6', '/', '49'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '6/49 = 0.1224489795918367346938775510',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_6_divided_by_50(self):
        self.assertEqual(run_calculator('6', '/', '50'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '6/50 = 0.12',
            'Thanks for using this calculator, goodbye :)',
        ])


if __name__ == '__main__':
    unittest.main()
