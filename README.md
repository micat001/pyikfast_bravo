# Python Bindings for `ikfast`

Generate a Python `ikfast` library from the given URDF file.
This project provides all necessary utilities to generate `ikpy` C++ files and Python bindings for it.

## Getting Started

Export URDF from xacro (inside bravo_description package):

`rosrun xacro xacro -o bravo_arm_only.urdf bravo_arm_only.xacro`

Move to the directory with `robot.urdf` and execute:
```bash
docker run -v ${PWD}:/output cyberbotics/pyikfast [base_link] [effector] [module_extension]
```
Replace `[base_link]` and `[effector]` with the link-names from the `robot.urdf`.

The `[module_extension]` will append to the generated Python module name.
The module name will be `pyikfast` + `[module_extension]`.
For example, `_irb4600` will generate the Python module named `pyikfast_irb4600`.

For Bravo:
```bash
docker run -v ${PWD}:/output cyberbotics/pyikfast bravo_base_link ee_link _bravo
```

After a few minutes your Python library should be ready ready!
Install it as:
```bash
pip3 install .
```

Use the library:
```python
import pyikfast


target_translation = [0.5, 0.5, 0.5]
target_rotation = [1, 0, 0, 0, 1, 0, 0, 0, 1]

# Calculate inverse kinematics
positions = pyikfast.inverse(target_translation, target_rotation)
print(positions)

# Calculate forward kinematics (we use the third IK solution)
translation, rotation = pyikfast.forward(positions[2])
print(translation, rotation)
```

## Distribution
To distribute the generated Python library you can make [a Python `*.whl` file](https://packaging.python.org/tutorials/packaging-projects/#generating-distribution-archives):
```bash
pip3 install setuptools wheel
python3 setup.py bdist_wheel
```
and your `*.whl` will be located in `./dist/pyikfast-*.whl`, so a user can install it as:
```bash
pip3 install pyikfast-*.whl
```

## Development
If you are interested into the library development here are a few notes:

```bash
# Building using Docker
docker build . --tag pyikfast
docker run -it -v ${PWD}/output:/output --entrypoint bash pyikfast
/entrypoint.bash base_link solid_12208 _ext

# Compile standalone
g++ $(find -name '*.cpp') -o ikfast
./ikfast 1 0 0 0.5 0 1 0 0.5 0 0 1 0.5

# Python
python3 -c "import pyikfast; print(pyikfast.inverse([0.5, 0.5, 0.5], [1, 0, 0, 0, 1, 0, 0, 0, 1]))"
python3 -c "import pyikfast; print(pyikfast.forward([0.927295218001612, -2.899331265288886, 2.048719302774242, -1.057447868999410, 1.163951188044116, 0.612010251709654]))"
```
