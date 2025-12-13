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
            raw_line = line[:varmı]
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


def build_inventory(lines):
    student=[]

    for line in lines:
        item=clean_student_record(line)
        if item is not None:
            student.append(item)