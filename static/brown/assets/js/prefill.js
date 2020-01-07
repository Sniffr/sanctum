var stuff;
var email_input = $("#id_email");
stuff = window.localStorage.getItem('mail');

function fillinput() {
     if (stuff){
         email_input.val(stuff);
         window.localStorage.removeItem('mail')
     }
};

fillinput();