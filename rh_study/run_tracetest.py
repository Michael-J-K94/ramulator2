import os, yaml, copy, itertools
from calc_rh_parameters import get_rh_parameters

base_config_file = "rh_dramtrace_baseline.yaml"
base_config = None
with open(base_config_file, 'r') as stream:
    try:
        base_config = yaml.safe_load(stream)
    except yaml.YamlError as exc:
        print(exc)
if(base_config == None):
    print("Error: base config is None")
    exit(1)


config = copy.deepcopy(base_config)
cmd = "./../ramulator2 -c '" + str(config) + "' > " + "dram_trace.out" + " 2>&1"
os.system(cmd)


