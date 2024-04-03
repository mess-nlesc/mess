"""Uses the model template to generate a model"""

import json
import pathlib
import os
from uuid import uuid4
import jinja2
from pydantic import ValidationError
from model import ParametersModel
from helpers import combine_variables

# output-related variables
experiment_count = 0  # current number of combinations
template_folder_name = "templates"  # output folder
output_folder_base = "experiment"  # output folder

# load the templates
parent_dir = os.path.dirname(__file__)
templates_folder = os.path.join(parent_dir, template_folder_name)
environment = jinja2.Environment(
    loader=jinja2.FileSystemLoader(templates_folder)
)

# read the variables for rendering
with open("model_variables.json", mode="r", encoding="utf-8") as variables_input:
    model_variables = json.load(variables_input)

# create a pydantic model
model_parameter_list = ParametersModel(variables=model_variables)

# validate the model
try:
    ParametersModel.model_validate(model_parameter_list)
except ValidationError as e:
    print(e)

# print(model_parameter_list.model_json_schema())  # show the schema
print(f"parsed variables: {model_parameter_list.model_dump_json()}\n")  # show the parsed values

# loop over the variable combinations and render all the files
for parameter_grid_item in combine_variables(model_parameter_list.variables):
    # define experiment name
    experiment_name = f"{output_folder_base}_{experiment_count}"

    # for each parameter combination create a new id
    parameter_grid_item['config_id'] = str(uuid4())

    # add a specific variable for the NetLogo code
    parameter_grid_item['experiment_name'] = experiment_name

    # show the parameter combination
    print(f"experiment:{experiment_count}  parameters:{parameter_grid_item}")

    # check if output(experiment) folder exists otherwise, create it
    if not os.path.exists(experiment_name):
        os.mkdir(experiment_name)

    # save the parameters to a file
    with open(f"{experiment_name}/parameters.json",  mode="w", encoding="utf-8") as parameters_file:
        json.dump(parameter_grid_item, parameters_file)

    # Iterate template directory to render all the template files
    for _file in os.listdir(template_folder_name):
        # check if current file_path is a file
        if os.path.isfile(os.path.join(template_folder_name, _file)):
            # define the path for output file
            save_as_name = pathlib.Path(_file).stem  # file name to save the rendered content
            output_path = f"{experiment_name}/{save_as_name}"  # path for the rendered file

            # get the template file to be rendered
            template = environment.get_template(_file)

            # render the template using the parameter combination
            content = template.render(
                parameter_grid_item
            )

            # save the rendered content
            with open(output_path, mode="w", encoding="utf-8") as model_file:
                model_file.write(content)

    experiment_count += 1
