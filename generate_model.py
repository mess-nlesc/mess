"""Uses the model template to generate a model"""

import os
import jinja2

# load templates
parent_dir = os.path.dirname(__file__)
templates_folder = os.path.join(parent_dir, "template")
environment = jinja2.Environment(
    loader=jinja2.FileSystemLoader(templates_folder)
)

# define variables
# output-related variables
experiment_name = "experiments_1"  # output folder
output_filename = f"{experiment_name}/experiments.xml"

# model variables
Qin_average_first = 111  # default: 40
Qin_average_step = 222  # default: 10
Qin_average_last = 333  # default: 200

ComparisonTime_first = 444  # default: 730
ComparisonTime_step = 555  # default: 365
ComparisonTime_last = 666  # default: 1825

# render the templates
template = environment.get_template("experiments.xml.jinja")
content = template.render(
    experiment_name=experiment_name,
    Qin_average_first=Qin_average_first,
    Qin_average_step=Qin_average_step,
    Qin_average_last=Qin_average_last,
    ComparisonTime_first=ComparisonTime_first,
    ComparisonTime_step=ComparisonTime_step,
    ComparisonTime_last=ComparisonTime_last,
)

# check if output folder exists otherwise, create it
if not os.path.exists(experiment_name):
    os.mkdir(experiment_name)

# save the rendered files
with open(output_filename, mode="w", encoding="utf-8") as model_file:
    model_file.write(content)
