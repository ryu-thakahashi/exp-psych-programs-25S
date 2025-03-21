let description = document.getElementById("description");
function updateDescription(input) {
    let give = parseInt(input.value);
    let keep = js_vars.endowment - give;
    description.innerHTML = `グループに <strong id="give_points">${give}</strong> ポイントを与え，<br> <strong>${keep}</strong> ポイントをキープする.`;

    document.getElementById("id_contribution").value = give;
}

const submit_btn = document.getElementsByClassName("otree-btn-next")[0];
submit_btn.addEventListener("click", function () {});
