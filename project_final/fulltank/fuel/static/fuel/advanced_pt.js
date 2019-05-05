document.addEventListener('DOMContentLoaded', () => {

    document.querySelector('#yearForm').onsubmit = () => {

        // Initialize new request
        const request = new XMLHttpRequest();

        // save year selected to local storage
        const year1 = document.querySelector('#year1').value;
        localStorage.setItem('year', year1);
        request.open('POST', '/car_city');

        // Callback function for when request completes
        request.onload = () => {

            // Extract JSON data from request
            const data = JSON.parse(request.responseText);

            document.querySelector('#brandForm').innerHTML = "";

            // Create select on brandForm
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
            document.querySelector('#brand').innerHTML = "Marca do Carro";
            var div2 = document.createElement('div');
            div2.className = 'input-group-append';
            div2.innerHTML = '<button class="btn">Próximo</button>';
            div.appendChild(div2);
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

            // Create select on modelForm
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

            document.querySelector('#model').innerHTML = "Modelo do Carro";
            var div2 = document.createElement('div');
            div2.className = 'input-group-append';
            div2.innerHTML = '<button class="btn">Próximo</button>';
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

            // Create select on versionForm
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

            document.querySelector('#version').innerHTML = "Versão do Carro";
            var div2 = document.createElement('div');
            div2.className = 'input-group-append';
            div2.innerHTML = '<button class="btn">Próximo</button>';
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

            // Create select on engineForm
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

            document.querySelector('#engine').innerHTML = "Motor do Carro";
            var div2 = document.createElement('div');
            div2.className = 'input-group-append';
            div2.innerHTML = '<button class="btn">Próximo</button>';
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

            // Create select on cityForm
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

            document.querySelector('#city').innerHTML = "Cidade";
            var div2 = document.createElement('div');
            div2.className = 'input-group-append';
            div2.innerHTML = '<button class="btn">Próximo</button>';
            div.appendChild(div2);
        }
        // Add data to send with request
        const data = new FormData();
        data.append('engine1', engine1);

        // Send request
        request.send(data);
        return false;
        };


    document.querySelector('#cityForm').onsubmit = () => {

        // Initialize new request
        const request = new XMLHttpRequest();

        const city1 = document.querySelector('#city1').value;

        // empty fields for reload
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

        request.open('POST', '/car_city6');

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
            if (car_city != 'gasolina' && car_city !='etanol') {
                document.querySelector('#car_city').innerHTML = car_city
            }
            else {
                document.querySelector('#car_city').innerHTML = '&nbsp&nbspNA CIDADE É MAIS BARATO USAR <strong id="' + car_city + '">' + car_city + '</strong>&nbsp&nbsp';
                    document.querySelector('#car_road').innerHTML = 'NA ESTRADA É MAIS BARATO USAR <strong id="' + car_road + '">' + car_road + '</strong>';
            }

            // insert details
            if (`${data.success}` == 1) {

                const knowmore1 = '+Detalhes <i class="fas fa-chevron-down"></i>';
                document.querySelector('#knowmore1').innerHTML = knowmore1;

                document.querySelector('#knowmore3').innerHTML = "";

                const price = 'Preço Etanol: R$ ' + `${data.ethanol_price}` + ' Preço Gasolina: R$ ' + `${data.gas_price}`;
                var li = document.createElement('li');
                li.innerHTML = price;
                document.querySelector('#knowmore3').append(li);


                const km_per_liter_city = 'Etanol na Cidade: ' + `${data.km_per_liter_ethanol_city}` + ' km/l' + ' Gasolina na Cidade: ' + `${data.km_per_liter_gas_city}` + ' km/l';
                var li = document.createElement('li');
                li.innerHTML = km_per_liter_city;
                document.querySelector('#knowmore3').append(li);

                const km_per_liter_road = 'Etanol na Estrada: ' + `${data.km_per_liter_ethanol_road}` + ' km/l' + ' Gasolina na Estrada: ' + `${data.km_per_liter_gas_road}` + ' km/l';
                var li = document.createElement('li');
                li.innerHTML = km_per_liter_road;
                document.querySelector('#knowmore3').append(li);

                const date = 'Preço dos combustíveis atualizados em: ' + `${data.date}`;
                var li = document.createElement('li');
                li.innerHTML = date;
                document.querySelector('#knowmore3').append(li);
            }

        };
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