$(document).ready(function () {

    const btnAvailableHours = document.getElementById('available-hours');
    let table = document.getElementById('schedule-table');
    let httpResponse = {};

    btnAvailableHours.addEventListener('click', function (httpResponse) {

        let formatedDate = '';
        const date = document.getElementById('datetimepicker1Input').value;
        const hours = ["09:00:00", "10:00:00", "11:00:00", "12:00:00", "13:00:00", "14:00:00", "15:00:00", "16:00:00", "17:00:00", "18:00:00"];

        // Convert date format: MM/DD/YYYY to YYYY-MM-DD
        const month = date.substr(0, 2);
        const day = date.substr(3, 2);
        const year = date.substr(6, 4);

        formatedDate = year + '-' + month + '-' + day;
        console.log(formatedDate);

        // AJAX GET DATA =>
        // parameters: codigo
        // return: dictionary (javascript object)

        let url ='http://127.0.0.1:5000/not-available-hours/' + formatedDate;

        function load(url, callback) {
            var xhr = new XMLHttpRequest();
          
            xhr.onreadystatechange = function() {
              if (xhr.readyState === 4) {
                callback(xhr.response);
              }
            }
          
            xhr.open('GET', url, true);
            xhr.send();
          }
          load('GET', url, true);
    });
    
    console.log(typeof httpResponse);
    console.log(httpResponse);
    
    if (httpResponse['message'] === "all office day available") {
        
        table.innerHTML = `
            <table class="table table-borderless" id="schedule-table">
                <tbody id="schedule-tbody">
                    <tr>
                        <td><button class="btn hour-btn" type="button" id="9" >09:00:00</button></td>
                        <td><button class="btn hour-btn" type="button" id="10" >10:00:00</button></td>
                        <td><button class="btn hour-btn" type="button" id="11" >11:00:00</button></td>
                        <td><button class="btn hour-btn" type="button" id="12" >12:00:00</button></td>
                        <td><button class="btn hour-btn" type="button" id="13" >13:00:00</button></td>
                    </tr>
                    <tr>
                        <td><button class="btn hour-btn" type="button" id="14" >14:00:00</button></td>
                        <td><button class="btn hour-btn" type="button" id="15" >15:00:00</button></td>
                        <td><button class="btn hour-btn" type="button" id="16" >16:00:00</button></td>
                        <td><button class="btn hour-btn" type="button" id="17" >17:00:00</button></td>
                        <td><button class="btn hour-btn" type="button" id="18" >18:00:00</button></td>
                    </tr>
                </tbody>
            </table>
        `;
    }


    $("#09").click(function () {
    time.value = document.getElementById('09').textContent;
});
$("#10").click(function () {
    time.value = document.getElementById('10').textContent;
});
$("#11").click(function () {
    time.value = document.getElementById('11').textContent;
});
$("#12").click(function () {
    time.value = document.getElementById('12').textContent;
});
$("#13").click(function () {
    time.value = document.getElementById('13').textContent;
});
$("#14").click(function () {
    time.value = document.getElementById('14').textContent;
});
$("#15").click(function () {
    time.value = document.getElementById('15').textContent;
});
$("#16").click(function () {
    time.value = document.getElementById('16').textContent;
});
$("#17").click(function () {
    time.value = document.getElementById('17').textContent;
});
$("#18").click(function () {
    time.value = document.getElementById('18').textContent;
});

});