# HTTP-Middleware

Клиент может иметь мидлварь, по умолчанию для клиента `AiohttpClient` это `JustLogHTTPMiddleware`

## Работа с мидлварем для http-клиента

### pre(method, url, data)

Выполняется до выполнения запроса. По параметрам - смотреть документацию http-client

### post(response)

Выполняется после закрытия сессии, получает первым аргументом результат выполнения функции-создателя реквеста

## Создание кастомного мидлваря для http-клиента

Необходимо унаследоваться от `ABCHTTPMiddleware` и имплементировать две асинхронные функции `pre` и `post`, упомянутые ранее  

Если `pre` вернет `HTTPMiddlewareResponse(False)` то выполенение будет остановлено и вернется `None`
