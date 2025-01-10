function onFormSubmit(e) {
    const response = e.values;
    //name and email as per the column nos. in your google sheet
    const name = response[1];  
    const email = response[2]; 
    sendJoke(name, email);
  }
  
function sendJoke(name, email) {
    const webhookURL = "https://jokes-automated.vercel.app/send-joke";
    const payload = {
      name: name,
      email: email
    };
    const options = {
      method: "POST",
      contentType: "application/json",
      payload: JSON.stringify(payload),
    };
    UrlFetchApp.fetch(webhookURL, options);
}