import * as echarts from 'echarts';

waitForElement('#chart-container').then(() => {
  // initialize the echarts instance
  const myChart = echarts.init(document.getElementById('chart-container'));
  const portfolioValue = JSON.parse(document.getElementById('portfolio_values').textContent);
  console.log(portfolioValue);
  const totalInvested = JSON.parse(document.getElementById('investment_totals').textContent);
  console.log(totalInvested);
  const tradeDates = JSON.parse(document.getElementById('trade_dates').textContent);
  console.log(tradeDates);
  // const stockPrices = JSON.parse(document.getElementById('amount_invested').textContent);

  // Draw the chart

  myChart.setOption({
    title: {
      text: 'Investment Performance'
    },
    tooltip: {
      trigger: 'axis'
    },
    legend: {
      data: ['Portfolio Value', 'Total Invested']
    },
    grid: {
      left: '3%',
      right: '4%',
      bottom: '3%',
      containLabel: true
    },
    toolbox: {
      feature: {
        saveAsImage: {}
      }
    },
    xAxis: {
      type: 'category',
      boundaryGap: false,
      data: tradeDates
    },
    yAxis: {
      type: 'value'
    },
    series: [
      {
        name: 'Portfolio Value',
        type: 'line',
        stack: 'Total',
        data: portfolioValue
      },
      {
        name: 'Total Invested',
        type: 'line',
        stack: 'Total',
        data: totalInvested
      }
      // {
      //   name: 'Stock Price',
      //   type: 'line',
      //   stack: 'Total',
      //   data: [150, 232, 201, 154, 190, 330, 410]
      // }
    ]
  });
});

function waitForElement(selector) {
  return new Promise(resolve => {
      if (document.querySelector(selector)) {
          return resolve(document.querySelector(selector));
      }
      
      const observer = new MutationObserver(mutations => {
          if (document.querySelector(selector)) {
              resolve(document.querySelector(selector));
              observer.disconnect();
          }
      });
      
      observer.observe(document.body, {
          childList: true,
          subtree: true
      });
  });
}