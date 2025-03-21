document.addEventListener("DOMContentLoaded", function () {
    // Aボタン（Cを選択）
    document.getElementById("button-A").addEventListener("click", function () {
        selectOptionAndSubmit(this.dataset.value);
    });

    // Bボタン（Dを選択）
    document.getElementById("button-B").addEventListener("click", function () {
        selectOptionAndSubmit(this.dataset.value);
    });

    function selectOptionAndSubmit(value) {
        // 対応するラジオボタンを選択
        let radioButton = document.querySelector(
            `input[type="radio"][value="${value}"]`
        );
        if (radioButton) {
            radioButton.checked = true;
        }

        // Next ボタンをクリック
        document.getElementById("next-button").click();
    }
});
