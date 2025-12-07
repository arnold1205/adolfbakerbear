document.addEventListener("DOMContentLoaded", () => {
  // Countdown 2030
  const countdownEl = document.getElementById("countdown");
  const target = new Date("Jan 1, 2030 00:00:00").getTime();
  setInterval(() => {
    const now = new Date().getTime();
    const distance = target - now;
    const days = Math.floor(distance / (1000*60*60*24));
    const hours = Math.floor((distance % (1000*60*60*24)) / (1000*60*60));
    countdownEl.innerHTML = `${days} days and ${hours} hours left`;
  }, 1000);

  // Niveles del horno (mock – luego lo conectas a DexScreener)
  const container = document.getElementById("oven-levels-container");
  const levels = [
    {size:128, cookies:10,   req:"$0 – $10k"},
    {size:160, cookies:100,  req:"$10k – $50k"},
    {size:192, cookies:500,  req:"$50k – $250k"},
    {size:224, cookies:2000, req:"$250k – $1M"},
    {size:288, cookies:10000,req:"$1M+"}
  ];

  container.innerHTML = levels.map((lvl, i) => `
    <div class="text-center">
   <div class="rounded-full overflow-hidden shadow-2xl border-8 ${i===0?'border-orange-400 ring-8 ring-orange-500 ring-opacity-70':'border-gray-700'}"
        style="width:${lvl.size}px;height:${lvl.size}px">
     <img src="/static/img/oven.png" class="w-full h-full object-cover ${i===0?'opacity-100':'opacity-30'}">
   </div>
   <p class="mt-6 text-3xl fredoka ${i===0?'text-orange-300':'text-gray-500'}">
     Level ${i+1}<br><span class="text-lg">${lvl.req}</span><br>
     <span class="text-2xl text-amber-300">${lvl.cookies} cookies/day</span>
   </p>
 </div>`).join("");
});