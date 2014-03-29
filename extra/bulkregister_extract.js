var domains = "";

$('#ctl00_Main_ctl01_pnlResults tr td:nth-child(2) a').each(function(){
        domains += $(this).text() + '\n';
});

console.log(domains);
