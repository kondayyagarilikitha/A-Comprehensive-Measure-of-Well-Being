const ctx = document.getElementById("indicatorChart");

if (ctx) {

    const life =
        Number(document.body.dataset.life) || 72;

    const expected =
        Number(document.body.dataset.expected) || 14;

    const mean =
        Number(document.body.dataset.mean) || 10;

    const gni =
        Number(document.body.dataset.gni) || 25000;

    new Chart(ctx, {

        type: "bar",

        data: {

            labels: [
                "Life Expectancy",
                "Expected Schooling",
                "Mean Schooling",
                "GNI /1000"
            ],

            datasets: [{

                label: "Input Indicators",

                data: [

                    life,
                    expected,
                    mean,
                    gni / 1000

                ],

                backgroundColor: [

                    "#2563eb",
                    "#10b981",
                    "#f59e0b",
                    "#ef4444"

                ],

                borderRadius: 12

            }]
        },

        options: {

            responsive: true,

            plugins: {

                legend: {

                    display: false

                }

            },

            animation: {

                duration: 1800

            },

            scales: {

                y: {

                    beginAtZero: true

                }

            }

        }

    });

}