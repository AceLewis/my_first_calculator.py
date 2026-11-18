# test_divided_by_30.py
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


class TestDividedBy30(unittest.TestCase):

    def test_30_divided_by_0(self):
        self.assertEqual(run_calculator('30', '/', '0'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '30/0 = Inf',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_30_divided_by_1(self):
        self.assertEqual(run_calculator('30', '/', '1'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '30/1 = 30',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_30_divided_by_2(self):
        self.assertEqual(run_calculator('30', '/', '2'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '30/2 = 15',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_30_divided_by_3(self):
        self.assertEqual(run_calculator('30', '/', '3'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '30/3 = 10',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_30_divided_by_4(self):
        self.assertEqual(run_calculator('30', '/', '4'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '30/4 = 7.5',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_30_divided_by_5(self):
        self.assertEqual(run_calculator('30', '/', '5'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '30/5 = 6',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_30_divided_by_6(self):
        self.assertEqual(run_calculator('30', '/', '6'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '30/6 = 5',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_30_divided_by_7(self):
        self.assertEqual(run_calculator('30', '/', '7'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '30/7 = 4.285714285714285714285714286',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_30_divided_by_8(self):
        self.assertEqual(run_calculator('30', '/', '8'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '30/8 = 3.75',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_30_divided_by_9(self):
        self.assertEqual(run_calculator('30', '/', '9'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '30/9 = 3.333333333333333333333333333',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_30_divided_by_10(self):
        self.assertEqual(run_calculator('30', '/', '10'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '30/10 = 3',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_30_divided_by_11(self):
        self.assertEqual(run_calculator('30', '/', '11'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '30/11 = 2.727272727272727272727272727',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_30_divided_by_12(self):
        self.assertEqual(run_calculator('30', '/', '12'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '30/12 = 2.5',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_30_divided_by_13(self):
        self.assertEqual(run_calculator('30', '/', '13'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '30/13 = 2.307692307692307692307692308',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_30_divided_by_14(self):
        self.assertEqual(run_calculator('30', '/', '14'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '30/14 = 2.142857142857142857142857143',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_30_divided_by_15(self):
        self.assertEqual(run_calculator('30', '/', '15'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '30/15 = 2',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_30_divided_by_16(self):
        self.assertEqual(run_calculator('30', '/', '16'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '30/16 = 1.875',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_30_divided_by_17(self):
        self.assertEqual(run_calculator('30', '/', '17'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '30/17 = 1.764705882352941176470588235',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_30_divided_by_18(self):
        self.assertEqual(run_calculator('30', '/', '18'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '30/18 = 1.666666666666666666666666667',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_30_divided_by_19(self):
        self.assertEqual(run_calculator('30', '/', '19'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '30/19 = 1.578947368421052631578947368',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_30_divided_by_20(self):
        self.assertEqual(run_calculator('30', '/', '20'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '30/20 = 1.5',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_30_divided_by_21(self):
        self.assertEqual(run_calculator('30', '/', '21'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '30/21 = 1.428571428571428571428571429',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_30_divided_by_22(self):
        self.assertEqual(run_calculator('30', '/', '22'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '30/22 = 1.363636363636363636363636364',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_30_divided_by_23(self):
        self.assertEqual(run_calculator('30', '/', '23'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '30/23 = 1.304347826086956521739130435',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_30_divided_by_24(self):
        self.assertEqual(run_calculator('30', '/', '24'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '30/24 = 1.25',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_30_divided_by_25(self):
        self.assertEqual(run_calculator('30', '/', '25'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '30/25 = 1.2',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_30_divided_by_26(self):
        self.assertEqual(run_calculator('30', '/', '26'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '30/26 = 1.153846153846153846153846154',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_30_divided_by_27(self):
        self.assertEqual(run_calculator('30', '/', '27'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '30/27 = 1.111111111111111111111111111',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_30_divided_by_28(self):
        self.assertEqual(run_calculator('30', '/', '28'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '30/28 = 1.071428571428571428571428571',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_30_divided_by_29(self):
        self.assertEqual(run_calculator('30', '/', '29'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '30/29 = 1.034482758620689655172413793',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_30_divided_by_30(self):
        self.assertEqual(run_calculator('30', '/', '30'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '30/30 = 1',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_30_divided_by_31(self):
        self.assertEqual(run_calculator('30', '/', '31'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '30/31 = 0.9677419354838709677419354839',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_30_divided_by_32(self):
        self.assertEqual(run_calculator('30', '/', '32'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '30/32 = 0.9375',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_30_divided_by_33(self):
        self.assertEqual(run_calculator('30', '/', '33'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '30/33 = 0.9090909090909090909090909091',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_30_divided_by_34(self):
        self.assertEqual(run_calculator('30', '/', '34'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '30/34 = 0.8823529411764705882352941176',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_30_divided_by_35(self):
        self.assertEqual(run_calculator('30', '/', '35'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '30/35 = 0.8571428571428571428571428571',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_30_divided_by_36(self):
        self.assertEqual(run_calculator('30', '/', '36'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '30/36 = 0.8333333333333333333333333333',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_30_divided_by_37(self):
        self.assertEqual(run_calculator('30', '/', '37'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '30/37 = 0.8108108108108108108108108108',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_30_divided_by_38(self):
        self.assertEqual(run_calculator('30', '/', '38'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '30/38 = 0.7894736842105263157894736842',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_30_divided_by_39(self):
        self.assertEqual(run_calculator('30', '/', '39'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '30/39 = 0.7692307692307692307692307692',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_30_divided_by_40(self):
        self.assertEqual(run_calculator('30', '/', '40'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '30/40 = 0.75',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_30_divided_by_41(self):
        self.assertEqual(run_calculator('30', '/', '41'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '30/41 = 0.7317073170731707317073170732',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_30_divided_by_42(self):
        self.assertEqual(run_calculator('30', '/', '42'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '30/42 = 0.7142857142857142857142857143',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_30_divided_by_43(self):
        self.assertEqual(run_calculator('30', '/', '43'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '30/43 = 0.6976744186046511627906976744',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_30_divided_by_44(self):
        self.assertEqual(run_calculator('30', '/', '44'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '30/44 = 0.6818181818181818181818181818',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_30_divided_by_45(self):
        self.assertEqual(run_calculator('30', '/', '45'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '30/45 = 0.6666666666666666666666666667',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_30_divided_by_46(self):
        self.assertEqual(run_calculator('30', '/', '46'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '30/46 = 0.6521739130434782608695652174',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_30_divided_by_47(self):
        self.assertEqual(run_calculator('30', '/', '47'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '30/47 = 0.6382978723404255319148936170',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_30_divided_by_48(self):
        self.assertEqual(run_calculator('30', '/', '48'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '30/48 = 0.625',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_30_divided_by_49(self):
        self.assertEqual(run_calculator('30', '/', '49'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '30/49 = 0.6122448979591836734693877551',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_30_divided_by_50(self):
        self.assertEqual(run_calculator('30', '/', '50'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '30/50 = 0.6',
            'Thanks for using this calculator, goodbye :)',
        ])


if __name__ == '__main__':
    unittest.main()
