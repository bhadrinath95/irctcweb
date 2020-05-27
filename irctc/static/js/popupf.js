$(document).ready(function() {
    $('#options').click(function() {
        window.open("optionsb.html");
    });
    chrome.storage.local.get(null, function(items) {
        if (items.loginUsername != null) {
            $('#irctc').removeClass("hidden");
        }
    });
    $('#irctc').click(function() {
        window.open("https://www.irctc.co.in/nget/train-search");
    });
});