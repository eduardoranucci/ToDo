$(document).ready(function() {

    let baseUrl = window.location.origin;
    let deleteBtn = $('.delete-btn');
    let searchBtn = $('#search-btn');
    let searchForm = $('#search-form');
    let filter = $('#filter');

    $(deleteBtn).on('click', function(event) {

        event.preventDefault();

        let delLink = $(this).attr('href');
        let result = confirm('Confirmar exclusão?');

        if(result) {
            window.location.href = delLink;
        }

    });

    $(searchBtn).on('click', function() {
        searchForm.submit();
    });

    $(filter).change(function() {
        let filter = $(this).val();
        window.location.href = baseUrl + '?filter=' + filter;
    });

});