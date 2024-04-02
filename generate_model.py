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
output_folder= "./output"
output_filename = f"{output_folder}/experiments.xml"

# model variables
Qin_average_first = 333
Qin_average_step = 666
Qin_average_last = 999

# render the templates
template = environment.get_template("experiments.xml.jinja")
content = template.render(
    experiment_name="hello_experiment",
    Qin_average_first=Qin_average_first,
    Qin_average_step=Qin_average_step,
    Qin_average_last=Qin_average_last
)

# check if output folder exists otherwise, create it
if not os.path.exists(output_folder):
    os.mkdir(output_folder)

# save the rendered files
with open(output_filename, mode="w", encoding="utf-8") as model_file:
    model_file.write(content)
