$(function(){
    var $cont = $("#message_container"),
        $message = $('#message'),
        $form = $('#message_form');
    
    $cont.on('click', 'button', function(e){
        var $t = $(e.target);
        $message.attr('value', 'to ' + $t.attr('by') + ':');
        $t.parents('.panel').after($form);
        $form.find('#to').attr('value', $t.attr('by'));
    });


});
