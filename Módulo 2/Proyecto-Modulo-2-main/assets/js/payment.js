$(document).ready(function() {
    $('#paymentHistoryForm').on('submit', function(event) {
        event.preventDefault();
        let student = $('#selectHistoryStudent').val();

        // Simulación de historial de pagos
        let paymentHistory = `
            <h4>Historial de Pagos</h4>
            <p>Estudiante: ${student}</p>
            <table class="table">
                <thead>
                    <tr>
                        <th>Concepto</th>
                        <th>Monto</th>
                        <th>Fecha de Pago</th>
                    </tr>
                </thead>
                <tbody>
                    <tr>
                        <td>Inscripción</td>
                        <td>$1000</td>
                        <td>01/01/2024</td>
                    </tr>
                    <!-- Más filas de historial aquí -->
                </tbody>
            </table>
        `;
        $('#paymentHistory').html(paymentHistory);
    });
});
