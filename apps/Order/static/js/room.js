    var chatSocket = new WebSocket(
       'ws://' + window.location.host +
       '/ws/chat/' + roomName + '/');

    chatSocket.onmessage = function(e) {
        var data = JSON.parse(e.data);
        let info = data['message'];
        var message = info['orders'];
        var time = info['time'];
        var ref_code = info['ref_code'];

        var order = document.createElement("div");
        order.setAttribute("id", ref_code);
        let ref = document.createElement("p");
        ref.setAttribute("class", "ref-code");
        ref_code = document.createTextNode('ref_code : ' + ref_code);
        ref.appendChild(ref_code);
        let timeOrder = document.createElement("p");
        timeOrder.setAttribute("class", "time-order");
        time = document.createTextNode('time : ' + time + "  ");
        timeOrder.appendChild(time);
        order.appendChild(timeOrder);
        order.appendChild(ref);

        var list = document.createElement("ul");
        Object.keys(message).map( dish => {
            let order = document.createElement("li");
            let text = document.createTextNode(message[dish] + " : " + dish);
            order.appendChild(text);
            list.appendChild(order);
        });

        order.appendChild(list);

        let orderList = document.querySelector('#order-log');

        orderList.insertBefore(order, orderList.firstChild);
    };

    chatSocket.onclose = function(e) {
        console.error('Chat socket closed unexpectedly');
    };

    // document.querySelector('#chat-message-input').focus();
    // document.querySelector('#chat-message-input').onkeyup = function(e) {
    //     if (e.keyCode === 13) {  // enter, return
    //         document.querySelector('#chat-message-submit').click();
    //     }
    // };
    //
    // document.querySelector('#chat-message-submit').onclick = function(e) {
    //     var messageInputDom = document.querySelector('#chat-message-input');
    //     var message = messageInputDom.value;
    //     chatSocket.send(JSON.stringify({
    //         'message': message
    //     }));
    //
    //     messageInputDom.value = '';
    // };