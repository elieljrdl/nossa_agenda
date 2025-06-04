document.addEventListener('DOMContentLoaded', function () {
  const exampleModal = document.getElementById('exampleModal');

  if (exampleModal) {
    $('#exampleModal').on('show.bs.modal', function (event) {
      const botao = $(event.relatedTarget);
      const dia = botao.data('dia').toString().padStart(2, '0');
      const mes = botao.data('mes').toString().padStart(2, '0');
      const ano = botao.data('ano');
      const dataFormatada = `${ano}-${mes}-${dia}`;
      $(this).find('#data').val(dataFormatada);
    });
  }

  const myModal = document.getElementById('myModal');
  const myInput = document.getElementById('myInput');

  if (myModal && myInput) {
    myModal.addEventListener('shown.bs.modal', () => {
      myInput.focus();
    });
  }
});