import csv
from statistics import mean

rtg_by_movie_id = {}
rtg_by_user_id = {}
movie_names = {}


def viewed_enough():
    print(rtg_by_movie_id)
    viewed_enough = [key for key in rtg_by_movie_id if len(rtg_by_movie_id[key][0]) > 15]
    return viewed_enough


def get_data(rtg_by_movie_id, rtg_by_user_id, movie_names):
    with open('u.data') as f:
        reader = csv.reader(f)
        for row in reader:
            row = row[0].split('\t')
            row[2] = int(row[2])
            if row[1] in rtg_by_movie_id:
                rtg_by_movie_id[row[1]].append(row[2])
            else:
                rtg_by_movie_id[row[1]] = [row[2]]
            if row[0] in rtg_by_user_id:
                rtg_by_user_id[row[0]].append((row[1], row[2]))
            else:
                rtg_by_user_id[row[0]] = [(row[1], row[2])]

    with open('u.item', encoding='latin_1') as f:
        reader = csv.reader(f)
        for row in reader:
            row = row[0].split('|')
            movie_names[row[0]] = [row[1]]

    return (rtg_by_movie_id, rtg_by_user_id, movie_names)


class Movie:
    def __init__(self, item_id):
        self.item_id = item_id
        self.avg_rtg = 0  #  change this 

    def avg_rtg(self, rtg_by_movie_id):
        return mean(rtg_by_movie_id(self.item_id))


class User:
    def __init__(self, user_id):
        self.user_id = user_id


def main():

    print(get_data(rtg_by_movie_id, rtg_by_user_id, movie_names))
    print(viewed_enough())

main()
