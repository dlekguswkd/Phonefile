# 

# 리스트 
file_path = "C:\\javaStudy\\workspace-python\\Phonefile\\PhoneDB.txt"

def read_phonefile(file_path):
    with open(file_path, "r", encoding="utf-8") as person_list:
        for index, person_vo in enumerate(person_list, start=1):  # start=1로 인덱스를 1부터 시작
            person = person_vo.strip().split(",")
            print(f"{index}     {person[0]}\t{person[1]}\t{person[2]}")  # 인덱스를 출력


# 등록
def add_phonefile(file_path):
    with open(file_path, "r", encoding="utf-8") as person_list:
        p_list = person_list.read() # 전체 내용 읽기
        #print(p_list)

    name = input(">이름: ")
    hp = input(">휴대전화: ")
    company = input(">회사전화: ")

    add = f"{name}, {hp}, {company}\n"

    with open(file_path, "w", encoding="utf-8") as person_list:
        person_list.write(p_list)   # 원래있던거 적기
        person_list.write(add)      # 새로운 데이터 적기

    print("[등록되었습니다.]")


# 삭제
def delete_phonefile(file_path):
    # 전화번호부를 읽어들여서 데이터를 리스트로 저장
    with open(file_path, "r", encoding="utf-8") as person_list:
        lines = person_list.readlines()  # 각 줄을 리스트로 읽어오기

    for index, person_vo in enumerate(lines, start=1):
        person = person_vo.strip().split(",")
        print(f"{index}     {person[0]}\t{person[1]}\t{person[2]}")  # 인덱스와 함께 출력


    # 삭제할 항목의 인덱스 입력
    try:
        delete_no = int(input(">번호: ")) - 1  # 0-based index로 처리
        if delete_no < 0 or delete_no >= len(lines):
            print("[잘못된 번호입니다. 다시 시도해주세요.]")
            return
    except ValueError:
        print("[유효하지 않은 입력입니다. 다시 시도해주세요.]")
        return

    # 선택한 인덱스에 해당하는 데이터를 삭제한 새 리스트 만들기
    del lines[delete_no]

    # 파일에 변경된 리스트 다시 저장
    with open(file_path, "w", encoding="utf-8") as person_list:
        person_list.writelines(lines)

    print("[삭제되었습니다.]")


# 검색
def search_phonefile(file_path):
    search_value = input(">이름: ")

    # 전화번호부를 읽어들여서 데이터를 리스트로 저장
    with open(file_path, "r", encoding="utf-8") as person_list:
        lines = person_list.readlines()  # 각 줄을 리스트로 읽어오기

    found = False  # 검색 결과가 있는지 체크하는 변수

    for index, person_vo in enumerate(lines, start=1):
        person = person_vo.strip().split(",")
        # 이름이나 휴대전화 번호가 검색어에 포함되어 있으면 출력
        if search_value in person[0] or search_value in person[1]:
            print(f"{index}     {person[0]}\t{person[1]}\t{person[2]}")  # 인덱스와 함께 출력
            found = True

    if not found:
        print("[검색된 결과가 없습니다.]")