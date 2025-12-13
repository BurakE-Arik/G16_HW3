def load_raw_lines(file:str):
    try:
        with open(file,"r") as fl:
            return fl.readlines()
    except Exception as e:
        print(f"An error occurred! {e}")

def clean_inventory_item(file="inventory_data.txt"):
    lines = load_raw_lines(file)
    temp_line_list = []
    for single_line in lines:
        
        single_line = single_line.strip()
        
        single_line = single_line.replace(" ","")
        
        if  "|" in single_line:
            single_line = single_line.replace("|"," >")
            
        if "-" in single_line:
            single_line = single_line.replace("-"," ")
        
        single_line = single_line.replace("\n","")
        
        single_line = single_line.title()
        
        single_line = single_line.replace("Kg","g")
        
        temp_line_list.append(single_line)

    return temp_line_list

def build_inventory(file = "inventory_data.txt"):
    temp_line_list = clean_inventory_item(file)
    inventory = []
    
    for line in temp_line_list:
        temp_inv_list = []
        first_half = line[:line.find(" >")]
        second_half = line[line.find(" >")+2:]
        
        second_half = second_half.replace("g","")
        second_half = float(second_half)
        second_half *= 100
        second_half = str(int(second_half)) + "g"
                
        temp_inv_list.append(first_half)
        temp_inv_list.append(second_half)
        
        inventory.append(tuple(temp_inv_list))
    return inventory
    
def clean_student_record(file:str):
    raw_lines = load_raw_lines(file)
    temp_list = []
    for raw_line in raw_lines:
        raw_line = raw_line.strip()
        raw_line = raw_line.lower()
        
        if ";" in raw_line:
            raw_line = raw_line.replace(";","")
            
        if "house" in raw_line:
            raw_line = raw_line.replace("house","")
            
        if "  " in raw_line:
            raw_line = raw_line.replace("  "," ")
            
        if "=" in raw_line:
            raw_line = raw_line.replace("=","")
        
        if "score" in raw_line:
            raw_line = raw_line.replace("score","")
            
        temp_list.append(raw_line.split())   
            
            
    return temp_list    

def build_student_list(file:str):
    temp_list = clean_student_record(file)
    
    student = []
    
    for list_inside in temp_list:
        for i in list_inside:
            temp_stu_list = []
            if i.isalpha() == True:
                list_inside[list_inside.index(i)] = i.capitalize()

            one_three = f"{list_inside[0]} {list_inside[1]}"
            two_three = list_inside[2]
            three_three = list_inside[3]

            temp_stu_list.append(one_three)
            temp_stu_list.append(two_three)
            temp_stu_list.append(three_three)

        student.append(tuple(temp_stu_list))
    return student


def compute_inventory_stats():
    inventory = build_inventory("inventory_data.txt")
    number_valid_item = 0
    total_weight = 0
    pre_item = 0
    for item in inventory:
        number_valid_item += 1
        temp_info = item[1]
        
        weight_of_object = item[1].replace("g","")
        
        weight_of_object = int(weight_of_object)   
        
        print(weight_of_object)
        
        if pre_item < weight_of_object:
            pre_item = weight_of_object
        else:
            heaviest_item = pre_item
             
        total_weight += weight_of_object
        
    total_weight /= 100
        
        
            
    print (f"Number of valid items: {number_valid_item}\nTotal weight: {total_weight:.2f} KG\nHeaviest item: {heaviest_item}")

    
    
compute_inventory_stats()
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    

def compute_student_stats():
    pass

def print_report():
    pass

def main():
    inventory=[]
    pass

