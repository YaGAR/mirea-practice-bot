# Правила работы в команде

## Git-стратегия

Мы используем [GitFlow / GitHub Flow / Trunk-Based].

### Ветвление
- `main` — стабильная версия
- `develop` — интеграционная ветка (если используем GitFlow)
- `feature/[название]` — новые функции
- `bugfix/[название]` — исправление багов

### Коммиты
Используем [Conventional Commits](https://www.conventionalcommits.org/):
- `feat:` новая функция
- `fix:` исправление бага
- `docs:` изменения в документации
- `style:` форматирование кода
- `refactor:` рефакторинг
- `test:` добавление тестов
- `chore:` рутинные задачи

Пример: `feat: add user authentication endpoint`