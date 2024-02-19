import logging
from typing import Any, Awaitable, Callable, Dict

from aiogram import BaseMiddleware
from aiogram.types import TelegramObject

logger = logging.getLogger(__name__)


class FirstOuterMiddleware(BaseMiddleware):

    async def __call__(
        self,
        handler: Callable[[TelegramObject, Dict[str, Any]], Awaitable[Any]],
        event: TelegramObject,
        data: Dict[str, Any]
    ) -> Any:

        logger.debug(
            'Вошли в миддлварь %s, тип события %s',
            __class__.__name__,
            event.__class__.__name__
        )

        result = await handler(event, data)

        logger.debug('Выходим из миддлвари  %s', __class__.__name__)

        return result


class SecondOuterMiddleware(BaseMiddleware):

    async def __call__(
        self,
        handler: Callable[[TelegramObject, Dict[str, Any]], Awaitable[Any]],
        event: TelegramObject,
        data: Dict[str, Any]
    ) -> Any:

        logger.debug(
            'Вошли в миддлварь %s, тип события %s',
            __class__.__name__,
            event.__class__.__name__
        )

        result = await handler(event, data)

        logger.debug('Выходим из миддлвари  %s', __class__.__name__)

        return result


class ThirdOuterMiddleware(BaseMiddleware):

    async def __call__(
        self,
        handler: Callable[[TelegramObject, Dict[str, Any]], Awaitable[Any]],
        event: TelegramObject,
        data: Dict[str, Any]
    ) -> Any:

        logger.debug(
            'Вошли в миддлварь %s, тип события %s',
            __class__.__name__,
            event.__class__.__name__
        )

        result = await handler(event, data)

        logger.debug('Выходим из миддлвари  %s', __class__.__name__)

        return result


# # Пример теневого бана
# from typing import Any, Awaitable, Callable, Dict

# from aiogram import BaseMiddleware
# from aiogram.types import TelegramObject, User

# CACHE = {
#     'banned': [254443334, 214454432, 112221212],
# }


# class ShadowBanMiddleware(BaseMiddleware):

#     async def __call__(
#         self,
#         handler: Callable[[TelegramObject, Dict[str, Any]], Awaitable[Any]],
#         event: TelegramObject,
#         data: Dict[str, Any]
#     ) -> Any:
        
#         user: User = data.get('event_from_user')
#         if user is not None:
#             if user.id in CACHE.get('banned'):
#                 return

#         return await handler(event, data)

# # Подключение миддлвари происходит уже знакомым нам образом:
# dp.update.middleware(ShadowBanMiddleware())


# # Пример тротлинга
# from typing import Any, Awaitable, Callable, Dict

# from aiogram import BaseMiddleware
# from aiogram.types import TelegramObject, User
# from cachetools import TTLCache

# CACHE = TTLCache(maxsize=10_000, ttl=5)  # Максимальный размер кэша - 10000 ключей, а время жизни ключа - 5 секунд

# class ThrottlingMiddleware(BaseMiddleware):

#     async def __call__(
#             self,
#             handler: Callable[[TelegramObject, Dict[str, Any]], Awaitable[Any]],
#             event: TelegramObject,
#             data: Dict[str, Any],
#     ) -> Any:
#         user: User = data.get('event_from_user')

#         if user.id in CACHE:
#             return

#         CACHE[user.id] = True

#         return await handler(event, data)

# # Зарегистрировать миддлварь также нужно на диспетчер
# dp.update.middleware(ThrottlingMiddleware())
