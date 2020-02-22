d3.json("samples.json").then((importedData) => {

  buildPlot();  
    
}); 

function buildPlot(element)
{


  d3.json("samples.json").then((importedData) => {

    console.log(importedData);
    //console.log(importedData);  
    var data = importedData;
    console.log(data);
  
    //save all ids as options
    
    var select = document.getElementById("selDataset"); 
    var options = data.names; 
    var optionsLength = options.length
    console.log(options);
  
    //traverse through options, create an options element for each with text and a value
    for(var i = 0; i < optionsLength; i++) {
      var opt = options[i];
      var el = document.createElement("option");
      el.textContent = opt;
      el.value = opt;
      select.appendChild(el)};
  
    // function optionChanged(sel) {
    //   var value = sel.value;  
    // }
    var dropdownMenu = d3.select("#selDataset");
    // Assign the value of the dropdown menu option to a variable
    
    
    
    var sel_id = dropdownMenu.property("value");
    
    var sel_opt = options.indexOf(sel_id);
    console.log(sel_opt);
    //var sel_opt = 0
    //metadata
  
    var metadata = data.metadata;
      
    id = metadata[sel_opt].id;
    ethnicity = metadata[sel_opt].ethnicity;
    gender = metadata[sel_opt].gender;
    age = metadata[sel_opt].age;
    place = metadata[sel_opt].location;
      
    document.getElementById('id').innerHTML = id;
    document.getElementById('ethnicity').innerHTML = ethnicity;
    document.getElementById('gender').innerHTML = gender;
    document.getElementById('age').innerHTML = age;
    document.getElementById('place').innerHTML = place;
  
    // Extract samples from data
    var samp_vals = data.samples;
  
    //log the first sample id
    console.log("ID = ", samp_vals[sel_opt].id);
      
    //create an array called table
    var table = [];
  
    // assign the number of samples to 'arrayLength'
    var arrayLength = samp_vals[sel_opt].otu_labels.length;
    console.log("Length = ", arrayLength);
  
    // traverse through the samples, extraccting the otu labels, ids and sample values.
    for (var i = 0; i < arrayLength; i++) {
      table.push(  
        {lab: samp_vals[sel_opt].otu_labels[i],
        y: samp_vals[sel_opt].otu_ids[i],
        x: samp_vals[sel_opt].sample_values[i]
      });
    };
  
    // assign the rows in the table to 'tableLength'
    var tableLength = table.length;
    console.log(table[sel_opt].y);
  
    // sort the table based on OTU id
    table.sort(function(a, b) {
      if(a.y < b.y) { return -1; }
      if(a.y > b.y) { return 1; }
      return 0;
    });
  
    console.log(table)
  
    // copy the table
    var table2 = table
  
    //Bubble Chart
  
    var trace1 = {
      x: table2.map(row => row.y),
      y: table2.map(row => row.x),
      mode: 'markers',
      marker: {
        size: table2.map(row => row.x),
        color: table2.map(row => row.y),
      }
    };
      
    var data = [trace1];
      
    Plotly.newPlot('bubble', data);
  
    //Bar Chart
    //Copy the table again
    var table3 = table
  
    //traverse through table 3 and append 'OTU' to the beginning of each id  
    for (var i = 0; i < tableLength; i++) {
      table3[i].y = "OTU " + String(table3[i].y); 
    };
  
    //Sort the data array using the x value
    table3.sort(function(a, b) {
      return parseFloat(b.x) - parseFloat(a.x);
    });
  
    table3 = table3.slice(0, 10);
    table3 = table3.reverse();
  
    console.log(table3);
  
    // Trace1 for the 
    var trace2 = {
      x: table3.map(row => row.x),
      y: table3.map(row => row.y),
      text: table3.map(row => row.lab),
      type: "bar",
      orientation: "h"
    };
    
    // data
    var chartData = [trace2];
    
    // Render the plot to the div tag with id "plot"
    Plotly.newPlot("bar", chartData);    
      
  }); 
  

}


function optionChanged(element)
{
  buildPlot(element);
}


// USE D3 TO ADD OPTION TAGS IN HTML

// d3.selectAll("#selDataset").on("change", updatePlotly);

// function updatePlotly() {
//     // Use D3 to select the dropdown menu
//     var dropdownMenu = d3.select("#selDataset");
//     // Assign the value of the dropdown menu option to a variable
//     var test_subject = dropdownMenu.property("value");