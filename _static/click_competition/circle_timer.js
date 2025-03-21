const parentCanvas = document.getElementById("timer");

function updateTimer(game_time, start_time) {
    const game_msec = game_time * 1000;
    let time_left = (game_msec + start_time - Date.now()) / 1000;

    if (time_left <= 0) {
        console.log("time is up!");
        time_left = 0;
    }

    clearCanvas();
    drawBaseCircle();
    drawTimerCircle(game_time, time_left);
    drawCenterWhiteCircle();
    addRemainingTimeText(time_left);
}

function drawBaseCircle() {
    parentCanvas.height = parentCanvas.width;

    const back_ctx = parentCanvas.getContext("2d");
    back_ctx.beginPath();

    let center_pos = parentCanvas.width / 2;
    back_ctx.moveTo(center_pos, center_pos); // 中心に移動

    let startAngle = 0;
    let endAngle = 2 * Math.PI;
    back_ctx.arc(center_pos, center_pos, center_pos, startAngle, endAngle); // 扇形の弧を描く
    back_ctx.closePath(); // パスを閉じる
    back_ctx.fillStyle = "gainsboro"; // 塗りつぶし色を設定
    back_ctx.fill(); // 塗りつぶしを実行
}

function drawTimerCircle(game_time, remainingTime) {
    const colored_timer_circle = parentCanvas.getContext("2d");
    colored_timer_circle.beginPath();

    let center_pos = parentCanvas.width / 2;
    colored_timer_circle.moveTo(center_pos, center_pos); // 中心に移動

    let formatted_remainingTime = remainingTime;
    let remainingTimePercentage = formatted_remainingTime / game_time;
    let startAngleItem = -2 * remainingTimePercentage + 3.5;
    let startAngle = startAngleItem * Math.PI;
    let endAngle = 3.5 * Math.PI;
    colored_timer_circle.arc(
        center_pos,
        center_pos,
        center_pos,
        startAngle,
        endAngle
    ); // 扇形の弧を描く
    colored_timer_circle.closePath(); // パスを閉じる
    colored_timer_circle.fillStyle = "#60A9FA"; // 塗りつぶし色を設定
    colored_timer_circle.fill(); // 塗りつぶしを実行
}

function drawCenterWhiteCircle() {
    // console.log("called drawCenterWhiteCircle!");

    const center_white_circle = parentCanvas.getContext("2d");
    center_white_circle.beginPath();

    let center_pos = parentCanvas.width / 2;
    center_white_circle.moveTo(center_pos, center_pos); // 中心に移動

    let radius = parentCanvas.width / 3;
    let startAngle = 0;
    let endAngle = 2 * Math.PI;
    center_white_circle.arc(
        center_pos,
        center_pos,
        radius,
        startAngle,
        endAngle
    );
    center_white_circle.closePath(); // パスを閉じる
    center_white_circle.fillStyle = "#fcfaf7"; // 塗りつぶし色を設定
    center_white_circle.fill(); // 塗りつぶしを実行
}

function addRemainingTimeText(left_sec) {
    // console.log("called addRemainingTimeText!");

    const time_text_front = parentCanvas.getContext("2d");

    let current_font_size = parentCanvas.width / 4;
    time_text_front.font = `bold ${current_font_size}px Arial`;
    time_text_front.textAlign = "center";
    time_text_front.textBaseline = "middle";
    time_text_front.fillStyle = "black";
    time_text_front.fillText(
        Math.floor(left_sec) + 1,
        parentCanvas.width / 2,
        parentCanvas.width / 2
    );
}

function clearCanvas() {
    const context = parentCanvas.getContext("2d");
    context.clearRect(0, 0, parentCanvas.width, parentCanvas.height);
}

function initTimer() {
    clearCanvas();
    drawBaseCircle();
    drawTimerCircle(200);
    drawCenterWhiteCircle();
    addRemainingTimeText(5);
}

let currentTimerId;
function startTimer(game_time, start_time) {
    if (currentTimerId !== null) {
        clearInterval(currentTimerId);
        currentTimerId = null;
    }

    initTimer();
    currentTimerId = setInterval(() => {
        updateTimer(game_time, start_time);
    }, 1000 / 60);
}

export { initTimer, startTimer };
