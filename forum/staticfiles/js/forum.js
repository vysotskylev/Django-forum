$(function(){
    var $cont = $("#message_container"),
        $messageTo = $('#messageTo'),
        $form = $('#message_form');
    
    $cont.on('click', 'button', function(e){
        var $t = $(e.target);
        $messageTo.html('Add your reply to ' + $t.attr('by') + ':');
        $t.parents('.panel').after($form);
        $form.find('[name=to]').attr('value', $t.attr('by'));
    });


});
