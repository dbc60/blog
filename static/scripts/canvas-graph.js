/* Initialization */

// To be called when the page finishes loading:
function init() {
 Draw() ;
}


/* Canvas and context objects */

var Canvas = document.getElementById('xy-graph');
var Ctx = null ;

var Width = Canvas.width ;
var Height = Canvas.height ;


/*
  The origin (0,0) of the canvas is the upper left:

  (0,0)
    --------- +X
   |
   |
   |
   |
   +Y

  Positive x coordinates go to the right, and positive y coordinates go down.

  The origin in mathematics is the "center," and positive y goes *up*.

  We'll refer to the mathematics coordinate system as the "logical"
  coordinate system, and the coordinate system for the canvas as the
  "physical" coordinate system.

  The functions just below set up a mapping between the two coordinate
  systems.

  They're defined as functions, so that one wanted to, they could read
  ther values from a from instead of having them hard-coded.

 */


// Returns the right boundary of the logical viewport:
function MaxX() {
  return 10 ;
}

// Returns the left boundary of the logical viewport:
function MinX() {
  return -10 ;
}

// Returns the top boundary of the logical viewport:
function MaxY() {
  return MaxX() * Height / Width;
}

// Returns the bottom boundary of the logical viewport:
function MinY() {
   return MinX() * Height / Width;
}

// Returns the physical x-coordinate of a logical x-coordinate:
function XC(x) {
  return (x - MinX()) / (MaxX() - MinX()) * Width ;
}

// Returns the physical y-coordinate of a logical y-coordinate:
function YC(y) {
  return Height - (y - MinY()) / (MaxY() - MinY()) * Height ;
}


/* Rendering functions */

// Clears the canvas, draws the axes and graphs the function F.
function Draw() {

 // Evaluate the user-supplied code, which must bind a value to F.
 eval(document.getElementById('function-code').value) ;

 if (Canvas.getContext) {

   // Set up the canvas:
   Ctx = Canvas.getContext('2d');
   Ctx.clearRect(0,0,Width,Height) ;

   // Draw:
   DrawAxes() ;
   RenderFunction(F) ;

  } else {
    // Do nothing.
  }
}


// Returns the distance between ticks on the X axis:
function XTickDelta() {
  return 1 ;
}

// Returns the distance between ticks on the Y axis:
function YTickDelta() {
  return 1 ;
}


// DrawAxes draws the X ad Y axes, with tick marks.
function DrawAxes() {
 Ctx.save() ;
 Ctx.lineWidth = 2 ;
 // +Y axis
 Ctx.beginPath() ;
 Ctx.moveTo(XC(0),YC(0)) ;
 Ctx.lineTo(XC(0),YC(MaxY())) ;
 Ctx.stroke() ;

 // -Y axis
 Ctx.beginPath() ;
 Ctx.moveTo(XC(0),YC(0)) ;
 Ctx.lineTo(XC(0),YC(MinY())) ;
 Ctx.stroke() ;

 // Y axis tick marks
 var delta = YTickDelta() ;
 for (var i = 1; (i * delta) < MaxY() ; ++i) {
  Ctx.beginPath() ;
  Ctx.moveTo(XC(0) - 5,YC(i * delta)) ;
  Ctx.lineTo(XC(0) + 5,YC(i * delta)) ;
  Ctx.stroke() ;
 }

 var delta = YTickDelta() ;
 for (var i = 1; (i * delta) > MinY() ; --i) {
  Ctx.beginPath() ;
  Ctx.moveTo(XC(0) - 5,YC(i * delta)) ;
  Ctx.lineTo(XC(0) + 5,YC(i * delta)) ;
  Ctx.stroke() ;
 }

 // +X axis
 Ctx.beginPath() ;
 Ctx.moveTo(XC(0),YC(0)) ;
 Ctx.lineTo(XC(MaxX()),YC(0)) ;
 Ctx.stroke() ;

 // -X axis
 Ctx.beginPath() ;
 Ctx.moveTo(XC(0),YC(0)) ;
 Ctx.lineTo(XC(MinX()),YC(0)) ;
 Ctx.stroke() ;

 // X tick marks
 var delta = XTickDelta() ;
 for (var i = 1; (i * delta) < MaxX() ; ++i) {
  Ctx.beginPath() ;
  Ctx.moveTo(XC(i * delta),YC(0)-5) ;
  Ctx.lineTo(XC(i * delta),YC(0)+5) ;
  Ctx.stroke() ;
 }

 var delta = XTickDelta() ;
 for (var i = 1; (i * delta) > MinX() ; --i) {
  Ctx.beginPath() ;
  Ctx.moveTo(XC(i * delta),YC(0)-5) ;
  Ctx.lineTo(XC(i * delta),YC(0)+5) ;
  Ctx.stroke() ;
 }
 Ctx.restore() ;
}


// When rendering, XSTEP determines the horizontal distance between points:
var XSTEP = (MaxX()-MinX())/Width ;


// RenderFunction(f) renders the input funtion f on the canvas.
function RenderFunction(f) {
  var first = true;

  Ctx.beginPath() ;
  for (var x = MinX(); x <= MaxX(); x += XSTEP) {
   var y = f(x) ;
   if (first) {
    Ctx.moveTo(XC(x),YC(y)) ;
    first = false ;
   } else {
    Ctx.lineTo(XC(x),YC(y)) ;
   }
  }
  Ctx.stroke() ;
}
