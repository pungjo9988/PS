case = int(input())

for i in range(case):
    days, teams = map(int, input().split())
    peelist = list(map(int, input().split()))
    avverlist = []
    for j in range(days - teams + 1):
        