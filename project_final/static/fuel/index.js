document.addEventListener('DOMContentLoaded', () => {
    document.querySelector('#button').onclick = () => {
         document.getElementById("myDropdown").classList.toggle("show");
    };

    document.querySelector('#myInput').onkeyup =() => {
        var input, filter, ul, li, a, i;
        input = document.getElementById("myInput");
        filter = input.value.toUpperCase();
        div = document.getElementById("myDropdown");
        a = div.getElementsByTagName("a");
        console.log(a.length)
        for (i = 0; i < a.length; i++) {
            txtValue = a[i].textContent || a[i].innerText;
            console.log(txtValue)
//            if (filter.length >= 3) {
                if (txtValue.toUpperCase().indexOf(filter) > -1) {
                    a[i].style.display = "";
                } else {
                    a[i].style.display = "none";
                }
//            }
        }
    };



//    $("input").click(function(){
//        $(this).next().show();
//        $(this).next().hide();
//    });

//    document.addEventListener('click', function(){
//        document.getElementsByTagName('input');
//        $(this).next().show();
//        $(this).next().hide();
//    });



//    function filterFunction() {
//        var input, filter, ul, li, a, i;
//        input = document.getElementById("myInput");
//        filter = input.value.toUpperCase();
//        div = document.getElementById("myDropdown");
//        a = div.getElementsByTagName("a");
//        for (i = 0; i < a.length; i++) {
//            txtValue = a[i].textContent || a[i].innerText;
//            if (txtValue.toUpperCase().indexOf(filter) > -1) {
//                a[i].style.display = "";
//            } else {
//                a[i].style.display = "none";
//            }
//        }
//    }
});