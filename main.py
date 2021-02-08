residence_limit = 90  # 45, 60
schengen_constraint = 180

cost_per_day = 15
first_of_january = 1  # первое января текущего года

visits = [[1, 10], [21, 30], [45, 46], [251, 260], 2]

for visit in visits:
  if not isinstance(visit, list):
    raise Exception("Effor in visit ", visit)


total_time_in_es = 0

days_in_eu = []

for visit in visits:
  past_days = 0
  for past_visit in visits:
    if past_visit[0] <= visit[0] and past_visit[0] > visit[0] - schengen_constraint:
      past_days += past_visit[1] - past_visit[0] + 1
  days_in_eu.append(past_days)
  total_time_in_es += visit[1] - visit[0] + 1

print(days_in_eu)
assert days_in_eu == [10, 10 + 10, 10 + 10 + 2, 10]

for visit, days in zip(visits, days_in_eu):
  if days > residence_limit:
    print("In visit", visit, "you was in EU too long:", days, "day(s)")

#assert total_time_in_es == 10 + 10 + 2 + 10

if total_time_in_es > residence_limit:
    print('Вы не можете прибывать в ЕС так долго')

print('Вы пробудете в ЕС дней:', total_time_in_es)