"""Utility functions to assist running and testing our solutions."""


def assert_solver(solver, test_inputs):
    for test_input, expected in test_inputs:
        actual = solver(*test_input)
        assert actual == expected, f'solver={solver}, input={test_input}, actual={actual}, expected={expected}'


def assert_solvers(solvers, test_inputs):
    for solver in solvers:
        assert_solver(solver, test_inputs)
