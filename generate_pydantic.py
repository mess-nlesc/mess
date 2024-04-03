"""Uses the model template to generate a model"""

import json
from itertools import product
import pathlib
import os
from typing import Dict, List
import jinja2
from pydantic import BaseModel, ValidationError


class ModelParameter(BaseModel):
    """_summary_
    """
    files: List[str]
    variables: Dict[str, List[int]]


class ParameterList(BaseModel):
    """_summary_
    """
    items: List[ModelParameter]


# load templates
parent_dir = os.path.dirname(__file__)
templates_folder = os.path.join(parent_dir, "template")
environment = jinja2.Environment(
    loader=jinja2.FileSystemLoader(templates_folder)
)


# output-related variables
experiment_count = 0
experiment_name = "experiment"  # output folder


# read the variables for rendering
with open("model_variables.json", mode="r", encoding="utf-8") as variables_entry:
    model_variables = json.load(variables_entry)


model_parameter_list = ParameterList(items=model_variables)

# validate the model
try:
    ParameterList.model_validate(model_parameter_list)
except ValidationError as e:
    print(e)


# print(model_parameter_list.model_json_schema())
# print(model_parameter_list.model_dump_json())
# print(model_parameter_list)
# print(type(model_parameter_list.items[0]))
# print(model_parameter_list.items[0])
# print(model_parameter_list.items[0].variables)


# for _entry in model_parameter_list.items:
#     print(_entry.file)

#     for _variable, _value in _entry.variables.items():
#         print(f"    {_variable}  ->  {_value} ({type(_value).__name__})")
#         if isinstance(_value, list):
#             for _num in _value:
#                 print(f"        {_num}")


def combine_variables(input_dictionary):
    """_summary_
    """
    for dict_product in product(*input_dictionary.values()):
        yield dict(zip(input_dictionary.keys(), dict_product))


for _entry in model_parameter_list.items:

    for parameter_grid_item in combine_variables(_entry.variables):

        # check if output(experiment) folder exists otherwise, create it
        experiment_path = f"{experiment_name}_{experiment_count}"
        if not os.path.exists(experiment_path):
            os.mkdir(experiment_path)

        # show the parameters
        print(f"parameters: {parameter_grid_item}")

        # save the parameters to a file
        with open(f"{experiment_path}/parameters.json",  mode="w", encoding="utf-8") as parameters_file:
            json.dump(parameter_grid_item, parameters_file)

        for _file in _entry.files:

            save_as_name = pathlib.Path(_file).stem  # file name to save the rendered content
            output_path = f"{experiment_path}/{save_as_name}"  # path for the rendered file
            print(f"    template file: {_file}")
            print(f"    output file: {output_path}")

            template = environment.get_template(_file)

            # render the templates
            content = template.render(
                parameter_grid_item
            )

            # save the rendered content
            with open(output_path, mode="w", encoding="utf-8") as model_file:
                model_file.write(content)

        experiment_count += 1
