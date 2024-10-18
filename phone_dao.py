# 

# 리스트 
file_path = "C:\\javaStudy\\workspace-python\\Phonefile\\PhoneDB.txt"

def read_phonefile(file_path):
    with open(file_path, "r", encoding="utf-8") as person_list:
        for person_vo in person_list:
            person = person_vo.strip().split(",")
            print(f"{person[0]}\t{person[1]}\t{person[2]}")


# 등록