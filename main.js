let url = "./logs.json"
let command;
let latest_time; //undefined
await fetch(url)
   .then((response) => {
       return response.json(); //ここでBodyからJSONを返す
   })
   .then((result) => {
    const latestCommand = result.reduce((latest, current) => {
        const latestTime = new Date(latest.time);
        const currentTime = new Date(current.time);
      
        return latestTime > currentTime ? latest : current;
      }, result[0]); 
    command = latestCommand ? (latestCommand.command) : ("コード");
    console.log(command);
   })
let elem = document.getElementById("text");
elem.textContent = `飲酒🍺${command}は`;
