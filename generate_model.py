"""Uses the model template to generate a model"""

import json
from itertools import product
import pathlib
import os
from typing import Dict, List
import jinja2
from pydantic import BaseModel, ValidationError


class ModelParameters(BaseModel):
    """_summary_
    """
    variables: Dict[str, List[int]]


# output-related variables
experiment_count = 0
template_folder_name = "templates"  # output folder
output_folder = "experiment"  # output folder


# load templates
parent_dir = os.path.dirname(__file__)
templates_folder = os.path.join(parent_dir, template_folder_name)
environment = jinja2.Environment(
    loader=jinja2.FileSystemLoader(templates_folder)
)

# read the variables for rendering
with open("model_variables.json", mode="r", encoding="utf-8") as variables_entry:
    model_variables = json.load(variables_entry)

# create a pydantic model
model_parameter_list = ModelParameters(variables=model_variables)

# validate the model
try:
    ModelParameters.model_validate(model_parameter_list)
except ValidationError as e:
    print(e)


# print(model_parameter_list.model_json_schema())
print(model_parameter_list.model_dump_json())


def combine_variables(input_dictionary):
    """_summary_
    """
    for dict_product in product(*input_dictionary.values()):
        yield dict(zip(input_dictionary.keys(), dict_product))


for parameter_grid_item in combine_variables(model_parameter_list.variables):
    # show the parameters
    print(f"experiment:{experiment_count}  parameters:{parameter_grid_item}")

    # check if output(experiment) folder exists otherwise, create it
    experiment_path = f"{output_folder}_{experiment_count}"
    if not os.path.exists(experiment_path):
        os.mkdir(experiment_path)

    # save the parameters to a file
    with open(f"{experiment_path}/parameters.json",  mode="w", encoding="utf-8") as parameters_file:
        json.dump(parameter_grid_item, parameters_file)

    # Iterate template directory to render all the template files
    for _file in os.listdir(template_folder_name):
        # check if current file_path is a file
        if os.path.isfile(os.path.join(template_folder_name, _file)):

            save_as_name = pathlib.Path(_file).stem  # file name to save the rendered content
            output_path = f"{experiment_path}/{save_as_name}"  # path for the rendered file
            # print(f"    template file: {_file}")
            # print(f"    output file: {output_path}")

            template = environment.get_template(_file)

            # render the templates
            content = template.render(
                parameter_grid_item
            )

            # save the rendered content
            with open(output_path, mode="w", encoding="utf-8") as model_file:
                model_file.write(content)

    experiment_count += 1
