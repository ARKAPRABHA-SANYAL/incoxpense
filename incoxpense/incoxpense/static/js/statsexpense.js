const renderChart = (data, labels) => {
  
  var ctx = document.getElementById("myChart").getContext("2d");
  var barColors = ["orange"]
  var myChart = new Chart(ctx, {
    type: "line",
    data: {
      labels: labels,
      datasets: [
        {
          label: "Last 6 months expenses",
          data: data,
          backgroundColor: barColors,
          
          borderWidth: 1,
        },
      ],
    },
    options: {
      title: {
        display: true,
        
        text: "Expenses per category" ,
      },
    },
  });
};

const getChartData = () => {
  console.log("fetching");
  fetch("/expense_category_summary")
    .then((res) => res.json())
    .then((results) => {
      console.log("results", results);
      const category_data = results.expense_category_data;
      const [labels, data] = [
        Object.keys(category_data),
        Object.values(category_data),
      ];

      renderChart(data, labels);
    });
};

document.onload = getChartData();