# Модуль 30
Задания 30.3.1 и 30.5.1.

Задание 30.3.1

Написать тест, который проверяет, что на странице со списком питомцев пользователя: 
1. Присутствуют все питомцы. 
2. Хотя бы у половины питомцев есть фото. 
3. У всех питомцев есть имя, возраст и порода. 
4. У всех питомцев разные имена. 
5. В списке нет повторяющихся питомцев. (Сложное задание).

Задание 30.5.1.

1. В написанном тесте (проверка карточек питомцев) добавьте неявные ожидания всех элементов (фото, имя питомца, его возраст). 
2. В написанном тесте (проверка таблицы питомцев) добавьте явные ожидания элементов страницы.

В файле conftest.py находятся 2 фикстуры:

фикстура с драйвером и переходом на страницу авторизации;
фикстура для перехода на страницу "Мои питомцы".
В файле settings.py находятся данные об эл.почте и пароле.