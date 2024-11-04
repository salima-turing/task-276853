import random

def generate_calibration_tests(num_tests=5, sensor_types=["Temperature", "Humidity", "Pressure"],
							   calibration_scenarios={"Normal": 0.5, "Extreme": 1.0}):
	test_id = 1

	for _ in range(num_tests):
		sensor_type = random.choice(sensor_types)
		calibration_scenario = random.choice(list(calibration_scenarios.keys()))

		expected_result = random.uniform(0, 100) if sensor_type != "Pressure" else random.uniform(900, 1100)
		tolerance = calibration_scenarios[calibration_scenario] if sensor_type != "Pressure" else 5

		test_case = {
			"test_id": test_id,
			"action": f"Calibrate {sensor_type} sensor in {calibration_scenario} scenario",
			"input_data": {"sensor_type": sensor_type},
			"expected_result": {"value": expected_result, "tolerance": tolerance},
		}
		yield test_case
		test_id += 1


if __name__ == "__main__":
	for test in generate_calibration_tests(num_tests=15, sensor_types=["Temperature", "Humidity", "Pressure", "CO2"],
										  calibration_scenarios={"Normal": 0.5, "High": 1.0, "Low": 0.1}):
		print(f"Test {test['test_id']}: {test['action']}")
		print(f"Input: {test['input_data']}")
		print(f"Expected Result: {test['expected_result']}")
		print("-" * 30)
