document.addEventListener('DOMContentLoaded', () => {


    document.querySelector('#yearForm').onsubmit = () => {

        // Initialize new request

        const request = new XMLHttpRequest();

        const year1 = document.querySelector('#year1').value;
        localStorage.setItem('year', year1);
        request.open('POST', '/car_city');

        // Callback function for when request completes
        request.onload = () => {

            // Extract JSON data from request
            const data = JSON.parse(request.responseText);

            document.querySelector('#brandForm').innerHTML = "";

            // Update the result div
            var div = document.createElement('div');
            div.className = 'input-group mb-3';
            document.querySelector('#brandForm').appendChild(div);

            var select = document.createElement('select');
            select.setAttribute('id', "brand1");
            select.setAttribute('class', "form-control");
             for (var i = 0; i < `${data.size}` ; i++) {
                      var option = document.createElement('option');
                      option.setAttribute('value', `${data.brands[i]}`);
                      var t = document.createTextNode(`${data.brands[i]}`);
                      option.appendChild(t);
                      select.appendChild(option);
                      div.appendChild(select);
                  }
            document.querySelector('#brand').innerHTML = "Car's brand";
            var div2 = document.createElement('div');
            div2.className = 'input-group-append';
            div2.innerHTML = '<button class="btn">Send</button>';
            div.appendChild(div2);

//            document.querySelector('#brandForm3').innerHTML += input;
        }
        // Add data to send with request
        const data = new FormData();
        data.append('year1', year1);

        // Send request
        request.send(data);
        return false;
    };

    document.querySelector('#brandForm').onsubmit = () => {

        // Initialize new request

        const request = new XMLHttpRequest();

        const brand1 = document.querySelector('#brand1').value;
        localStorage.setItem('brand', brand1);
        request.open('POST', '/car_city2');

        // Callback function for when request completes
        request.onload = () => {

            // Extract JSON data from request
            const data = JSON.parse(request.responseText);

            document.querySelector('#modelForm').innerHTML = "";

            // Update the result div
            var div = document.createElement('div');
            div.className = 'input-group mb-3';
            document.querySelector('#modelForm').appendChild(div);
            var select = document.createElement('select');
            select.setAttribute('id', "model1");
            select.setAttribute('class', "form-control");
             for (var i = 0; i < `${data.size_models}` ; i++) {
                      var option = document.createElement('option');
                      option.setAttribute('value', `${data.models[i]}`);
                      var t = document.createTextNode(`${data.models[i]}`);
                      option.appendChild(t);
                      select.appendChild(option)
                      div.appendChild(select);
                  }

            document.querySelector('#model').innerHTML = "Car's model";
            var div2 = document.createElement('div');
            div2.className = 'input-group-append';
            div2.innerHTML = '<button class="btn">Send</button>';
            div.appendChild(div2);

        }
        // Add data to send with request
        const data = new FormData();
        data.append('brand1', brand1);
        year = localStorage.getItem('year');
        data.append('year', year);

        // Send request
        request.send(data);
        return false;
    };

    document.querySelector('#modelForm').onsubmit = () => {

        // Initialize new request

        const request = new XMLHttpRequest();

        const model1 = document.querySelector('#model1').value;
        localStorage.setItem('model', model1);
        request.open('POST', '/car_city3');

        // Callback function for when request completes
        request.onload = () => {

            // Extract JSON data from request
            const data = JSON.parse(request.responseText);

            document.querySelector('#versionForm').innerHTML = "";

            // Update the result div
            var div = document.createElement('div');
            div.className = 'input-group mb-3';
            document.querySelector('#versionForm').appendChild(div);
            var select = document.createElement('select');
            select.setAttribute('id', "version1");
            select.setAttribute('class', "form-control");
             for (var i = 0; i < `${data.size_versions}` ; i++) {
                      var option = document.createElement('option');
                      option.setAttribute('value', `${data.versions[i]}`);
                      var t = document.createTextNode(`${data.versions[i]}`);
                      option.appendChild(t);
                      select.appendChild(option)
                      div.appendChild(select);
                  }

            document.querySelector('#version').innerHTML = "Car's version";
            var div2 = document.createElement('div');
            div2.className = 'input-group-append';
            div2.innerHTML = '<button class="btn">Send</button>';
            div.appendChild(div2);
        }
        // Add data to send with request
        const data = new FormData();
        data.append('model1', model1);
        year = localStorage.getItem('year');
        data.append('year', year);
        brand = localStorage.getItem('brand');
        data.append('brand', brand);

        // Send request
        request.send(data);
        return false;
    };

    document.querySelector('#versionForm').onsubmit = () => {

        // Initialize new request

        const request = new XMLHttpRequest();

        const version1 = document.querySelector('#version1').value;
        localStorage.setItem('version', version1);
        request.open('POST', '/car_city4');

        // Callback function for when request completes
        request.onload = () => {

            // Extract JSON data from request
            const data = JSON.parse(request.responseText);

            document.querySelector('#engineForm').innerHTML = "";

            // Update the result div
            var div = document.createElement('div');
            div.className = 'input-group mb-3';
            document.querySelector('#engineForm').appendChild(div);
            var select = document.createElement('select');
            select.setAttribute('id', "engine1");
            select.setAttribute('class', "form-control");
             for (var i = 0; i < `${data.size_engines}` ; i++) {
                      var option = document.createElement('option');
                      option.setAttribute('value', `${data.engines[i]}`);
                      var t = document.createTextNode(`${data.engines[i]}`);
                      option.appendChild(t);
                      select.appendChild(option)
                      div.appendChild(select);
                  }

            document.querySelector('#engine').innerHTML = "Car's engine";
            var div2 = document.createElement('div');
            div2.className = 'input-group-append';
            div2.innerHTML = '<button class="btn">Send</button>';
            div.appendChild(div2);
        }
        // Add data to send with request
        const data = new FormData();
        data.append('version1', version1);
        year = localStorage.getItem('year');
        data.append('year', year);
        brand = localStorage.getItem('brand');
        data.append('brand', brand);
        model = localStorage.getItem('model');
        data.append('model', model);

        // Send request
        request.send(data);
        return false;
    };


   document.querySelector('#engineForm').onsubmit = () => {

        // Initialize new request

        const request = new XMLHttpRequest();

        const engine1 = document.querySelector('#engine1').value;
        localStorage.setItem('engine', engine1);
        request.open('POST', '/car_city5');

        // Callback function for when request completes
        request.onload = () => {

            // Extract JSON data from request
            const data = JSON.parse(request.responseText);

            document.querySelector('#cityForm').innerHTML = "";

            // Update the result div
            var div = document.createElement('div');
            div.className = 'input-group mb-3';
            document.querySelector('#cityForm').appendChild(div);
            var select = document.createElement('select');
            select.setAttribute('id', "city1");
            select.setAttribute('class', "form-control");
             for (var i = 0; i < `${data.size_cities}` ; i++) {
                      var option = document.createElement('option');
                      option.setAttribute('value', `${data.cities[i]}`);
                      var t = document.createTextNode(`${data.cities[i]}`);
                      option.appendChild(t);
                      select.appendChild(option)
                      div.appendChild(select);
                  }

            document.querySelector('#city').innerHTML = "Location";
            var div2 = document.createElement('div');
            div2.className = 'input-group-append';
            div2.innerHTML = '<button class="btn">Send</button>';
            div.appendChild(div2);
        }
        // Add data to send with request
        const data = new FormData();
        data.append('engine1', engine1);
//        year = localStorage.getItem('year');
//        data.append('year', year);
//        brand = localStorage.getItem('brand');
//        data.append('brand', brand);
//        model = localStorage.getItem('model');
//        data.append('model', model);
//        version = localStorage.getItem('version');
//        data.append('version', version);

        // Send request
        request.send(data);
        return false;
        };


    document.querySelector('#cityForm').onsubmit = () => {

        // Initialize new request

        const request = new XMLHttpRequest();

        const city1 = document.querySelector('#city1').value;
        request.open('POST', '/car_city6');

        // Callback function for when request completes
        request.onload = () => {

            // Extract JSON data from request
            const data = JSON.parse(request.responseText);

            // Update the result div
            const car_summary1 = `${data.message}`
            document.querySelector('#car_summary1').innerHTML = car_summary1;
            const car_summary2 = `${data.message_city}`
            document.querySelector('#car_summary2').innerHTML = car_summary2;
            const car_summary3 = `${data.message_road}`
            document.querySelector('#car_summary3').innerHTML = car_summary3;

            const knowmore1 = 'Details &#xf078';
            document.querySelector('#knowmore1').innerHTML = knowmore1;

            document.querySelector('#knowmore3').innerHTML = "";

            const price_ethanol = 'Ethanol price: R$ ' + `${data.ethanol_price}`;
            var li = document.createElement('li');
            li.innerHTML = price_ethanol;
            document.querySelector('#knowmore3').append(li);

            const price_gas = 'Gasoline price: R$ ' + `${data.gas_price}`;
            var li = document.createElement('li');
            li.innerHTML = price_gas;
            document.querySelector('#knowmore3').append(li);

            const km_per_liter_ethanol_city = 'Ethanol city: ' + `${data.km_per_liter_ethanol_city}` + ' km/l';
            var li = document.createElement('li');
            li.innerHTML = km_per_liter_ethanol_city;
            document.querySelector('#knowmore3').append(li);

            const km_per_liter_ethanol_road = 'Ethanol road: ' + `${data.km_per_liter_ethanol_road}` + ' km/l';
            var li = document.createElement('li');
            li.innerHTML = km_per_liter_ethanol_road;
            document.querySelector('#knowmore3').append(li);

            const km_per_liter_gas_city = 'Gas city: ' + `${data.km_per_liter_gas_city}` + ' km/l';
            var li = document.createElement('li');
            li.innerHTML = km_per_liter_gas_city;
            document.querySelector('#knowmore3').append(li);

            const km_per_liter_gas_road = 'Gas road: ' + `${data.km_per_liter_gas_road}` + ' km/l';
            var li = document.createElement('li');
            li.innerHTML = km_per_liter_gas_road;
            document.querySelector('#knowmore3').append(li);

            const date = 'Fuel prices updated on: ' + `${data.date}`;
            var li = document.createElement('li');
            li.innerHTML = date;
            document.querySelector('#knowmore3').append(li);

        }
        // Add data to send with request
        const data = new FormData();
        data.append('city1', city1);

        year = localStorage.getItem('year');
        brand = localStorage.getItem('brand');
        model = localStorage.getItem('model');
        version = localStorage.getItem('version');
        engine = localStorage.getItem('engine');
        data.append('year', year);
        data.append('brand', brand);
        data.append('model', model);
        data.append('version', version);
        data.append('engine', engine);

        // Send request
        request.send(data);
        return false;
    };


});