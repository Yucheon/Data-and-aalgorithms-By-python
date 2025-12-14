# part1_feil_pickle.py
# 피클링(pickling) 예제

import pickle as pkl

data = {
    "name": "홍길동",
    "age": 30
}

class Person():
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        print(f"my name is {self.name}\n age is {self.age}")

if __name__ == "__main__":
    # data 딕셔너리를 바이너리 형식으로 피클링하여 'my_data.pkl' 파일로 저장한다.
    with open("my_data.pkl", "wb") as file:
        pkl.dump(data, file)

    # Person 클래스 자체를 피클링하여 'hong_person.pkl' 파일로 저장한다.
    # (클래스 정의 자체를 직렬화하는 경우는 흔하지 않고, 이렇게 하면
    # 이후에 피클에서 클래스를 불러올 수 있다.)
    with open("hong_person.pkl", "wb") as file:  # 'hong_person.pkl' 파일을 쓰기 모드로 열고
        pkl.dump(Person, file)  # Person 클래스를 파일에 피클링(직렬화)한다.
