$(document).on('submit','#guestform',function(e){
        e.preventDefault();

        $.ajax({


            type:'POST',
            async:false,
            url:'{% url "gp" %}',
            data:
            {
                name:$("#id_Author").val(),

                email:$("#id_email").val(),
                title:$("#id_title").val(),
                excerpt:$("#id_excerpt").val(),
                content:$("#id_content").val(),
                csrfmiddlewaretoken:$('input[name=csrfmiddlewaretoken]').val(),


            },
            success:function(){
                setTimeout(() => {
                  document.location.reload();
                }, 4000);

                    }
            })
        });