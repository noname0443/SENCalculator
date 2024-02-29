function sleep(ms) {
    var start = new Date().getTime(), expire = start + ms;
    while (new Date().getTime() < expire) { }
    return;
}

function SendString(data, host, evaluateFunction) {
    var connection = new WebSocket(`ws://${host}:444`);

    connection.onopen = function () {
      connection.send(data);
    };

    connection.onmessage = evaluateFunction;
}