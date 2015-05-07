var STATIC_LABEL = "/static/data/";

var day = d3.time.format("%w"),
    week = d3.time.format("%U"),
    percent = d3.format(".1%"),
    format = d3.time.format("%Y-%m-%d");

var MAX = 3200;
var MIN = 193;

var csvData;
var lineData;

var color_choices = ["#D73027","#F46D43","#FDAE61","#FEE08B","#FFFFBF","#D9EF8B","#A6D96A","#66BD63","#1A9850","#006837","#A50026"];
var color = d3.scale.quantize()
    .domain([MIN,MAX])
    .range(d3.range(11).map(function(d) { return color_choices[d] }));


var cellSize = 17; // cell size

function addCalendar(csv) {
  var width = 960,
    height = 136;
  var svg = d3.select("#wrapper").selectAll("svg.calendar")
    .data(d3.range(2012, 2013))
  .enter().append("svg")
    .attr("width", width)
    .attr("height", height)
    .attr("class", "RdYlGn")
    .attr("class", "calendar")
    .attr("id", "calendar")
  .append("g")
    .attr("transform", "translate(" + ((width - cellSize * 53) / 2) + "," + (height - cellSize * 7 - 1) + ")");

  svg.append("text")
      .attr("transform", "translate(-6," + cellSize * 3.5 + ")rotate(-90)")
      .style("text-anchor", "middle")
      .text(function(d) { return d; });

  var rect = svg.selectAll(".day")
      .data(function(d) { return d3.time.days(new Date(d, 0, 1), new Date(d + 1, 0, 1)); })
    .enter().append("rect")
      .attr("class", "day")
      .attr("width", cellSize)
      .attr("height", cellSize)
      .attr("x", function(d) { return week(d) * cellSize; })
      .attr("y", function(d) { return day(d) * cellSize; })
      .datum(format)
      .on("mouseover", function(day) {
        var div = d3.select("body").append("div")   
       .attr("class", "nvtooltip")               
       .style("opacity", 0);
        div.transition()        
          .duration(200)      
          .style("opacity", .9);
        div.html('<h3 style="background-color: '
                  + color(parseInt(data[day])) + '">' + day + '</h3>'
                  + '<p><b>' + data[day] + '</b> occurrences</p>')  
                  .style("left", (d3.event.pageX) + "px")     
                  .style("top", (d3.event.pageY - 28) + "px")
          .style("left", (d3.event.pageX) + "px")     
          .style("top", (d3.event.pageY - 28) + "px");
      })   
      .on("mouseout", function(precinct) {
        d3.selectAll(".nvtooltip").remove();
      });;

  rect.append("title")
      .text(function(d) { return d; });

  svg.selectAll(".month")
      .data(function(d) { return d3.time.months(new Date(d, 0, 1), new Date(d + 1, 0, 1)); })
    .enter().append("path")
      .attr("class", "month")
      .attr("d", monthPath);
        data = d3.nest()
    .key(function(d) { return d.datestop; })
    .rollup(function(d) { return (d[0].num_stops); })
    .map(csv);

  rect.filter(function(d) { return d in data; })
      .attr("class", function(d) { return "day"; })
      .style("fill", function(d) { return color(parseInt(data[d])); })
    .select("title")
      .text(function(d) { return d + ": " + percent(data[d]); });
}

function monthPath(t0) {
  var t1 = new Date(t0.getFullYear(), t0.getMonth() + 1, 0),
      d0 = +day(t0), w0 = +week(t0),
      d1 = +day(t1), w1 = +week(t1);
  return "M" + (w0 + 1) * cellSize + "," + d0 * cellSize
      + "H" + w0 * cellSize + "V" + 7 * cellSize
      + "H" + w1 * cellSize + "V" + (d1 + 1) * cellSize
      + "H" + (w1 + 1) * cellSize + "V" + 0
      + "H" + (w0 + 1) * cellSize + "Z";
}

var margin = {top: 20, right: 50, bottom: 30, left: 50},
    width = 960 - margin.left - margin.right,
    height = 500 - margin.top - margin.bottom;

var parseDate = d3.time.format("%Y-%m-%d").parse,
    bisectDate = d3.bisector(function(d) { return d.date; }).left;

var lineData;

var x = d3.time.scale()
    .range([0, width]);

var y = d3.scale.linear()
    .range([height, 0]);

var xAxis = d3.svg.axis()
    .scale(x)
    .orient("bottom");

var yAxis = d3.svg.axis()
    .scale(y)
    .orient("left");

var line = d3.svg.line()
    .x(function(d) { return x(d.date); })
    .y(function(d) { console.log(d.stops); return y(d.stops); });

function addGraph(data) {
  var svg = d3.select("#wrapper").append("svg")
    .attr("width", width + margin.left + margin.right)
    .attr("height", height + margin.top + margin.bottom)
    .attr("id", "linegraph")
  .append("g")
    .attr("transform", "translate(" + margin.left + "," + margin.top + ")");
  lineData = []
  data.forEach(function(d) {
    var datum = {};
    datum.date = parseDate(d.datestop);
    datum.stops = parseInt(d.num_stops);
    lineData.push(datum);
  });

  x.domain([parseDate("2012-01-01"), parseDate("2012-12-31")]);
  y.domain(d3.extent(lineData, function(d) { return d.stops; }));

  svg.append("g")
      .attr("class", "x axis")
      .attr("transform", "translate(0," + height + ")")
      .call(xAxis)
      .selectAll("text")
        .attr("class", "label");

  svg.append("g")
      .attr("class", "y axis")
      .call(yAxis)
      .selectAll("text")
        .attr("class", "label")
    .append("text")
      .attr("transform", "rotate(-90)")
      .attr("y", 6)
      .attr("dy", ".71em")
      .style("text-anchor", "end")
      .text("Number of Stops");

  svg.append("path")
      .datum(lineData)
      .attr("class", "line")
      .attr("d", line);

  var focus = svg.append("g")
      .attr("class", "focus")
      .style("display", "none");

  focus.append("circle")
      .attr("r", 4.5);

  focus.append("text")
      .attr("x", 9)
      .attr("dy", ".35em");

  svg.append("rect")
      .attr("class", "overlay")
      .attr("width", width)
      .attr("height", height)
      .on("mouseover", function() { focus.style("display", null); })
      .on("mouseout", function() { focus.style("display", "none"); })
      .on("mousemove", mousemove);

  function mousemove() {
    var x0 = x.invert(d3.mouse(this)[0]),
        i = bisectDate(lineData, x0, 1),
        d0 = lineData[i - 1],
        d1 = lineData[i],
        d = x0 - d0.date > d1.date - x0 ? d1 : d0;
    focus.attr("transform", "translate(" + x(d.date) + "," + y(d.stops) + ")");
    focus.select("text").text(d.stops + " stops")
      .attr("class","tooltip");
  }
}

d3.csv(STATIC_LABEL + "calendar.csv", function(error, data) {
  csvData = data;
  addGraph(data);
});

$(document).ready(function() {
  $("#calendar-button").click(function() {
    $("#calendar-button").prop('disabled', true);
    $("#linegraph-button").prop('disabled', false);
    d3.select("#linegraph").remove();
    addCalendar(csvData);
  });
  $("#linegraph-button").click(function() {
    $("#linegraph-button").prop('disabled', true);
    $("#calendar-button").prop('disabled', false);
    d3.select("#calendar").remove();
    addGraph(csvData);
  });
});