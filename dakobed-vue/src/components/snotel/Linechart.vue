<template><div>
  <svg width="100%" height="100%" viewBox="0 0 800 330"
  preserveAspectRatio="xMidYMid meet" >
    
    <g class='lineChart' v-bind:transform="translate">
      <axis class='yA' v-bind:scales="getScales().yAxis" v-bind:chartDefaults='chartDefaults' v-bind:data='data' v-bind:trns='trnsY'/>
      <axis class='xA' v-bind:scales="getScales().xAxis" v-bind:chartDefaults='chartDefaults' v-bind:data='data' v-bind:trns='trnsX()'/>
      <axis class='grid' v-bind:scales="getScales().yGrid" v-bind:chartDefaults='chartDefaults' v-bind:data='data' v-bind:trns='trnsY' v-bind:style="{opacity: chartDefaults.gridOpacity}"/>
    <path class='line' :d="line" />

    </g>
      
  </svg>

</div>
</template>

<script>
/* eslint-disable */
import * as d3 from "d3";
import Axis from "./axis";
export default {
  components: {
    axis: Axis // Using reusable component to draw x,y axis and Grid.
  },
  props:{
    data: Array,

  },
  created(){
    console.log("data " + JSON.stringify(this.data.slice(0,2)))

  },
  data() {
    return {

      chartDefaults: {
        width: 800,
        height: 300,
        chartId: "linechart-vue",
        title: "UK Rainfall for 2018",
        margin: {
          top: 5,
          right: 5,
          bottom: 15,
          left: 50
        },
        gridOpacity: 1,
        data: []
      },
      line: "",
      median:"",
      //Translate co-ords for chart, x axis and yaxis. This is injected into template
      translate: "translate(" + 50 + "," + 5 + ")",
      trnsY: "translate(0,0)",
      trnsX: this.getTrnsx,
      toggleClass: true
    };
  },
  mounted() {
    var scale = {};
    //Kick off drawing chart once component is mounted
    this.calculatePath();
  },
  methods: {
    getScales() {
      // All the maths to work chart co ordinates and woring out Axis
      var parseDate = d3.timeParse("%m-%d-%Y");

      this.data.forEach(function(d) {
        d.date = parseDate(d.day);
      });

      const x = d3
        .scaleTime()
        .domain(
          d3.extent(this.data, function(d) {
            return d.date;
          })
        )
        .rangeRound([0, this.chartDefaults.width - 100]);
      const y = d3
        .scaleLinear()
        .domain([
          0,
          d3.max(this.data, function(d) {
            return d.count + 100;
          })
        ])
        .range([this.chartDefaults.height, 0]);
      d3.axisBottom().scale(x);
      d3.axisLeft().scale(y);

      //Key funtions to draw X-axis,YAxis and the grid. All uses component axis
      //play around with time format to get it to display as you want : d3.timeFormat("%b-%d")
      var xAxis = d3
        .axisBottom()
        .scale(x)
        .tickFormat(d3.timeFormat("%b"))
        .tickValues(
          this.data
            .map(function(d, i) {
              if (i > 0) {
                return d.date;
              }
              return false;
            })
            .splice(1)
        )
        .ticks(4);

      var yAxis = d3
        .axisLeft()
        .scale(y)
        .ticks(5);
      var yGrid = d3
        .axisLeft()
        .scale(y)
        .tickSize(-(this.chartDefaults.width - 100), 0, 0)
        .tickFormat("");
      // Return the key calculations and functions to draw the chart
      return {
        x,
        y,
        xAxis,
        yAxis,
        yGrid
      };
    },
    getTrnsx(chartDefaults) {
      //works out translate value in realtive to dynamic height
      const t = "translate(0," + this.chartDefaults.height + ")";
      return t;
    },
    calculatePath() {
      //Get key calculation funtions to draw chart , Ie scale, axis mapping and plotting
      const scale = this.getScales();
      // Define calcultion to draw chart
      const path = d3
        .line()
        .x(d => {
          return scale.x(d.date);
        })
        .y(d => {
          return scale.y(d.count);
        })
        .curve(d3.curveCardinal);

      // draw line then this.line is injected into the template
      this.line = path(this.data);

    }
  }
};
</script>
<!-- css loaderhttps://vue-loader.vuejs.org/guide/scoped-css.html#mixing-local-and-global-styles -->
<style scoped>

text {
  color: #fff;
}

path.line {
  fill: none;
  stroke: #ecbc3a;
  stroke-width: 3px;
}

.grid line {
  opacity: 0.05;
}
.xA line {
  opacity: 0.5;
}

/*Some fancy animation to draw chart* I do not need this righ now but maybe in the future.. / 
/* svg .lineChart > path {
  stroke: #ecbc3a;
  stroke-width: 3;
  stroke-dasharray: 4813.713;
  stroke-dashoffset: 4813.713;
  -webkit-animation-name: draw2;
  animation-name: draw2;
  -webkit-animation-duration: 10s;
  animation-duration: 10s;
  -webkit-animation-fill-mode: forwards;
  animation-fill-mode: forwards;
  -webkit-animation-iteration-count: 1;
  animation-iteration-count: 1;
  -webkit-animation-timing-function: linear;
  animation-timing-function: linear;
} */

.ani2 svg .lineChart > path {
  stroke: #ecbc3a;
  -webkit-animation-name: draw-2;
  animation-name: draw-2;
}
.ani1 svg .lineChart > path {
  stroke: #ecbc3a;
  -webkit-animation-name: draw;
  animation-name: draw;
}
#Layer_1 {
  width: 100%;
}
@-webkit-keyframes draw {
  85% {
  }
  100% {
    stroke-dashoffset: 0;
  }
}
@keyframes draw {
  85% {
  }
  100% {
    stroke-dashoffset: 0;
  }
}

@-webkit-keyframes draw-2 {
  85% {
  }
  100% {
    stroke-dashoffset: 0;
  }
}

@keyframes draw-2 {
  85% {
  }
  100% {
    stroke-dashoffset: 0;
  }
}
.text {
  display: inline-block;
  font-size: 3vw;
  margin: 0.5vw 0 1.5vw;
}

svg {
  background-color: #003f5c;
}
</style>
