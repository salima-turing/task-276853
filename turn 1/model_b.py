import random


def generate_calibration_actions(num_actions=5):
    """
    Generate a set of calibration actions for an IoT device.

    Yields:
        dict: A dictionary containing calibration action details.
    """
    sensors = ["temperature", "humidity", "pressure"]

    for _ in range(num_actions):
        sensor_name = random.choice(sensors)
        calibration_value = random.uniform(0, 100)
        expected_result = calibration_value + random.uniform(-5, 5)

        yield {
            "sensor_name": sensor_name,
            "calibration_value": calibration_value,
            "expected_result": expected_result,
        }


def simulate_calibration(action):
    """
    Simulate the calibration action on an IoT device and return the result.

    Args:
        action (dict): A dictionary containing calibration action details.

    Returns:
        float: The simulated calibration result.
    """
    sensor_name = action["sensor_name"]
    calibration_value = action["calibration_value"]
    print(f"Simulating calibration of {sensor_name} with value: {calibration_value}")

    return calibration_value + random.uniform(-2, 2)


import unittest


class TestIoTDeviceCalibration(unittest.TestCase):
    def test_calibration_accuracy(self):
        for action in generate_calibration_actions():
            result = simulate_calibration(action)
            expected_result = action["expected_result"]
            tolerance = 1.5

            self.assertAlmostEqual(
                result, expected_result, delta=tolerance,
                msg=f"Calibration failed for {action['sensor_name']}: Expected {expected_result}, Got {result}"
            )a


if __name__ == "__main__":
    unittest.main()
