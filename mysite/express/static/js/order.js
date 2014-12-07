
// checkASAP
// ---------
// User want his food asap.
function checkASAP() {
    document.getElementById("textPickTime").disabled = true;
}

// checkPickTime
// -------------
// User want to set his own pickup time.
function checkPickTime() {
    document.getElementById("textPickTime").disabled = false;
}

// pickTimeOkay
// ------------
// User has picked time.
function pickTimeOkay() {
    document.getElementById("spanOkay").innerHTML = "";
    var addZero = function(i) {
        if (i < 10) {
            i = "0" + i;
        }
        return i;
    };
    if (document.getElementById("textPickTime").disabled) {
        // asap
        var date = new Date();
        data.pickedTime = addZero(date.getHours()) + ":" + addZero(date.getMinutes()) + ":" + addZero(date.getSeconds());
        document.getElementById("divWhenWantFood").innerHTML = data.pickedTime;
        data.timePicked = true;
        updatePage();
        document.getElementById("but_send_order").disabled = false;
    } else {
        // user picked time.
        var time = document.getElementById("textPickTime").value;
        var A = time.split(/\D+/);
        A = [+A[0], +A[1], +A[2]];
        var date = new Date();
        var currentSecond = HMStoSec(addZero(date.getHours()) + ":" + addZero(date.getMinutes()) + ":" + addZero(date.getSeconds()));

        if (A[0] >= 0 && A[0] <= 23 && A[1] >= 0 && A[1] <= 59 && A[2] >= 0 && A[2] <= 59 && currentSecond <= HMStoSec(time)) {
            // valid time
            data.pickedTime = addZero(A[0]) + ":" + addZero(A[1]) + ":" + addZero(A[2]);
            document.getElementById("divWhenWantFood").innerHTML = data.pickedTime;
            data.timePicked = true;
            updatePage();
            document.getElementById("but_send_order").disabled = false;
        } else {
            // invalid time
            document.getElementById("spanOkay").innerHTML = "It turns out the time you entered is not valid. Please try again.";
        }
    }
}

// genTable
// --------
// Generate the table of items of a certain type
function genTable() {
    var str = "";
    data.items.forEach(function(item) {
        if (item.tid != data.tid) {
            return;
        }
        str += "<tr>";
        str += "<td>" + item.name + "</td>";
        str += "<td>" + item.timeToCook + "</td>";
        str += "<td>" + genTimeBar(item.startTime, item.endTime) + "</td>";
        str += "<td>$" + (item.price / 100.0).toFixed(2) + "</td>";

        // calculate the number ordered.
        var number = 0;
        data.orders.forEach(function(order) {
            if (item.iid == order.iid) {
                number = order.number;
            }
        });
        if (number == 0) {
            number = "";
        }

        str += "<td>";
        str +=   "<form class='form-inline' role='form'>";
        str +=    "<input id='input" + item.iid + "' type='number' min='0'";
        if (!data.timePicked || !timeAvailable(document.getElementById("divWhenWantFood").innerHTML, item.startTime, item.endTime)) {
            str += " disabled ";
        }
        str +=           "class='form-control' placeholder='0' style='max-width: 60px;'";
        str +=           "onchange='changeOrder(" + item.iid + ")' value='" + number + "'>";
        str +=   "</form>";
        str += "</td>";
        str += "</tr>";
    });
    return str;
}

// updateTable
// -----------
// Update the table of items in this page.
function updateTable() {
    document.getElementById("itemTable").innerHTML = genTable();
}


// genSidebar
// ----------
// Generate the left sidebar.
function genSidebar() {
    var str = "";
    str += "<ul class='nav nav-sidebar'>";
    data.types.forEach(function(type) {
        str += "<li";
        if (type.tid == data.tid) {
            str += " class='active'>";
        } else {
            str += ">";
        }
        str += "<a href='javascript:changeType(" + type.tid + ")'>";
        str += type.name;
        str += "</a></li>";
    });
    str += "</ul>";
    return str;
}

