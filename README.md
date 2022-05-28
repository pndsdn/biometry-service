# Biometry tracking service
## Установка
Склонируйте репозиторий, используя команду:
```bash
git clone https://github.com/pndsdn/biometry-service.git
```
Перейдите в директорию проекта и запустите docker-compose:
```bash
cd biometry-service
docker-compose up -d
```
__ПРИМЕЧАНИЕ:__
Версия docker-compose должна быть 1.26 и выше.

После сборки образа запустите следующую команду для создания схемы и таблицы БД:
```bash
docker-compose up -d init_db
```
__ПРИМЕЧАНИЕ:__
Данную команду нужно выполнить один раз. После остановки и 
повторного запуска контейнеров её выполнять __НЕНУЖНО__

Остановка контейнеров:
```bash
docker-compose stop
```
Повторный запуск:
```bash
docker-compose start
```