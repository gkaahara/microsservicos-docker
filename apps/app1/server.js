const express = require(`express`);
const app = express();
const port = 3001;

app.get('/', (req, res) => {
    res.json({
        service: 'Node.js Microservice 1',
        message: 'API Node funcionando!',
        timestamp: new Date().toISOString()
    });
});

app.listen(port, () => {
    console.log('Node.js App1 rodando na porta ${port}');
});
