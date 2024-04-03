# mess

Generate a NetLogo code from a template

## Usage

We will use  `jinja2` template engine to create a NetLogo code with combination of different parameters which we will refer to as an `experiment`. The Python code (`generate_model.py`) will use jinja to update the variables, in the template files and generate a code. In order to do that we will follow the steps below.

### Step 1: Update the templates

Suppose you want to turn a hard-coded value specified in `experiments.xml` file into a variable and generate copies of the NetLogo code with a different values of this variable. To prepare the experiments for running on HPC, you need to create a template file with extension `.jinja` in which you define the variables that will be replaced by the actual values of the experiments (`.json`).

For example, if your `experiments.xml` is:

```xml
<steppedValueSet variable="Qin_average" first="30" step="10" last="200"/>
```

Corresponding `jinja2` template file (`experiments.xml.jinja`) in the `templates` folder will be:

```jinja
<steppedValueSet variable="Qin_average" first="30" step="{{Qin_average_step}}" last="200"/>
```

In this example we converted the hard-coded value of 10 into a variable which will be used to generate a new code.

### Step 2: Define the variables

Define the variables in `model_variables.json`.

```json
{
    "Qin_average_step": [10, 20]
}

```

### Step 3: Generate the experiments

Once the variables are defined in the templates and the `model_variables.json` file, you can generate a new code by running the commands below.

```bash
python -m venv venv
source venv/bin/activate
python generate_model.py
```


