//  agregation d'info météo
//  Copyright (C) 2009  Marc Poulhiès
//
//  This program is free software: you can redistribute it and/or modify
//  it under the terms of the GNU General Public License as published by
//  the Free Software Foundation, either version 3 of the License, or
//  (at your option) any later version.
//
//  This program is distributed in the hope that it will be useful,
//  but WITHOUT ANY WARRANTY; without even the implied warranty of
//  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
//  GNU General Public License for more details.
//
//  You should have received a copy of the GNU General Public License
//  along with this program.  If not, see <http://www.gnu.org/licenses/>.


var url_base="http://www.balisemeteo.com/";
var url_graph_base = url_base + "graphs/";

var histo_vent="histo_vent.php";
var histo_direc="histo_direction.php";

var histo_inter="1";
var histo_marks="false";

var webcam_height = "240px";

var balises = new Array();

balises["Moucherotte"] = "15";
balises["Saint Hil"] = "61";
balises["La Scia"] = "13";

var webcams = new Array();
webcams["Mallatrait(Allevard)"] = "http://pagesperso-orange.fr/lecollet.com/zzwebcam/image.jpg";

function wind_speed_img(balise) {
  var str = url_graph_base + histo_vent + "?idBalise=" + balise + "&interval=" + histo_inter +
    "&marks=" + histo_marks;
  return str;
}

function wind_direc_img(balise) {
  var str = url_graph_base + histo_direc + "?idBalise=" + balise + "&interval=" + histo_inter +
    "&marks=" + histo_marks;
  return str;
}

function balise_url(balise) {
  var str = url_base + "balise.php?idBalise=" + balise;
  return str;
}

function gen_balises(){
  var total = "";
  var total_head = "Les balises FFVL: <ul>";
  var elt;

  for (var b in balises) {
    elt =       '<a name="balise-' + b + '"><table class="balise">\n';
    elt = elt + ' <tr><th colspan="2">' + b + '  <a href="'+ balise_url(balises[b]) + '">[fflv]</a>' + '</th></tr>\n';
    elt = elt + ' <tr> <td><img src="' + wind_speed_img(balises[b]) + '"/> </td>\n';
    elt = elt + '      <td><img src="' + wind_direc_img(balises[b]) + '"/> </td></tr>\n';
    elt = elt + '</table></a>\n\n<br />\n';
    total = total + elt;
  
    total_head = total_head + '<li><a href="#balise-' + b + '">' + b + '</a>\n</li>';
  }

  total_head = total_head + "</ul>";
  return [total, total_head];
}


function gen_webcams(){
  var total = "";
  var total_head = "Les webcams: <ul>";
  var elt;

  for (var w in webcams) {
     elt = '<a name="webcam-' + w + '">\n' + 
       '<table class="webcam">\n' + 
       '<tr><th>' + w + '</th></tr>\n' +
       '<tr><td><a href="' + webcams[w] + '"><img src="' + webcams[w] + '" alt="' + w + '" height="' + webcam_height +'"/></a></td></tr>\n' + 
       '</table>\n';
     total = total + elt;
     total_head = total_head + '<li><a href="#webcam-' + w + '">' + w + '</a>\n</li>';
  }
  total_head = total_head + "</ul>";
  return [total, total_head];
}