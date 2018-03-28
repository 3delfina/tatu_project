$('.comment-button').click(function() {
    $.post('/update',{
        what:'comment',
        id:$(this).data('id'),
        comment:$('#comment-text').val(),
        csrfmiddlewaretoken: document.getElementsByName('csrfmiddlewaretoken')[0].value
    },function(data) {
        if(data.status=="success") {
            //put in the right values from the data into the html string and append it
            var html = '<p><a href=\'{% url \'profile\' '+data.id+' %}\'><img class="img-circle"  src="{{ com.poster.avatar.url }}" alt="fuc" width="30"height="30"></a>{{com.poster}} says : {{com.text}}</p><br>';
            $('.talk').append(html);
        } else {
            alert('error posting a comment');
        }
    });
});

$('.like-button').click(function() {
    var elem = $(this);
    $.post('/update',{
        what:'like',
        id:elem.data('id'),
        csrfmiddlewaretoken: document.getElementsByName('csrfmiddlewaretoken')[0].value
    },function(data) {
        if(data=="liked"){
            $('.likes').empty().append('Likes : '+Number.parseInt(elem.data('num'))+1);            
        } else if (data=="unliked") {
            $('.likes').empty().append('Likes : '+Number.parseInt(elem.data('num'))-1);                        
        } else {
            alert('There is problem liking the post');
        }
    });
});