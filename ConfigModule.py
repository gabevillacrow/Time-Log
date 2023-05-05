from configparser import ConfigParser

#FUNCTION TO WRITE CONFIG FILE
def Write_Config(config):

    with open('Config.ini','w') as configfile:
        config.write(configfile)

config = ConfigParser()
config["Time Codes"] = {
    "Lunch":0000000,
    "IT Downtime":1101693,
    "Training - Compliance":1101704,
    "Indirect - Other":1101681,
    "Training - On the Job":1101705,
    "Meetings - All Hands":1099543,
    "Meetings - Others":1099544,
    "CFD - Projects":1182541,
    "Electronics - Projects":1182542,
    "FireX - Projects":1182543,
    "FireX - Projects":1182543,
    "Overheat - Projects":1182544,
    "CFD - Support":1184286,
    "Electronics - Support":1184287,
    "FireX - Support":1184288,
    "Overheat - Support":1184289}

Write_Config(config)
