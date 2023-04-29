const renderChart = (data, labels) => {
  
  var ctx = document.getElementById("myChart").getContext("2d");
  var barColors = ["orange"]
  var myChart = new Chart(ctx, {
    type: "line",
    data: {
      labels: labels,
      datasets: [
        {
          label: "Last 6 months incomes",
          data: data,
          backgroundColor: barColors,
          
          borderWidth: 1,
        },
      ],
    },
    options: {
      title: {
        display: true,
        
        text: "incomes per source" ,
      },
    },
  });
};

const getChartData = () => {
  console.log("fetching");
  fetch("/income/income_source_summary")
    .then((res) => res.json())
    .then((results) => {
      console.log("results", results);
      const source_data = results.income_source_data;
      const [labels, data] = [
        Object.keys(source_data),
        Object.values(source_data),
      ];

      renderChart(data, labels);
    });
};

document.onload = getChartData();