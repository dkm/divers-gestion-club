//  agregation d'info mÃ©tÃ©o
//  Copyright (C) 2009  Marc PoulhiÃ¨s
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


// largement inspiré par http://www.toulouseparapente.fr/meteo-parapente-pyrenees.php

/*
 * FFVL "balises météo"
 * Give a name (free form string) and its id.
 */
var balises = [
               { name: "Moucherotte", id:"15"},
               { name: "Saint Hil",   id: "61"},
               { name: "La Scia", id: "13"}
               ];

/*
 * Webcams.
 * Give a name (free form string) and a directed URL
 * to an image.
 */
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


/*
 *
 */
var sat_img = [
	       { name: "Image globale de la France",
		 url: "http://www.meteo.fr/temps/europe/satellite/bigsateuj.jpg",
		 ref: "http://www.meteo.fr"}
	       ];

/*
 * Meteociel config
 */

/*
 * 2 ways of including meteociel GFS data.
 * Set meteociel_get_gfs to either:
 * - meteociel_get_gfs_object: to include an <object /> including the
 *   web page
 * - meteociel_get_gfs_ajax: to include a more 'ajaxian'
 *   version. Currently, this solution provides less infos.
 */
meteociel_get_gfs = meteociel_get_gfs_object;
/*
 * width and size. When using the object method above
 * this can result in horiz/vert scrolling bars (ugly).
 */
meteociel_width=650;
meteociel_height=700;

/*
 * enable/disable stuff
 *
 * Whenever possible, lightbox is used to display higher resolution for pictures.
 * Related images are grouped.
 */
var enable_lightbox = true;

/*
 * Controls the displaying of wind info from FFVL "balises météo".
 */
var histo_inter="1";
var histo_marks="false";

/*
 * Height used for resizing webcam images.
 * All images are resized.
 */
var webcam_height = "240px";

