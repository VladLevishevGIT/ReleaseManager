//indicates whether the mouse over tooltip
var hover = false;
var a=0;
//for convenience
var $TT = $('#dropdownMenu li');
$TT.tooltip({
    selector: "a[rel=tooltip]",
    placement: "right"
})
$('body').on('mouseenter', '.tooltip,a[rel=tooltip]', function () {
    hover = true;
})
$('a').on('mouseenter', function() {
    hover=false;
    $('.tooltip').hide();
})
//if it is true hover prevents the tooltip close
$TT.on('hide.bs.tooltip', function () {
    return !hover;
})