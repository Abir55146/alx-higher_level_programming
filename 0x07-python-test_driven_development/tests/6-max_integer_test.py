  0.5742929278531704, 0.43940976988732966,
                    0.09537099783126887, 1.4936141049902174,
                    5.764320019082692, 4.322880498170903, 2.004237813008687,
                    0.5565243581024599, 4.302022962278392, 5.680293004785562,
                    2.178866303290743, 1.0390412554953965,
                    0.45132551361896317, 1.4643609109467473,
                    0.6904822043628014, 7.42850599670902, 0.8174242076055683,
                    0.6560986886071569, 0.6513016647379839, 0.7402037152516,
                    1.3480227709351067, 10.667222236398727,
                    1.1255361340134915, 0.3631658619504303,
                    0.8812949657884553, 1.1100323642668828,
                    5.0119643460188845, 2.8953551308720056,
                    2.5574324632368866, 9.169493642307119, 0.4175692708444569,
                    2.344748944605401, 1.1674261590629318, 0.6998588019912835,
                    0.42770576125452897, 1.7136005979522013,
                    8.877571036363525, 0.6825287480571863, 2.6834294650218338,
                    0.7504024417975861, 0.2762206358275793,
                    0.20607476376994402, 0.9497689034126077,
                    2.1498649449691807]), 29.496355326217376)

    def test_numeric_string(self):
        """Unittest for max_integer([..])"""
        self.assertEqual(max_integer("192834754"), "9")

    def test_string(self):
        """Unittest for max_integer([..])"""
        self.assertEqual(max_integer("Holberton"), "t")

    def test_lists(self):
        """Unittest for max_integer([..])"""
        self.assertEqual(max_integer([[], [2], [4], [2, 9]]), [4])

    def test_str_list(self):
        """Unittest for max_integer([..])"""
        self.assertEqual(
            max_integer([["foo"], ["boo"], ["abc"], ["sic"], ["ric"]]),
            ["sic"])

    def test_inf(self):
        """Unittest for max_integer([..])"""
        self.assertEqual(max_integer([99, float('inf'), float('-inf')]),
                         float('inf'))

    def test_nan(self):
        """Unittest for max_integer([..])"""
        self.assertEqual(max_integer([99, float('nan'), 100]), 100)

    def test_mixed_list(self):
        """Unittest for max_integer([..])"""
        with self.assertRaises(TypeError):
            max_integer([[], [2], [4], [2, 9], 99, "foo"])

    def test_mixed_list_int_str(self):
        """Unittest for max_integer([..])"""
        with self.assertRaises(TypeError):
            max_integer([99, "foo"])

    def test_none(self):
        """Unittest for max_integer([..])"""
        with self.assertRaises(TypeError):
            max_integer(None)

    def test_dict(self):
        """Unittest for max_integer([..])"""
        with self.assertRaises(TypeError):
            max_integer([{20: 23, 14: 45}, {"a": "b"}])

    def test_int(self):
        """Unittest for max_integer([..])"""
        with self.assertRaises(TypeError):
            max_integer(98)

    def test_float(self):
        """Unittest for max_integer([..])"""
        with self.assertRaises(TypeError):
            max_integer(9.8)

if __name__ == '__main__':
    unittest.main()
