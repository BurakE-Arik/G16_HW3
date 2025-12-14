def load_raw_lines(filename):
    filenamelister=[]
    try:
        with open (filename, "r") as f:
            for line in f :
                filenamelister.append(line.strip())
        return filenamelister
    except FileNotFoundError:
        print("Dosya bulunamadı ismini kontrol et ")
        return []
    except Exception as e:
        print("bir hata oluştu",e)
        return []


def clean_inventory_item(line):
    if line=="":
        print("satır boş")
        return None
    else:
        line=line.replace("-"," ")
        line=line.replace("*","")
        line=line.strip()
        line=line.title()
        line_list=line.split()
        if len(line_list)<2:
            print("linedaki karakter sayısında bir problem var ")
            return None
        try:
            weight_str =line_list.pop()
            weight=float(weight_str)

            name= " ".join(line_list)
            return name , weight
        except Exception as e:
            print("bir hata oluştu " , e)
            return None
        
def build_inventory(lines):
    inventory=[]

    for line in lines:
        item=clean_inventory_item(line)
        if item is not None:
            inventory.append(item)


def clean_student_record(line):
    if line =="":
        print("satırboş")
        return None
    else :
        varmı=line.find("House")
        varmı2=line.find("score=")
        if varmı != -1 and varmı2 != -1:
            raw_line = line[:house_index]
            name=raw_line.strip().capitalize()
            deneme=line.split("; ")
            house_kısmı=deneme[1]
            house_kısmı=house_kısmı.split()
            house=house[1]
            puan_kısmı=deneme[2]
            puan=puan_kısmı.split("=")

            if 0<int(puan[1])<100:
                return (name,house,puan[1])

            
        else:
            print("house ve score yok ")     


def build_student_list(lines):
    student=[]

    for line in lines:
        item=clean_student_record(line)
        if item is not None:
            student.append(item)

def compute_inventory_stats(inventory_list):
    total_items=0
    total_weight=0
    heaviest_item=None
    max_weight=-1
    for item in inventory_list:
        total_items+=1
        total_weight+=item[1]
        if item [1]>max_weight:
            max_weight=item[1]
            heaviest_item=item
    return (heaviest_item,max_weight,total_weight,total_items)

def compute_students_stats(student_list):
    total_students=0
    passing_count=0
    total_score=0
    best_student=None
    max_score=-1
    house_counts={}
    for students in student_list:
        total_students+=1
        total_score+=students[2]

        if students [2]>max_score:
            max_score=students[2]
            best_student=students

        #bina sayımını anlamadım dönünce anlatırsın 





    if total_students!=0:
        ortalama=total_score/total_students
    else:
        ortalama=0
    
    return total_students, passing_count, ortalama, best_student, house_counts



def print_report(inv_stats,stud_stats):
    print("Inventory Summary")
    print("totalitem" total_items)
    print("totalweight"total_weight)#ondalıklı yazılcakmış tam anlamadım
    print("heaviest_item" heaviest_item[0],heaviest_item[1]"kg")
    print("students performance ")

    print("total students"total_students)
    print("passing_students"passing_count)
    print("ortalama" ortalama)
    print("topstudnets" best_student[0] ,beststudent[1] best_student[2])
    #sortedla sıralıcaz ama tam anlamadım for döngüsü artı sortad galiba
    print(house_counts)