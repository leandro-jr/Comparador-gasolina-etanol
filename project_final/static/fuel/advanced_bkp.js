document.addEventListener('DOMContentLoaded', () => {


    document.querySelector('#brandForm').onsubmit = () => {

        // Initialize new request

        const request = new XMLHttpRequest();

        const car3 = document.querySelector('#car3').value;
        localStorage.setItem('brand', car3);
        request.open('POST', '/car_city');

        // Callback function for when request completes
        request.onload = () => {

            // Extract JSON data from request
            const data = JSON.parse(request.responseText);

            // Update the result div
            var select = document.createElement('select');
            select.setAttribute('id', "car4");
             for (var i = 0; i < `${data.size}` ; i++) {
                      var option = document.createElement('option');
                      option.setAttribute('value', `${data.models[i]}`);
                      var t = document.createTextNode(`${data.models[i]}`);
                      option.appendChild(t);
                      select.appendChild(option)
                      document.querySelector('#modelForm').append(select);
                  }

            document.querySelector('#model').innerHTML = "2 - What's your car model?";
            var input = document.createElement('input');
            input.setAttribute('type', "submit");
            input.setAttribute('value', "Send");
            document.querySelector('#modelForm').append(input);
        }
        // Add data to send with request
        const data = new FormData();
        data.append('car3', car3);

        // Send request
        request.send(data);
        return false;
    };

    document.querySelector('#modelForm').onsubmit = () => {

        // Initialize new request

        const request = new XMLHttpRequest();

        const car4 = document.querySelector('#car4').value;
        localStorage.setItem('model', car4);
        request.open('POST', '/car_city2');

        // Callback function for when request completes
        request.onload = () => {

            // Extract JSON data from request
            const data = JSON.parse(request.responseText);

            // Update the result div
            var select = document.createElement('select');
            select.setAttribute('id', "car5");
             for (var i = 0; i < `${data.size_versions}` ; i++) {
                      var option = document.createElement('option');
                      option.setAttribute('value', `${data.versions[i]}`);
                      var t = document.createTextNode(`${data.versions[i]}`);
                      option.appendChild(t);
                      select.appendChild(option)
                      document.querySelector('#versionForm').append(select);
                  }

            document.querySelector('#version').innerHTML = "3 - What's your car version?";
            var input = document.createElement('input');
            input.setAttribute('type', "submit");
            input.setAttribute('value', "Send");
            document.querySelector('#versionForm').append(input);
        }
        // Add data to send with request
        const data = new FormData();
        data.append('car4', car4);

        // Send request
        request.send(data);
        return false;
    };

    document.querySelector('#versionForm').onsubmit = () => {

        // Initialize new request

        const request = new XMLHttpRequest();

        const car5 = document.querySelector('#car5').value;
        localStorage.setItem('version', car5);
        request.open('POST', '/car_city3');

        // Callback function for when request completes
        request.onload = () => {

            // Extract JSON data from request
            const data = JSON.parse(request.responseText);

            // Update the result div
            var select = document.createElement('select');
            select.setAttribute('id', "city1");
             for (var i = 0; i < `${data.size_cities}` ; i++) {
                      var option = document.createElement('option');
                      option.setAttribute('value', `${data.cities[i]}`);
                      var t = document.createTextNode(`${data.cities[i]}`);
                      option.appendChild(t);
                      select.appendChild(option)
                      document.querySelector('#cityForm').append(select);
                  }

            document.querySelector('#city').innerHTML = "4 - Where are you going to fill the tank?";
            var input = document.createElement('input');
            input.setAttribute('type', "submit");
            input.setAttribute('value', "Send");
            document.querySelector('#cityForm').append(input);
        }
        // Add data to send with request
        const data = new FormData();
        data.append('car5', car5);

        // Send request
        request.send(data);
        return false;
    };

    document.querySelector('#cityForm').onsubmit = () => {

        // Initialize new request

        const request = new XMLHttpRequest();

        const city1 = document.querySelector('#city1').value;
        request.open('POST', '/car_city4');

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
        }
        // Add data to send with request
        const data = new FormData();
        data.append('city1', city1);

        brand = localStorage.getItem('brand');
        model = localStorage.getItem('model');
        version = localStorage.getItem('version');
        data.append('brand', brand);
        data.append('model', model);
        data.append('version', version);

        // Send request
        request.send(data);
        return false;
    };


});