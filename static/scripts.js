document.addEventListener('DOMContentLoaded', () => {
    const computeButton = document.getElementById('compute-button');
    computeButton.addEventListener('click', () => {
        // Simulación de datos del árbol (deberías obtener esto dinámicamente)
        const treeData = {
            value: 0,
            depth: 3,
            children: [
                {
                    value: 1,
                    children: [
                        { value: 3, children: [] },
                        { value: 5, children: [] }
                    ]
                },
                {
                    value: 2,
                    children: [
                        { value: 6, children: [] },
                        { value: 9, children: [] }
                    ]
                }
            ]
        };

        fetch('/compute', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(treeData)
        })
        .then(response => response.json())
        .then(data => {
            console.log('Resultado de Alpha-Beta:', data.result);
            // Aquí puedes actualizar la interfaz de usuario con los resultados
        })
        .catch(error => console.error('Error:', error));
    });
});
