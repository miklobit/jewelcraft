# ##### BEGIN GPL LICENSE BLOCK #####
#
#  mod_update automatic add-on updates.
#  Copyright (C) 2019  Mikhail Rachinskiy
#
#  This program is free software: you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program.  If not, see <https://www.gnu.org/licenses/>.
#
# ##### END GPL LICENSE BLOCK #####


_ru = {
    "*": {
        # Interface
        "Update completed": "Обновление завершено",
        "Close Blender to complete the installation": "Для завершения установки закройте Blender",
        "Installing...": "Установка...",
        "Checking...": "Проверка...",
        "Update {} is available": "Доступно обновление {}",
        "Last checked never": "Последняя проверка никогда",
        "Last checked today": "Последняя проверка сегодня",
        "Last checked yesterday": "Последняя проверка вчера",
        "Last checked {} days ago": "Последняя проверка {} дней назад",
        "Automatically check for updates": "Автоматически проверять наличие обновлений",
        "Auto-check Interval": "Интервал автопроверки",
        "Once a day": "Раз в день",
        "Once a week": "Раз в неделю",
        "Once a month": "Раз в месяц",
        "Update to pre-release": "Обновление до пре-релиза",
        # Tooltips
        "Check for new add-on release": "Проверить наличие новой версии дополнения",
        "Download and install new version of the add-on": "Загрузить и установить новую версию дополнения",
        "Open release notes in web browser": "Открыть страницу изменений в веб-браузере",
        "Automatically check for updates with specified interval":
            "Автоматически проверять наличие обновлений с указанным интервалом",
        "Auto-check interval": "Интервал автопроверки",
        "Update add-on to pre-release version if available":
            "Обновить до пре-релизной версии (если доступно)",
    },
    "Operator": {
        "Check for Updates": "Проверить наличие обновлений",
        "Install Update": "Установить обновление",
        "See What's New": "Смотреть изменения",
    },
}


# Translation dictionary
# -----------------------------


def translation_dict(x):
    d = {}

    for ctxt, msgs in x.items():

        for msg_key, msg_translation in msgs.items():
            d[(ctxt, msg_key)] = msg_translation

    return d


DICTIONARY = {"ru_RU": translation_dict(_ru)}

del _ru