import pandas as pd
from collections import defaultdict
import pprint

if __name__ == "__main__":
    df = pd.read_excel("../data/202110_1st_audit_C_A_Results.xlsx")
    # Learning Experience Team
    lx_iloc = {
        4: "Home Page tab not present or doesn't provide intro to course",
        6: "Modality mentioned and language is incorrect",
        7: "Instructor Information missing",
        13: "Required Writing, Class Participation, and UC policies don't match\
             minimum verbiage", 
        16: "(ICT ONLY) Course reserves noted incorrectly in syllabus and course\
             home module",
        17: "(ICT ONLY) Alma Leganto Course Reserves language is not present",
        18: "Unmatched 'Grading Criteria and Evaluation' section",
        19: "Unmatched 'What is expected of me?' section",
        20: "Unmatched 'Canvas Learning Management System' section",
        21: "Unmatched 'DU Writing Center' section",
        22: "Unmatched 'DU Policies and Procedures' section",
        28: "No Course Home module under Modules tab",
        29: "No Introductions or Welcome activity",
        33: "Course files not organized into module/weekly folders" 
    }
    

    # Academic Directors
    ac_dir_iloc = {
        8: "Course description not consistent",
        9: "Not all required texts in Turabian format",
        10: "ISBNs missing", 
        11: "Not all required readings match the HQ",
        12: "Course Description, required readings, weekly topics incomplete",
        23: "Student-Faculty communication policy not clear",
        24: "Module/weekly topics not outlined",
        25: "Class participation expectations not clear",
        26: "Published assignments in the Syllabus Overview match a 1,000 point scale",
        27: "Late work policy is unclear",
        30: "Modules/weeks not organized into 10 weekly modules",
        31: "Modules and included items have inconsistent naming or don't \
            include module/week",
        32: "Modules have different names than topics listed in syllabus module outline",
        34: "Not all pages are associated with a module/week",
        35: "Published Assignments do not match Syllabus overview and/or do not \
            match a 1,000 point scale",
        36: "Not all assignments organized by type",
        37: "Not all assignments categorized under a corresponding module/week",
        38: "Not all assignments have a unique name and/or include week they are due in",
        39: "Required discussions missing due date and/or points for grading",
        40: "Not all discussions are threaded with a due date",
        46: "outcomes are not measurable or being with Blooms verbs",
        47: "OUtcomes are not the corresponding level",
        48: "There's not between 4-6 outcomes"
    }

    def task_list_with_courses(df, stakeholder):
        """
        input: pandas dataframe
        output: Under each task, there is a list of courses that need intervention 
        """
        df = df.copy()
        tasks = stakeholder
        pass


    def course_list_with_tasks(df, stakeholder):
        """
        input: pandas dataframe
        output: Under each course, there is a list of tasks that needs intervention 
        """
        pass
    # for k,v in lx_iloc.items():
    #     if df.iloc[:, k] == "No":
    #         lst = []
    #         lst.append(df['Course Title'])
    #     print(v, lst)
    def get_to_do_list(df):
        df = df.copy()
        course_dict = defaultdict(list)
        for index, row in df.iterrows():
            name = row['Course Title']
            for i in range(df.shape[1]):
                if row[i] == "No" or row[i] == "Not sure":
                    course_dict[name].append(i)
        return course_dict
    
    def course_list_with_tasks(dictionary):
        """
        input: dictionary. keys are course titles, values are columns with 'no' responses.
        output: Under each course, there is a list of tasks that needs intervention 
        """
        #for k,v in lx_iloc.items():
        lx_to_do_lst = {key: lx_iloc.get(key, dictionary[key]) for key in dictionary}
        #for k,v in ac_dir_iloc.items():
        ### BECAUSE THIS CHANGES IN-PLACE
        ac_dir_to_do_lst = {key: ac_dir_iloc.get(key, dictionary[key]) for key in dictionary}
        return lx_to_do_lst, ac_dir_to_do_lst
    #print(to_do_list)
    to_do_list = get_to_do_list(df)
    lx_lst, ac_dir_lst = course_list_with_tasks(to_do_list)
    pprint.pprint(ac_dir_lst)
    
    # Association Dean