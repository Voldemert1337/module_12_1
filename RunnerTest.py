import runner as rn
import unittest


class TestRunner(unittest.TestCase):
    def test_run(self):
        runner_1 = rn.Runner("Маша")
        for run_ in range(10):
            runner_1.run()
        self.assertEqual(runner_1.distance, 100)

    def test_walk(self):
        runner_2 = rn.Runner("Лена")
        for walk_ in range(10):
            runner_2.walk()
        self.assertEqual(runner_2.distance, 50)

    def test_challenge(self):
        runner_one = rn.Runner('Максим')
        runner_two = rn.Runner('Дима')
        for i in range(10):
            runner_one.run()
            runner_two.walk()
        self.assertNotEqual(runner_one.distance, runner_two.distance)


if __name__ == '__main__':
    unittest.main()