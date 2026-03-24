#!/usr/bin/node

const add_item = document.querySelector("#add_item");

add_item.addEventListener("click", function () {
    const li = document.createElement("li");
    li.textContent = "Item";
    const my_list = document.querySelector(".my_list");
    my_list.appendChild(li);
})