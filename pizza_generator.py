# Let's generate a highly functional, beautifully styled HTML calculator application.
# It will embed the exact logic, ingredients, and 22°C poolish timeline we just established,
# while dynamically adjusting the weights and times based on the user's input toggles/sliders.

html_app = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Dynamic Poolish Pizza Calculator</title>
    <style>
        :root {
            --bg-color: #f4f6f9;
            --card-bg: #ffffff;
            --primary: #1a252f;
            --accent: #d35400;
            --text-main: #2c3e50;
            --text-muted: #7f8c8d;
            --border: #dcdde1;
        }
        * { box-sizing: border-box; margin: 0; padding: 0; font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; }
        body { background-color: var(--bg-color); color: var(--text-main); padding: 20px; line-height: 1.6; }
        .wrapper { max-width: 1000px; margin: 0 auto; }
        header { background: var(--primary); color: #fff; padding: 30px; border-radius: 8px 8px 0 0; text-align: center; border-bottom: 5px solid var(--accent); }
        header h1 { font-size: 24px; text-transform: uppercase; letter-spacing: 1px; margin-bottom: 5px; }
        header p { color: #bdc3c7; font-style: italic; font-size: 14px; }
        
        .main-layout { display: grid; grid-template-columns: 1fr; gap: 20px; margin-top: 20px; }
        @media (min-width: 768px) { .main-layout { grid-template-columns: 350px 1fr; } }
        
        .panel { background: var(--card-bg); padding: 25px; border-radius: 8px; box-shadow: 0 4px 6px rgba(0,0,0,0.05); height: fit-content; }
        .panel h2 { font-size: 16px; text-transform: uppercase; color: var(--primary); margin-bottom: 20px; border-bottom: 2px solid var(--border); padding-bottom: 5px; }
        
        .control-group { margin-bottom: 20px; }
        .control-group label { display: block; font-weight: 600; font-size: 13px; margin-bottom: 8px; text-transform: uppercase; color: var(--text-main); }
        .control-group input[type="range"], .control-group input[type="time"], .control-group select { width: 100%; padding: 10px; border: 1px solid var(--border); border-radius: 4px; font-size: 14px; background: #fff; }
        .val-display { float: right; color: var(--accent); font-weight: bold; }
        
        .results-area { display: flex; flex-direction: column; gap: 20px; }
        .card { background: var(--card-bg); padding: 25px; border-radius: 8px; box-shadow: 0 4px 6px rgba(0,0,0,0.05); }
        .card h2 { font-size: 16px; text-transform: uppercase; color: var(--primary); margin-bottom: 15px; border-bottom: 2px solid var(--accent); padding-bottom: 5px; }
        
        .ingredients-grid { display: grid; grid-template-columns: 1fr; gap: 15px; }
        @media (min-width: 480px) { .ingredients-grid { grid-template-columns: 1fr 1fr; } }
        .ing-box { background: #f8f9fa; border-left: 4px solid var(--primary); padding: 15px; border-radius: 0 4px 4px 0; }
        .ing-box.accent-box { border-left-color: var(--accent); background: #fffaf0; }
        .ing-box h3 { font-size: 13px; text-transform: uppercase; margin-bottom: 8px; color: var(--text-main); }
        .ing-box ul { list-style: none; }
        .ing-box li { font-size: 14px; margin-bottom: 5px; display: flex; justify-content: space-between; }
        .ing-box li span { font-weight: bold; color: var(--accent); }
        
        .timeline { position: relative; padding-left: 20px; border-left: 2px solid var(--border); margin-top: 15px; }
        .timeline-step { position: relative; margin-bottom: 25px; }
        .timeline-step::before { content: ''; position: absolute; left: -26px; top: 4px; width: 10px; height: 10px; border-radius: 50%; background: var(--accent); border: 2px solid #fff; box-shadow: 0 0 0 2px var(--accent); }
        .time-tag { display: inline-block; background: var(--primary); color: #fff; font-size: 11px; font-weight: bold; padding: 2px 6px; border-radius: 3px; margin-bottom: 5px; }
        .step-title { font-weight: bold; font-size: 14px; color: var(--primary); margin-left: 5px; }
        .step-desc { font-size: 13.5px; color: #34495e; margin-top: 4px; }
        
        .tip-box { background: #eef9ff; border-left: 4px solid #3498db; padding: 15px; font-size: 13px; border-radius: 4px; margin-top: 15px; }
        
        /* Print Styles */
        @media print {
            body { background: #fff; padding: 0; font-size: 11px; color: #000; }
            .panel, .print-btn { display: none !important; }
            .main-layout { display: block; margin-top: 0; }
            .results-area { display: grid; grid-template-columns: 280px 1fr; gap: 15px; align-items: start; }
            .wrapper { max-width: 100%; margin: 0; }
            header { background: #fff !important; color: #000 !important; border-bottom: 1px solid #000; padding: 5px 0; text-align: left; }
            header h1 { font-size: 18px; margin-bottom: 2px; }
            header p { font-size: 11px; color: #555 !important; }
            .card { box-shadow: none; border: 1px solid #eee; margin-bottom: 0; padding: 12px; page-break-inside: avoid; }
            .card h2 { border-bottom: 1px solid #000; color: #000; font-size: 14px; margin-bottom: 8px; padding-bottom: 2px; }
            .ingredients-grid { display: block; }
            .ing-box { background: #fff !important; border: 1px solid #ddd; border-left: 3px solid #000; padding: 8px; margin-bottom: 8px; }
            .ing-box h3 { font-size: 11px; margin-bottom: 4px; }
            .ing-box li { font-size: 11px; margin-bottom: 2px; }
            .ing-box li span { color: #000 !important; }
            .timeline { padding-left: 15px; margin-top: 5px; border-left: 1px solid #ddd; }
            .timeline-step { margin-bottom: 12px; }
            .timeline-step::before { content: ''; position: absolute; left: -20px; top: 4px; width: 8px; height: 8px; background: #000; border: none; box-shadow: none; }
            .time-tag { background: #000 !important; color: #fff !important; font-size: 9px; padding: 1px 4px; }
            .step-title { font-size: 12px; color: #000; }
            .step-desc { font-size: 10.5px; color: #333; margin-top: 2px; line-height: 1.3; }
            .tip-box { background: #fff !important; border: 1px solid #ccc; color: #000; padding: 8px; font-size: 10px; margin-top: 10px; }
            @page { margin: 0.8cm; }
        }
        
        .print-btn { 
            background: var(--accent); color: white; border: none; padding: 12px 20px; 
            border-radius: 4px; cursor: pointer; font-weight: bold; width: 100%; 
            margin-top: 10px; text-transform: uppercase; font-size: 14px;
        }
        .print-btn:hover { background: #a04000; }
    </style>
</head>
<body>

<div class="wrapper">
    <header>
        <h1>Ooni Pizza Masterclass Calculator</h1>
        <p>Interactive Poolish Workflow & Timeline Engine</p>
    </header>

    <div class="main-layout">
        <!-- CONTROLS PANEL -->
        <div class="panel">
            <h2>Tweak Parameters</h2>
            
            <div class="control-group">
                <label>Number of Pizzas <span class="val-display" id="qty-val">6</span></label>
                <input type="range" id="pizza-qty" min="1" max="20" value="6" step="1">
            </div>

            <div class="control-group">
                <label>Ambient Kitchen Temp <span class="val-display" id="temp-val">22°C</span></label>
                <input type="range" id="kitchen-temp" min="16" max="30" value="22" step="1">
            </div>

            <div class="control-group">
                <label>Target Dinner Time</label>
                <input type="time" id="target-time" value="18:30">
            </div>

            <div class="control-group">
                <label>Type of Oven</label>
                <select id="oven-type">
                    <option value="high-heat" selected>High-Heat Pizza Oven (Ooni/Gozney)</option>
                    <option value="home-oven">Standard Kitchen Oven (with Steel/Stone)</option>
                </select>
            </div>

            <div class="control-group">
                <label>Flour Strength / Type</label>
                <select id="flour-type">
                    <option value="cuoco" selected>Caputo Cuoco (Red) / High Protein (13%+)</option>
                    <option value="pizzeria">Caputo Pizzeria (Blue) / Medium Protein (~12.5%)</option>
                </select>
            </div>

            <button class="print-btn" onclick="window.print()">Print Recipe</button>
        </div>

        <!-- RESULTS / CALCULATION AREA -->
        <div class="results-area">
            <!-- INGREDIENTS CARD -->
            <div class="card">
                <h2>Dynamic Ingredients Breakdown</h2>
                <div class="ingredients-grid">
                    <div class="ing-box">
                        <h3>Phase 1: Saturday Night Poolish</h3>
                        <ul>
                            <li>Flour (Caputo): <span id="p-flour">300g</span></li>
                            <li>Water (Room Temp): <span id="p-water">300g</span></li>
                            <li>Yeast (Active Dry): <span id="p-yeast">2.0g</span></li>
                        </ul>
                    </div>
                    <div class="ing-box">
                        <h3>Phase 2: Sunday Main Dough</h3>
                        <ul>
                            <li>Flour (Caputo): <span id="d-flour">600g</span></li>
                            <li>Water (Cold): <span id="d-water">285g</span></li>
                            <li>Fine Sea Salt: <span id="d-salt">25g</span></li>
                            <li id="oil-row" style="display:none;">Olive Oil: <span id="d-oil">0g</span></li>
                        </ul>
                    </div>
                </div>
                <div class="ingredients-grid" style="margin-top: 15px;">
                    <div class="ing-box accent-box" style="grid-column: 1 / -1;">
                        <h3>Grand Totals & Metrics</h3>
                        <ul style="display: grid; grid-template-columns: 1fr 1fr; gap: 10px;">
                            <li>Total Flour: <span id="t-flour">900g</span></li>
                            <li>Total Water: <span id="t-water">585g</span></li>
                            <li>Total Dough Weight: <span id="t-weight">1510g</span></li>
                            <li>Hydration Ratio: <span id="t-hyd">65%</span></li>
                        </ul>
                    </div>
                </div>
                <div class="tip-box" id="dynamic-warning">
                    <strong>Smart System Notification:</strong> Current temperature baseline (22°C) combined with Caputo Cuoco flour guarantees a safe, structured rise window.
                </div>
            </div>

            <!-- TIMELINE CARD -->
            <div class="card">
                <h2>Precision Timeline Schedule</h2>
                <div class="timeline">
                    <div class="timeline-step">
                        <div class="time-tag" id="time-step1">08:00 PM Sat</div>
                        <div class="step-title">Initialize Poolish Preferment</div>
                        <div class="step-desc">Mix all Phase 1 flour, water, and yeast in a large jar or container with a fork until smooth like pancake batter. Cover loosely.</div>
                    </div>
                    <div class="timeline-step">
                        <div class="time-tag" id="time-step2">08:05 PM Sat</div>
                        <div class="step-title">Ambient Bench Rest</div>
                        <div class="step-desc" id="desc-step2">Leave out on the kitchen counter for exactly 1.5 hours to kickstart fermentation active cells.</div>
                    </div>
                    <div class="timeline-step">
                        <div class="time-tag" id="time-step3">09:30 PM Sat</div>
                        <div class="step-title">The Cold Cold Brake</div>
                        <div class="step-desc">Seal container tightly and transfer to the refrigerator for an overnight slow cold fermentation (15-16 hours) to harvest complex flavors.</div>
                    </div>
                    <div class="timeline-step">
                        <div class="time-tag" id="time-step4">12:30 PM Sun</div>
                        <div class="step-title">Retrieve Poolish</div>
                        <div class="step-desc">Pull the poolish from the fridge. It should be highly active, domed, and covered with thousands of micro-bubbles.</div>
                    </div>
                    <div class="timeline-step">
                        <div class="time-tag" id="time-step5">12:45 PM Sun</div>
                        <div class="step-title">The Final Dough Integration</div>
                        <div class="step-desc" id="desc-step5">Dissolve poolish into the remaining cold water. Mix in half the remaining flour, add all the salt, then knead with the remaining flour for 10-12 minutes until matte and smooth. Shape into a large ball and cover for a 30-minute bench rest.</div>
                    </div>
                    <div class="timeline-step">
                        <div class="time-tag" id="time-step6">01:40 PM Sun</div>
                        <div class="step-title">Divide and Ball</div>
                        <div class="step-desc" id="desc-step6">Cut dough cleanly into equal balls (~250g each). Shape tightly and place into individual silicone containers smeared with a tiny wipe of oil. Seal the lids.</div>
                    </div>
                    <div class="timeline-step">
                        <div class="time-tag" id="time-step7">01:45 PM Sun</div>
                        <div class="step-title">The Crucial Final Proof Window</div>
                        <div class="step-desc" id="desc-step7">Leave silicone containers out on the counter. Based on your inputs, they will proof safely for 4.5 hours.</div>
                    </div>
                    <div class="timeline-step">
                        <div class="time-tag" id="time-step8">05:45 PM Sun</div>
                        <div class="step-title">Fire Up Your Oven</div>
                        <div class="step-desc" id="desc-step8">Ignite your Ooni 12" to maximum flame. Let the floor stone saturate with heat for a minimum of 45 minutes until it approaches 430°C-450°C.</div>
                    </div>
                    <div class="timeline-step">
                        <div class="time-tag" id="time-step9">06:30 PM Sun</div>
                        <div class="step-title">Stretch, Top & Launch!</div>
                        <div class="step-desc" id="desc-step9">Drop dough into a bowl of flour/semolina. Push gas to the rim. Stretch cleanly. Turn flame to LOW right before launching to bake without scorching edges. Turn every 15 seconds.</div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</div>

<script>
    // Elements
    const pizzaQty = document.getElementById('pizza-qty');
    const kitchenTemp = document.getElementById('kitchen-temp');
    const targetTime = document.getElementById('target-time');
    const ovenType = document.getElementById('oven-type');
    const flourType = document.getElementById('flour-type');

    // Display values
    const qtyVal = document.getElementById('qty-val');
    const tempVal = document.getElementById('temp-val');

    function parseTime(tStr) {
        let parts = tStr.split(':');
        return parseInt(parts[0]) * 60 + parseInt(parts[1]);
    }

    function formatTime(minutes, daySuffix = " Sun") {
        let mins = minutes;
        while (mins < 0) mins += 1440;
        mins = mins % 1440;
        let hours = Math.floor(mins / 60);
        let m = mins % 60;
        let ampm = hours >= 12 ? 'PM' : 'AM';
        let displayHours = hours % 12;
        displayHours = displayHours ? displayHours : 12; 
        let displayMins = m < 10 ? '0' + m : m;
        return `${displayHours}:${displayMins} ${ampm}${daySuffix}`;
    }

    function calculate() {
        const qty = parseInt(pizzaQty.value);
        const temp = parseInt(kitchenTemp.value);
        const oven = ovenType.value;
        const flour = flourType.value;
        const tTimeStr = targetTime.value;

        qtyVal.innerText = qty;
        tempVal.innerText = temp + "°C";

        // 1. INGREDIENT MATH (Baseline per ball is ~250g: 150g total flour, 97.5g total water, 4.1g salt)
        let singleFlour = 150;
        let hydration = 0.65;
        let singleSalt = 4.16;
        let singleYeast = 0.33; 

        // Adjustments based on oven
        let oilPercent = 0;
        if (oven === 'home-oven') {
            oilPercent = 0.025; // 2.5% oil for home ovens
        }

        let totFlour = singleFlour * qty;
        let totWater = Math.round(totFlour * hydration);
        let totSalt = Math.round(singleSalt * qty);
        let totYeast = (singleYeast * qty).toFixed(1);
        let totOil = Math.round(totFlour * oilPercent);

        // Poolish allocation (33.3% of flour)
        let poolishFlour = Math.round(totFlour * 0.3333);
        let poolishWater = poolishFlour; // 100% hydration poolish
        let poolishYeast = totYeast; // All yeast goes in poolish

        // Main dough remainder
        let mainFlour = totFlour - poolishFlour;
        let mainWater = totWater - poolishWater;

        // Render ingredients
        document.getElementById('p-flour').innerText = poolishFlour + "g";
        document.getElementById('p-water').innerText = poolishWater + "g";
        document.getElementById('p-yeast').innerText = poolishYeast + "g";

        document.getElementById('d-flour').innerText = mainFlour + "g";
        document.getElementById('d-water').innerText = mainWater + "g";
        document.getElementById('d-salt').innerText = totSalt + "g";
        
        if (totOil > 0) {
            document.getElementById('oil-row').style.display = 'flex';
            document.getElementById('d-oil').innerText = totOil + "g";
        } else {
            document.getElementById('oil-row').style.display = 'none';
        }

        document.getElementById('t-flour').innerText = totFlour + "g";
        document.getElementById('t-water').innerText = totWater + "g";
        document.getElementById('t-weight').innerText = (totFlour + totWater + totSalt + totOil) + "g (approx " + Math.round((totFlour + totWater + totSalt + totOil)/qty) + "g/ball)";

        // 2. TIMELINE DYNAMICS
        // Base timings backwards from target target dinner time (in minutes)
        let targetMins = parseTime(tTimeStr);
        
        // Final proof scaling factor based on temp
        // Baseline: 22C -> 4.5 hours final proof (270 mins). Every degree warmer speeds up by ~25 mins.
        let baseProofMins = 270;
        let tempDiff = temp - 22;
        let finalProofMins = baseProofMins - (tempDiff * 25);
        if (finalProofMins < 120) finalProofMins = 120; // safe floor limit
        if (finalProofMins > 420) finalProofMins = 420; // safe ceiling limit

        // Flour adjustments to proof window
        if (flour === 'pizzeria') {
            finalProofMins = Math.round(finalProofMins * 0.85); // Blue ferments faster/slackens quicker
        }

        let ovenPreheatMins = (oven === 'home-oven') ? 45 : 45;

        // Calculate back from dinner
        let step9_launch = targetMins;
        let step8_preheat = step9_launch - ovenPreheatMins;
        let step7_proofStart = step9_launch - finalProofMins;
        let step6_balling = step7_proofStart - 5;
        let step5_kneading = step6_balling - 40; // 10 min knead + 30 min rest
        let step4_retrieve = step5_kneading - 15;

        // Saturday timings (standard night before offsets)
        let step1_poolishStart = 1200; // 8:00 PM Sat static baseline matching your clean schedule
        let step2_ambientRest = step1_poolishStart + 5;
        let step3_coldBrake = step1_poolishStart + 90; // 1.5 hr jumpstart

        // Write times
        document.getElementById('time-step1').innerText = formatTime(step1_poolishStart, " Sat");
        document.getElementById('time-step2').innerText = formatTime(step2_ambientRest, " Sat");
        document.getElementById('time-step3').innerText = formatTime(step3_coldBrake, " Sat");
        document.getElementById('time-step4').innerText = formatTime(step4_retrieve, " Sun");
        document.getElementById('time-step5').innerText = formatTime(step5_kneading, " Sun");
        document.getElementById('time-step6').innerText = formatTime(step6_balling, " Sun");
        document.getElementById('time-step7').innerText = formatTime(step7_proofStart, " Sun");
        document.getElementById('time-step8').innerText = formatTime(step8_preheat, " Sun");
        document.getElementById('time-step9').innerText = formatTime(step9_launch, " Sun");

        // Dynamic Descriptions & Hints
        document.getElementById('desc-step7').innerText = `Leave the individual containers on your kitchen counter. At current ambient kitchen temperature (${temp}°C) and utilizing ${flour === 'cuoco' ? 'Caputo Red' : 'Caputo Blue'} flour, the dough balls require exactly ${Math.floor(finalProofMins/60)}h ${finalProofMins%60}m to hit peak relaxation.`;
        
        let warningBox = document.getElementById('dynamic-warning');
        if (temp >= 25) {
            warningBox.innerHTML = `<strong>⚠️ High Temperature Warning:</strong> At ${temp}°C, the ambient rise is heavily accelerated. Keep an eye on the dough balls at the 2-hour mark. If they double in size and flatten out prematurely, execute the <em>Emergency Fridge Brake</em> to slow them down.`;
            warningBox.style.background = "#fff0f0";
            warningBox.style.borderLeftColor = "#c0392b";
        } else if (flour === 'pizzeria' && temp >= 23) {
            warningBox.innerHTML = `<strong>💡 Flour Property Notice:</strong> You are using Caputo Pizzeria (Blue). This flour has a softer gluten network than the Red bag. Combined with your current room temp, do not let the final proof exceed the suggested calculation or the balls will turn flat and sticky.`;
            warningBox.style.background = "#fffaf0";
            warningBox.style.borderLeftColor = "#e67e22";
        } else {
            warningBox.innerHTML = `<strong>⭐ Smart System Notification:</strong> Conditions are optimal. Your combination of ${flour === 'cuoco' ? 'Caputo Cuoco (Red)' : 'Caputo Pizzeria (Blue)'} and a balanced room temperature of ${temp}°C will yield structural integrity with pristine leopard spotting.`;
            warningBox.style.background = "#eef9ff";
            warningBox.style.borderLeftColor = "#3498db";
        }
    }

    // Attach listeners
    [pizzaQty, kitchenTemp, targetTime, ovenType, flourType].forEach(el => {
        el.addEventListener('input', calculate);
        el.addEventListener('change', calculate);
    });

    // Run initial on load
    calculate();
</script>
</body>
</html>
"""

with open("pizza_calculator.html", "w") as f:
    f.write(html_app)
print("Interactive pizza web app successfully generated.")