// updateSidebar
// -------------
// Update the left sidebar.
function updateSidebar() {
    document.getElementById("typeSidebar").innerHTML = genSidebar();
}

// genOrderTable
// -------------
// Generate the table of current order based on the data.
function genOrderTable() {
    var str = "";
    var totalPrice = 0;
    data.orders.forEach(function(order) { // for each order in orders
        if (order.number == 0) {
            return;
        }
        data.items.forEach(function(item) { // 
            if (order.iid == item.iid) {
                str += "<tr>";
                str += "<td>" + item.name + "</td>";
                str += "<td>" + order.number + "</td>";
                str += "<td>$" + (item.price * order.number / 100.0).toFixed(2) + "</td>";
                str += "</tr>";
                totalPrice += item.price * order.number;
            }
        });
    });

    str += "<tr>";
    str += "<td style='font-weight: bold;'>Total</td>";
    str += "<td></td>";
    str += "<td style='font-weight: bold;'>$" + (totalPrice / 100.0).toFixed(2) + "</td>";
    str += "</tr>";
    return str;
}

// updateOrderTsble
// ----------------
// Update the table of current order.
function updateOrderTable() {
    document.getElementById("orderTable").innerHTML = genOrderTable();
}

function updatePage() {
    updateSidebar();
    updateTable();
    updateOrderTable();
}

// changeOrder
// -----------
// Triggered by onchange of input
function changeOrder(iid) {
    var number = document.getElementById("input" + iid).value;
    var found = false;
    data.orders.forEach(function(order) {
        if (order.iid == iid) {
            order.number = number;
            found = true;
        }
    });

    if (!found) {
        data.orders.push({ "iid": iid, "number": number });
    }

    updateOrderTable();
}

function changeType(tid) {
    data.tid = tid;
    updatePage();
}

function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie != '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) == (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

function submitOrder() {
    var xmlhttp;
    if (window.XMLHttpRequest) {
        xmlhttp = new XMLHttpRequest();
    } else {
        xmlhttp = new ActiveXObject("Microsoft.XMLHTTP");
    }
    xmlhttp.onreadystatechange = function() {
        if (4 == xmlhttp.readyState && 200 == xmlhttp.status) {
            if (xmlhttp.responseText == "send_order_finished") {
                document.getElementById("modal_title").innerHTML = "Order sent";
                document.getElementById("modal_text").innerHTML = "You will receive an email when the restaurant confirms your order.";

            } else {
                document.getElementById("modal_title").innerHTML = "Sending failed";
                document.getElementById("modal_text").innerHTML = "Sending failed";
            }
            // console.log(xmlhttp.responseText);
            // document.getElementById("but_show_modal").click();
            $('#myModal').modal('show');
        }
    };
    xmlhttp.open("POST", "send_order", true);
    var csrftoken = getCookie('csrftoken');
    xmlhttp.setRequestHeader("X-CSRFToken", csrftoken);
    xmlhttp.setRequestHeader("Content-Type", "application/json;charset=UTF-8");

    var pickUpTime = moment();
    console.log(pickUpTime);
    var max_seconds = 0;

    // for each ordered item.
    data.orders.forEach(function(order) {

        // get number of seconds to cook
        seconds = 0;
        data.items.forEach(function(item) {
            if (item.iid == order.iid) {
                seconds = HMStoSec(item.timeToCook);
                return;
            }
        });

        if (seconds > max_seconds) {
            max_seconds = seconds;
        }
    });

    pickUpTime.add(max_seconds, 's');
    var writtenTime = moment(document.getElementById("divWhenWantFood").innerHTML, "HH:MM:SS");
    console.log(pickUpTime);
    var req_body = {
        'cardid' :      document.getElementById('inputCard').value,
        'name':         document.getElementById('inputName').value,
        'email':        document.getElementById('inputEmail').value,
        'phone':        document.getElementById('inputPhone').value,
        'pickUpTime':   pickUpTime.toJSON(),
        'did':          data.did,
        'orders':       data.orders,
    };

    xmlhttp.send(JSON.stringify(req_body));
}

updatePage();
