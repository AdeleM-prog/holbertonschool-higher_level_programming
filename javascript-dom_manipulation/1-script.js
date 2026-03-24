#!/usr/bin/node

const button = document.querySelector("#red_header");

button.addEventListener("click", function() {
    const header = document.querySelector("header");
    header.style.color = "#FF0000";
});