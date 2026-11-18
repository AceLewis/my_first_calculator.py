# test_divided_by_16.py
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


class TestDividedBy16(unittest.TestCase):

    def test_16_divided_by_0(self):
        self.assertEqual(run_calculator('16', '/', '0'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '16/0 = Inf',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_16_divided_by_1(self):
        self.assertEqual(run_calculator('16', '/', '1'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '16/1 = 16',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_16_divided_by_2(self):
        self.assertEqual(run_calculator('16', '/', '2'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '16/2 = 8',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_16_divided_by_3(self):
        self.assertEqual(run_calculator('16', '/', '3'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '16/3 = 5.333333333333333333333333333',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_16_divided_by_4(self):
        self.assertEqual(run_calculator('16', '/', '4'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '16/4 = 4',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_16_divided_by_5(self):
        self.assertEqual(run_calculator('16', '/', '5'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '16/5 = 3.2',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_16_divided_by_6(self):
        self.assertEqual(run_calculator('16', '/', '6'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '16/6 = 2.666666666666666666666666667',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_16_divided_by_7(self):
        self.assertEqual(run_calculator('16', '/', '7'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '16/7 = 2.285714285714285714285714286',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_16_divided_by_8(self):
        self.assertEqual(run_calculator('16', '/', '8'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '16/8 = 2',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_16_divided_by_9(self):
        self.assertEqual(run_calculator('16', '/', '9'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '16/9 = 1.777777777777777777777777778',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_16_divided_by_10(self):
        self.assertEqual(run_calculator('16', '/', '10'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '16/10 = 1.6',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_16_divided_by_11(self):
        self.assertEqual(run_calculator('16', '/', '11'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '16/11 = 1.454545454545454545454545455',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_16_divided_by_12(self):
        self.assertEqual(run_calculator('16', '/', '12'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '16/12 = 1.333333333333333333333333333',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_16_divided_by_13(self):
        self.assertEqual(run_calculator('16', '/', '13'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '16/13 = 1.230769230769230769230769231',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_16_divided_by_14(self):
        self.assertEqual(run_calculator('16', '/', '14'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '16/14 = 1.142857142857142857142857143',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_16_divided_by_15(self):
        self.assertEqual(run_calculator('16', '/', '15'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '16/15 = 1.066666666666666666666666667',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_16_divided_by_16(self):
        self.assertEqual(run_calculator('16', '/', '16'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '16/16 = 1',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_16_divided_by_17(self):
        self.assertEqual(run_calculator('16', '/', '17'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '16/17 = 0.9411764705882352941176470588',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_16_divided_by_18(self):
        self.assertEqual(run_calculator('16', '/', '18'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '16/18 = 0.8888888888888888888888888889',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_16_divided_by_19(self):
        self.assertEqual(run_calculator('16', '/', '19'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '16/19 = 0.8421052631578947368421052632',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_16_divided_by_20(self):
        self.assertEqual(run_calculator('16', '/', '20'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '16/20 = 0.8',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_16_divided_by_21(self):
        self.assertEqual(run_calculator('16', '/', '21'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '16/21 = 0.7619047619047619047619047619',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_16_divided_by_22(self):
        self.assertEqual(run_calculator('16', '/', '22'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '16/22 = 0.7272727272727272727272727273',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_16_divided_by_23(self):
        self.assertEqual(run_calculator('16', '/', '23'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '16/23 = 0.6956521739130434782608695652',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_16_divided_by_24(self):
        self.assertEqual(run_calculator('16', '/', '24'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '16/24 = 0.6666666666666666666666666667',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_16_divided_by_25(self):
        self.assertEqual(run_calculator('16', '/', '25'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '16/25 = 0.64',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_16_divided_by_26(self):
        self.assertEqual(run_calculator('16', '/', '26'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '16/26 = 0.6153846153846153846153846154',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_16_divided_by_27(self):
        self.assertEqual(run_calculator('16', '/', '27'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '16/27 = 0.5925925925925925925925925926',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_16_divided_by_28(self):
        self.assertEqual(run_calculator('16', '/', '28'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '16/28 = 0.5714285714285714285714285714',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_16_divided_by_29(self):
        self.assertEqual(run_calculator('16', '/', '29'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '16/29 = 0.5517241379310344827586206897',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_16_divided_by_30(self):
        self.assertEqual(run_calculator('16', '/', '30'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '16/30 = 0.5333333333333333333333333333',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_16_divided_by_31(self):
        self.assertEqual(run_calculator('16', '/', '31'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '16/31 = 0.5161290322580645161290322581',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_16_divided_by_32(self):
        self.assertEqual(run_calculator('16', '/', '32'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '16/32 = 0.5',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_16_divided_by_33(self):
        self.assertEqual(run_calculator('16', '/', '33'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '16/33 = 0.4848484848484848484848484848',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_16_divided_by_34(self):
        self.assertEqual(run_calculator('16', '/', '34'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '16/34 = 0.4705882352941176470588235294',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_16_divided_by_35(self):
        self.assertEqual(run_calculator('16', '/', '35'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '16/35 = 0.4571428571428571428571428571',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_16_divided_by_36(self):
        self.assertEqual(run_calculator('16', '/', '36'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '16/36 = 0.4444444444444444444444444444',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_16_divided_by_37(self):
        self.assertEqual(run_calculator('16', '/', '37'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '16/37 = 0.4324324324324324324324324324',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_16_divided_by_38(self):
        self.assertEqual(run_calculator('16', '/', '38'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '16/38 = 0.4210526315789473684210526316',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_16_divided_by_39(self):
        self.assertEqual(run_calculator('16', '/', '39'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '16/39 = 0.4102564102564102564102564103',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_16_divided_by_40(self):
        self.assertEqual(run_calculator('16', '/', '40'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '16/40 = 0.4',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_16_divided_by_41(self):
        self.assertEqual(run_calculator('16', '/', '41'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '16/41 = 0.3902439024390243902439024390',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_16_divided_by_42(self):
        self.assertEqual(run_calculator('16', '/', '42'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '16/42 = 0.3809523809523809523809523810',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_16_divided_by_43(self):
        self.assertEqual(run_calculator('16', '/', '43'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '16/43 = 0.3720930232558139534883720930',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_16_divided_by_44(self):
        self.assertEqual(run_calculator('16', '/', '44'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '16/44 = 0.3636363636363636363636363636',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_16_divided_by_45(self):
        self.assertEqual(run_calculator('16', '/', '45'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '16/45 = 0.3555555555555555555555555556',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_16_divided_by_46(self):
        self.assertEqual(run_calculator('16', '/', '46'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '16/46 = 0.3478260869565217391304347826',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_16_divided_by_47(self):
        self.assertEqual(run_calculator('16', '/', '47'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '16/47 = 0.3404255319148936170212765957',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_16_divided_by_48(self):
        self.assertEqual(run_calculator('16', '/', '48'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '16/48 = 0.3333333333333333333333333333',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_16_divided_by_49(self):
        self.assertEqual(run_calculator('16', '/', '49'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '16/49 = 0.3265306122448979591836734694',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_16_divided_by_50(self):
        self.assertEqual(run_calculator('16', '/', '50'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '16/50 = 0.32',
            'Thanks for using this calculator, goodbye :)',
        ])


if __name__ == '__main__':
    unittest.main()
