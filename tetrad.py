
# python -m venv venv # Создает виртуальное окружение в папке venv
# .\venv\Scripts\activate # Активирует виртуальное окружение (Windows)
# source venv/bin/activate # Активирует виртуальное окружение (Linux/Mac)

# pip install django # Устанавливает Django в виртуальное окружение
# django-admin startproject core . # Создает новый проект Django в текущей папке
# python manage.py startapp main # Создает новое приложение Django с именем main
# python manage.py migrate # Применяет миграции к базе данных
# python manage.py runserver # Запускает сервер разработки Django
# python manage.py createsuperuser # Создает суперпользователя для доступа к админке Django



# Django — это фреймворк на Python для веб-разработки.
# Он помогает быстро создавать сайты и веб-приложения.







# Django — это фреймворк на Python для веб-разработки.
# Он помогает быстро создавать сайты и веб-приложения.
# Основан на принципе MTV (Model–Template–View) — 
#                          это похоже на MVC (Model–View–Controller).


# Model — это работа с данными (как таблица в базе данных).
# Template — это внешний вид (HTML-страницы).
# View — это логика (код, который обрабатывает запросы).



# Библиотека — это как набор инструментов (молоток, отвертка, линейка). 
# Ты сам решаешь, как их использовать.

# Фреймворк — это уже половина построенного дома, в который ты вставляешь 
# свои окна и двери. Он задаёт структуру проекта.





# MTV
# Model (Модель) → отвечает за работу с базой данных. (Таблицы → Классы Python)
# Template (Шаблон) → отвечает за внешний вид, HTML-страницы.
# View (Представление) → связывает модель и шаблон, управляет логикой.


# python manage.py makemigrations # Создает миграции на основе изменений в моделях
# python manage.py migrate # Применяет миграции к базе данных














# Django админ-панель

# Это встроенный интерфейс для управления данными в базе (CRUD — Create, Read, Update, Delete).
# Автоматически генерируется для моделей.
# Очень удобно для админов, тестов, менеджеров.
# Чтобы включить её, в settings.py уже есть:

# INSTALLED_APPS = [
#     ...
#     'django.contrib.admin',
#     ...
# ]

# urlpatterns = [
#     path('admin/', admin.site.urls),
# ]


# 1. list_display
# Показывает колонки в списке объектов.

# 2. search_fields
# Добавляет строку поиска.
# Можно искать даже по ForeignKey (search_fields = ('group__name',)).

# 3. list_filter
# Фильтрация справа по указанным полям.

# 4. ordering
# Сортировка по умолчанию.

# 5. list_editable
# Позволяет редактировать поля прямо в списке.

# 6. list_per_page
# Сколько записей отображать на одной странице.

# 7. readonly_fields
# Поля только для чтения (например, даты).

# 8. fieldsets
# Группировка полей в админке.

# 9. prepopulated_fields
# Автогенерация значений. Например, last_name из name:
# prepopulated_fields = {'last_name': ('name',)}

# 10. date_hierarchy
# Навигация по датам сверху.
# date_hierarchy = 'created_at'

# 11. fields
# Определяет порядок и набор отображаемых полей в форме.

# 12. exclude
# Исключает поля из формы редактирования.

# 13. actions
# Создаёт кастомные действия для списка объектов.

# @admin.action(description="Активировать пользователей")
# def make_active(modeladmin, request, queryset):
#     queryset.update(is_active=True)

# actions = [make_active]


# 14. list_display_links
# Делает поля из list_display кликабельными для перехода в детали объекта.

# 15. save_on_top
# Кнопки "Сохранить" появляются сверху формы.

















