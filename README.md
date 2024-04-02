## mess
Run NetLogo code on HPC using kunefe

## Installation

```bash
python -m venv venv
source venv/bin/activate
python -m pip install kunefe
```
## Usage
We will use  `jinja2` template engine to create the experiments. 
Suppose your experiments are specified in `experiments.xml` file. To prepare the experiments for running on HPC, you need to create a template file with extension `.jinja` in which you define the variables that will be replaced by the actual values of the experiments (`.json`). 

For example, if your `experiments.xml` is:

```xml
<experiment name="Experiment_1" repetitions="1" runMetricsEveryStep="true">
```

Corresponding `jinja2` template file will be:

```jinja2
<experiment name="{{ experiment_name }}" repetitions="1" runMetricsEveryStep="true">
```

With the data file:

```json
{
    "experiment_name": "Experiment_1"
}
```
If we have `steppedValueSet` and `enumeratedValueSet` variable in the `experiments.xml`  the corresponding template and data file will be as follows:

```xml
<steppedValueSet variable="Qin_average" first="40" step="10" last="200" /> 
<enumeratedValueSet variable="Qin_randomizer"> <value value="0" />
```

```jinja2
{% for variable, first, step, last in stepped_values %}
<steppedValueSet variable="{{ Qin_average }}" first="{{ first }}" step="{{ step }}" last="{{ last }}" />
{% endfor %}
<enumeratedValueSet variable="{{ Qin_randomizer }}">
<value value="{{ value }}" />
```

```json
"stepped_values": 
[{
  "variable": "Qin_average",
  "first": 40,
  "step": 10,
  "last": 200
  }
],
"Qin_randomizer":[0,1,2]
```




