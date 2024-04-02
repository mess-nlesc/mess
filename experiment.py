"""
Create a job script from netlogo experiment
"""

import json

from kunefe import Kunefe

kunefe = Kunefe(username="olyashevska", hostname="snellius.surf.nl", port=22)

# define the constants
OUTPUT_FOLDER_LOCAL = "./output/"  # local folder to save output
REMOTE_HOME = "/home/olyashevska/"  # home folder on the remote system
OUTPUT_FOLDER_REMOTE = REMOTE_HOME + "test_folder/"

# specify the Docker image
NETLOGO_VERSION = "6.3.0"
DOCKER_IMAGE = f"comses/netlogo:{NETLOGO_VERSION}"

# specify the apptainer image
SIF_FILE_NAME = "netlogo_6.3.0.sif"
SIF_FILE_PATH_LOCAL = OUTPUT_FOLDER_LOCAL + SIF_FILE_NAME
SIF_FILE_PATH_REMOTE = OUTPUT_FOLDER_REMOTE + SIF_FILE_NAME

try:
    os.mkdir(OUTPUT_FOLDER_LOCAL)
    print(f"Directory '{OUTPUT_FOLDER_LOCAL}' created.")
except FileExistsError:
    print(f"Directory '{OUTPUT_FOLDER_LOCAL}' already exists.")

# build apptainer image from a Docker image
# kunefe.build_apptainer_image(
#     docker_image=DOCKER_IMAGE, sif_file_name=SIF_FILE_PATH_LOCAL
# )

# make a connection to the remote
# kunefe.connect_remote()

# create a folder which the files will be copied to
# kunefe.create_remote_folder(remote_folder=OUTPUT_FOLDER_REMOTE)

# define the job name and the command to be used to run NetLogo
JOB_NAME = "kunefe_netlogo_experiment_job"
NETLOGO_COMMAND = """/opt/netlogo/netlogo-headless.sh \
--model 'model/main.nlogo' \
--setup-file 'model/experiments.xml' \
--table 'output/output'
"""

# load context data for the template
with open("experiments.json", "r") as f:
    experiments = json.load(f)

for experiment in experiments:
    job_name = f"kunefe_netlogo_experiment_job_{experiment['experiment_name']}"

    # generate a job script to be submitted to HPC
    kunefe.generate_job_script(
        job_name=job_name,
        sif_file_path=SIF_FILE_PATH_REMOTE,
        command=NETLOGO_COMMAND,
        env_vars="JAVA_TOOL_OPTIONS=-Xmx8G",
        job_file_path=OUTPUT_FOLDER_LOCAL,
        job_time="0:1:00",
        template_name="exp",
    )
