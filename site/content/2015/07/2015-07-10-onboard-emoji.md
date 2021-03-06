Title: Экранная Emoji клавиатура для Ubuntu
Date: 2015-07-10 21:40:00
Category: it  
Tags: ubuntu, onboard, emoji, keyboard
Author: qnub  
Image: /images/it/onboard-emoji.png
Slug: 2015-07-10-onboard-emoji

Наконец дошли руки сделать экранную клавиатуру для ввода **«emoji»**.

**TL;DR** <https://github.com/qnub/onboard-emoji>

Точнее не клавиатуру, а раскладку для уже существующей софтверной клавиатуры **«OnBoard»**. Я тут пару месяцев проводил эксперимент с жизнью в **Mac OS**, после чего успешно вернулся к родной **Ubuntu**. Не буду здесь расписывать чем она лучше/хуже для меня — это тема для отдельного поста, но скажу, что некоторых штук которые были там мне в здесь не достаёт. В частности вызываемая хоткеем панель для ввода **«emoji»**. Почему-то оказалось что в убунтах аналога этому нет хотя возможности для несложной реализации имеются.

Я много гуглил разные варианты ввода emoji в **linux** но всё заканчивалось только их выводом. Кстати для этого достаточно просто установить шрифт **Symbola**:

    :::bash
    sudo apt-get install ttf-ancient-fonts

Как вариант можно установить [Noto Emoji](https://github.com/googlei18n/noto-emoji) или [EmojiSymbols](http://emojisymbols.com/beforeuse.php) (или всё сразу). Система в большинстве случаев пытается найти отсутсвующий в шрифте по-умолчанию символ в других шрифтах. Бывают казусы, вроде как в редакторе **Atom** но тут он решается простым указанием нескольких шрифтов через запятую:

![atom font config]({filename}/images/it/atom-font-config.png)

В общем при наличии довольно неплохой и настраиваемой экранной клавиатуры **OnBoard** с довольно прямолинейным созданием любых раскладок для неё — оказалось ни кто ещё не создал раскладки с emoji. Т.е. раскладки где они есть — существуют, но ≈25 emoji это же не серьёзно! 😂 А так как у меня тут выдалась свободная неделька — я решил этот пробел заполнить.

Для уcтановки emoji раскладки в OnBoard нужно [скачать архив c emoji раскладкой для **OnBoard**](https://github.com/qnub/onboard-emoji/archive/master.zip) и скопировать содержимое папки `layout` в `~/.local/share/onboard/layouts`.

Дальше в `Параметры системы… → Специальные возможности` на вкладке `Ввод` включить `Экранную клавиатуру`:

![onscreen keyboard enable]({filename}/images/it/onscreen-keyboard-enable.png)

Это будет автоматически запускать сервис **OnBoard** для вас. Теперь в трее появится значок запущенной клавиатуры и, скорее всего появится плавающий значок на экране. Рекомендую зайти в настройки и перенастроить на свой вкус, там довольно много опций и вариантов использования. Основные настройки у меня выглядят так:

![onboard general settings]({filename}/images/it/onboard-general-settings.png)

Также в `Параметры системы… → Клавиатура` я добавил сочетание клавиш для быстрого вызова кливатуры (команда `onboard`):

![onboard hotkey]({filename}/images/it/onboard-hotkey.png)

Теперь когда нужно где-то вставить смайлик я жму `Ctrl+Super+Space`, тыкаю в появившейся клавиатуре нужную кнопку и нажимаю справа на ней «крест» чтобы эту клавиатуру скрыть… На [гитхабе](https://github.com/googlei18n/noto-emoji) есть сорцы, а также описание как кастомизировать всё это дело. Пулл-реквесты приветствуются!

[GitHub](https://github.com/googlei18n/noto-emoji)  
[архив c emoji раскладкой для **OnBoard**](https://github.com/qnub/onboard-emoji/archive/master.zip)
