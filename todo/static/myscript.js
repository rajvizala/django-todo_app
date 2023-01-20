const searchInput = document.querySelector("[data-search]");
const allTr = document.querySelectorAll("#records tr");
const recordsDisplay = document.getElementById('records')

searchInput.addEventListener("input", function (e) {
    let searchValue = e.target.value.toLowerCase();

    recordsDisplay.innerHTML = "";

    allTr.forEach(tr => {
        console.log("Bye..")
        const td_in_tr = tr.querySelectorAll('td');

        if (td_in_tr[0].innerText.toLocaleLowerCase().indexOf(searchValue) > -1) {
            recordsDisplay.appendChild(tr);
        }

    });

})

