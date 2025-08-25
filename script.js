/* Elements */
const chatWindow  = document.getElementById("chat-window");
const chatForm    = document.getElementById("chat-form");
const msgInput    = document.getElementById("message-input");
const hiddenSelect= document.getElementById("lang-select");
const entrance    = document.getElementById("entrance");
const enterAvatar = document.getElementById("enter-avatar");
const enterText   = document.getElementById("enter-text");
const suggestionBar = document.getElementById("suggestion-bar");

/* pill switch elements */
const langButtons = document.querySelectorAll(".lang-switch button");
const slider      = document.querySelector(".lang-switch .slider");

const API_URL="https://ph4z1v4c5f.execute-api.us-east-1.amazonaws.com/prod/chat";

/* sample Qs */
const SAMPLES={
  en:["What are the admission dates?","What documents are required for admission?","What is the KG1 fee?","What is Grade 7 fees?","What are the school timings?","Tell me about school bus service.","When is the academic calendar?","Who is the principal?"],
  ar:["ما هي مواعيد القبول؟","ما المستندات المطلوبة للتسجيل؟","ما رسوم مرحلة KG1؟","ما رسوم الصف السابع؟","ما مواعيد الدوام المدرسي؟","حدثني عن خدمة الحافلات المدرسية.","متى التقويم الأكاديمي؟","من هو مدير المدرسة؟"]
};

/* state */
let currentLang="en";

/* helpers */
const append=(txt,who="bot")=>{
  const d=document.createElement("div");
  d.className=`message ${who}`;d.textContent=txt;
  chatWindow.appendChild(d);chatWindow.scrollTop=chatWindow.scrollHeight;
};
const loadPills=()=>{
  suggestionBar.innerHTML="";
  SAMPLES[currentLang].forEach(q=>{
    const b=document.createElement("button");
    b.textContent=q;b.onclick=()=>send(q);suggestionBar.appendChild(b);
  });
};
const syncUI=()=>{
  enterText.innerHTML=currentLang==="ar"?"مرحباً<br>أنا نواي":"Hello<br> How can I help you?";
  msgInput.placeholder=currentLang==="ar"?"اكتب رسالتك...":"Type a message…";
  loadPills();
  /* toggle pill state */
  langButtons.forEach(btn=>btn.classList.toggle("active",btn.dataset.lang===currentLang));
  slider.style.transform=currentLang==="ar"?"translateX(100%)":"translateX(0)";
  hiddenSelect.value=currentLang; // keep hidden <select> in sync
};

/* send */
async function send(msg){
  append(msg,"user");msgInput.value="";msgInput.focus();
  try{
    const r=await fetch(API_URL,{method:"POST",headers:{"Content-Type":"application/json"},body:JSON.stringify({message:msg,language:currentLang})});
    if(!r.ok)throw new Error();
    const {response}=await r.json();append(response,"bot");
  }catch{
    append(currentLang==="ar"?"حدث خطأ ما. حاول مرة أخرى.":"😞 Something went wrong. Please try again.");
  }
}

/* events */
chatForm.addEventListener("submit",e=>{e.preventDefault();const t=msgInput.value.trim();if(t)send(t);});
langButtons.forEach(btn=>btn.addEventListener("click",()=>{
  currentLang=btn.dataset.lang;syncUI();
}));
enterAvatar.addEventListener("click",()=>{
  entrance.classList.add("fade-out");
  setTimeout(()=>entrance.style.display="none",300);
  append(currentLang==="ar"?"مرحباً! كيف يمكنني مساعدتك اليوم؟":"Hello! How can I help you today?");
  loadPills();msgInput.focus();
});

/* init */
syncUI();
