# test_times_22.py
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


class TestTimes22(unittest.TestCase):

    def test_22_times_0(self):
        self.assertEqual(run_calculator('22', '*', '0'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '22*0 = 0',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_22_times_1(self):
        self.assertEqual(run_calculator('22', '*', '1'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '22*1 = 22',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_22_times_2(self):
        self.assertEqual(run_calculator('22', '*', '2'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '22*2 = 44',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_22_times_3(self):
        self.assertEqual(run_calculator('22', '*', '3'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '22*3 = 66',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_22_times_4(self):
        self.assertEqual(run_calculator('22', '*', '4'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '22*4 = 88',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_22_times_5(self):
        self.assertEqual(run_calculator('22', '*', '5'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '22*5 = 110',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_22_times_6(self):
        self.assertEqual(run_calculator('22', '*', '6'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '22*6 = 132',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_22_times_7(self):
        self.assertEqual(run_calculator('22', '*', '7'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '22*7 = 154',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_22_times_8(self):
        self.assertEqual(run_calculator('22', '*', '8'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '22*8 = 176',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_22_times_9(self):
        self.assertEqual(run_calculator('22', '*', '9'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '22*9 = 198',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_22_times_10(self):
        self.assertEqual(run_calculator('22', '*', '10'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '22*10 = 220',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_22_times_11(self):
        self.assertEqual(run_calculator('22', '*', '11'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '22*11 = 242',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_22_times_12(self):
        self.assertEqual(run_calculator('22', '*', '12'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '22*12 = 264',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_22_times_13(self):
        self.assertEqual(run_calculator('22', '*', '13'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '22*13 = 286',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_22_times_14(self):
        self.assertEqual(run_calculator('22', '*', '14'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '22*14 = 308',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_22_times_15(self):
        self.assertEqual(run_calculator('22', '*', '15'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '22*15 = 330',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_22_times_16(self):
        self.assertEqual(run_calculator('22', '*', '16'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '22*16 = 352',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_22_times_17(self):
        self.assertEqual(run_calculator('22', '*', '17'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '22*17 = 374',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_22_times_18(self):
        self.assertEqual(run_calculator('22', '*', '18'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '22*18 = 396',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_22_times_19(self):
        self.assertEqual(run_calculator('22', '*', '19'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '22*19 = 418',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_22_times_20(self):
        self.assertEqual(run_calculator('22', '*', '20'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '22*20 = 440',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_22_times_21(self):
        self.assertEqual(run_calculator('22', '*', '21'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '22*21 = 462',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_22_times_22(self):
        self.assertEqual(run_calculator('22', '*', '22'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '22*22 = 484',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_22_times_23(self):
        self.assertEqual(run_calculator('22', '*', '23'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '22*23 = 506',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_22_times_24(self):
        self.assertEqual(run_calculator('22', '*', '24'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '22*24 = 528',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_22_times_25(self):
        self.assertEqual(run_calculator('22', '*', '25'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '22*25 = 550',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_22_times_26(self):
        self.assertEqual(run_calculator('22', '*', '26'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '22*26 = 572',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_22_times_27(self):
        self.assertEqual(run_calculator('22', '*', '27'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '22*27 = 594',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_22_times_28(self):
        self.assertEqual(run_calculator('22', '*', '28'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '22*28 = 616',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_22_times_29(self):
        self.assertEqual(run_calculator('22', '*', '29'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '22*29 = 638',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_22_times_30(self):
        self.assertEqual(run_calculator('22', '*', '30'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '22*30 = 660',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_22_times_31(self):
        self.assertEqual(run_calculator('22', '*', '31'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '22*31 = 682',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_22_times_32(self):
        self.assertEqual(run_calculator('22', '*', '32'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '22*32 = 704',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_22_times_33(self):
        self.assertEqual(run_calculator('22', '*', '33'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '22*33 = 726',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_22_times_34(self):
        self.assertEqual(run_calculator('22', '*', '34'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '22*34 = 748',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_22_times_35(self):
        self.assertEqual(run_calculator('22', '*', '35'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '22*35 = 770',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_22_times_36(self):
        self.assertEqual(run_calculator('22', '*', '36'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '22*36 = 792',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_22_times_37(self):
        self.assertEqual(run_calculator('22', '*', '37'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '22*37 = 814',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_22_times_38(self):
        self.assertEqual(run_calculator('22', '*', '38'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '22*38 = 836',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_22_times_39(self):
        self.assertEqual(run_calculator('22', '*', '39'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '22*39 = 858',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_22_times_40(self):
        self.assertEqual(run_calculator('22', '*', '40'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '22*40 = 880',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_22_times_41(self):
        self.assertEqual(run_calculator('22', '*', '41'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '22*41 = 902',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_22_times_42(self):
        self.assertEqual(run_calculator('22', '*', '42'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '22*42 = 924',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_22_times_43(self):
        self.assertEqual(run_calculator('22', '*', '43'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '22*43 = 946',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_22_times_44(self):
        self.assertEqual(run_calculator('22', '*', '44'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '22*44 = 968',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_22_times_45(self):
        self.assertEqual(run_calculator('22', '*', '45'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '22*45 = 990',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_22_times_46(self):
        self.assertEqual(run_calculator('22', '*', '46'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '22*46 = 1012',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_22_times_47(self):
        self.assertEqual(run_calculator('22', '*', '47'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '22*47 = 1034',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_22_times_48(self):
        self.assertEqual(run_calculator('22', '*', '48'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '22*48 = 1056',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_22_times_49(self):
        self.assertEqual(run_calculator('22', '*', '49'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '22*49 = 1078',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_22_times_50(self):
        self.assertEqual(run_calculator('22', '*', '50'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '22*50 = 1100',
            'Thanks for using this calculator, goodbye :)',
        ])


if __name__ == '__main__':
    unittest.main()
