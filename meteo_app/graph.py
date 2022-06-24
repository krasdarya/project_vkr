# Выпускная квалификационная работа
# Студентки группы А-12-18
# Красавиной Дарьи Дмитриевны

# Листинг модуля "graph.py"

# =========================

# Импортируемые модули
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
from meteo_app.models import MeteoData, WindData, Invertor


# Функция построения графика
def plot_graphic(queryset=None, range=1, param=None, seconds=False):
    if queryset:
        # Списки для отображения осей
        x = list()
        y = list()
        # Датасет - список кортежей вида (дата, параметр из таблицы)
        dataset = [(d.date, getattr(d, param)) for d in queryset]
        # Если строить по секундам
        if seconds:
            for i, d in enumerate(dataset):
                # Отображение каждого значения
                if i % range == 0:
                    x.append(d[0].strftime('%Y-%m-%d %H:%M:%S'))
                    y.append(d[1])
        # Отображение по минутам
        else:
            xy = dict()
            for d in dataset:
                # Если ключа по этой дате нет в словаре
                if d[0].strftime('%Y-%m-%d %H:%M') not in xy:
                    # Добавить значение по ключу
                    xy[d[0].strftime('%Y-%m-%d %H:%M')] = d[1]
            
            print(xy)
            # Добавить значения в списки - формирование осей х, у
            for ax, ay in xy.items():
                x.append(ax)
                y.append(ay)

        # Директива для корректного отображения png
        matplotlib.use('Agg')
        fig = plt.figure()
        fig.set_figheight(12)
        fig.set_figwidth(10)
        
        ax = fig.add_subplot()

        ax.set_xlim([0, len(x) + 1])
        ax.set_xlim([0, len(y) + 1])
        
        ax.set_xlabel("Дата")
        ax.set_ylabel("Значение параметра")
        ax.set_title("Граф")

        # Если на оси больше 25 значений
        if len(x) >= 25:
            # не подписывать точки по оси
            ax.set_xticks([])
        if len(y) >= 25:
            ax.set_yticks([])
        # Параметры графика
        ax.plot(x, y, color='blue', label='Параметр')
        plt.xticks(rotation=30, fontsize=10)
        ax.legend()
        plt.grid(True)
        plt.savefig('meteo_app/static/meteo_app/graph.png', dpi=100)
        print('LOGGING: IMAGE CREATED')
        
        return True
    else:
        return False

