$(document).ready(function(){
    var getData = $.get('/data');
    getData.done(function(res){
        var trace1 = {
            type: "scatter",
            mode: "lines",
            name: 'Temp1',
            x: res.Time,
            y: res.Temp1,
            line: {color: '#e61a1a'}
          }
          var trace2 = {
            type: "scatter",
            mode: "lines",
            name: 'Temp2',
            x: res.Time,
            y: res.Temp2,
            line: {color: '#0d1acc'}
          }
          var trace3 = {
            type: "scatter",
            mode: "lines",
            name: 'Ambiant',
            x: res.Time,
            y: res.Tambiant,
            line: {color: '#41d053'}
          }
          var data = [trace1,trace2,trace3];
          var layout = {
            title: 'Temperature',
            font: {
              family: 'Courier New, monospace',
              color: '#f3f3ff'
            },
            legend: {"orientation": "v"},
            yaxis: {
                title: 'Temp °C'
              },
              xaxis: {
                autorange: true,
                range: [res.Time[(res.Time.length - 1)], res.Time[0]],
                //rangeslider: {range: [res.Time[(res.Time.length - 1)], res.Time[0]]},
                type: 'date'
              },
              plot_bgcolor:"transparent",
              paper_bgcolor:'rgba(0,0,0,0)'
          };
          Plotly.newPlot('chart1', data, layout , {responsive: true} );
          var trace4 = {
          type: "scatter",
          mode: "lines",
          name: 'Humidity',
          x: res.Time,
          y: res.Humidity,
          line: {color: '#8541a7'}
          }
          var data = [trace4];
          var layout2 = {
          title: 'Humidity',
          font: {
            family: 'Courier New, monospace',
            color: '#f3f3ff'
          },
          xaxis: {
            autorange: true,
            range: [res.Time[(res.Time.length - 1)], res.Time[0]],
            rangeslider: {range: [res.Time[(res.Time.length - 1)], res.Time[0]]},
            type: 'date',
          },
          yaxis: {
              autorange: false,
              range: [10, 100],
              type: 'linear' ,
              title: 'Relative Humidity %'
          },
          plot_bgcolor:"transparent",
          paper_bgcolor:'rgba(0,0,0,0)'
          };
          Plotly.newPlot('chart2', data, layout2 , {responsive: true});


          //data table:
          var dataSet=[];
          for(var i=0; i < res.Time.length ; i++){
            dataSet.push([res.Time[i],res.Temp1[i],res.Temp2[i],res.Tambiant[i],res.Humidity[i]])
          }

          console.log(dataSet)

          $('#tb2').DataTable({
            data: dataSet,
             "columns": [
                 { "title": "Time" },
                 { "title": "Temp1" },
                 { "title": "Temp2" },
                 { "title": "Tambiant" },
                 { "title": "Humidity" }
             ]
         } );
         
    });

    var APIData = $.get('/api_data');
    APIData.done(function(API){
      var table = document.getElementById("API_table");
      table.rows[0].cells[1].innerHTML = String((API.main.temp - 273.15).toFixed(2)) + " °C";
      table.rows[1].cells[1].innerHTML = String(API.main.humidity) + " %";
      table.rows[2].cells[1].innerHTML = String(API.main.pressure) + " hPa";
      table.rows[3].cells[1].innerHTML = String(API.wind.speed) + " m/s";
      table.rows[4].cells[1].innerHTML = String(API.wind.deg) + " °";
      table.rows[5].cells[1].innerHTML = String(API.weather[0].main) ;
    });
});