# PyWEB_HW-12_AIOHTTP
## Home work #11 - Weather app with AIOHTTP
В інтернеті багато інформації з різних джерел на одну й ту саму тему. Часто потрібно порівняти інформацію з різних джерел в одному місці. Це може бути потрібно для, наприклад, порівняння курсу валют у різних банках для пошуку найвигіднішого та/або середнього, порівняння цін на групи товарів у різних постачальників, пошуку першоджерела повідомлень новин тощо.

Основне завдання агрегатора полягає у зборі із зазначених Web-ресурсів інформації та відображення її в одному місці та зручній формі. Під ресурсом варто розуміти URL адресу сторінки, що вас цікавить.

### Напишіть свій агрегатор на Python з використанням AIOHTTP:
1. Виберіть тему, що вас цікавить, наприклад, результати спортивних подій.
2. Для теми, що вас цікавить, визначте кілька (2-3, можна більше) ресурсів, які будуть для вас першоджерелами.
3. На кожному такому ресурсі оберіть розділ або кілька сторінок з даними, що вас цікавлять.
4. апишіть відповідь для кожного ресурсу. Завданням обробника буде отримати з HTML відповіді лише ті дані, які вам потрібні у зручному форматі для відображення у вашому агрегаторі.
5. Реалізуйте відображення агрегованих та очищених даних на сторінці на вашому сервісі.
### Умови виконання:
1. Звідки збирати інформацію можете вказати у файлі налаштувань або зробити для цього окрему сторінку та зберігати список ресурсів у базі даних (можна sqlite).
2. Результати збирання інформації з джерел можете зберігати у базі даних чи зберігати стан, а відображати результат у режимі реального часу.
3. Реалізуйте обробку інформації з джерел, паралельно використовуючи корутини.
