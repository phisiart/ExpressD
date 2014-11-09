function HMStoSec(T) { // h:m:s
    var A = T.split(/\D+/);
    return (A[0] * 60 + +A[1]) * 60 + +A[2];
}

function genTimeBar(startTime, endTime) {
    var s = HMStoSec(startTime);
    var e = HMStoSec(endTime);
    var str = "<div style=\"position:relative; min-width:120px;\">";
    str += "<div class=\"progress\" style=\"margin-bottom: 0px; position:relative;\">";
    if (e >= s) {
        var p1 = s / 86400.0 * 100;
        var p2 = (e - s) / 86400.0 * 100;
        var p3 = (86400 - e) / 86400.0 * 100;
        str += "<div class=\"progress-bar progress-bar-danger progress-bar-striped\" style=\"width: " + p1 + "%\"></div>";
        str += "<div class=\"progress-bar progress-bar-success\" style=\"width: " + p2 + "%\"></div>";
        str += "<div class=\"progress-bar progress-bar-danger progress-bar-striped\" style=\"width: " + p3 + "%\"></div>";
    } else {
        var p1 = e / 86400.0 * 100;
        var p2 = (s - e) / 86400.0 * 100;
        var p3 = (86400 - s) / 86400.0 * 100;
        str += "<div class=\"progress-bar progress-bar-success\" style=\"width: " + p1 + "%\"></div>";
        str += "<div class=\"progress-bar progress-bar-danger progress-bar-striped\" style=\"width: " + p2 + "%\"></div>";
        str += "<div class=\"progress-bar progress-bar-danger progress-bar-striped\" style=\"width: " + p3 + "%\"></div>";
    }
    str += "<div style=\"position:absolute; top:0; left:0; width:100%; color: #ffffff; text-align: center; text-shadow: 0px 1px 3px rgba(0,0,0,.5);\">"

    startTime = startTime.split(/\D+/);
    startTime = startTime[0] + ":" + startTime[1];
    endTime = endTime.split(/\D+/);
    endTime = endTime[0] + ":" + endTime[1];
    if (e >= s) {
        str += startTime + " - " + endTime;
    } else {
        str += "- " + endTime + ", " + startTime + " -";
    }
    // str += - 21:00, 22:00 -
    str += "</div>";
    str += "</div>";
    str += "</div>";
    return str;
}
