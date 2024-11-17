import plotly.graph_objs as go
import csv

# Загрузка данных из CSV-файла
with open('data.csv') as file:
    reader = csv.DictReader(file)
    data = list(reader)

# Определение соответствия дат индексам
date_mapping = {'12.09.2018': 0, '12.10.2018': 1, '12.11.2018': 2, '12.12.2018': 3}
reverse_date_mapping = {v: k for k, v in date_mapping.items()}

# Инициализация контейнеров для каждого показателя
metrics = ['<OPEN>', '<HIGH>', '<LOW>', '<CLOSE>']
data_by_date = {metric: [[] for _ in range(4)] for metric in metrics}

# Обработка и группировка данных
for row in data:
    date_index = date_mapping[row['<DATE>']]  # Получаем индекс для текущей даты
    for metric, col_index in zip(metrics, range(4, 8)):
        # Добавляем значения показателей (Open, High, Low, Close) в соответствующую группу
        data_by_date[metric][date_index].append(int(row[metric]))

# Создание графиков Box Plot с использованием Plotly
fig = go.Figure()

for i in range(4):
    current_date = reverse_date_mapping[i]  # Получаем дату по индексу
    for metric in metrics:
        trace_name = f"{current_date} - {metric[1:-1].lower().capitalize()}"  # Имя для текущего графика
        fig.add_trace(go.Box(y=data_by_date[metric][i], name=trace_name))

# Настройка макета графика
fig.update_layout(
    legend=dict(yanchor="top", orientation="h", y=1.2),  # Положение легенды
    xaxis=dict(tickangle=90, title_standoff=25)  # Настройка оси X
)

fig.show()  # Отображение графика
