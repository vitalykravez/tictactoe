Игра «Крестики-нолики»

Игра реализована на базе библиотеки pygame. Компьютер играет за обе стороны по очереди. В конце игры выводится результат и история ходов обоих игроков. 

Управление:

Для совершения очередного хода нажмите на клавиатуре клавишу KEY_RIGHT (стрелка вправо). Для выхода из игры нажмите на клавиатуре на клавишу ESCAPE (Esc).

В игре реализован алгоритм случайного проставления символов на поле обеими игроками.

<<<<<<< HEAD
Запуск исполняемого файла ttt.py: py src/ttt.py
=======
Замечания автора:

В дальнейшем возможна реализация ИИ ботов методом минимакса и методом альфа-бета отсечения (актуально для большего размера игрального поля). Так же вполне реалистично выглядит написание и обучение нейронной сети, или же использование существующих (для большого размера игрального поля данная задача перетекает в реализацию игры в шашки Go).

Увеличение игрового поля или длины победной линии считаю не целесообразным без вменяемого алгоритма ИИ бота. На данном этапе моих знаний (как и времени на выполнение), очевидно, не достаточно для реализации сложных алгоритмов из таких сфер, как теория игр и машинное обучение.
>>>>>>> 3ea46fbe95ee248bff3abe7348ef18921143c880
