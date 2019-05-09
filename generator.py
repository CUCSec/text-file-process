import random
import datetime

if __name__ == '__main__':
  sid_list = list()
  with open('students@python', encoding='utf8') as f:
    for line in f:
      sid = line.split(',')[0]
      sid_list.append(sid)

  for sid in sid_list:
    others = sid_list.copy()
    others.remove(sid)

    count = random.randint(50, 200)

    output_records = list()
    for i in range(0, count):
      time = datetime.datetime.now().isoformat()
      record = f'课程：python, 学号：{sid}, 时间：{time}'
      output_records.append(record)

    for i in range(count, 1000):
      time = datetime.datetime.now().isoformat()
      random_id = random.choice(others)
      record = f'课程：python, 学号：{random_id}, 时间：{time}'
      output_records.append(record)

    random.shuffle(output_records)

    with open(f'{sid}.log', 'w', encoding='utf8') as output_file:
      for r in output_records:
        output_file.write(r + '\n')
