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

Если же хотите запустить не используя Docker то необходимо убрать файл settings.py из папки tree_menu и переименовать файл settings_base.py в setting.py

После необходимо установить необходимые зависимости командой:  

```bash
pip install -r requirements.txt
```

и все готово для работы.  
Запускайте приложение командой  
```bash
python3 manage.py runserver
```
И переходите по адресу http://127.0.0.1:8000/ 

Проверено на Ubuntu
