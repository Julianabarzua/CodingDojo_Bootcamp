var player = {
    left: 262,
    top: 600
}

var enemies = [
    {left: 25, top: 100},
    {left: 125, top: 50},
    {left: 225, top: 100},
    {left: 325, top: 50},
    {left: 425, top: 100}
]

var missiles = []

function drawPlayer() {
    content = "<div class='player' style='left: "+player.left+"px; top: "+player.top+"px'></div>";
    document.getElementById("players").innerHTML = content;
}

function drawEnemies() {
    content = ""
    for (var idx=0;idx<enemies.length; idx++) {
        content += "<div class='enemy' style='left: "+enemies[idx].left+"px; top: "+enemies[idx].top+"px'></div>";
    }
    document.getElementById("enemies").innerHTML = content
}

function moveenemies(){
    for(var idx=0; idx<enemies.length; idx++){
        enemies[idx].top += 1;
        if(enemies[idx].top >730){
            enemies.splice(idx,1);
            alert("YOU LOST!, WANT TO RESTART?")
            restart()
        }
    }
}

function moveMissiles(){
    for(var idx=0; idx<missiles.length; idx++){
        missiles[idx].top -= 6 ;
    }
}

function drawMissiles(){
    content = "";
    for(var idx=0; idx<missiles.length;idx++){
        content +="<div class='missile' style='left:"+missiles[idx].left+"px; top:"+missiles[idx].top+"px'></div>" 
    }
    document.getElementById("missiles").innerHTML = content;
}

function restart(){

    player = {
        left: 262,
        top: 600
    }
    
    enemies = [
        {left: 25, top: 100},
        {left: 125, top: 50},
        {left: 225, top: 100},
        {left: 325, top: 50},
        {left: 425, top: 100}
    ]
    
    missiles = []

}

function gameloop(){
    console.log("gameloop is running");
    drawPlayer();
    moveenemies();
    moveMissiles();
    drawEnemies();
    drawMissiles();

    setTimeout(gameloop, 20)  ;
}


gameloop();


document.onkeydown = function(e){
    if(e.keyCode ==37){ //LEFT
        if(player.left-10>-30){
            player.left = player.left - 10;
        }
    }
    if(e.keyCode ==38){ //UP
        if(player.top-10>600){
            player.top = player.top - 10;
        }
    }
    if(e.keyCode ==39){ //RIGHT
        if(player.left < 555){
            player.left = player.left + 10;
        }
    }
    if(e.keyCode ==40){ //DOWN
        if (player.top+10<750){
            player.top = player.top + 10;
        }
    }
    if(e.keyCode == 32){  //FIRE
        missiles.push({left: (player.left+50), top:(player.top+30)})
        drawMissiles();
    }

    drawPlayer()

}
