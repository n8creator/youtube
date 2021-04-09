# Техническая информация по разработке

# Содержание
[1. Загрузчик списка видео с YouTube канала](#1.-Загрузчик-списка-видео-с-YouTube-канала)



## 1. Загрузчик списка видео с YouTube канала
***
### 1.1. Задача

* Необходима разработка скрипта, который бы позволял сохранять список всех загруженных роликов с конкретного YouTube-канала
* Выгрузка должна производиться в CSV-файл в формате *"Название | URL | Дата загрузки"*


### 1.2. Попытка решения задачи с помощью requests и Selenium
1. Первоначальное решение было сделано в с помощью библиотеки `requests` ([ссылка на решение в проекте Edu](https://github.com/n8creator/edu/blob/main/m-parsing/11-ajax2.py)), но оно имеет ряд недостатков:
   1. Достаточно сложный и объемный код
   2.  Сложная логика &mdash; при первом запросе через `requests` отдается `html` содержимое, из которого нужно выдергивать `Continuation Tags`, и потом уже с помощью них составлять новые запросы, которые будут отдавать JSON-объекты
   3.  Для выполнения `request` запросов к YouTube, нужно передавать `headers` и `cookie` &mdash; в проекте [Edu](https://github.com/n8creator/edu/blob/main/m-parsing/11-ajax2.py) я делал их статическими, что было неправильно, поскольку терялась автономность библиотеки (куки и заголовки устаревают, и значит их нужно вручную копировать из браузера)
2. Для решения проблемы с `cookies` и `headers` я реализовал скрипт на Selenium, который загружал страницу в `headless` браузере и получал все неободимые данные &mdash; `cookies`, `headers` и контент страницы (см. решение в коммите [9ffad9c](https://github.com/n8creator/youtube/commit/9ffad9cf14e11e58f44825fa7ffd3b3888493dd6#diff-24e6654bfd1ab85bebb1f721a4be46e6fdb9ea8974d14442d3aaecd1f971fcbb)).

    Но к этому моменту узнал, что есть API YouTube который позволяет всю необходимую информацию в структурированном виде
3. Разобравшись с API YouTube, я понял, что это самое элегантное решение, и все прочие способы (с помощью `requests` и `Selenium`) &mdash; страдают избыточной логикой и перегруженностью


### 1.3. Проблемы с API YouTube

При работе с API YouTube есть несколько моментов:
1. Каждый день на 1 аккаунт выделяется 10 000 лимитов к API YouTube
2.  Для получения списка роликов, загруженных на канал можно использовать разные `endpoints` &mdash; они имеют разную стоимость лимитов ([YouTube Data API (v3) - Quota Calculator](https://developers.google.com/youtube/v3/determine_quota_cost)):
    * запрос к `search` &mdash; стоит 100 лимитов
    * запросы к `channel` и `PlaylistItems` &mdash; стоят 1 лимит

    Соответственно для того, чтобы уложиться в 10 000 лимитов я выбрал работу через endpoint `channel`
3. Для того, чтобы работать с API YouTube нужно указывать `ChannelID` &mdash; он имеет следующий вид: `UUpRmvjdu3ixew5ahydZ67uA`.

    `ChannelID` отличается от списка загруженных видео только одной буквой &mdash; вместо `UU...` используется `UC...`, например так: `UCpRmvjdu3ixew5ahydZ67uA`

4. Один и тот же YouTube канал может иметь несколько идентификаторов:
    * `forUsername` типа `topgtru`, и
    * `id` типа `UUpRmvjdu3ixew5ahydZ67uA` &mdash; *для работы с API YouTube нужно использовать именно этот идентификатор

    Теоретически `id` *для работы с API YouTube можно получить через endpoint `channels`, но он работает странно, и не отдает информацию для некоторых каналов*. Например для канала `topgtru` он нормально отдает контент, а для `SeniorSoftwareVlogger` не возвращает ничего. Примеры обоих запросов:
    ```text
    # Возвращает нормальный ответ
    https://www.googleapis.com/youtube/v3/channels?part=snippet,id&forUsername=topgtru&key={key}

    # Ничего не возвращает
    https://www.googleapis.com/youtube/v3/channels?part=snippet,id&forUsername=SeniorSoftwareVlogger&key={key}
    ```

    Собственно это баг на стороне YouTube, и я не один, кто столкнулся с этим. Такая же проблема описана на Stackoverflow &mdash; [YouTube API v3 Channels: list method doesn't work for some channels names](https://stackoverflow.com/questions/35051882/youtube-api-v3-channels-list-method-doesnt-work-for-some-channels-names)


### 1.4. Итоговое решение
1. В итоге, для работы с API YouTube нужно получать `id`, который с помощью API получить не всегда возможно.

    Я конечно сделал загрузчик на Selenium, который позволяет вытягивать `channelId` со страницы (реализован в коммите [9ffad9c](https://github.com/n8creator/youtube/commit/9ffad9cf14e11e58f44825fa7ffd3b3888493dd6#diff-24e6654bfd1ab85bebb1f721a4be46e6fdb9ea8974d14442d3aaecd1f971fcbb)) &mdash; но там опять возникают неочевидные проблемы постоянно меняющейся верстки на странице YouTube. Т.о это технически не стабильное решение.

    Решение на Selenium описано на Stackoverflow &mdash; [Selenium python, click agree to youtube cookie](https://stackoverflow.com/questions/66902404/selenium-python-click-agree-to-youtube-cookie)

2. В итоге, я пришел к тому, чтобы вообще "забить" на проблему программного способа получения `channelID` &mdash; если уж и нужно получить информацию о списке видео с канала, можно просто посмотреть содержимое страницы и скопировать параметр `channelID` из метатега `itemprop`:
    ```
    <meta itemprop="channelId" content="UCxn-8f1slSjWi_ABio5H8YA">
    ```

3. **Итоговое решение**:

    В итоге запрос к API YouTube имеет следующий синтаксис:
    ```text
    https://www.googleapis.com/youtube/v3/playlistItems?part=snippet,contentDetails&maxResults=50&playlistId={playlistId}&key={key}
    ```

    где,

    * `playlistId` &mdash; получаем руками из свойства `<meta itemprop="channelId"` значение `channelId` и меняем `UU...` на `UC...`
    * `key` &mdash; получаем на странице [Google Cloud Platform](https://console.cloud.google.com/ ) > APIs & Services > Credentials


4. **Для отладки:**
    Информация об общем количестве видео на канале и количестве в текущем ответе отдается в параметре `pageInfo`:
    ```json
    ...  ],
    "pageInfo": {
        "totalResults": 1147,
        "resultsPerPage": 50
    }
    }
    ```

    Для перебора `totalResults` используется `nextPageToken` и `prevPageToken`, который возвращается в ответе:
    ```json
    ...
    "etag": "kna7TTBcYL64TTAkIF9pPUmSXGk",
    "nextPageToken": "CDIQAA",
    "items": [
        ...
    ```

    Для перехода по `nextPageToken` и `prevPageToken` используется параметр `pageToken` например:
    ```
    https://www.googleapis.com/youtube/v3/playlistItems?part=snippet,contentDetails&maxResults=50&playlistId={playlistId}&key={key}&pageToken={token}
    ```
