document.addEventListener("DOMContentLoaded", function() {
    const menuItems = document.querySelectorAll(".menu li");
    const itemsPerPage = 10;
    const totalItems = menuItems.length;
    let currentPage = 1;

    function showPage(page) {
        const startIndex = (page - 1) * itemsPerPage;
        const endIndex = startIndex + itemsPerPage;

        menuItems.forEach(function(item, index) {
            if (index >= startIndex && index < endIndex) {
                item.style.display = "block";
            } else {
                item.style.display = "none";
            }
        });
    }

    function updatePaginationButtons() {
        const totalPages = Math.ceil(totalItems / itemsPerPage);
        const pagination = document.querySelector(".pagination");
        pagination.innerHTML = "";

        for (let i = 1; i <= totalPages; i++) {
            const button = document.createElement("a");
            button.href = "#";
            button.textContent = i;
            if (i === currentPage) {
                button.classList.add("active");
            }
            button.addEventListener("click", function(event) {
                event.preventDefault();
                currentPage = i;
                showPage(currentPage);
                updatePaginationButtons();
            });
            pagination.appendChild(button);
        }
    }

    showPage(currentPage);
    updatePaginationButtons();
});
