require('dotenv').config();
const express = require('express');
const morgan = require('morgan');

const port = process.env.PORT || 1245;
const app = express();

// Логирование запросов
app.use(morgan('dev'));

app.get('/', (req, res) => {
  res.send('Hello Holberton School!');
});

// Обработка ошибок 404
app.use((req, res, next) => {
  res.status(404).send('Not Found');
});

// Общая обработка ошибок
app.use((err, req, res, next) => {
  console.error(err.stack);
  res.status(500).send('Something broke!');
});

// Запускаем сервер
app.listen(port, () => {
  console.log(`Server is running on http://localhost:${port}`);
});

// Экспортируем приложение
module.exports = app;
