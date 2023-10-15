# Tree menu


![alt text](https://github.com/Homerw223v/tree_menu/blob/main/example.png)

Для запуска в докере необходимо в консоли в корневой директории запустить команды по очереди:  
```bash
sudo docker-compose build
sudo docker-compose up
```
После запуска контейнера необходимо создать суперпольхователя. Откройте еще одно окно консоли и запустите команду:  

```bash
sudo docker-compose exec -ti django python manage.py createsuperuser

```

После ввода данных можете переходить по адресу http://0.0.0.0:8000/  или http://0.0.0.0:8000/admin/ для добавления меню.

Если же хотите запустить не используя Docker то необходимо:  

Установить зависимости командой:  

```bash
pip install -r requirements.txt
```
создать суперпользователя  

```bash
python3 manage.py createsuperuser --settings=tree_menu.settings_base
```
и запустить приложение.
```bash
python3 manage.py runserver --settings=tree_menu.settings_base
```
И переходите по адресу http://127.0.0.1:8000/ 

Проверено на Ubuntu
