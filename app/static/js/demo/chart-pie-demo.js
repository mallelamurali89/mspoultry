// Set new default font family and font color to mimic Bootstrap's default styling
Chart.defaults.global.defaultFontFamily = 'Nunito', '-apple-system,system-ui,BlinkMacSystemFont,"Segoe UI",Roboto,"Helvetica Neue",Arial,sans-serif';
Chart.defaults.global.defaultFontColor = '#858796';
// Pie Chart Example
var ctx = document.getElementById("myPieChart");
var myPieChart = new Chart(ctx, {
  type: 'doughnut',
  data: {
    labels: ["Products", "Hatching", "Traveling", "Chick Feed", "Grower Feed", "Layer Feed", "Medicines", "Workers", "Rent", "Others"],
    datasets: [{
      data: [pro, hat, tra, chf, gwf, lyf, med, wrk, rnt, oth],
      backgroundColor: ['#4e73df', '#1cc88a', '#36b9cc','#2085ec','#72b4eb','#0a417a','#8464a0','#cea9bc','#323232','#8464a0'],
      hoverBackgroundColor: ['#2e59d9', '#17a673', '#2c9faf','#2e59d9', '#17a673', '#2c9faf','#2e59d9', '#17a673', '#2c9faf','#DBE5D2'],
      hoverBorderColor: "rgba(234, 236, 244, 1)",
    }],
  },
  options: {
    maintainAspectRatio: false,
    tooltips: {
      backgroundColor: "rgb(255,255,255)",
      bodyFontColor: "#858796",
      borderColor: '#dddfeb',
      borderWidth: 1,
      xPadding: 15,
      yPadding: 15,
      displayColors: false,
      caretPadding: 10,
    },
    legend: {
      display: false
    },
    cutoutPercentage: 80,
  },
});
