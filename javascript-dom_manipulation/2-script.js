#!/usr/bin/node

const elmt = document.querySelector("#red_header");

elmt.addEventListener("click", function () {
    const header = document.querySelector("header");
    header.classList.add("red");
})