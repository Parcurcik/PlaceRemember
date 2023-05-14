# Тестовое задание для компании "Очень интересно"

Клонируем репозиторий

## Подключение api-ключей

Для начала необходимо создать файл .env в корне проекта, прописать там все api-ключи доступа в таком формате:

    SOCIAL_AUTH_GOOGLE_OAUTH2_KEY=
    SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET=
    SOCIAL_AUTH_VK_OAUTH2_KEY=
    SOCIAL_AUTH_VK_OAUTH2_SECRET=

## Локальный запуск через виртуальное окружение

Необходимо в терминале прописать команды:

    python -m venv venv

    pip install -r requirements.txt
    
    python manage.py makemigrations
    python manage.py migrate

## Запуск через Докер

В файле settings.py изменить значение на:

    ALLOWED_HOSTS = ['0.0.0.0']

В корневой папке проекта прописать:

    docker compose up

### Отчет по проделанной работе:

- Запуск тестов при новых коммитах был реализован с использованием github actions.
- Запуск через докер присутствует.
- Правила для линтеров, а также их запуск реализованы.
- [Приложение выгружено на облачный сервис](http://placerememberbezborodov.pythonanywhere.com/)
- Текущее покрытие тестами проекта можно посмотреть ниже:

<details>
<summary>Посмотреть отчет о покрытии тестами</summary>
<p>
<!DOCTYPE html>
<html>
<head>
    <meta http-equiv="Content-Type" content="text/html; charset=utf-8">
    <title>Coverage report</title>
    <link rel="icon" sizes="32x32" href="favicon_32.png">
    <link rel="stylesheet" href="style.css" type="text/css">
    <script type="text/javascript" src="coverage_html.js" defer></script>
</head>
<body class="indexfile">
<header>
    <div class="content">
        <h1>Coverage report:
            <span class="pc_cov">81%</span>
        </h1>
        <aside id="help_panel_wrapper">
            <input id="help_panel_state" type="checkbox">
            <label for="help_panel_state">
                <img id="keyboard_icon" src="keybd_closed.png" alt="Show/hide keyboard shortcuts" />
            </label>
            <div id="help_panel">
                <p class="legend">Shortcuts on this page</p>
                <div class="keyhelp">
                    <p>
                        <kbd>n</kbd>
                        <kbd>s</kbd>
                        <kbd>m</kbd>
                        <kbd>x</kbd>
                        <kbd>c</kbd>
                        &nbsp; change column sorting
                    </p>
                    <p>
                        <kbd>[</kbd>
                        <kbd>]</kbd>
                        &nbsp; prev/next file
                    </p>
                    <p>
                        <kbd>?</kbd> &nbsp; show/hide this help
                    </p>
                </div>
            </div>
        </aside>
        <form id="filter_container">
            <input id="filter" type="text" value="" placeholder="filter..." />
        </form>
        <p class="text">
            <a class="nav" href="https://coverage.readthedocs.io">coverage.py v6.5.0</a>,
            created at 2023-05-14 20:54 +0500
        </p>
    </div>
</header>
<main id="index">
    <table class="index" data-sortable>
        <thead>
            <tr class="tablehead" title="Click to sort">
                <th class="name left" aria-sort="none" data-shortcut="n">Module</th>
                <th aria-sort="none" data-default-sort-order="descending" data-shortcut="s">statements</th>
                <th aria-sort="none" data-default-sort-order="descending" data-shortcut="m">missing</th>
                <th aria-sort="none" data-default-sort-order="descending" data-shortcut="x">excluded</th>
                <th class="right" aria-sort="none" data-shortcut="c">coverage</th>
            </tr>
        </thead>
        <tbody>
            <tr class="file">
                <td class="name left"><a href="d_3235b88ed21677c9_get_profile_py.html">authorization\get_profile.py</a></td>
                <td>31</td>
                <td>19</td>
                <td>0</td>
                <td class="right" data-ratio="12 31">39%</td>
            </tr>
            <tr class="file">
                <td class="name left"><a href="d_02cf018b501c0399___init___py.html">impressions\__init__.py</a></td>
                <td>0</td>
                <td>0</td>
                <td>0</td>
                <td class="right" data-ratio="0 0">100%</td>
            </tr>
            <tr class="file">
                <td class="name left"><a href="d_02cf018b501c0399_asgi_py.html">impressions\asgi.py</a></td>
                <td>4</td>
                <td>4</td>
                <td>0</td>
                <td class="right" data-ratio="0 4">0%</td>
            </tr>
            <tr class="file">
                <td class="name left"><a href="d_02cf018b501c0399_settings_py.html">impressions\settings.py</a></td>
                <td>29</td>
                <td>0</td>
                <td>0</td>
                <td class="right" data-ratio="29 29">100%</td>
            </tr>
            <tr class="file">
                <td class="name left"><a href="d_02cf018b501c0399_urls_py.html">impressions\urls.py</a></td>
                <td>3</td>
                <td>0</td>
                <td>0</td>
                <td class="right" data-ratio="3 3">100%</td>
            </tr>
            <tr class="file">
                <td class="name left"><a href="d_02cf018b501c0399_wsgi_py.html">impressions\wsgi.py</a></td>
                <td>4</td>
                <td>4</td>
                <td>0</td>
                <td class="right" data-ratio="0 4">0%</td>
            </tr>
            <tr class="file">
                <td class="name left"><a href="manage_py.html">manage.py</a></td>
                <td>12</td>
                <td>2</td>
                <td>0</td>
                <td class="right" data-ratio="10 12">83%</td>
            </tr>
            <tr class="file">
                <td class="name left"><a href="d_3314341192b385fa___init___py.html">memories\__init__.py</a></td>
                <td>0</td>
                <td>0</td>
                <td>0</td>
                <td class="right" data-ratio="0 0">100%</td>
            </tr>
            <tr class="file">
                <td class="name left"><a href="d_3314341192b385fa_admin_py.html">memories\admin.py</a></td>
                <td>3</td>
                <td>0</td>
                <td>0</td>
                <td class="right" data-ratio="3 3">100%</td>
            </tr>
            <tr class="file">
                <td class="name left"><a href="d_3314341192b385fa_apps_py.html">memories\apps.py</a></td>
                <td>4</td>
                <td>0</td>
                <td>0</td>
                <td class="right" data-ratio="4 4">100%</td>
            </tr>
            <tr class="file">
                <td class="name left"><a href="d_3314341192b385fa_forms_py.html">memories\forms.py</a></td>
                <td>8</td>
                <td>0</td>
                <td>0</td>
                <td class="right" data-ratio="8 8">100%</td>
            </tr>
            <tr class="file">
                <td class="name left"><a href="d_9720caafdf80a008_0001_initial_py.html">memories\migrations\0001_initial.py</a></td>
                <td>7</td>
                <td>0</td>
                <td>0</td>
                <td class="right" data-ratio="7 7">100%</td>
            </tr>
            <tr class="file">
                <td class="name left"><a href="d_9720caafdf80a008_0002_rename_location_name_memory_memory_name_py.html">memories\migrations\0002_rename_location_name_memory_memory_name.py</a></td>
                <td>4</td>
                <td>0</td>
                <td>0</td>
                <td class="right" data-ratio="4 4">100%</td>
            </tr>
            <tr class="file">
                <td class="name left"><a href="d_9720caafdf80a008___init___py.html">memories\migrations\__init__.py</a></td>
                <td>0</td>
                <td>0</td>
                <td>0</td>
                <td class="right" data-ratio="0 0">100%</td>
            </tr>
            <tr class="file">
                <td class="name left"><a href="d_3314341192b385fa_models_py.html">memories\models.py</a></td>
                <td>8</td>
                <td>0</td>
                <td>0</td>
                <td class="right" data-ratio="8 8">100%</td>
            </tr>
            <tr class="file">
                <td class="name left"><a href="d_3314341192b385fa_tests_py.html">memories\tests.py</a></td>
                <td>36</td>
                <td>0</td>
                <td>0</td>
                <td class="right" data-ratio="36 36">100%</td>
            </tr>
            <tr class="file">
                <td class="name left"><a href="d_3314341192b385fa_urls_py.html">memories\urls.py</a></td>
                <td>3</td>
                <td>0</td>
                <td>0</td>
                <td class="right" data-ratio="3 3">100%</td>
            </tr>
            <tr class="file">
                <td class="name left"><a href="d_3314341192b385fa_views_py.html">memories\views.py</a></td>
                <td>51</td>
                <td>11</td>
                <td>0</td>
                <td class="right" data-ratio="40 51">78%</td>
            </tr>
        </tbody>
        <tfoot>
            <tr class="total">
                <td class="name left">Total</td>
                <td>207</td>
                <td>40</td>
                <td>0</td>
                <td class="right" data-ratio="167 207">81%</td>
            </tr>
        </tfoot>
    </table>
    <p id="no_rows">
        No items found using the specified filter.
    </p>
</main>
<footer>
    <div class="content">
        <p>
            <a class="nav" href="https://coverage.readthedocs.io">coverage.py v6.5.0</a>,
            created at 2023-05-14 20:54 +0500
        </p>
    </div>
    <aside class="hidden">
        <a id="prevFileLink" class="nav" href="d_3314341192b385fa_views_py.html"/>
        <a id="nextFileLink" class="nav" href="d_3235b88ed21677c9_get_profile_py.html"/>
        <button type="button" class="button_prev_file" data-shortcut="["/>
        <button type="button" class="button_next_file" data-shortcut="]"/>
        <button type="button" class="button_show_hide_help" data-shortcut="?"/>
    </aside>
</footer>
</body>
</html>

</p>
</details>
