async function sendQuery() {
  const input = document.getElementById("user-input").value.toLowerCase();
  const box = document.getElementById("chat-box");

  box.innerHTML += `<div><b>You:</b> ${input}</div>`;

  let response;

  if (input.includes("top 5")) {
    response = await fetch("/api/top-products").then(res => res.json());
  } else if (input.includes("order id")) {
    const id = input.match(/\d+/)?.[0];
    response = await fetch(`/api/order-status?order_id=${id}`).then(res => res.json());
  } else if (input.includes("stock") || input.includes("left")) {
    const product = input.replace("how many", "").replace("are left in stock", "").trim();
    response = await fetch(`/api/stock?product_name=${product}`).then(res => res.json());
  } else {
    response = { message: "I didn't understand that." };
  }

  box.innerHTML += `<div><b>Bot:</b> ${JSON.stringify(response)}</div>`;
  document.getElementById("user-input").value = "";
}
