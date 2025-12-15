# part1_file_unpickle.py

import pickle as pkl
from part1_file_pickle import Person  # 원래 Person 클래스를 임포트하지만 아래에서 덮어씌워짐

if __name__ == "__main__":
    # 피클링된 'my_data.pkl' 파일을 바이너리 읽기 모드로 열어 데이터를 로드한다.
    with open("my_data.pkl", "rb") as file:
        data = pkl.load(file)

    # 불러온 데이터의 'name' 값을 출력한다.
    print(data["name"])

    # 'hong_person.pkl' 파일을 바이너리 읽기 모드로 열어 클래스를 로드한다.
    with open("hong_person.pkl", "rb") as file:
        Person = pkl.load(file)  # 피클에서 불러온 Person 클래스를 변수에 할당

    # 불러온 Person 클래스를 사용해 새로운 인스턴스 생성
    hong = Person("김범준", 30)

    # 인스턴스의 introduce 메서드를 호출해 정보를 출력한다.
    print(hong.introduce())
