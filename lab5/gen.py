import matplotlib.pyplot as plt
import random

# Создаем списки для названий и координат точек
labels = [
    "Исполнительный директор",
    "Отдел разработки",
    "Отдел маркетинга",
    "Разработчик бэкэнда",
    "Разработчик сайта",
    "Архитектор",
    "Маркетолог"
]

x_values = [random.uniform(0, 10) for _ in labels]
y_values = [random.uniform(0, 10) for _ in labels]

# Создаем график
plt.figure(figsize=(10, 8))
plt.scatter(x_values, y_values, marker='o', color='b')

# Добавляем названия точек
for i in range(len(labels)):
    plt.annotate(labels[i], (x_values[i], y_values[i]), fontsize=12, ha='center', va='bottom')

# Добавляем перекрестные пунктирные линии
plt.axhline(5, linestyle='--', color='gray')
plt.axvline(5, linestyle='--', color='gray')

# Настройки осей и заголовок
plt.xlabel('Доходность')
plt.ylabel('Перспективность')
plt.title('График Доходности и Перспективности')

# Сохраняем график в файл
plt.savefig('график.png')

# Отображаем график
# plt.show()