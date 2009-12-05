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



var balises = [
               { name: "Moucherotte", id:"15"},
               { name: "Saint Hil",   id: "61"},
               { name: "La Scia", id: "13"}
               ];

var webcams = [
               { name: "Mallatrait(Allevard)", 
                 url:"http://pagesperso-orange.fr/lecollet.com/zzwebcam/image.jpg"},

               { name: "Chamrousse (RB)", 
                 url: "http://www.meteo-chamrousse.com/roche.jpg"},

               { name: "Grenoble INP (Bastille)", 
                 url: "http://webcam.minatec.grenoble-inp.fr/axis-cgi/jpg/image.cgi?resolution=640x480&text=1&textstring=Grenoble%20INP%20-%20Minatec%20-%20Vue%20sur%20la%20bastillle"},

               { name: "Versoud (Saint Eynard)", 
                 url: "http://www.meteosite-38.fr/vue-webcam.jpg"}
               ];


// enable/disable stuff
var enable_lightbox = true;

// some internals
var histo_inter="1";
var histo_marks="false";

var webcam_height = "240px";

