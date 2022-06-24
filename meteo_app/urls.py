# Выпускная квалификационная работа
# Студентки группы А-12-18
# Красавиной Дарьи Дмитриевны

# Листинг модуля "urls.py" приложения "meteo_app"

# ==========

# Импортируемые модули
from django.urls import path
from . import views

urlpatterns = [
    # Адрес страницы авторизации
    path('', views.auth_page, name="auth-page"),
    # Адрес страницы регистрации
    path('reg', views.reg_view, name="reg-page"),
    # Адрес для выхода
    path('logout', views.logout_view, name='logout'),
    # Адрес страницы информации о приложении
    path('info', views.info_view, name='info-page'),
    # Адрес главной страницы
    path('main', views.main, name='main-page'),
    path('main-logout', views.main_logout, name='main-logout'),
    # Адреса для отображения данных
    path('meteo-data', views.meteo_data, name='meteo-data'),
    path('wind-data', views.wind_data, name='wind-data'),
    path('invertor-data', views.invertor_data, name='invertor-data'),
    # Адреса для скачивания данных в различных форматах
    path('download/meteo-data', views.download_meteo_data, name='download-meteo-data'),
    path('download/meteo-data-xlsx', views.download_meteo_data_xlsx, name='download-meteo-data-xlsx'),
    path('download/wind-data', views.download_wind_data, name='download-wind-data'),
    path('download/wind-data-xlsx', views.download_wind_data_xlsx, name='download-wind-data-xlsx'),
    path('download/invertor-data', views.download_invertor_data, name='download-invertor-data'),
    path('download/invertor-data-xlsx', views.download_invertor_data_xlsx, name='download-invertor-data-xlsx'),
    # Адреса для отображения графиков
    path('meteo-data/meteo-graph', views.create_meteo_graph, name='meteo-data-graph'),
    path('meteo-data/wind-graph', views.create_wind_graph, name='wind-data-graph'),
    path('meteo-data/invertor-graph', views.create_invertor_graph, name='invertor-data-graph'),
]
