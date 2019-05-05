document.addEventListener('DOMContentLoaded', () => {


    if (localStorage.getItem('city')) {
            document.querySelector('#city4').value = localStorage.getItem('city');
    }

//    if (localStorage.getItem('car')) {
//            document.querySelector('#answer').value = localStorage.getItem('car');
//    }

    if ((document.querySelector('#city4').value.length > 0) && (document.querySelector('#answer').value.length > 0))
        document.querySelector('#submit').disabled = false;
    else
        document.querySelector('#submit').disabled = true;

    // By default, submit button is disabled
//    document.querySelector('#submit').disabled = true;

    // Enable button only if there is text in the input field
    document.querySelector('#city4').onkeyup = () => {

            console.log(document.querySelector('#city4').value);
            string = document.querySelector('#city4').value;
            var replaceChars = { "ç":"c" , "ã":"a" , "á":"a" , "â":"a" , "õ":"o" , "ó":"o" , "ô":"o" , "é":"e" , "ê":"e" , "ú":"u" , "í":"i"};
            var new_city = string.replace(/ç|ã|á|â|õ|ó|ô|é|ê|ú|í/g,function(match) {return replaceChars[match];})
            document.querySelector('#city4').value = new_city;
            console.log(document.querySelector('#city4').value);


        let city = document.querySelector('#city4').value;
        localStorage.setItem('city', city);

        if ((document.querySelector('#city4').value.length > 0) && (document.querySelector('#answer').value.length > 0))
            document.querySelector('#submit').disabled = false;
        else
            document.querySelector('#submit').disabled = true;
    };

    document.querySelector('#answer').onkeyup = () => {

//        let car = document.querySelector('#answer').value;
//        localStorage.setItem('car', car);

        if ((document.querySelector('#city4').value.length > 0) && (document.querySelector('#answer').value.length > 0))
            document.querySelector('#submit').disabled = false;
        else
            document.querySelector('#submit').disabled = true;
    };

    document.querySelector('#delete').onclick = () => {
        document.querySelector('#city4').value = '';
        return false;
    };

    document.querySelector('#delete_car').onclick = () => {
        document.querySelector('#answer').value = '';
        return false;
    };

//    document.querySelector('#expand').onclick = () => {
        document.addEventListener('click', event => {
                const element = event.target;
                if (element.className === 'expand') {

                    element.parentElement.style.animationPlayState = 'running';
                    element.parentElement.addEventListener('animationend', () =>  {

                    var label = document.createElement('label');
                     label.setAttribute('for', "ethanol_price1");
                     var t = document.createTextNode("Ethanol R$/Liter");
                     label.appendChild(t);

                     document.querySelector('#manual_input').append(label);

                     var input = document.createElement('input');
                     input.setAttribute('name', "ethanol_price");
                     input.setAttribute('id', "ethanol_price1");
                     input.setAttribute('type', "number");
                     input.setAttribute('step', "0.001");
                     input.setAttribute('placeholder', "Ex: 2.99");
                     input.setAttribute('autocomplete', "off");

                     document.querySelector('#manual_input').append(input);

                     var label = document.createElement('label');
                     label.setAttribute('for', "gas_price1");
                     var t = document.createTextNode("Gasoline R$/Liter");
                     label.appendChild(t);

                     document.querySelector('#manual_input').append(label);

                     var input = document.createElement('input');
                     input.setAttribute('name', "gas_price");
                     input.setAttribute('id', "gas_price1");
                     input.setAttribute('type', "number");
                     input.setAttribute('step', "0.001");
                     input.setAttribute('placeholder', "Ex: 3.99");
                     input.setAttribute('autocomplete', "off");

                     document.querySelector('#manual_input').append(input);

                     return false;

                    });


                }
            });

//         var label = document.createElement('label');
//         label.setAttribute('for', "ethanol_price1");
//         var t = document.createTextNode("Ethanol R$/Liter");
//         label.appendChild(t);
//
//         document.querySelector('#manual_input').append(label);
//
//         var input = document.createElement('input');
//         input.setAttribute('name', "ethanol_price");
//         input.setAttribute('id', "ethanol_price1");
//         input.setAttribute('type', "number");
//         input.setAttribute('step', "0.001");
//         input.setAttribute('placeholder', "Ex: 2.99");
//         input.setAttribute('autocomplete', "off");
//
//         document.querySelector('#manual_input').append(input);
//
//         var label = document.createElement('label');
//         label.setAttribute('for', "gas_price1");
//         var t = document.createTextNode("Gasoline R$/Liter");
//         label.appendChild(t);
//
//         document.querySelector('#manual_input').append(label);
//
//         var input = document.createElement('input');
//         input.setAttribute('name', "gas_price");
//         input.setAttribute('id', "gas_price1");
//         input.setAttribute('type', "number");
//         input.setAttribute('step', "0.001");
//         input.setAttribute('placeholder', "Ex: 3.99");
//         input.setAttribute('autocomplete', "off");
//
//         document.querySelector('#manual_input').append(input);
//
//         return false;
//    };



    document.querySelector('input[list]').addEventListener('input', function(e) {
        var input = e.target,
            list = input.getAttribute('list'),
            options = document.querySelectorAll('#' + list + ' option'),
            hiddenInput = document.getElementById(input.getAttribute('id') + '-hidden'),
            label = input.value;


        hiddenInput.value = label;

        for(var i = 0; i < options.length; i++) {
            var option = options[i];

            if(option.innerText == label) {
                hiddenInput.value = option.getAttribute('data-value');
                break;
            }
        }
    });



    document.querySelector('#myForm').onsubmit = () => {


        // Initialize new request

        const request = new XMLHttpRequest();


        const city2 = document.querySelector('#city4').value;
        const answer = document.querySelector('#answer-hidden').value;


        var ethanol_price = document.querySelector('#ethanol_price1').value;
        var gas_price = document.querySelector('#gas_price1').value;

//        if (ethanol_price == null) {
//            ethanol_price = "";
//        }
//        if (gas_price == null) {
//            gas_price = "";
//        }



        request.open('POST', '/search_car_city');

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
        data.append('city2', city2);
        data.append('answer', answer);
        data.append('ethanol_price', ethanol_price);
        data.append('gas_price', gas_price);

        // Send request
        request.send(data);
        return false;
    };

//     var selected_city = document.querySelector('#selected_city').dataset.selected_city;
//     document.querySelector('#city4').innerHTML = selected_city;
//     console.log(selected_city)


});


