# mess

This code generates NetLogo codes for a user-defined grid of variables.

For example, if your existing code or model has hard-coded values of `value_1`, `value_2`, `value_3`, this Python code can generate combinations of values and generate a new code using these values.

## Usage

To use this code in your own project:

1. Place all the model files into the folder called `templates` and add an extention `.jinja` to each file
1. Replace hard-coded values of a template file with a `{{ variable }}`
1. Add the added variables and their desired values to `variables.json` file and place this file in the root folder of your project
1. Run the generator code

    Create a new virtual environment:

    ```shell
    python -m venv venv
    source ./venv/bin/activate
    ```

    Install the required dependencies:

    ```shell
    python -m pip install -r requirements.txt
    ```

    Generate the codes from the templates:

    ```shell
    python generate_model.py
    ```

New rendered models will be in folder `experiments_n`, where `n` is the number of experiments equal to the number of variable combinations.

**Note:** If you run `generate_model.py` again, `experiments_n` folders and the content will be overwritten

## Tutorial

If you want to know more about how the code works and the templates are used to create new models you can read [TUTORIAL.md](TUTORIAL.md).
