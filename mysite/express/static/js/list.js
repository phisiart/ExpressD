String.prototype.format = function() {
    var s = this,
        i = arguments.length;

    while (i--) {
        s = s.replace(new RegExp('\\{' + i + '\\}', 'gm'), arguments[i]);
    }
    return s;
};

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

function changeStatus(oid, stat) {
    var xmlhttp;
    if (window.XMLHttpRequest) {
        xmlhttp = new XMLHttpRequest();
    } else {
        xmlhttp = new ActiveXObject("Microsoft.XMLHTTP");
    }
    xmlhttp.onreadystatechange = function() {
        if (4 == xmlhttp.readyState && 200 == xmlhttp.status) {
            document.location.reload();
        }
    };
    xmlhttp.open("POST", "change_status", true);
    var csrftoken = getCookie('csrftoken');
    xmlhttp.setRequestHeader("X-CSRFToken", csrftoken);
    xmlhttp.setRequestHeader("Content-Type", "application/json;charset=UTF-8");
    var req_body = {
        "oid": oid,
        "stat": stat,
    };
    xmlhttp.send(JSON.stringify(req_body));
}

function updateTable() {
    var str = "";
    data["orders"].reverse().forEach(function(order) {
        var status = "";
        switch (order["stat"]) {
            case "PE": status = "Pending"; break;
            case "AC": status = "Accepted"; break;
            case "RE": status = "Ready"; break;
            case "PI": status = "Picked"; break;
        }
        str += '<div class="panel panel-default">';
        str += '    <div class="panel-heading" style="font-weight: bold;">';
        str += "        DukeCard: {0} | {1} | {2}".format(order["cardid"], order["scheduledPickUpTime"], status);
        str += '    </div>';
        str += '    <table class="table">';
        str += '        <thead>';
        str += '            <tr>';
        str += '                <th>Item</th>';
        str += '                <th>Number</th>';
        str += '            </tr>';
        str += '        </thead>';
        str += '        <tbody>';
        order["items"].forEach(function(item) {
            str += '        <tr>';
            str += '            <td>{0}</td>'.format(item["name"]);
            str += '            <td>{0}</td>'.format(item["number"]);
            str += '        </tr>';
        });
        str += '        </tbody>';
        str += '    </table>';
        str += '    <div class="panel-footer clearfix" style="padding-top: 5px; padding-bottom: 5px;">';
        str += '        <div class="pull-right">';
        str += '            <div class="dropdown">';
        str += '                <button class="btn btn-default dropdown-toggle" type="button" id="dropdownMenu1" data-toggle="dropdown" aria-expanded="true">';
        str +=                      status;
        str += '                    <span class="caret" />';
        str += '                </button>';
        str += '                <ul class="dropdown-menu" role="menu" aria-labelledby="dropdownMenu1">';
        str += '                    <li role="presentation"><a role="menuitem" tabindex="-1" href="javascript:changeStatus({0}, \'PE\')">Pending</a></li>'.format(order["oid"]);
        str += '                    <li role="presentation"><a role="menuitem" tabindex="-1" href="javascript:changeStatus({0}, \'AC\')">Accepted</a></li>'.format(order["oid"]);
        str += '                    <li role="presentation"><a role="menuitem" tabindex="-1" href="javascript:changeStatus({0}, \'RE\')">Ready</a></li>'.format(order["oid"]);
        str += '                    <li role="presentation"><a role="menuitem" tabindex="-1" href="javascript:changeStatus({0}, \'PI\')">Picked</a></li>'.format(order["oid"]);
        str += '                </ul>';
        str += '            </div>';
        str += '        </div>';
        str += '    </div>';
        str += '</div>';
    });
    document.getElementById("orders").innerHTML = str;
}

updateTable();
