document.addEventListener('DOMContentLoaded', () => {

    // place last used city on #city4
    if (localStorage.getItem('city')) {
            document.querySelector('#city4').value = localStorage.getItem('city');
    }

    // Replace accent chars on city4 input
    document.querySelector('#city4').onkeyup = () => {

            console.log(document.querySelector('#city4').value);
            string = document.querySelector('#city4').value;
            var replaceChars = { "ç":"c" , "ã":"a" , "á":"a" , "â":"a" , "õ":"o" , "ó":"o" , "ô":"o" , "é":"e" , "ê":"e" , "ú":"u" , "í":"i"};
            var new_city = string.replace(/ç|ã|á|â|õ|ó|ô|é|ê|ú|í/g,function(match) {return replaceChars[match];})
            document.querySelector('#city4').value = new_city;
            console.log(document.querySelector('#city4').value);

        // Save entered city to local localStorage
        let city = document.querySelector('#city4').value;
        localStorage.setItem('city', city);
    };

    // Empty fields when delete is clicked
    document.querySelector('#delete').onclick = () => {
        document.querySelector('#city4').value = '';
        return false;
    };

    document.querySelector('#delete_car').onclick = () => {
        document.querySelector('#answer').value = '';
        return false;
    };

    document.querySelector('#delete_gas').onclick = () => {
        document.querySelector('#gas_price1').value = '';
        return false;
    };

    document.querySelector('#delete_ethanol').onclick = () => {
        document.querySelector('#ethanol_price1').value = '';
        return false;
    };

    // replace car selected on datalist by the car.id
    document.querySelector('input[list]').addEventListener('input', function(e) {

        var input = e.target,
            list = input.getAttribute('list'),
            options = document.querySelectorAll('#' + list + ' option'),
            hiddenInput = document.getElementById(input.getAttribute('id') + '-hidden'),
            label = input.value;

        hiddenInput.value = label;

        for(var i = 0; i < options.length; i++) {
            var option = options[i];
            if(option.value == label) {
                hiddenInput.value = option.getAttribute('data-value');
                break;
            }
        }
    });

    document.querySelector('#myForm').onsubmit = () => {

        // Initialize new request
        const request = new XMLHttpRequest();
        // obtain car.id
        const answer = document.querySelector('#answer-hidden').value;
        if (answer == "") {
            return false;
        }
        // obtain selected city
        const city2 = document.querySelector('#city4').value;
        // obtain fuel prices manually entered
        var ethanol_price = document.querySelector('#ethanol_price1').value;
        var gas_price = document.querySelector('#gas_price1').value;

        if (city2 == "" && (ethanol_price == "" || gas_price == "")) {
            return false;
        }

        // empty selector for when resubmiting
        document.querySelector('#results').innerHTML = "";
        document.querySelector('#car_summary').innerHTML = "";
        document.querySelector('#knowmore1').innerHTML = "";
        document.querySelector('#knowmore3').innerHTML = "";
        document.querySelector('#loading').innerHTML = "";

        // loading spinner
        var div = document.createElement('div');
        div.className = 'spinner-border';
        div.setAttribute('role', "status");
        div.innerHTML = '<span class="sr-only">Loading...</span>';
        document.querySelector('#loading').append(div);

        request.open('POST', '/search_car_city');

        // Callback function for when request completes
        request.onload = () => {

            // Extract JSON data from request
            const data = JSON.parse(request.responseText);

            document.querySelector('#loading').innerHTML = "";
            // create table
            var table = document.createElement('table');
            var tr = document.createElement('tr');
            var td = document.createElement('td');
            td.setAttribute('id', 'car_city');
            table.appendChild(tr);
            tr.appendChild(td);

            var tr2 = document.createElement('tr');
            var td2 = document.createElement('td');
            td2.setAttribute('id', 'car_road');
            table.appendChild(tr2);
            tr2.appendChild(td2);
            document.querySelector('#results').appendChild(table);

            // insert car_summary data
            const car_summary = `${data.message}`
            document.querySelector('#car_summary').innerHTML = car_summary;

            // insert car_city/car_road
            const car_road = `${data.message_road}`;
            const car_city = `${data.message_city}`;
            if (car_city != 'gasoline' && car_city !='ethanol') {
                document.querySelector('#car_city').innerHTML = car_city
            }
            else {
                document.querySelector('#car_city').innerHTML = 'CITY: <strong id="' + car_city + '">' + car_city + '</strong> IS CHEAPER';
                document.querySelector('#car_road').innerHTML = 'ROAD: <strong id="' + car_road + '">' + car_road + '</strong> IS CHEAPER';
            }

            // insert details
            if (`${data.success}` == 1) {

                const knowmore1 = '+Details <i class="fas fa-chevron-down"></i>';
                document.querySelector('#knowmore1').innerHTML = knowmore1;

                document.querySelector('#knowmore3').innerHTML = "";

                const price = 'Ethanol price: R$ ' + `${data.ethanol_price}` + ' Gasoline price: R$ ' + `${data.gas_price}`;
                var li = document.createElement('li');
                li.innerHTML = price;
                document.querySelector('#knowmore3').append(li);


                const km_per_liter_city = 'Ethanol city: ' + `${data.km_per_liter_ethanol_city}` + ' km/l' + ' Gas city: ' + `${data.km_per_liter_gas_city}` + ' km/l';
                var li = document.createElement('li');
                li.innerHTML = km_per_liter_city;
                document.querySelector('#knowmore3').append(li);

                const km_per_liter_road = 'Ethanol road: ' + `${data.km_per_liter_ethanol_road}` + ' km/l' + ' Gas road: ' + `${data.km_per_liter_gas_road}` + ' km/l';
                var li = document.createElement('li');
                li.innerHTML = km_per_liter_road;
                document.querySelector('#knowmore3').append(li);

                if (`${data.date}` != "") {
                const date = 'Fuel prices updated on: '  + `${data.date}`;
                var li = document.createElement('li');
                li.innerHTML = date;
                document.querySelector('#knowmore3').append(li);
                }
                else {
                    const date = 'Fuel prices provided by the user';
                    var li = document.createElement('li');
                    li.innerHTML = date;
                    document.querySelector('#knowmore3').append(li);
                }
            }
        };

        // Add data to send with request
        const data = new FormData();
        data.append('city2', city2);
        data.append('answer', answer);
        data.append('ethanol_price', ethanol_price);
        data.append('gas_price', gas_price);

        // Send request
        request.send(data);
        return false;
    };
});