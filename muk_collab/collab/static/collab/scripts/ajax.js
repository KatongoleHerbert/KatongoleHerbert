/**
 * Created by lucy on 4/3/2018.
 */

$(function()
{
    $('#search').keyup(function () {
        $.ajax({
            type: 'GET',
            url: '/book/',
            data: {
                'search_text' : $('#search').val()
            },
            success: searchSuccess,
            dataType: 'html'
        });

    });

});

function searchSuccess(data, textStatus, jqXHR)
{
    $('#search-results').html(data);

}
