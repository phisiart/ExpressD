function HMStoSec(T) { // h:m:s
    var A = T.split(/\D+/);
    return (A[0] * 60 + +A[1]) * 60 + +A[2];
}

function genTimeBar(startTime, endTime) {
    var s = HMStoSec(startTime);
    var e = HMStoSec(endTime);
    var str = "<div class=\"progress\" style=\"margin-bottom: 0px;\">";
    if (e >= s) {
        var p1 = s / 86400.0 * 100;
        var p2 = (e - s) / 86400.0 * 100;
        var p3 = (86400 - e) / 86400.0 * 100;
        str += "<div class=\"progress-bar progress-bar-danger progress-bar-striped\" style=\"width: " + p1 + "%\"></div>";
        str += "<div class=\"progress-bar progress-bar-success\" style=\"width: " + p2 + "%\"></div>";
        str += "<div class=\"progress-bar progress-bar-danger progress-bar-striped\" style=\"width: " + p3 + "%\"></div>";
    } else {

    }
    str += "</div>";
    return str;
}
