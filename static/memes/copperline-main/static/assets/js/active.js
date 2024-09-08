$(document).ready(function(){
    $('#logReport, #SourceInstance, #MappingTable').DataTable({
        "searching": false,
        "dom": 'rtip',
        "pageLength": 5,
    });

    $('#purches_Datatable').DataTable({
        "searching": false,
        paging: false,
        info: false,
    });

});