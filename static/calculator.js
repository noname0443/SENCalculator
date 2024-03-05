function SendString(data, host, evaluateFunction) {
    var connection = new WebSocket(`ws://${host}:31234`);

    connection.onopen = function () {
      connection.send(data);
    };

    connection.onmessage = evaluateFunction;
}