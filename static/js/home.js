// function to reload page with showing resubmission dialog
window.onload = function () {
    history.replaceState("", "", "/");

    // for changing state according to rules
    original_link = document.getElementById('og-link').textContent;
    link = document.getElementById('linkhere').textContent;
    const action = document.getElementById('submit');

    if (link == 'Generate a link !' || link == 'Put a link !!' || link == 'Invalid URL' && original_link.length == 0) { action.innerHTML = 'Short'; }
    else { action.innerHTML = 'Copy'; }
};

// for redirecting to the link which is sorted by clicking on it. 
function click_redirect_to() {
    link = document.getElementById('linkhere').textContent;
    if (link == 'Generate a link !' || link == 'Put a link !!') { }
    else { window.open(link, "_blank"); }
};

// for copying shorted link directly from 'short' button by changing it to 'copy'
function copy_text() {
    link = document.getElementById('linkhere').textContent;
    if (link == 'Generate a link !' || link == 'Put a link !!') { }
    else { navigator.clipboard.writeText(link).then(function () { alert('Copied !'); }, function () { }); }

};

// for redirecting to my github account.
function click_redirect_to_anas() {
    window.open('https://github.com/Anas-Dew', "_blank");
};