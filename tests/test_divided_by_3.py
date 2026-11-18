# test_divided_by_3.py
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


class TestDividedBy3(unittest.TestCase):

    def test_3_divided_by_0(self):
        self.assertEqual(run_calculator('3', '/', '0'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '3/0 = Inf',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_3_divided_by_1(self):
        self.assertEqual(run_calculator('3', '/', '1'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '3/1 = 3',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_3_divided_by_2(self):
        self.assertEqual(run_calculator('3', '/', '2'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '3/2 = 1.5',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_3_divided_by_3(self):
        self.assertEqual(run_calculator('3', '/', '3'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '3/3 = 1',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_3_divided_by_4(self):
        self.assertEqual(run_calculator('3', '/', '4'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '3/4 = 0.75',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_3_divided_by_5(self):
        self.assertEqual(run_calculator('3', '/', '5'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '3/5 = 0.6',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_3_divided_by_6(self):
        self.assertEqual(run_calculator('3', '/', '6'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '3/6 = 0.5',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_3_divided_by_7(self):
        self.assertEqual(run_calculator('3', '/', '7'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '3/7 = 0.4285714285714285714285714286',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_3_divided_by_8(self):
        self.assertEqual(run_calculator('3', '/', '8'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '3/8 = 0.375',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_3_divided_by_9(self):
        self.assertEqual(run_calculator('3', '/', '9'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '3/9 = 0.3333333333333333333333333333',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_3_divided_by_10(self):
        self.assertEqual(run_calculator('3', '/', '10'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '3/10 = 0.3',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_3_divided_by_11(self):
        self.assertEqual(run_calculator('3', '/', '11'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '3/11 = 0.2727272727272727272727272727',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_3_divided_by_12(self):
        self.assertEqual(run_calculator('3', '/', '12'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '3/12 = 0.25',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_3_divided_by_13(self):
        self.assertEqual(run_calculator('3', '/', '13'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '3/13 = 0.2307692307692307692307692308',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_3_divided_by_14(self):
        self.assertEqual(run_calculator('3', '/', '14'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '3/14 = 0.2142857142857142857142857143',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_3_divided_by_15(self):
        self.assertEqual(run_calculator('3', '/', '15'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '3/15 = 0.2',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_3_divided_by_16(self):
        self.assertEqual(run_calculator('3', '/', '16'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '3/16 = 0.1875',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_3_divided_by_17(self):
        self.assertEqual(run_calculator('3', '/', '17'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '3/17 = 0.1764705882352941176470588235',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_3_divided_by_18(self):
        self.assertEqual(run_calculator('3', '/', '18'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '3/18 = 0.1666666666666666666666666667',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_3_divided_by_19(self):
        self.assertEqual(run_calculator('3', '/', '19'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '3/19 = 0.1578947368421052631578947368',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_3_divided_by_20(self):
        self.assertEqual(run_calculator('3', '/', '20'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '3/20 = 0.15',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_3_divided_by_21(self):
        self.assertEqual(run_calculator('3', '/', '21'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '3/21 = 0.1428571428571428571428571429',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_3_divided_by_22(self):
        self.assertEqual(run_calculator('3', '/', '22'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '3/22 = 0.1363636363636363636363636364',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_3_divided_by_23(self):
        self.assertEqual(run_calculator('3', '/', '23'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '3/23 = 0.1304347826086956521739130435',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_3_divided_by_24(self):
        self.assertEqual(run_calculator('3', '/', '24'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '3/24 = 0.125',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_3_divided_by_25(self):
        self.assertEqual(run_calculator('3', '/', '25'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '3/25 = 0.12',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_3_divided_by_26(self):
        self.assertEqual(run_calculator('3', '/', '26'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '3/26 = 0.1153846153846153846153846154',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_3_divided_by_27(self):
        self.assertEqual(run_calculator('3', '/', '27'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '3/27 = 0.1111111111111111111111111111',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_3_divided_by_28(self):
        self.assertEqual(run_calculator('3', '/', '28'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '3/28 = 0.1071428571428571428571428571',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_3_divided_by_29(self):
        self.assertEqual(run_calculator('3', '/', '29'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '3/29 = 0.1034482758620689655172413793',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_3_divided_by_30(self):
        self.assertEqual(run_calculator('3', '/', '30'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '3/30 = 0.1',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_3_divided_by_31(self):
        self.assertEqual(run_calculator('3', '/', '31'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '3/31 = 0.09677419354838709677419354839',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_3_divided_by_32(self):
        self.assertEqual(run_calculator('3', '/', '32'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '3/32 = 0.09375',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_3_divided_by_33(self):
        self.assertEqual(run_calculator('3', '/', '33'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '3/33 = 0.09090909090909090909090909091',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_3_divided_by_34(self):
        self.assertEqual(run_calculator('3', '/', '34'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '3/34 = 0.08823529411764705882352941176',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_3_divided_by_35(self):
        self.assertEqual(run_calculator('3', '/', '35'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '3/35 = 0.08571428571428571428571428571',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_3_divided_by_36(self):
        self.assertEqual(run_calculator('3', '/', '36'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '3/36 = 0.08333333333333333333333333333',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_3_divided_by_37(self):
        self.assertEqual(run_calculator('3', '/', '37'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '3/37 = 0.08108108108108108108108108108',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_3_divided_by_38(self):
        self.assertEqual(run_calculator('3', '/', '38'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '3/38 = 0.07894736842105263157894736842',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_3_divided_by_39(self):
        self.assertEqual(run_calculator('3', '/', '39'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '3/39 = 0.07692307692307692307692307692',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_3_divided_by_40(self):
        self.assertEqual(run_calculator('3', '/', '40'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '3/40 = 0.075',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_3_divided_by_41(self):
        self.assertEqual(run_calculator('3', '/', '41'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '3/41 = 0.07317073170731707317073170732',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_3_divided_by_42(self):
        self.assertEqual(run_calculator('3', '/', '42'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '3/42 = 0.07142857142857142857142857143',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_3_divided_by_43(self):
        self.assertEqual(run_calculator('3', '/', '43'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '3/43 = 0.06976744186046511627906976744',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_3_divided_by_44(self):
        self.assertEqual(run_calculator('3', '/', '44'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '3/44 = 0.06818181818181818181818181818',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_3_divided_by_45(self):
        self.assertEqual(run_calculator('3', '/', '45'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '3/45 = 0.06666666666666666666666666667',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_3_divided_by_46(self):
        self.assertEqual(run_calculator('3', '/', '46'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '3/46 = 0.06521739130434782608695652174',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_3_divided_by_47(self):
        self.assertEqual(run_calculator('3', '/', '47'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '3/47 = 0.06382978723404255319148936170',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_3_divided_by_48(self):
        self.assertEqual(run_calculator('3', '/', '48'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '3/48 = 0.0625',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_3_divided_by_49(self):
        self.assertEqual(run_calculator('3', '/', '49'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '3/49 = 0.06122448979591836734693877551',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_3_divided_by_50(self):
        self.assertEqual(run_calculator('3', '/', '50'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '3/50 = 0.06',
            'Thanks for using this calculator, goodbye :)',
        ])


if __name__ == '__main__':
    unittest.main()
