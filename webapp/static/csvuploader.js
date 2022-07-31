// var csvData = $.csv.toObjects(csv);
// var regex = /^([a-zA-Z0-9\s_\\.\-:])+(.csv)$/;
// if (regex.text(fileUpload.value.toLowerCase())) {
//     if (typeof (FileReader) != "undefined") {
//         var readFile = new FileReader();
//         readFile.onload = function (e) {
//             var table = document.createElement("table");
//             var rows = e.target.result.split("\n");
//             for (var i = 0; i < rows.length; i++) {
//                 var cells = rows[i].split(",");
//                 if (cells.length > 1) {
//                     var row = table.insertRow(-1);
//                     for (var j = 0; j < cells.length; j++) {
//                         var cell = row.insertCell(-1);
//                         cell.innerHTML = cells[j];
//                     }
//                 }
//             }
//             var csv = document.getElementById("CSV");
//             csv.innerHTML = "";
//             csv.appendChild(table);
//         }
//         readFile.readAsText(fileUpload.files[0]);
//     }
// }

function readFile(e) {
    var file = e.target.files[0];
    if (!file) {
        return;
    }
    var readFile = new FileReader();
    readFile.onload = function(e) {
        var contents = e.target.result;
        displayContents(contents);
    };
    readFile.readAsText(file);
}

function displayContents(contents) {
    var element = document.getElementById("CSV");
    element.innerHTML = contents;
}