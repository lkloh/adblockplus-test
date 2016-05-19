window.addEventListener("load", function load(event){
    wait(3000);
    SubscriptionActions.remove();
    wait(3000);
    SubscriptionActions.remove();
    alert("a forum page is loaded");
    window.removeEventListener("load", load, false); //remove listener, no longer needed
},false);