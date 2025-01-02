# 새로운 가상환경 생성
# conda create --name codyssey pandas
# 가상 환경 실행
# conda activate codyssey
# 영화 개수, 배급사 수, 감독 수, 출연진 수, 장르 수를 파악

import pandas as pd

# 데이터 읽기
data = pd.read_csv('prob-0101.csv')

# 각 항목 계산
num_movies = len(data)  # 영화 개수
num_distributors = data['배급사'].nunique()  # 배급사 수 (중복 제거)
num_directors = data['감독'].nunique()  # 감독 수 (중복 제거)
num_actors = data['출연진'].apply(lambda x: len(x.split(','))).sum()  # 출연진 수 (쉼표로 구분 후 합산)
num_genres = data['장르'].apply(lambda x: len(x.split(','))).sum()  # 장르 수 (쉼표로 구분 후 합산)

# 출연진의 중복을 제거하고 고유한 출연진 수를 계산
unique_actors = set()

def add_actors(actors_string):
    if isinstance(actors_string, str):
        actors = [actor.strip() for actor in actors_string.split(',')]
        unique_actors.update(actors)

data['출연진'].apply(add_actors)
num_unique_actors = len(unique_actors)


# 결과 출력
print(f"영화 개수: {num_movies}")
print(f"배급사 수: {num_distributors}")
print(f"감독 수: {num_directors}")
print(f"출연진 수: {num_actors}")
print(f"고유한 출연진 수: {num_unique_actors}")
print(f"장르 수: {num_genres}")
