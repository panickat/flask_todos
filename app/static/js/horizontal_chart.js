$(document).ready(function(){
     
    var MONTHS = ['months'];
    var color = Chart.helpers.color;
    var colorNames = Object.keys(window.chartColors);
    
    var horizontalBarChartData = { // all Bars
        labels: ['labels'],
        datasets: []
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
                },
                layout: {
                    padding: {
                        left: 50,                
                        right: 50,
                    }
                }
            }
        });
    
    };
    
         $('#randomizeData').on('click', function() {
        var zero = Math.random() < 0.2 ? true : false;
        horizontalBarChartData.datasets.forEach(function(dataset) {
            dataset.data = dataset.data.map(function() {
                return zero ? 0.0 : randomScalingFactor();
            });
    
        });
        window.myHorizontalBar.update();
    }); 
    
    $('#addData').on('click', function() { 
        if (horizontalBarChartData.datasets.length > 0) {
            var month = MONTHS[horizontalBarChartData.labels.length % MONTHS.length];
            horizontalBarChartData.labels.push(month);
    
            for (var index = 0; index < horizontalBarChartData.datasets.length; ++index) {
                horizontalBarChartData.datasets[index].data.push(1);
            }
    
            window.myHorizontalBar.update();
        }
    });
    
    $('#removeDataset').on('click', function() {
        horizontalBarChartData.datasets.pop();
        window.myHorizontalBar.update();
    });
    

    function ds(name,dsColor){
        var newDataset = {
            label: name,
            backgroundColor: color(dsColor).alpha(0.5).rgbString(),
            borderColor: dsColor,
            data: [] 
        };
        return newDataset;
    }
    
    $('#addDataset').on('click', function() {   
    $.getJSON( "charts/get_alltime", function( data ) { 
        $.each(data, function(name, obj) {
            var colorName = colorNames[horizontalBarChartData.datasets.length % colorNames.length];
            var dsColor = window.chartColors[colorName];

            newDataset = ds(name,dsColor);
            newDataset.data.push( obj.point_over );
            horizontalBarChartData.datasets.push(newDataset);

            newDataset = ds(name,dsColor);
            newDataset.data.push( obj.point_under * -1 );
            horizontalBarChartData.datasets.push(newDataset);
        });
        window.myHorizontalBar.update();
    });        
    
        

    });    
    
    $('#removeData').on('click', function() {
        horizontalBarChartData.labels.splice(-1, 1); // remove the label first
    
        horizontalBarChartData.datasets.forEach(function(dataset) {
            dataset.data.pop();
        });
    
        window.myHorizontalBar.update();
    });

}); 

