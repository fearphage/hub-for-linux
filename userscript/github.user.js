/*
 * Copyright (C) 2013 Peter Golm
 *
 * Authors:
 *  Peter Golm <golm.peter@gmail.com>
 *
 * This file is part of hub:linux.
 *
 * hub:linux is free software; you can redistribute it and/or modify it under
 * the terms of the GNU General Public License as published by the Free Software
 * Foundation; version 3.
 *
 * hub:linux is distributed in the hope that it will be useful, but WITHOUT
 * ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
 * FOR A PARTICULAR PURPOSE.  See the GNU General Public License for more
 * details.
 *
 * You should have received a copy of the GNU General Public License along with
 * this program; if not, write to the Free Software Foundation, Inc.,
 * 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA
 */
 
// ==UserScript==
// @name        hub:linux
// @version     0.0.1
// @description Add a clone button to repository.
// @author 	Peter Golm
// @namespace   http://www.github.com
// @include     http://*github.com/*
// @include     https://*github.com/*
// ==/UserScript==

(function() {
	if(document.getElementsByClassName("native-clones").length > 0) {
		url = 'github-linux://openRepo/' + window.location.origin + window.location.pathname;

		cloneLi = document.createElement('li')
		cloneLi.innerHTML = '<a href="'
			+ url +
			'" class="button minibutton " icon_class="mini-icon-download" rel="nofollow" title="Clone this repository"><span style="float:left; display: block; width: 16px; height: 22px; background-position: 0 4px; background-repeat: no-repeat; background-image: url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAA0AAAAPCAYAAAA/I0V3AAAABmJLR0QA/wD/AP+gvaeTAAAACXBIWXMAAAsTAAALEwEAmpwYAAAAB3RJTUUH3QMVCBUFC987DwAAAQNJREFUKM+N0r8uhFEQBfDfWkHI+hMKdgmJBmGjUbLiGSSeQOgUNAqRaJR676ARrURBITQ2PIAIFaViiaUZmy+fj3WSuTeZe885c+dO3k90YBtrGEQVH5pgHZ+J2EpfyGWQ9rCIPN4xFtFASwbpHq14CqeSf2A19k5sBrG3mdMCZjGCG7xh9y+XQ+ykBC9Qw3IWYRqXaE/ly/G+UxTT5VVwHKpJVPGIIcwkSUUs4eiXsu/QFs1pkPpwjbkMwmRMxijq359bCaVnHITrSqqbPZjCOa5gPqV8goGEy0birB8TYhlOjFQh1M7iY/cj341xFHIxY13RnVqoFXAbF0t4xQseUP8CluYvOrGy4wsAAAAASUVORK5CYII=);"></span>Clone in Linux</a>';
	
		nativeClonesNode = document.getElementsByClassName("native-clones")[0];
		nativeClonesNode.insertBefore(cloneLi, nativeClonesNode.firstElementChild);
	}
})()
