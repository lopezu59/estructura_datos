// Mostrar tareas desde el backend
async function mostrarTareas() {
    const response = await fetch('/queues');
    if (!response.ok) {
        console.error("Error al obtener las tareas");
        return;
    }

    const data = await response.json();

    // Limpiar contenedores primero
    document.getElementById("tareas-alta").innerHTML = "";
    document.getElementById("tareas-media").innerHTML = "";
    document.getElementById("tareas-baja").innerHTML = "";

    // Mostrar tareas en la sección correspondiente
    for (const prioridad in data) {
        data[prioridad].forEach(tarea => {
            const tareaHTML = `
                <p>
                    ${tarea}
                    <button class="button-form" onclick="confirmarEliminar('${prioridad}', '${tarea}')">❌</button>
                </p>
            `;
            document.getElementById(`tareas-${prioridad.toLowerCase()}`).innerHTML += tareaHTML;
        });
    }
}

// Agregar nueva tarea
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
        await mostrarTareas();  // Refrescar la vista
    } else {
        alert("Error: " + data.error);
    }
});

// Confirmar con SweetAlert y eliminar
function confirmarEliminar(prioridad, tarea) {
    Swal.fire({
        title: "¿Estás seguro?",
        text: "No podrás deshacer esto.",
        icon: "warning",
        showCancelButton: true,
        confirmButtonColor: "#3085d6",
        cancelButtonColor: "#d33",
        confirmButtonText: "Sí, eliminar"
    }).then((result) => {
        if (result.isConfirmed) {
            eliminarTarea(prioridad, tarea);
        }
    });
}

// Eliminar tarea del backend
function eliminarTarea(prioridad, tarea) {
    fetch('/remove-task', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ priority: prioridad, task: tarea })
    })
        .then(response => response.json())
        .then(data => {
            if (data.error) {
                Swal.fire("Error", data.error, "error");
            } else {
                Swal.fire("Eliminado", "La tarea fue eliminada", "success");
                mostrarTareas();
            }
        });
}

function dequeueFIFO(prioridad) {
    fetch(`/dequeue/${prioridad}`, {
        method: 'POST',
    })
        .then(response => response.json())
        .then(data => {
            if (data.error) {
                Swal.fire("Vacío", data.error, "info");
            } else {
                Swal.fire("Eliminado", `Se eliminó: ${data.task}`, "success");
                mostrarTareas();  // Refresca las tareas
            }
        })
        .catch(error => {
            console.error("Error al hacer dequeue:", error);
            Swal.fire("Error", "Ocurrió un error al eliminar la tarea", "error");
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
        "¡Hola! Soy Clippy, tu asistente inteligente 🧠",
        "Aquí puedes crear tareas nuevas escribiéndolas arriba.",
        "Las tareas se clasifican automáticamente por prioridad: Alta, Media o Baja.",
        "Puedes eliminarlas una por una o usar los botones FIFO para eliminar la primera tarea en cada categoría.",
        "Usa palabras como 'urgente', 'importante', o 'repasar' para que el sistema detecte la prioridad.",
        "Revisa tus colas de tareas a la derecha y mantenlas organizadas.",
        "Recuerda: las tareas más antiguas se eliminan primero si usas el botón FIFO ⏳",
        "¡Vamos a ponerte al día con todo! 📋💪"
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
