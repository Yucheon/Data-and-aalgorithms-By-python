# part1_file_unpicke.py

import pickle as pkl
from part1_file_pickle import Person


if __name__ == "__main__":
    # 피클링된 파일을 읽어올 떄에는 바이너리 읽기 모드로 읽어 온다.
    with open("my_data.pkl","rb") as file:
        data = pkl.load(file)

    # 가져온 기능을 실행해보자
    print(data["name"])


    with open("hong_person.pkl", "rb") as file: # hong_person.pkl이란 파일을 바이너리 일기모드로 읽어와서
        Person = pkl.load(file) # Person을 정의하고

    hong = Person("김범준", 30) # 내용을 초기화 시키고
    my = Person("지완", 29)
    print(hong.introduce()) # 클래스 내부의 함수를 출력 시킨다.
    print(my.introduce())