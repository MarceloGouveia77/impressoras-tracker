// REMOVE O CONTEUDO DO MODAL APÓS SER FECHADO
$(document).on('hidden.bs.modal', function (e) {
    var target = $(e.target);
    target.removeData('bs.modal')
          .find(".modal-content").html('');
});

// MODAL PARA EDITAR E INSERIR NOVOS DADOS
$('.openPopup').on('click', function () {
    var dataURL = $(this).attr('data-href');
    $('.modal-content').load(dataURL, function () {
        $('#statusModal').modal({ show: true });
    });
});