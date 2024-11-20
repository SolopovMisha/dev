# Обрезка ссылок с помощью ВКонтакте

Это приложение позволяет пользователям сокращать длинные URL-адреса, используя API ВКонтакте. Оно упрощает процесс обмена ссылками, делая их более удобными для использования.

## Как установить

1. Убедитесь, что Python 3 установлен. Вы можете скачать его с [официального сайта](https://www.python.org/downloads/).
2. Установите зависимости с помощью pip (или pip3, если есть конфликт с Python 2):
   

   `pip install -r requirements.txt`
   
3. Получите токен доступа к API ВКонтакте:
   - Перейдите на [страницу разработчиков ВКонтакте](https://vk.com/dev/access_token).
   - Создайте новое приложение и получите токен.
   - Токен будет выглядеть как строка, например: abcdef1234567890abcdef1234567890abcdef1234567890.
4. Создайте файл .env в корневом каталоге проекта и добавьте туда ваш токен в следующем формате:
   
   `telegram_token = ваш токен доступа`
   
## Использование

После установки и настройки приложения вы можете запустить его через командную строку (CMD):

1. Откройте командную строку (CMD).
2. Перейдите в каталог проекта с помощью команды cd, например:
   ⠀
    `cd путь\к\вашему\проекту`
⠀   
3. Запустите приложение, выполнив команду:
   
⠀    ⠀`python имя_вашего_скрипта.py http://ваша_ссылка_для_сокращения`

## Цель проекта

Код написан в образовательных целях на онлайн-курсе для веб-разработчиков [dvmn.org](https://dvmn.org/). Проект помогает понять, как работать с API и обрабатывать HTTP-запросы на Python.