//    document.querySelector('#expand').onclick = () => {
        document.addEventListener('click', event => {
                const element = event.target;
                if (element.className === 'expand') {

                    element.parentElement.style.animationPlayState = 'running';
                    element.parentElement.addEventListener('animationend', () =>  {

                    var label = document.createElement('label');
                     label.setAttribute('for', "ethanol_price1");
                     var t = document.createTextNode("Ethanol R$/Liter");
                     label.appendChild(t);

                     element.parentElement.append(label);

                     var input = document.createElement('input');
                     input.setAttribute('name', "ethanol_price");
                     input.setAttribute('id', "ethanol_price1");
                     input.setAttribute('type', "number");
                     input.setAttribute('step', "0.001");
                     input.setAttribute('placeholder', "Ex: 2.99");
                     input.setAttribute('autocomplete', "off");

                     element.parentElement.append(input);

                     var label = document.createElement('label');
                     label.setAttribute('for', "gas_price1");
                     var t = document.createTextNode("Gasoline R$/Liter");
                     label.appendChild(t);

                     document.querySelector('#manual_input').append(label);

                     var input = document.createElement('input');
                     input.setAttribute('name', "gas_price");
                     input.setAttribute('id', "gas_price1");
                     input.setAttribute('type', "number");
                     input.setAttribute('step', "0.001");
                     input.setAttribute('placeholder', "Ex: 3.99");
                     input.setAttribute('autocomplete', "off");

                     document.querySelector('#manual_input').append(input);

//                     return false;

                    });


                }
            });