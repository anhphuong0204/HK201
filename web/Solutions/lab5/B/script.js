var expr = '';
function addToExp() {
    var btn = event.target;
    var valueOfBtn = btn.innerHTML;

    if (['+', '-', '*', '/', '**'].find(ele => ele == valueOfBtn) == undefined) {
        expr += valueOfBtn;
    }
    else {
        if (['+', '-'].find(ele => ele == valueOfBtn) == undefined)
            expr = '(' + expr + ')' + valueOfBtn;
        else
            expr += valueOfBtn;
    }
    document.getElementById('exp').value = expr;
    
}

function evaluateIt() {
    document.getElementById('exp').value = eval(expr);
}