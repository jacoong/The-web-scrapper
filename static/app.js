
const index_submit_button = document.querySelector(".index_submit_button");
const index_loading_button = document.querySelector(".index_loading_button");



function loading(){
    index_submit_button.classList.add("hidden");
    index_loading_button.classList.remove("hidden");
}

function main(){
    location.href = "/";
    index_submit_button.classList.remove("hidden");
    index_loading_button.classList.add("hidden");

}




index_submit_button.addEventListener("click",loading);

