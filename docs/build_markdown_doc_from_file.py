import os

"/home/vagrant/docs/../"

def clear_line(line):
    return line.replace("\t", "").replace("\n", "").replace("\r", "").strip()

def get_object_data(line, begin, end):
    begin_index = line.find(begin) + len(begin)
    end_index = line.find(end, begin_index)
    return line[begin_index:end_index].strip()
    
def get_object_data_to_the_end(line, begin):
    return line[line.find(begin) + len(begin):].strip()

def analyze_file(path):

    lines = open(path, "r").readlines()
    ignore_everything = False
    endpoint_data = ""
    
    for i in range(len(lines)):
        line = clear_line(lines[i])
        
        if "class " in line:
            print ""
            print "# " + get_object_data(line, "class ", "(")
            print ""
            print "*Obtained from file:* [" + path.replace(GLOBAL_IGNORE_PATH_WHEN_PRINTING,"") + "](" + path.replace(GLOBAL_IGNORE_PATH_WHEN_PRINTING, GLOBAL_GITHUB_BAE_PATH) + ")"
            print ""
        
        if "def " in line:
            method_name = get_object_data(line, "def ", "(")
            if method_name.startswith("_"):
                ignore_everything = method_name.startswith("_")
            else:
                ignore_everything = False
                if method_name.startswith("test_"):
                    method_name = get_object_data_to_the_end(method_name, "test_").replace("_", " ")
                
                print ""
                print "> " + endpoint_data + method_name + " method"
                print ""
                endpoint_data = ""
            
        if "\"\"\"" in line and not ignore_everything:
            print get_object_data(line, "\"\"\"", "\"\"\"")
            print ""
            
        if "#" in line and not ignore_everything and not "##" in line:
            data = get_object_data_to_the_end(line, "#")
            if data.startswith("Given"):
                data = "**Given** " + get_object_data_to_the_end(data, "Given")
            elif data.startswith("When"):
                data = "**When** " + get_object_data_to_the_end(data, "When")
            elif data.startswith("Then"):
                data = "**Then** " + get_object_data_to_the_end(data, "Then")
            elif data.startswith("And"):
                data = "**And** " + get_object_data_to_the_end(data, "And")
            
            print "* " + data

        if "@app.route" in line:
            app_route_data = get_object_data(line, "(", ")").split(",")
            method = get_object_data(app_route_data[1], "['", "']")
            endpoint_data = "[**" + method + " " + app_route_data[0].replace("'", "") + "**] "
            
        if "@groups" in line:
            groups_data = get_object_data(line, "(", ")").replace("_GROUP", "")
            endpoint_data = "[**" + groups_data + "**] "
        
def navigate_trough_folders(path):
    items = os.listdir(path)
    for i in items:
        new_path = os.path.join(path, i)
        if os.path.isdir(new_path):
            navigate_trough_folders(new_path)
        elif i.endswith(".py") and not i.startswith("__init__"):
            analyze_file(new_path)

if __name__ == "__main__":
    basedir = os.path.abspath(os.path.dirname(__file__))
    GLOBAL_IGNORE_PATH_WHEN_PRINTING = basedir + "/../"
    GLOBAL_GITHUB_BAE_PATH = "https://github.com/gpaOliveira/SuperDiffer/blob/master/" 
    navigate_trough_folders(basedir + "/../SuperDiffer/")