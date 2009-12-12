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
var instant_speed_direct = "graph_vent.php";


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

function wind_speed_direc(balise){
  var str = url_graph_base + instant_speed_direct + "?idBalise=" + balise;
  return str;
}

function balise_url(balise) {
  var str = url_base + "balise.php?idBalise=" + balise;
  return str;
}

function gen_balises(){
  var total = "";
  var total_head = "Les balises FFVL:\n <ul>";
  var elt;
  var img_width = Math.min(Math.round(window.innerWidth / 3)-20, 350);

  balises.each(function(balise) {
        elt = '<a name="balise-'     + balise.name + '" /><table class="balise">\n'
          +    ' <tr><th colspan="3">'+ balise.name + '  <a href="'+ balise_url(balise.id) + '">[ffvl]</a>' + '</th></tr>\n'
          +    ' <tr> <td>';
        if (enable_lightbox) {
          elt = elt + 
            '   <a href="'  + wind_speed_img(balise.id) +'" rel="lightbox[balises]" title="' + balise.name +'">';
        }
        elt = elt
          +    '   <img src="' + wind_speed_img(balise.id) + '" width="'+img_width +'" /> ';
        if (enable_lightbox){
          elt = elt + '   </a>'; 
        }
        elt = elt 
          +    ' </td>\n'
          +    ' <td>';
        
        if (enable_lightbox)
          elt = elt 
            +    '   <a href="'  + wind_direc_img(balise.id) +'" rel="lightbox[balises]" title="' + balise.name +'">';
        elt = elt
          +    '   <img src="' + wind_direc_img(balise.id) + '" width="'+img_width +'" />';

        if (enable_lightbox)
          elt = elt + '   </a>';
        elt = elt
          +    ' </td>\n'
          +    ' <td>';
        if (enable_lightbox)
          elt = elt
            +    '   <a href="'  + wind_speed_direc(balise.id) +'" rel="lightbox[balises]" title="' + balise.name +'">';
        elt = elt
          +    '   <img src="' + wind_speed_direc(balise.id)+'" width="'+img_width +'" />';
        if (enable_lightbox)
          elt = elt + '   </a>';
        elt = elt
          +    ' </td></tr>\n'
          +    '</table>\n\n<br />\n';
        total = total + elt;
  
        total_head = total_head + '<li><a href="#balise-' + balise.name + '">' + balise.name + '</a>\n</li>';
      });

  total_head = total_head + "</ul>";
  return [total, total_head];
}


function gen_webcams(){
  var total = "";
  var total_head = "Les webcams: <ul>";
  var elt;

  webcams.each(function(webcam){
     elt = '<a name="webcam-' + webcam.name + '">\n' + 
       '<table class="webcam">\n' + 
       '<tr><th>' + webcam.name + '</th></tr>\n' +
       '<tr><td>'+
       '<a href="' + webcam.url + '"><img src="' + webcam.url + '" alt="' + webcam.name + '" height="' + webcam_height +'"/></a></td></tr>\n' + 
       '</table>\n';
     total = total + elt;
     total_head = total_head + '<li><a href="#webcam-' + webcam.name + '">' + webcam.name + '</a>\n</li>';
    });

  total_head = total_head + "</ul>";
  return [total, total_head];
}