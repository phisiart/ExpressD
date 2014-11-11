// let's put all the data in here.
var data = {
    "timePicked": false,

    "pickedTime": "17:00:00",

    "tid": 1,

    "types": [
        {
            "tid":        1,
            "name":       "Dinner"
        },
        {
            "tid":        2,
            "name":       "Breakfast"
        }
    ],

    "items": [
        {
            "iid":        1,
            "tid":        1,
            "name":       "Chicken Pommes Frites",
            "price":      1300,
            "timeToCook": "00:05:00",
            "startTime":  "17:00:00",
            "endTime":    "23:00:00"
        },
        {
            "iid":        2,
            "tid":        1,
            "name":       "Spaghetti And Meatballs",
            "price":      1200,
            "timeToCook": "00:05:00",
            "startTime":  "17:00:00",
            "endTime":    "23:00:00"
        }
    ],

    "orders": [
        { iid: 1, number: 2 },
        { iid: 2, number: 3 }
    ]
};

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
    } else {
        // user picked time.
        var time = document.getElementById("textPickTime").value;
        var A = time.split(/\D+/);
        A = [+A[0], +A[1], +A[2]];
        if (A[0] >= 0 && A[0] <= 23 && A[1] >= 0 && A[1] <= 23 && A[2] >= 0 && A[2] <= 23) {
            // valid time
            data.pickedTime = addZero(A[0]) + ":" + addZero(A[1]) + ":" + addZero(A[2]);
            document.getElementById("divWhenWantFood").innerHTML = data.pickedTime;
            data.timePicked = true;
            updatePage();
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
        if (!data.timePicked) {
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

updatePage();
