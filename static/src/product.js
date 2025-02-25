/** @odoo-module **/
$(document).ready(function () {
    let fechaPreventa = $("#is_preventa").attr("data-preventa");

    if (fechaPreventa && fechaPreventa !== "False") {
        $("#preventaFecha").text(fechaPreventa);
        $("#preventaModal").modal("show");
    }

    // Delegación de eventos para asegurar que el botón funcione
    $(document).on("click", "#preventaModal .btn-secondary", function () {
        $("#preventaModal").modal("hide");
    });
});
