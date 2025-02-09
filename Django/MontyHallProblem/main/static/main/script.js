
doors = [false,false,false]
doorVisibility = [true,true,true]
gameStage = 1

doors[parseInt(Math.random()*3)] = true

document.getElementById("slot1").innerHTML = doors[0]? "Sports Car" : "Goat"
document.getElementById("slot2").innerHTML = doors[1]? "Sports Car" : "Goat"
document.getElementById("slot3").innerHTML = doors[2]? "Sports Car" : "Goat"

document.getElementById("door1").addEventListener("click", () => {
    doorClicked(0)
})
document.getElementById("door2").addEventListener("click", () => {
    doorClicked(0)
})
document.getElementById("door3").addEventListener("click", () => {
    doorClicked(2)
})

function doorClicked(doorClicked){ // doorClicked is an index
    console.log(doorClicked);
    //hello
    if(gameStage == 1){
        goatDoor = 0 //is an index
        for(var i = 0; i < doors.length;i++){
            if(doorClicked == i){
                continue
            }

            if(!doors[i]){
                goatDoor = i
                break
            }
        }
        document.getElementById("door" + (goatDoor+1)).innerText=""
        doorVisibility[goatDoor] = false
        document.getElementById("door" + (goatDoor+1)).style.backgroundColor = "transparent"
        document.getElementById("prompField").innerText = "Wait, you clicked on door " + (doorClicked+1) + " but door " + (goatDoor+1) + " has a goat behind it. Do you want to stay with door " + (doorClicked+1) + " or switch to the other free door?"
        gameStage = 2
    } else if (gameStage == 2 && doorVisibility[doorClicked]){
        for(var i = 0; i < doors.length; i++){
            document.getElementById("door" + (i+1)).innerText=""
            document.getElementById("door" + (i+1)).style.backgroundColor = "transparent"
        }
        if(document.getElementById("slot" + (doorClicked+1)).innerText == "Sports Car"){
            document.getElementById("prompField").innerText = "Congrats, you won the sports car!"

        } else {
            document.getElementById("prompField").innerText = "That sucks; you got the goat :("
        }

        gameStage = 3
    }
}
