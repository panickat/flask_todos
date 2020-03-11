$(document).ready(function(){
 
    var MONTHS = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'];
    var color = Chart.helpers.color;
    var colorNames = Object.keys(window.chartColors);
    
    var horizontalBarChartData = { // all Bars
        labels: ['January', 'February', 'March', 'April', 'May', 'June', 'July'],
        datasets: [{
            label: 'Dataset 1',
            backgroundColor: color(window.chartColors.red).alpha(0.5).rgbString(),
            borderColor: window.chartColors.red,
            borderWidth: 1,
            data: [
                //long for each bar
                1
    
            ]
        }, {
            label: 'Dataset 2',
            backgroundColor: color(window.chartColors.blue).alpha(0.5).rgbString(),
            borderColor: window.chartColors.blue,
            data: [
                1
            ]
        }]
    
    };
    
    window.onload = function() {
        var ctx = $('#canvas').get(0).getContext('2d');
        window.myHorizontalBar = new Chart(ctx, {
            type: 'horizontalBar',
            data: horizontalBarChartData,
            options: {
                // Elements options apply to all of the options unless overridden in a dataset
                // In this case, we are setting the border of each horizontal bar to be 2px wide
                elements: {
                    rectangle: {
                        borderWidth: 2,
                    }
                },
                responsive: true,
                legend: {
                    position: 'right',
                },
                title: {
                    display: true,
                    text: 'Chart.js Horizontal Bar Chart'
                }
            }
        });
    
    };
    
    /*     $('#randomizeData').on('click', function() {
        var zero = Math.random() < 0.2 ? true : false;
        horizontalBarChartData.datasets.forEach(function(dataset) {
            dataset.data = dataset.data.map(function() {
                return zero ? 0.0 : randomScalingFactor();
            });
    
        });
        window.myHorizontalBar.update();
    }); */
    
    x =0;
    $('#addData').on('click', function() { x +=1;
        if (horizontalBarChartData.datasets.length > 0) {
            var month = MONTHS[horizontalBarChartData.labels.length % MONTHS.length];
            horizontalBarChartData.labels.push(month);
    
            for (var index = 0; index < horizontalBarChartData.datasets.length; ++index) {
                horizontalBarChartData.datasets[index].data.push(x);
            }
    
            window.myHorizontalBar.update();
        }
    });
    
    $('#removeDataset').on('click', function() {
        horizontalBarChartData.datasets.pop();
        window.myHorizontalBar.update();
    });
    
     $('#addDataset').on('click', function() { console.log("add dataset")
        var colorName = colorNames[horizontalBarChartData.datasets.length % colorNames.length];
        var dsColor = window.chartColors[colorName];
        var newDataset = {
            label: 'Dataset ' + (horizontalBarChartData.datasets.length + 1),
            backgroundColor: color(dsColor).alpha(0.5).rgbString(),
            borderColor: dsColor,
            data: []
        };
    
            newDataset.data.push(1);
        
    
        horizontalBarChartData.datasets.push(newDataset);
        window.myHorizontalBar.update();
    });    
    
    $('#removeData').on('click', function() {
        horizontalBarChartData.labels.splice(-1, 1); // remove the label first
    
        horizontalBarChartData.datasets.forEach(function(dataset) {
            dataset.data.pop();
        });
    
        window.myHorizontalBar.update();
    });

}); 

