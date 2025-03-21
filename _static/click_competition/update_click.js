let clicks = 0;
document.getElementById("click_button").addEventListener("click", function () {
    clicks++;
    document.getElementById("click_count").innerText = clicks;
    liveSend({ click: true });
});

liveRecv(function (data) {
    console.log("リアルタイムデータ:", data); // デバッグ用

    if (!data || typeof data !== "object") {
        console.error("データ構造が不正です:", data);
        return; // データが壊れていたら処理を中断
    }

    let scoresList = document.getElementById("scores");
    let progressContainer = document.getElementById("progress_container");

    scoresList.innerHTML = "";
    progressContainer.innerHTML = "";

    let maxClicks = Math.max(...Object.values(data), 1); // 0だとNaNになるため1をデフォルト

    for (let [id, score] of Object.entries(data)) {
        let listItem = document.createElement("li");
        listItem.innerText = `プレイヤー ${id}: ${score} クリック`;
        if (parseInt(id) === playerId) {
            listItem.style.fontWeight = "bold"; // 自分のスコアを強調
        }
        scoresList.appendChild(listItem);

        let progressBarContainer = document.createElement("div");
        progressBarContainer.className = "progress-bar-container";

        let progressBar = document.createElement("div");
        progressBar.className = "progress-bar";
        progressBar.style.width = (score / maxClicks) * 100 + "%";

        let progressLabel = document.createElement("div");
        progressLabel.className = "progress-label";
        progressLabel.innerText = `プレイヤー ${id} - ${score} クリック`;

        progressBarContainer.appendChild(progressBar);
        progressBarContainer.appendChild(progressLabel);
        progressContainer.appendChild(progressBarContainer);
    }
});
