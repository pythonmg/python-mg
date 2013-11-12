selecionaMenu = function(nome_menu){
    $('.menu').children().each(function(){
      if($(this).hasClass(nome_menu)){
        $(this).addClass('selected_menu');
        return;
      }
    });
  };