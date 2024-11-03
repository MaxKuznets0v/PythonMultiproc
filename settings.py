from configparser import ConfigParser

# Parsing configuration from a file.
config = ConfigParser()
config.read("config.ini")

commands = config["Commands"]
HELLO_CMD = commands["Hello"]
GET_RANDOM_CMD = commands["GetRandom"]
TERMINATE_CMD = commands["Terminate"]

responses = config["Responses"]
HELLO_RESPONSE = responses["Hello"]

gen_config = config["Generator"]
MIN_GEN_VAL = int(gen_config["MinValue"])
MAX_GEN_VAL = int(gen_config["MaxValue"])
NUM_SAMPLES = int(gen_config["NumSamples"])
