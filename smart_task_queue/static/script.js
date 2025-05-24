// Función para mostrar tareas desde backend
async function mostrarTareas() {
    const response = await fetch('/queues');
    if (!response.ok) {
        console.error("Error al obtener las tareas");
        return;
    }
    const data = await response.json();

    document.getElementById("tareas-alta").innerHTML = data.Alta.map(t => `<p>${t} <button class="button-form" onclick="eliminarTarea('Alta', '${t.replace(/'/g, "\\'")}')">Eliminar</button></p>`).join("");
    document.getElementById("tareas-media").innerHTML = data.Media.map(t => `<p>${t} <button class="button-form" onclick="eliminarTarea('Media', '${t.replace(/'/g, "\\'")}')">Eliminar</button></p>`).join("");
    document.getElementById("tareas-baja").innerHTML = data.Baja.map(t => `<p>${t} <button class="button-form" onclick="eliminarTarea('Baja', '${t.replace(/'/g, "\\'")}')">Eliminar</button></p>`).join("");
}

// Evento submit del formulario para enviar tarea y actualizar vista
document.getElementById("formulario-tarea").addEventListener("submit", async function (e) {
    e.preventDefault();
    const input = document.getElementById("inputTarea");
    const texto = input.value.trim();
    if (!texto) return;

    const response = await fetch('/add-task', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ task: texto })
    });

    const data = await response.json();

    if (response.ok) {
        input.value = "";
        await mostrarTareas();
    } else {
        alert("Error: " + data.error);
    }
});

// Función para eliminar tarea
async function eliminarTarea(prioridad, tarea) {
    Swal.fire({
        title: "Estas seguro?",
        text: "No podra revertirse!",
        icon: "warning",
        showCancelButton: true,
        confirmButtonColor: "#3085d6",
        cancelButtonColor: "#d33",
        confirmButtonText: "Eliminar",
        cancelButtonText: "Cancelar"
    }).then(async (result) => {
        if (result.isConfirmed) {
            // Llamada para eliminar la tarea
            const response = await fetch('/remove-task', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ priority: prioridad, task: tarea })
            });
            const data = await response.json();

            if (data.error) {
                Swal.fire("Error", data.error, "error");
            } else {
                Swal.fire("Eliminado!", "Se a eliminado tu tarea con exito", "success");
                mostrarTareas(); // refrescar lista
            }
        }
    });
}

// Mostrar tareas al cargar la página
window.onload = mostrarTareas;

// Animación de ojos siguiendo el mouse
document.addEventListener('mousemove', (e) => {
    const eyes = document.querySelectorAll('.eye');
    eyes.forEach(eye => {
        const pupil = eye.querySelector('.pupil');
        const rect = eye.getBoundingClientRect();
        const eyeX = rect.left + rect.width / 2;
        const eyeY = rect.top + rect.height / 2;

        const angle = Math.atan2(e.clientY - eyeY, e.clientX - eyeX);
        const x = Math.cos(angle) * (rect.width / 6);
        const y = Math.sin(angle) * (rect.height / 6);

        pupil.style.transform = `translate(calc(-50% + ${x}px), calc(-50% + ${y}px))`;
    });
});

const clip = document.querySelector('.clip');
const expressions = ["surprised", "angry", "sad", "confused", "excited", "curious", "raise-right"];

let isDancing = false;

function setExpression(expression) {
    if (!clip.classList.contains(expression) && !isDancing) {
        clip.classList.remove("neutral", ...expressions);
        clip.offsetHeight; // reflow

        // Control específico para ceja derecha en 'raise-right'
        const rightEyebrow = clip.querySelector('.eyebrow.right');
        rightEyebrow.classList.remove('raise-right');

        if (expression === "raise-right") {
            rightEyebrow.classList.add('raise-right');
            clip.classList.add('neutral'); // clip no tiene otras animaciones
        } else {
            clip.classList.add(expression);
        }

        setTimeout(() => {
            clip.classList.remove(expression);
            rightEyebrow.classList.remove('raise-right');
            clip.classList.add("neutral");
        }, 800);
    }
}

function resetExpression() {
    clip.classList.remove(...expressions);
    const rightEyebrow = clip.querySelector('.eyebrow.right');
    rightEyebrow.classList.remove('raise-right');
    clip.offsetHeight;
    clip.classList.add("neutral");
}

function randomExpression() {
    if (!isDancing) {
        const expression = expressions[Math.floor(Math.random() * expressions.length)];
        setExpression(expression);
        setTimeout(resetExpression, 2000);
    }
}

function loopExpressions() {
    randomExpression();
    const nextDelay = Math.random() * 4000 + 4000;
    setTimeout(loopExpressions, nextDelay);
}

clip.classList.add('neutral');
loopExpressions();

// Bailar cuando se "habla" (click para activar/desactivar)
clip.addEventListener('click', () => {
    if (isDancing) {
        // Parar baile
        clip.classList.remove('dancing');
        isDancing = false;
        resetExpression();
    } else {
        // Empezar baile
        clip.classList.add('dancing');
        isDancing = true;
    }
});

// codigo mensajes bot
let demoInProgress = false;

function startDemo() {
    if (demoInProgress) return;
    demoInProgress = true;

    const clip = document.querySelector('.clip');
    const popup = document.getElementById('clippyPopup');

    const mensajes = [
        "¡Hola! Soy Clippy. Bienvenido a tu asistente inteligente.",
        "Aquí puedes crear tareas nuevas en el cuadro superior.",
        "Las tareas se clasifican automáticamente según su prioridad.",
        "Puedes verlas en las columnas: Alta, Media y Baja.",
        "intenta poner palabras como 'Urgente' o 'Importante' para tareas altas.",
        "para prioridad media, puedes usar 'repasar' o 'estudiar'.",
        "y para baja, palabras como 'revisar' o 'leer'.",
        "¡Y eso es todo! Vamos a mantenerte organizado 🧠✨"
    ];
    let index = 0;

    popup.style.display = 'block';
    clip.classList.add('dancing');
    clip.classList.remove('neutral');

    popup.textContent = mensajes[index];

    const interval = setInterval(() => {
        index++;
        if (index < mensajes.length) {
            popup.textContent = mensajes[index];
        } else {
            clearInterval(interval);
            clip.classList.remove('dancing');
            clip.classList.add('neutral');
            setTimeout(() => {
                popup.style.display = 'none';
                demoInProgress = false; // Permitir otra vez después de terminar
            }, 2000);
        }
    }, 3500);
}







