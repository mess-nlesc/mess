# mess

This code generates NetLogo codes for a user-defined grid of variables.

For example, if your existing code or model has hard-coded values of `value_1`, `value_2`, `value_3`, this Python code can generate combinations of values and generate a new code using these values.

## Usage

We will use  `jinja` template engine to create a NetLogo code with combination of different parameters which we will refer to as an `experiment`. The Python code (`generate_model.py`) will use jinja to update the variables in the template files and generate a new code. In order to do that we will follow the steps below.

### Step 1: Update the templates

Suppose you want to turn a hard-coded value specified in a file into a variable and generate copies of the NetLogo code with a different values of this variable. For this we will need to update the template file to define the variables that will be replaced by the actual values of the experiments.

For example, suppose you want to update a line of an xml file (`experiments.xml`) below:

```xml
<steppedValueSet variable="Qin_average" first="30" step="10" last="200"/>
```

Corresponding `jinja2` template file (`experiments.xml.jinja`) in the `templates` folder will be:

```jinja
<steppedValueSet variable="Qin_average" first="30" step="{{Qin_average_step}}" last="200"/>
```

In this example we converted the hard-coded value of `10` into a variable called `Qin_average_step` which will be used to generate a new code. The values this variable can take will be defined in the next step.

### Step 2: Define the variables

Now we have a variable called `Qin_average_step` in our example file (`experiments.xml`) and we want to generate different versions of it. In each version we we will replace `Qin_average_step` with a value we want.

The values which the jinja templates will be rendered for can be defined in `variables.json`.

For example:

```json
{
    "Qin_average_step": [20, 30]
}

```

Here, we want our `Qin_average_step` to be replaced by two different values `20` and `30`. As a result, two new files will be generated which contain the lines below.

The first `experiments.xml` will contain:
```xml
<steppedValueSet variable="Qin_average" first="30" step="20" last="200"/>
```

The second `experiments.xml` will contain:
```xml
<steppedValueSet variable="Qin_average" first="30" step="20" last="200"/>
```

In order to generate these files, we will need to follow one more step and run the Python code which will render the templates.

### Step 3: Generate the experiments

Once the variables are defined in the templates and the `variables.json` file, you can generate a new code by running the commands below.

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

The output for the example in this documentation will be:

```shell
parsed variables: {"variables":{"Qin_average_step":[20,30]}}

experiment:0  parameters:{'Qin_average_step': 20, 'config_id': '17b74c98-6ed3-4d01-8d05-d00fa77cfe57', 'experiment_name': 'experiment_0'}
experiment:1  parameters:{'Qin_average_step': 30, 'config_id': 'dbea87fe-d6b1-421c-b622-e3d3e12698ac', 'experiment_name': 'experiment_1'}
```
