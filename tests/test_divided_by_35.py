# test_divided_by_35.py
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


class TestDividedBy35(unittest.TestCase):

    def test_35_divided_by_0(self):
        self.assertEqual(run_calculator('35', '/', '0'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '35/0 = Inf',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_35_divided_by_1(self):
        self.assertEqual(run_calculator('35', '/', '1'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '35/1 = 35',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_35_divided_by_2(self):
        self.assertEqual(run_calculator('35', '/', '2'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '35/2 = 17.5',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_35_divided_by_3(self):
        self.assertEqual(run_calculator('35', '/', '3'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '35/3 = 11.66666666666666666666666667',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_35_divided_by_4(self):
        self.assertEqual(run_calculator('35', '/', '4'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '35/4 = 8.75',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_35_divided_by_5(self):
        self.assertEqual(run_calculator('35', '/', '5'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '35/5 = 7',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_35_divided_by_6(self):
        self.assertEqual(run_calculator('35', '/', '6'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '35/6 = 5.833333333333333333333333333',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_35_divided_by_7(self):
        self.assertEqual(run_calculator('35', '/', '7'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '35/7 = 5',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_35_divided_by_8(self):
        self.assertEqual(run_calculator('35', '/', '8'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '35/8 = 4.375',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_35_divided_by_9(self):
        self.assertEqual(run_calculator('35', '/', '9'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '35/9 = 3.888888888888888888888888889',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_35_divided_by_10(self):
        self.assertEqual(run_calculator('35', '/', '10'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '35/10 = 3.5',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_35_divided_by_11(self):
        self.assertEqual(run_calculator('35', '/', '11'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '35/11 = 3.181818181818181818181818182',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_35_divided_by_12(self):
        self.assertEqual(run_calculator('35', '/', '12'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '35/12 = 2.916666666666666666666666667',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_35_divided_by_13(self):
        self.assertEqual(run_calculator('35', '/', '13'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '35/13 = 2.692307692307692307692307692',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_35_divided_by_14(self):
        self.assertEqual(run_calculator('35', '/', '14'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '35/14 = 2.5',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_35_divided_by_15(self):
        self.assertEqual(run_calculator('35', '/', '15'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '35/15 = 2.333333333333333333333333333',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_35_divided_by_16(self):
        self.assertEqual(run_calculator('35', '/', '16'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '35/16 = 2.1875',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_35_divided_by_17(self):
        self.assertEqual(run_calculator('35', '/', '17'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '35/17 = 2.058823529411764705882352941',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_35_divided_by_18(self):
        self.assertEqual(run_calculator('35', '/', '18'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '35/18 = 1.944444444444444444444444444',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_35_divided_by_19(self):
        self.assertEqual(run_calculator('35', '/', '19'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '35/19 = 1.842105263157894736842105263',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_35_divided_by_20(self):
        self.assertEqual(run_calculator('35', '/', '20'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '35/20 = 1.75',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_35_divided_by_21(self):
        self.assertEqual(run_calculator('35', '/', '21'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '35/21 = 1.666666666666666666666666667',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_35_divided_by_22(self):
        self.assertEqual(run_calculator('35', '/', '22'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '35/22 = 1.590909090909090909090909091',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_35_divided_by_23(self):
        self.assertEqual(run_calculator('35', '/', '23'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '35/23 = 1.521739130434782608695652174',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_35_divided_by_24(self):
        self.assertEqual(run_calculator('35', '/', '24'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '35/24 = 1.458333333333333333333333333',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_35_divided_by_25(self):
        self.assertEqual(run_calculator('35', '/', '25'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '35/25 = 1.4',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_35_divided_by_26(self):
        self.assertEqual(run_calculator('35', '/', '26'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '35/26 = 1.346153846153846153846153846',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_35_divided_by_27(self):
        self.assertEqual(run_calculator('35', '/', '27'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '35/27 = 1.296296296296296296296296296',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_35_divided_by_28(self):
        self.assertEqual(run_calculator('35', '/', '28'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '35/28 = 1.25',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_35_divided_by_29(self):
        self.assertEqual(run_calculator('35', '/', '29'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '35/29 = 1.206896551724137931034482759',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_35_divided_by_30(self):
        self.assertEqual(run_calculator('35', '/', '30'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '35/30 = 1.166666666666666666666666667',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_35_divided_by_31(self):
        self.assertEqual(run_calculator('35', '/', '31'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '35/31 = 1.129032258064516129032258065',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_35_divided_by_32(self):
        self.assertEqual(run_calculator('35', '/', '32'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '35/32 = 1.09375',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_35_divided_by_33(self):
        self.assertEqual(run_calculator('35', '/', '33'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '35/33 = 1.060606060606060606060606061',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_35_divided_by_34(self):
        self.assertEqual(run_calculator('35', '/', '34'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '35/34 = 1.029411764705882352941176471',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_35_divided_by_35(self):
        self.assertEqual(run_calculator('35', '/', '35'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '35/35 = 1',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_35_divided_by_36(self):
        self.assertEqual(run_calculator('35', '/', '36'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '35/36 = 0.9722222222222222222222222222',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_35_divided_by_37(self):
        self.assertEqual(run_calculator('35', '/', '37'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '35/37 = 0.9459459459459459459459459459',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_35_divided_by_38(self):
        self.assertEqual(run_calculator('35', '/', '38'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '35/38 = 0.9210526315789473684210526316',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_35_divided_by_39(self):
        self.assertEqual(run_calculator('35', '/', '39'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '35/39 = 0.8974358974358974358974358974',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_35_divided_by_40(self):
        self.assertEqual(run_calculator('35', '/', '40'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '35/40 = 0.875',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_35_divided_by_41(self):
        self.assertEqual(run_calculator('35', '/', '41'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '35/41 = 0.8536585365853658536585365854',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_35_divided_by_42(self):
        self.assertEqual(run_calculator('35', '/', '42'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '35/42 = 0.8333333333333333333333333333',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_35_divided_by_43(self):
        self.assertEqual(run_calculator('35', '/', '43'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '35/43 = 0.8139534883720930232558139535',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_35_divided_by_44(self):
        self.assertEqual(run_calculator('35', '/', '44'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '35/44 = 0.7954545454545454545454545455',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_35_divided_by_45(self):
        self.assertEqual(run_calculator('35', '/', '45'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '35/45 = 0.7777777777777777777777777778',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_35_divided_by_46(self):
        self.assertEqual(run_calculator('35', '/', '46'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '35/46 = 0.7608695652173913043478260870',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_35_divided_by_47(self):
        self.assertEqual(run_calculator('35', '/', '47'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '35/47 = 0.7446808510638297872340425532',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_35_divided_by_48(self):
        self.assertEqual(run_calculator('35', '/', '48'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '35/48 = 0.7291666666666666666666666667',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_35_divided_by_49(self):
        self.assertEqual(run_calculator('35', '/', '49'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '35/49 = 0.7142857142857142857142857143',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_35_divided_by_50(self):
        self.assertEqual(run_calculator('35', '/', '50'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '35/50 = 0.7',
            'Thanks for using this calculator, goodbye :)',
        ])


if __name__ == '__main__':
    unittest.main()
