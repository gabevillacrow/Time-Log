import time
import os
from configparser import ConfigParser

#########################################CLASSES###################################################
class Time_Codes():
    #INITIALIZE CLASS INSTANCE
    def __init__(self,desc,code):
        self.desc = desc
        self.code = code
        self.start_time = 0
        self.end_time = 0
        self.total_time = 0

    #RECORD THE HOUR START TIME 
    def Start_Time(self):
        self.start_time = time.time()/3600

    #RECORD THE HOUR END TIME
    def End_Time(self):
        self.end_time = time.time()/3600
        self.Record_Time()

    #CALCULATE THE TOTAL TIME SPENT
    def Record_Time(self):
        self.total_time = self.total_time + (self.end_time - self.start_time)

###########################################FUNCTIONS##############################################
#PULLS TIME CODES FROM CONFIG FILE
def Get_Time_Codes(config):
    config.read('Config.ini')
    sections = config.sections()
    time_code_section_index = sections.index('Time Codes')
    time_code_dict = {}
    
    for key in config[sections[time_code_section_index]]:
        time_code_dict[key] = config.get('Time Codes',key)

    return time_code_dict        
#CREATES INSTANCES OF TIME CODES
def Create_Time_Code_Instance(io_var_list,time_code_dict):

    
    

#DISPLAY MENU OPTIONS TO USER
def Display_IO_Options(menu_to_io_codes):
    i = 1
    for name in menu_to_io_codes:
        print(str(i) + ". " + menu_to_io_codes[name].desc)
        i += 1
    print("To call it a day, type 'EOD'.")

#PROMPT USER FOR MENU OPTION
def Request_IO_Code(current_active_io_name):

    if current_active_io_name == "":
        selected_time_code = input("Select new IO Code: ")

    if current_active_io_name != "":
        print(f"Current active IO Code: {current_active_io_name}")
        selected_time_code = input("Select new IO Code: ")

    return selected_time_code.upper()

#VALIDATE MENU OPTION SELECTED IS ACTUALLY AN OPTION
def Validate_Code(selected_time_code,current_active_io_name,menu_to_io_codes):
    ioList = [key.upper() for key in menu_to_io_codes]
    if selected_time_code == "EOD":
        return True
    if selected_time_code == current_active_io_name:
        print("Time Code selected is already active")
        return False
    if selected_time_code != current_active_io_name:
        if selected_time_code not in ioList:
            print("Not a valid entry")
            return False
        if selected_time_code in ioList:
            return True

#TAKE THE USER PROVIDED TIMECODE AND CREATE A NEW TIMESTAMP FOR IT.
def Clock_In(current_active_io_num,selected_time_code,menu_to_io_codes):
    if current_active_io_num != "":
        Clock_Out(current_active_io_num,menu_to_io_codes)
        menu_to_io_codes[selected_time_code].Start_Time()
    if current_active_io_num == "":
        menu_to_io_codes[selected_time_code].Start_Time()
    io_name_and_num = (menu_to_io_codes[selected_time_code].desc,selected_time_code)
    return io_name_and_num

#TAKE THE CURRENT ACTIVE TIMECODE AND CREATE AN ENDTIME TIMESTAMP
def Clock_Out(current_active_io_num, menu_to_io_codes):
    menu_to_io_codes[current_active_io_num].End_Time()

#CLOCK OUT OF CURRENT TIMECODE AND SUM ALL TIMES PER TIME CODE
def Closing_Time(menu_to_io_codes):
    ioCodes = list(menu_to_io_codes.values())
    for code in ioCodes:
        print("{}({}): {:1.1f}".format(code.desc,code.code ,code.total_time))

#########################################DECLARE VARIABLES###################################################

#IO CODES
#lunch = Time_Codes("Lunch",0000000)
#it_downtime = Time_Codes("IT Downtime",1101693)
#training_compliance = Time_Codes("Training - Compliance",1101704)
#indirect_other = Time_Codes("Indirect - Other",1101681)
#training_on_the_job = Time_Codes("Training - On the Job",1101705)
#meetings_all_hands = Time_Codes("Meetings - All Hands",1099543)
#meetings_others = Time_Codes("Meetings - Others",1099544)
#cfd_projects = Time_Codes("CFD - Projects",1182541)
#electronics_projects = Time_Codes("Electronics - Projects",1182542)
#firex_projects = Time_Codes("FireX - Projects",1182543)
#overheat_projects = Time_Codes("Overheat - Projects",1182544)
#cfd_support = Time_Codes("CFD - Support",1184286)
#electronics_support = Time_Codes("Electronics - Support",1184287)
#firex_support = Time_Codes("FireX - Support",1184288)
#overheat_support = Time_Codes("Overheat - Support",1184289)

#DICTIONARIES
menu_to_io_codes = {"1":lunch,"2":it_downtime,"3":training_compliance,"4":indirect_other,"5":training_on_the_job,"6":meetings_all_hands,"6":meetings_others,"7":cfd_projects,"8":electronics_projects,"9":firex_projects,"10":overheat_projects,"11":cfd_support,"12":electronics_support,"13":firex_support,"14":overheat_support}

#LIST
io_var_list = [lunch,it_downtime,training_compliance,indirect_other,training_on_the_job,meetings_all_hands,meetings_others,cfd_projects,electronics_projects,firex_projects,overheat_projects,cfd_support,electronics_support,firex_support,overheat_support]
#OTHER VARIABLES
current_active_io_name = ""
current_active_io_num = ""
valid_code = False
eod = False
config = ConfigParser()

#########################################MAIN###################################################


while eod == False:
    time_code_dict = Get_Time_Codes(config)
    while valid_code == False:
        Display_IO_Options(menu_to_io_codes)
        selected_time_code = Request_IO_Code(current_active_io_name)
        print(current_active_io_name)
        os.system('cls')
        valid_code = Validate_Code(selected_time_code,current_active_io_name,menu_to_io_codes)

    valid_code = False
    if selected_time_code != "EOD":
        current_active_io_name,current_active_io_num = Clock_In(current_active_io_num,selected_time_code,menu_to_io_codes)
    if selected_time_code == "EOD":
        if current_active_io_name == "":
            eod = Closing_Time(menu_to_io_codes)
        if current_active_io_name != "":
            Clock_Out(current_active_io_num, menu_to_io_codes)
            eod = Closing_Time(menu_to_io_codes)