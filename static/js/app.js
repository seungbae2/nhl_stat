
// var svg = d3.select("#chart")
//     .append("svg")


d3.json("static/data/result.json").then(function(data){
    console.log(data)
});

d3.json("static/data/game_stat.json").then(function(data){
    console.log(data)
});