$(document).ready(function() {
    console.log("Page Loaded");

    $("#filter").click(function() {
        // alert("button clicked!");
        makePredictions();
    });
});

// call Flask API endpoint
function makePredictions() {
    let track_name = $("#track_name").val();
    let track_artist = $("#track_artist").val();

    // check if inputs are valid

    // create the payload
    let payload = {
        "track_name": track_name,
        "track_artist": track_artist
    }

    // Perform a POST request to the query URL
    $.ajax({
        type: "POST",
        url: "/makePredictions",
        contentType: 'application/json;charset=UTF-8',
        data: JSON.stringify({ "data": payload }),
        success: function(returnedData) {
            // print it
            console.log(returnedData);
            renderTable(returnedData["prediction"]);

        },
        error: function(XMLHttpRequest, textStatus, errorThrown) {
            alert("Status: " + textStatus);
            alert("Error: " + errorThrown);
        }
    });

}

    function renderTable(inp_data) {
        // init html string
        let html = "";
    
        // destroy datatable
        $('#sql_table').DataTable().clear().destroy();
    
        // loop through all rows
        inp_data.forEach(function(row) {
            html += "<tr>";
           
            // loop through each cell (order matters)
            html += `<td>${row.track_id}</td>`;
            html += `<td>${row.track_name}</td>`;
            html += `<td>${row.track_artist}</td>`;
            html += `<td>${row.album_name}</td>`;
        
            // close the row
            html += "</tr>";
        });
    
        // shove the html in our elements
        console.log(html);
        $("#sql_table tbody").html("");
        $("#sql_table tbody").append(html);
    
        // remake data table
        $('#sql_table').DataTable({order: [[6, 'asc']]});
    }