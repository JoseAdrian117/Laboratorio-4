<!DOCTYPE html>
<html>
<head><meta charset="utf-8" />

<title>P4</title>

<script src="https://cdnjs.cloudflare.com/ajax/libs/require.js/2.1.10/require.min.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/jquery/2.0.3/jquery.min.js"></script>



<style type="text/css">
    /*!
*
* Twitter Bootstrap
*
*/
/*!
 * Bootstrap v3.3.7 (http://getbootstrap.com)
 * Copyright 2011-2016 Twitter, Inc.
 * Licensed under MIT (https://github.com/twbs/bootstrap/blob/master/LICENSE)
 */
/*! normalize.css v3.0.3 | MIT License | github.com/necolas/normalize.css */
html {
  font-family: sans-serif;
  -ms-text-size-adjust: 100%;
  -webkit-text-size-adjust: 100%;
}
body {
  margin: 0;
}
article,
aside,
details,
figcaption,
figure,
footer,
header,
hgroup,
main,
menu,
nav,
section,
summary {
  display: block;
}
audio,
canvas,
progress,
video {
  display: inline-block;
  vertical-align: baseline;
}
audio:not([controls]) {
  display: none;
  height: 0;
}
[hidden],
template {
  display: none;
}
a {
  background-color: transparent;
}
a:active,
a:hover {
  outline: 0;
}
abbr[title] {
  border-bottom: 1px dotted;
}
b,
strong {
  font-weight: bold;
}
dfn {
  font-style: italic;
}
h1 {
  font-size: 2em;
  margin: 0.67em 0;
}
mark {
  background: #ff0;
  color: #000;
}
small {
  font-size: 80%;
}
sub,
sup {
  font-size: 75%;
  line-height: 0;
  position: relative;
  vertical-align: baseline;
}
sup {
  top: -0.5em;
}
sub {
  bottom: -0.25em;
}
img {
  border: 0;
}
svg:not(:root) {
  overflow: hidden;
}
figure {
  margin: 1em 40px;
}
hr {
  box-sizing: content-box;
  height: 0;
}
pre {
  overflow: auto;
}
code,
kbd,
pre,
samp {
  font-family: monospace, monospace;
  font-size: 1em;
}
button,
input,
optgroup,
select,
textarea {
  color: inherit;
  font: inherit;
  margin: 0;
}
button {
  overflow: visible;
}
button,
select {
  text-transform: none;
}
button,
html input[type="button"],
input[type="reset"],
input[type="submit"] {
  -webkit-appearance: button;
  cursor: pointer;
}
button[disabled],
html input[disabled] {
  cursor: default;
}
button::-moz-focus-inner,
input::-moz-focus-inner {
  border: 0;
  padding: 0;
}
input {
  line-height: normal;
}
input[type="checkbox"],
input[type="radio"] {
  box-sizing: border-box;
  padding: 0;
}
input[type="number"]::-webkit-inner-spin-button,
input[type="number"]::-webkit-outer-spin-button {
  height: auto;
}
input[type="search"] {
  -webkit-appearance: textfield;
  box-sizing: content-box;
}
input[type="search"]::-webkit-search-cancel-button,
input[type="search"]::-webkit-search-decoration {
  -webkit-appearance: none;
}
fieldset {
  border: 1px solid #c0c0c0;
  margin: 0 2px;
  padding: 0.35em 0.625em 0.75em;
}
legend {
  border: 0;
  padding: 0;
}
textarea {
  overflow: auto;
}
optgroup {
  font-weight: bold;
}
table {
  border-collapse: collapse;
  border-spacing: 0;
}
td,
th {
  padding: 0;
}
/*! Source: https://github.com/h5bp/html5-boilerplate/blob/master/src/css/main.css */
@media print {
  *,
  *:before,
  *:after {
    background: transparent !important;
    box-shadow: none !important;
    text-shadow: none !important;
  }
  a,
  a:visited {
    text-decoration: underline;
  }
  a[href]:after {
    content: " (" attr(href) ")";
  }
  abbr[title]:after {
    content: " (" attr(title) ")";
  }
  a[href^="#"]:after,
  a[href^="javascript:"]:after {
    content: "";
  }
  pre,
  blockquote {
    border: 1px solid #999;
    page-break-inside: avoid;
  }
  thead {
    display: table-header-group;
  }
  tr,
  img {
    page-break-inside: avoid;
  }
  img {
    max-width: 100% !important;
  }
  p,
  h2,
  h3 {
    orphans: 3;
    widows: 3;
  }
  h2,
  h3 {
    page-break-after: avoid;
  }
  .navbar {
    display: none;
  }
  .btn > .caret,
  .dropup > .btn > .caret {
    border-top-color: #000 !important;
  }
  .label {
    border: 1px solid #000;
  }
  .table {
    border-collapse: collapse !important;
  }
  .table td,
  .table th {
    background-color: #fff !important;
  }
  .table-bordered th,
  .table-bordered td {
    border: 1px solid #ddd !important;
  }
}
@font-face {
  font-family: 'Glyphicons Halflings';
  src: url('../components/bootstrap/fonts/glyphicons-halflings-regular.eot');
  src: url('../components/bootstrap/fonts/glyphicons-halflings-regular.eot?#iefix') format('embedded-opentype'), url('../components/bootstrap/fonts/glyphicons-halflings-regular.woff2') format('woff2'), url('../components/bootstrap/fonts/glyphicons-halflings-regular.woff') format('woff'), url('../components/bootstrap/fonts/glyphicons-halflings-regular.ttf') format('truetype'), url('../components/bootstrap/fonts/glyphicons-halflings-regular.svg#glyphicons_halflingsregular') format('svg');
}
.glyphicon {
  position: relative;
  top: 1px;
  display: inline-block;
  font-family: 'Glyphicons Halflings';
  font-style: normal;
  font-weight: normal;
  line-height: 1;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
}
.glyphicon-asterisk:before {
  content: "\002a";
}
.glyphicon-plus:before {
  content: "\002b";
}
.glyphicon-euro:before,
.glyphicon-eur:before {
  content: "\20ac";
}
.glyphicon-minus:before {
  content: "\2212";
}
.glyphicon-cloud:before {
  content: "\2601";
}
.glyphicon-envelope:before {
  content: "\2709";
}
.glyphicon-pencil:before {
  content: "\270f";
}
.glyphicon-glass:before {
  content: "\e001";
}
.glyphicon-music:before {
  content: "\e002";
}
.glyphicon-search:before {
  content: "\e003";
}
.glyphicon-heart:before {
  content: "\e005";
}
.glyphicon-star:before {
  content: "\e006";
}
.glyphicon-star-empty:before {
  content: "\e007";
}
.glyphicon-user:before {
  content: "\e008";
}
.glyphicon-film:before {
  content: "\e009";
}
.glyphicon-th-large:before {
  content: "\e010";
}
.glyphicon-th:before {
  content: "\e011";
}
.glyphicon-th-list:before {
  content: "\e012";
}
.glyphicon-ok:before {
  content: "\e013";
}
.glyphicon-remove:before {
  content: "\e014";
}
.glyphicon-zoom-in:before {
  content: "\e015";
}
.glyphicon-zoom-out:before {
  content: "\e016";
}
.glyphicon-off:before {
  content: "\e017";
}
.glyphicon-signal:before {
  content: "\e018";
}
.glyphicon-cog:before {
  content: "\e019";
}
.glyphicon-trash:before {
  content: "\e020";
}
.glyphicon-home:before {
  content: "\e021";
}
.glyphicon-file:before {
  content: "\e022";
}
.glyphicon-time:before {
  content: "\e023";
}
.glyphicon-road:before {
  content: "\e024";
}
.glyphicon-download-alt:before {
  content: "\e025";
}
.glyphicon-download:before {
  content: "\e026";
}
.glyphicon-upload:before {
  content: "\e027";
}
.glyphicon-inbox:before {
  content: "\e028";
}
.glyphicon-play-circle:before {
  content: "\e029";
}
.glyphicon-repeat:before {
  content: "\e030";
}
.glyphicon-refresh:before {
  content: "\e031";
}
.glyphicon-list-alt:before {
  content: "\e032";
}
.glyphicon-lock:before {
  content: "\e033";
}
.glyphicon-flag:before {
  content: "\e034";
}
.glyphicon-headphones:before {
  content: "\e035";
}
.glyphicon-volume-off:before {
  content: "\e036";
}
.glyphicon-volume-down:before {
  content: "\e037";
}
.glyphicon-volume-up:before {
  content: "\e038";
}
.glyphicon-qrcode:before {
  content: "\e039";
}
.glyphicon-barcode:before {
  content: "\e040";
}
.glyphicon-tag:before {
  content: "\e041";
}
.glyphicon-tags:before {
  content: "\e042";
}
.glyphicon-book:before {
  content: "\e043";
}
.glyphicon-bookmark:before {
  content: "\e044";
}
.glyphicon-print:before {
  content: "\e045";
}
.glyphicon-camera:before {
  content: "\e046";
}
.glyphicon-font:before {
  content: "\e047";
}
.glyphicon-bold:before {
  content: "\e048";
}
.glyphicon-italic:before {
  content: "\e049";
}
.glyphicon-text-height:before {
  content: "\e050";
}
.glyphicon-text-width:before {
  content: "\e051";
}
.glyphicon-align-left:before {
  content: "\e052";
}
.glyphicon-align-center:before {
  content: "\e053";
}
.glyphicon-align-right:before {
  content: "\e054";
}
.glyphicon-align-justify:before {
  content: "\e055";
}
.glyphicon-list:before {
  content: "\e056";
}
.glyphicon-indent-left:before {
  content: "\e057";
}
.glyphicon-indent-right:before {
  content: "\e058";
}
.glyphicon-facetime-video:before {
  content: "\e059";
}
.glyphicon-picture:before {
  content: "\e060";
}
.glyphicon-map-marker:before {
  content: "\e062";
}
.glyphicon-adjust:before {
  content: "\e063";
}
.glyphicon-tint:before {
  content: "\e064";
}
.glyphicon-edit:before {
  content: "\e065";
}
.glyphicon-share:before {
  content: "\e066";
}
.glyphicon-check:before {
  content: "\e067";
}
.glyphicon-move:before {
  content: "\e068";
}
.glyphicon-step-backward:before {
  content: "\e069";
}
.glyphicon-fast-backward:before {
  content: "\e070";
}
.glyphicon-backward:before {
  content: "\e071";
}
.glyphicon-play:before {
  content: "\e072";
}
.glyphicon-pause:before {
  content: "\e073";
}
.glyphicon-stop:before {
  content: "\e074";
}
.glyphicon-forward:before {
  content: "\e075";
}
.glyphicon-fast-forward:before {
  content: "\e076";
}
.glyphicon-step-forward:before {
  content: "\e077";
}
.glyphicon-eject:before {
  content: "\e078";
}
.glyphicon-chevron-left:before {
  content: "\e079";
}
.glyphicon-chevron-right:before {
  content: "\e080";
}
.glyphicon-plus-sign:before {
  content: "\e081";
}
.glyphicon-minus-sign:before {
  content: "\e082";
}
.glyphicon-remove-sign:before {
  content: "\e083";
}
.glyphicon-ok-sign:before {
  content: "\e084";
}
.glyphicon-question-sign:before {
  content: "\e085";
}
.glyphicon-info-sign:before {
  content: "\e086";
}
.glyphicon-screenshot:before {
  content: "\e087";
}
.glyphicon-remove-circle:before {
  content: "\e088";
}
.glyphicon-ok-circle:before {
  content: "\e089";
}
.glyphicon-ban-circle:before {
  content: "\e090";
}
.glyphicon-arrow-left:before {
  content: "\e091";
}
.glyphicon-arrow-right:before {
  content: "\e092";
}
.glyphicon-arrow-up:before {
  content: "\e093";
}
.glyphicon-arrow-down:before {
  content: "\e094";
}
.glyphicon-share-alt:before {
  content: "\e095";
}
.glyphicon-resize-full:before {
  content: "\e096";
}
.glyphicon-resize-small:before {
  content: "\e097";
}
.glyphicon-exclamation-sign:before {
  content: "\e101";
}
.glyphicon-gift:before {
  content: "\e102";
}
.glyphicon-leaf:before {
  content: "\e103";
}
.glyphicon-fire:before {
  content: "\e104";
}
.glyphicon-eye-open:before {
  content: "\e105";
}
.glyphicon-eye-close:before {
  content: "\e106";
}
.glyphicon-warning-sign:before {
  content: "\e107";
}
.glyphicon-plane:before {
  content: "\e108";
}
.glyphicon-calendar:before {
  content: "\e109";
}
.glyphicon-random:before {
  content: "\e110";
}
.glyphicon-comment:before {
  content: "\e111";
}
.glyphicon-magnet:before {
  content: "\e112";
}
.glyphicon-chevron-up:before {
  content: "\e113";
}
.glyphicon-chevron-down:before {
  content: "\e114";
}
.glyphicon-retweet:before {
  content: "\e115";
}
.glyphicon-shopping-cart:before {
  content: "\e116";
}
.glyphicon-folder-close:before {
  content: "\e117";
}
.glyphicon-folder-open:before {
  content: "\e118";
}
.glyphicon-resize-vertical:before {
  content: "\e119";
}
.glyphicon-resize-horizontal:before {
  content: "\e120";
}
.glyphicon-hdd:before {
  content: "\e121";
}
.glyphicon-bullhorn:before {
  content: "\e122";
}
.glyphicon-bell:before {
  content: "\e123";
}
.glyphicon-certificate:before {
  content: "\e124";
}
.glyphicon-thumbs-up:before {
  content: "\e125";
}
.glyphicon-thumbs-down:before {
  content: "\e126";
}
.glyphicon-hand-right:before {
  content: "\e127";
}
.glyphicon-hand-left:before {
  content: "\e128";
}
.glyphicon-hand-up:before {
  content: "\e129";
}
.glyphicon-hand-down:before {
  content: "\e130";
}
.glyphicon-circle-arrow-right:before {
  content: "\e131";
}
.glyphicon-circle-arrow-left:before {
  content: "\e132";
}
.glyphicon-circle-arrow-up:before {
  content: "\e133";
}
.glyphicon-circle-arrow-down:before {
  content: "\e134";
}
.glyphicon-globe:before {
  content: "\e135";
}
.glyphicon-wrench:before {
  content: "\e136";
}
.glyphicon-tasks:before {
  content: "\e137";
}
.glyphicon-filter:before {
  content: "\e138";
}
.glyphicon-briefcase:before {
  content: "\e139";
}
.glyphicon-fullscreen:before {
  content: "\e140";
}
.glyphicon-dashboard:before {
  content: "\e141";
}
.glyphicon-paperclip:before {
  content: "\e142";
}
.glyphicon-heart-empty:before {
  content: "\e143";
}
.glyphicon-link:before {
  content: "\e144";
}
.glyphicon-phone:before {
  content: "\e145";
}
.glyphicon-pushpin:before {
  content: "\e146";
}
.glyphicon-usd:before {
  content: "\e148";
}
.glyphicon-gbp:before {
  content: "\e149";
}
.glyphicon-sort:before {
  content: "\e150";
}
.glyphicon-sort-by-alphabet:before {
  content: "\e151";
}
.glyphicon-sort-by-alphabet-alt:before {
  content: "\e152";
}
.glyphicon-sort-by-order:before {
  content: "\e153";
}
.glyphicon-sort-by-order-alt:before {
  content: "\e154";
}
.glyphicon-sort-by-attributes:before {
  content: "\e155";
}
.glyphicon-sort-by-attributes-alt:before {
  content: "\e156";
}
.glyphicon-unchecked:before {
  content: "\e157";
}
.glyphicon-expand:before {
  content: "\e158";
}
.glyphicon-collapse-down:before {
  content: "\e159";
}
.glyphicon-collapse-up:before {
  content: "\e160";
}
.glyphicon-log-in:before {
  content: "\e161";
}
.glyphicon-flash:before {
  content: "\e162";
}
.glyphicon-log-out:before {
  content: "\e163";
}
.glyphicon-new-window:before {
  content: "\e164";
}
.glyphicon-record:before {
  content: "\e165";
}
.glyphicon-save:before {
  content: "\e166";
}
.glyphicon-open:before {
  content: "\e167";
}
.glyphicon-saved:before {
  content: "\e168";
}
.glyphicon-import:before {
  content: "\e169";
}
.glyphicon-export:before {
  content: "\e170";
}
.glyphicon-send:before {
  content: "\e171";
}
.glyphicon-floppy-disk:before {
  content: "\e172";
}
.glyphicon-floppy-saved:before {
  content: "\e173";
}
.glyphicon-floppy-remove:before {
  content: "\e174";
}
.glyphicon-floppy-save:before {
  content: "\e175";
}
.glyphicon-floppy-open:before {
  content: "\e176";
}
.glyphicon-credit-card:before {
  content: "\e177";
}
.glyphicon-transfer:before {
  content: "\e178";
}
.glyphicon-cutlery:before {
  content: "\e179";
}
.glyphicon-header:before {
  content: "\e180";
}
.glyphicon-compressed:before {
  content: "\e181";
}
.glyphicon-earphone:before {
  content: "\e182";
}
.glyphicon-phone-alt:before {
  content: "\e183";
}
.glyphicon-tower:before {
  content: "\e184";
}
.glyphicon-stats:before {
  content: "\e185";
}
.glyphicon-sd-video:before {
  content: "\e186";
}
.glyphicon-hd-video:before {
  content: "\e187";
}
.glyphicon-subtitles:before {
  content: "\e188";
}
.glyphicon-sound-stereo:before {
  content: "\e189";
}
.glyphicon-sound-dolby:before {
  content: "\e190";
}
.glyphicon-sound-5-1:before {
  content: "\e191";
}
.glyphicon-sound-6-1:before {
  content: "\e192";
}
.glyphicon-sound-7-1:before {
  content: "\e193";
}
.glyphicon-copyright-mark:before {
  content: "\e194";
}
.glyphicon-registration-mark:before {
  content: "\e195";
}
.glyphicon-cloud-download:before {
  content: "\e197";
}
.glyphicon-cloud-upload:before {
  content: "\e198";
}
.glyphicon-tree-conifer:before {
  content: "\e199";
}
.glyphicon-tree-deciduous:before {
  content: "\e200";
}
.glyphicon-cd:before {
  content: "\e201";
}
.glyphicon-save-file:before {
  content: "\e202";
}
.glyphicon-open-file:before {
  content: "\e203";
}
.glyphicon-level-up:before {
  content: "\e204";
}
.glyphicon-copy:before {
  content: "\e205";
}
.glyphicon-paste:before {
  content: "\e206";
}
.glyphicon-alert:before {
  content: "\e209";
}
.glyphicon-equalizer:before {
  content: "\e210";
}
.glyphicon-king:before {
  content: "\e211";
}
.glyphicon-queen:before {
  content: "\e212";
}
.glyphicon-pawn:before {
  content: "\e213";
}
.glyphicon-bishop:before {
  content: "\e214";
}
.glyphicon-knight:before {
  content: "\e215";
}
.glyphicon-baby-formula:before {
  content: "\e216";
}
.glyphicon-tent:before {
  content: "\26fa";
}
.glyphicon-blackboard:before {
  content: "\e218";
}
.glyphicon-bed:before {
  content: "\e219";
}
.glyphicon-apple:before {
  content: "\f8ff";
}
.glyphicon-erase:before {
  content: "\e221";
}
.glyphicon-hourglass:before {
  content: "\231b";
}
.glyphicon-lamp:before {
  content: "\e223";
}
.glyphicon-duplicate:before {
  content: "\e224";
}
.glyphicon-piggy-bank:before {
  content: "\e225";
}
.glyphicon-scissors:before {
  content: "\e226";
}
.glyphicon-bitcoin:before {
  content: "\e227";
}
.glyphicon-btc:before {
  content: "\e227";
}
.glyphicon-xbt:before {
  content: "\e227";
}
.glyphicon-yen:before {
  content: "\00a5";
}
.glyphicon-jpy:before {
  content: "\00a5";
}
.glyphicon-ruble:before {
  content: "\20bd";
}
.glyphicon-rub:before {
  content: "\20bd";
}
.glyphicon-scale:before {
  content: "\e230";
}
.glyphicon-ice-lolly:before {
  content: "\e231";
}
.glyphicon-ice-lolly-tasted:before {
  content: "\e232";
}
.glyphicon-education:before {
  content: "\e233";
}
.glyphicon-option-horizontal:before {
  content: "\e234";
}
.glyphicon-option-vertical:before {
  content: "\e235";
}
.glyphicon-menu-hamburger:before {
  content: "\e236";
}
.glyphicon-modal-window:before {
  content: "\e237";
}
.glyphicon-oil:before {
  content: "\e238";
}
.glyphicon-grain:before {
  content: "\e239";
}
.glyphicon-sunglasses:before {
  content: "\e240";
}
.glyphicon-text-size:before {
  content: "\e241";
}
.glyphicon-text-color:before {
  content: "\e242";
}
.glyphicon-text-background:before {
  content: "\e243";
}
.glyphicon-object-align-top:before {
  content: "\e244";
}
.glyphicon-object-align-bottom:before {
  content: "\e245";
}
.glyphicon-object-align-horizontal:before {
  content: "\e246";
}
.glyphicon-object-align-left:before {
  content: "\e247";
}
.glyphicon-object-align-vertical:before {
  content: "\e248";
}
.glyphicon-object-align-right:before {
  content: "\e249";
}
.glyphicon-triangle-right:before {
  content: "\e250";
}
.glyphicon-triangle-left:before {
  content: "\e251";
}
.glyphicon-triangle-bottom:before {
  content: "\e252";
}
.glyphicon-triangle-top:before {
  content: "\e253";
}
.glyphicon-console:before {
  content: "\e254";
}
.glyphicon-superscript:before {
  content: "\e255";
}
.glyphicon-subscript:before {
  content: "\e256";
}
.glyphicon-menu-left:before {
  content: "\e257";
}
.glyphicon-menu-right:before {
  content: "\e258";
}
.glyphicon-menu-down:before {
  content: "\e259";
}
.glyphicon-menu-up:before {
  content: "\e260";
}
* {
  -webkit-box-sizing: border-box;
  -moz-box-sizing: border-box;
  box-sizing: border-box;
}
*:before,
*:after {
  -webkit-box-sizing: border-box;
  -moz-box-sizing: border-box;
  box-sizing: border-box;
}
html {
  font-size: 10px;
  -webkit-tap-highlight-color: rgba(0, 0, 0, 0);
}
body {
  font-family: "Helvetica Neue", Helvetica, Arial, sans-serif;
  font-size: 13px;
  line-height: 1.42857143;
  color: #000;
  background-color: #fff;
}
input,
button,
select,
textarea {
  font-family: inherit;
  font-size: inherit;
  line-height: inherit;
}
a {
  color: #337ab7;
  text-decoration: none;
}
a:hover,
a:focus {
  color: #23527c;
  text-decoration: underline;
}
a:focus {
  outline: 5px auto -webkit-focus-ring-color;
  outline-offset: -2px;
}
figure {
  margin: 0;
}
img {
  vertical-align: middle;
}
.img-responsive,
.thumbnail > img,
.thumbnail a > img,
.carousel-inner > .item > img,
.carousel-inner > .item > a > img {
  display: block;
  max-width: 100%;
  height: auto;
}
.img-rounded {
  border-radius: 3px;
}
.img-thumbnail {
  padding: 4px;
  line-height: 1.42857143;
  background-color: #fff;
  border: 1px solid #ddd;
  border-radius: 2px;
  -webkit-transition: all 0.2s ease-in-out;
  -o-transition: all 0.2s ease-in-out;
  transition: all 0.2s ease-in-out;
  display: inline-block;
  max-width: 100%;
  height: auto;
}
.img-circle {
  border-radius: 50%;
}
hr {
  margin-top: 18px;
  margin-bottom: 18px;
  border: 0;
  border-top: 1px solid #eeeeee;
}
.sr-only {
  position: absolute;
  width: 1px;
  height: 1px;
  margin: -1px;
  padding: 0;
  overflow: hidden;
  clip: rect(0, 0, 0, 0);
  border: 0;
}
.sr-only-focusable:active,
.sr-only-focusable:focus {
  position: static;
  width: auto;
  height: auto;
  margin: 0;
  overflow: visible;
  clip: auto;
}
[role="button"] {
  cursor: pointer;
}
h1,
h2,
h3,
h4,
h5,
h6,
.h1,
.h2,
.h3,
.h4,
.h5,
.h6 {
  font-family: inherit;
  font-weight: 500;
  line-height: 1.1;
  color: inherit;
}
h1 small,
h2 small,
h3 small,
h4 small,
h5 small,
h6 small,
.h1 small,
.h2 small,
.h3 small,
.h4 small,
.h5 small,
.h6 small,
h1 .small,
h2 .small,
h3 .small,
h4 .small,
h5 .small,
h6 .small,
.h1 .small,
.h2 .small,
.h3 .small,
.h4 .small,
.h5 .small,
.h6 .small {
  font-weight: normal;
  line-height: 1;
  color: #777777;
}
h1,
.h1,
h2,
.h2,
h3,
.h3 {
  margin-top: 18px;
  margin-bottom: 9px;
}
h1 small,
.h1 small,
h2 small,
.h2 small,
h3 small,
.h3 small,
h1 .small,
.h1 .small,
h2 .small,
.h2 .small,
h3 .small,
.h3 .small {
  font-size: 65%;
}
h4,
.h4,
h5,
.h5,
h6,
.h6 {
  margin-top: 9px;
  margin-bottom: 9px;
}
h4 small,
.h4 small,
h5 small,
.h5 small,
h6 small,
.h6 small,
h4 .small,
.h4 .small,
h5 .small,
.h5 .small,
h6 .small,
.h6 .small {
  font-size: 75%;
}
h1,
.h1 {
  font-size: 33px;
}
h2,
.h2 {
  font-size: 27px;
}
h3,
.h3 {
  font-size: 23px;
}
h4,
.h4 {
  font-size: 17px;
}
h5,
.h5 {
  font-size: 13px;
}
h6,
.h6 {
  font-size: 12px;
}
p {
  margin: 0 0 9px;
}
.lead {
  margin-bottom: 18px;
  font-size: 14px;
  font-weight: 300;
  line-height: 1.4;
}
@media (min-width: 768px) {
  .lead {
    font-size: 19.5px;
  }
}
small,
.small {
  font-size: 92%;
}
mark,
.mark {
  background-color: #fcf8e3;
  padding: .2em;
}
.text-left {
  text-align: left;
}
.text-right {
  text-align: right;
}
.text-center {
  text-align: center;
}
.text-justify {
  text-align: justify;
}
.text-nowrap {
  white-space: nowrap;
}
.text-lowercase {
  text-transform: lowercase;
}
.text-uppercase {
  text-transform: uppercase;
}
.text-capitalize {
  text-transform: capitalize;
}
.text-muted {
  color: #777777;
}
.text-primary {
  color: #337ab7;
}
a.text-primary:hover,
a.text-primary:focus {
  color: #286090;
}
.text-success {
  color: #3c763d;
}
a.text-success:hover,
a.text-success:focus {
  color: #2b542c;
}
.text-info {
  color: #31708f;
}
a.text-info:hover,
a.text-info:focus {
  color: #245269;
}
.text-warning {
  color: #8a6d3b;
}
a.text-warning:hover,
a.text-warning:focus {
  color: #66512c;
}
.text-danger {
  color: #a94442;
}
a.text-danger:hover,
a.text-danger:focus {
  color: #843534;
}
.bg-primary {
  color: #fff;
  background-color: #337ab7;
}
a.bg-primary:hover,
a.bg-primary:focus {
  background-color: #286090;
}
.bg-success {
  background-color: #dff0d8;
}
a.bg-success:hover,
a.bg-success:focus {
  background-color: #c1e2b3;
}
.bg-info {
  background-color: #d9edf7;
}
a.bg-info:hover,
a.bg-info:focus {
  background-color: #afd9ee;
}
.bg-warning {
  background-color: #fcf8e3;
}
a.bg-warning:hover,
a.bg-warning:focus {
  background-color: #f7ecb5;
}
.bg-danger {
  background-color: #f2dede;
}
a.bg-danger:hover,
a.bg-danger:focus {
  background-color: #e4b9b9;
}
.page-header {
  padding-bottom: 8px;
  margin: 36px 0 18px;
  border-bottom: 1px solid #eeeeee;
}
ul,
ol {
  margin-top: 0;
  margin-bottom: 9px;
}
ul ul,
ol ul,
ul ol,
ol ol {
  margin-bottom: 0;
}
.list-unstyled {
  padding-left: 0;
  list-style: none;
}
.list-inline {
  padding-left: 0;
  list-style: none;
  margin-left: -5px;
}
.list-inline > li {
  display: inline-block;
  padding-left: 5px;
  padding-right: 5px;
}
dl {
  margin-top: 0;
  margin-bottom: 18px;
}
dt,
dd {
  line-height: 1.42857143;
}
dt {
  font-weight: bold;
}
dd {
  margin-left: 0;
}
@media (min-width: 541px) {
  .dl-horizontal dt {
    float: left;
    width: 160px;
    clear: left;
    text-align: right;
    overflow: hidden;
    text-overflow: ellipsis;
    white-space: nowrap;
  }
  .dl-horizontal dd {
    margin-left: 180px;
  }
}
abbr[title],
abbr[data-original-title] {
  cursor: help;
  border-bottom: 1px dotted #777777;
}
.initialism {
  font-size: 90%;
  text-transform: uppercase;
}
blockquote {
  padding: 9px 18px;
  margin: 0 0 18px;
  font-size: inherit;
  border-left: 5px solid #eeeeee;
}
blockquote p:last-child,
blockquote ul:last-child,
blockquote ol:last-child {
  margin-bottom: 0;
}
blockquote footer,
blockquote small,
blockquote .small {
  display: block;
  font-size: 80%;
  line-height: 1.42857143;
  color: #777777;
}
blockquote footer:before,
blockquote small:before,
blockquote .small:before {
  content: '\2014 \00A0';
}
.blockquote-reverse,
blockquote.pull-right {
  padding-right: 15px;
  padding-left: 0;
  border-right: 5px solid #eeeeee;
  border-left: 0;
  text-align: right;
}
.blockquote-reverse footer:before,
blockquote.pull-right footer:before,
.blockquote-reverse small:before,
blockquote.pull-right small:before,
.blockquote-reverse .small:before,
blockquote.pull-right .small:before {
  content: '';
}
.blockquote-reverse footer:after,
blockquote.pull-right footer:after,
.blockquote-reverse small:after,
blockquote.pull-right small:after,
.blockquote-reverse .small:after,
blockquote.pull-right .small:after {
  content: '\00A0 \2014';
}
address {
  margin-bottom: 18px;
  font-style: normal;
  line-height: 1.42857143;
}
code,
kbd,
pre,
samp {
  font-family: monospace;
}
code {
  padding: 2px 4px;
  font-size: 90%;
  color: #c7254e;
  background-color: #f9f2f4;
  border-radius: 2px;
}
kbd {
  padding: 2px 4px;
  font-size: 90%;
  color: #888;
  background-color: transparent;
  border-radius: 1px;
  box-shadow: inset 0 -1px 0 rgba(0, 0, 0, 0.25);
}
kbd kbd {
  padding: 0;
  font-size: 100%;
  font-weight: bold;
  box-shadow: none;
}
pre {
  display: block;
  padding: 8.5px;
  margin: 0 0 9px;
  font-size: 12px;
  line-height: 1.42857143;
  word-break: break-all;
  word-wrap: break-word;
  color: #333333;
  background-color: #f5f5f5;
  border: 1px solid #ccc;
  border-radius: 2px;
}
pre code {
  padding: 0;
  font-size: inherit;
  color: inherit;
  white-space: pre-wrap;
  background-color: transparent;
  border-radius: 0;
}
.pre-scrollable {
  max-height: 340px;
  overflow-y: scroll;
}
.container {
  margin-right: auto;
  margin-left: auto;
  padding-left: 0px;
  padding-right: 0px;
}
@media (min-width: 768px) {
  .container {
    width: 768px;
  }
}
@media (min-width: 992px) {
  .container {
    width: 940px;
  }
}
@media (min-width: 1200px) {
  .container {
    width: 1140px;
  }
}
.container-fluid {
  margin-right: auto;
  margin-left: auto;
  padding-left: 0px;
  padding-right: 0px;
}
.row {
  margin-left: 0px;
  margin-right: 0px;
}
.col-xs-1, .col-sm-1, .col-md-1, .col-lg-1, .col-xs-2, .col-sm-2, .col-md-2, .col-lg-2, .col-xs-3, .col-sm-3, .col-md-3, .col-lg-3, .col-xs-4, .col-sm-4, .col-md-4, .col-lg-4, .col-xs-5, .col-sm-5, .col-md-5, .col-lg-5, .col-xs-6, .col-sm-6, .col-md-6, .col-lg-6, .col-xs-7, .col-sm-7, .col-md-7, .col-lg-7, .col-xs-8, .col-sm-8, .col-md-8, .col-lg-8, .col-xs-9, .col-sm-9, .col-md-9, .col-lg-9, .col-xs-10, .col-sm-10, .col-md-10, .col-lg-10, .col-xs-11, .col-sm-11, .col-md-11, .col-lg-11, .col-xs-12, .col-sm-12, .col-md-12, .col-lg-12 {
  position: relative;
  min-height: 1px;
  padding-left: 0px;
  padding-right: 0px;
}
.col-xs-1, .col-xs-2, .col-xs-3, .col-xs-4, .col-xs-5, .col-xs-6, .col-xs-7, .col-xs-8, .col-xs-9, .col-xs-10, .col-xs-11, .col-xs-12 {
  float: left;
}
.col-xs-12 {
  width: 100%;
}
.col-xs-11 {
  width: 91.66666667%;
}
.col-xs-10 {
  width: 83.33333333%;
}
.col-xs-9 {
  width: 75%;
}
.col-xs-8 {
  width: 66.66666667%;
}
.col-xs-7 {
  width: 58.33333333%;
}
.col-xs-6 {
  width: 50%;
}
.col-xs-5 {
  width: 41.66666667%;
}
.col-xs-4 {
  width: 33.33333333%;
}
.col-xs-3 {
  width: 25%;
}
.col-xs-2 {
  width: 16.66666667%;
}
.col-xs-1 {
  width: 8.33333333%;
}
.col-xs-pull-12 {
  right: 100%;
}
.col-xs-pull-11 {
  right: 91.66666667%;
}
.col-xs-pull-10 {
  right: 83.33333333%;
}
.col-xs-pull-9 {
  right: 75%;
}
.col-xs-pull-8 {
  right: 66.66666667%;
}
.col-xs-pull-7 {
  right: 58.33333333%;
}
.col-xs-pull-6 {
  right: 50%;
}
.col-xs-pull-5 {
  right: 41.66666667%;
}
.col-xs-pull-4 {
  right: 33.33333333%;
}
.col-xs-pull-3 {
  right: 25%;
}
.col-xs-pull-2 {
  right: 16.66666667%;
}
.col-xs-pull-1 {
  right: 8.33333333%;
}
.col-xs-pull-0 {
  right: auto;
}
.col-xs-push-12 {
  left: 100%;
}
.col-xs-push-11 {
  left: 91.66666667%;
}
.col-xs-push-10 {
  left: 83.33333333%;
}
.col-xs-push-9 {
  left: 75%;
}
.col-xs-push-8 {
  left: 66.66666667%;
}
.col-xs-push-7 {
  left: 58.33333333%;
}
.col-xs-push-6 {
  left: 50%;
}
.col-xs-push-5 {
  left: 41.66666667%;
}
.col-xs-push-4 {
  left: 33.33333333%;
}
.col-xs-push-3 {
  left: 25%;
}
.col-xs-push-2 {
  left: 16.66666667%;
}
.col-xs-push-1 {
  left: 8.33333333%;
}
.col-xs-push-0 {
  left: auto;
}
.col-xs-offset-12 {
  margin-left: 100%;
}
.col-xs-offset-11 {
  margin-left: 91.66666667%;
}
.col-xs-offset-10 {
  margin-left: 83.33333333%;
}
.col-xs-offset-9 {
  margin-left: 75%;
}
.col-xs-offset-8 {
  margin-left: 66.66666667%;
}
.col-xs-offset-7 {
  margin-left: 58.33333333%;
}
.col-xs-offset-6 {
  margin-left: 50%;
}
.col-xs-offset-5 {
  margin-left: 41.66666667%;
}
.col-xs-offset-4 {
  margin-left: 33.33333333%;
}
.col-xs-offset-3 {
  margin-left: 25%;
}
.col-xs-offset-2 {
  margin-left: 16.66666667%;
}
.col-xs-offset-1 {
  margin-left: 8.33333333%;
}
.col-xs-offset-0 {
  margin-left: 0%;
}
@media (min-width: 768px) {
  .col-sm-1, .col-sm-2, .col-sm-3, .col-sm-4, .col-sm-5, .col-sm-6, .col-sm-7, .col-sm-8, .col-sm-9, .col-sm-10, .col-sm-11, .col-sm-12 {
    float: left;
  }
  .col-sm-12 {
    width: 100%;
  }
  .col-sm-11 {
    width: 91.66666667%;
  }
  .col-sm-10 {
    width: 83.33333333%;
  }
  .col-sm-9 {
    width: 75%;
  }
  .col-sm-8 {
    width: 66.66666667%;
  }
  .col-sm-7 {
    width: 58.33333333%;
  }
  .col-sm-6 {
    width: 50%;
  }
  .col-sm-5 {
    width: 41.66666667%;
  }
  .col-sm-4 {
    width: 33.33333333%;
  }
  .col-sm-3 {
    width: 25%;
  }
  .col-sm-2 {
    width: 16.66666667%;
  }
  .col-sm-1 {
    width: 8.33333333%;
  }
  .col-sm-pull-12 {
    right: 100%;
  }
  .col-sm-pull-11 {
    right: 91.66666667%;
  }
  .col-sm-pull-10 {
    right: 83.33333333%;
  }
  .col-sm-pull-9 {
    right: 75%;
  }
  .col-sm-pull-8 {
    right: 66.66666667%;
  }
  .col-sm-pull-7 {
    right: 58.33333333%;
  }
  .col-sm-pull-6 {
    right: 50%;
  }
  .col-sm-pull-5 {
    right: 41.66666667%;
  }
  .col-sm-pull-4 {
    right: 33.33333333%;
  }
  .col-sm-pull-3 {
    right: 25%;
  }
  .col-sm-pull-2 {
    right: 16.66666667%;
  }
  .col-sm-pull-1 {
    right: 8.33333333%;
  }
  .col-sm-pull-0 {
    right: auto;
  }
  .col-sm-push-12 {
    left: 100%;
  }
  .col-sm-push-11 {
    left: 91.66666667%;
  }
  .col-sm-push-10 {
    left: 83.33333333%;
  }
  .col-sm-push-9 {
    left: 75%;
  }
  .col-sm-push-8 {
    left: 66.66666667%;
  }
  .col-sm-push-7 {
    left: 58.33333333%;
  }
  .col-sm-push-6 {
    left: 50%;
  }
  .col-sm-push-5 {
    left: 41.66666667%;
  }
  .col-sm-push-4 {
    left: 33.33333333%;
  }
  .col-sm-push-3 {
    left: 25%;
  }
  .col-sm-push-2 {
    left: 16.66666667%;
  }
  .col-sm-push-1 {
    left: 8.33333333%;
  }
  .col-sm-push-0 {
    left: auto;
  }
  .col-sm-offset-12 {
    margin-left: 100%;
  }
  .col-sm-offset-11 {
    margin-left: 91.66666667%;
  }
  .col-sm-offset-10 {
    margin-left: 83.33333333%;
  }
  .col-sm-offset-9 {
    margin-left: 75%;
  }
  .col-sm-offset-8 {
    margin-left: 66.66666667%;
  }
  .col-sm-offset-7 {
    margin-left: 58.33333333%;
  }
  .col-sm-offset-6 {
    margin-left: 50%;
  }
  .col-sm-offset-5 {
    margin-left: 41.66666667%;
  }
  .col-sm-offset-4 {
    margin-left: 33.33333333%;
  }
  .col-sm-offset-3 {
    margin-left: 25%;
  }
  .col-sm-offset-2 {
    margin-left: 16.66666667%;
  }
  .col-sm-offset-1 {
    margin-left: 8.33333333%;
  }
  .col-sm-offset-0 {
    margin-left: 0%;
  }
}
@media (min-width: 992px) {
  .col-md-1, .col-md-2, .col-md-3, .col-md-4, .col-md-5, .col-md-6, .col-md-7, .col-md-8, .col-md-9, .col-md-10, .col-md-11, .col-md-12 {
    float: left;
  }
  .col-md-12 {
    width: 100%;
  }
  .col-md-11 {
    width: 91.66666667%;
  }
  .col-md-10 {
    width: 83.33333333%;
  }
  .col-md-9 {
    width: 75%;
  }
  .col-md-8 {
    width: 66.66666667%;
  }
  .col-md-7 {
    width: 58.33333333%;
  }
  .col-md-6 {
    width: 50%;
  }
  .col-md-5 {
    width: 41.66666667%;
  }
  .col-md-4 {
    width: 33.33333333%;
  }
  .col-md-3 {
    width: 25%;
  }
  .col-md-2 {
    width: 16.66666667%;
  }
  .col-md-1 {
    width: 8.33333333%;
  }
  .col-md-pull-12 {
    right: 100%;
  }
  .col-md-pull-11 {
    right: 91.66666667%;
  }
  .col-md-pull-10 {
    right: 83.33333333%;
  }
  .col-md-pull-9 {
    right: 75%;
  }
  .col-md-pull-8 {
    right: 66.66666667%;
  }
  .col-md-pull-7 {
    right: 58.33333333%;
  }
  .col-md-pull-6 {
    right: 50%;
  }
  .col-md-pull-5 {
    right: 41.66666667%;
  }
  .col-md-pull-4 {
    right: 33.33333333%;
  }
  .col-md-pull-3 {
    right: 25%;
  }
  .col-md-pull-2 {
    right: 16.66666667%;
  }
  .col-md-pull-1 {
    right: 8.33333333%;
  }
  .col-md-pull-0 {
    right: auto;
  }
  .col-md-push-12 {
    left: 100%;
  }
  .col-md-push-11 {
    left: 91.66666667%;
  }
  .col-md-push-10 {
    left: 83.33333333%;
  }
  .col-md-push-9 {
    left: 75%;
  }
  .col-md-push-8 {
    left: 66.66666667%;
  }
  .col-md-push-7 {
    left: 58.33333333%;
  }
  .col-md-push-6 {
    left: 50%;
  }
  .col-md-push-5 {
    left: 41.66666667%;
  }
  .col-md-push-4 {
    left: 33.33333333%;
  }
  .col-md-push-3 {
    left: 25%;
  }
  .col-md-push-2 {
    left: 16.66666667%;
  }
  .col-md-push-1 {
    left: 8.33333333%;
  }
  .col-md-push-0 {
    left: auto;
  }
  .col-md-offset-12 {
    margin-left: 100%;
  }
  .col-md-offset-11 {
    margin-left: 91.66666667%;
  }
  .col-md-offset-10 {
    margin-left: 83.33333333%;
  }
  .col-md-offset-9 {
    margin-left: 75%;
  }
  .col-md-offset-8 {
    margin-left: 66.66666667%;
  }
  .col-md-offset-7 {
    margin-left: 58.33333333%;
  }
  .col-md-offset-6 {
    margin-left: 50%;
  }
  .col-md-offset-5 {
    margin-left: 41.66666667%;
  }
  .col-md-offset-4 {
    margin-left: 33.33333333%;
  }
  .col-md-offset-3 {
    margin-left: 25%;
  }
  .col-md-offset-2 {
    margin-left: 16.66666667%;
  }
  .col-md-offset-1 {
    margin-left: 8.33333333%;
  }
  .col-md-offset-0 {
    margin-left: 0%;
  }
}
@media (min-width: 1200px) {
  .col-lg-1, .col-lg-2, .col-lg-3, .col-lg-4, .col-lg-5, .col-lg-6, .col-lg-7, .col-lg-8, .col-lg-9, .col-lg-10, .col-lg-11, .col-lg-12 {
    float: left;
  }
  .col-lg-12 {
    width: 100%;
  }
  .col-lg-11 {
    width: 91.66666667%;
  }
  .col-lg-10 {
    width: 83.33333333%;
  }
  .col-lg-9 {
    width: 75%;
  }
  .col-lg-8 {
    width: 66.66666667%;
  }
  .col-lg-7 {
    width: 58.33333333%;
  }
  .col-lg-6 {
    width: 50%;
  }
  .col-lg-5 {
    width: 41.66666667%;
  }
  .col-lg-4 {
    width: 33.33333333%;
  }
  .col-lg-3 {
    width: 25%;
  }
  .col-lg-2 {
    width: 16.66666667%;
  }
  .col-lg-1 {
    width: 8.33333333%;
  }
  .col-lg-pull-12 {
    right: 100%;
  }
  .col-lg-pull-11 {
    right: 91.66666667%;
  }
  .col-lg-pull-10 {
    right: 83.33333333%;
  }
  .col-lg-pull-9 {
    right: 75%;
  }
  .col-lg-pull-8 {
    right: 66.66666667%;
  }
  .col-lg-pull-7 {
    right: 58.33333333%;
  }
  .col-lg-pull-6 {
    right: 50%;
  }
  .col-lg-pull-5 {
    right: 41.66666667%;
  }
  .col-lg-pull-4 {
    right: 33.33333333%;
  }
  .col-lg-pull-3 {
    right: 25%;
  }
  .col-lg-pull-2 {
    right: 16.66666667%;
  }
  .col-lg-pull-1 {
    right: 8.33333333%;
  }
  .col-lg-pull-0 {
    right: auto;
  }
  .col-lg-push-12 {
    left: 100%;
  }
  .col-lg-push-11 {
    left: 91.66666667%;
  }
  .col-lg-push-10 {
    left: 83.33333333%;
  }
  .col-lg-push-9 {
    left: 75%;
  }
  .col-lg-push-8 {
    left: 66.66666667%;
  }
  .col-lg-push-7 {
    left: 58.33333333%;
  }
  .col-lg-push-6 {
    left: 50%;
  }
  .col-lg-push-5 {
    left: 41.66666667%;
  }
  .col-lg-push-4 {
    left: 33.33333333%;
  }
  .col-lg-push-3 {
    left: 25%;
  }
  .col-lg-push-2 {
    left: 16.66666667%;
  }
  .col-lg-push-1 {
    left: 8.33333333%;
  }
  .col-lg-push-0 {
    left: auto;
  }
  .col-lg-offset-12 {
    margin-left: 100%;
  }
  .col-lg-offset-11 {
    margin-left: 91.66666667%;
  }
  .col-lg-offset-10 {
    margin-left: 83.33333333%;
  }
  .col-lg-offset-9 {
    margin-left: 75%;
  }
  .col-lg-offset-8 {
    margin-left: 66.66666667%;
  }
  .col-lg-offset-7 {
    margin-left: 58.33333333%;
  }
  .col-lg-offset-6 {
    margin-left: 50%;
  }
  .col-lg-offset-5 {
    margin-left: 41.66666667%;
  }
  .col-lg-offset-4 {
    margin-left: 33.33333333%;
  }
  .col-lg-offset-3 {
    margin-left: 25%;
  }
  .col-lg-offset-2 {
    margin-left: 16.66666667%;
  }
  .col-lg-offset-1 {
    margin-left: 8.33333333%;
  }
  .col-lg-offset-0 {
    margin-left: 0%;
  }
}
table {
  background-color: transparent;
}
caption {
  padding-top: 8px;
  padding-bottom: 8px;
  color: #777777;
  text-align: left;
}
th {
  text-align: left;
}
.table {
  width: 100%;
  max-width: 100%;
  margin-bottom: 18px;
}
.table > thead > tr > th,
.table > tbody > tr > th,
.table > tfoot > tr > th,
.table > thead > tr > td,
.table > tbody > tr > td,
.table > tfoot > tr > td {
  padding: 8px;
  line-height: 1.42857143;
  vertical-align: top;
  border-top: 1px solid #ddd;
}
.table > thead > tr > th {
  vertical-align: bottom;
  border-bottom: 2px solid #ddd;
}
.table > caption + thead > tr:first-child > th,
.table > colgroup + thead > tr:first-child > th,
.table > thead:first-child > tr:first-child > th,
.table > caption + thead > tr:first-child > td,
.table > colgroup + thead > tr:first-child > td,
.table > thead:first-child > tr:first-child > td {
  border-top: 0;
}
.table > tbody + tbody {
  border-top: 2px solid #ddd;
}
.table .table {
  background-color: #fff;
}
.table-condensed > thead > tr > th,
.table-condensed > tbody > tr > th,
.table-condensed > tfoot > tr > th,
.table-condensed > thead > tr > td,
.table-condensed > tbody > tr > td,
.table-condensed > tfoot > tr > td {
  padding: 5px;
}
.table-bordered {
  border: 1px solid #ddd;
}
.table-bordered > thead > tr > th,
.table-bordered > tbody > tr > th,
.table-bordered > tfoot > tr > th,
.table-bordered > thead > tr > td,
.table-bordered > tbody > tr > td,
.table-bordered > tfoot > tr > td {
  border: 1px solid #ddd;
}
.table-bordered > thead > tr > th,
.table-bordered > thead > tr > td {
  border-bottom-width: 2px;
}
.table-striped > tbody > tr:nth-of-type(odd) {
  background-color: #f9f9f9;
}
.table-hover > tbody > tr:hover {
  background-color: #f5f5f5;
}
table col[class*="col-"] {
  position: static;
  float: none;
  display: table-column;
}
table td[class*="col-"],
table th[class*="col-"] {
  position: static;
  float: none;
  display: table-cell;
}
.table > thead > tr > td.active,
.table > tbody > tr > td.active,
.table > tfoot > tr > td.active,
.table > thead > tr > th.active,
.table > tbody > tr > th.active,
.table > tfoot > tr > th.active,
.table > thead > tr.active > td,
.table > tbody > tr.active > td,
.table > tfoot > tr.active > td,
.table > thead > tr.active > th,
.table > tbody > tr.active > th,
.table > tfoot > tr.active > th {
  background-color: #f5f5f5;
}
.table-hover > tbody > tr > td.active:hover,
.table-hover > tbody > tr > th.active:hover,
.table-hover > tbody > tr.active:hover > td,
.table-hover > tbody > tr:hover > .active,
.table-hover > tbody > tr.active:hover > th {
  background-color: #e8e8e8;
}
.table > thead > tr > td.success,
.table > tbody > tr > td.success,
.table > tfoot > tr > td.success,
.table > thead > tr > th.success,
.table > tbody > tr > th.success,
.table > tfoot > tr > th.success,
.table > thead > tr.success > td,
.table > tbody > tr.success > td,
.table > tfoot > tr.success > td,
.table > thead > tr.success > th,
.table > tbody > tr.success > th,
.table > tfoot > tr.success > th {
  background-color: #dff0d8;
}
.table-hover > tbody > tr > td.success:hover,
.table-hover > tbody > tr > th.success:hover,
.table-hover > tbody > tr.success:hover > td,
.table-hover > tbody > tr:hover > .success,
.table-hover > tbody > tr.success:hover > th {
  background-color: #d0e9c6;
}
.table > thead > tr > td.info,
.table > tbody > tr > td.info,
.table > tfoot > tr > td.info,
.table > thead > tr > th.info,
.table > tbody > tr > th.info,
.table > tfoot > tr > th.info,
.table > thead > tr.info > td,
.table > tbody > tr.info > td,
.table > tfoot > tr.info > td,
.table > thead > tr.info > th,
.table > tbody > tr.info > th,
.table > tfoot > tr.info > th {
  background-color: #d9edf7;
}
.table-hover > tbody > tr > td.info:hover,
.table-hover > tbody > tr > th.info:hover,
.table-hover > tbody > tr.info:hover > td,
.table-hover > tbody > tr:hover > .info,
.table-hover > tbody > tr.info:hover > th {
  background-color: #c4e3f3;
}
.table > thead > tr > td.warning,
.table > tbody > tr > td.warning,
.table > tfoot > tr > td.warning,
.table > thead > tr > th.warning,
.table > tbody > tr > th.warning,
.table > tfoot > tr > th.warning,
.table > thead > tr.warning > td,
.table > tbody > tr.warning > td,
.table > tfoot > tr.warning > td,
.table > thead > tr.warning > th,
.table > tbody > tr.warning > th,
.table > tfoot > tr.warning > th {
  background-color: #fcf8e3;
}
.table-hover > tbody > tr > td.warning:hover,
.table-hover > tbody > tr > th.warning:hover,
.table-hover > tbody > tr.warning:hover > td,
.table-hover > tbody > tr:hover > .warning,
.table-hover > tbody > tr.warning:hover > th {
  background-color: #faf2cc;
}
.table > thead > tr > td.danger,
.table > tbody > tr > td.danger,
.table > tfoot > tr > td.danger,
.table > thead > tr > th.danger,
.table > tbody > tr > th.danger,
.table > tfoot > tr > th.danger,
.table > thead > tr.danger > td,
.table > tbody > tr.danger > td,
.table > tfoot > tr.danger > td,
.table > thead > tr.danger > th,
.table > tbody > tr.danger > th,
.table > tfoot > tr.danger > th {
  background-color: #f2dede;
}
.table-hover > tbody > tr > td.danger:hover,
.table-hover > tbody > tr > th.danger:hover,
.table-hover > tbody > tr.danger:hover > td,
.table-hover > tbody > tr:hover > .danger,
.table-hover > tbody > tr.danger:hover > th {
  background-color: #ebcccc;
}
.table-responsive {
  overflow-x: auto;
  min-height: 0.01%;
}
@media screen and (max-width: 767px) {
  .table-responsive {
    width: 100%;
    margin-bottom: 13.5px;
    overflow-y: hidden;
    -ms-overflow-style: -ms-autohiding-scrollbar;
    border: 1px solid #ddd;
  }
  .table-responsive > .table {
    margin-bottom: 0;
  }
  .table-responsive > .table > thead > tr > th,
  .table-responsive > .table > tbody > tr > th,
  .table-responsive > .table > tfoot > tr > th,
  .table-responsive > .table > thead > tr > td,
  .table-responsive > .table > tbody > tr > td,
  .table-responsive > .table > tfoot > tr > td {
    white-space: nowrap;
  }
  .table-responsive > .table-bordered {
    border: 0;
  }
  .table-responsive > .table-bordered > thead > tr > th:first-child,
  .table-responsive > .table-bordered > tbody > tr > th:first-child,
  .table-responsive > .table-bordered > tfoot > tr > th:first-child,
  .table-responsive > .table-bordered > thead > tr > td:first-child,
  .table-responsive > .table-bordered > tbody > tr > td:first-child,
  .table-responsive > .table-bordered > tfoot > tr > td:first-child {
    border-left: 0;
  }
  .table-responsive > .table-bordered > thead > tr > th:last-child,
  .table-responsive > .table-bordered > tbody > tr > th:last-child,
  .table-responsive > .table-bordered > tfoot > tr > th:last-child,
  .table-responsive > .table-bordered > thead > tr > td:last-child,
  .table-responsive > .table-bordered > tbody > tr > td:last-child,
  .table-responsive > .table-bordered > tfoot > tr > td:last-child {
    border-right: 0;
  }
  .table-responsive > .table-bordered > tbody > tr:last-child > th,
  .table-responsive > .table-bordered > tfoot > tr:last-child > th,
  .table-responsive > .table-bordered > tbody > tr:last-child > td,
  .table-responsive > .table-bordered > tfoot > tr:last-child > td {
    border-bottom: 0;
  }
}
fieldset {
  padding: 0;
  margin: 0;
  border: 0;
  min-width: 0;
}
legend {
  display: block;
  width: 100%;
  padding: 0;
  margin-bottom: 18px;
  font-size: 19.5px;
  line-height: inherit;
  color: #333333;
  border: 0;
  border-bottom: 1px solid #e5e5e5;
}
label {
  display: inline-block;
  max-width: 100%;
  margin-bottom: 5px;
  font-weight: bold;
}
input[type="search"] {
  -webkit-box-sizing: border-box;
  -moz-box-sizing: border-box;
  box-sizing: border-box;
}
input[type="radio"],
input[type="checkbox"] {
  margin: 4px 0 0;
  margin-top: 1px \9;
  line-height: normal;
}
input[type="file"] {
  display: block;
}
input[type="range"] {
  display: block;
  width: 100%;
}
select[multiple],
select[size] {
  height: auto;
}
input[type="file"]:focus,
input[type="radio"]:focus,
input[type="checkbox"]:focus {
  outline: 5px auto -webkit-focus-ring-color;
  outline-offset: -2px;
}
output {
  display: block;
  padding-top: 7px;
  font-size: 13px;
  line-height: 1.42857143;
  color: #555555;
}
.form-control {
  display: block;
  width: 100%;
  height: 32px;
  padding: 6px 12px;
  font-size: 13px;
  line-height: 1.42857143;
  color: #555555;
  background-color: #fff;
  background-image: none;
  border: 1px solid #ccc;
  border-radius: 2px;
  -webkit-box-shadow: inset 0 1px 1px rgba(0, 0, 0, 0.075);
  box-shadow: inset 0 1px 1px rgba(0, 0, 0, 0.075);
  -webkit-transition: border-color ease-in-out .15s, box-shadow ease-in-out .15s;
  -o-transition: border-color ease-in-out .15s, box-shadow ease-in-out .15s;
  transition: border-color ease-in-out .15s, box-shadow ease-in-out .15s;
}
.form-control:focus {
  border-color: #66afe9;
  outline: 0;
  -webkit-box-shadow: inset 0 1px 1px rgba(0,0,0,.075), 0 0 8px rgba(102, 175, 233, 0.6);
  box-shadow: inset 0 1px 1px rgba(0,0,0,.075), 0 0 8px rgba(102, 175, 233, 0.6);
}
.form-control::-moz-placeholder {
  color: #999;
  opacity: 1;
}
.form-control:-ms-input-placeholder {
  color: #999;
}
.form-control::-webkit-input-placeholder {
  color: #999;
}
.form-control::-ms-expand {
  border: 0;
  background-color: transparent;
}
.form-control[disabled],
.form-control[readonly],
fieldset[disabled] .form-control {
  background-color: #eeeeee;
  opacity: 1;
}
.form-control[disabled],
fieldset[disabled] .form-control {
  cursor: not-allowed;
}
textarea.form-control {
  height: auto;
}
input[type="search"] {
  -webkit-appearance: none;
}
@media screen and (-webkit-min-device-pixel-ratio: 0) {
  input[type="date"].form-control,
  input[type="time"].form-control,
  input[type="datetime-local"].form-control,
  input[type="month"].form-control {
    line-height: 32px;
  }
  input[type="date"].input-sm,
  input[type="time"].input-sm,
  input[type="datetime-local"].input-sm,
  input[type="month"].input-sm,
  .input-group-sm input[type="date"],
  .input-group-sm input[type="time"],
  .input-group-sm input[type="datetime-local"],
  .input-group-sm input[type="month"] {
    line-height: 30px;
  }
  input[type="date"].input-lg,
  input[type="time"].input-lg,
  input[type="datetime-local"].input-lg,
  input[type="month"].input-lg,
  .input-group-lg input[type="date"],
  .input-group-lg input[type="time"],
  .input-group-lg input[type="datetime-local"],
  .input-group-lg input[type="month"] {
    line-height: 45px;
  }
}
.form-group {
  margin-bottom: 15px;
}
.radio,
.checkbox {
  position: relative;
  display: block;
  margin-top: 10px;
  margin-bottom: 10px;
}
.radio label,
.checkbox label {
  min-height: 18px;
  padding-left: 20px;
  margin-bottom: 0;
  font-weight: normal;
  cursor: pointer;
}
.radio input[type="radio"],
.radio-inline input[type="radio"],
.checkbox input[type="checkbox"],
.checkbox-inline input[type="checkbox"] {
  position: absolute;
  margin-left: -20px;
  margin-top: 4px \9;
}
.radio + .radio,
.checkbox + .checkbox {
  margin-top: -5px;
}
.radio-inline,
.checkbox-inline {
  position: relative;
  display: inline-block;
  padding-left: 20px;
  margin-bottom: 0;
  vertical-align: middle;
  font-weight: normal;
  cursor: pointer;
}
.radio-inline + .radio-inline,
.checkbox-inline + .checkbox-inline {
  margin-top: 0;
  margin-left: 10px;
}
input[type="radio"][disabled],
input[type="checkbox"][disabled],
input[type="radio"].disabled,
input[type="checkbox"].disabled,
fieldset[disabled] input[type="radio"],
fieldset[disabled] input[type="checkbox"] {
  cursor: not-allowed;
}
.radio-inline.disabled,
.checkbox-inline.disabled,
fieldset[disabled] .radio-inline,
fieldset[disabled] .checkbox-inline {
  cursor: not-allowed;
}
.radio.disabled label,
.checkbox.disabled label,
fieldset[disabled] .radio label,
fieldset[disabled] .checkbox label {
  cursor: not-allowed;
}
.form-control-static {
  padding-top: 7px;
  padding-bottom: 7px;
  margin-bottom: 0;
  min-height: 31px;
}
.form-control-static.input-lg,
.form-control-static.input-sm {
  padding-left: 0;
  padding-right: 0;
}
.input-sm {
  height: 30px;
  padding: 5px 10px;
  font-size: 12px;
  line-height: 1.5;
  border-radius: 1px;
}
select.input-sm {
  height: 30px;
  line-height: 30px;
}
textarea.input-sm,
select[multiple].input-sm {
  height: auto;
}
.form-group-sm .form-control {
  height: 30px;
  padding: 5px 10px;
  font-size: 12px;
  line-height: 1.5;
  border-radius: 1px;
}
.form-group-sm select.form-control {
  height: 30px;
  line-height: 30px;
}
.form-group-sm textarea.form-control,
.form-group-sm select[multiple].form-control {
  height: auto;
}
.form-group-sm .form-control-static {
  height: 30px;
  min-height: 30px;
  padding: 6px 10px;
  font-size: 12px;
  line-height: 1.5;
}
.input-lg {
  height: 45px;
  padding: 10px 16px;
  font-size: 17px;
  line-height: 1.3333333;
  border-radius: 3px;
}
select.input-lg {
  height: 45px;
  line-height: 45px;
}
textarea.input-lg,
select[multiple].input-lg {
  height: auto;
}
.form-group-lg .form-control {
  height: 45px;
  padding: 10px 16px;
  font-size: 17px;
  line-height: 1.3333333;
  border-radius: 3px;
}
.form-group-lg select.form-control {
  height: 45px;
  line-height: 45px;
}
.form-group-lg textarea.form-control,
.form-group-lg select[multiple].form-control {
  height: auto;
}
.form-group-lg .form-control-static {
  height: 45px;
  min-height: 35px;
  padding: 11px 16px;
  font-size: 17px;
  line-height: 1.3333333;
}
.has-feedback {
  position: relative;
}
.has-feedback .form-control {
  padding-right: 40px;
}
.form-control-feedback {
  position: absolute;
  top: 0;
  right: 0;
  z-index: 2;
  display: block;
  width: 32px;
  height: 32px;
  line-height: 32px;
  text-align: center;
  pointer-events: none;
}
.input-lg + .form-control-feedback,
.input-group-lg + .form-control-feedback,
.form-group-lg .form-control + .form-control-feedback {
  width: 45px;
  height: 45px;
  line-height: 45px;
}
.input-sm + .form-control-feedback,
.input-group-sm + .form-control-feedback,
.form-group-sm .form-control + .form-control-feedback {
  width: 30px;
  height: 30px;
  line-height: 30px;
}
.has-success .help-block,
.has-success .control-label,
.has-success .radio,
.has-success .checkbox,
.has-success .radio-inline,
.has-success .checkbox-inline,
.has-success.radio label,
.has-success.checkbox label,
.has-success.radio-inline label,
.has-success.checkbox-inline label {
  color: #3c763d;
}
.has-success .form-control {
  border-color: #3c763d;
  -webkit-box-shadow: inset 0 1px 1px rgba(0, 0, 0, 0.075);
  box-shadow: inset 0 1px 1px rgba(0, 0, 0, 0.075);
}
.has-success .form-control:focus {
  border-color: #2b542c;
  -webkit-box-shadow: inset 0 1px 1px rgba(0, 0, 0, 0.075), 0 0 6px #67b168;
  box-shadow: inset 0 1px 1px rgba(0, 0, 0, 0.075), 0 0 6px #67b168;
}
.has-success .input-group-addon {
  color: #3c763d;
  border-color: #3c763d;
  background-color: #dff0d8;
}
.has-success .form-control-feedback {
  color: #3c763d;
}
.has-warning .help-block,
.has-warning .control-label,
.has-warning .radio,
.has-warning .checkbox,
.has-warning .radio-inline,
.has-warning .checkbox-inline,
.has-warning.radio label,
.has-warning.checkbox label,
.has-warning.radio-inline label,
.has-warning.checkbox-inline label {
  color: #8a6d3b;
}
.has-warning .form-control {
  border-color: #8a6d3b;
  -webkit-box-shadow: inset 0 1px 1px rgba(0, 0, 0, 0.075);
  box-shadow: inset 0 1px 1px rgba(0, 0, 0, 0.075);
}
.has-warning .form-control:focus {
  border-color: #66512c;
  -webkit-box-shadow: inset 0 1px 1px rgba(0, 0, 0, 0.075), 0 0 6px #c0a16b;
  box-shadow: inset 0 1px 1px rgba(0, 0, 0, 0.075), 0 0 6px #c0a16b;
}
.has-warning .input-group-addon {
  color: #8a6d3b;
  border-color: #8a6d3b;
  background-color: #fcf8e3;
}
.has-warning .form-control-feedback {
  color: #8a6d3b;
}
.has-error .help-block,
.has-error .control-label,
.has-error .radio,
.has-error .checkbox,
.has-error .radio-inline,
.has-error .checkbox-inline,
.has-error.radio label,
.has-error.checkbox label,
.has-error.radio-inline label,
.has-error.checkbox-inline label {
  color: #a94442;
}
.has-error .form-control {
  border-color: #a94442;
  -webkit-box-shadow: inset 0 1px 1px rgba(0, 0, 0, 0.075);
  box-shadow: inset 0 1px 1px rgba(0, 0, 0, 0.075);
}
.has-error .form-control:focus {
  border-color: #843534;
  -webkit-box-shadow: inset 0 1px 1px rgba(0, 0, 0, 0.075), 0 0 6px #ce8483;
  box-shadow: inset 0 1px 1px rgba(0, 0, 0, 0.075), 0 0 6px #ce8483;
}
.has-error .input-group-addon {
  color: #a94442;
  border-color: #a94442;
  background-color: #f2dede;
}
.has-error .form-control-feedback {
  color: #a94442;
}
.has-feedback label ~ .form-control-feedback {
  top: 23px;
}
.has-feedback label.sr-only ~ .form-control-feedback {
  top: 0;
}
.help-block {
  display: block;
  margin-top: 5px;
  margin-bottom: 10px;
  color: #404040;
}
@media (min-width: 768px) {
  .form-inline .form-group {
    display: inline-block;
    margin-bottom: 0;
    vertical-align: middle;
  }
  .form-inline .form-control {
    display: inline-block;
    width: auto;
    vertical-align: middle;
  }
  .form-inline .form-control-static {
    display: inline-block;
  }
  .form-inline .input-group {
    display: inline-table;
    vertical-align: middle;
  }
  .form-inline .input-group .input-group-addon,
  .form-inline .input-group .input-group-btn,
  .form-inline .input-group .form-control {
    width: auto;
  }
  .form-inline .input-group > .form-control {
    width: 100%;
  }
  .form-inline .control-label {
    margin-bottom: 0;
    vertical-align: middle;
  }
  .form-inline .radio,
  .form-inline .checkbox {
    display: inline-block;
    margin-top: 0;
    margin-bottom: 0;
    vertical-align: middle;
  }
  .form-inline .radio label,
  .form-inline .checkbox label {
    padding-left: 0;
  }
  .form-inline .radio input[type="radio"],
  .form-inline .checkbox input[type="checkbox"] {
    position: relative;
    margin-left: 0;
  }
  .form-inline .has-feedback .form-control-feedback {
    top: 0;
  }
}
.form-horizontal .radio,
.form-horizontal .checkbox,
.form-horizontal .radio-inline,
.form-horizontal .checkbox-inline {
  margin-top: 0;
  margin-bottom: 0;
  padding-top: 7px;
}
.form-horizontal .radio,
.form-horizontal .checkbox {
  min-height: 25px;
}
.form-horizontal .form-group {
  margin-left: 0px;
  margin-right: 0px;
}
@media (min-width: 768px) {
  .form-horizontal .control-label {
    text-align: right;
    margin-bottom: 0;
    padding-top: 7px;
  }
}
.form-horizontal .has-feedback .form-control-feedback {
  right: 0px;
}
@media (min-width: 768px) {
  .form-horizontal .form-group-lg .control-label {
    padding-top: 11px;
    font-size: 17px;
  }
}
@media (min-width: 768px) {
  .form-horizontal .form-group-sm .control-label {
    padding-top: 6px;
    font-size: 12px;
  }
}
.btn {
  display: inline-block;
  margin-bottom: 0;
  font-weight: normal;
  text-align: center;
  vertical-align: middle;
  touch-action: manipulation;
  cursor: pointer;
  background-image: none;
  border: 1px solid transparent;
  white-space: nowrap;
  padding: 6px 12px;
  font-size: 13px;
  line-height: 1.42857143;
  border-radius: 2px;
  -webkit-user-select: none;
  -moz-user-select: none;
  -ms-user-select: none;
  user-select: none;
}
.btn:focus,
.btn:active:focus,
.btn.active:focus,
.btn.focus,
.btn:active.focus,
.btn.active.focus {
  outline: 5px auto -webkit-focus-ring-color;
  outline-offset: -2px;
}
.btn:hover,
.btn:focus,
.btn.focus {
  color: #333;
  text-decoration: none;
}
.btn:active,
.btn.active {
  outline: 0;
  background-image: none;
  -webkit-box-shadow: inset 0 3px 5px rgba(0, 0, 0, 0.125);
  box-shadow: inset 0 3px 5px rgba(0, 0, 0, 0.125);
}
.btn.disabled,
.btn[disabled],
fieldset[disabled] .btn {
  cursor: not-allowed;
  opacity: 0.65;
  filter: alpha(opacity=65);
  -webkit-box-shadow: none;
  box-shadow: none;
}
a.btn.disabled,
fieldset[disabled] a.btn {
  pointer-events: none;
}
.btn-default {
  color: #333;
  background-color: #fff;
  border-color: #ccc;
}
.btn-default:focus,
.btn-default.focus {
  color: #333;
  background-color: #e6e6e6;
  border-color: #8c8c8c;
}
.btn-default:hover {
  color: #333;
  background-color: #e6e6e6;
  border-color: #adadad;
}
.btn-default:active,
.btn-default.active,
.open > .dropdown-toggle.btn-default {
  color: #333;
  background-color: #e6e6e6;
  border-color: #adadad;
}
.btn-default:active:hover,
.btn-default.active:hover,
.open > .dropdown-toggle.btn-default:hover,
.btn-default:active:focus,
.btn-default.active:focus,
.open > .dropdown-toggle.btn-default:focus,
.btn-default:active.focus,
.btn-default.active.focus,
.open > .dropdown-toggle.btn-default.focus {
  color: #333;
  background-color: #d4d4d4;
  border-color: #8c8c8c;
}
.btn-default:active,
.btn-default.active,
.open > .dropdown-toggle.btn-default {
  background-image: none;
}
.btn-default.disabled:hover,
.btn-default[disabled]:hover,
fieldset[disabled] .btn-default:hover,
.btn-default.disabled:focus,
.btn-default[disabled]:focus,
fieldset[disabled] .btn-default:focus,
.btn-default.disabled.focus,
.btn-default[disabled].focus,
fieldset[disabled] .btn-default.focus {
  background-color: #fff;
  border-color: #ccc;
}
.btn-default .badge {
  color: #fff;
  background-color: #333;
}
.btn-primary {
  color: #fff;
  background-color: #337ab7;
  border-color: #2e6da4;
}
.btn-primary:focus,
.btn-primary.focus {
  color: #fff;
  background-color: #286090;
  border-color: #122b40;
}
.btn-primary:hover {
  color: #fff;
  background-color: #286090;
  border-color: #204d74;
}
.btn-primary:active,
.btn-primary.active,
.open > .dropdown-toggle.btn-primary {
  color: #fff;
  background-color: #286090;
  border-color: #204d74;
}
.btn-primary:active:hover,
.btn-primary.active:hover,
.open > .dropdown-toggle.btn-primary:hover,
.btn-primary:active:focus,
.btn-primary.active:focus,
.open > .dropdown-toggle.btn-primary:focus,
.btn-primary:active.focus,
.btn-primary.active.focus,
.open > .dropdown-toggle.btn-primary.focus {
  color: #fff;
  background-color: #204d74;
  border-color: #122b40;
}
.btn-primary:active,
.btn-primary.active,
.open > .dropdown-toggle.btn-primary {
  background-image: none;
}
.btn-primary.disabled:hover,
.btn-primary[disabled]:hover,
fieldset[disabled] .btn-primary:hover,
.btn-primary.disabled:focus,
.btn-primary[disabled]:focus,
fieldset[disabled] .btn-primary:focus,
.btn-primary.disabled.focus,
.btn-primary[disabled].focus,
fieldset[disabled] .btn-primary.focus {
  background-color: #337ab7;
  border-color: #2e6da4;
}
.btn-primary .badge {
  color: #337ab7;
  background-color: #fff;
}
.btn-success {
  color: #fff;
  background-color: #5cb85c;
  border-color: #4cae4c;
}
.btn-success:focus,
.btn-success.focus {
  color: #fff;
  background-color: #449d44;
  border-color: #255625;
}
.btn-success:hover {
  color: #fff;
  background-color: #449d44;
  border-color: #398439;
}
.btn-success:active,
.btn-success.active,
.open > .dropdown-toggle.btn-success {
  color: #fff;
  background-color: #449d44;
  border-color: #398439;
}
.btn-success:active:hover,
.btn-success.active:hover,
.open > .dropdown-toggle.btn-success:hover,
.btn-success:active:focus,
.btn-success.active:focus,
.open > .dropdown-toggle.btn-success:focus,
.btn-success:active.focus,
.btn-success.active.focus,
.open > .dropdown-toggle.btn-success.focus {
  color: #fff;
  background-color: #398439;
  border-color: #255625;
}
.btn-success:active,
.btn-success.active,
.open > .dropdown-toggle.btn-success {
  background-image: none;
}
.btn-success.disabled:hover,
.btn-success[disabled]:hover,
fieldset[disabled] .btn-success:hover,
.btn-success.disabled:focus,
.btn-success[disabled]:focus,
fieldset[disabled] .btn-success:focus,
.btn-success.disabled.focus,
.btn-success[disabled].focus,
fieldset[disabled] .btn-success.focus {
  background-color: #5cb85c;
  border-color: #4cae4c;
}
.btn-success .badge {
  color: #5cb85c;
  background-color: #fff;
}
.btn-info {
  color: #fff;
  background-color: #5bc0de;
  border-color: #46b8da;
}
.btn-info:focus,
.btn-info.focus {
  color: #fff;
  background-color: #31b0d5;
  border-color: #1b6d85;
}
.btn-info:hover {
  color: #fff;
  background-color: #31b0d5;
  border-color: #269abc;
}
.btn-info:active,
.btn-info.active,
.open > .dropdown-toggle.btn-info {
  color: #fff;
  background-color: #31b0d5;
  border-color: #269abc;
}
.btn-info:active:hover,
.btn-info.active:hover,
.open > .dropdown-toggle.btn-info:hover,
.btn-info:active:focus,
.btn-info.active:focus,
.open > .dropdown-toggle.btn-info:focus,
.btn-info:active.focus,
.btn-info.active.focus,
.open > .dropdown-toggle.btn-info.focus {
  color: #fff;
  background-color: #269abc;
  border-color: #1b6d85;
}
.btn-info:active,
.btn-info.active,
.open > .dropdown-toggle.btn-info {
  background-image: none;
}
.btn-info.disabled:hover,
.btn-info[disabled]:hover,
fieldset[disabled] .btn-info:hover,
.btn-info.disabled:focus,
.btn-info[disabled]:focus,
fieldset[disabled] .btn-info:focus,
.btn-info.disabled.focus,
.btn-info[disabled].focus,
fieldset[disabled] .btn-info.focus {
  background-color: #5bc0de;
  border-color: #46b8da;
}
.btn-info .badge {
  color: #5bc0de;
  background-color: #fff;
}
.btn-warning {
  color: #fff;
  background-color: #f0ad4e;
  border-color: #eea236;
}
.btn-warning:focus,
.btn-warning.focus {
  color: #fff;
  background-color: #ec971f;
  border-color: #985f0d;
}
.btn-warning:hover {
  color: #fff;
  background-color: #ec971f;
  border-color: #d58512;
}
.btn-warning:active,
.btn-warning.active,
.open > .dropdown-toggle.btn-warning {
  color: #fff;
  background-color: #ec971f;
  border-color: #d58512;
}
.btn-warning:active:hover,
.btn-warning.active:hover,
.open > .dropdown-toggle.btn-warning:hover,
.btn-warning:active:focus,
.btn-warning.active:focus,
.open > .dropdown-toggle.btn-warning:focus,
.btn-warning:active.focus,
.btn-warning.active.focus,
.open > .dropdown-toggle.btn-warning.focus {
  color: #fff;
  background-color: #d58512;
  border-color: #985f0d;
}
.btn-warning:active,
.btn-warning.active,
.open > .dropdown-toggle.btn-warning {
  background-image: none;
}
.btn-warning.disabled:hover,
.btn-warning[disabled]:hover,
fieldset[disabled] .btn-warning:hover,
.btn-warning.disabled:focus,
.btn-warning[disabled]:focus,
fieldset[disabled] .btn-warning:focus,
.btn-warning.disabled.focus,
.btn-warning[disabled].focus,
fieldset[disabled] .btn-warning.focus {
  background-color: #f0ad4e;
  border-color: #eea236;
}
.btn-warning .badge {
  color: #f0ad4e;
  background-color: #fff;
}
.btn-danger {
  color: #fff;
  background-color: #d9534f;
  border-color: #d43f3a;
}
.btn-danger:focus,
.btn-danger.focus {
  color: #fff;
  background-color: #c9302c;
  border-color: #761c19;
}
.btn-danger:hover {
  color: #fff;
  background-color: #c9302c;
  border-color: #ac2925;
}
.btn-danger:active,
.btn-danger.active,
.open > .dropdown-toggle.btn-danger {
  color: #fff;
  background-color: #c9302c;
  border-color: #ac2925;
}
.btn-danger:active:hover,
.btn-danger.active:hover,
.open > .dropdown-toggle.btn-danger:hover,
.btn-danger:active:focus,
.btn-danger.active:focus,
.open > .dropdown-toggle.btn-danger:focus,
.btn-danger:active.focus,
.btn-danger.active.focus,
.open > .dropdown-toggle.btn-danger.focus {
  color: #fff;
  background-color: #ac2925;
  border-color: #761c19;
}
.btn-danger:active,
.btn-danger.active,
.open > .dropdown-toggle.btn-danger {
  background-image: none;
}
.btn-danger.disabled:hover,
.btn-danger[disabled]:hover,
fieldset[disabled] .btn-danger:hover,
.btn-danger.disabled:focus,
.btn-danger[disabled]:focus,
fieldset[disabled] .btn-danger:focus,
.btn-danger.disabled.focus,
.btn-danger[disabled].focus,
fieldset[disabled] .btn-danger.focus {
  background-color: #d9534f;
  border-color: #d43f3a;
}
.btn-danger .badge {
  color: #d9534f;
  background-color: #fff;
}
.btn-link {
  color: #337ab7;
  font-weight: normal;
  border-radius: 0;
}
.btn-link,
.btn-link:active,
.btn-link.active,
.btn-link[disabled],
fieldset[disabled] .btn-link {
  background-color: transparent;
  -webkit-box-shadow: none;
  box-shadow: none;
}
.btn-link,
.btn-link:hover,
.btn-link:focus,
.btn-link:active {
  border-color: transparent;
}
.btn-link:hover,
.btn-link:focus {
  color: #23527c;
  text-decoration: underline;
  background-color: transparent;
}
.btn-link[disabled]:hover,
fieldset[disabled] .btn-link:hover,
.btn-link[disabled]:focus,
fieldset[disabled] .btn-link:focus {
  color: #777777;
  text-decoration: none;
}
.btn-lg,
.btn-group-lg > .btn {
  padding: 10px 16px;
  font-size: 17px;
  line-height: 1.3333333;
  border-radius: 3px;
}
.btn-sm,
.btn-group-sm > .btn {
  padding: 5px 10px;
  font-size: 12px;
  line-height: 1.5;
  border-radius: 1px;
}
.btn-xs,
.btn-group-xs > .btn {
  padding: 1px 5px;
  font-size: 12px;
  line-height: 1.5;
  border-radius: 1px;
}
.btn-block {
  display: block;
  width: 100%;
}
.btn-block + .btn-block {
  margin-top: 5px;
}
input[type="submit"].btn-block,
input[type="reset"].btn-block,
input[type="button"].btn-block {
  width: 100%;
}
.fade {
  opacity: 0;
  -webkit-transition: opacity 0.15s linear;
  -o-transition: opacity 0.15s linear;
  transition: opacity 0.15s linear;
}
.fade.in {
  opacity: 1;
}
.collapse {
  display: none;
}
.collapse.in {
  display: block;
}
tr.collapse.in {
  display: table-row;
}
tbody.collapse.in {
  display: table-row-group;
}
.collapsing {
  position: relative;
  height: 0;
  overflow: hidden;
  -webkit-transition-property: height, visibility;
  transition-property: height, visibility;
  -webkit-transition-duration: 0.35s;
  transition-duration: 0.35s;
  -webkit-transition-timing-function: ease;
  transition-timing-function: ease;
}
.caret {
  display: inline-block;
  width: 0;
  height: 0;
  margin-left: 2px;
  vertical-align: middle;
  border-top: 4px dashed;
  border-top: 4px solid \9;
  border-right: 4px solid transparent;
  border-left: 4px solid transparent;
}
.dropup,
.dropdown {
  position: relative;
}
.dropdown-toggle:focus {
  outline: 0;
}
.dropdown-menu {
  position: absolute;
  top: 100%;
  left: 0;
  z-index: 1000;
  display: none;
  float: left;
  min-width: 160px;
  padding: 5px 0;
  margin: 2px 0 0;
  list-style: none;
  font-size: 13px;
  text-align: left;
  background-color: #fff;
  border: 1px solid #ccc;
  border: 1px solid rgba(0, 0, 0, 0.15);
  border-radius: 2px;
  -webkit-box-shadow: 0 6px 12px rgba(0, 0, 0, 0.175);
  box-shadow: 0 6px 12px rgba(0, 0, 0, 0.175);
  background-clip: padding-box;
}
.dropdown-menu.pull-right {
  right: 0;
  left: auto;
}
.dropdown-menu .divider {
  height: 1px;
  margin: 8px 0;
  overflow: hidden;
  background-color: #e5e5e5;
}
.dropdown-menu > li > a {
  display: block;
  padding: 3px 20px;
  clear: both;
  font-weight: normal;
  line-height: 1.42857143;
  color: #333333;
  white-space: nowrap;
}
.dropdown-menu > li > a:hover,
.dropdown-menu > li > a:focus {
  text-decoration: none;
  color: #262626;
  background-color: #f5f5f5;
}
.dropdown-menu > .active > a,
.dropdown-menu > .active > a:hover,
.dropdown-menu > .active > a:focus {
  color: #fff;
  text-decoration: none;
  outline: 0;
  background-color: #337ab7;
}
.dropdown-menu > .disabled > a,
.dropdown-menu > .disabled > a:hover,
.dropdown-menu > .disabled > a:focus {
  color: #777777;
}
.dropdown-menu > .disabled > a:hover,
.dropdown-menu > .disabled > a:focus {
  text-decoration: none;
  background-color: transparent;
  background-image: none;
  filter: progid:DXImageTransform.Microsoft.gradient(enabled = false);
  cursor: not-allowed;
}
.open > .dropdown-menu {
  display: block;
}
.open > a {
  outline: 0;
}
.dropdown-menu-right {
  left: auto;
  right: 0;
}
.dropdown-menu-left {
  left: 0;
  right: auto;
}
.dropdown-header {
  display: block;
  padding: 3px 20px;
  font-size: 12px;
  line-height: 1.42857143;
  color: #777777;
  white-space: nowrap;
}
.dropdown-backdrop {
  position: fixed;
  left: 0;
  right: 0;
  bottom: 0;
  top: 0;
  z-index: 990;
}
.pull-right > .dropdown-menu {
  right: 0;
  left: auto;
}
.dropup .caret,
.navbar-fixed-bottom .dropdown .caret {
  border-top: 0;
  border-bottom: 4px dashed;
  border-bottom: 4px solid \9;
  content: "";
}
.dropup .dropdown-menu,
.navbar-fixed-bottom .dropdown .dropdown-menu {
  top: auto;
  bottom: 100%;
  margin-bottom: 2px;
}
@media (min-width: 541px) {
  .navbar-right .dropdown-menu {
    left: auto;
    right: 0;
  }
  .navbar-right .dropdown-menu-left {
    left: 0;
    right: auto;
  }
}
.btn-group,
.btn-group-vertical {
  position: relative;
  display: inline-block;
  vertical-align: middle;
}
.btn-group > .btn,
.btn-group-vertical > .btn {
  position: relative;
  float: left;
}
.btn-group > .btn:hover,
.btn-group-vertical > .btn:hover,
.btn-group > .btn:focus,
.btn-group-vertical > .btn:focus,
.btn-group > .btn:active,
.btn-group-vertical > .btn:active,
.btn-group > .btn.active,
.btn-group-vertical > .btn.active {
  z-index: 2;
}
.btn-group .btn + .btn,
.btn-group .btn + .btn-group,
.btn-group .btn-group + .btn,
.btn-group .btn-group + .btn-group {
  margin-left: -1px;
}
.btn-toolbar {
  margin-left: -5px;
}
.btn-toolbar .btn,
.btn-toolbar .btn-group,
.btn-toolbar .input-group {
  float: left;
}
.btn-toolbar > .btn,
.btn-toolbar > .btn-group,
.btn-toolbar > .input-group {
  margin-left: 5px;
}
.btn-group > .btn:not(:first-child):not(:last-child):not(.dropdown-toggle) {
  border-radius: 0;
}
.btn-group > .btn:first-child {
  margin-left: 0;
}
.btn-group > .btn:first-child:not(:last-child):not(.dropdown-toggle) {
  border-bottom-right-radius: 0;
  border-top-right-radius: 0;
}
.btn-group > .btn:last-child:not(:first-child),
.btn-group > .dropdown-toggle:not(:first-child) {
  border-bottom-left-radius: 0;
  border-top-left-radius: 0;
}
.btn-group > .btn-group {
  float: left;
}
.btn-group > .btn-group:not(:first-child):not(:last-child) > .btn {
  border-radius: 0;
}
.btn-group > .btn-group:first-child:not(:last-child) > .btn:last-child,
.btn-group > .btn-group:first-child:not(:last-child) > .dropdown-toggle {
  border-bottom-right-radius: 0;
  border-top-right-radius: 0;
}
.btn-group > .btn-group:last-child:not(:first-child) > .btn:first-child {
  border-bottom-left-radius: 0;
  border-top-left-radius: 0;
}
.btn-group .dropdown-toggle:active,
.btn-group.open .dropdown-toggle {
  outline: 0;
}
.btn-group > .btn + .dropdown-toggle {
  padding-left: 8px;
  padding-right: 8px;
}
.btn-group > .btn-lg + .dropdown-toggle {
  padding-left: 12px;
  padding-right: 12px;
}
.btn-group.open .dropdown-toggle {
  -webkit-box-shadow: inset 0 3px 5px rgba(0, 0, 0, 0.125);
  box-shadow: inset 0 3px 5px rgba(0, 0, 0, 0.125);
}
.btn-group.open .dropdown-toggle.btn-link {
  -webkit-box-shadow: none;
  box-shadow: none;
}
.btn .caret {
  margin-left: 0;
}
.btn-lg .caret {
  border-width: 5px 5px 0;
  border-bottom-width: 0;
}
.dropup .btn-lg .caret {
  border-width: 0 5px 5px;
}
.btn-group-vertical > .btn,
.btn-group-vertical > .btn-group,
.btn-group-vertical > .btn-group > .btn {
  display: block;
  float: none;
  width: 100%;
  max-width: 100%;
}
.btn-group-vertical > .btn-group > .btn {
  float: none;
}
.btn-group-vertical > .btn + .btn,
.btn-group-vertical > .btn + .btn-group,
.btn-group-vertical > .btn-group + .btn,
.btn-group-vertical > .btn-group + .btn-group {
  margin-top: -1px;
  margin-left: 0;
}
.btn-group-vertical > .btn:not(:first-child):not(:last-child) {
  border-radius: 0;
}
.btn-group-vertical > .btn:first-child:not(:last-child) {
  border-top-right-radius: 2px;
  border-top-left-radius: 2px;
  border-bottom-right-radius: 0;
  border-bottom-left-radius: 0;
}
.btn-group-vertical > .btn:last-child:not(:first-child) {
  border-top-right-radius: 0;
  border-top-left-radius: 0;
  border-bottom-right-radius: 2px;
  border-bottom-left-radius: 2px;
}
.btn-group-vertical > .btn-group:not(:first-child):not(:last-child) > .btn {
  border-radius: 0;
}
.btn-group-vertical > .btn-group:first-child:not(:last-child) > .btn:last-child,
.btn-group-vertical > .btn-group:first-child:not(:last-child) > .dropdown-toggle {
  border-bottom-right-radius: 0;
  border-bottom-left-radius: 0;
}
.btn-group-vertical > .btn-group:last-child:not(:first-child) > .btn:first-child {
  border-top-right-radius: 0;
  border-top-left-radius: 0;
}
.btn-group-justified {
  display: table;
  width: 100%;
  table-layout: fixed;
  border-collapse: separate;
}
.btn-group-justified > .btn,
.btn-group-justified > .btn-group {
  float: none;
  display: table-cell;
  width: 1%;
}
.btn-group-justified > .btn-group .btn {
  width: 100%;
}
.btn-group-justified > .btn-group .dropdown-menu {
  left: auto;
}
[data-toggle="buttons"] > .btn input[type="radio"],
[data-toggle="buttons"] > .btn-group > .btn input[type="radio"],
[data-toggle="buttons"] > .btn input[type="checkbox"],
[data-toggle="buttons"] > .btn-group > .btn input[type="checkbox"] {
  position: absolute;
  clip: rect(0, 0, 0, 0);
  pointer-events: none;
}
.input-group {
  position: relative;
  display: table;
  border-collapse: separate;
}
.input-group[class*="col-"] {
  float: none;
  padding-left: 0;
  padding-right: 0;
}
.input-group .form-control {
  position: relative;
  z-index: 2;
  float: left;
  width: 100%;
  margin-bottom: 0;
}
.input-group .form-control:focus {
  z-index: 3;
}
.input-group-lg > .form-control,
.input-group-lg > .input-group-addon,
.input-group-lg > .input-group-btn > .btn {
  height: 45px;
  padding: 10px 16px;
  font-size: 17px;
  line-height: 1.3333333;
  border-radius: 3px;
}
select.input-group-lg > .form-control,
select.input-group-lg > .input-group-addon,
select.input-group-lg > .input-group-btn > .btn {
  height: 45px;
  line-height: 45px;
}
textarea.input-group-lg > .form-control,
textarea.input-group-lg > .input-group-addon,
textarea.input-group-lg > .input-group-btn > .btn,
select[multiple].input-group-lg > .form-control,
select[multiple].input-group-lg > .input-group-addon,
select[multiple].input-group-lg > .input-group-btn > .btn {
  height: auto;
}
.input-group-sm > .form-control,
.input-group-sm > .input-group-addon,
.input-group-sm > .input-group-btn > .btn {
  height: 30px;
  padding: 5px 10px;
  font-size: 12px;
  line-height: 1.5;
  border-radius: 1px;
}
select.input-group-sm > .form-control,
select.input-group-sm > .input-group-addon,
select.input-group-sm > .input-group-btn > .btn {
  height: 30px;
  line-height: 30px;
}
textarea.input-group-sm > .form-control,
textarea.input-group-sm > .input-group-addon,
textarea.input-group-sm > .input-group-btn > .btn,
select[multiple].input-group-sm > .form-control,
select[multiple].input-group-sm > .input-group-addon,
select[multiple].input-group-sm > .input-group-btn > .btn {
  height: auto;
}
.input-group-addon,
.input-group-btn,
.input-group .form-control {
  display: table-cell;
}
.input-group-addon:not(:first-child):not(:last-child),
.input-group-btn:not(:first-child):not(:last-child),
.input-group .form-control:not(:first-child):not(:last-child) {
  border-radius: 0;
}
.input-group-addon,
.input-group-btn {
  width: 1%;
  white-space: nowrap;
  vertical-align: middle;
}
.input-group-addon {
  padding: 6px 12px;
  font-size: 13px;
  font-weight: normal;
  line-height: 1;
  color: #555555;
  text-align: center;
  background-color: #eeeeee;
  border: 1px solid #ccc;
  border-radius: 2px;
}
.input-group-addon.input-sm {
  padding: 5px 10px;
  font-size: 12px;
  border-radius: 1px;
}
.input-group-addon.input-lg {
  padding: 10px 16px;
  font-size: 17px;
  border-radius: 3px;
}
.input-group-addon input[type="radio"],
.input-group-addon input[type="checkbox"] {
  margin-top: 0;
}
.input-group .form-control:first-child,
.input-group-addon:first-child,
.input-group-btn:first-child > .btn,
.input-group-btn:first-child > .btn-group > .btn,
.input-group-btn:first-child > .dropdown-toggle,
.input-group-btn:last-child > .btn:not(:last-child):not(.dropdown-toggle),
.input-group-btn:last-child > .btn-group:not(:last-child) > .btn {
  border-bottom-right-radius: 0;
  border-top-right-radius: 0;
}
.input-group-addon:first-child {
  border-right: 0;
}
.input-group .form-control:last-child,
.input-group-addon:last-child,
.input-group-btn:last-child > .btn,
.input-group-btn:last-child > .btn-group > .btn,
.input-group-btn:last-child > .dropdown-toggle,
.input-group-btn:first-child > .btn:not(:first-child),
.input-group-btn:first-child > .btn-group:not(:first-child) > .btn {
  border-bottom-left-radius: 0;
  border-top-left-radius: 0;
}
.input-group-addon:last-child {
  border-left: 0;
}
.input-group-btn {
  position: relative;
  font-size: 0;
  white-space: nowrap;
}
.input-group-btn > .btn {
  position: relative;
}
.input-group-btn > .btn + .btn {
  margin-left: -1px;
}
.input-group-btn > .btn:hover,
.input-group-btn > .btn:focus,
.input-group-btn > .btn:active {
  z-index: 2;
}
.input-group-btn:first-child > .btn,
.input-group-btn:first-child > .btn-group {
  margin-right: -1px;
}
.input-group-btn:last-child > .btn,
.input-group-btn:last-child > .btn-group {
  z-index: 2;
  margin-left: -1px;
}
.nav {
  margin-bottom: 0;
  padding-left: 0;
  list-style: none;
}
.nav > li {
  position: relative;
  display: block;
}
.nav > li > a {
  position: relative;
  display: block;
  padding: 10px 15px;
}
.nav > li > a:hover,
.nav > li > a:focus {
  text-decoration: none;
  background-color: #eeeeee;
}
.nav > li.disabled > a {
  color: #777777;
}
.nav > li.disabled > a:hover,
.nav > li.disabled > a:focus {
  color: #777777;
  text-decoration: none;
  background-color: transparent;
  cursor: not-allowed;
}
.nav .open > a,
.nav .open > a:hover,
.nav .open > a:focus {
  background-color: #eeeeee;
  border-color: #337ab7;
}
.nav .nav-divider {
  height: 1px;
  margin: 8px 0;
  overflow: hidden;
  background-color: #e5e5e5;
}
.nav > li > a > img {
  max-width: none;
}
.nav-tabs {
  border-bottom: 1px solid #ddd;
}
.nav-tabs > li {
  float: left;
  margin-bottom: -1px;
}
.nav-tabs > li > a {
  margin-right: 2px;
  line-height: 1.42857143;
  border: 1px solid transparent;
  border-radius: 2px 2px 0 0;
}
.nav-tabs > li > a:hover {
  border-color: #eeeeee #eeeeee #ddd;
}
.nav-tabs > li.active > a,
.nav-tabs > li.active > a:hover,
.nav-tabs > li.active > a:focus {
  color: #555555;
  background-color: #fff;
  border: 1px solid #ddd;
  border-bottom-color: transparent;
  cursor: default;
}
.nav-tabs.nav-justified {
  width: 100%;
  border-bottom: 0;
}
.nav-tabs.nav-justified > li {
  float: none;
}
.nav-tabs.nav-justified > li > a {
  text-align: center;
  margin-bottom: 5px;
}
.nav-tabs.nav-justified > .dropdown .dropdown-menu {
  top: auto;
  left: auto;
}
@media (min-width: 768px) {
  .nav-tabs.nav-justified > li {
    display: table-cell;
    width: 1%;
  }
  .nav-tabs.nav-justified > li > a {
    margin-bottom: 0;
  }
}
.nav-tabs.nav-justified > li > a {
  margin-right: 0;
  border-radius: 2px;
}
.nav-tabs.nav-justified > .active > a,
.nav-tabs.nav-justified > .active > a:hover,
.nav-tabs.nav-justified > .active > a:focus {
  border: 1px solid #ddd;
}
@media (min-width: 768px) {
  .nav-tabs.nav-justified > li > a {
    border-bottom: 1px solid #ddd;
    border-radius: 2px 2px 0 0;
  }
  .nav-tabs.nav-justified > .active > a,
  .nav-tabs.nav-justified > .active > a:hover,
  .nav-tabs.nav-justified > .active > a:focus {
    border-bottom-color: #fff;
  }
}
.nav-pills > li {
  float: left;
}
.nav-pills > li > a {
  border-radius: 2px;
}
.nav-pills > li + li {
  margin-left: 2px;
}
.nav-pills > li.active > a,
.nav-pills > li.active > a:hover,
.nav-pills > li.active > a:focus {
  color: #fff;
  background-color: #337ab7;
}
.nav-stacked > li {
  float: none;
}
.nav-stacked > li + li {
  margin-top: 2px;
  margin-left: 0;
}
.nav-justified {
  width: 100%;
}
.nav-justified > li {
  float: none;
}
.nav-justified > li > a {
  text-align: center;
  margin-bottom: 5px;
}
.nav-justified > .dropdown .dropdown-menu {
  top: auto;
  left: auto;
}
@media (min-width: 768px) {
  .nav-justified > li {
    display: table-cell;
    width: 1%;
  }
  .nav-justified > li > a {
    margin-bottom: 0;
  }
}
.nav-tabs-justified {
  border-bottom: 0;
}
.nav-tabs-justified > li > a {
  margin-right: 0;
  border-radius: 2px;
}
.nav-tabs-justified > .active > a,
.nav-tabs-justified > .active > a:hover,
.nav-tabs-justified > .active > a:focus {
  border: 1px solid #ddd;
}
@media (min-width: 768px) {
  .nav-tabs-justified > li > a {
    border-bottom: 1px solid #ddd;
    border-radius: 2px 2px 0 0;
  }
  .nav-tabs-justified > .active > a,
  .nav-tabs-justified > .active > a:hover,
  .nav-tabs-justified > .active > a:focus {
    border-bottom-color: #fff;
  }
}
.tab-content > .tab-pane {
  display: none;
}
.tab-content > .active {
  display: block;
}
.nav-tabs .dropdown-menu {
  margin-top: -1px;
  border-top-right-radius: 0;
  border-top-left-radius: 0;
}
.navbar {
  position: relative;
  min-height: 30px;
  margin-bottom: 18px;
  border: 1px solid transparent;
}
@media (min-width: 541px) {
  .navbar {
    border-radius: 2px;
  }
}
@media (min-width: 541px) {
  .navbar-header {
    float: left;
  }
}
.navbar-collapse {
  overflow-x: visible;
  padding-right: 0px;
  padding-left: 0px;
  border-top: 1px solid transparent;
  box-shadow: inset 0 1px 0 rgba(255, 255, 255, 0.1);
  -webkit-overflow-scrolling: touch;
}
.navbar-collapse.in {
  overflow-y: auto;
}
@media (min-width: 541px) {
  .navbar-collapse {
    width: auto;
    border-top: 0;
    box-shadow: none;
  }
  .navbar-collapse.collapse {
    display: block !important;
    height: auto !important;
    padding-bottom: 0;
    overflow: visible !important;
  }
  .navbar-collapse.in {
    overflow-y: visible;
  }
  .navbar-fixed-top .navbar-collapse,
  .navbar-static-top .navbar-collapse,
  .navbar-fixed-bottom .navbar-collapse {
    padding-left: 0;
    padding-right: 0;
  }
}
.navbar-fixed-top .navbar-collapse,
.navbar-fixed-bottom .navbar-collapse {
  max-height: 340px;
}
@media (max-device-width: 540px) and (orientation: landscape) {
  .navbar-fixed-top .navbar-collapse,
  .navbar-fixed-bottom .navbar-collapse {
    max-height: 200px;
  }
}
.container > .navbar-header,
.container-fluid > .navbar-header,
.container > .navbar-collapse,
.container-fluid > .navbar-collapse {
  margin-right: 0px;
  margin-left: 0px;
}
@media (min-width: 541px) {
  .container > .navbar-header,
  .container-fluid > .navbar-header,
  .container > .navbar-collapse,
  .container-fluid > .navbar-collapse {
    margin-right: 0;
    margin-left: 0;
  }
}
.navbar-static-top {
  z-index: 1000;
  border-width: 0 0 1px;
}
@media (min-width: 541px) {
  .navbar-static-top {
    border-radius: 0;
  }
}
.navbar-fixed-top,
.navbar-fixed-bottom {
  position: fixed;
  right: 0;
  left: 0;
  z-index: 1030;
}
@media (min-width: 541px) {
  .navbar-fixed-top,
  .navbar-fixed-bottom {
    border-radius: 0;
  }
}
.navbar-fixed-top {
  top: 0;
  border-width: 0 0 1px;
}
.navbar-fixed-bottom {
  bottom: 0;
  margin-bottom: 0;
  border-width: 1px 0 0;
}
.navbar-brand {
  float: left;
  padding: 6px 0px;
  font-size: 17px;
  line-height: 18px;
  height: 30px;
}
.navbar-brand:hover,
.navbar-brand:focus {
  text-decoration: none;
}
.navbar-brand > img {
  display: block;
}
@media (min-width: 541px) {
  .navbar > .container .navbar-brand,
  .navbar > .container-fluid .navbar-brand {
    margin-left: 0px;
  }
}
.navbar-toggle {
  position: relative;
  float: right;
  margin-right: 0px;
  padding: 9px 10px;
  margin-top: -2px;
  margin-bottom: -2px;
  background-color: transparent;
  background-image: none;
  border: 1px solid transparent;
  border-radius: 2px;
}
.navbar-toggle:focus {
  outline: 0;
}
.navbar-toggle .icon-bar {
  display: block;
  width: 22px;
  height: 2px;
  border-radius: 1px;
}
.navbar-toggle .icon-bar + .icon-bar {
  margin-top: 4px;
}
@media (min-width: 541px) {
  .navbar-toggle {
    display: none;
  }
}
.navbar-nav {
  margin: 3px 0px;
}
.navbar-nav > li > a {
  padding-top: 10px;
  padding-bottom: 10px;
  line-height: 18px;
}
@media (max-width: 540px) {
  .navbar-nav .open .dropdown-menu {
    position: static;
    float: none;
    width: auto;
    margin-top: 0;
    background-color: transparent;
    border: 0;
    box-shadow: none;
  }
  .navbar-nav .open .dropdown-menu > li > a,
  .navbar-nav .open .dropdown-menu .dropdown-header {
    padding: 5px 15px 5px 25px;
  }
  .navbar-nav .open .dropdown-menu > li > a {
    line-height: 18px;
  }
  .navbar-nav .open .dropdown-menu > li > a:hover,
  .navbar-nav .open .dropdown-menu > li > a:focus {
    background-image: none;
  }
}
@media (min-width: 541px) {
  .navbar-nav {
    float: left;
    margin: 0;
  }
  .navbar-nav > li {
    float: left;
  }
  .navbar-nav > li > a {
    padding-top: 6px;
    padding-bottom: 6px;
  }
}
.navbar-form {
  margin-left: 0px;
  margin-right: 0px;
  padding: 10px 0px;
  border-top: 1px solid transparent;
  border-bottom: 1px solid transparent;
  -webkit-box-shadow: inset 0 1px 0 rgba(255, 255, 255, 0.1), 0 1px 0 rgba(255, 255, 255, 0.1);
  box-shadow: inset 0 1px 0 rgba(255, 255, 255, 0.1), 0 1px 0 rgba(255, 255, 255, 0.1);
  margin-top: -1px;
  margin-bottom: -1px;
}
@media (min-width: 768px) {
  .navbar-form .form-group {
    display: inline-block;
    margin-bottom: 0;
    vertical-align: middle;
  }
  .navbar-form .form-control {
    display: inline-block;
    width: auto;
    vertical-align: middle;
  }
  .navbar-form .form-control-static {
    display: inline-block;
  }
  .navbar-form .input-group {
    display: inline-table;
    vertical-align: middle;
  }
  .navbar-form .input-group .input-group-addon,
  .navbar-form .input-group .input-group-btn,
  .navbar-form .input-group .form-control {
    width: auto;
  }
  .navbar-form .input-group > .form-control {
    width: 100%;
  }
  .navbar-form .control-label {
    margin-bottom: 0;
    vertical-align: middle;
  }
  .navbar-form .radio,
  .navbar-form .checkbox {
    display: inline-block;
    margin-top: 0;
    margin-bottom: 0;
    vertical-align: middle;
  }
  .navbar-form .radio label,
  .navbar-form .checkbox label {
    padding-left: 0;
  }
  .navbar-form .radio input[type="radio"],
  .navbar-form .checkbox input[type="checkbox"] {
    position: relative;
    margin-left: 0;
  }
  .navbar-form .has-feedback .form-control-feedback {
    top: 0;
  }
}
@media (max-width: 540px) {
  .navbar-form .form-group {
    margin-bottom: 5px;
  }
  .navbar-form .form-group:last-child {
    margin-bottom: 0;
  }
}
@media (min-width: 541px) {
  .navbar-form {
    width: auto;
    border: 0;
    margin-left: 0;
    margin-right: 0;
    padding-top: 0;
    padding-bottom: 0;
    -webkit-box-shadow: none;
    box-shadow: none;
  }
}
.navbar-nav > li > .dropdown-menu {
  margin-top: 0;
  border-top-right-radius: 0;
  border-top-left-radius: 0;
}
.navbar-fixed-bottom .navbar-nav > li > .dropdown-menu {
  margin-bottom: 0;
  border-top-right-radius: 2px;
  border-top-left-radius: 2px;
  border-bottom-right-radius: 0;
  border-bottom-left-radius: 0;
}
.navbar-btn {
  margin-top: -1px;
  margin-bottom: -1px;
}
.navbar-btn.btn-sm {
  margin-top: 0px;
  margin-bottom: 0px;
}
.navbar-btn.btn-xs {
  margin-top: 4px;
  margin-bottom: 4px;
}
.navbar-text {
  margin-top: 6px;
  margin-bottom: 6px;
}
@media (min-width: 541px) {
  .navbar-text {
    float: left;
    margin-left: 0px;
    margin-right: 0px;
  }
}
@media (min-width: 541px) {
  .navbar-left {
    float: left !important;
    float: left;
  }
  .navbar-right {
    float: right !important;
    float: right;
    margin-right: 0px;
  }
  .navbar-right ~ .navbar-right {
    margin-right: 0;
  }
}
.navbar-default {
  background-color: #f8f8f8;
  border-color: #e7e7e7;
}
.navbar-default .navbar-brand {
  color: #777;
}
.navbar-default .navbar-brand:hover,
.navbar-default .navbar-brand:focus {
  color: #5e5e5e;
  background-color: transparent;
}
.navbar-default .navbar-text {
  color: #777;
}
.navbar-default .navbar-nav > li > a {
  color: #777;
}
.navbar-default .navbar-nav > li > a:hover,
.navbar-default .navbar-nav > li > a:focus {
  color: #333;
  background-color: transparent;
}
.navbar-default .navbar-nav > .active > a,
.navbar-default .navbar-nav > .active > a:hover,
.navbar-default .navbar-nav > .active > a:focus {
  color: #555;
  background-color: #e7e7e7;
}
.navbar-default .navbar-nav > .disabled > a,
.navbar-default .navbar-nav > .disabled > a:hover,
.navbar-default .navbar-nav > .disabled > a:focus {
  color: #ccc;
  background-color: transparent;
}
.navbar-default .navbar-toggle {
  border-color: #ddd;
}
.navbar-default .navbar-toggle:hover,
.navbar-default .navbar-toggle:focus {
  background-color: #ddd;
}
.navbar-default .navbar-toggle .icon-bar {
  background-color: #888;
}
.navbar-default .navbar-collapse,
.navbar-default .navbar-form {
  border-color: #e7e7e7;
}
.navbar-default .navbar-nav > .open > a,
.navbar-default .navbar-nav > .open > a:hover,
.navbar-default .navbar-nav > .open > a:focus {
  background-color: #e7e7e7;
  color: #555;
}
@media (max-width: 540px) {
  .navbar-default .navbar-nav .open .dropdown-menu > li > a {
    color: #777;
  }
  .navbar-default .navbar-nav .open .dropdown-menu > li > a:hover,
  .navbar-default .navbar-nav .open .dropdown-menu > li > a:focus {
    color: #333;
    background-color: transparent;
  }
  .navbar-default .navbar-nav .open .dropdown-menu > .active > a,
  .navbar-default .navbar-nav .open .dropdown-menu > .active > a:hover,
  .navbar-default .navbar-nav .open .dropdown-menu > .active > a:focus {
    color: #555;
    background-color: #e7e7e7;
  }
  .navbar-default .navbar-nav .open .dropdown-menu > .disabled > a,
  .navbar-default .navbar-nav .open .dropdown-menu > .disabled > a:hover,
  .navbar-default .navbar-nav .open .dropdown-menu > .disabled > a:focus {
    color: #ccc;
    background-color: transparent;
  }
}
.navbar-default .navbar-link {
  color: #777;
}
.navbar-default .navbar-link:hover {
  color: #333;
}
.navbar-default .btn-link {
  color: #777;
}
.navbar-default .btn-link:hover,
.navbar-default .btn-link:focus {
  color: #333;
}
.navbar-default .btn-link[disabled]:hover,
fieldset[disabled] .navbar-default .btn-link:hover,
.navbar-default .btn-link[disabled]:focus,
fieldset[disabled] .navbar-default .btn-link:focus {
  color: #ccc;
}
.navbar-inverse {
  background-color: #222;
  border-color: #080808;
}
.navbar-inverse .navbar-brand {
  color: #9d9d9d;
}
.navbar-inverse .navbar-brand:hover,
.navbar-inverse .navbar-brand:focus {
  color: #fff;
  background-color: transparent;
}
.navbar-inverse .navbar-text {
  color: #9d9d9d;
}
.navbar-inverse .navbar-nav > li > a {
  color: #9d9d9d;
}
.navbar-inverse .navbar-nav > li > a:hover,
.navbar-inverse .navbar-nav > li > a:focus {
  color: #fff;
  background-color: transparent;
}
.navbar-inverse .navbar-nav > .active > a,
.navbar-inverse .navbar-nav > .active > a:hover,
.navbar-inverse .navbar-nav > .active > a:focus {
  color: #fff;
  background-color: #080808;
}
.navbar-inverse .navbar-nav > .disabled > a,
.navbar-inverse .navbar-nav > .disabled > a:hover,
.navbar-inverse .navbar-nav > .disabled > a:focus {
  color: #444;
  background-color: transparent;
}
.navbar-inverse .navbar-toggle {
  border-color: #333;
}
.navbar-inverse .navbar-toggle:hover,
.navbar-inverse .navbar-toggle:focus {
  background-color: #333;
}
.navbar-inverse .navbar-toggle .icon-bar {
  background-color: #fff;
}
.navbar-inverse .navbar-collapse,
.navbar-inverse .navbar-form {
  border-color: #101010;
}
.navbar-inverse .navbar-nav > .open > a,
.navbar-inverse .navbar-nav > .open > a:hover,
.navbar-inverse .navbar-nav > .open > a:focus {
  background-color: #080808;
  color: #fff;
}
@media (max-width: 540px) {
  .navbar-inverse .navbar-nav .open .dropdown-menu > .dropdown-header {
    border-color: #080808;
  }
  .navbar-inverse .navbar-nav .open .dropdown-menu .divider {
    background-color: #080808;
  }
  .navbar-inverse .navbar-nav .open .dropdown-menu > li > a {
    color: #9d9d9d;
  }
  .navbar-inverse .navbar-nav .open .dropdown-menu > li > a:hover,
  .navbar-inverse .navbar-nav .open .dropdown-menu > li > a:focus {
    color: #fff;
    background-color: transparent;
  }
  .navbar-inverse .navbar-nav .open .dropdown-menu > .active > a,
  .navbar-inverse .navbar-nav .open .dropdown-menu > .active > a:hover,
  .navbar-inverse .navbar-nav .open .dropdown-menu > .active > a:focus {
    color: #fff;
    background-color: #080808;
  }
  .navbar-inverse .navbar-nav .open .dropdown-menu > .disabled > a,
  .navbar-inverse .navbar-nav .open .dropdown-menu > .disabled > a:hover,
  .navbar-inverse .navbar-nav .open .dropdown-menu > .disabled > a:focus {
    color: #444;
    background-color: transparent;
  }
}
.navbar-inverse .navbar-link {
  color: #9d9d9d;
}
.navbar-inverse .navbar-link:hover {
  color: #fff;
}
.navbar-inverse .btn-link {
  color: #9d9d9d;
}
.navbar-inverse .btn-link:hover,
.navbar-inverse .btn-link:focus {
  color: #fff;
}
.navbar-inverse .btn-link[disabled]:hover,
fieldset[disabled] .navbar-inverse .btn-link:hover,
.navbar-inverse .btn-link[disabled]:focus,
fieldset[disabled] .navbar-inverse .btn-link:focus {
  color: #444;
}
.breadcrumb {
  padding: 8px 15px;
  margin-bottom: 18px;
  list-style: none;
  background-color: #f5f5f5;
  border-radius: 2px;
}
.breadcrumb > li {
  display: inline-block;
}
.breadcrumb > li + li:before {
  content: "/\00a0";
  padding: 0 5px;
  color: #5e5e5e;
}
.breadcrumb > .active {
  color: #777777;
}
.pagination {
  display: inline-block;
  padding-left: 0;
  margin: 18px 0;
  border-radius: 2px;
}
.pagination > li {
  display: inline;
}
.pagination > li > a,
.pagination > li > span {
  position: relative;
  float: left;
  padding: 6px 12px;
  line-height: 1.42857143;
  text-decoration: none;
  color: #337ab7;
  background-color: #fff;
  border: 1px solid #ddd;
  margin-left: -1px;
}
.pagination > li:first-child > a,
.pagination > li:first-child > span {
  margin-left: 0;
  border-bottom-left-radius: 2px;
  border-top-left-radius: 2px;
}
.pagination > li:last-child > a,
.pagination > li:last-child > span {
  border-bottom-right-radius: 2px;
  border-top-right-radius: 2px;
}
.pagination > li > a:hover,
.pagination > li > span:hover,
.pagination > li > a:focus,
.pagination > li > span:focus {
  z-index: 2;
  color: #23527c;
  background-color: #eeeeee;
  border-color: #ddd;
}
.pagination > .active > a,
.pagination > .active > span,
.pagination > .active > a:hover,
.pagination > .active > span:hover,
.pagination > .active > a:focus,
.pagination > .active > span:focus {
  z-index: 3;
  color: #fff;
  background-color: #337ab7;
  border-color: #337ab7;
  cursor: default;
}
.pagination > .disabled > span,
.pagination > .disabled > span:hover,
.pagination > .disabled > span:focus,
.pagination > .disabled > a,
.pagination > .disabled > a:hover,
.pagination > .disabled > a:focus {
  color: #777777;
  background-color: #fff;
  border-color: #ddd;
  cursor: not-allowed;
}
.pagination-lg > li > a,
.pagination-lg > li > span {
  padding: 10px 16px;
  font-size: 17px;
  line-height: 1.3333333;
}
.pagination-lg > li:first-child > a,
.pagination-lg > li:first-child > span {
  border-bottom-left-radius: 3px;
  border-top-left-radius: 3px;
}
.pagination-lg > li:last-child > a,
.pagination-lg > li:last-child > span {
  border-bottom-right-radius: 3px;
  border-top-right-radius: 3px;
}
.pagination-sm > li > a,
.pagination-sm > li > span {
  padding: 5px 10px;
  font-size: 12px;
  line-height: 1.5;
}
.pagination-sm > li:first-child > a,
.pagination-sm > li:first-child > span {
  border-bottom-left-radius: 1px;
  border-top-left-radius: 1px;
}
.pagination-sm > li:last-child > a,
.pagination-sm > li:last-child > span {
  border-bottom-right-radius: 1px;
  border-top-right-radius: 1px;
}
.pager {
  padding-left: 0;
  margin: 18px 0;
  list-style: none;
  text-align: center;
}
.pager li {
  display: inline;
}
.pager li > a,
.pager li > span {
  display: inline-block;
  padding: 5px 14px;
  background-color: #fff;
  border: 1px solid #ddd;
  border-radius: 15px;
}
.pager li > a:hover,
.pager li > a:focus {
  text-decoration: none;
  background-color: #eeeeee;
}
.pager .next > a,
.pager .next > span {
  float: right;
}
.pager .previous > a,
.pager .previous > span {
  float: left;
}
.pager .disabled > a,
.pager .disabled > a:hover,
.pager .disabled > a:focus,
.pager .disabled > span {
  color: #777777;
  background-color: #fff;
  cursor: not-allowed;
}
.label {
  display: inline;
  padding: .2em .6em .3em;
  font-size: 75%;
  font-weight: bold;
  line-height: 1;
  color: #fff;
  text-align: center;
  white-space: nowrap;
  vertical-align: baseline;
  border-radius: .25em;
}
a.label:hover,
a.label:focus {
  color: #fff;
  text-decoration: none;
  cursor: pointer;
}
.label:empty {
  display: none;
}
.btn .label {
  position: relative;
  top: -1px;
}
.label-default {
  background-color: #777777;
}
.label-default[href]:hover,
.label-default[href]:focus {
  background-color: #5e5e5e;
}
.label-primary {
  background-color: #337ab7;
}
.label-primary[href]:hover,
.label-primary[href]:focus {
  background-color: #286090;
}
.label-success {
  background-color: #5cb85c;
}
.label-success[href]:hover,
.label-success[href]:focus {
  background-color: #449d44;
}
.label-info {
  background-color: #5bc0de;
}
.label-info[href]:hover,
.label-info[href]:focus {
  background-color: #31b0d5;
}
.label-warning {
  background-color: #f0ad4e;
}
.label-warning[href]:hover,
.label-warning[href]:focus {
  background-color: #ec971f;
}
.label-danger {
  background-color: #d9534f;
}
.label-danger[href]:hover,
.label-danger[href]:focus {
  background-color: #c9302c;
}
.badge {
  display: inline-block;
  min-width: 10px;
  padding: 3px 7px;
  font-size: 12px;
  font-weight: bold;
  color: #fff;
  line-height: 1;
  vertical-align: middle;
  white-space: nowrap;
  text-align: center;
  background-color: #777777;
  border-radius: 10px;
}
.badge:empty {
  display: none;
}
.btn .badge {
  position: relative;
  top: -1px;
}
.btn-xs .badge,
.btn-group-xs > .btn .badge {
  top: 0;
  padding: 1px 5px;
}
a.badge:hover,
a.badge:focus {
  color: #fff;
  text-decoration: none;
  cursor: pointer;
}
.list-group-item.active > .badge,
.nav-pills > .active > a > .badge {
  color: #337ab7;
  background-color: #fff;
}
.list-group-item > .badge {
  float: right;
}
.list-group-item > .badge + .badge {
  margin-right: 5px;
}
.nav-pills > li > a > .badge {
  margin-left: 3px;
}
.jumbotron {
  padding-top: 30px;
  padding-bottom: 30px;
  margin-bottom: 30px;
  color: inherit;
  background-color: #eeeeee;
}
.jumbotron h1,
.jumbotron .h1 {
  color: inherit;
}
.jumbotron p {
  margin-bottom: 15px;
  font-size: 20px;
  font-weight: 200;
}
.jumbotron > hr {
  border-top-color: #d5d5d5;
}
.container .jumbotron,
.container-fluid .jumbotron {
  border-radius: 3px;
  padding-left: 0px;
  padding-right: 0px;
}
.jumbotron .container {
  max-width: 100%;
}
@media screen and (min-width: 768px) {
  .jumbotron {
    padding-top: 48px;
    padding-bottom: 48px;
  }
  .container .jumbotron,
  .container-fluid .jumbotron {
    padding-left: 60px;
    padding-right: 60px;
  }
  .jumbotron h1,
  .jumbotron .h1 {
    font-size: 59px;
  }
}
.thumbnail {
  display: block;
  padding: 4px;
  margin-bottom: 18px;
  line-height: 1.42857143;
  background-color: #fff;
  border: 1px solid #ddd;
  border-radius: 2px;
  -webkit-transition: border 0.2s ease-in-out;
  -o-transition: border 0.2s ease-in-out;
  transition: border 0.2s ease-in-out;
}
.thumbnail > img,
.thumbnail a > img {
  margin-left: auto;
  margin-right: auto;
}
a.thumbnail:hover,
a.thumbnail:focus,
a.thumbnail.active {
  border-color: #337ab7;
}
.thumbnail .caption {
  padding: 9px;
  color: #000;
}
.alert {
  padding: 15px;
  margin-bottom: 18px;
  border: 1px solid transparent;
  border-radius: 2px;
}
.alert h4 {
  margin-top: 0;
  color: inherit;
}
.alert .alert-link {
  font-weight: bold;
}
.alert > p,
.alert > ul {
  margin-bottom: 0;
}
.alert > p + p {
  margin-top: 5px;
}
.alert-dismissable,
.alert-dismissible {
  padding-right: 35px;
}
.alert-dismissable .close,
.alert-dismissible .close {
  position: relative;
  top: -2px;
  right: -21px;
  color: inherit;
}
.alert-success {
  background-color: #dff0d8;
  border-color: #d6e9c6;
  color: #3c763d;
}
.alert-success hr {
  border-top-color: #c9e2b3;
}
.alert-success .alert-link {
  color: #2b542c;
}
.alert-info {
  background-color: #d9edf7;
  border-color: #bce8f1;
  color: #31708f;
}
.alert-info hr {
  border-top-color: #a6e1ec;
}
.alert-info .alert-link {
  color: #245269;
}
.alert-warning {
  background-color: #fcf8e3;
  border-color: #faebcc;
  color: #8a6d3b;
}
.alert-warning hr {
  border-top-color: #f7e1b5;
}
.alert-warning .alert-link {
  color: #66512c;
}
.alert-danger {
  background-color: #f2dede;
  border-color: #ebccd1;
  color: #a94442;
}
.alert-danger hr {
  border-top-color: #e4b9c0;
}
.alert-danger .alert-link {
  color: #843534;
}
@-webkit-keyframes progress-bar-stripes {
  from {
    background-position: 40px 0;
  }
  to {
    background-position: 0 0;
  }
}
@keyframes progress-bar-stripes {
  from {
    background-position: 40px 0;
  }
  to {
    background-position: 0 0;
  }
}
.progress {
  overflow: hidden;
  height: 18px;
  margin-bottom: 18px;
  background-color: #f5f5f5;
  border-radius: 2px;
  -webkit-box-shadow: inset 0 1px 2px rgba(0, 0, 0, 0.1);
  box-shadow: inset 0 1px 2px rgba(0, 0, 0, 0.1);
}
.progress-bar {
  float: left;
  width: 0%;
  height: 100%;
  font-size: 12px;
  line-height: 18px;
  color: #fff;
  text-align: center;
  background-color: #337ab7;
  -webkit-box-shadow: inset 0 -1px 0 rgba(0, 0, 0, 0.15);
  box-shadow: inset 0 -1px 0 rgba(0, 0, 0, 0.15);
  -webkit-transition: width 0.6s ease;
  -o-transition: width 0.6s ease;
  transition: width 0.6s ease;
}
.progress-striped .progress-bar,
.progress-bar-striped {
  background-image: -webkit-linear-gradient(45deg, rgba(255, 255, 255, 0.15) 25%, transparent 25%, transparent 50%, rgba(255, 255, 255, 0.15) 50%, rgba(255, 255, 255, 0.15) 75%, transparent 75%, transparent);
  background-image: -o-linear-gradient(45deg, rgba(255, 255, 255, 0.15) 25%, transparent 25%, transparent 50%, rgba(255, 255, 255, 0.15) 50%, rgba(255, 255, 255, 0.15) 75%, transparent 75%, transparent);
  background-image: linear-gradient(45deg, rgba(255, 255, 255, 0.15) 25%, transparent 25%, transparent 50%, rgba(255, 255, 255, 0.15) 50%, rgba(255, 255, 255, 0.15) 75%, transparent 75%, transparent);
  background-size: 40px 40px;
}
.progress.active .progress-bar,
.progress-bar.active {
  -webkit-animation: progress-bar-stripes 2s linear infinite;
  -o-animation: progress-bar-stripes 2s linear infinite;
  animation: progress-bar-stripes 2s linear infinite;
}
.progress-bar-success {
  background-color: #5cb85c;
}
.progress-striped .progress-bar-success {
  background-image: -webkit-linear-gradient(45deg, rgba(255, 255, 255, 0.15) 25%, transparent 25%, transparent 50%, rgba(255, 255, 255, 0.15) 50%, rgba(255, 255, 255, 0.15) 75%, transparent 75%, transparent);
  background-image: -o-linear-gradient(45deg, rgba(255, 255, 255, 0.15) 25%, transparent 25%, transparent 50%, rgba(255, 255, 255, 0.15) 50%, rgba(255, 255, 255, 0.15) 75%, transparent 75%, transparent);
  background-image: linear-gradient(45deg, rgba(255, 255, 255, 0.15) 25%, transparent 25%, transparent 50%, rgba(255, 255, 255, 0.15) 50%, rgba(255, 255, 255, 0.15) 75%, transparent 75%, transparent);
}
.progress-bar-info {
  background-color: #5bc0de;
}
.progress-striped .progress-bar-info {
  background-image: -webkit-linear-gradient(45deg, rgba(255, 255, 255, 0.15) 25%, transparent 25%, transparent 50%, rgba(255, 255, 255, 0.15) 50%, rgba(255, 255, 255, 0.15) 75%, transparent 75%, transparent);
  background-image: -o-linear-gradient(45deg, rgba(255, 255, 255, 0.15) 25%, transparent 25%, transparent 50%, rgba(255, 255, 255, 0.15) 50%, rgba(255, 255, 255, 0.15) 75%, transparent 75%, transparent);
  background-image: linear-gradient(45deg, rgba(255, 255, 255, 0.15) 25%, transparent 25%, transparent 50%, rgba(255, 255, 255, 0.15) 50%, rgba(255, 255, 255, 0.15) 75%, transparent 75%, transparent);
}
.progress-bar-warning {
  background-color: #f0ad4e;
}
.progress-striped .progress-bar-warning {
  background-image: -webkit-linear-gradient(45deg, rgba(255, 255, 255, 0.15) 25%, transparent 25%, transparent 50%, rgba(255, 255, 255, 0.15) 50%, rgba(255, 255, 255, 0.15) 75%, transparent 75%, transparent);
  background-image: -o-linear-gradient(45deg, rgba(255, 255, 255, 0.15) 25%, transparent 25%, transparent 50%, rgba(255, 255, 255, 0.15) 50%, rgba(255, 255, 255, 0.15) 75%, transparent 75%, transparent);
  background-image: linear-gradient(45deg, rgba(255, 255, 255, 0.15) 25%, transparent 25%, transparent 50%, rgba(255, 255, 255, 0.15) 50%, rgba(255, 255, 255, 0.15) 75%, transparent 75%, transparent);
}
.progress-bar-danger {
  background-color: #d9534f;
}
.progress-striped .progress-bar-danger {
  background-image: -webkit-linear-gradient(45deg, rgba(255, 255, 255, 0.15) 25%, transparent 25%, transparent 50%, rgba(255, 255, 255, 0.15) 50%, rgba(255, 255, 255, 0.15) 75%, transparent 75%, transparent);
  background-image: -o-linear-gradient(45deg, rgba(255, 255, 255, 0.15) 25%, transparent 25%, transparent 50%, rgba(255, 255, 255, 0.15) 50%, rgba(255, 255, 255, 0.15) 75%, transparent 75%, transparent);
  background-image: linear-gradient(45deg, rgba(255, 255, 255, 0.15) 25%, transparent 25%, transparent 50%, rgba(255, 255, 255, 0.15) 50%, rgba(255, 255, 255, 0.15) 75%, transparent 75%, transparent);
}
.media {
  margin-top: 15px;
}
.media:first-child {
  margin-top: 0;
}
.media,
.media-body {
  zoom: 1;
  overflow: hidden;
}
.media-body {
  width: 10000px;
}
.media-object {
  display: block;
}
.media-object.img-thumbnail {
  max-width: none;
}
.media-right,
.media > .pull-right {
  padding-left: 10px;
}
.media-left,
.media > .pull-left {
  padding-right: 10px;
}
.media-left,
.media-right,
.media-body {
  display: table-cell;
  vertical-align: top;
}
.media-middle {
  vertical-align: middle;
}
.media-bottom {
  vertical-align: bottom;
}
.media-heading {
  margin-top: 0;
  margin-bottom: 5px;
}
.media-list {
  padding-left: 0;
  list-style: none;
}
.list-group {
  margin-bottom: 20px;
  padding-left: 0;
}
.list-group-item {
  position: relative;
  display: block;
  padding: 10px 15px;
  margin-bottom: -1px;
  background-color: #fff;
  border: 1px solid #ddd;
}
.list-group-item:first-child {
  border-top-right-radius: 2px;
  border-top-left-radius: 2px;
}
.list-group-item:last-child {
  margin-bottom: 0;
  border-bottom-right-radius: 2px;
  border-bottom-left-radius: 2px;
}
a.list-group-item,
button.list-group-item {
  color: #555;
}
a.list-group-item .list-group-item-heading,
button.list-group-item .list-group-item-heading {
  color: #333;
}
a.list-group-item:hover,
button.list-group-item:hover,
a.list-group-item:focus,
button.list-group-item:focus {
  text-decoration: none;
  color: #555;
  background-color: #f5f5f5;
}
button.list-group-item {
  width: 100%;
  text-align: left;
}
.list-group-item.disabled,
.list-group-item.disabled:hover,
.list-group-item.disabled:focus {
  background-color: #eeeeee;
  color: #777777;
  cursor: not-allowed;
}
.list-group-item.disabled .list-group-item-heading,
.list-group-item.disabled:hover .list-group-item-heading,
.list-group-item.disabled:focus .list-group-item-heading {
  color: inherit;
}
.list-group-item.disabled .list-group-item-text,
.list-group-item.disabled:hover .list-group-item-text,
.list-group-item.disabled:focus .list-group-item-text {
  color: #777777;
}
.list-group-item.active,
.list-group-item.active:hover,
.list-group-item.active:focus {
  z-index: 2;
  color: #fff;
  background-color: #337ab7;
  border-color: #337ab7;
}
.list-group-item.active .list-group-item-heading,
.list-group-item.active:hover .list-group-item-heading,
.list-group-item.active:focus .list-group-item-heading,
.list-group-item.active .list-group-item-heading > small,
.list-group-item.active:hover .list-group-item-heading > small,
.list-group-item.active:focus .list-group-item-heading > small,
.list-group-item.active .list-group-item-heading > .small,
.list-group-item.active:hover .list-group-item-heading > .small,
.list-group-item.active:focus .list-group-item-heading > .small {
  color: inherit;
}
.list-group-item.active .list-group-item-text,
.list-group-item.active:hover .list-group-item-text,
.list-group-item.active:focus .list-group-item-text {
  color: #c7ddef;
}
.list-group-item-success {
  color: #3c763d;
  background-color: #dff0d8;
}
a.list-group-item-success,
button.list-group-item-success {
  color: #3c763d;
}
a.list-group-item-success .list-group-item-heading,
button.list-group-item-success .list-group-item-heading {
  color: inherit;
}
a.list-group-item-success:hover,
button.list-group-item-success:hover,
a.list-group-item-success:focus,
button.list-group-item-success:focus {
  color: #3c763d;
  background-color: #d0e9c6;
}
a.list-group-item-success.active,
button.list-group-item-success.active,
a.list-group-item-success.active:hover,
button.list-group-item-success.active:hover,
a.list-group-item-success.active:focus,
button.list-group-item-success.active:focus {
  color: #fff;
  background-color: #3c763d;
  border-color: #3c763d;
}
.list-group-item-info {
  color: #31708f;
  background-color: #d9edf7;
}
a.list-group-item-info,
button.list-group-item-info {
  color: #31708f;
}
a.list-group-item-info .list-group-item-heading,
button.list-group-item-info .list-group-item-heading {
  color: inherit;
}
a.list-group-item-info:hover,
button.list-group-item-info:hover,
a.list-group-item-info:focus,
button.list-group-item-info:focus {
  color: #31708f;
  background-color: #c4e3f3;
}
a.list-group-item-info.active,
button.list-group-item-info.active,
a.list-group-item-info.active:hover,
button.list-group-item-info.active:hover,
a.list-group-item-info.active:focus,
button.list-group-item-info.active:focus {
  color: #fff;
  background-color: #31708f;
  border-color: #31708f;
}
.list-group-item-warning {
  color: #8a6d3b;
  background-color: #fcf8e3;
}
a.list-group-item-warning,
button.list-group-item-warning {
  color: #8a6d3b;
}
a.list-group-item-warning .list-group-item-heading,
button.list-group-item-warning .list-group-item-heading {
  color: inherit;
}
a.list-group-item-warning:hover,
button.list-group-item-warning:hover,
a.list-group-item-warning:focus,
button.list-group-item-warning:focus {
  color: #8a6d3b;
  background-color: #faf2cc;
}
a.list-group-item-warning.active,
button.list-group-item-warning.active,
a.list-group-item-warning.active:hover,
button.list-group-item-warning.active:hover,
a.list-group-item-warning.active:focus,
button.list-group-item-warning.active:focus {
  color: #fff;
  background-color: #8a6d3b;
  border-color: #8a6d3b;
}
.list-group-item-danger {
  color: #a94442;
  background-color: #f2dede;
}
a.list-group-item-danger,
button.list-group-item-danger {
  color: #a94442;
}
a.list-group-item-danger .list-group-item-heading,
button.list-group-item-danger .list-group-item-heading {
  color: inherit;
}
a.list-group-item-danger:hover,
button.list-group-item-danger:hover,
a.list-group-item-danger:focus,
button.list-group-item-danger:focus {
  color: #a94442;
  background-color: #ebcccc;
}
a.list-group-item-danger.active,
button.list-group-item-danger.active,
a.list-group-item-danger.active:hover,
button.list-group-item-danger.active:hover,
a.list-group-item-danger.active:focus,
button.list-group-item-danger.active:focus {
  color: #fff;
  background-color: #a94442;
  border-color: #a94442;
}
.list-group-item-heading {
  margin-top: 0;
  margin-bottom: 5px;
}
.list-group-item-text {
  margin-bottom: 0;
  line-height: 1.3;
}
.panel {
  margin-bottom: 18px;
  background-color: #fff;
  border: 1px solid transparent;
  border-radius: 2px;
  -webkit-box-shadow: 0 1px 1px rgba(0, 0, 0, 0.05);
  box-shadow: 0 1px 1px rgba(0, 0, 0, 0.05);
}
.panel-body {
  padding: 15px;
}
.panel-heading {
  padding: 10px 15px;
  border-bottom: 1px solid transparent;
  border-top-right-radius: 1px;
  border-top-left-radius: 1px;
}
.panel-heading > .dropdown .dropdown-toggle {
  color: inherit;
}
.panel-title {
  margin-top: 0;
  margin-bottom: 0;
  font-size: 15px;
  color: inherit;
}
.panel-title > a,
.panel-title > small,
.panel-title > .small,
.panel-title > small > a,
.panel-title > .small > a {
  color: inherit;
}
.panel-footer {
  padding: 10px 15px;
  background-color: #f5f5f5;
  border-top: 1px solid #ddd;
  border-bottom-right-radius: 1px;
  border-bottom-left-radius: 1px;
}
.panel > .list-group,
.panel > .panel-collapse > .list-group {
  margin-bottom: 0;
}
.panel > .list-group .list-group-item,
.panel > .panel-collapse > .list-group .list-group-item {
  border-width: 1px 0;
  border-radius: 0;
}
.panel > .list-group:first-child .list-group-item:first-child,
.panel > .panel-collapse > .list-group:first-child .list-group-item:first-child {
  border-top: 0;
  border-top-right-radius: 1px;
  border-top-left-radius: 1px;
}
.panel > .list-group:last-child .list-group-item:last-child,
.panel > .panel-collapse > .list-group:last-child .list-group-item:last-child {
  border-bottom: 0;
  border-bottom-right-radius: 1px;
  border-bottom-left-radius: 1px;
}
.panel > .panel-heading + .panel-collapse > .list-group .list-group-item:first-child {
  border-top-right-radius: 0;
  border-top-left-radius: 0;
}
.panel-heading + .list-group .list-group-item:first-child {
  border-top-width: 0;
}
.list-group + .panel-footer {
  border-top-width: 0;
}
.panel > .table,
.panel > .table-responsive > .table,
.panel > .panel-collapse > .table {
  margin-bottom: 0;
}
.panel > .table caption,
.panel > .table-responsive > .table caption,
.panel > .panel-collapse > .table caption {
  padding-left: 15px;
  padding-right: 15px;
}
.panel > .table:first-child,
.panel > .table-responsive:first-child > .table:first-child {
  border-top-right-radius: 1px;
  border-top-left-radius: 1px;
}
.panel > .table:first-child > thead:first-child > tr:first-child,
.panel > .table-responsive:first-child > .table:first-child > thead:first-child > tr:first-child,
.panel > .table:first-child > tbody:first-child > tr:first-child,
.panel > .table-responsive:first-child > .table:first-child > tbody:first-child > tr:first-child {
  border-top-left-radius: 1px;
  border-top-right-radius: 1px;
}
.panel > .table:first-child > thead:first-child > tr:first-child td:first-child,
.panel > .table-responsive:first-child > .table:first-child > thead:first-child > tr:first-child td:first-child,
.panel > .table:first-child > tbody:first-child > tr:first-child td:first-child,
.panel > .table-responsive:first-child > .table:first-child > tbody:first-child > tr:first-child td:first-child,
.panel > .table:first-child > thead:first-child > tr:first-child th:first-child,
.panel > .table-responsive:first-child > .table:first-child > thead:first-child > tr:first-child th:first-child,
.panel > .table:first-child > tbody:first-child > tr:first-child th:first-child,
.panel > .table-responsive:first-child > .table:first-child > tbody:first-child > tr:first-child th:first-child {
  border-top-left-radius: 1px;
}
.panel > .table:first-child > thead:first-child > tr:first-child td:last-child,
.panel > .table-responsive:first-child > .table:first-child > thead:first-child > tr:first-child td:last-child,
.panel > .table:first-child > tbody:first-child > tr:first-child td:last-child,
.panel > .table-responsive:first-child > .table:first-child > tbody:first-child > tr:first-child td:last-child,
.panel > .table:first-child > thead:first-child > tr:first-child th:last-child,
.panel > .table-responsive:first-child > .table:first-child > thead:first-child > tr:first-child th:last-child,
.panel > .table:first-child > tbody:first-child > tr:first-child th:last-child,
.panel > .table-responsive:first-child > .table:first-child > tbody:first-child > tr:first-child th:last-child {
  border-top-right-radius: 1px;
}
.panel > .table:last-child,
.panel > .table-responsive:last-child > .table:last-child {
  border-bottom-right-radius: 1px;
  border-bottom-left-radius: 1px;
}
.panel > .table:last-child > tbody:last-child > tr:last-child,
.panel > .table-responsive:last-child > .table:last-child > tbody:last-child > tr:last-child,
.panel > .table:last-child > tfoot:last-child > tr:last-child,
.panel > .table-responsive:last-child > .table:last-child > tfoot:last-child > tr:last-child {
  border-bottom-left-radius: 1px;
  border-bottom-right-radius: 1px;
}
.panel > .table:last-child > tbody:last-child > tr:last-child td:first-child,
.panel > .table-responsive:last-child > .table:last-child > tbody:last-child > tr:last-child td:first-child,
.panel > .table:last-child > tfoot:last-child > tr:last-child td:first-child,
.panel > .table-responsive:last-child > .table:last-child > tfoot:last-child > tr:last-child td:first-child,
.panel > .table:last-child > tbody:last-child > tr:last-child th:first-child,
.panel > .table-responsive:last-child > .table:last-child > tbody:last-child > tr:last-child th:first-child,
.panel > .table:last-child > tfoot:last-child > tr:last-child th:first-child,
.panel > .table-responsive:last-child > .table:last-child > tfoot:last-child > tr:last-child th:first-child {
  border-bottom-left-radius: 1px;
}
.panel > .table:last-child > tbody:last-child > tr:last-child td:last-child,
.panel > .table-responsive:last-child > .table:last-child > tbody:last-child > tr:last-child td:last-child,
.panel > .table:last-child > tfoot:last-child > tr:last-child td:last-child,
.panel > .table-responsive:last-child > .table:last-child > tfoot:last-child > tr:last-child td:last-child,
.panel > .table:last-child > tbody:last-child > tr:last-child th:last-child,
.panel > .table-responsive:last-child > .table:last-child > tbody:last-child > tr:last-child th:last-child,
.panel > .table:last-child > tfoot:last-child > tr:last-child th:last-child,
.panel > .table-responsive:last-child > .table:last-child > tfoot:last-child > tr:last-child th:last-child {
  border-bottom-right-radius: 1px;
}
.panel > .panel-body + .table,
.panel > .panel-body + .table-responsive,
.panel > .table + .panel-body,
.panel > .table-responsive + .panel-body {
  border-top: 1px solid #ddd;
}
.panel > .table > tbody:first-child > tr:first-child th,
.panel > .table > tbody:first-child > tr:first-child td {
  border-top: 0;
}
.panel > .table-bordered,
.panel > .table-responsive > .table-bordered {
  border: 0;
}
.panel > .table-bordered > thead > tr > th:first-child,
.panel > .table-responsive > .table-bordered > thead > tr > th:first-child,
.panel > .table-bordered > tbody > tr > th:first-child,
.panel > .table-responsive > .table-bordered > tbody > tr > th:first-child,
.panel > .table-bordered > tfoot > tr > th:first-child,
.panel > .table-responsive > .table-bordered > tfoot > tr > th:first-child,
.panel > .table-bordered > thead > tr > td:first-child,
.panel > .table-responsive > .table-bordered > thead > tr > td:first-child,
.panel > .table-bordered > tbody > tr > td:first-child,
.panel > .table-responsive > .table-bordered > tbody > tr > td:first-child,
.panel > .table-bordered > tfoot > tr > td:first-child,
.panel > .table-responsive > .table-bordered > tfoot > tr > td:first-child {
  border-left: 0;
}
.panel > .table-bordered > thead > tr > th:last-child,
.panel > .table-responsive > .table-bordered > thead > tr > th:last-child,
.panel > .table-bordered > tbody > tr > th:last-child,
.panel > .table-responsive > .table-bordered > tbody > tr > th:last-child,
.panel > .table-bordered > tfoot > tr > th:last-child,
.panel > .table-responsive > .table-bordered > tfoot > tr > th:last-child,
.panel > .table-bordered > thead > tr > td:last-child,
.panel > .table-responsive > .table-bordered > thead > tr > td:last-child,
.panel > .table-bordered > tbody > tr > td:last-child,
.panel > .table-responsive > .table-bordered > tbody > tr > td:last-child,
.panel > .table-bordered > tfoot > tr > td:last-child,
.panel > .table-responsive > .table-bordered > tfoot > tr > td:last-child {
  border-right: 0;
}
.panel > .table-bordered > thead > tr:first-child > td,
.panel > .table-responsive > .table-bordered > thead > tr:first-child > td,
.panel > .table-bordered > tbody > tr:first-child > td,
.panel > .table-responsive > .table-bordered > tbody > tr:first-child > td,
.panel > .table-bordered > thead > tr:first-child > th,
.panel > .table-responsive > .table-bordered > thead > tr:first-child > th,
.panel > .table-bordered > tbody > tr:first-child > th,
.panel > .table-responsive > .table-bordered > tbody > tr:first-child > th {
  border-bottom: 0;
}
.panel > .table-bordered > tbody > tr:last-child > td,
.panel > .table-responsive > .table-bordered > tbody > tr:last-child > td,
.panel > .table-bordered > tfoot > tr:last-child > td,
.panel > .table-responsive > .table-bordered > tfoot > tr:last-child > td,
.panel > .table-bordered > tbody > tr:last-child > th,
.panel > .table-responsive > .table-bordered > tbody > tr:last-child > th,
.panel > .table-bordered > tfoot > tr:last-child > th,
.panel > .table-responsive > .table-bordered > tfoot > tr:last-child > th {
  border-bottom: 0;
}
.panel > .table-responsive {
  border: 0;
  margin-bottom: 0;
}
.panel-group {
  margin-bottom: 18px;
}
.panel-group .panel {
  margin-bottom: 0;
  border-radius: 2px;
}
.panel-group .panel + .panel {
  margin-top: 5px;
}
.panel-group .panel-heading {
  border-bottom: 0;
}
.panel-group .panel-heading + .panel-collapse > .panel-body,
.panel-group .panel-heading + .panel-collapse > .list-group {
  border-top: 1px solid #ddd;
}
.panel-group .panel-footer {
  border-top: 0;
}
.panel-group .panel-footer + .panel-collapse .panel-body {
  border-bottom: 1px solid #ddd;
}
.panel-default {
  border-color: #ddd;
}
.panel-default > .panel-heading {
  color: #333333;
  background-color: #f5f5f5;
  border-color: #ddd;
}
.panel-default > .panel-heading + .panel-collapse > .panel-body {
  border-top-color: #ddd;
}
.panel-default > .panel-heading .badge {
  color: #f5f5f5;
  background-color: #333333;
}
.panel-default > .panel-footer + .panel-collapse > .panel-body {
  border-bottom-color: #ddd;
}
.panel-primary {
  border-color: #337ab7;
}
.panel-primary > .panel-heading {
  color: #fff;
  background-color: #337ab7;
  border-color: #337ab7;
}
.panel-primary > .panel-heading + .panel-collapse > .panel-body {
  border-top-color: #337ab7;
}
.panel-primary > .panel-heading .badge {
  color: #337ab7;
  background-color: #fff;
}
.panel-primary > .panel-footer + .panel-collapse > .panel-body {
  border-bottom-color: #337ab7;
}
.panel-success {
  border-color: #d6e9c6;
}
.panel-success > .panel-heading {
  color: #3c763d;
  background-color: #dff0d8;
  border-color: #d6e9c6;
}
.panel-success > .panel-heading + .panel-collapse > .panel-body {
  border-top-color: #d6e9c6;
}
.panel-success > .panel-heading .badge {
  color: #dff0d8;
  background-color: #3c763d;
}
.panel-success > .panel-footer + .panel-collapse > .panel-body {
  border-bottom-color: #d6e9c6;
}
.panel-info {
  border-color: #bce8f1;
}
.panel-info > .panel-heading {
  color: #31708f;
  background-color: #d9edf7;
  border-color: #bce8f1;
}
.panel-info > .panel-heading + .panel-collapse > .panel-body {
  border-top-color: #bce8f1;
}
.panel-info > .panel-heading .badge {
  color: #d9edf7;
  background-color: #31708f;
}
.panel-info > .panel-footer + .panel-collapse > .panel-body {
  border-bottom-color: #bce8f1;
}
.panel-warning {
  border-color: #faebcc;
}
.panel-warning > .panel-heading {
  color: #8a6d3b;
  background-color: #fcf8e3;
  border-color: #faebcc;
}
.panel-warning > .panel-heading + .panel-collapse > .panel-body {
  border-top-color: #faebcc;
}
.panel-warning > .panel-heading .badge {
  color: #fcf8e3;
  background-color: #8a6d3b;
}
.panel-warning > .panel-footer + .panel-collapse > .panel-body {
  border-bottom-color: #faebcc;
}
.panel-danger {
  border-color: #ebccd1;
}
.panel-danger > .panel-heading {
  color: #a94442;
  background-color: #f2dede;
  border-color: #ebccd1;
}
.panel-danger > .panel-heading + .panel-collapse > .panel-body {
  border-top-color: #ebccd1;
}
.panel-danger > .panel-heading .badge {
  color: #f2dede;
  background-color: #a94442;
}
.panel-danger > .panel-footer + .panel-collapse > .panel-body {
  border-bottom-color: #ebccd1;
}
.embed-responsive {
  position: relative;
  display: block;
  height: 0;
  padding: 0;
  overflow: hidden;
}
.embed-responsive .embed-responsive-item,
.embed-responsive iframe,
.embed-responsive embed,
.embed-responsive object,
.embed-responsive video {
  position: absolute;
  top: 0;
  left: 0;
  bottom: 0;
  height: 100%;
  width: 100%;
  border: 0;
}
.embed-responsive-16by9 {
  padding-bottom: 56.25%;
}
.embed-responsive-4by3 {
  padding-bottom: 75%;
}
.well {
  min-height: 20px;
  padding: 19px;
  margin-bottom: 20px;
  background-color: #f5f5f5;
  border: 1px solid #e3e3e3;
  border-radius: 2px;
  -webkit-box-shadow: inset 0 1px 1px rgba(0, 0, 0, 0.05);
  box-shadow: inset 0 1px 1px rgba(0, 0, 0, 0.05);
}
.well blockquote {
  border-color: #ddd;
  border-color: rgba(0, 0, 0, 0.15);
}
.well-lg {
  padding: 24px;
  border-radius: 3px;
}
.well-sm {
  padding: 9px;
  border-radius: 1px;
}
.close {
  float: right;
  font-size: 19.5px;
  font-weight: bold;
  line-height: 1;
  color: #000;
  text-shadow: 0 1px 0 #fff;
  opacity: 0.2;
  filter: alpha(opacity=20);
}
.close:hover,
.close:focus {
  color: #000;
  text-decoration: none;
  cursor: pointer;
  opacity: 0.5;
  filter: alpha(opacity=50);
}
button.close {
  padding: 0;
  cursor: pointer;
  background: transparent;
  border: 0;
  -webkit-appearance: none;
}
.modal-open {
  overflow: hidden;
}
.modal {
  display: none;
  overflow: hidden;
  position: fixed;
  top: 0;
  right: 0;
  bottom: 0;
  left: 0;
  z-index: 1050;
  -webkit-overflow-scrolling: touch;
  outline: 0;
}
.modal.fade .modal-dialog {
  -webkit-transform: translate(0, -25%);
  -ms-transform: translate(0, -25%);
  -o-transform: translate(0, -25%);
  transform: translate(0, -25%);
  -webkit-transition: -webkit-transform 0.3s ease-out;
  -moz-transition: -moz-transform 0.3s ease-out;
  -o-transition: -o-transform 0.3s ease-out;
  transition: transform 0.3s ease-out;
}
.modal.in .modal-dialog {
  -webkit-transform: translate(0, 0);
  -ms-transform: translate(0, 0);
  -o-transform: translate(0, 0);
  transform: translate(0, 0);
}
.modal-open .modal {
  overflow-x: hidden;
  overflow-y: auto;
}
.modal-dialog {
  position: relative;
  width: auto;
  margin: 10px;
}
.modal-content {
  position: relative;
  background-color: #fff;
  border: 1px solid #999;
  border: 1px solid rgba(0, 0, 0, 0.2);
  border-radius: 3px;
  -webkit-box-shadow: 0 3px 9px rgba(0, 0, 0, 0.5);
  box-shadow: 0 3px 9px rgba(0, 0, 0, 0.5);
  background-clip: padding-box;
  outline: 0;
}
.modal-backdrop {
  position: fixed;
  top: 0;
  right: 0;
  bottom: 0;
  left: 0;
  z-index: 1040;
  background-color: #000;
}
.modal-backdrop.fade {
  opacity: 0;
  filter: alpha(opacity=0);
}
.modal-backdrop.in {
  opacity: 0.5;
  filter: alpha(opacity=50);
}
.modal-header {
  padding: 15px;
  border-bottom: 1px solid #e5e5e5;
}
.modal-header .close {
  margin-top: -2px;
}
.modal-title {
  margin: 0;
  line-height: 1.42857143;
}
.modal-body {
  position: relative;
  padding: 15px;
}
.modal-footer {
  padding: 15px;
  text-align: right;
  border-top: 1px solid #e5e5e5;
}
.modal-footer .btn + .btn {
  margin-left: 5px;
  margin-bottom: 0;
}
.modal-footer .btn-group .btn + .btn {
  margin-left: -1px;
}
.modal-footer .btn-block + .btn-block {
  margin-left: 0;
}
.modal-scrollbar-measure {
  position: absolute;
  top: -9999px;
  width: 50px;
  height: 50px;
  overflow: scroll;
}
@media (min-width: 768px) {
  .modal-dialog {
    width: 600px;
    margin: 30px auto;
  }
  .modal-content {
    -webkit-box-shadow: 0 5px 15px rgba(0, 0, 0, 0.5);
    box-shadow: 0 5px 15px rgba(0, 0, 0, 0.5);
  }
  .modal-sm {
    width: 300px;
  }
}
@media (min-width: 992px) {
  .modal-lg {
    width: 900px;
  }
}
.tooltip {
  position: absolute;
  z-index: 1070;
  display: block;
  font-family: "Helvetica Neue", Helvetica, Arial, sans-serif;
  font-style: normal;
  font-weight: normal;
  letter-spacing: normal;
  line-break: auto;
  line-height: 1.42857143;
  text-align: left;
  text-align: start;
  text-decoration: none;
  text-shadow: none;
  text-transform: none;
  white-space: normal;
  word-break: normal;
  word-spacing: normal;
  word-wrap: normal;
  font-size: 12px;
  opacity: 0;
  filter: alpha(opacity=0);
}
.tooltip.in {
  opacity: 0.9;
  filter: alpha(opacity=90);
}
.tooltip.top {
  margin-top: -3px;
  padding: 5px 0;
}
.tooltip.right {
  margin-left: 3px;
  padding: 0 5px;
}
.tooltip.bottom {
  margin-top: 3px;
  padding: 5px 0;
}
.tooltip.left {
  margin-left: -3px;
  padding: 0 5px;
}
.tooltip-inner {
  max-width: 200px;
  padding: 3px 8px;
  color: #fff;
  text-align: center;
  background-color: #000;
  border-radius: 2px;
}
.tooltip-arrow {
  position: absolute;
  width: 0;
  height: 0;
  border-color: transparent;
  border-style: solid;
}
.tooltip.top .tooltip-arrow {
  bottom: 0;
  left: 50%;
  margin-left: -5px;
  border-width: 5px 5px 0;
  border-top-color: #000;
}
.tooltip.top-left .tooltip-arrow {
  bottom: 0;
  right: 5px;
  margin-bottom: -5px;
  border-width: 5px 5px 0;
  border-top-color: #000;
}
.tooltip.top-right .tooltip-arrow {
  bottom: 0;
  left: 5px;
  margin-bottom: -5px;
  border-width: 5px 5px 0;
  border-top-color: #000;
}
.tooltip.right .tooltip-arrow {
  top: 50%;
  left: 0;
  margin-top: -5px;
  border-width: 5px 5px 5px 0;
  border-right-color: #000;
}
.tooltip.left .tooltip-arrow {
  top: 50%;
  right: 0;
  margin-top: -5px;
  border-width: 5px 0 5px 5px;
  border-left-color: #000;
}
.tooltip.bottom .tooltip-arrow {
  top: 0;
  left: 50%;
  margin-left: -5px;
  border-width: 0 5px 5px;
  border-bottom-color: #000;
}
.tooltip.bottom-left .tooltip-arrow {
  top: 0;
  right: 5px;
  margin-top: -5px;
  border-width: 0 5px 5px;
  border-bottom-color: #000;
}
.tooltip.bottom-right .tooltip-arrow {
  top: 0;
  left: 5px;
  margin-top: -5px;
  border-width: 0 5px 5px;
  border-bottom-color: #000;
}
.popover {
  position: absolute;
  top: 0;
  left: 0;
  z-index: 1060;
  display: none;
  max-width: 276px;
  padding: 1px;
  font-family: "Helvetica Neue", Helvetica, Arial, sans-serif;
  font-style: normal;
  font-weight: normal;
  letter-spacing: normal;
  line-break: auto;
  line-height: 1.42857143;
  text-align: left;
  text-align: start;
  text-decoration: none;
  text-shadow: none;
  text-transform: none;
  white-space: normal;
  word-break: normal;
  word-spacing: normal;
  word-wrap: normal;
  font-size: 13px;
  background-color: #fff;
  background-clip: padding-box;
  border: 1px solid #ccc;
  border: 1px solid rgba(0, 0, 0, 0.2);
  border-radius: 3px;
  -webkit-box-shadow: 0 5px 10px rgba(0, 0, 0, 0.2);
  box-shadow: 0 5px 10px rgba(0, 0, 0, 0.2);
}
.popover.top {
  margin-top: -10px;
}
.popover.right {
  margin-left: 10px;
}
.popover.bottom {
  margin-top: 10px;
}
.popover.left {
  margin-left: -10px;
}
.popover-title {
  margin: 0;
  padding: 8px 14px;
  font-size: 13px;
  background-color: #f7f7f7;
  border-bottom: 1px solid #ebebeb;
  border-radius: 2px 2px 0 0;
}
.popover-content {
  padding: 9px 14px;
}
.popover > .arrow,
.popover > .arrow:after {
  position: absolute;
  display: block;
  width: 0;
  height: 0;
  border-color: transparent;
  border-style: solid;
}
.popover > .arrow {
  border-width: 11px;
}
.popover > .arrow:after {
  border-width: 10px;
  content: "";
}
.popover.top > .arrow {
  left: 50%;
  margin-left: -11px;
  border-bottom-width: 0;
  border-top-color: #999999;
  border-top-color: rgba(0, 0, 0, 0.25);
  bottom: -11px;
}
.popover.top > .arrow:after {
  content: " ";
  bottom: 1px;
  margin-left: -10px;
  border-bottom-width: 0;
  border-top-color: #fff;
}
.popover.right > .arrow {
  top: 50%;
  left: -11px;
  margin-top: -11px;
  border-left-width: 0;
  border-right-color: #999999;
  border-right-color: rgba(0, 0, 0, 0.25);
}
.popover.right > .arrow:after {
  content: " ";
  left: 1px;
  bottom: -10px;
  border-left-width: 0;
  border-right-color: #fff;
}
.popover.bottom > .arrow {
  left: 50%;
  margin-left: -11px;
  border-top-width: 0;
  border-bottom-color: #999999;
  border-bottom-color: rgba(0, 0, 0, 0.25);
  top: -11px;
}
.popover.bottom > .arrow:after {
  content: " ";
  top: 1px;
  margin-left: -10px;
  border-top-width: 0;
  border-bottom-color: #fff;
}
.popover.left > .arrow {
  top: 50%;
  right: -11px;
  margin-top: -11px;
  border-right-width: 0;
  border-left-color: #999999;
  border-left-color: rgba(0, 0, 0, 0.25);
}
.popover.left > .arrow:after {
  content: " ";
  right: 1px;
  border-right-width: 0;
  border-left-color: #fff;
  bottom: -10px;
}
.carousel {
  position: relative;
}
.carousel-inner {
  position: relative;
  overflow: hidden;
  width: 100%;
}
.carousel-inner > .item {
  display: none;
  position: relative;
  -webkit-transition: 0.6s ease-in-out left;
  -o-transition: 0.6s ease-in-out left;
  transition: 0.6s ease-in-out left;
}
.carousel-inner > .item > img,
.carousel-inner > .item > a > img {
  line-height: 1;
}
@media all and (transform-3d), (-webkit-transform-3d) {
  .carousel-inner > .item {
    -webkit-transition: -webkit-transform 0.6s ease-in-out;
    -moz-transition: -moz-transform 0.6s ease-in-out;
    -o-transition: -o-transform 0.6s ease-in-out;
    transition: transform 0.6s ease-in-out;
    -webkit-backface-visibility: hidden;
    -moz-backface-visibility: hidden;
    backface-visibility: hidden;
    -webkit-perspective: 1000px;
    -moz-perspective: 1000px;
    perspective: 1000px;
  }
  .carousel-inner > .item.next,
  .carousel-inner > .item.active.right {
    -webkit-transform: translate3d(100%, 0, 0);
    transform: translate3d(100%, 0, 0);
    left: 0;
  }
  .carousel-inner > .item.prev,
  .carousel-inner > .item.active.left {
    -webkit-transform: translate3d(-100%, 0, 0);
    transform: translate3d(-100%, 0, 0);
    left: 0;
  }
  .carousel-inner > .item.next.left,
  .carousel-inner > .item.prev.right,
  .carousel-inner > .item.active {
    -webkit-transform: translate3d(0, 0, 0);
    transform: translate3d(0, 0, 0);
    left: 0;
  }
}
.carousel-inner > .active,
.carousel-inner > .next,
.carousel-inner > .prev {
  display: block;
}
.carousel-inner > .active {
  left: 0;
}
.carousel-inner > .next,
.carousel-inner > .prev {
  position: absolute;
  top: 0;
  width: 100%;
}
.carousel-inner > .next {
  left: 100%;
}
.carousel-inner > .prev {
  left: -100%;
}
.carousel-inner > .next.left,
.carousel-inner > .prev.right {
  left: 0;
}
.carousel-inner > .active.left {
  left: -100%;
}
.carousel-inner > .active.right {
  left: 100%;
}
.carousel-control {
  position: absolute;
  top: 0;
  left: 0;
  bottom: 0;
  width: 15%;
  opacity: 0.5;
  filter: alpha(opacity=50);
  font-size: 20px;
  color: #fff;
  text-align: center;
  text-shadow: 0 1px 2px rgba(0, 0, 0, 0.6);
  background-color: rgba(0, 0, 0, 0);
}
.carousel-control.left {
  background-image: -webkit-linear-gradient(left, rgba(0, 0, 0, 0.5) 0%, rgba(0, 0, 0, 0.0001) 100%);
  background-image: -o-linear-gradient(left, rgba(0, 0, 0, 0.5) 0%, rgba(0, 0, 0, 0.0001) 100%);
  background-image: linear-gradient(to right, rgba(0, 0, 0, 0.5) 0%, rgba(0, 0, 0, 0.0001) 100%);
  background-repeat: repeat-x;
  filter: progid:DXImageTransform.Microsoft.gradient(startColorstr='#80000000', endColorstr='#00000000', GradientType=1);
}
.carousel-control.right {
  left: auto;
  right: 0;
  background-image: -webkit-linear-gradient(left, rgba(0, 0, 0, 0.0001) 0%, rgba(0, 0, 0, 0.5) 100%);
  background-image: -o-linear-gradient(left, rgba(0, 0, 0, 0.0001) 0%, rgba(0, 0, 0, 0.5) 100%);
  background-image: linear-gradient(to right, rgba(0, 0, 0, 0.0001) 0%, rgba(0, 0, 0, 0.5) 100%);
  background-repeat: repeat-x;
  filter: progid:DXImageTransform.Microsoft.gradient(startColorstr='#00000000', endColorstr='#80000000', GradientType=1);
}
.carousel-control:hover,
.carousel-control:focus {
  outline: 0;
  color: #fff;
  text-decoration: none;
  opacity: 0.9;
  filter: alpha(opacity=90);
}
.carousel-control .icon-prev,
.carousel-control .icon-next,
.carousel-control .glyphicon-chevron-left,
.carousel-control .glyphicon-chevron-right {
  position: absolute;
  top: 50%;
  margin-top: -10px;
  z-index: 5;
  display: inline-block;
}
.carousel-control .icon-prev,
.carousel-control .glyphicon-chevron-left {
  left: 50%;
  margin-left: -10px;
}
.carousel-control .icon-next,
.carousel-control .glyphicon-chevron-right {
  right: 50%;
  margin-right: -10px;
}
.carousel-control .icon-prev,
.carousel-control .icon-next {
  width: 20px;
  height: 20px;
  line-height: 1;
  font-family: serif;
}
.carousel-control .icon-prev:before {
  content: '\2039';
}
.carousel-control .icon-next:before {
  content: '\203a';
}
.carousel-indicators {
  position: absolute;
  bottom: 10px;
  left: 50%;
  z-index: 15;
  width: 60%;
  margin-left: -30%;
  padding-left: 0;
  list-style: none;
  text-align: center;
}
.carousel-indicators li {
  display: inline-block;
  width: 10px;
  height: 10px;
  margin: 1px;
  text-indent: -999px;
  border: 1px solid #fff;
  border-radius: 10px;
  cursor: pointer;
  background-color: #000 \9;
  background-color: rgba(0, 0, 0, 0);
}
.carousel-indicators .active {
  margin: 0;
  width: 12px;
  height: 12px;
  background-color: #fff;
}
.carousel-caption {
  position: absolute;
  left: 15%;
  right: 15%;
  bottom: 20px;
  z-index: 10;
  padding-top: 20px;
  padding-bottom: 20px;
  color: #fff;
  text-align: center;
  text-shadow: 0 1px 2px rgba(0, 0, 0, 0.6);
}
.carousel-caption .btn {
  text-shadow: none;
}
@media screen and (min-width: 768px) {
  .carousel-control .glyphicon-chevron-left,
  .carousel-control .glyphicon-chevron-right,
  .carousel-control .icon-prev,
  .carousel-control .icon-next {
    width: 30px;
    height: 30px;
    margin-top: -10px;
    font-size: 30px;
  }
  .carousel-control .glyphicon-chevron-left,
  .carousel-control .icon-prev {
    margin-left: -10px;
  }
  .carousel-control .glyphicon-chevron-right,
  .carousel-control .icon-next {
    margin-right: -10px;
  }
  .carousel-caption {
    left: 20%;
    right: 20%;
    padding-bottom: 30px;
  }
  .carousel-indicators {
    bottom: 20px;
  }
}
.clearfix:before,
.clearfix:after,
.dl-horizontal dd:before,
.dl-horizontal dd:after,
.container:before,
.container:after,
.container-fluid:before,
.container-fluid:after,
.row:before,
.row:after,
.form-horizontal .form-group:before,
.form-horizontal .form-group:after,
.btn-toolbar:before,
.btn-toolbar:after,
.btn-group-vertical > .btn-group:before,
.btn-group-vertical > .btn-group:after,
.nav:before,
.nav:after,
.navbar:before,
.navbar:after,
.navbar-header:before,
.navbar-header:after,
.navbar-collapse:before,
.navbar-collapse:after,
.pager:before,
.pager:after,
.panel-body:before,
.panel-body:after,
.modal-header:before,
.modal-header:after,
.modal-footer:before,
.modal-footer:after,
.item_buttons:before,
.item_buttons:after {
  content: " ";
  display: table;
}
.clearfix:after,
.dl-horizontal dd:after,
.container:after,
.container-fluid:after,
.row:after,
.form-horizontal .form-group:after,
.btn-toolbar:after,
.btn-group-vertical > .btn-group:after,
.nav:after,
.navbar:after,
.navbar-header:after,
.navbar-collapse:after,
.pager:after,
.panel-body:after,
.modal-header:after,
.modal-footer:after,
.item_buttons:after {
  clear: both;
}
.center-block {
  display: block;
  margin-left: auto;
  margin-right: auto;
}
.pull-right {
  float: right !important;
}
.pull-left {
  float: left !important;
}
.hide {
  display: none !important;
}
.show {
  display: block !important;
}
.invisible {
  visibility: hidden;
}
.text-hide {
  font: 0/0 a;
  color: transparent;
  text-shadow: none;
  background-color: transparent;
  border: 0;
}
.hidden {
  display: none !important;
}
.affix {
  position: fixed;
}
@-ms-viewport {
  width: device-width;
}
.visible-xs,
.visible-sm,
.visible-md,
.visible-lg {
  display: none !important;
}
.visible-xs-block,
.visible-xs-inline,
.visible-xs-inline-block,
.visible-sm-block,
.visible-sm-inline,
.visible-sm-inline-block,
.visible-md-block,
.visible-md-inline,
.visible-md-inline-block,
.visible-lg-block,
.visible-lg-inline,
.visible-lg-inline-block {
  display: none !important;
}
@media (max-width: 767px) {
  .visible-xs {
    display: block !important;
  }
  table.visible-xs {
    display: table !important;
  }
  tr.visible-xs {
    display: table-row !important;
  }
  th.visible-xs,
  td.visible-xs {
    display: table-cell !important;
  }
}
@media (max-width: 767px) {
  .visible-xs-block {
    display: block !important;
  }
}
@media (max-width: 767px) {
  .visible-xs-inline {
    display: inline !important;
  }
}
@media (max-width: 767px) {
  .visible-xs-inline-block {
    display: inline-block !important;
  }
}
@media (min-width: 768px) and (max-width: 991px) {
  .visible-sm {
    display: block !important;
  }
  table.visible-sm {
    display: table !important;
  }
  tr.visible-sm {
    display: table-row !important;
  }
  th.visible-sm,
  td.visible-sm {
    display: table-cell !important;
  }
}
@media (min-width: 768px) and (max-width: 991px) {
  .visible-sm-block {
    display: block !important;
  }
}
@media (min-width: 768px) and (max-width: 991px) {
  .visible-sm-inline {
    display: inline !important;
  }
}
@media (min-width: 768px) and (max-width: 991px) {
  .visible-sm-inline-block {
    display: inline-block !important;
  }
}
@media (min-width: 992px) and (max-width: 1199px) {
  .visible-md {
    display: block !important;
  }
  table.visible-md {
    display: table !important;
  }
  tr.visible-md {
    display: table-row !important;
  }
  th.visible-md,
  td.visible-md {
    display: table-cell !important;
  }
}
@media (min-width: 992px) and (max-width: 1199px) {
  .visible-md-block {
    display: block !important;
  }
}
@media (min-width: 992px) and (max-width: 1199px) {
  .visible-md-inline {
    display: inline !important;
  }
}
@media (min-width: 992px) and (max-width: 1199px) {
  .visible-md-inline-block {
    display: inline-block !important;
  }
}
@media (min-width: 1200px) {
  .visible-lg {
    display: block !important;
  }
  table.visible-lg {
    display: table !important;
  }
  tr.visible-lg {
    display: table-row !important;
  }
  th.visible-lg,
  td.visible-lg {
    display: table-cell !important;
  }
}
@media (min-width: 1200px) {
  .visible-lg-block {
    display: block !important;
  }
}
@media (min-width: 1200px) {
  .visible-lg-inline {
    display: inline !important;
  }
}
@media (min-width: 1200px) {
  .visible-lg-inline-block {
    display: inline-block !important;
  }
}
@media (max-width: 767px) {
  .hidden-xs {
    display: none !important;
  }
}
@media (min-width: 768px) and (max-width: 991px) {
  .hidden-sm {
    display: none !important;
  }
}
@media (min-width: 992px) and (max-width: 1199px) {
  .hidden-md {
    display: none !important;
  }
}
@media (min-width: 1200px) {
  .hidden-lg {
    display: none !important;
  }
}
.visible-print {
  display: none !important;
}
@media print {
  .visible-print {
    display: block !important;
  }
  table.visible-print {
    display: table !important;
  }
  tr.visible-print {
    display: table-row !important;
  }
  th.visible-print,
  td.visible-print {
    display: table-cell !important;
  }
}
.visible-print-block {
  display: none !important;
}
@media print {
  .visible-print-block {
    display: block !important;
  }
}
.visible-print-inline {
  display: none !important;
}
@media print {
  .visible-print-inline {
    display: inline !important;
  }
}
.visible-print-inline-block {
  display: none !important;
}
@media print {
  .visible-print-inline-block {
    display: inline-block !important;
  }
}
@media print {
  .hidden-print {
    display: none !important;
  }
}
/*!
*
* Font Awesome
*
*/
/*!
 *  Font Awesome 4.7.0 by @davegandy - http://fontawesome.io - @fontawesome
 *  License - http://fontawesome.io/license (Font: SIL OFL 1.1, CSS: MIT License)
 */
/* FONT PATH
 * -------------------------- */
@font-face {
  font-family: 'FontAwesome';
  src: url('../components/font-awesome/fonts/fontawesome-webfont.eot?v=4.7.0');
  src: url('../components/font-awesome/fonts/fontawesome-webfont.eot?#iefix&v=4.7.0') format('embedded-opentype'), url('../components/font-awesome/fonts/fontawesome-webfont.woff2?v=4.7.0') format('woff2'), url('../components/font-awesome/fonts/fontawesome-webfont.woff?v=4.7.0') format('woff'), url('../components/font-awesome/fonts/fontawesome-webfont.ttf?v=4.7.0') format('truetype'), url('../components/font-awesome/fonts/fontawesome-webfont.svg?v=4.7.0#fontawesomeregular') format('svg');
  font-weight: normal;
  font-style: normal;
}
.fa {
  display: inline-block;
  font: normal normal normal 14px/1 FontAwesome;
  font-size: inherit;
  text-rendering: auto;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
}
/* makes the font 33% larger relative to the icon container */
.fa-lg {
  font-size: 1.33333333em;
  line-height: 0.75em;
  vertical-align: -15%;
}
.fa-2x {
  font-size: 2em;
}
.fa-3x {
  font-size: 3em;
}
.fa-4x {
  font-size: 4em;
}
.fa-5x {
  font-size: 5em;
}
.fa-fw {
  width: 1.28571429em;
  text-align: center;
}
.fa-ul {
  padding-left: 0;
  margin-left: 2.14285714em;
  list-style-type: none;
}
.fa-ul > li {
  position: relative;
}
.fa-li {
  position: absolute;
  left: -2.14285714em;
  width: 2.14285714em;
  top: 0.14285714em;
  text-align: center;
}
.fa-li.fa-lg {
  left: -1.85714286em;
}
.fa-border {
  padding: .2em .25em .15em;
  border: solid 0.08em #eee;
  border-radius: .1em;
}
.fa-pull-left {
  float: left;
}
.fa-pull-right {
  float: right;
}
.fa.fa-pull-left {
  margin-right: .3em;
}
.fa.fa-pull-right {
  margin-left: .3em;
}
/* Deprecated as of 4.4.0 */
.pull-right {
  float: right;
}
.pull-left {
  float: left;
}
.fa.pull-left {
  margin-right: .3em;
}
.fa.pull-right {
  margin-left: .3em;
}
.fa-spin {
  -webkit-animation: fa-spin 2s infinite linear;
  animation: fa-spin 2s infinite linear;
}
.fa-pulse {
  -webkit-animation: fa-spin 1s infinite steps(8);
  animation: fa-spin 1s infinite steps(8);
}
@-webkit-keyframes fa-spin {
  0% {
    -webkit-transform: rotate(0deg);
    transform: rotate(0deg);
  }
  100% {
    -webkit-transform: rotate(359deg);
    transform: rotate(359deg);
  }
}
@keyframes fa-spin {
  0% {
    -webkit-transform: rotate(0deg);
    transform: rotate(0deg);
  }
  100% {
    -webkit-transform: rotate(359deg);
    transform: rotate(359deg);
  }
}
.fa-rotate-90 {
  -ms-filter: "progid:DXImageTransform.Microsoft.BasicImage(rotation=1)";
  -webkit-transform: rotate(90deg);
  -ms-transform: rotate(90deg);
  transform: rotate(90deg);
}
.fa-rotate-180 {
  -ms-filter: "progid:DXImageTransform.Microsoft.BasicImage(rotation=2)";
  -webkit-transform: rotate(180deg);
  -ms-transform: rotate(180deg);
  transform: rotate(180deg);
}
.fa-rotate-270 {
  -ms-filter: "progid:DXImageTransform.Microsoft.BasicImage(rotation=3)";
  -webkit-transform: rotate(270deg);
  -ms-transform: rotate(270deg);
  transform: rotate(270deg);
}
.fa-flip-horizontal {
  -ms-filter: "progid:DXImageTransform.Microsoft.BasicImage(rotation=0, mirror=1)";
  -webkit-transform: scale(-1, 1);
  -ms-transform: scale(-1, 1);
  transform: scale(-1, 1);
}
.fa-flip-vertical {
  -ms-filter: "progid:DXImageTransform.Microsoft.BasicImage(rotation=2, mirror=1)";
  -webkit-transform: scale(1, -1);
  -ms-transform: scale(1, -1);
  transform: scale(1, -1);
}
:root .fa-rotate-90,
:root .fa-rotate-180,
:root .fa-rotate-270,
:root .fa-flip-horizontal,
:root .fa-flip-vertical {
  filter: none;
}
.fa-stack {
  position: relative;
  display: inline-block;
  width: 2em;
  height: 2em;
  line-height: 2em;
  vertical-align: middle;
}
.fa-stack-1x,
.fa-stack-2x {
  position: absolute;
  left: 0;
  width: 100%;
  text-align: center;
}
.fa-stack-1x {
  line-height: inherit;
}
.fa-stack-2x {
  font-size: 2em;
}
.fa-inverse {
  color: #fff;
}
/* Font Awesome uses the Unicode Private Use Area (PUA) to ensure screen
   readers do not read off random characters that represent icons */
.fa-glass:before {
  content: "\f000";
}
.fa-music:before {
  content: "\f001";
}
.fa-search:before {
  content: "\f002";
}
.fa-envelope-o:before {
  content: "\f003";
}
.fa-heart:before {
  content: "\f004";
}
.fa-star:before {
  content: "\f005";
}
.fa-star-o:before {
  content: "\f006";
}
.fa-user:before {
  content: "\f007";
}
.fa-film:before {
  content: "\f008";
}
.fa-th-large:before {
  content: "\f009";
}
.fa-th:before {
  content: "\f00a";
}
.fa-th-list:before {
  content: "\f00b";
}
.fa-check:before {
  content: "\f00c";
}
.fa-remove:before,
.fa-close:before,
.fa-times:before {
  content: "\f00d";
}
.fa-search-plus:before {
  content: "\f00e";
}
.fa-search-minus:before {
  content: "\f010";
}
.fa-power-off:before {
  content: "\f011";
}
.fa-signal:before {
  content: "\f012";
}
.fa-gear:before,
.fa-cog:before {
  content: "\f013";
}
.fa-trash-o:before {
  content: "\f014";
}
.fa-home:before {
  content: "\f015";
}
.fa-file-o:before {
  content: "\f016";
}
.fa-clock-o:before {
  content: "\f017";
}
.fa-road:before {
  content: "\f018";
}
.fa-download:before {
  content: "\f019";
}
.fa-arrow-circle-o-down:before {
  content: "\f01a";
}
.fa-arrow-circle-o-up:before {
  content: "\f01b";
}
.fa-inbox:before {
  content: "\f01c";
}
.fa-play-circle-o:before {
  content: "\f01d";
}
.fa-rotate-right:before,
.fa-repeat:before {
  content: "\f01e";
}
.fa-refresh:before {
  content: "\f021";
}
.fa-list-alt:before {
  content: "\f022";
}
.fa-lock:before {
  content: "\f023";
}
.fa-flag:before {
  content: "\f024";
}
.fa-headphones:before {
  content: "\f025";
}
.fa-volume-off:before {
  content: "\f026";
}
.fa-volume-down:before {
  content: "\f027";
}
.fa-volume-up:before {
  content: "\f028";
}
.fa-qrcode:before {
  content: "\f029";
}
.fa-barcode:before {
  content: "\f02a";
}
.fa-tag:before {
  content: "\f02b";
}
.fa-tags:before {
  content: "\f02c";
}
.fa-book:before {
  content: "\f02d";
}
.fa-bookmark:before {
  content: "\f02e";
}
.fa-print:before {
  content: "\f02f";
}
.fa-camera:before {
  content: "\f030";
}
.fa-font:before {
  content: "\f031";
}
.fa-bold:before {
  content: "\f032";
}
.fa-italic:before {
  content: "\f033";
}
.fa-text-height:before {
  content: "\f034";
}
.fa-text-width:before {
  content: "\f035";
}
.fa-align-left:before {
  content: "\f036";
}
.fa-align-center:before {
  content: "\f037";
}
.fa-align-right:before {
  content: "\f038";
}
.fa-align-justify:before {
  content: "\f039";
}
.fa-list:before {
  content: "\f03a";
}
.fa-dedent:before,
.fa-outdent:before {
  content: "\f03b";
}
.fa-indent:before {
  content: "\f03c";
}
.fa-video-camera:before {
  content: "\f03d";
}
.fa-photo:before,
.fa-image:before,
.fa-picture-o:before {
  content: "\f03e";
}
.fa-pencil:before {
  content: "\f040";
}
.fa-map-marker:before {
  content: "\f041";
}
.fa-adjust:before {
  content: "\f042";
}
.fa-tint:before {
  content: "\f043";
}
.fa-edit:before,
.fa-pencil-square-o:before {
  content: "\f044";
}
.fa-share-square-o:before {
  content: "\f045";
}
.fa-check-square-o:before {
  content: "\f046";
}
.fa-arrows:before {
  content: "\f047";
}
.fa-step-backward:before {
  content: "\f048";
}
.fa-fast-backward:before {
  content: "\f049";
}
.fa-backward:before {
  content: "\f04a";
}
.fa-play:before {
  content: "\f04b";
}
.fa-pause:before {
  content: "\f04c";
}
.fa-stop:before {
  content: "\f04d";
}
.fa-forward:before {
  content: "\f04e";
}
.fa-fast-forward:before {
  content: "\f050";
}
.fa-step-forward:before {
  content: "\f051";
}
.fa-eject:before {
  content: "\f052";
}
.fa-chevron-left:before {
  content: "\f053";
}
.fa-chevron-right:before {
  content: "\f054";
}
.fa-plus-circle:before {
  content: "\f055";
}
.fa-minus-circle:before {
  content: "\f056";
}
.fa-times-circle:before {
  content: "\f057";
}
.fa-check-circle:before {
  content: "\f058";
}
.fa-question-circle:before {
  content: "\f059";
}
.fa-info-circle:before {
  content: "\f05a";
}
.fa-crosshairs:before {
  content: "\f05b";
}
.fa-times-circle-o:before {
  content: "\f05c";
}
.fa-check-circle-o:before {
  content: "\f05d";
}
.fa-ban:before {
  content: "\f05e";
}
.fa-arrow-left:before {
  content: "\f060";
}
.fa-arrow-right:before {
  content: "\f061";
}
.fa-arrow-up:before {
  content: "\f062";
}
.fa-arrow-down:before {
  content: "\f063";
}
.fa-mail-forward:before,
.fa-share:before {
  content: "\f064";
}
.fa-expand:before {
  content: "\f065";
}
.fa-compress:before {
  content: "\f066";
}
.fa-plus:before {
  content: "\f067";
}
.fa-minus:before {
  content: "\f068";
}
.fa-asterisk:before {
  content: "\f069";
}
.fa-exclamation-circle:before {
  content: "\f06a";
}
.fa-gift:before {
  content: "\f06b";
}
.fa-leaf:before {
  content: "\f06c";
}
.fa-fire:before {
  content: "\f06d";
}
.fa-eye:before {
  content: "\f06e";
}
.fa-eye-slash:before {
  content: "\f070";
}
.fa-warning:before,
.fa-exclamation-triangle:before {
  content: "\f071";
}
.fa-plane:before {
  content: "\f072";
}
.fa-calendar:before {
  content: "\f073";
}
.fa-random:before {
  content: "\f074";
}
.fa-comment:before {
  content: "\f075";
}
.fa-magnet:before {
  content: "\f076";
}
.fa-chevron-up:before {
  content: "\f077";
}
.fa-chevron-down:before {
  content: "\f078";
}
.fa-retweet:before {
  content: "\f079";
}
.fa-shopping-cart:before {
  content: "\f07a";
}
.fa-folder:before {
  content: "\f07b";
}
.fa-folder-open:before {
  content: "\f07c";
}
.fa-arrows-v:before {
  content: "\f07d";
}
.fa-arrows-h:before {
  content: "\f07e";
}
.fa-bar-chart-o:before,
.fa-bar-chart:before {
  content: "\f080";
}
.fa-twitter-square:before {
  content: "\f081";
}
.fa-facebook-square:before {
  content: "\f082";
}
.fa-camera-retro:before {
  content: "\f083";
}
.fa-key:before {
  content: "\f084";
}
.fa-gears:before,
.fa-cogs:before {
  content: "\f085";
}
.fa-comments:before {
  content: "\f086";
}
.fa-thumbs-o-up:before {
  content: "\f087";
}
.fa-thumbs-o-down:before {
  content: "\f088";
}
.fa-star-half:before {
  content: "\f089";
}
.fa-heart-o:before {
  content: "\f08a";
}
.fa-sign-out:before {
  content: "\f08b";
}
.fa-linkedin-square:before {
  content: "\f08c";
}
.fa-thumb-tack:before {
  content: "\f08d";
}
.fa-external-link:before {
  content: "\f08e";
}
.fa-sign-in:before {
  content: "\f090";
}
.fa-trophy:before {
  content: "\f091";
}
.fa-github-square:before {
  content: "\f092";
}
.fa-upload:before {
  content: "\f093";
}
.fa-lemon-o:before {
  content: "\f094";
}
.fa-phone:before {
  content: "\f095";
}
.fa-square-o:before {
  content: "\f096";
}
.fa-bookmark-o:before {
  content: "\f097";
}
.fa-phone-square:before {
  content: "\f098";
}
.fa-twitter:before {
  content: "\f099";
}
.fa-facebook-f:before,
.fa-facebook:before {
  content: "\f09a";
}
.fa-github:before {
  content: "\f09b";
}
.fa-unlock:before {
  content: "\f09c";
}
.fa-credit-card:before {
  content: "\f09d";
}
.fa-feed:before,
.fa-rss:before {
  content: "\f09e";
}
.fa-hdd-o:before {
  content: "\f0a0";
}
.fa-bullhorn:before {
  content: "\f0a1";
}
.fa-bell:before {
  content: "\f0f3";
}
.fa-certificate:before {
  content: "\f0a3";
}
.fa-hand-o-right:before {
  content: "\f0a4";
}
.fa-hand-o-left:before {
  content: "\f0a5";
}
.fa-hand-o-up:before {
  content: "\f0a6";
}
.fa-hand-o-down:before {
  content: "\f0a7";
}
.fa-arrow-circle-left:before {
  content: "\f0a8";
}
.fa-arrow-circle-right:before {
  content: "\f0a9";
}
.fa-arrow-circle-up:before {
  content: "\f0aa";
}
.fa-arrow-circle-down:before {
  content: "\f0ab";
}
.fa-globe:before {
  content: "\f0ac";
}
.fa-wrench:before {
  content: "\f0ad";
}
.fa-tasks:before {
  content: "\f0ae";
}
.fa-filter:before {
  content: "\f0b0";
}
.fa-briefcase:before {
  content: "\f0b1";
}
.fa-arrows-alt:before {
  content: "\f0b2";
}
.fa-group:before,
.fa-users:before {
  content: "\f0c0";
}
.fa-chain:before,
.fa-link:before {
  content: "\f0c1";
}
.fa-cloud:before {
  content: "\f0c2";
}
.fa-flask:before {
  content: "\f0c3";
}
.fa-cut:before,
.fa-scissors:before {
  content: "\f0c4";
}
.fa-copy:before,
.fa-files-o:before {
  content: "\f0c5";
}
.fa-paperclip:before {
  content: "\f0c6";
}
.fa-save:before,
.fa-floppy-o:before {
  content: "\f0c7";
}
.fa-square:before {
  content: "\f0c8";
}
.fa-navicon:before,
.fa-reorder:before,
.fa-bars:before {
  content: "\f0c9";
}
.fa-list-ul:before {
  content: "\f0ca";
}
.fa-list-ol:before {
  content: "\f0cb";
}
.fa-strikethrough:before {
  content: "\f0cc";
}
.fa-underline:before {
  content: "\f0cd";
}
.fa-table:before {
  content: "\f0ce";
}
.fa-magic:before {
  content: "\f0d0";
}
.fa-truck:before {
  content: "\f0d1";
}
.fa-pinterest:before {
  content: "\f0d2";
}
.fa-pinterest-square:before {
  content: "\f0d3";
}
.fa-google-plus-square:before {
  content: "\f0d4";
}
.fa-google-plus:before {
  content: "\f0d5";
}
.fa-money:before {
  content: "\f0d6";
}
.fa-caret-down:before {
  content: "\f0d7";
}
.fa-caret-up:before {
  content: "\f0d8";
}
.fa-caret-left:before {
  content: "\f0d9";
}
.fa-caret-right:before {
  content: "\f0da";
}
.fa-columns:before {
  content: "\f0db";
}
.fa-unsorted:before,
.fa-sort:before {
  content: "\f0dc";
}
.fa-sort-down:before,
.fa-sort-desc:before {
  content: "\f0dd";
}
.fa-sort-up:before,
.fa-sort-asc:before {
  content: "\f0de";
}
.fa-envelope:before {
  content: "\f0e0";
}
.fa-linkedin:before {
  content: "\f0e1";
}
.fa-rotate-left:before,
.fa-undo:before {
  content: "\f0e2";
}
.fa-legal:before,
.fa-gavel:before {
  content: "\f0e3";
}
.fa-dashboard:before,
.fa-tachometer:before {
  content: "\f0e4";
}
.fa-comment-o:before {
  content: "\f0e5";
}
.fa-comments-o:before {
  content: "\f0e6";
}
.fa-flash:before,
.fa-bolt:before {
  content: "\f0e7";
}
.fa-sitemap:before {
  content: "\f0e8";
}
.fa-umbrella:before {
  content: "\f0e9";
}
.fa-paste:before,
.fa-clipboard:before {
  content: "\f0ea";
}
.fa-lightbulb-o:before {
  content: "\f0eb";
}
.fa-exchange:before {
  content: "\f0ec";
}
.fa-cloud-download:before {
  content: "\f0ed";
}
.fa-cloud-upload:before {
  content: "\f0ee";
}
.fa-user-md:before {
  content: "\f0f0";
}
.fa-stethoscope:before {
  content: "\f0f1";
}
.fa-suitcase:before {
  content: "\f0f2";
}
.fa-bell-o:before {
  content: "\f0a2";
}
.fa-coffee:before {
  content: "\f0f4";
}
.fa-cutlery:before {
  content: "\f0f5";
}
.fa-file-text-o:before {
  content: "\f0f6";
}
.fa-building-o:before {
  content: "\f0f7";
}
.fa-hospital-o:before {
  content: "\f0f8";
}
.fa-ambulance:before {
  content: "\f0f9";
}
.fa-medkit:before {
  content: "\f0fa";
}
.fa-fighter-jet:before {
  content: "\f0fb";
}
.fa-beer:before {
  content: "\f0fc";
}
.fa-h-square:before {
  content: "\f0fd";
}
.fa-plus-square:before {
  content: "\f0fe";
}
.fa-angle-double-left:before {
  content: "\f100";
}
.fa-angle-double-right:before {
  content: "\f101";
}
.fa-angle-double-up:before {
  content: "\f102";
}
.fa-angle-double-down:before {
  content: "\f103";
}
.fa-angle-left:before {
  content: "\f104";
}
.fa-angle-right:before {
  content: "\f105";
}
.fa-angle-up:before {
  content: "\f106";
}
.fa-angle-down:before {
  content: "\f107";
}
.fa-desktop:before {
  content: "\f108";
}
.fa-laptop:before {
  content: "\f109";
}
.fa-tablet:before {
  content: "\f10a";
}
.fa-mobile-phone:before,
.fa-mobile:before {
  content: "\f10b";
}
.fa-circle-o:before {
  content: "\f10c";
}
.fa-quote-left:before {
  content: "\f10d";
}
.fa-quote-right:before {
  content: "\f10e";
}
.fa-spinner:before {
  content: "\f110";
}
.fa-circle:before {
  content: "\f111";
}
.fa-mail-reply:before,
.fa-reply:before {
  content: "\f112";
}
.fa-github-alt:before {
  content: "\f113";
}
.fa-folder-o:before {
  content: "\f114";
}
.fa-folder-open-o:before {
  content: "\f115";
}
.fa-smile-o:before {
  content: "\f118";
}
.fa-frown-o:before {
  content: "\f119";
}
.fa-meh-o:before {
  content: "\f11a";
}
.fa-gamepad:before {
  content: "\f11b";
}
.fa-keyboard-o:before {
  content: "\f11c";
}
.fa-flag-o:before {
  content: "\f11d";
}
.fa-flag-checkered:before {
  content: "\f11e";
}
.fa-terminal:before {
  content: "\f120";
}
.fa-code:before {
  content: "\f121";
}
.fa-mail-reply-all:before,
.fa-reply-all:before {
  content: "\f122";
}
.fa-star-half-empty:before,
.fa-star-half-full:before,
.fa-star-half-o:before {
  content: "\f123";
}
.fa-location-arrow:before {
  content: "\f124";
}
.fa-crop:before {
  content: "\f125";
}
.fa-code-fork:before {
  content: "\f126";
}
.fa-unlink:before,
.fa-chain-broken:before {
  content: "\f127";
}
.fa-question:before {
  content: "\f128";
}
.fa-info:before {
  content: "\f129";
}
.fa-exclamation:before {
  content: "\f12a";
}
.fa-superscript:before {
  content: "\f12b";
}
.fa-subscript:before {
  content: "\f12c";
}
.fa-eraser:before {
  content: "\f12d";
}
.fa-puzzle-piece:before {
  content: "\f12e";
}
.fa-microphone:before {
  content: "\f130";
}
.fa-microphone-slash:before {
  content: "\f131";
}
.fa-shield:before {
  content: "\f132";
}
.fa-calendar-o:before {
  content: "\f133";
}
.fa-fire-extinguisher:before {
  content: "\f134";
}
.fa-rocket:before {
  content: "\f135";
}
.fa-maxcdn:before {
  content: "\f136";
}
.fa-chevron-circle-left:before {
  content: "\f137";
}
.fa-chevron-circle-right:before {
  content: "\f138";
}
.fa-chevron-circle-up:before {
  content: "\f139";
}
.fa-chevron-circle-down:before {
  content: "\f13a";
}
.fa-html5:before {
  content: "\f13b";
}
.fa-css3:before {
  content: "\f13c";
}
.fa-anchor:before {
  content: "\f13d";
}
.fa-unlock-alt:before {
  content: "\f13e";
}
.fa-bullseye:before {
  content: "\f140";
}
.fa-ellipsis-h:before {
  content: "\f141";
}
.fa-ellipsis-v:before {
  content: "\f142";
}
.fa-rss-square:before {
  content: "\f143";
}
.fa-play-circle:before {
  content: "\f144";
}
.fa-ticket:before {
  content: "\f145";
}
.fa-minus-square:before {
  content: "\f146";
}
.fa-minus-square-o:before {
  content: "\f147";
}
.fa-level-up:before {
  content: "\f148";
}
.fa-level-down:before {
  content: "\f149";
}
.fa-check-square:before {
  content: "\f14a";
}
.fa-pencil-square:before {
  content: "\f14b";
}
.fa-external-link-square:before {
  content: "\f14c";
}
.fa-share-square:before {
  content: "\f14d";
}
.fa-compass:before {
  content: "\f14e";
}
.fa-toggle-down:before,
.fa-caret-square-o-down:before {
  content: "\f150";
}
.fa-toggle-up:before,
.fa-caret-square-o-up:before {
  content: "\f151";
}
.fa-toggle-right:before,
.fa-caret-square-o-right:before {
  content: "\f152";
}
.fa-euro:before,
.fa-eur:before {
  content: "\f153";
}
.fa-gbp:before {
  content: "\f154";
}
.fa-dollar:before,
.fa-usd:before {
  content: "\f155";
}
.fa-rupee:before,
.fa-inr:before {
  content: "\f156";
}
.fa-cny:before,
.fa-rmb:before,
.fa-yen:before,
.fa-jpy:before {
  content: "\f157";
}
.fa-ruble:before,
.fa-rouble:before,
.fa-rub:before {
  content: "\f158";
}
.fa-won:before,
.fa-krw:before {
  content: "\f159";
}
.fa-bitcoin:before,
.fa-btc:before {
  content: "\f15a";
}
.fa-file:before {
  content: "\f15b";
}
.fa-file-text:before {
  content: "\f15c";
}
.fa-sort-alpha-asc:before {
  content: "\f15d";
}
.fa-sort-alpha-desc:before {
  content: "\f15e";
}
.fa-sort-amount-asc:before {
  content: "\f160";
}
.fa-sort-amount-desc:before {
  content: "\f161";
}
.fa-sort-numeric-asc:before {
  content: "\f162";
}
.fa-sort-numeric-desc:before {
  content: "\f163";
}
.fa-thumbs-up:before {
  content: "\f164";
}
.fa-thumbs-down:before {
  content: "\f165";
}
.fa-youtube-square:before {
  content: "\f166";
}
.fa-youtube:before {
  content: "\f167";
}
.fa-xing:before {
  content: "\f168";
}
.fa-xing-square:before {
  content: "\f169";
}
.fa-youtube-play:before {
  content: "\f16a";
}
.fa-dropbox:before {
  content: "\f16b";
}
.fa-stack-overflow:before {
  content: "\f16c";
}
.fa-instagram:before {
  content: "\f16d";
}
.fa-flickr:before {
  content: "\f16e";
}
.fa-adn:before {
  content: "\f170";
}
.fa-bitbucket:before {
  content: "\f171";
}
.fa-bitbucket-square:before {
  content: "\f172";
}
.fa-tumblr:before {
  content: "\f173";
}
.fa-tumblr-square:before {
  content: "\f174";
}
.fa-long-arrow-down:before {
  content: "\f175";
}
.fa-long-arrow-up:before {
  content: "\f176";
}
.fa-long-arrow-left:before {
  content: "\f177";
}
.fa-long-arrow-right:before {
  content: "\f178";
}
.fa-apple:before {
  content: "\f179";
}
.fa-windows:before {
  content: "\f17a";
}
.fa-android:before {
  content: "\f17b";
}
.fa-linux:before {
  content: "\f17c";
}
.fa-dribbble:before {
  content: "\f17d";
}
.fa-skype:before {
  content: "\f17e";
}
.fa-foursquare:before {
  content: "\f180";
}
.fa-trello:before {
  content: "\f181";
}
.fa-female:before {
  content: "\f182";
}
.fa-male:before {
  content: "\f183";
}
.fa-gittip:before,
.fa-gratipay:before {
  content: "\f184";
}
.fa-sun-o:before {
  content: "\f185";
}
.fa-moon-o:before {
  content: "\f186";
}
.fa-archive:before {
  content: "\f187";
}
.fa-bug:before {
  content: "\f188";
}
.fa-vk:before {
  content: "\f189";
}
.fa-weibo:before {
  content: "\f18a";
}
.fa-renren:before {
  content: "\f18b";
}
.fa-pagelines:before {
  content: "\f18c";
}
.fa-stack-exchange:before {
  content: "\f18d";
}
.fa-arrow-circle-o-right:before {
  content: "\f18e";
}
.fa-arrow-circle-o-left:before {
  content: "\f190";
}
.fa-toggle-left:before,
.fa-caret-square-o-left:before {
  content: "\f191";
}
.fa-dot-circle-o:before {
  content: "\f192";
}
.fa-wheelchair:before {
  content: "\f193";
}
.fa-vimeo-square:before {
  content: "\f194";
}
.fa-turkish-lira:before,
.fa-try:before {
  content: "\f195";
}
.fa-plus-square-o:before {
  content: "\f196";
}
.fa-space-shuttle:before {
  content: "\f197";
}
.fa-slack:before {
  content: "\f198";
}
.fa-envelope-square:before {
  content: "\f199";
}
.fa-wordpress:before {
  content: "\f19a";
}
.fa-openid:before {
  content: "\f19b";
}
.fa-institution:before,
.fa-bank:before,
.fa-university:before {
  content: "\f19c";
}
.fa-mortar-board:before,
.fa-graduation-cap:before {
  content: "\f19d";
}
.fa-yahoo:before {
  content: "\f19e";
}
.fa-google:before {
  content: "\f1a0";
}
.fa-reddit:before {
  content: "\f1a1";
}
.fa-reddit-square:before {
  content: "\f1a2";
}
.fa-stumbleupon-circle:before {
  content: "\f1a3";
}
.fa-stumbleupon:before {
  content: "\f1a4";
}
.fa-delicious:before {
  content: "\f1a5";
}
.fa-digg:before {
  content: "\f1a6";
}
.fa-pied-piper-pp:before {
  content: "\f1a7";
}
.fa-pied-piper-alt:before {
  content: "\f1a8";
}
.fa-drupal:before {
  content: "\f1a9";
}
.fa-joomla:before {
  content: "\f1aa";
}
.fa-language:before {
  content: "\f1ab";
}
.fa-fax:before {
  content: "\f1ac";
}
.fa-building:before {
  content: "\f1ad";
}
.fa-child:before {
  content: "\f1ae";
}
.fa-paw:before {
  content: "\f1b0";
}
.fa-spoon:before {
  content: "\f1b1";
}
.fa-cube:before {
  content: "\f1b2";
}
.fa-cubes:before {
  content: "\f1b3";
}
.fa-behance:before {
  content: "\f1b4";
}
.fa-behance-square:before {
  content: "\f1b5";
}
.fa-steam:before {
  content: "\f1b6";
}
.fa-steam-square:before {
  content: "\f1b7";
}
.fa-recycle:before {
  content: "\f1b8";
}
.fa-automobile:before,
.fa-car:before {
  content: "\f1b9";
}
.fa-cab:before,
.fa-taxi:before {
  content: "\f1ba";
}
.fa-tree:before {
  content: "\f1bb";
}
.fa-spotify:before {
  content: "\f1bc";
}
.fa-deviantart:before {
  content: "\f1bd";
}
.fa-soundcloud:before {
  content: "\f1be";
}
.fa-database:before {
  content: "\f1c0";
}
.fa-file-pdf-o:before {
  content: "\f1c1";
}
.fa-file-word-o:before {
  content: "\f1c2";
}
.fa-file-excel-o:before {
  content: "\f1c3";
}
.fa-file-powerpoint-o:before {
  content: "\f1c4";
}
.fa-file-photo-o:before,
.fa-file-picture-o:before,
.fa-file-image-o:before {
  content: "\f1c5";
}
.fa-file-zip-o:before,
.fa-file-archive-o:before {
  content: "\f1c6";
}
.fa-file-sound-o:before,
.fa-file-audio-o:before {
  content: "\f1c7";
}
.fa-file-movie-o:before,
.fa-file-video-o:before {
  content: "\f1c8";
}
.fa-file-code-o:before {
  content: "\f1c9";
}
.fa-vine:before {
  content: "\f1ca";
}
.fa-codepen:before {
  content: "\f1cb";
}
.fa-jsfiddle:before {
  content: "\f1cc";
}
.fa-life-bouy:before,
.fa-life-buoy:before,
.fa-life-saver:before,
.fa-support:before,
.fa-life-ring:before {
  content: "\f1cd";
}
.fa-circle-o-notch:before {
  content: "\f1ce";
}
.fa-ra:before,
.fa-resistance:before,
.fa-rebel:before {
  content: "\f1d0";
}
.fa-ge:before,
.fa-empire:before {
  content: "\f1d1";
}
.fa-git-square:before {
  content: "\f1d2";
}
.fa-git:before {
  content: "\f1d3";
}
.fa-y-combinator-square:before,
.fa-yc-square:before,
.fa-hacker-news:before {
  content: "\f1d4";
}
.fa-tencent-weibo:before {
  content: "\f1d5";
}
.fa-qq:before {
  content: "\f1d6";
}
.fa-wechat:before,
.fa-weixin:before {
  content: "\f1d7";
}
.fa-send:before,
.fa-paper-plane:before {
  content: "\f1d8";
}
.fa-send-o:before,
.fa-paper-plane-o:before {
  content: "\f1d9";
}
.fa-history:before {
  content: "\f1da";
}
.fa-circle-thin:before {
  content: "\f1db";
}
.fa-header:before {
  content: "\f1dc";
}
.fa-paragraph:before {
  content: "\f1dd";
}
.fa-sliders:before {
  content: "\f1de";
}
.fa-share-alt:before {
  content: "\f1e0";
}
.fa-share-alt-square:before {
  content: "\f1e1";
}
.fa-bomb:before {
  content: "\f1e2";
}
.fa-soccer-ball-o:before,
.fa-futbol-o:before {
  content: "\f1e3";
}
.fa-tty:before {
  content: "\f1e4";
}
.fa-binoculars:before {
  content: "\f1e5";
}
.fa-plug:before {
  content: "\f1e6";
}
.fa-slideshare:before {
  content: "\f1e7";
}
.fa-twitch:before {
  content: "\f1e8";
}
.fa-yelp:before {
  content: "\f1e9";
}
.fa-newspaper-o:before {
  content: "\f1ea";
}
.fa-wifi:before {
  content: "\f1eb";
}
.fa-calculator:before {
  content: "\f1ec";
}
.fa-paypal:before {
  content: "\f1ed";
}
.fa-google-wallet:before {
  content: "\f1ee";
}
.fa-cc-visa:before {
  content: "\f1f0";
}
.fa-cc-mastercard:before {
  content: "\f1f1";
}
.fa-cc-discover:before {
  content: "\f1f2";
}
.fa-cc-amex:before {
  content: "\f1f3";
}
.fa-cc-paypal:before {
  content: "\f1f4";
}
.fa-cc-stripe:before {
  content: "\f1f5";
}
.fa-bell-slash:before {
  content: "\f1f6";
}
.fa-bell-slash-o:before {
  content: "\f1f7";
}
.fa-trash:before {
  content: "\f1f8";
}
.fa-copyright:before {
  content: "\f1f9";
}
.fa-at:before {
  content: "\f1fa";
}
.fa-eyedropper:before {
  content: "\f1fb";
}
.fa-paint-brush:before {
  content: "\f1fc";
}
.fa-birthday-cake:before {
  content: "\f1fd";
}
.fa-area-chart:before {
  content: "\f1fe";
}
.fa-pie-chart:before {
  content: "\f200";
}
.fa-line-chart:before {
  content: "\f201";
}
.fa-lastfm:before {
  content: "\f202";
}
.fa-lastfm-square:before {
  content: "\f203";
}
.fa-toggle-off:before {
  content: "\f204";
}
.fa-toggle-on:before {
  content: "\f205";
}
.fa-bicycle:before {
  content: "\f206";
}
.fa-bus:before {
  content: "\f207";
}
.fa-ioxhost:before {
  content: "\f208";
}
.fa-angellist:before {
  content: "\f209";
}
.fa-cc:before {
  content: "\f20a";
}
.fa-shekel:before,
.fa-sheqel:before,
.fa-ils:before {
  content: "\f20b";
}
.fa-meanpath:before {
  content: "\f20c";
}
.fa-buysellads:before {
  content: "\f20d";
}
.fa-connectdevelop:before {
  content: "\f20e";
}
.fa-dashcube:before {
  content: "\f210";
}
.fa-forumbee:before {
  content: "\f211";
}
.fa-leanpub:before {
  content: "\f212";
}
.fa-sellsy:before {
  content: "\f213";
}
.fa-shirtsinbulk:before {
  content: "\f214";
}
.fa-simplybuilt:before {
  content: "\f215";
}
.fa-skyatlas:before {
  content: "\f216";
}
.fa-cart-plus:before {
  content: "\f217";
}
.fa-cart-arrow-down:before {
  content: "\f218";
}
.fa-diamond:before {
  content: "\f219";
}
.fa-ship:before {
  content: "\f21a";
}
.fa-user-secret:before {
  content: "\f21b";
}
.fa-motorcycle:before {
  content: "\f21c";
}
.fa-street-view:before {
  content: "\f21d";
}
.fa-heartbeat:before {
  content: "\f21e";
}
.fa-venus:before {
  content: "\f221";
}
.fa-mars:before {
  content: "\f222";
}
.fa-mercury:before {
  content: "\f223";
}
.fa-intersex:before,
.fa-transgender:before {
  content: "\f224";
}
.fa-transgender-alt:before {
  content: "\f225";
}
.fa-venus-double:before {
  content: "\f226";
}
.fa-mars-double:before {
  content: "\f227";
}
.fa-venus-mars:before {
  content: "\f228";
}
.fa-mars-stroke:before {
  content: "\f229";
}
.fa-mars-stroke-v:before {
  content: "\f22a";
}
.fa-mars-stroke-h:before {
  content: "\f22b";
}
.fa-neuter:before {
  content: "\f22c";
}
.fa-genderless:before {
  content: "\f22d";
}
.fa-facebook-official:before {
  content: "\f230";
}
.fa-pinterest-p:before {
  content: "\f231";
}
.fa-whatsapp:before {
  content: "\f232";
}
.fa-server:before {
  content: "\f233";
}
.fa-user-plus:before {
  content: "\f234";
}
.fa-user-times:before {
  content: "\f235";
}
.fa-hotel:before,
.fa-bed:before {
  content: "\f236";
}
.fa-viacoin:before {
  content: "\f237";
}
.fa-train:before {
  content: "\f238";
}
.fa-subway:before {
  content: "\f239";
}
.fa-medium:before {
  content: "\f23a";
}
.fa-yc:before,
.fa-y-combinator:before {
  content: "\f23b";
}
.fa-optin-monster:before {
  content: "\f23c";
}
.fa-opencart:before {
  content: "\f23d";
}
.fa-expeditedssl:before {
  content: "\f23e";
}
.fa-battery-4:before,
.fa-battery:before,
.fa-battery-full:before {
  content: "\f240";
}
.fa-battery-3:before,
.fa-battery-three-quarters:before {
  content: "\f241";
}
.fa-battery-2:before,
.fa-battery-half:before {
  content: "\f242";
}
.fa-battery-1:before,
.fa-battery-quarter:before {
  content: "\f243";
}
.fa-battery-0:before,
.fa-battery-empty:before {
  content: "\f244";
}
.fa-mouse-pointer:before {
  content: "\f245";
}
.fa-i-cursor:before {
  content: "\f246";
}
.fa-object-group:before {
  content: "\f247";
}
.fa-object-ungroup:before {
  content: "\f248";
}
.fa-sticky-note:before {
  content: "\f249";
}
.fa-sticky-note-o:before {
  content: "\f24a";
}
.fa-cc-jcb:before {
  content: "\f24b";
}
.fa-cc-diners-club:before {
  content: "\f24c";
}
.fa-clone:before {
  content: "\f24d";
}
.fa-balance-scale:before {
  content: "\f24e";
}
.fa-hourglass-o:before {
  content: "\f250";
}
.fa-hourglass-1:before,
.fa-hourglass-start:before {
  content: "\f251";
}
.fa-hourglass-2:before,
.fa-hourglass-half:before {
  content: "\f252";
}
.fa-hourglass-3:before,
.fa-hourglass-end:before {
  content: "\f253";
}
.fa-hourglass:before {
  content: "\f254";
}
.fa-hand-grab-o:before,
.fa-hand-rock-o:before {
  content: "\f255";
}
.fa-hand-stop-o:before,
.fa-hand-paper-o:before {
  content: "\f256";
}
.fa-hand-scissors-o:before {
  content: "\f257";
}
.fa-hand-lizard-o:before {
  content: "\f258";
}
.fa-hand-spock-o:before {
  content: "\f259";
}
.fa-hand-pointer-o:before {
  content: "\f25a";
}
.fa-hand-peace-o:before {
  content: "\f25b";
}
.fa-trademark:before {
  content: "\f25c";
}
.fa-registered:before {
  content: "\f25d";
}
.fa-creative-commons:before {
  content: "\f25e";
}
.fa-gg:before {
  content: "\f260";
}
.fa-gg-circle:before {
  content: "\f261";
}
.fa-tripadvisor:before {
  content: "\f262";
}
.fa-odnoklassniki:before {
  content: "\f263";
}
.fa-odnoklassniki-square:before {
  content: "\f264";
}
.fa-get-pocket:before {
  content: "\f265";
}
.fa-wikipedia-w:before {
  content: "\f266";
}
.fa-safari:before {
  content: "\f267";
}
.fa-chrome:before {
  content: "\f268";
}
.fa-firefox:before {
  content: "\f269";
}
.fa-opera:before {
  content: "\f26a";
}
.fa-internet-explorer:before {
  content: "\f26b";
}
.fa-tv:before,
.fa-television:before {
  content: "\f26c";
}
.fa-contao:before {
  content: "\f26d";
}
.fa-500px:before {
  content: "\f26e";
}
.fa-amazon:before {
  content: "\f270";
}
.fa-calendar-plus-o:before {
  content: "\f271";
}
.fa-calendar-minus-o:before {
  content: "\f272";
}
.fa-calendar-times-o:before {
  content: "\f273";
}
.fa-calendar-check-o:before {
  content: "\f274";
}
.fa-industry:before {
  content: "\f275";
}
.fa-map-pin:before {
  content: "\f276";
}
.fa-map-signs:before {
  content: "\f277";
}
.fa-map-o:before {
  content: "\f278";
}
.fa-map:before {
  content: "\f279";
}
.fa-commenting:before {
  content: "\f27a";
}
.fa-commenting-o:before {
  content: "\f27b";
}
.fa-houzz:before {
  content: "\f27c";
}
.fa-vimeo:before {
  content: "\f27d";
}
.fa-black-tie:before {
  content: "\f27e";
}
.fa-fonticons:before {
  content: "\f280";
}
.fa-reddit-alien:before {
  content: "\f281";
}
.fa-edge:before {
  content: "\f282";
}
.fa-credit-card-alt:before {
  content: "\f283";
}
.fa-codiepie:before {
  content: "\f284";
}
.fa-modx:before {
  content: "\f285";
}
.fa-fort-awesome:before {
  content: "\f286";
}
.fa-usb:before {
  content: "\f287";
}
.fa-product-hunt:before {
  content: "\f288";
}
.fa-mixcloud:before {
  content: "\f289";
}
.fa-scribd:before {
  content: "\f28a";
}
.fa-pause-circle:before {
  content: "\f28b";
}
.fa-pause-circle-o:before {
  content: "\f28c";
}
.fa-stop-circle:before {
  content: "\f28d";
}
.fa-stop-circle-o:before {
  content: "\f28e";
}
.fa-shopping-bag:before {
  content: "\f290";
}
.fa-shopping-basket:before {
  content: "\f291";
}
.fa-hashtag:before {
  content: "\f292";
}
.fa-bluetooth:before {
  content: "\f293";
}
.fa-bluetooth-b:before {
  content: "\f294";
}
.fa-percent:before {
  content: "\f295";
}
.fa-gitlab:before {
  content: "\f296";
}
.fa-wpbeginner:before {
  content: "\f297";
}
.fa-wpforms:before {
  content: "\f298";
}
.fa-envira:before {
  content: "\f299";
}
.fa-universal-access:before {
  content: "\f29a";
}
.fa-wheelchair-alt:before {
  content: "\f29b";
}
.fa-question-circle-o:before {
  content: "\f29c";
}
.fa-blind:before {
  content: "\f29d";
}
.fa-audio-description:before {
  content: "\f29e";
}
.fa-volume-control-phone:before {
  content: "\f2a0";
}
.fa-braille:before {
  content: "\f2a1";
}
.fa-assistive-listening-systems:before {
  content: "\f2a2";
}
.fa-asl-interpreting:before,
.fa-american-sign-language-interpreting:before {
  content: "\f2a3";
}
.fa-deafness:before,
.fa-hard-of-hearing:before,
.fa-deaf:before {
  content: "\f2a4";
}
.fa-glide:before {
  content: "\f2a5";
}
.fa-glide-g:before {
  content: "\f2a6";
}
.fa-signing:before,
.fa-sign-language:before {
  content: "\f2a7";
}
.fa-low-vision:before {
  content: "\f2a8";
}
.fa-viadeo:before {
  content: "\f2a9";
}
.fa-viadeo-square:before {
  content: "\f2aa";
}
.fa-snapchat:before {
  content: "\f2ab";
}
.fa-snapchat-ghost:before {
  content: "\f2ac";
}
.fa-snapchat-square:before {
  content: "\f2ad";
}
.fa-pied-piper:before {
  content: "\f2ae";
}
.fa-first-order:before {
  content: "\f2b0";
}
.fa-yoast:before {
  content: "\f2b1";
}
.fa-themeisle:before {
  content: "\f2b2";
}
.fa-google-plus-circle:before,
.fa-google-plus-official:before {
  content: "\f2b3";
}
.fa-fa:before,
.fa-font-awesome:before {
  content: "\f2b4";
}
.fa-handshake-o:before {
  content: "\f2b5";
}
.fa-envelope-open:before {
  content: "\f2b6";
}
.fa-envelope-open-o:before {
  content: "\f2b7";
}
.fa-linode:before {
  content: "\f2b8";
}
.fa-address-book:before {
  content: "\f2b9";
}
.fa-address-book-o:before {
  content: "\f2ba";
}
.fa-vcard:before,
.fa-address-card:before {
  content: "\f2bb";
}
.fa-vcard-o:before,
.fa-address-card-o:before {
  content: "\f2bc";
}
.fa-user-circle:before {
  content: "\f2bd";
}
.fa-user-circle-o:before {
  content: "\f2be";
}
.fa-user-o:before {
  content: "\f2c0";
}
.fa-id-badge:before {
  content: "\f2c1";
}
.fa-drivers-license:before,
.fa-id-card:before {
  content: "\f2c2";
}
.fa-drivers-license-o:before,
.fa-id-card-o:before {
  content: "\f2c3";
}
.fa-quora:before {
  content: "\f2c4";
}
.fa-free-code-camp:before {
  content: "\f2c5";
}
.fa-telegram:before {
  content: "\f2c6";
}
.fa-thermometer-4:before,
.fa-thermometer:before,
.fa-thermometer-full:before {
  content: "\f2c7";
}
.fa-thermometer-3:before,
.fa-thermometer-three-quarters:before {
  content: "\f2c8";
}
.fa-thermometer-2:before,
.fa-thermometer-half:before {
  content: "\f2c9";
}
.fa-thermometer-1:before,
.fa-thermometer-quarter:before {
  content: "\f2ca";
}
.fa-thermometer-0:before,
.fa-thermometer-empty:before {
  content: "\f2cb";
}
.fa-shower:before {
  content: "\f2cc";
}
.fa-bathtub:before,
.fa-s15:before,
.fa-bath:before {
  content: "\f2cd";
}
.fa-podcast:before {
  content: "\f2ce";
}
.fa-window-maximize:before {
  content: "\f2d0";
}
.fa-window-minimize:before {
  content: "\f2d1";
}
.fa-window-restore:before {
  content: "\f2d2";
}
.fa-times-rectangle:before,
.fa-window-close:before {
  content: "\f2d3";
}
.fa-times-rectangle-o:before,
.fa-window-close-o:before {
  content: "\f2d4";
}
.fa-bandcamp:before {
  content: "\f2d5";
}
.fa-grav:before {
  content: "\f2d6";
}
.fa-etsy:before {
  content: "\f2d7";
}
.fa-imdb:before {
  content: "\f2d8";
}
.fa-ravelry:before {
  content: "\f2d9";
}
.fa-eercast:before {
  content: "\f2da";
}
.fa-microchip:before {
  content: "\f2db";
}
.fa-snowflake-o:before {
  content: "\f2dc";
}
.fa-superpowers:before {
  content: "\f2dd";
}
.fa-wpexplorer:before {
  content: "\f2de";
}
.fa-meetup:before {
  content: "\f2e0";
}
.sr-only {
  position: absolute;
  width: 1px;
  height: 1px;
  padding: 0;
  margin: -1px;
  overflow: hidden;
  clip: rect(0, 0, 0, 0);
  border: 0;
}
.sr-only-focusable:active,
.sr-only-focusable:focus {
  position: static;
  width: auto;
  height: auto;
  margin: 0;
  overflow: visible;
  clip: auto;
}
.sr-only-focusable:active,
.sr-only-focusable:focus {
  position: static;
  width: auto;
  height: auto;
  margin: 0;
  overflow: visible;
  clip: auto;
}
/*!
*
* IPython base
*
*/
.modal.fade .modal-dialog {
  -webkit-transform: translate(0, 0);
  -ms-transform: translate(0, 0);
  -o-transform: translate(0, 0);
  transform: translate(0, 0);
}
code {
  color: #000;
}
pre {
  font-size: inherit;
  line-height: inherit;
}
label {
  font-weight: normal;
}
/* Make the page background atleast 100% the height of the view port */
/* Make the page itself atleast 70% the height of the view port */
.border-box-sizing {
  box-sizing: border-box;
  -moz-box-sizing: border-box;
  -webkit-box-sizing: border-box;
}
.corner-all {
  border-radius: 2px;
}
.no-padding {
  padding: 0px;
}
/* Flexible box model classes */
/* Taken from Alex Russell http://infrequently.org/2009/08/css-3-progress/ */
/* This file is a compatability layer.  It allows the usage of flexible box 
model layouts accross multiple browsers, including older browsers.  The newest,
universal implementation of the flexible box model is used when available (see
`Modern browsers` comments below).  Browsers that are known to implement this 
new spec completely include:

    Firefox 28.0+
    Chrome 29.0+
    Internet Explorer 11+ 
    Opera 17.0+

Browsers not listed, including Safari, are supported via the styling under the
`Old browsers` comments below.
*/
.hbox {
  /* Old browsers */
  display: -webkit-box;
  -webkit-box-orient: horizontal;
  -webkit-box-align: stretch;
  display: -moz-box;
  -moz-box-orient: horizontal;
  -moz-box-align: stretch;
  display: box;
  box-orient: horizontal;
  box-align: stretch;
  /* Modern browsers */
  display: flex;
  flex-direction: row;
  align-items: stretch;
}
.hbox > * {
  /* Old browsers */
  -webkit-box-flex: 0;
  -moz-box-flex: 0;
  box-flex: 0;
  /* Modern browsers */
  flex: none;
}
.vbox {
  /* Old browsers */
  display: -webkit-box;
  -webkit-box-orient: vertical;
  -webkit-box-align: stretch;
  display: -moz-box;
  -moz-box-orient: vertical;
  -moz-box-align: stretch;
  display: box;
  box-orient: vertical;
  box-align: stretch;
  /* Modern browsers */
  display: flex;
  flex-direction: column;
  align-items: stretch;
}
.vbox > * {
  /* Old browsers */
  -webkit-box-flex: 0;
  -moz-box-flex: 0;
  box-flex: 0;
  /* Modern browsers */
  flex: none;
}
.hbox.reverse,
.vbox.reverse,
.reverse {
  /* Old browsers */
  -webkit-box-direction: reverse;
  -moz-box-direction: reverse;
  box-direction: reverse;
  /* Modern browsers */
  flex-direction: row-reverse;
}
.hbox.box-flex0,
.vbox.box-flex0,
.box-flex0 {
  /* Old browsers */
  -webkit-box-flex: 0;
  -moz-box-flex: 0;
  box-flex: 0;
  /* Modern browsers */
  flex: none;
  width: auto;
}
.hbox.box-flex1,
.vbox.box-flex1,
.box-flex1 {
  /* Old browsers */
  -webkit-box-flex: 1;
  -moz-box-flex: 1;
  box-flex: 1;
  /* Modern browsers */
  flex: 1;
}
.hbox.box-flex,
.vbox.box-flex,
.box-flex {
  /* Old browsers */
  /* Old browsers */
  -webkit-box-flex: 1;
  -moz-box-flex: 1;
  box-flex: 1;
  /* Modern browsers */
  flex: 1;
}
.hbox.box-flex2,
.vbox.box-flex2,
.box-flex2 {
  /* Old browsers */
  -webkit-box-flex: 2;
  -moz-box-flex: 2;
  box-flex: 2;
  /* Modern browsers */
  flex: 2;
}
.box-group1 {
  /*  Deprecated */
  -webkit-box-flex-group: 1;
  -moz-box-flex-group: 1;
  box-flex-group: 1;
}
.box-group2 {
  /* Deprecated */
  -webkit-box-flex-group: 2;
  -moz-box-flex-group: 2;
  box-flex-group: 2;
}
.hbox.start,
.vbox.start,
.start {
  /* Old browsers */
  -webkit-box-pack: start;
  -moz-box-pack: start;
  box-pack: start;
  /* Modern browsers */
  justify-content: flex-start;
}
.hbox.end,
.vbox.end,
.end {
  /* Old browsers */
  -webkit-box-pack: end;
  -moz-box-pack: end;
  box-pack: end;
  /* Modern browsers */
  justify-content: flex-end;
}
.hbox.center,
.vbox.center,
.center {
  /* Old browsers */
  -webkit-box-pack: center;
  -moz-box-pack: center;
  box-pack: center;
  /* Modern browsers */
  justify-content: center;
}
.hbox.baseline,
.vbox.baseline,
.baseline {
  /* Old browsers */
  -webkit-box-pack: baseline;
  -moz-box-pack: baseline;
  box-pack: baseline;
  /* Modern browsers */
  justify-content: baseline;
}
.hbox.stretch,
.vbox.stretch,
.stretch {
  /* Old browsers */
  -webkit-box-pack: stretch;
  -moz-box-pack: stretch;
  box-pack: stretch;
  /* Modern browsers */
  justify-content: stretch;
}
.hbox.align-start,
.vbox.align-start,
.align-start {
  /* Old browsers */
  -webkit-box-align: start;
  -moz-box-align: start;
  box-align: start;
  /* Modern browsers */
  align-items: flex-start;
}
.hbox.align-end,
.vbox.align-end,
.align-end {
  /* Old browsers */
  -webkit-box-align: end;
  -moz-box-align: end;
  box-align: end;
  /* Modern browsers */
  align-items: flex-end;
}
.hbox.align-center,
.vbox.align-center,
.align-center {
  /* Old browsers */
  -webkit-box-align: center;
  -moz-box-align: center;
  box-align: center;
  /* Modern browsers */
  align-items: center;
}
.hbox.align-baseline,
.vbox.align-baseline,
.align-baseline {
  /* Old browsers */
  -webkit-box-align: baseline;
  -moz-box-align: baseline;
  box-align: baseline;
  /* Modern browsers */
  align-items: baseline;
}
.hbox.align-stretch,
.vbox.align-stretch,
.align-stretch {
  /* Old browsers */
  -webkit-box-align: stretch;
  -moz-box-align: stretch;
  box-align: stretch;
  /* Modern browsers */
  align-items: stretch;
}
div.error {
  margin: 2em;
  text-align: center;
}
div.error > h1 {
  font-size: 500%;
  line-height: normal;
}
div.error > p {
  font-size: 200%;
  line-height: normal;
}
div.traceback-wrapper {
  text-align: left;
  max-width: 800px;
  margin: auto;
}
div.traceback-wrapper pre.traceback {
  max-height: 600px;
  overflow: auto;
}
/**
 * Primary styles
 *
 * Author: Jupyter Development Team
 */
body {
  background-color: #fff;
  /* This makes sure that the body covers the entire window and needs to
       be in a different element than the display: box in wrapper below */
  position: absolute;
  left: 0px;
  right: 0px;
  top: 0px;
  bottom: 0px;
  overflow: visible;
}
body > #header {
  /* Initially hidden to prevent FLOUC */
  display: none;
  background-color: #fff;
  /* Display over codemirror */
  position: relative;
  z-index: 100;
}
body > #header #header-container {
  display: flex;
  flex-direction: row;
  justify-content: space-between;
  padding: 5px;
  padding-bottom: 5px;
  padding-top: 5px;
  box-sizing: border-box;
  -moz-box-sizing: border-box;
  -webkit-box-sizing: border-box;
}
body > #header .header-bar {
  width: 100%;
  height: 1px;
  background: #e7e7e7;
  margin-bottom: -1px;
}
@media print {
  body > #header {
    display: none !important;
  }
}
#header-spacer {
  width: 100%;
  visibility: hidden;
}
@media print {
  #header-spacer {
    display: none;
  }
}
#ipython_notebook {
  padding-left: 0px;
  padding-top: 1px;
  padding-bottom: 1px;
}
[dir="rtl"] #ipython_notebook {
  margin-right: 10px;
  margin-left: 0;
}
[dir="rtl"] #ipython_notebook.pull-left {
  float: right !important;
  float: right;
}
.flex-spacer {
  flex: 1;
}
#noscript {
  width: auto;
  padding-top: 16px;
  padding-bottom: 16px;
  text-align: center;
  font-size: 22px;
  color: red;
  font-weight: bold;
}
#ipython_notebook img {
  height: 28px;
}
#site {
  width: 100%;
  display: none;
  box-sizing: border-box;
  -moz-box-sizing: border-box;
  -webkit-box-sizing: border-box;
  overflow: auto;
}
@media print {
  #site {
    height: auto !important;
  }
}
/* Smaller buttons */
.ui-button .ui-button-text {
  padding: 0.2em 0.8em;
  font-size: 77%;
}
input.ui-button {
  padding: 0.3em 0.9em;
}
span#kernel_logo_widget {
  margin: 0 10px;
}
span#login_widget {
  float: right;
}
[dir="rtl"] span#login_widget {
  float: left;
}
span#login_widget > .button,
#logout {
  color: #333;
  background-color: #fff;
  border-color: #ccc;
}
span#login_widget > .button:focus,
#logout:focus,
span#login_widget > .button.focus,
#logout.focus {
  color: #333;
  background-color: #e6e6e6;
  border-color: #8c8c8c;
}
span#login_widget > .button:hover,
#logout:hover {
  color: #333;
  background-color: #e6e6e6;
  border-color: #adadad;
}
span#login_widget > .button:active,
#logout:active,
span#login_widget > .button.active,
#logout.active,
.open > .dropdown-togglespan#login_widget > .button,
.open > .dropdown-toggle#logout {
  color: #333;
  background-color: #e6e6e6;
  border-color: #adadad;
}
span#login_widget > .button:active:hover,
#logout:active:hover,
span#login_widget > .button.active:hover,
#logout.active:hover,
.open > .dropdown-togglespan#login_widget > .button:hover,
.open > .dropdown-toggle#logout:hover,
span#login_widget > .button:active:focus,
#logout:active:focus,
span#login_widget > .button.active:focus,
#logout.active:focus,
.open > .dropdown-togglespan#login_widget > .button:focus,
.open > .dropdown-toggle#logout:focus,
span#login_widget > .button:active.focus,
#logout:active.focus,
span#login_widget > .button.active.focus,
#logout.active.focus,
.open > .dropdown-togglespan#login_widget > .button.focus,
.open > .dropdown-toggle#logout.focus {
  color: #333;
  background-color: #d4d4d4;
  border-color: #8c8c8c;
}
span#login_widget > .button:active,
#logout:active,
span#login_widget > .button.active,
#logout.active,
.open > .dropdown-togglespan#login_widget > .button,
.open > .dropdown-toggle#logout {
  background-image: none;
}
span#login_widget > .button.disabled:hover,
#logout.disabled:hover,
span#login_widget > .button[disabled]:hover,
#logout[disabled]:hover,
fieldset[disabled] span#login_widget > .button:hover,
fieldset[disabled] #logout:hover,
span#login_widget > .button.disabled:focus,
#logout.disabled:focus,
span#login_widget > .button[disabled]:focus,
#logout[disabled]:focus,
fieldset[disabled] span#login_widget > .button:focus,
fieldset[disabled] #logout:focus,
span#login_widget > .button.disabled.focus,
#logout.disabled.focus,
span#login_widget > .button[disabled].focus,
#logout[disabled].focus,
fieldset[disabled] span#login_widget > .button.focus,
fieldset[disabled] #logout.focus {
  background-color: #fff;
  border-color: #ccc;
}
span#login_widget > .button .badge,
#logout .badge {
  color: #fff;
  background-color: #333;
}
.nav-header {
  text-transform: none;
}
#header > span {
  margin-top: 10px;
}
.modal_stretch .modal-dialog {
  /* Old browsers */
  display: -webkit-box;
  -webkit-box-orient: vertical;
  -webkit-box-align: stretch;
  display: -moz-box;
  -moz-box-orient: vertical;
  -moz-box-align: stretch;
  display: box;
  box-orient: vertical;
  box-align: stretch;
  /* Modern browsers */
  display: flex;
  flex-direction: column;
  align-items: stretch;
  min-height: 80vh;
}
.modal_stretch .modal-dialog .modal-body {
  max-height: calc(100vh - 200px);
  overflow: auto;
  flex: 1;
}
.modal-header {
  cursor: move;
}
@media (min-width: 768px) {
  .modal .modal-dialog {
    width: 700px;
  }
}
@media (min-width: 768px) {
  select.form-control {
    margin-left: 12px;
    margin-right: 12px;
  }
}
/*!
*
* IPython auth
*
*/
.center-nav {
  display: inline-block;
  margin-bottom: -4px;
}
[dir="rtl"] .center-nav form.pull-left {
  float: right !important;
  float: right;
}
[dir="rtl"] .center-nav .navbar-text {
  float: right;
}
[dir="rtl"] .navbar-inner {
  text-align: right;
}
[dir="rtl"] div.text-left {
  text-align: right;
}
/*!
*
* IPython tree view
*
*/
/* We need an invisible input field on top of the sentense*/
/* "Drag file onto the list ..." */
.alternate_upload {
  background-color: none;
  display: inline;
}
.alternate_upload.form {
  padding: 0;
  margin: 0;
}
.alternate_upload input.fileinput {
  position: absolute;
  display: block;
  width: 100%;
  height: 100%;
  overflow: hidden;
  cursor: pointer;
  opacity: 0;
  z-index: 2;
}
.alternate_upload .btn-xs > input.fileinput {
  margin: -1px -5px;
}
.alternate_upload .btn-upload {
  position: relative;
  height: 22px;
}
::-webkit-file-upload-button {
  cursor: pointer;
}
/**
 * Primary styles
 *
 * Author: Jupyter Development Team
 */
ul#tabs {
  margin-bottom: 4px;
}
ul#tabs a {
  padding-top: 6px;
  padding-bottom: 4px;
}
[dir="rtl"] ul#tabs.nav-tabs > li {
  float: right;
}
[dir="rtl"] ul#tabs.nav.nav-tabs {
  padding-right: 0;
}
ul.breadcrumb a:focus,
ul.breadcrumb a:hover {
  text-decoration: none;
}
ul.breadcrumb i.icon-home {
  font-size: 16px;
  margin-right: 4px;
}
ul.breadcrumb span {
  color: #5e5e5e;
}
.list_toolbar {
  padding: 4px 0 4px 0;
  vertical-align: middle;
}
.list_toolbar .tree-buttons {
  padding-top: 1px;
}
[dir="rtl"] .list_toolbar .tree-buttons .pull-right {
  float: left !important;
  float: left;
}
[dir="rtl"] .list_toolbar .col-sm-4,
[dir="rtl"] .list_toolbar .col-sm-8 {
  float: right;
}
.dynamic-buttons {
  padding-top: 3px;
  display: inline-block;
}
.list_toolbar [class*="span"] {
  min-height: 24px;
}
.list_header {
  font-weight: bold;
  background-color: #EEE;
}
.list_placeholder {
  font-weight: bold;
  padding-top: 4px;
  padding-bottom: 4px;
  padding-left: 7px;
  padding-right: 7px;
}
.list_container {
  margin-top: 4px;
  margin-bottom: 20px;
  border: 1px solid #ddd;
  border-radius: 2px;
}
.list_container > div {
  border-bottom: 1px solid #ddd;
}
.list_container > div:hover .list-item {
  background-color: red;
}
.list_container > div:last-child {
  border: none;
}
.list_item:hover .list_item {
  background-color: #ddd;
}
.list_item a {
  text-decoration: none;
}
.list_item:hover {
  background-color: #fafafa;
}
.list_header > div,
.list_item > div {
  padding-top: 4px;
  padding-bottom: 4px;
  padding-left: 7px;
  padding-right: 7px;
  line-height: 22px;
}
.list_header > div input,
.list_item > div input {
  margin-right: 7px;
  margin-left: 14px;
  vertical-align: text-bottom;
  line-height: 22px;
  position: relative;
  top: -1px;
}
.list_header > div .item_link,
.list_item > div .item_link {
  margin-left: -1px;
  vertical-align: baseline;
  line-height: 22px;
}
[dir="rtl"] .list_item > div input {
  margin-right: 0;
}
.new-file input[type=checkbox] {
  visibility: hidden;
}
.item_name {
  line-height: 22px;
  height: 24px;
}
.item_icon {
  font-size: 14px;
  color: #5e5e5e;
  margin-right: 7px;
  margin-left: 7px;
  line-height: 22px;
  vertical-align: baseline;
}
.item_modified {
  margin-right: 7px;
  margin-left: 7px;
}
[dir="rtl"] .item_modified.pull-right {
  float: left !important;
  float: left;
}
.item_buttons {
  line-height: 1em;
  margin-left: -5px;
}
.item_buttons .btn,
.item_buttons .btn-group,
.item_buttons .input-group {
  float: left;
}
.item_buttons > .btn,
.item_buttons > .btn-group,
.item_buttons > .input-group {
  margin-left: 5px;
}
.item_buttons .btn {
  min-width: 13ex;
}
.item_buttons .running-indicator {
  padding-top: 4px;
  color: #5cb85c;
}
.item_buttons .kernel-name {
  padding-top: 4px;
  color: #5bc0de;
  margin-right: 7px;
  float: left;
}
[dir="rtl"] .item_buttons.pull-right {
  float: left !important;
  float: left;
}
[dir="rtl"] .item_buttons .kernel-name {
  margin-left: 7px;
  float: right;
}
.toolbar_info {
  height: 24px;
  line-height: 24px;
}
.list_item input:not([type=checkbox]) {
  padding-top: 3px;
  padding-bottom: 3px;
  height: 22px;
  line-height: 14px;
  margin: 0px;
}
.highlight_text {
  color: blue;
}
#project_name {
  display: inline-block;
  padding-left: 7px;
  margin-left: -2px;
}
#project_name > .breadcrumb {
  padding: 0px;
  margin-bottom: 0px;
  background-color: transparent;
  font-weight: bold;
}
.sort_button {
  display: inline-block;
  padding-left: 7px;
}
[dir="rtl"] .sort_button.pull-right {
  float: left !important;
  float: left;
}
#tree-selector {
  padding-right: 0px;
}
#button-select-all {
  min-width: 50px;
}
[dir="rtl"] #button-select-all.btn {
  float: right ;
}
#select-all {
  margin-left: 7px;
  margin-right: 2px;
  margin-top: 2px;
  height: 16px;
}
[dir="rtl"] #select-all.pull-left {
  float: right !important;
  float: right;
}
.menu_icon {
  margin-right: 2px;
}
.tab-content .row {
  margin-left: 0px;
  margin-right: 0px;
}
.folder_icon:before {
  display: inline-block;
  font: normal normal normal 14px/1 FontAwesome;
  font-size: inherit;
  text-rendering: auto;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  content: "\f114";
}
.folder_icon:before.fa-pull-left {
  margin-right: .3em;
}
.folder_icon:before.fa-pull-right {
  margin-left: .3em;
}
.folder_icon:before.pull-left {
  margin-right: .3em;
}
.folder_icon:before.pull-right {
  margin-left: .3em;
}
.notebook_icon:before {
  display: inline-block;
  font: normal normal normal 14px/1 FontAwesome;
  font-size: inherit;
  text-rendering: auto;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  content: "\f02d";
  position: relative;
  top: -1px;
}
.notebook_icon:before.fa-pull-left {
  margin-right: .3em;
}
.notebook_icon:before.fa-pull-right {
  margin-left: .3em;
}
.notebook_icon:before.pull-left {
  margin-right: .3em;
}
.notebook_icon:before.pull-right {
  margin-left: .3em;
}
.running_notebook_icon:before {
  display: inline-block;
  font: normal normal normal 14px/1 FontAwesome;
  font-size: inherit;
  text-rendering: auto;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  content: "\f02d";
  position: relative;
  top: -1px;
  color: #5cb85c;
}
.running_notebook_icon:before.fa-pull-left {
  margin-right: .3em;
}
.running_notebook_icon:before.fa-pull-right {
  margin-left: .3em;
}
.running_notebook_icon:before.pull-left {
  margin-right: .3em;
}
.running_notebook_icon:before.pull-right {
  margin-left: .3em;
}
.file_icon:before {
  display: inline-block;
  font: normal normal normal 14px/1 FontAwesome;
  font-size: inherit;
  text-rendering: auto;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  content: "\f016";
  position: relative;
  top: -2px;
}
.file_icon:before.fa-pull-left {
  margin-right: .3em;
}
.file_icon:before.fa-pull-right {
  margin-left: .3em;
}
.file_icon:before.pull-left {
  margin-right: .3em;
}
.file_icon:before.pull-right {
  margin-left: .3em;
}
#notebook_toolbar .pull-right {
  padding-top: 0px;
  margin-right: -1px;
}
ul#new-menu {
  left: auto;
  right: 0;
}
#new-menu .dropdown-header {
  font-size: 10px;
  border-bottom: 1px solid #e5e5e5;
  padding: 0 0 3px;
  margin: -3px 20px 0;
}
.kernel-menu-icon {
  padding-right: 12px;
  width: 24px;
  content: "\f096";
}
.kernel-menu-icon:before {
  content: "\f096";
}
.kernel-menu-icon-current:before {
  content: "\f00c";
}
#tab_content {
  padding-top: 20px;
}
#running .panel-group .panel {
  margin-top: 3px;
  margin-bottom: 1em;
}
#running .panel-group .panel .panel-heading {
  background-color: #EEE;
  padding-top: 4px;
  padding-bottom: 4px;
  padding-left: 7px;
  padding-right: 7px;
  line-height: 22px;
}
#running .panel-group .panel .panel-heading a:focus,
#running .panel-group .panel .panel-heading a:hover {
  text-decoration: none;
}
#running .panel-group .panel .panel-body {
  padding: 0px;
}
#running .panel-group .panel .panel-body .list_container {
  margin-top: 0px;
  margin-bottom: 0px;
  border: 0px;
  border-radius: 0px;
}
#running .panel-group .panel .panel-body .list_container .list_item {
  border-bottom: 1px solid #ddd;
}
#running .panel-group .panel .panel-body .list_container .list_item:last-child {
  border-bottom: 0px;
}
.delete-button {
  display: none;
}
.duplicate-button {
  display: none;
}
.rename-button {
  display: none;
}
.move-button {
  display: none;
}
.download-button {
  display: none;
}
.shutdown-button {
  display: none;
}
.dynamic-instructions {
  display: inline-block;
  padding-top: 4px;
}
/*!
*
* IPython text editor webapp
*
*/
.selected-keymap i.fa {
  padding: 0px 5px;
}
.selected-keymap i.fa:before {
  content: "\f00c";
}
#mode-menu {
  overflow: auto;
  max-height: 20em;
}
.edit_app #header {
  -webkit-box-shadow: 0px 0px 12px 1px rgba(87, 87, 87, 0.2);
  box-shadow: 0px 0px 12px 1px rgba(87, 87, 87, 0.2);
}
.edit_app #menubar .navbar {
  /* Use a negative 1 bottom margin, so the border overlaps the border of the
    header */
  margin-bottom: -1px;
}
.dirty-indicator {
  display: inline-block;
  font: normal normal normal 14px/1 FontAwesome;
  font-size: inherit;
  text-rendering: auto;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  width: 20px;
}
.dirty-indicator.fa-pull-left {
  margin-right: .3em;
}
.dirty-indicator.fa-pull-right {
  margin-left: .3em;
}
.dirty-indicator.pull-left {
  margin-right: .3em;
}
.dirty-indicator.pull-right {
  margin-left: .3em;
}
.dirty-indicator-dirty {
  display: inline-block;
  font: normal normal normal 14px/1 FontAwesome;
  font-size: inherit;
  text-rendering: auto;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  width: 20px;
}
.dirty-indicator-dirty.fa-pull-left {
  margin-right: .3em;
}
.dirty-indicator-dirty.fa-pull-right {
  margin-left: .3em;
}
.dirty-indicator-dirty.pull-left {
  margin-right: .3em;
}
.dirty-indicator-dirty.pull-right {
  margin-left: .3em;
}
.dirty-indicator-clean {
  display: inline-block;
  font: normal normal normal 14px/1 FontAwesome;
  font-size: inherit;
  text-rendering: auto;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  width: 20px;
}
.dirty-indicator-clean.fa-pull-left {
  margin-right: .3em;
}
.dirty-indicator-clean.fa-pull-right {
  margin-left: .3em;
}
.dirty-indicator-clean.pull-left {
  margin-right: .3em;
}
.dirty-indicator-clean.pull-right {
  margin-left: .3em;
}
.dirty-indicator-clean:before {
  display: inline-block;
  font: normal normal normal 14px/1 FontAwesome;
  font-size: inherit;
  text-rendering: auto;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  content: "\f00c";
}
.dirty-indicator-clean:before.fa-pull-left {
  margin-right: .3em;
}
.dirty-indicator-clean:before.fa-pull-right {
  margin-left: .3em;
}
.dirty-indicator-clean:before.pull-left {
  margin-right: .3em;
}
.dirty-indicator-clean:before.pull-right {
  margin-left: .3em;
}
#filename {
  font-size: 16pt;
  display: table;
  padding: 0px 5px;
}
#current-mode {
  padding-left: 5px;
  padding-right: 5px;
}
#texteditor-backdrop {
  padding-top: 20px;
  padding-bottom: 20px;
}
@media not print {
  #texteditor-backdrop {
    background-color: #EEE;
  }
}
@media print {
  #texteditor-backdrop #texteditor-container .CodeMirror-gutter,
  #texteditor-backdrop #texteditor-container .CodeMirror-gutters {
    background-color: #fff;
  }
}
@media not print {
  #texteditor-backdrop #texteditor-container .CodeMirror-gutter,
  #texteditor-backdrop #texteditor-container .CodeMirror-gutters {
    background-color: #fff;
  }
}
@media not print {
  #texteditor-backdrop #texteditor-container {
    padding: 0px;
    background-color: #fff;
    -webkit-box-shadow: 0px 0px 12px 1px rgba(87, 87, 87, 0.2);
    box-shadow: 0px 0px 12px 1px rgba(87, 87, 87, 0.2);
  }
}
.CodeMirror-dialog {
  background-color: #fff;
}
/*!
*
* IPython notebook
*
*/
/* CSS font colors for translated ANSI escape sequences */
/* The color values are a mix of
   http://www.xcolors.net/dl/baskerville-ivorylight and
   http://www.xcolors.net/dl/euphrasia */
.ansi-black-fg {
  color: #3E424D;
}
.ansi-black-bg {
  background-color: #3E424D;
}
.ansi-black-intense-fg {
  color: #282C36;
}
.ansi-black-intense-bg {
  background-color: #282C36;
}
.ansi-red-fg {
  color: #E75C58;
}
.ansi-red-bg {
  background-color: #E75C58;
}
.ansi-red-intense-fg {
  color: #B22B31;
}
.ansi-red-intense-bg {
  background-color: #B22B31;
}
.ansi-green-fg {
  color: #00A250;
}
.ansi-green-bg {
  background-color: #00A250;
}
.ansi-green-intense-fg {
  color: #007427;
}
.ansi-green-intense-bg {
  background-color: #007427;
}
.ansi-yellow-fg {
  color: #DDB62B;
}
.ansi-yellow-bg {
  background-color: #DDB62B;
}
.ansi-yellow-intense-fg {
  color: #B27D12;
}
.ansi-yellow-intense-bg {
  background-color: #B27D12;
}
.ansi-blue-fg {
  color: #208FFB;
}
.ansi-blue-bg {
  background-color: #208FFB;
}
.ansi-blue-intense-fg {
  color: #0065CA;
}
.ansi-blue-intense-bg {
  background-color: #0065CA;
}
.ansi-magenta-fg {
  color: #D160C4;
}
.ansi-magenta-bg {
  background-color: #D160C4;
}
.ansi-magenta-intense-fg {
  color: #A03196;
}
.ansi-magenta-intense-bg {
  background-color: #A03196;
}
.ansi-cyan-fg {
  color: #60C6C8;
}
.ansi-cyan-bg {
  background-color: #60C6C8;
}
.ansi-cyan-intense-fg {
  color: #258F8F;
}
.ansi-cyan-intense-bg {
  background-color: #258F8F;
}
.ansi-white-fg {
  color: #C5C1B4;
}
.ansi-white-bg {
  background-color: #C5C1B4;
}
.ansi-white-intense-fg {
  color: #A1A6B2;
}
.ansi-white-intense-bg {
  background-color: #A1A6B2;
}
.ansi-default-inverse-fg {
  color: #FFFFFF;
}
.ansi-default-inverse-bg {
  background-color: #000000;
}
.ansi-bold {
  font-weight: bold;
}
.ansi-underline {
  text-decoration: underline;
}
/* The following styles are deprecated an will be removed in a future version */
.ansibold {
  font-weight: bold;
}
.ansi-inverse {
  outline: 0.5px dotted;
}
/* use dark versions for foreground, to improve visibility */
.ansiblack {
  color: black;
}
.ansired {
  color: darkred;
}
.ansigreen {
  color: darkgreen;
}
.ansiyellow {
  color: #c4a000;
}
.ansiblue {
  color: darkblue;
}
.ansipurple {
  color: darkviolet;
}
.ansicyan {
  color: steelblue;
}
.ansigray {
  color: gray;
}
/* and light for background, for the same reason */
.ansibgblack {
  background-color: black;
}
.ansibgred {
  background-color: red;
}
.ansibggreen {
  background-color: green;
}
.ansibgyellow {
  background-color: yellow;
}
.ansibgblue {
  background-color: blue;
}
.ansibgpurple {
  background-color: magenta;
}
.ansibgcyan {
  background-color: cyan;
}
.ansibggray {
  background-color: gray;
}
div.cell {
  /* Old browsers */
  display: -webkit-box;
  -webkit-box-orient: vertical;
  -webkit-box-align: stretch;
  display: -moz-box;
  -moz-box-orient: vertical;
  -moz-box-align: stretch;
  display: box;
  box-orient: vertical;
  box-align: stretch;
  /* Modern browsers */
  display: flex;
  flex-direction: column;
  align-items: stretch;
  border-radius: 2px;
  box-sizing: border-box;
  -moz-box-sizing: border-box;
  -webkit-box-sizing: border-box;
  border-width: 1px;
  border-style: solid;
  border-color: transparent;
  width: 100%;
  padding: 5px;
  /* This acts as a spacer between cells, that is outside the border */
  margin: 0px;
  outline: none;
  position: relative;
  overflow: visible;
}
div.cell:before {
  position: absolute;
  display: block;
  top: -1px;
  left: -1px;
  width: 5px;
  height: calc(100% +  2px);
  content: '';
  background: transparent;
}
div.cell.jupyter-soft-selected {
  border-left-color: #E3F2FD;
  border-left-width: 1px;
  padding-left: 5px;
  border-right-color: #E3F2FD;
  border-right-width: 1px;
  background: #E3F2FD;
}
@media print {
  div.cell.jupyter-soft-selected {
    border-color: transparent;
  }
}
div.cell.selected,
div.cell.selected.jupyter-soft-selected {
  border-color: #ababab;
}
div.cell.selected:before,
div.cell.selected.jupyter-soft-selected:before {
  position: absolute;
  display: block;
  top: -1px;
  left: -1px;
  width: 5px;
  height: calc(100% +  2px);
  content: '';
  background: #42A5F5;
}
@media print {
  div.cell.selected,
  div.cell.selected.jupyter-soft-selected {
    border-color: transparent;
  }
}
.edit_mode div.cell.selected {
  border-color: #66BB6A;
}
.edit_mode div.cell.selected:before {
  position: absolute;
  display: block;
  top: -1px;
  left: -1px;
  width: 5px;
  height: calc(100% +  2px);
  content: '';
  background: #66BB6A;
}
@media print {
  .edit_mode div.cell.selected {
    border-color: transparent;
  }
}
.prompt {
  /* This needs to be wide enough for 3 digit prompt numbers: In[100]: */
  min-width: 14ex;
  /* This padding is tuned to match the padding on the CodeMirror editor. */
  padding: 0.4em;
  margin: 0px;
  font-family: monospace;
  text-align: right;
  /* This has to match that of the the CodeMirror class line-height below */
  line-height: 1.21429em;
  /* Don't highlight prompt number selection */
  -webkit-touch-callout: none;
  -webkit-user-select: none;
  -khtml-user-select: none;
  -moz-user-select: none;
  -ms-user-select: none;
  user-select: none;
  /* Use default cursor */
  cursor: default;
}
@media (max-width: 540px) {
  .prompt {
    text-align: left;
  }
}
div.inner_cell {
  min-width: 0;
  /* Old browsers */
  display: -webkit-box;
  -webkit-box-orient: vertical;
  -webkit-box-align: stretch;
  display: -moz-box;
  -moz-box-orient: vertical;
  -moz-box-align: stretch;
  display: box;
  box-orient: vertical;
  box-align: stretch;
  /* Modern browsers */
  display: flex;
  flex-direction: column;
  align-items: stretch;
  /* Old browsers */
  -webkit-box-flex: 1;
  -moz-box-flex: 1;
  box-flex: 1;
  /* Modern browsers */
  flex: 1;
}
/* input_area and input_prompt must match in top border and margin for alignment */
div.input_area {
  border: 1px solid #cfcfcf;
  border-radius: 2px;
  background: #f7f7f7;
  line-height: 1.21429em;
}
/* This is needed so that empty prompt areas can collapse to zero height when there
   is no content in the output_subarea and the prompt. The main purpose of this is
   to make sure that empty JavaScript output_subareas have no height. */
div.prompt:empty {
  padding-top: 0;
  padding-bottom: 0;
}
div.unrecognized_cell {
  padding: 5px 5px 5px 0px;
  /* Old browsers */
  display: -webkit-box;
  -webkit-box-orient: horizontal;
  -webkit-box-align: stretch;
  display: -moz-box;
  -moz-box-orient: horizontal;
  -moz-box-align: stretch;
  display: box;
  box-orient: horizontal;
  box-align: stretch;
  /* Modern browsers */
  display: flex;
  flex-direction: row;
  align-items: stretch;
}
div.unrecognized_cell .inner_cell {
  border-radius: 2px;
  padding: 5px;
  font-weight: bold;
  color: red;
  border: 1px solid #cfcfcf;
  background: #eaeaea;
}
div.unrecognized_cell .inner_cell a {
  color: inherit;
  text-decoration: none;
}
div.unrecognized_cell .inner_cell a:hover {
  color: inherit;
  text-decoration: none;
}
@media (max-width: 540px) {
  div.unrecognized_cell > div.prompt {
    display: none;
  }
}
div.code_cell {
  /* avoid page breaking on code cells when printing */
}
@media print {
  div.code_cell {
    page-break-inside: avoid;
  }
}
/* any special styling for code cells that are currently running goes here */
div.input {
  page-break-inside: avoid;
  /* Old browsers */
  display: -webkit-box;
  -webkit-box-orient: horizontal;
  -webkit-box-align: stretch;
  display: -moz-box;
  -moz-box-orient: horizontal;
  -moz-box-align: stretch;
  display: box;
  box-orient: horizontal;
  box-align: stretch;
  /* Modern browsers */
  display: flex;
  flex-direction: row;
  align-items: stretch;
}
@media (max-width: 540px) {
  div.input {
    /* Old browsers */
    display: -webkit-box;
    -webkit-box-orient: vertical;
    -webkit-box-align: stretch;
    display: -moz-box;
    -moz-box-orient: vertical;
    -moz-box-align: stretch;
    display: box;
    box-orient: vertical;
    box-align: stretch;
    /* Modern browsers */
    display: flex;
    flex-direction: column;
    align-items: stretch;
  }
}
/* input_area and input_prompt must match in top border and margin for alignment */
div.input_prompt {
  color: #303F9F;
  border-top: 1px solid transparent;
}
div.input_area > div.highlight {
  margin: 0.4em;
  border: none;
  padding: 0px;
  background-color: transparent;
}
div.input_area > div.highlight > pre {
  margin: 0px;
  border: none;
  padding: 0px;
  background-color: transparent;
}
/* The following gets added to the <head> if it is detected that the user has a
 * monospace font with inconsistent normal/bold/italic height.  See
 * notebookmain.js.  Such fonts will have keywords vertically offset with
 * respect to the rest of the text.  The user should select a better font.
 * See: https://github.com/ipython/ipython/issues/1503
 *
 * .CodeMirror span {
 *      vertical-align: bottom;
 * }
 */
.CodeMirror {
  line-height: 1.21429em;
  /* Changed from 1em to our global default */
  font-size: 14px;
  height: auto;
  /* Changed to auto to autogrow */
  background: none;
  /* Changed from white to allow our bg to show through */
}
.CodeMirror-scroll {
  /*  The CodeMirror docs are a bit fuzzy on if overflow-y should be hidden or visible.*/
  /*  We have found that if it is visible, vertical scrollbars appear with font size changes.*/
  overflow-y: hidden;
  overflow-x: auto;
}
.CodeMirror-lines {
  /* In CM2, this used to be 0.4em, but in CM3 it went to 4px. We need the em value because */
  /* we have set a different line-height and want this to scale with that. */
  /* Note that this should set vertical padding only, since CodeMirror assumes
       that horizontal padding will be set on CodeMirror pre */
  padding: 0.4em 0;
}
.CodeMirror-linenumber {
  padding: 0 8px 0 4px;
}
.CodeMirror-gutters {
  border-bottom-left-radius: 2px;
  border-top-left-radius: 2px;
}
.CodeMirror pre {
  /* In CM3 this went to 4px from 0 in CM2. This sets horizontal padding only,
    use .CodeMirror-lines for vertical */
  padding: 0 0.4em;
  border: 0;
  border-radius: 0;
}
.CodeMirror-cursor {
  border-left: 1.4px solid black;
}
@media screen and (min-width: 2138px) and (max-width: 4319px) {
  .CodeMirror-cursor {
    border-left: 2px solid black;
  }
}
@media screen and (min-width: 4320px) {
  .CodeMirror-cursor {
    border-left: 4px solid black;
  }
}
/*

Original style from softwaremaniacs.org (c) Ivan Sagalaev <Maniac@SoftwareManiacs.Org>
Adapted from GitHub theme

*/
.highlight-base {
  color: #000;
}
.highlight-variable {
  color: #000;
}
.highlight-variable-2 {
  color: #1a1a1a;
}
.highlight-variable-3 {
  color: #333333;
}
.highlight-string {
  color: #BA2121;
}
.highlight-comment {
  color: #408080;
  font-style: italic;
}
.highlight-number {
  color: #080;
}
.highlight-atom {
  color: #88F;
}
.highlight-keyword {
  color: #008000;
  font-weight: bold;
}
.highlight-builtin {
  color: #008000;
}
.highlight-error {
  color: #f00;
}
.highlight-operator {
  color: #AA22FF;
  font-weight: bold;
}
.highlight-meta {
  color: #AA22FF;
}
/* previously not defined, copying from default codemirror */
.highlight-def {
  color: #00f;
}
.highlight-string-2 {
  color: #f50;
}
.highlight-qualifier {
  color: #555;
}
.highlight-bracket {
  color: #997;
}
.highlight-tag {
  color: #170;
}
.highlight-attribute {
  color: #00c;
}
.highlight-header {
  color: blue;
}
.highlight-quote {
  color: #090;
}
.highlight-link {
  color: #00c;
}
/* apply the same style to codemirror */
.cm-s-ipython span.cm-keyword {
  color: #008000;
  font-weight: bold;
}
.cm-s-ipython span.cm-atom {
  color: #88F;
}
.cm-s-ipython span.cm-number {
  color: #080;
}
.cm-s-ipython span.cm-def {
  color: #00f;
}
.cm-s-ipython span.cm-variable {
  color: #000;
}
.cm-s-ipython span.cm-operator {
  color: #AA22FF;
  font-weight: bold;
}
.cm-s-ipython span.cm-variable-2 {
  color: #1a1a1a;
}
.cm-s-ipython span.cm-variable-3 {
  color: #333333;
}
.cm-s-ipython span.cm-comment {
  color: #408080;
  font-style: italic;
}
.cm-s-ipython span.cm-string {
  color: #BA2121;
}
.cm-s-ipython span.cm-string-2 {
  color: #f50;
}
.cm-s-ipython span.cm-meta {
  color: #AA22FF;
}
.cm-s-ipython span.cm-qualifier {
  color: #555;
}
.cm-s-ipython span.cm-builtin {
  color: #008000;
}
.cm-s-ipython span.cm-bracket {
  color: #997;
}
.cm-s-ipython span.cm-tag {
  color: #170;
}
.cm-s-ipython span.cm-attribute {
  color: #00c;
}
.cm-s-ipython span.cm-header {
  color: blue;
}
.cm-s-ipython span.cm-quote {
  color: #090;
}
.cm-s-ipython span.cm-link {
  color: #00c;
}
.cm-s-ipython span.cm-error {
  color: #f00;
}
.cm-s-ipython span.cm-tab {
  background: url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAADAAAAAMCAYAAAAkuj5RAAAAAXNSR0IArs4c6QAAAGFJREFUSMft1LsRQFAQheHPowAKoACx3IgEKtaEHujDjORSgWTH/ZOdnZOcM/sgk/kFFWY0qV8foQwS4MKBCS3qR6ixBJvElOobYAtivseIE120FaowJPN75GMu8j/LfMwNjh4HUpwg4LUAAAAASUVORK5CYII=);
  background-position: right;
  background-repeat: no-repeat;
}
div.output_wrapper {
  /* this position must be relative to enable descendents to be absolute within it */
  position: relative;
  /* Old browsers */
  display: -webkit-box;
  -webkit-box-orient: vertical;
  -webkit-box-align: stretch;
  display: -moz-box;
  -moz-box-orient: vertical;
  -moz-box-align: stretch;
  display: box;
  box-orient: vertical;
  box-align: stretch;
  /* Modern browsers */
  display: flex;
  flex-direction: column;
  align-items: stretch;
  z-index: 1;
}
/* class for the output area when it should be height-limited */
div.output_scroll {
  /* ideally, this would be max-height, but FF barfs all over that */
  height: 24em;
  /* FF needs this *and the wrapper* to specify full width, or it will shrinkwrap */
  width: 100%;
  overflow: auto;
  border-radius: 2px;
  -webkit-box-shadow: inset 0 2px 8px rgba(0, 0, 0, 0.8);
  box-shadow: inset 0 2px 8px rgba(0, 0, 0, 0.8);
  display: block;
}
/* output div while it is collapsed */
div.output_collapsed {
  margin: 0px;
  padding: 0px;
  /* Old browsers */
  display: -webkit-box;
  -webkit-box-orient: vertical;
  -webkit-box-align: stretch;
  display: -moz-box;
  -moz-box-orient: vertical;
  -moz-box-align: stretch;
  display: box;
  box-orient: vertical;
  box-align: stretch;
  /* Modern browsers */
  display: flex;
  flex-direction: column;
  align-items: stretch;
}
div.out_prompt_overlay {
  height: 100%;
  padding: 0px 0.4em;
  position: absolute;
  border-radius: 2px;
}
div.out_prompt_overlay:hover {
  /* use inner shadow to get border that is computed the same on WebKit/FF */
  -webkit-box-shadow: inset 0 0 1px #000;
  box-shadow: inset 0 0 1px #000;
  background: rgba(240, 240, 240, 0.5);
}
div.output_prompt {
  color: #D84315;
}
/* This class is the outer container of all output sections. */
div.output_area {
  padding: 0px;
  page-break-inside: avoid;
  /* Old browsers */
  display: -webkit-box;
  -webkit-box-orient: horizontal;
  -webkit-box-align: stretch;
  display: -moz-box;
  -moz-box-orient: horizontal;
  -moz-box-align: stretch;
  display: box;
  box-orient: horizontal;
  box-align: stretch;
  /* Modern browsers */
  display: flex;
  flex-direction: row;
  align-items: stretch;
}
div.output_area .MathJax_Display {
  text-align: left !important;
}
div.output_area .rendered_html table {
  margin-left: 0;
  margin-right: 0;
}
div.output_area .rendered_html img {
  margin-left: 0;
  margin-right: 0;
}
div.output_area img,
div.output_area svg {
  max-width: 100%;
  height: auto;
}
div.output_area img.unconfined,
div.output_area svg.unconfined {
  max-width: none;
}
div.output_area .mglyph > img {
  max-width: none;
}
/* This is needed to protect the pre formating from global settings such
   as that of bootstrap */
.output {
  /* Old browsers */
  display: -webkit-box;
  -webkit-box-orient: vertical;
  -webkit-box-align: stretch;
  display: -moz-box;
  -moz-box-orient: vertical;
  -moz-box-align: stretch;
  display: box;
  box-orient: vertical;
  box-align: stretch;
  /* Modern browsers */
  display: flex;
  flex-direction: column;
  align-items: stretch;
}
@media (max-width: 540px) {
  div.output_area {
    /* Old browsers */
    display: -webkit-box;
    -webkit-box-orient: vertical;
    -webkit-box-align: stretch;
    display: -moz-box;
    -moz-box-orient: vertical;
    -moz-box-align: stretch;
    display: box;
    box-orient: vertical;
    box-align: stretch;
    /* Modern browsers */
    display: flex;
    flex-direction: column;
    align-items: stretch;
  }
}
div.output_area pre {
  margin: 0;
  padding: 1px 0 1px 0;
  border: 0;
  vertical-align: baseline;
  color: black;
  background-color: transparent;
  border-radius: 0;
}
/* This class is for the output subarea inside the output_area and after
   the prompt div. */
div.output_subarea {
  overflow-x: auto;
  padding: 0.4em;
  /* Old browsers */
  -webkit-box-flex: 1;
  -moz-box-flex: 1;
  box-flex: 1;
  /* Modern browsers */
  flex: 1;
  max-width: calc(100% - 14ex);
}
div.output_scroll div.output_subarea {
  overflow-x: visible;
}
/* The rest of the output_* classes are for special styling of the different
   output types */
/* all text output has this class: */
div.output_text {
  text-align: left;
  color: #000;
  /* This has to match that of the the CodeMirror class line-height below */
  line-height: 1.21429em;
}
/* stdout/stderr are 'text' as well as 'stream', but execute_result/error are *not* streams */
div.output_stderr {
  background: #fdd;
  /* very light red background for stderr */
}
div.output_latex {
  text-align: left;
}
/* Empty output_javascript divs should have no height */
div.output_javascript:empty {
  padding: 0;
}
.js-error {
  color: darkred;
}
/* raw_input styles */
div.raw_input_container {
  line-height: 1.21429em;
  padding-top: 5px;
}
pre.raw_input_prompt {
  /* nothing needed here. */
}
input.raw_input {
  font-family: monospace;
  font-size: inherit;
  color: inherit;
  width: auto;
  /* make sure input baseline aligns with prompt */
  vertical-align: baseline;
  /* padding + margin = 0.5em between prompt and cursor */
  padding: 0em 0.25em;
  margin: 0em 0.25em;
}
input.raw_input:focus {
  box-shadow: none;
}
p.p-space {
  margin-bottom: 10px;
}
div.output_unrecognized {
  padding: 5px;
  font-weight: bold;
  color: red;
}
div.output_unrecognized a {
  color: inherit;
  text-decoration: none;
}
div.output_unrecognized a:hover {
  color: inherit;
  text-decoration: none;
}
.rendered_html {
  color: #000;
  /* any extras will just be numbers: */
}
.rendered_html em {
  font-style: italic;
}
.rendered_html strong {
  font-weight: bold;
}
.rendered_html u {
  text-decoration: underline;
}
.rendered_html :link {
  text-decoration: underline;
}
.rendered_html :visited {
  text-decoration: underline;
}
.rendered_html h1 {
  font-size: 185.7%;
  margin: 1.08em 0 0 0;
  font-weight: bold;
  line-height: 1.0;
}
.rendered_html h2 {
  font-size: 157.1%;
  margin: 1.27em 0 0 0;
  font-weight: bold;
  line-height: 1.0;
}
.rendered_html h3 {
  font-size: 128.6%;
  margin: 1.55em 0 0 0;
  font-weight: bold;
  line-height: 1.0;
}
.rendered_html h4 {
  font-size: 100%;
  margin: 2em 0 0 0;
  font-weight: bold;
  line-height: 1.0;
}
.rendered_html h5 {
  font-size: 100%;
  margin: 2em 0 0 0;
  font-weight: bold;
  line-height: 1.0;
  font-style: italic;
}
.rendered_html h6 {
  font-size: 100%;
  margin: 2em 0 0 0;
  font-weight: bold;
  line-height: 1.0;
  font-style: italic;
}
.rendered_html h1:first-child {
  margin-top: 0.538em;
}
.rendered_html h2:first-child {
  margin-top: 0.636em;
}
.rendered_html h3:first-child {
  margin-top: 0.777em;
}
.rendered_html h4:first-child {
  margin-top: 1em;
}
.rendered_html h5:first-child {
  margin-top: 1em;
}
.rendered_html h6:first-child {
  margin-top: 1em;
}
.rendered_html ul:not(.list-inline),
.rendered_html ol:not(.list-inline) {
  padding-left: 2em;
}
.rendered_html ul {
  list-style: disc;
}
.rendered_html ul ul {
  list-style: square;
  margin-top: 0;
}
.rendered_html ul ul ul {
  list-style: circle;
}
.rendered_html ol {
  list-style: decimal;
}
.rendered_html ol ol {
  list-style: upper-alpha;
  margin-top: 0;
}
.rendered_html ol ol ol {
  list-style: lower-alpha;
}
.rendered_html ol ol ol ol {
  list-style: lower-roman;
}
.rendered_html ol ol ol ol ol {
  list-style: decimal;
}
.rendered_html * + ul {
  margin-top: 1em;
}
.rendered_html * + ol {
  margin-top: 1em;
}
.rendered_html hr {
  color: black;
  background-color: black;
}
.rendered_html pre {
  margin: 1em 2em;
  padding: 0px;
  background-color: #fff;
}
.rendered_html code {
  background-color: #eff0f1;
}
.rendered_html p code {
  padding: 1px 5px;
}
.rendered_html pre code {
  background-color: #fff;
}
.rendered_html pre,
.rendered_html code {
  border: 0;
  color: #000;
  font-size: 100%;
}
.rendered_html blockquote {
  margin: 1em 2em;
}
.rendered_html table {
  margin-left: auto;
  margin-right: auto;
  border: none;
  border-collapse: collapse;
  border-spacing: 0;
  color: black;
  font-size: 12px;
  table-layout: fixed;
}
.rendered_html thead {
  border-bottom: 1px solid black;
  vertical-align: bottom;
}
.rendered_html tr,
.rendered_html th,
.rendered_html td {
  text-align: right;
  vertical-align: middle;
  padding: 0.5em 0.5em;
  line-height: normal;
  white-space: normal;
  max-width: none;
  border: none;
}
.rendered_html th {
  font-weight: bold;
}
.rendered_html tbody tr:nth-child(odd) {
  background: #f5f5f5;
}
.rendered_html tbody tr:hover {
  background: rgba(66, 165, 245, 0.2);
}
.rendered_html * + table {
  margin-top: 1em;
}
.rendered_html p {
  text-align: left;
}
.rendered_html * + p {
  margin-top: 1em;
}
.rendered_html img {
  display: block;
  margin-left: auto;
  margin-right: auto;
}
.rendered_html * + img {
  margin-top: 1em;
}
.rendered_html img,
.rendered_html svg {
  max-width: 100%;
  height: auto;
}
.rendered_html img.unconfined,
.rendered_html svg.unconfined {
  max-width: none;
}
.rendered_html .alert {
  margin-bottom: initial;
}
.rendered_html * + .alert {
  margin-top: 1em;
}
[dir="rtl"] .rendered_html p {
  text-align: right;
}
div.text_cell {
  /* Old browsers */
  display: -webkit-box;
  -webkit-box-orient: horizontal;
  -webkit-box-align: stretch;
  display: -moz-box;
  -moz-box-orient: horizontal;
  -moz-box-align: stretch;
  display: box;
  box-orient: horizontal;
  box-align: stretch;
  /* Modern browsers */
  display: flex;
  flex-direction: row;
  align-items: stretch;
}
@media (max-width: 540px) {
  div.text_cell > div.prompt {
    display: none;
  }
}
div.text_cell_render {
  /*font-family: "Helvetica Neue", Arial, Helvetica, Geneva, sans-serif;*/
  outline: none;
  resize: none;
  width: inherit;
  border-style: none;
  padding: 0.5em 0.5em 0.5em 0.4em;
  color: #000;
  box-sizing: border-box;
  -moz-box-sizing: border-box;
  -webkit-box-sizing: border-box;
}
a.anchor-link:link {
  text-decoration: none;
  padding: 0px 20px;
  visibility: hidden;
}
h1:hover .anchor-link,
h2:hover .anchor-link,
h3:hover .anchor-link,
h4:hover .anchor-link,
h5:hover .anchor-link,
h6:hover .anchor-link {
  visibility: visible;
}
.text_cell.rendered .input_area {
  display: none;
}
.text_cell.rendered .rendered_html {
  overflow-x: auto;
  overflow-y: hidden;
}
.text_cell.rendered .rendered_html tr,
.text_cell.rendered .rendered_html th,
.text_cell.rendered .rendered_html td {
  max-width: none;
}
.text_cell.unrendered .text_cell_render {
  display: none;
}
.text_cell .dropzone .input_area {
  border: 2px dashed #bababa;
  margin: -1px;
}
.cm-header-1,
.cm-header-2,
.cm-header-3,
.cm-header-4,
.cm-header-5,
.cm-header-6 {
  font-weight: bold;
  font-family: "Helvetica Neue", Helvetica, Arial, sans-serif;
}
.cm-header-1 {
  font-size: 185.7%;
}
.cm-header-2 {
  font-size: 157.1%;
}
.cm-header-3 {
  font-size: 128.6%;
}
.cm-header-4 {
  font-size: 110%;
}
.cm-header-5 {
  font-size: 100%;
  font-style: italic;
}
.cm-header-6 {
  font-size: 100%;
  font-style: italic;
}
/*!
*
* IPython notebook webapp
*
*/
@media (max-width: 767px) {
  .notebook_app {
    padding-left: 0px;
    padding-right: 0px;
  }
}
#ipython-main-app {
  box-sizing: border-box;
  -moz-box-sizing: border-box;
  -webkit-box-sizing: border-box;
  height: 100%;
}
div#notebook_panel {
  margin: 0px;
  padding: 0px;
  box-sizing: border-box;
  -moz-box-sizing: border-box;
  -webkit-box-sizing: border-box;
  height: 100%;
}
div#notebook {
  font-size: 14px;
  line-height: 20px;
  overflow-y: hidden;
  overflow-x: auto;
  width: 100%;
  /* This spaces the page away from the edge of the notebook area */
  padding-top: 20px;
  margin: 0px;
  outline: none;
  box-sizing: border-box;
  -moz-box-sizing: border-box;
  -webkit-box-sizing: border-box;
  min-height: 100%;
}
@media not print {
  #notebook-container {
    padding: 15px;
    background-color: #fff;
    min-height: 0;
    -webkit-box-shadow: 0px 0px 12px 1px rgba(87, 87, 87, 0.2);
    box-shadow: 0px 0px 12px 1px rgba(87, 87, 87, 0.2);
  }
}
@media print {
  #notebook-container {
    width: 100%;
  }
}
div.ui-widget-content {
  border: 1px solid #ababab;
  outline: none;
}
pre.dialog {
  background-color: #f7f7f7;
  border: 1px solid #ddd;
  border-radius: 2px;
  padding: 0.4em;
  padding-left: 2em;
}
p.dialog {
  padding: 0.2em;
}
/* Word-wrap output correctly.  This is the CSS3 spelling, though Firefox seems
   to not honor it correctly.  Webkit browsers (Chrome, rekonq, Safari) do.
 */
pre,
code,
kbd,
samp {
  white-space: pre-wrap;
}
#fonttest {
  font-family: monospace;
}
p {
  margin-bottom: 0;
}
.end_space {
  min-height: 100px;
  transition: height .2s ease;
}
.notebook_app > #header {
  -webkit-box-shadow: 0px 0px 12px 1px rgba(87, 87, 87, 0.2);
  box-shadow: 0px 0px 12px 1px rgba(87, 87, 87, 0.2);
}
@media not print {
  .notebook_app {
    background-color: #EEE;
  }
}
kbd {
  border-style: solid;
  border-width: 1px;
  box-shadow: none;
  margin: 2px;
  padding-left: 2px;
  padding-right: 2px;
  padding-top: 1px;
  padding-bottom: 1px;
}
.jupyter-keybindings {
  padding: 1px;
  line-height: 24px;
  border-bottom: 1px solid gray;
}
.jupyter-keybindings input {
  margin: 0;
  padding: 0;
  border: none;
}
.jupyter-keybindings i {
  padding: 6px;
}
.well code {
  background-color: #ffffff;
  border-color: #ababab;
  border-width: 1px;
  border-style: solid;
  padding: 2px;
  padding-top: 1px;
  padding-bottom: 1px;
}
/* CSS for the cell toolbar */
.celltoolbar {
  border: thin solid #CFCFCF;
  border-bottom: none;
  background: #EEE;
  border-radius: 2px 2px 0px 0px;
  width: 100%;
  height: 29px;
  padding-right: 4px;
  /* Old browsers */
  display: -webkit-box;
  -webkit-box-orient: horizontal;
  -webkit-box-align: stretch;
  display: -moz-box;
  -moz-box-orient: horizontal;
  -moz-box-align: stretch;
  display: box;
  box-orient: horizontal;
  box-align: stretch;
  /* Modern browsers */
  display: flex;
  flex-direction: row;
  align-items: stretch;
  /* Old browsers */
  -webkit-box-pack: end;
  -moz-box-pack: end;
  box-pack: end;
  /* Modern browsers */
  justify-content: flex-end;
  display: -webkit-flex;
}
@media print {
  .celltoolbar {
    display: none;
  }
}
.ctb_hideshow {
  display: none;
  vertical-align: bottom;
}
/* ctb_show is added to the ctb_hideshow div to show the cell toolbar.
   Cell toolbars are only shown when the ctb_global_show class is also set.
*/
.ctb_global_show .ctb_show.ctb_hideshow {
  display: block;
}
.ctb_global_show .ctb_show + .input_area,
.ctb_global_show .ctb_show + div.text_cell_input,
.ctb_global_show .ctb_show ~ div.text_cell_render {
  border-top-right-radius: 0px;
  border-top-left-radius: 0px;
}
.ctb_global_show .ctb_show ~ div.text_cell_render {
  border: 1px solid #cfcfcf;
}
.celltoolbar {
  font-size: 87%;
  padding-top: 3px;
}
.celltoolbar select {
  display: block;
  width: 100%;
  height: 32px;
  padding: 6px 12px;
  font-size: 13px;
  line-height: 1.42857143;
  color: #555555;
  background-color: #fff;
  background-image: none;
  border: 1px solid #ccc;
  border-radius: 2px;
  -webkit-box-shadow: inset 0 1px 1px rgba(0, 0, 0, 0.075);
  box-shadow: inset 0 1px 1px rgba(0, 0, 0, 0.075);
  -webkit-transition: border-color ease-in-out .15s, box-shadow ease-in-out .15s;
  -o-transition: border-color ease-in-out .15s, box-shadow ease-in-out .15s;
  transition: border-color ease-in-out .15s, box-shadow ease-in-out .15s;
  height: 30px;
  padding: 5px 10px;
  font-size: 12px;
  line-height: 1.5;
  border-radius: 1px;
  width: inherit;
  font-size: inherit;
  height: 22px;
  padding: 0px;
  display: inline-block;
}
.celltoolbar select:focus {
  border-color: #66afe9;
  outline: 0;
  -webkit-box-shadow: inset 0 1px 1px rgba(0,0,0,.075), 0 0 8px rgba(102, 175, 233, 0.6);
  box-shadow: inset 0 1px 1px rgba(0,0,0,.075), 0 0 8px rgba(102, 175, 233, 0.6);
}
.celltoolbar select::-moz-placeholder {
  color: #999;
  opacity: 1;
}
.celltoolbar select:-ms-input-placeholder {
  color: #999;
}
.celltoolbar select::-webkit-input-placeholder {
  color: #999;
}
.celltoolbar select::-ms-expand {
  border: 0;
  background-color: transparent;
}
.celltoolbar select[disabled],
.celltoolbar select[readonly],
fieldset[disabled] .celltoolbar select {
  background-color: #eeeeee;
  opacity: 1;
}
.celltoolbar select[disabled],
fieldset[disabled] .celltoolbar select {
  cursor: not-allowed;
}
textarea.celltoolbar select {
  height: auto;
}
select.celltoolbar select {
  height: 30px;
  line-height: 30px;
}
textarea.celltoolbar select,
select[multiple].celltoolbar select {
  height: auto;
}
.celltoolbar label {
  margin-left: 5px;
  margin-right: 5px;
}
.tags_button_container {
  width: 100%;
  display: flex;
}
.tag-container {
  display: flex;
  flex-direction: row;
  flex-grow: 1;
  overflow: hidden;
  position: relative;
}
.tag-container > * {
  margin: 0 4px;
}
.remove-tag-btn {
  margin-left: 4px;
}
.tags-input {
  display: flex;
}
.cell-tag:last-child:after {
  content: "";
  position: absolute;
  right: 0;
  width: 40px;
  height: 100%;
  /* Fade to background color of cell toolbar */
  background: linear-gradient(to right, rgba(0, 0, 0, 0), #EEE);
}
.tags-input > * {
  margin-left: 4px;
}
.cell-tag,
.tags-input input,
.tags-input button {
  display: block;
  width: 100%;
  height: 32px;
  padding: 6px 12px;
  font-size: 13px;
  line-height: 1.42857143;
  color: #555555;
  background-color: #fff;
  background-image: none;
  border: 1px solid #ccc;
  border-radius: 2px;
  -webkit-box-shadow: inset 0 1px 1px rgba(0, 0, 0, 0.075);
  box-shadow: inset 0 1px 1px rgba(0, 0, 0, 0.075);
  -webkit-transition: border-color ease-in-out .15s, box-shadow ease-in-out .15s;
  -o-transition: border-color ease-in-out .15s, box-shadow ease-in-out .15s;
  transition: border-color ease-in-out .15s, box-shadow ease-in-out .15s;
  height: 30px;
  padding: 5px 10px;
  font-size: 12px;
  line-height: 1.5;
  border-radius: 1px;
  box-shadow: none;
  width: inherit;
  font-size: inherit;
  height: 22px;
  line-height: 22px;
  padding: 0px 4px;
  display: inline-block;
}
.cell-tag:focus,
.tags-input input:focus,
.tags-input button:focus {
  border-color: #66afe9;
  outline: 0;
  -webkit-box-shadow: inset 0 1px 1px rgba(0,0,0,.075), 0 0 8px rgba(102, 175, 233, 0.6);
  box-shadow: inset 0 1px 1px rgba(0,0,0,.075), 0 0 8px rgba(102, 175, 233, 0.6);
}
.cell-tag::-moz-placeholder,
.tags-input input::-moz-placeholder,
.tags-input button::-moz-placeholder {
  color: #999;
  opacity: 1;
}
.cell-tag:-ms-input-placeholder,
.tags-input input:-ms-input-placeholder,
.tags-input button:-ms-input-placeholder {
  color: #999;
}
.cell-tag::-webkit-input-placeholder,
.tags-input input::-webkit-input-placeholder,
.tags-input button::-webkit-input-placeholder {
  color: #999;
}
.cell-tag::-ms-expand,
.tags-input input::-ms-expand,
.tags-input button::-ms-expand {
  border: 0;
  background-color: transparent;
}
.cell-tag[disabled],
.tags-input input[disabled],
.tags-input button[disabled],
.cell-tag[readonly],
.tags-input input[readonly],
.tags-input button[readonly],
fieldset[disabled] .cell-tag,
fieldset[disabled] .tags-input input,
fieldset[disabled] .tags-input button {
  background-color: #eeeeee;
  opacity: 1;
}
.cell-tag[disabled],
.tags-input input[disabled],
.tags-input button[disabled],
fieldset[disabled] .cell-tag,
fieldset[disabled] .tags-input input,
fieldset[disabled] .tags-input button {
  cursor: not-allowed;
}
textarea.cell-tag,
textarea.tags-input input,
textarea.tags-input button {
  height: auto;
}
select.cell-tag,
select.tags-input input,
select.tags-input button {
  height: 30px;
  line-height: 30px;
}
textarea.cell-tag,
textarea.tags-input input,
textarea.tags-input button,
select[multiple].cell-tag,
select[multiple].tags-input input,
select[multiple].tags-input button {
  height: auto;
}
.cell-tag,
.tags-input button {
  padding: 0px 4px;
}
.cell-tag {
  background-color: #fff;
  white-space: nowrap;
}
.tags-input input[type=text]:focus {
  outline: none;
  box-shadow: none;
  border-color: #ccc;
}
.completions {
  position: absolute;
  z-index: 110;
  overflow: hidden;
  border: 1px solid #ababab;
  border-radius: 2px;
  -webkit-box-shadow: 0px 6px 10px -1px #adadad;
  box-shadow: 0px 6px 10px -1px #adadad;
  line-height: 1;
}
.completions select {
  background: white;
  outline: none;
  border: none;
  padding: 0px;
  margin: 0px;
  overflow: auto;
  font-family: monospace;
  font-size: 110%;
  color: #000;
  width: auto;
}
.completions select option.context {
  color: #286090;
}
#kernel_logo_widget .current_kernel_logo {
  display: none;
  margin-top: -1px;
  margin-bottom: -1px;
  width: 32px;
  height: 32px;
}
[dir="rtl"] #kernel_logo_widget {
  float: left !important;
  float: left;
}
.modal .modal-body .move-path {
  display: flex;
  flex-direction: row;
  justify-content: space;
  align-items: center;
}
.modal .modal-body .move-path .server-root {
  padding-right: 20px;
}
.modal .modal-body .move-path .path-input {
  flex: 1;
}
#menubar {
  box-sizing: border-box;
  -moz-box-sizing: border-box;
  -webkit-box-sizing: border-box;
  margin-top: 1px;
}
#menubar .navbar {
  border-top: 1px;
  border-radius: 0px 0px 2px 2px;
  margin-bottom: 0px;
}
#menubar .navbar-toggle {
  float: left;
  padding-top: 7px;
  padding-bottom: 7px;
  border: none;
}
#menubar .navbar-collapse {
  clear: left;
}
[dir="rtl"] #menubar .navbar-toggle {
  float: right;
}
[dir="rtl"] #menubar .navbar-collapse {
  clear: right;
}
[dir="rtl"] #menubar .navbar-nav {
  float: right;
}
[dir="rtl"] #menubar .nav {
  padding-right: 0px;
}
[dir="rtl"] #menubar .navbar-nav > li {
  float: right;
}
[dir="rtl"] #menubar .navbar-right {
  float: left !important;
}
[dir="rtl"] ul.dropdown-menu {
  text-align: right;
  left: auto;
}
[dir="rtl"] ul#new-menu.dropdown-menu {
  right: auto;
  left: 0;
}
.nav-wrapper {
  border-bottom: 1px solid #e7e7e7;
}
i.menu-icon {
  padding-top: 4px;
}
[dir="rtl"] i.menu-icon.pull-right {
  float: left !important;
  float: left;
}
ul#help_menu li a {
  overflow: hidden;
  padding-right: 2.2em;
}
ul#help_menu li a i {
  margin-right: -1.2em;
}
[dir="rtl"] ul#help_menu li a {
  padding-left: 2.2em;
}
[dir="rtl"] ul#help_menu li a i {
  margin-right: 0;
  margin-left: -1.2em;
}
[dir="rtl"] ul#help_menu li a i.pull-right {
  float: left !important;
  float: left;
}
.dropdown-submenu {
  position: relative;
}
.dropdown-submenu > .dropdown-menu {
  top: 0;
  left: 100%;
  margin-top: -6px;
  margin-left: -1px;
}
[dir="rtl"] .dropdown-submenu > .dropdown-menu {
  right: 100%;
  margin-right: -1px;
}
.dropdown-submenu:hover > .dropdown-menu {
  display: block;
}
.dropdown-submenu > a:after {
  display: inline-block;
  font: normal normal normal 14px/1 FontAwesome;
  font-size: inherit;
  text-rendering: auto;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  display: block;
  content: "\f0da";
  float: right;
  color: #333333;
  margin-top: 2px;
  margin-right: -10px;
}
.dropdown-submenu > a:after.fa-pull-left {
  margin-right: .3em;
}
.dropdown-submenu > a:after.fa-pull-right {
  margin-left: .3em;
}
.dropdown-submenu > a:after.pull-left {
  margin-right: .3em;
}
.dropdown-submenu > a:after.pull-right {
  margin-left: .3em;
}
[dir="rtl"] .dropdown-submenu > a:after {
  float: left;
  content: "\f0d9";
  margin-right: 0;
  margin-left: -10px;
}
.dropdown-submenu:hover > a:after {
  color: #262626;
}
.dropdown-submenu.pull-left {
  float: none;
}
.dropdown-submenu.pull-left > .dropdown-menu {
  left: -100%;
  margin-left: 10px;
}
#notification_area {
  float: right !important;
  float: right;
  z-index: 10;
}
[dir="rtl"] #notification_area {
  float: left !important;
  float: left;
}
.indicator_area {
  float: right !important;
  float: right;
  color: #777;
  margin-left: 5px;
  margin-right: 5px;
  width: 11px;
  z-index: 10;
  text-align: center;
  width: auto;
}
[dir="rtl"] .indicator_area {
  float: left !important;
  float: left;
}
#kernel_indicator {
  float: right !important;
  float: right;
  color: #777;
  margin-left: 5px;
  margin-right: 5px;
  width: 11px;
  z-index: 10;
  text-align: center;
  width: auto;
  border-left: 1px solid;
}
#kernel_indicator .kernel_indicator_name {
  padding-left: 5px;
  padding-right: 5px;
}
[dir="rtl"] #kernel_indicator {
  float: left !important;
  float: left;
  border-left: 0;
  border-right: 1px solid;
}
#modal_indicator {
  float: right !important;
  float: right;
  color: #777;
  margin-left: 5px;
  margin-right: 5px;
  width: 11px;
  z-index: 10;
  text-align: center;
  width: auto;
}
[dir="rtl"] #modal_indicator {
  float: left !important;
  float: left;
}
#readonly-indicator {
  float: right !important;
  float: right;
  color: #777;
  margin-left: 5px;
  margin-right: 5px;
  width: 11px;
  z-index: 10;
  text-align: center;
  width: auto;
  margin-top: 2px;
  margin-bottom: 0px;
  margin-left: 0px;
  margin-right: 0px;
  display: none;
}
.modal_indicator:before {
  width: 1.28571429em;
  text-align: center;
}
.edit_mode .modal_indicator:before {
  display: inline-block;
  font: normal normal normal 14px/1 FontAwesome;
  font-size: inherit;
  text-rendering: auto;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  content: "\f040";
}
.edit_mode .modal_indicator:before.fa-pull-left {
  margin-right: .3em;
}
.edit_mode .modal_indicator:before.fa-pull-right {
  margin-left: .3em;
}
.edit_mode .modal_indicator:before.pull-left {
  margin-right: .3em;
}
.edit_mode .modal_indicator:before.pull-right {
  margin-left: .3em;
}
.command_mode .modal_indicator:before {
  display: inline-block;
  font: normal normal normal 14px/1 FontAwesome;
  font-size: inherit;
  text-rendering: auto;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  content: ' ';
}
.command_mode .modal_indicator:before.fa-pull-left {
  margin-right: .3em;
}
.command_mode .modal_indicator:before.fa-pull-right {
  margin-left: .3em;
}
.command_mode .modal_indicator:before.pull-left {
  margin-right: .3em;
}
.command_mode .modal_indicator:before.pull-right {
  margin-left: .3em;
}
.kernel_idle_icon:before {
  display: inline-block;
  font: normal normal normal 14px/1 FontAwesome;
  font-size: inherit;
  text-rendering: auto;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  content: "\f10c";
}
.kernel_idle_icon:before.fa-pull-left {
  margin-right: .3em;
}
.kernel_idle_icon:before.fa-pull-right {
  margin-left: .3em;
}
.kernel_idle_icon:before.pull-left {
  margin-right: .3em;
}
.kernel_idle_icon:before.pull-right {
  margin-left: .3em;
}
.kernel_busy_icon:before {
  display: inline-block;
  font: normal normal normal 14px/1 FontAwesome;
  font-size: inherit;
  text-rendering: auto;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  content: "\f111";
}
.kernel_busy_icon:before.fa-pull-left {
  margin-right: .3em;
}
.kernel_busy_icon:before.fa-pull-right {
  margin-left: .3em;
}
.kernel_busy_icon:before.pull-left {
  margin-right: .3em;
}
.kernel_busy_icon:before.pull-right {
  margin-left: .3em;
}
.kernel_dead_icon:before {
  display: inline-block;
  font: normal normal normal 14px/1 FontAwesome;
  font-size: inherit;
  text-rendering: auto;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  content: "\f1e2";
}
.kernel_dead_icon:before.fa-pull-left {
  margin-right: .3em;
}
.kernel_dead_icon:before.fa-pull-right {
  margin-left: .3em;
}
.kernel_dead_icon:before.pull-left {
  margin-right: .3em;
}
.kernel_dead_icon:before.pull-right {
  margin-left: .3em;
}
.kernel_disconnected_icon:before {
  display: inline-block;
  font: normal normal normal 14px/1 FontAwesome;
  font-size: inherit;
  text-rendering: auto;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  content: "\f127";
}
.kernel_disconnected_icon:before.fa-pull-left {
  margin-right: .3em;
}
.kernel_disconnected_icon:before.fa-pull-right {
  margin-left: .3em;
}
.kernel_disconnected_icon:before.pull-left {
  margin-right: .3em;
}
.kernel_disconnected_icon:before.pull-right {
  margin-left: .3em;
}
.notification_widget {
  color: #777;
  z-index: 10;
  background: rgba(240, 240, 240, 0.5);
  margin-right: 4px;
  color: #333;
  background-color: #fff;
  border-color: #ccc;
}
.notification_widget:focus,
.notification_widget.focus {
  color: #333;
  background-color: #e6e6e6;
  border-color: #8c8c8c;
}
.notification_widget:hover {
  color: #333;
  background-color: #e6e6e6;
  border-color: #adadad;
}
.notification_widget:active,
.notification_widget.active,
.open > .dropdown-toggle.notification_widget {
  color: #333;
  background-color: #e6e6e6;
  border-color: #adadad;
}
.notification_widget:active:hover,
.notification_widget.active:hover,
.open > .dropdown-toggle.notification_widget:hover,
.notification_widget:active:focus,
.notification_widget.active:focus,
.open > .dropdown-toggle.notification_widget:focus,
.notification_widget:active.focus,
.notification_widget.active.focus,
.open > .dropdown-toggle.notification_widget.focus {
  color: #333;
  background-color: #d4d4d4;
  border-color: #8c8c8c;
}
.notification_widget:active,
.notification_widget.active,
.open > .dropdown-toggle.notification_widget {
  background-image: none;
}
.notification_widget.disabled:hover,
.notification_widget[disabled]:hover,
fieldset[disabled] .notification_widget:hover,
.notification_widget.disabled:focus,
.notification_widget[disabled]:focus,
fieldset[disabled] .notification_widget:focus,
.notification_widget.disabled.focus,
.notification_widget[disabled].focus,
fieldset[disabled] .notification_widget.focus {
  background-color: #fff;
  border-color: #ccc;
}
.notification_widget .badge {
  color: #fff;
  background-color: #333;
}
.notification_widget.warning {
  color: #fff;
  background-color: #f0ad4e;
  border-color: #eea236;
}
.notification_widget.warning:focus,
.notification_widget.warning.focus {
  color: #fff;
  background-color: #ec971f;
  border-color: #985f0d;
}
.notification_widget.warning:hover {
  color: #fff;
  background-color: #ec971f;
  border-color: #d58512;
}
.notification_widget.warning:active,
.notification_widget.warning.active,
.open > .dropdown-toggle.notification_widget.warning {
  color: #fff;
  background-color: #ec971f;
  border-color: #d58512;
}
.notification_widget.warning:active:hover,
.notification_widget.warning.active:hover,
.open > .dropdown-toggle.notification_widget.warning:hover,
.notification_widget.warning:active:focus,
.notification_widget.warning.active:focus,
.open > .dropdown-toggle.notification_widget.warning:focus,
.notification_widget.warning:active.focus,
.notification_widget.warning.active.focus,
.open > .dropdown-toggle.notification_widget.warning.focus {
  color: #fff;
  background-color: #d58512;
  border-color: #985f0d;
}
.notification_widget.warning:active,
.notification_widget.warning.active,
.open > .dropdown-toggle.notification_widget.warning {
  background-image: none;
}
.notification_widget.warning.disabled:hover,
.notification_widget.warning[disabled]:hover,
fieldset[disabled] .notification_widget.warning:hover,
.notification_widget.warning.disabled:focus,
.notification_widget.warning[disabled]:focus,
fieldset[disabled] .notification_widget.warning:focus,
.notification_widget.warning.disabled.focus,
.notification_widget.warning[disabled].focus,
fieldset[disabled] .notification_widget.warning.focus {
  background-color: #f0ad4e;
  border-color: #eea236;
}
.notification_widget.warning .badge {
  color: #f0ad4e;
  background-color: #fff;
}
.notification_widget.success {
  color: #fff;
  background-color: #5cb85c;
  border-color: #4cae4c;
}
.notification_widget.success:focus,
.notification_widget.success.focus {
  color: #fff;
  background-color: #449d44;
  border-color: #255625;
}
.notification_widget.success:hover {
  color: #fff;
  background-color: #449d44;
  border-color: #398439;
}
.notification_widget.success:active,
.notification_widget.success.active,
.open > .dropdown-toggle.notification_widget.success {
  color: #fff;
  background-color: #449d44;
  border-color: #398439;
}
.notification_widget.success:active:hover,
.notification_widget.success.active:hover,
.open > .dropdown-toggle.notification_widget.success:hover,
.notification_widget.success:active:focus,
.notification_widget.success.active:focus,
.open > .dropdown-toggle.notification_widget.success:focus,
.notification_widget.success:active.focus,
.notification_widget.success.active.focus,
.open > .dropdown-toggle.notification_widget.success.focus {
  color: #fff;
  background-color: #398439;
  border-color: #255625;
}
.notification_widget.success:active,
.notification_widget.success.active,
.open > .dropdown-toggle.notification_widget.success {
  background-image: none;
}
.notification_widget.success.disabled:hover,
.notification_widget.success[disabled]:hover,
fieldset[disabled] .notification_widget.success:hover,
.notification_widget.success.disabled:focus,
.notification_widget.success[disabled]:focus,
fieldset[disabled] .notification_widget.success:focus,
.notification_widget.success.disabled.focus,
.notification_widget.success[disabled].focus,
fieldset[disabled] .notification_widget.success.focus {
  background-color: #5cb85c;
  border-color: #4cae4c;
}
.notification_widget.success .badge {
  color: #5cb85c;
  background-color: #fff;
}
.notification_widget.info {
  color: #fff;
  background-color: #5bc0de;
  border-color: #46b8da;
}
.notification_widget.info:focus,
.notification_widget.info.focus {
  color: #fff;
  background-color: #31b0d5;
  border-color: #1b6d85;
}
.notification_widget.info:hover {
  color: #fff;
  background-color: #31b0d5;
  border-color: #269abc;
}
.notification_widget.info:active,
.notification_widget.info.active,
.open > .dropdown-toggle.notification_widget.info {
  color: #fff;
  background-color: #31b0d5;
  border-color: #269abc;
}
.notification_widget.info:active:hover,
.notification_widget.info.active:hover,
.open > .dropdown-toggle.notification_widget.info:hover,
.notification_widget.info:active:focus,
.notification_widget.info.active:focus,
.open > .dropdown-toggle.notification_widget.info:focus,
.notification_widget.info:active.focus,
.notification_widget.info.active.focus,
.open > .dropdown-toggle.notification_widget.info.focus {
  color: #fff;
  background-color: #269abc;
  border-color: #1b6d85;
}
.notification_widget.info:active,
.notification_widget.info.active,
.open > .dropdown-toggle.notification_widget.info {
  background-image: none;
}
.notification_widget.info.disabled:hover,
.notification_widget.info[disabled]:hover,
fieldset[disabled] .notification_widget.info:hover,
.notification_widget.info.disabled:focus,
.notification_widget.info[disabled]:focus,
fieldset[disabled] .notification_widget.info:focus,
.notification_widget.info.disabled.focus,
.notification_widget.info[disabled].focus,
fieldset[disabled] .notification_widget.info.focus {
  background-color: #5bc0de;
  border-color: #46b8da;
}
.notification_widget.info .badge {
  color: #5bc0de;
  background-color: #fff;
}
.notification_widget.danger {
  color: #fff;
  background-color: #d9534f;
  border-color: #d43f3a;
}
.notification_widget.danger:focus,
.notification_widget.danger.focus {
  color: #fff;
  background-color: #c9302c;
  border-color: #761c19;
}
.notification_widget.danger:hover {
  color: #fff;
  background-color: #c9302c;
  border-color: #ac2925;
}
.notification_widget.danger:active,
.notification_widget.danger.active,
.open > .dropdown-toggle.notification_widget.danger {
  color: #fff;
  background-color: #c9302c;
  border-color: #ac2925;
}
.notification_widget.danger:active:hover,
.notification_widget.danger.active:hover,
.open > .dropdown-toggle.notification_widget.danger:hover,
.notification_widget.danger:active:focus,
.notification_widget.danger.active:focus,
.open > .dropdown-toggle.notification_widget.danger:focus,
.notification_widget.danger:active.focus,
.notification_widget.danger.active.focus,
.open > .dropdown-toggle.notification_widget.danger.focus {
  color: #fff;
  background-color: #ac2925;
  border-color: #761c19;
}
.notification_widget.danger:active,
.notification_widget.danger.active,
.open > .dropdown-toggle.notification_widget.danger {
  background-image: none;
}
.notification_widget.danger.disabled:hover,
.notification_widget.danger[disabled]:hover,
fieldset[disabled] .notification_widget.danger:hover,
.notification_widget.danger.disabled:focus,
.notification_widget.danger[disabled]:focus,
fieldset[disabled] .notification_widget.danger:focus,
.notification_widget.danger.disabled.focus,
.notification_widget.danger[disabled].focus,
fieldset[disabled] .notification_widget.danger.focus {
  background-color: #d9534f;
  border-color: #d43f3a;
}
.notification_widget.danger .badge {
  color: #d9534f;
  background-color: #fff;
}
div#pager {
  background-color: #fff;
  font-size: 14px;
  line-height: 20px;
  overflow: hidden;
  display: none;
  position: fixed;
  bottom: 0px;
  width: 100%;
  max-height: 50%;
  padding-top: 8px;
  -webkit-box-shadow: 0px 0px 12px 1px rgba(87, 87, 87, 0.2);
  box-shadow: 0px 0px 12px 1px rgba(87, 87, 87, 0.2);
  /* Display over codemirror */
  z-index: 100;
  /* Hack which prevents jquery ui resizable from changing top. */
  top: auto !important;
}
div#pager pre {
  line-height: 1.21429em;
  color: #000;
  background-color: #f7f7f7;
  padding: 0.4em;
}
div#pager #pager-button-area {
  position: absolute;
  top: 8px;
  right: 20px;
}
div#pager #pager-contents {
  position: relative;
  overflow: auto;
  width: 100%;
  height: 100%;
}
div#pager #pager-contents #pager-container {
  position: relative;
  padding: 15px 0px;
  box-sizing: border-box;
  -moz-box-sizing: border-box;
  -webkit-box-sizing: border-box;
}
div#pager .ui-resizable-handle {
  top: 0px;
  height: 8px;
  background: #f7f7f7;
  border-top: 1px solid #cfcfcf;
  border-bottom: 1px solid #cfcfcf;
  /* This injects handle bars (a short, wide = symbol) for 
        the resize handle. */
}
div#pager .ui-resizable-handle::after {
  content: '';
  top: 2px;
  left: 50%;
  height: 3px;
  width: 30px;
  margin-left: -15px;
  position: absolute;
  border-top: 1px solid #cfcfcf;
}
.quickhelp {
  /* Old browsers */
  display: -webkit-box;
  -webkit-box-orient: horizontal;
  -webkit-box-align: stretch;
  display: -moz-box;
  -moz-box-orient: horizontal;
  -moz-box-align: stretch;
  display: box;
  box-orient: horizontal;
  box-align: stretch;
  /* Modern browsers */
  display: flex;
  flex-direction: row;
  align-items: stretch;
  line-height: 1.8em;
}
.shortcut_key {
  display: inline-block;
  width: 21ex;
  text-align: right;
  font-family: monospace;
}
.shortcut_descr {
  display: inline-block;
  /* Old browsers */
  -webkit-box-flex: 1;
  -moz-box-flex: 1;
  box-flex: 1;
  /* Modern browsers */
  flex: 1;
}
span.save_widget {
  height: 30px;
  margin-top: 4px;
  display: flex;
  justify-content: flex-start;
  align-items: baseline;
  width: 50%;
  flex: 1;
}
span.save_widget span.filename {
  height: 100%;
  line-height: 1em;
  margin-left: 16px;
  border: none;
  font-size: 146.5%;
  text-overflow: ellipsis;
  overflow: hidden;
  white-space: nowrap;
  border-radius: 2px;
}
span.save_widget span.filename:hover {
  background-color: #e6e6e6;
}
[dir="rtl"] span.save_widget.pull-left {
  float: right !important;
  float: right;
}
[dir="rtl"] span.save_widget span.filename {
  margin-left: 0;
  margin-right: 16px;
}
span.checkpoint_status,
span.autosave_status {
  font-size: small;
  white-space: nowrap;
  padding: 0 5px;
}
@media (max-width: 767px) {
  span.save_widget {
    font-size: small;
    padding: 0 0 0 5px;
  }
  span.checkpoint_status,
  span.autosave_status {
    display: none;
  }
}
@media (min-width: 768px) and (max-width: 991px) {
  span.checkpoint_status {
    display: none;
  }
  span.autosave_status {
    font-size: x-small;
  }
}
.toolbar {
  padding: 0px;
  margin-left: -5px;
  margin-top: 2px;
  margin-bottom: 5px;
  box-sizing: border-box;
  -moz-box-sizing: border-box;
  -webkit-box-sizing: border-box;
}
.toolbar select,
.toolbar label {
  width: auto;
  vertical-align: middle;
  margin-right: 2px;
  margin-bottom: 0px;
  display: inline;
  font-size: 92%;
  margin-left: 0.3em;
  margin-right: 0.3em;
  padding: 0px;
  padding-top: 3px;
}
.toolbar .btn {
  padding: 2px 8px;
}
.toolbar .btn-group {
  margin-top: 0px;
  margin-left: 5px;
}
.toolbar-btn-label {
  margin-left: 6px;
}
#maintoolbar {
  margin-bottom: -3px;
  margin-top: -8px;
  border: 0px;
  min-height: 27px;
  margin-left: 0px;
  padding-top: 11px;
  padding-bottom: 3px;
}
#maintoolbar .navbar-text {
  float: none;
  vertical-align: middle;
  text-align: right;
  margin-left: 5px;
  margin-right: 0px;
  margin-top: 0px;
}
.select-xs {
  height: 24px;
}
[dir="rtl"] .btn-group > .btn,
.btn-group-vertical > .btn {
  float: right;
}
.pulse,
.dropdown-menu > li > a.pulse,
li.pulse > a.dropdown-toggle,
li.pulse.open > a.dropdown-toggle {
  background-color: #F37626;
  color: white;
}
/**
 * Primary styles
 *
 * Author: Jupyter Development Team
 */
/** WARNING IF YOU ARE EDITTING THIS FILE, if this is a .css file, It has a lot
 * of chance of beeing generated from the ../less/[samename].less file, you can
 * try to get back the less file by reverting somme commit in history
 **/
/*
 * We'll try to get something pretty, so we
 * have some strange css to have the scroll bar on
 * the left with fix button on the top right of the tooltip
 */
@-moz-keyframes fadeOut {
  from {
    opacity: 1;
  }
  to {
    opacity: 0;
  }
}
@-webkit-keyframes fadeOut {
  from {
    opacity: 1;
  }
  to {
    opacity: 0;
  }
}
@-moz-keyframes fadeIn {
  from {
    opacity: 0;
  }
  to {
    opacity: 1;
  }
}
@-webkit-keyframes fadeIn {
  from {
    opacity: 0;
  }
  to {
    opacity: 1;
  }
}
/*properties of tooltip after "expand"*/
.bigtooltip {
  overflow: auto;
  height: 200px;
  -webkit-transition-property: height;
  -webkit-transition-duration: 500ms;
  -moz-transition-property: height;
  -moz-transition-duration: 500ms;
  transition-property: height;
  transition-duration: 500ms;
}
/*properties of tooltip before "expand"*/
.smalltooltip {
  -webkit-transition-property: height;
  -webkit-transition-duration: 500ms;
  -moz-transition-property: height;
  -moz-transition-duration: 500ms;
  transition-property: height;
  transition-duration: 500ms;
  text-overflow: ellipsis;
  overflow: hidden;
  height: 80px;
}
.tooltipbuttons {
  position: absolute;
  padding-right: 15px;
  top: 0px;
  right: 0px;
}
.tooltiptext {
  /*avoid the button to overlap on some docstring*/
  padding-right: 30px;
}
.ipython_tooltip {
  max-width: 700px;
  /*fade-in animation when inserted*/
  -webkit-animation: fadeOut 400ms;
  -moz-animation: fadeOut 400ms;
  animation: fadeOut 400ms;
  -webkit-animation: fadeIn 400ms;
  -moz-animation: fadeIn 400ms;
  animation: fadeIn 400ms;
  vertical-align: middle;
  background-color: #f7f7f7;
  overflow: visible;
  border: #ababab 1px solid;
  outline: none;
  padding: 3px;
  margin: 0px;
  padding-left: 7px;
  font-family: monospace;
  min-height: 50px;
  -moz-box-shadow: 0px 6px 10px -1px #adadad;
  -webkit-box-shadow: 0px 6px 10px -1px #adadad;
  box-shadow: 0px 6px 10px -1px #adadad;
  border-radius: 2px;
  position: absolute;
  z-index: 1000;
}
.ipython_tooltip a {
  float: right;
}
.ipython_tooltip .tooltiptext pre {
  border: 0;
  border-radius: 0;
  font-size: 100%;
  background-color: #f7f7f7;
}
.pretooltiparrow {
  left: 0px;
  margin: 0px;
  top: -16px;
  width: 40px;
  height: 16px;
  overflow: hidden;
  position: absolute;
}
.pretooltiparrow:before {
  background-color: #f7f7f7;
  border: 1px #ababab solid;
  z-index: 11;
  content: "";
  position: absolute;
  left: 15px;
  top: 10px;
  width: 25px;
  height: 25px;
  -webkit-transform: rotate(45deg);
  -moz-transform: rotate(45deg);
  -ms-transform: rotate(45deg);
  -o-transform: rotate(45deg);
}
ul.typeahead-list i {
  margin-left: -10px;
  width: 18px;
}
[dir="rtl"] ul.typeahead-list i {
  margin-left: 0;
  margin-right: -10px;
}
ul.typeahead-list {
  max-height: 80vh;
  overflow: auto;
}
ul.typeahead-list > li > a {
  /** Firefox bug **/
  /* see https://github.com/jupyter/notebook/issues/559 */
  white-space: normal;
}
ul.typeahead-list  > li > a.pull-right {
  float: left !important;
  float: left;
}
[dir="rtl"] .typeahead-list {
  text-align: right;
}
.cmd-palette .modal-body {
  padding: 7px;
}
.cmd-palette form {
  background: white;
}
.cmd-palette input {
  outline: none;
}
.no-shortcut {
  min-width: 20px;
  color: transparent;
}
[dir="rtl"] .no-shortcut.pull-right {
  float: left !important;
  float: left;
}
[dir="rtl"] .command-shortcut.pull-right {
  float: left !important;
  float: left;
}
.command-shortcut:before {
  content: "(command mode)";
  padding-right: 3px;
  color: #777777;
}
.edit-shortcut:before {
  content: "(edit)";
  padding-right: 3px;
  color: #777777;
}
[dir="rtl"] .edit-shortcut.pull-right {
  float: left !important;
  float: left;
}
#find-and-replace #replace-preview .match,
#find-and-replace #replace-preview .insert {
  background-color: #BBDEFB;
  border-color: #90CAF9;
  border-style: solid;
  border-width: 1px;
  border-radius: 0px;
}
[dir="ltr"] #find-and-replace .input-group-btn + .form-control {
  border-left: none;
}
[dir="rtl"] #find-and-replace .input-group-btn + .form-control {
  border-right: none;
}
#find-and-replace #replace-preview .replace .match {
  background-color: #FFCDD2;
  border-color: #EF9A9A;
  border-radius: 0px;
}
#find-and-replace #replace-preview .replace .insert {
  background-color: #C8E6C9;
  border-color: #A5D6A7;
  border-radius: 0px;
}
#find-and-replace #replace-preview {
  max-height: 60vh;
  overflow: auto;
}
#find-and-replace #replace-preview pre {
  padding: 5px 10px;
}
.terminal-app {
  background: #EEE;
}
.terminal-app #header {
  background: #fff;
  -webkit-box-shadow: 0px 0px 12px 1px rgba(87, 87, 87, 0.2);
  box-shadow: 0px 0px 12px 1px rgba(87, 87, 87, 0.2);
}
.terminal-app .terminal {
  width: 100%;
  float: left;
  font-family: monospace;
  color: white;
  background: black;
  padding: 0.4em;
  border-radius: 2px;
  -webkit-box-shadow: 0px 0px 12px 1px rgba(87, 87, 87, 0.4);
  box-shadow: 0px 0px 12px 1px rgba(87, 87, 87, 0.4);
}
.terminal-app .terminal,
.terminal-app .terminal dummy-screen {
  line-height: 1em;
  font-size: 14px;
}
.terminal-app .terminal .xterm-rows {
  padding: 10px;
}
.terminal-app .terminal-cursor {
  color: black;
  background: white;
}
.terminal-app #terminado-container {
  margin-top: 20px;
}
/*# sourceMappingURL=style.min.css.map */
    </style>
<style type="text/css">
    .highlight .hll { background-color: #ffffcc }
.highlight  { background: #f8f8f8; }
.highlight .c { color: #408080; font-style: italic } /* Comment */
.highlight .err { border: 1px solid #FF0000 } /* Error */
.highlight .k { color: #008000; font-weight: bold } /* Keyword */
.highlight .o { color: #666666 } /* Operator */
.highlight .ch { color: #408080; font-style: italic } /* Comment.Hashbang */
.highlight .cm { color: #408080; font-style: italic } /* Comment.Multiline */
.highlight .cp { color: #BC7A00 } /* Comment.Preproc */
.highlight .cpf { color: #408080; font-style: italic } /* Comment.PreprocFile */
.highlight .c1 { color: #408080; font-style: italic } /* Comment.Single */
.highlight .cs { color: #408080; font-style: italic } /* Comment.Special */
.highlight .gd { color: #A00000 } /* Generic.Deleted */
.highlight .ge { font-style: italic } /* Generic.Emph */
.highlight .gr { color: #FF0000 } /* Generic.Error */
.highlight .gh { color: #000080; font-weight: bold } /* Generic.Heading */
.highlight .gi { color: #00A000 } /* Generic.Inserted */
.highlight .go { color: #888888 } /* Generic.Output */
.highlight .gp { color: #000080; font-weight: bold } /* Generic.Prompt */
.highlight .gs { font-weight: bold } /* Generic.Strong */
.highlight .gu { color: #800080; font-weight: bold } /* Generic.Subheading */
.highlight .gt { color: #0044DD } /* Generic.Traceback */
.highlight .kc { color: #008000; font-weight: bold } /* Keyword.Constant */
.highlight .kd { color: #008000; font-weight: bold } /* Keyword.Declaration */
.highlight .kn { color: #008000; font-weight: bold } /* Keyword.Namespace */
.highlight .kp { color: #008000 } /* Keyword.Pseudo */
.highlight .kr { color: #008000; font-weight: bold } /* Keyword.Reserved */
.highlight .kt { color: #B00040 } /* Keyword.Type */
.highlight .m { color: #666666 } /* Literal.Number */
.highlight .s { color: #BA2121 } /* Literal.String */
.highlight .na { color: #7D9029 } /* Name.Attribute */
.highlight .nb { color: #008000 } /* Name.Builtin */
.highlight .nc { color: #0000FF; font-weight: bold } /* Name.Class */
.highlight .no { color: #880000 } /* Name.Constant */
.highlight .nd { color: #AA22FF } /* Name.Decorator */
.highlight .ni { color: #999999; font-weight: bold } /* Name.Entity */
.highlight .ne { color: #D2413A; font-weight: bold } /* Name.Exception */
.highlight .nf { color: #0000FF } /* Name.Function */
.highlight .nl { color: #A0A000 } /* Name.Label */
.highlight .nn { color: #0000FF; font-weight: bold } /* Name.Namespace */
.highlight .nt { color: #008000; font-weight: bold } /* Name.Tag */
.highlight .nv { color: #19177C } /* Name.Variable */
.highlight .ow { color: #AA22FF; font-weight: bold } /* Operator.Word */
.highlight .w { color: #bbbbbb } /* Text.Whitespace */
.highlight .mb { color: #666666 } /* Literal.Number.Bin */
.highlight .mf { color: #666666 } /* Literal.Number.Float */
.highlight .mh { color: #666666 } /* Literal.Number.Hex */
.highlight .mi { color: #666666 } /* Literal.Number.Integer */
.highlight .mo { color: #666666 } /* Literal.Number.Oct */
.highlight .sa { color: #BA2121 } /* Literal.String.Affix */
.highlight .sb { color: #BA2121 } /* Literal.String.Backtick */
.highlight .sc { color: #BA2121 } /* Literal.String.Char */
.highlight .dl { color: #BA2121 } /* Literal.String.Delimiter */
.highlight .sd { color: #BA2121; font-style: italic } /* Literal.String.Doc */
.highlight .s2 { color: #BA2121 } /* Literal.String.Double */
.highlight .se { color: #BB6622; font-weight: bold } /* Literal.String.Escape */
.highlight .sh { color: #BA2121 } /* Literal.String.Heredoc */
.highlight .si { color: #BB6688; font-weight: bold } /* Literal.String.Interpol */
.highlight .sx { color: #008000 } /* Literal.String.Other */
.highlight .sr { color: #BB6688 } /* Literal.String.Regex */
.highlight .s1 { color: #BA2121 } /* Literal.String.Single */
.highlight .ss { color: #19177C } /* Literal.String.Symbol */
.highlight .bp { color: #008000 } /* Name.Builtin.Pseudo */
.highlight .fm { color: #0000FF } /* Name.Function.Magic */
.highlight .vc { color: #19177C } /* Name.Variable.Class */
.highlight .vg { color: #19177C } /* Name.Variable.Global */
.highlight .vi { color: #19177C } /* Name.Variable.Instance */
.highlight .vm { color: #19177C } /* Name.Variable.Magic */
.highlight .il { color: #666666 } /* Literal.Number.Integer.Long */
    </style>
<style type="text/css">
    
/* Temporary definitions which will become obsolete with Notebook release 5.0 */
.ansi-black-fg { color: #3E424D; }
.ansi-black-bg { background-color: #3E424D; }
.ansi-black-intense-fg { color: #282C36; }
.ansi-black-intense-bg { background-color: #282C36; }
.ansi-red-fg { color: #E75C58; }
.ansi-red-bg { background-color: #E75C58; }
.ansi-red-intense-fg { color: #B22B31; }
.ansi-red-intense-bg { background-color: #B22B31; }
.ansi-green-fg { color: #00A250; }
.ansi-green-bg { background-color: #00A250; }
.ansi-green-intense-fg { color: #007427; }
.ansi-green-intense-bg { background-color: #007427; }
.ansi-yellow-fg { color: #DDB62B; }
.ansi-yellow-bg { background-color: #DDB62B; }
.ansi-yellow-intense-fg { color: #B27D12; }
.ansi-yellow-intense-bg { background-color: #B27D12; }
.ansi-blue-fg { color: #208FFB; }
.ansi-blue-bg { background-color: #208FFB; }
.ansi-blue-intense-fg { color: #0065CA; }
.ansi-blue-intense-bg { background-color: #0065CA; }
.ansi-magenta-fg { color: #D160C4; }
.ansi-magenta-bg { background-color: #D160C4; }
.ansi-magenta-intense-fg { color: #A03196; }
.ansi-magenta-intense-bg { background-color: #A03196; }
.ansi-cyan-fg { color: #60C6C8; }
.ansi-cyan-bg { background-color: #60C6C8; }
.ansi-cyan-intense-fg { color: #258F8F; }
.ansi-cyan-intense-bg { background-color: #258F8F; }
.ansi-white-fg { color: #C5C1B4; }
.ansi-white-bg { background-color: #C5C1B4; }
.ansi-white-intense-fg { color: #A1A6B2; }
.ansi-white-intense-bg { background-color: #A1A6B2; }

.ansi-bold { font-weight: bold; }

    </style>


<style type="text/css">
/* Overrides of notebook CSS for static HTML export */
body {
  overflow: visible;
  padding: 8px;
}

div#notebook {
  overflow: visible;
  border-top: none;
}@media print {
  div.cell {
    display: block;
    page-break-inside: avoid;
  } 
  div.output_wrapper { 
    display: block;
    page-break-inside: avoid; 
  }
  div.output { 
    display: block;
    page-break-inside: avoid; 
  }
}
</style>

<!-- Custom stylesheet, it must be in the same directory as the html file -->
<link rel="stylesheet" href="custom.css">

<!-- Loading mathjax macro -->
<!-- Load mathjax -->
    <script src="https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.1/MathJax.js?config=TeX-AMS_HTML"></script>
    <!-- MathJax configuration -->
    <script type="text/x-mathjax-config">
    MathJax.Hub.Config({
        tex2jax: {
            inlineMath: [ ['$','$'], ["\\(","\\)"] ],
            displayMath: [ ['$$','$$'], ["\\[","\\]"] ],
            processEscapes: true,
            processEnvironments: true
        },
        // Center justify equations in code and markdown cells. Elsewhere
        // we use CSS to left justify single line equations in code cells.
        displayAlign: 'center',
        "HTML-CSS": {
            styles: {'.MathJax_Display': {"margin": 0}},
            linebreaks: { automatic: true }
        }
    });
    </script>
    <!-- End of mathjax configuration --></head>
<body>
  <div tabindex="-1" id="notebook" class="border-box-sizing">
    <div class="container" id="notebook-container">

<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<hr>
<h2 id="Universidad-de-Costa-Rica">Universidad de Costa Rica<a class="anchor-link" href="#Universidad-de-Costa-Rica">&#182;</a></h2><h3 id="Escuela-de-Ingenier&#237;a-El&#233;ctrica">Escuela de Ingenier&#237;a El&#233;ctrica<a class="anchor-link" href="#Escuela-de-Ingenier&#237;a-El&#233;ctrica">&#182;</a></h3><h4 id="IE0405---Modelos-Probabil&#237;sticos-de-Se&#241;ales-y-Sistemas">IE0405 - Modelos Probabil&#237;sticos de Se&#241;ales y Sistemas<a class="anchor-link" href="#IE0405---Modelos-Probabil&#237;sticos-de-Se&#241;ales-y-Sistemas">&#182;</a></h4><hr>
<ul>
<li>Estudiante: <strong>Adonay Juárez Moraga</strong></li>
<li>Carné: <strong>B74047</strong></li>
<li>Grupo: <strong>1-2</strong></li>
<li>Estudiante: <strong>Gloriana Mejías Segura</strong></li>
<li>Carné: <strong>B74636</strong></li>
<li>Grupo: <strong>1-2</strong></li>
<li>Estudiante: <strong>Jose Adrián Blanco Sánchez</strong></li>
<li>Carné: <strong>B81161</strong></li>
<li>Grupo: <strong>1-2</strong></li>
</ul>
<hr>
<h1 id="P4---Modulaci&#243;n-digital-IQ"><code>P4</code> - <em>Modulaci&#243;n digital IQ</em><a class="anchor-link" href="#P4---Modulaci&#243;n-digital-IQ">&#182;</a></h1><blockquote><p>La modulación digital es una de las aplicaciones del análisis de procesos estocásticos, y es parte de los sistemas digitales de comunicación. Este proyecto presenta una introdución a tópicos fundamentales de la ingeniería de comunicaciones para simular un sistema de transmisión de imágenes de baja resolución.</p>
</blockquote>
<hr>
<ul>
<li>Elaboración de nota teórica y demostración: <strong>Jeaustin Sirias Chacón</strong>, como parte de IE0499 - Proyecto Eléctrico: <em>Estudio y simulación de aplicaciones de la teoría de probabilidad en la ingeniería eléctrica</em>.</li>
<li>Revisión y edición: <strong>Fabián Abarca Calderón</strong></li>
</ul>

</div>
</div>
</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<p><span id="Chapter1"></span></p>
<h2 id="1.---Una-introducci&#243;n-a-los-sistemas-de-comunicaciones">1. - Una introducci&#243;n a los sistemas de comunicaciones<a class="anchor-link" href="#1.---Una-introducci&#243;n-a-los-sistemas-de-comunicaciones">&#182;</a></h2><p>La ingeniería de comunicaciones es la rama de la ciencia y la tecnología que busca establecer sistemas de transmisión de información entre emisores y receptores separados espacial o temporalmente.</p>
<p>El modelo más generalizado de un sistema de comunicaciones incluye una fuente de información, un transmisor que codifica la información, un esquema de modulación que adapta la señal al medio, un canal de transmisión, un receptor que decodifica la información y un destino. El siguiente es un ejemplo de envío de imágenes:</p>
<p><img align='center' src='https://i.imgur.com/ZqQ9Psh.png' width ='450'/></p>
<p>Un sistema de comunicaciones completo implica etapas altamente complejas y detalladas, tales como la multiplexación de múltiples usuarios, compresión de la información, así como corrección de datos erróneos. En esta actividad se estudiará solamente <strong>los esquemas de modulación digital y el canal ruidoso</strong>, que corresponde a dos de las etapas más relevantes.</p>

</div>
</div>
</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h3 id="1.1.---La-modulaci&#243;n-digital">1.1. - La modulaci&#243;n digital<a class="anchor-link" href="#1.1.---La-modulaci&#243;n-digital">&#182;</a></h3><p>Supóngase, por ejemplo, la tramisión inalámbrica de una imagen a largas distancias, ¿cómo es posible enviar sus pixeles (que se asumen como "algo digital") de un punto a otro, a través de un medio físico que es esencialmente "analógico"?</p>
<p>La <em>modulación</em> en ingeniería de comunicaciones consiste en depositar la información de una <strong>señal moduladora</strong> (fuente de información) en una <strong>señal portadora</strong> que está diseñada para el medio físico de transmisión. En el caso específico de la modulación <em>digital</em>, la fuente de información es, precisamente, <em>digital</em> (discreta en el tiempo y la amplitud).</p>
<p><img align='center' src='https://i.imgur.com/eVnhbbG.png' width ='400'/></p>
<p>La modulación sirve dos propósitos importantes:</p>
<ul>
<li>La señal portadora está <strong>adaptada al medio</strong> por el que se va a transmitir o a las tecnologías que se utilizan para ello. Por ejemplo: una señal de audio, en sus frecuencias originales, no puede ser transmitida eficientemente con antenas pequeñas y portables. Otro ejemplo: las señales digitales cuadradas (transiciones entre 0 y 1) sufrirían graves distorsiones y atenuación si se transmiten tal cual a grandes distancias por un conductor eléctrico.</li>
<li>Como la señal portadora puede modificarse a conveniencia, es posible crear esquemas de <strong>acceso al medio</strong> para múltiples usuarios. Por ejemplo: la modulación FM (<em>frequency modulation</em>) utiliza distintas franjas del espectro radioeléctrico para acomodar distintas emisiones ("radioemisoras").</li>
</ul>
<p>La modulación digital presenta ventajas adicionales:</p>
<ul>
<li>Un esquema de modulación con técnicas de codificación apropiadas es capaz de reconstruir señales distorsionadas.</li>
<li>El flujo de información (bits por unidad de tiempo) es adaptativo, según las condiciones del canal.</li>
</ul>

</div>
</div>
</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h3 id="1.2.---La-demodulaci&#243;n">1.2. - La demodulaci&#243;n<a class="anchor-link" href="#1.2.---La-demodulaci&#243;n">&#182;</a></h3><p>Si una señal ha atravesado un canal físico y se encuentra en el receptor: <em>¿cómo pueden los bits ser reconstruidos nuevamente a partir de la señal modulada $s(t)$ que fue recibida?</em>, <em>¿qué ocurrirá si esta señal fue distorsionada por cierto ruido durante su travesía por el medio de transmisión?</em> Estas son preguntas claves para el diseño de sistema de comunicación.</p>
<p>Algunas de las técnicas de procesamiento de señales para extraer la información de la señal son:</p>
<ul>
<li>Demodulación por <strong>detección de envolvente</strong></li>
<li>Demodulación por <strong>detección de energía</strong></li>
<li>Demodulación por <strong>mínima distancia euclidiana</strong></li>
<li>Demodulación por <strong>detección de lazo de seguimiento de fase</strong></li>
<li>Demodulación por <strong>detección de fuerza en recepción</strong></li>
</ul>
<h3 id="1.3.---Sobre-canales-ruidosos">1.3. - Sobre canales ruidosos<a class="anchor-link" href="#1.3.---Sobre-canales-ruidosos">&#182;</a></h3><blockquote><p>El ruido en un medio de transmisión generalmente se debe a variables físicas de comportamiento aleatorio. Por ejemplo: los fenómenos atmosféricos, las vibraciones, la interferencia entre señales y la temperatura.</p>
</blockquote>
<p>En particular, los sistemas eléctricos y electrónicos son comúnmente afectados por el denominado <strong>ruido aditivo blanco gaussiano</strong> (AWGN, por las siglas en inglés de <em>Additive White Gaussian Noise</em>).</p>
<ul>
<li>Es <strong>aditivo</strong> porque la perturbación se "adhiere" o se "suma" a la señal viajera $s(t)$ al atravesar un determinado canal. De forma genérica, la señal resultante es la original más ruido, es decir, $\hat{s}(t) = s(t) + n(t)$.</li>
<li>Es <strong>blanco</strong> porque tiene una <a href="https://es.wikipedia.org/wiki/Densidad_espectral">densidad espectral de potencia</a> aproximadamente constante dentro del ancho de banda de interés, es decir, está presente en todos los componentes de frecuencia. ¿Por qué entonces "blanco"?, podrían preguntarse ustedes.</li>
<li>Es <strong>gaussiano</strong> porque la función de densidad probabilística (PDF) de la <strong>amplitud</strong> del ruido es precisamente una distribución normal, con parámetros tales que la media es típicamente cero (lo que implica que tiene valores positivos y negativos) y la varianza tiene un valor relacionado con la potencia del ruido.</li>
</ul>
<p><img align='center' src='https://i.imgur.com/gtiM5SJ.png' width='850'/></p>

</div>
</div>
</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h3 id="1.4----La-relaci&#243;n-se&#241;al-a-ruido">1.4 -  La relaci&#243;n se&#241;al-a-ruido<a class="anchor-link" href="#1.4----La-relaci&#243;n-se&#241;al-a-ruido">&#182;</a></h3><p>La relación señal-a-ruido (<strong>SNR</strong>, <em>Signal-to-Noise Ratio</em>) es una medida de la proporción entre la potencia $P_s$ de una señal $s(t)$ y la potencia $P_n$ del ruido $n(t)$ que la corrompe. Su magnitud suele ser especificada en decibel (dB). Un SNR alto indica que la presencia de una señal es más fuerte que la presencia del ruido, mientras que un SNR bajo indica lo contrario. Por ejemplo: el audio de un disco de vinilo tiene un SNR de unos 60 dB mientras que un disco compacto tiene 90 dB.</p>
<p>Su relación se expresa de la siguiente manera:</p>
$$
\mathrm{SNR}_{\mathrm{dB}} = 10\log(\mathrm{SNR}) = 10\log\left ( \frac{P_s}{P_n} \right )
$$<p>Dado lo anterior, 60 dB implica una señal un millón de veces más potente que el ruido, y 90 dB mil millones de veces más grande. Hay que notar en el caso del audio que la percepción humana de la audición no es lineal, y por eso se prefiere una medida logarítmica como el dB.</p>
<h3 id="1.5---Tasa-de-error-binario">1.5 - Tasa de error binario<a class="anchor-link" href="#1.5---Tasa-de-error-binario">&#182;</a></h3><p>La tasa de error de bit (<strong>BER</strong>, <em>Bit Error Rate</em>) es una medida del error $p(\epsilon)$ que contiene un medio de transmisión no ideal (ruidoso). Según la definición estadística de la probabilidad, la probabilidad de ocurrencia de un suceso es la razón de los casos favorables entre los casos posibles:</p>
$$
\displaystyle
p(\epsilon) = \frac{\text{bits fallidos}}{\text{bit totales}}
$$<p>En sistemas de comunicaciones usuales, las tasas de error aceptables son de $10^{-5}$ o menores (un error por cada cien mil bits).</p>

</div>
</div>
</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<hr>
<h2 id="2.---Conceptos-b&#225;sicos-del-procesamiento-de-im&#225;genes">2. - Conceptos b&#225;sicos del procesamiento de im&#225;genes<a class="anchor-link" href="#2.---Conceptos-b&#225;sicos-del-procesamiento-de-im&#225;genes">&#182;</a></h2><h3 id="2.1---Los-p&#237;xeles">2.1 - Los p&#237;xeles<a class="anchor-link" href="#2.1---Los-p&#237;xeles">&#182;</a></h3><p>Una imagen digital es un conjunto de pixeles (unidad mínima de color) en un plano. La sinergia de sus colores permite visualizar una imagen con sentido para el ojo humano.</p>
<p><img align='center' src='https://i.imgur.com/ohBErgV.jpg' width='350'/></p>
<h3 id="2.2---El-modelo-de-colores-RGB">2.2 - El modelo de colores <em>RGB</em><a class="anchor-link" href="#2.2---El-modelo-de-colores-RGB">&#182;</a></h3><p>El modelo RGB (por las siglas en inglés de <em>Red, Green, Blue</em>) es el esquema de colores digitales más tradicional. Es "aditivo" en el sentido de que los colores se forman por la combinación de los componentes R, G, y B. Algunos ejemplos son:</p>
<table>
<thead><tr>
<th>Color</th>
<th>Tripleta RGB</th>
</tr>
</thead>
<tbody>
<tr>
<td><img src="https://i.pinimg.com/564x/2c/c6/2e/2cc62efc5998bc3bfdec089acf1e12c4.jpg" width="30"></img></td>
<td><code>(255, 0, 0)</code></td>
</tr>
<tr>
<td><img src="https://i.pinimg.com/564x/ad/2f/b5/ad2fb5dd9b658483cb5c4f6120fe528b.jpg" width="30"></img></td>
<td><code>(0, 0, 255)</code></td>
</tr>
<tr>
<td><img src="https://i.pinimg.com/564x/26/8b/2c/268b2c4f2742bfdc73dfbc8154ef5d11.jpg" width="30"></img></td>
<td><code>(0, 0, 255)</code></td>
</tr>
<tr>
<td><img src="https://i.pinimg.com/564x/e5/be/78/e5be78c8312fd6ce650408abb87bd0ce.jpg" width="30"></img></td>
<td><code>(0, 0, 0)</code></td>
</tr>
<tr>
<td><img src="https://i.pinimg.com/564x/a2/73/09/a27309683bfcaaf152864a0e19e79fd9.jpg" width="30"></img></td>
<td><code>(0, 0, 128)</code></td>
</tr>
</tbody>
</table>
<p>A cada color se le denomina <strong>canal</strong>, de forma que un pixel RGB tiene tres canales. El modelo RGB es un esquema de colores discreto: cada canal tiene un rango de libertad entre 0 y 255, es decir, 256 tonos posibles por canal. La cantidad de memoria necesaria para almacenar un canal es de 8 bits, lo que significa que un pixel RGB tiene 8 $\times$ 3 = 24 bits. De aquí viene el comentario "<em>este televisor tiene 16 millones de colores, las imágenes se verán buenísimas</em>", un número obtenido por la regla de la multiplicación:</p>
$$
256 \times 256 \times 256 = 2^{24} = 16\,777\,216 \,\text{combinaciones de colores}
$$<h3 id="2.3---El-formato-de-compresi&#243;n-de-im&#225;genes-JPG">2.3 - El formato de compresi&#243;n de im&#225;genes <em>JPG</em><a class="anchor-link" href="#2.3---El-formato-de-compresi&#243;n-de-im&#225;genes-JPG">&#182;</a></h3><p>Las imágenes digitales con formato JPG poseen un modelo de colores <strong>RGB</strong> y se trata de un "formato con compresión", en el que la imagen ha sido sometida a un proceso de reducción de información redundante para "aligerar" su peso en memoria.</p>
<p>Por ejemplo, la imagen mostrada anteriormente es de 198 $\times$ 89 pixeles, lo que implicaría un tamaño total de 198 $\times$ 89 $\times$ 24 bit / 8 = 52,87 kB, sin embargo el tamaño del archivo de la compresión es de solamente 8,58 kB. El nivel de compresión depende de cada imagen, pero alcanza típicamente la relación 10:1.</p>

</div>
</div>
</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<hr>
<h2 id="3.---Simulando-un-sistema-de-comunicaciones">3. - Simulando un sistema de comunicaciones<a class="anchor-link" href="#3.---Simulando-un-sistema-de-comunicaciones">&#182;</a></h2><p>Para utilizar los conocimientos adquiridos, se procederá a simular un <strong>sistema de comunicaciones para la transmisión de imágenes de baja resolución</strong>.</p>
<p>El objetivo es transmitir la siguiente imagen (o cualquiera de baja resolución de su elección):</p>
<p><img align='center' src='https://i.imgur.com/ohBErgV.jpg' width='250'/></p>
<p>Las condiciones iniciales para el sistema de comunicaciones serán las siguientes:</p>
<ul>
<li>Una onda portadora banda base con <strong>frecuencia $f_s$ = 5 kHz.</strong></li>
<li>Una frecuencia de muestreo de <strong>20 muestras por período</strong>.</li>
<li>Una relación señal/ruido de <strong>5 dB</strong>.</li>
</ul>
<h3 id="3.1.---Funciones-implementadas">3.1. - Funciones implementadas<a class="anchor-link" href="#3.1.---Funciones-implementadas">&#182;</a></h3><p>A continuación se especificarán las funciones desarrolladas en la simulación del sistema (considerar que en telecomunicaciones se utiliza <strong>Tx</strong> para referirse a transmisión y <strong>Rx</strong> a recepción):</p>
<ol>
<li><code>fuente_info(imagen)</code>: Extrae en un <code>array</code> de NumPy los pixeles contenidos en la imagen.</li>
</ol>
<ul>
<li><code>rgb_a_bit(vector_pixel)</code>: Convierte los pixeles del 'array' de NumPy en una cadena <code>bits_Tx</code> continua de tamaño $(1 \times k)$, en donde $k$ es la cantidad total de bits de la imagen.</li>
<li><code>modulador(bits_Rx, FS, MPP)</code>: Convierte la señal de información (arreglo de <code>bits_Tx</code>) en una señal modulada bajo un esquema <strong>BPSK</strong>.</li>
<li><code>canal_ruidoso(senal_Tx, Pm, SNR)</code>: Simula un canala ruidoso con <strong>AWGN</strong> para <code>senal_Tx</code>.</li>
<li><code>demodulador(senal_Rx, carrier, MPP)</code>: Demodula a <code>senal_Rx</code> (señal recibida) y determina los bits recibidos usando el criterio de demodulación por detección de energía.</li>
<li><code>bits_a_rgb(bits_Rx, dims)</code>: Reconstruye los bits recibidos en <code>bits_Rx</code> en una imagen.</li>
</ul>
<p>Las bibliotecas de Python de interés para este proyecto son:</p>
<div class="highlight"><pre><span></span><span class="c1"># Para manipular imágenes (Python Imaging Library)</span>
<span class="kn">from</span> <span class="nn">PIL</span> <span class="kn">import</span> <span class="n">Image</span>

<span class="c1"># Para manipular &#39;arrays&#39; de pixeles y bits, señales y operaciones</span>
<span class="kn">import</span> <span class="nn">numpy</span> <span class="kn">as</span> <span class="nn">np</span>

<span class="c1"># Para visualizar imágenes y señales</span>
<span class="kn">import</span> <span class="nn">matplotlib.pyplot</span> <span class="kn">as</span> <span class="nn">plt</span>

<span class="c1"># Para medir el tiempo de simulación</span>
<span class="kn">import</span> <span class="nn">time</span>
</pre></div>

</div>
</div>
</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h4 id="3.1.1---Extracci&#243;n-de-los-pixeles-de-una-imagen-(fuente-de-informaci&#243;n)">3.1.1 - Extracci&#243;n de los pixeles de una imagen (fuente de informaci&#243;n)<a class="anchor-link" href="#3.1.1---Extracci&#243;n-de-los-pixeles-de-una-imagen-(fuente-de-informaci&#243;n)">&#182;</a></h4>
</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[16]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="kn">from</span> <span class="nn">PIL</span> <span class="k">import</span> <span class="n">Image</span>
<span class="kn">import</span> <span class="nn">numpy</span> <span class="k">as</span> <span class="nn">np</span>

<span class="k">def</span> <span class="nf">fuente_info</span><span class="p">(</span><span class="n">imagen</span><span class="p">):</span>
    <span class="sd">&#39;&#39;&#39;Una función que simula una fuente de</span>
<span class="sd">    información al importar una imagen y </span>
<span class="sd">    retornar un vector de NumPy con las </span>
<span class="sd">    dimensiones de la imagen, incluidos los</span>
<span class="sd">    canales RGB: alto x largo x 3 canales</span>

<span class="sd">    :param imagen: Una imagen en formato JPG</span>
<span class="sd">    :return: un vector de pixeles</span>
<span class="sd">    &#39;&#39;&#39;</span>
    <span class="n">img</span> <span class="o">=</span> <span class="n">Image</span><span class="o">.</span><span class="n">open</span><span class="p">(</span><span class="n">imagen</span><span class="p">)</span>
    
    <span class="k">return</span> <span class="n">np</span><span class="o">.</span><span class="n">array</span><span class="p">(</span><span class="n">img</span><span class="p">)</span>
</pre></div>

    </div>
</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<p>Es relevante considerar la forma de la salida de la función anterior.</p>
<div class="highlight"><pre><span></span><span class="o">&gt;&gt;&gt;</span> <span class="n">pixeles</span> <span class="o">=</span> <span class="n">fuente_info</span><span class="p">(</span><span class="s1">&#39;imagen.jpg&#39;</span><span class="p">)</span>
<span class="o">&gt;&gt;&gt;</span> <span class="k">print</span><span class="p">(</span><span class="s1">&#39;Dimensiones: &#39;</span><span class="p">,</span> <span class="n">pixeles</span><span class="o">.</span><span class="n">shape</span><span class="p">,</span> <span class="s1">&#39;</span><span class="se">\n</span><span class="s1">&#39;</span><span class="p">)</span>
<span class="o">&gt;&gt;&gt;</span> <span class="k">print</span><span class="p">(</span><span class="n">pixeles</span><span class="p">)</span>

<span class="n">Dimensiones</span><span class="p">:</span> <span class="p">(</span><span class="mi">300</span><span class="p">,</span> <span class="mi">300</span><span class="p">,</span> <span class="mi">3</span><span class="p">)</span>

<span class="p">[[[</span><span class="mi">132</span> <span class="mi">123</span> <span class="mi">118</span><span class="p">]</span>
  <span class="p">[</span><span class="mi">133</span> <span class="mi">124</span> <span class="mi">119</span><span class="p">]</span>
  <span class="p">[</span><span class="mi">136</span> <span class="mi">127</span> <span class="mi">122</span><span class="p">]</span>
  <span class="o">...</span>
  <span class="p">[</span>  <span class="mi">8</span>   <span class="mi">2</span>   <span class="mi">2</span><span class="p">]</span>
  <span class="p">[</span> <span class="mi">10</span>   <span class="mi">1</span>   <span class="mi">4</span><span class="p">]</span>
  <span class="p">[</span> <span class="mi">10</span>   <span class="mi">1</span>   <span class="mi">2</span><span class="p">]]</span>

 <span class="p">[[</span><span class="mi">143</span> <span class="mi">134</span> <span class="mi">129</span><span class="p">]</span>
  <span class="p">[</span><span class="mi">145</span> <span class="mi">136</span> <span class="mi">131</span><span class="p">]</span>
  <span class="p">[</span><span class="mi">144</span> <span class="mi">135</span> <span class="mi">130</span><span class="p">]</span>
  <span class="o">...</span>
  <span class="p">[</span> <span class="mi">13</span>   <span class="mi">3</span>   <span class="mi">1</span><span class="p">]</span>
  <span class="p">[</span> <span class="mi">15</span>   <span class="mi">5</span>   <span class="mi">3</span><span class="p">]</span>
  <span class="p">[</span> <span class="mi">15</span>   <span class="mi">7</span>   <span class="mi">5</span><span class="p">]]]</span>
</pre></div>
<ul>
<li>Las dimensiones de la imagen elegida son (300, 300, 3); esto es su resolución: 300 px $\times$ 300 px. </li>
<li>La tercera entrada del vector de dimensiones se refiere a las tres "capas" o canales R, G y B que componen aditivamente cada uno de los pixeles de esta imagen. </li>
<li>En este caso específico hay $300 \times 300 = 90\,000$ pixeles por canal. </li>
<li>¿Puede estimarse cuántos bits tiene la imagen? Puesto que un solo canal tiene 8 bits de profundidad (256 niveles) por pixel, entonces la imagen en transmisión tiene, <em>antes de la compresión</em>:</li>
</ul>
$$
90\,000 \times 8 \times 3 = 2\,160\,000 \,\text{bit}
$$
</div>
</div>
</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h4 id="3.1.2.---Codificaci&#243;n-de-pixeles-a-una-base-binaria-(bits)">3.1.2. - Codificaci&#243;n de pixeles a una base binaria (bits)<a class="anchor-link" href="#3.1.2.---Codificaci&#243;n-de-pixeles-a-una-base-binaria-(bits)">&#182;</a></h4>
</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[17]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="kn">import</span> <span class="nn">numpy</span> <span class="k">as</span> <span class="nn">np</span>

<span class="k">def</span> <span class="nf">rgb_a_bit</span><span class="p">(</span><span class="n">array_imagen</span><span class="p">):</span>
    <span class="sd">&#39;&#39;&#39;Convierte los pixeles de base </span>
<span class="sd">    decimal (de 0 a 255) a binaria </span>
<span class="sd">    (de 00000000 a 11111111).</span>

<span class="sd">    :param imagen: array de una imagen </span>
<span class="sd">    :return: Un vector de (1 x k) bits &#39;int&#39;</span>
<span class="sd">    &#39;&#39;&#39;</span>
    <span class="c1"># Obtener las dimensiones de la imagen</span>
    <span class="n">x</span><span class="p">,</span> <span class="n">y</span><span class="p">,</span> <span class="n">z</span> <span class="o">=</span> <span class="n">array_imagen</span><span class="o">.</span><span class="n">shape</span>
    
    <span class="c1"># Número total de elementos (pixeles x canales)</span>
    <span class="n">n_elementos</span> <span class="o">=</span> <span class="n">x</span> <span class="o">*</span> <span class="n">y</span> <span class="o">*</span> <span class="n">z</span>

    <span class="c1"># Convertir la imagen a un vector unidimensional de n_elementos</span>
    <span class="n">pixeles</span> <span class="o">=</span> <span class="n">np</span><span class="o">.</span><span class="n">reshape</span><span class="p">(</span><span class="n">array_imagen</span><span class="p">,</span> <span class="n">n_elementos</span><span class="p">)</span>

    <span class="c1"># Convertir los canales a base 2</span>
    <span class="n">bits</span> <span class="o">=</span> <span class="p">[</span><span class="nb">format</span><span class="p">(</span><span class="n">pixel</span><span class="p">,</span> <span class="s1">&#39;08b&#39;</span><span class="p">)</span> <span class="k">for</span> <span class="n">pixel</span> <span class="ow">in</span> <span class="n">pixeles</span><span class="p">]</span>
    <span class="n">bits_Rx</span> <span class="o">=</span> <span class="n">np</span><span class="o">.</span><span class="n">array</span><span class="p">(</span><span class="nb">list</span><span class="p">(</span><span class="s1">&#39;&#39;</span><span class="o">.</span><span class="n">join</span><span class="p">(</span><span class="n">bits</span><span class="p">)))</span>
    
    <span class="k">return</span> <span class="n">bits_Rx</span><span class="o">.</span><span class="n">astype</span><span class="p">(</span><span class="nb">int</span><span class="p">)</span>
</pre></div>

    </div>
</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h4 id="3.1.3.---Esquema-de-modulaci&#243;n-BPSK">3.1.3. - Esquema de modulaci&#243;n BPSK<a class="anchor-link" href="#3.1.3.---Esquema-de-modulaci&#243;n-BPSK">&#182;</a></h4><p>El esquema de modulación o "codificación" por desplazamiento de fase o <a href="https://es.wikipedia.org/wiki/Modulaci%C3%B3n_por_desplazamiento_de_fase">PSK</a> (de <em>phase shift keying</em>) consiste, como lo sugiere su nombre, en <strong>variar la fase</strong> de la onda portadora $c(t)$ a partir grupos de bits codificados en símbolos discretos. El caso <strong>BPSK</strong> hace referencia a la modulación bi-fase, con dos símbolos disponibles. En general hay $M = 2^k$ símbolos, con $k$ la cantidad de bits para representarlos. Por tanto, con BPSK y despejando para $k$ con $M = 2$:</p>
$$
\log_2(2) = 1 \quad \text{bit/símbolo}
$$<p>Puede haber un <code>0</code> o un <code>1</code> por cada símbolo. Puesto que el esquema se basa en el desplazamiento de fase entonces es conveniente asignar valores angulares de fase en radianes, como 0 y $\pi$:</p>
$$
s(t) = A_c \cdot \sin(2\pi f_c t - \theta_c), \quad \text{con}\, \theta_c \in \{0, \pi\}
$$<p>Por la identidad trigonométrica $\sin(\alpha - \pi) = \sin(-\alpha) = -\sin(\alpha)$, implícitamente $s(t)$ puede manipular su desplazamiento de fase desde la óptica de la amplitud $A_c$:</p>
$$
A_c= 
\begin{cases}
             1, &amp;   \text{si} \quad \theta_c = 0 \\
             -1, &amp;  \text{si} \quad \theta_c = \pi \\
\end{cases}
$$<p>A través de este "artificio" la modulación <strong>BPSK</strong> (pero solo BPSK) pasa de ser un asunto de fases a un tema de amplitud. Esto simplifica en gran medida la programación del esquema, puesto que si el bit entrante es cero, entonces la fase de la portadora se invierte con solo tomar $A_c = -1$. En el caso contrario (si el bit entrante es un uno), entonces $A_c = 1$ y ya no es necesario lidiar con las fases en términos del ángulo $\theta_c$. A continuación se muestra una implementación de esta modulación.</p>

</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[18]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="kn">import</span> <span class="nn">numpy</span> <span class="k">as</span> <span class="nn">np</span>

<span class="k">def</span> <span class="nf">modulador</span><span class="p">(</span><span class="n">bits</span><span class="p">,</span> <span class="n">fc</span><span class="p">,</span> <span class="n">mpp</span><span class="p">):</span>
    <span class="sd">&#39;&#39;&#39;Un método que simula el esquema de </span>
<span class="sd">    modulación digital BPSK.</span>

<span class="sd">    :param bits: Vector unidimensional de bits</span>
<span class="sd">    :param fc: Frecuencia de la portadora en Hz</span>
<span class="sd">    :param mpp: Cantidad de muestras por periodo de onda portadora</span>
<span class="sd">    :return: Un vector con la señal modulada</span>
<span class="sd">    :return: Un valor con la potencia promedio [W]</span>
<span class="sd">    :return: La onda portadora c(t)</span>
<span class="sd">    :return: La onda cuadrada moduladora (información)</span>
<span class="sd">    &#39;&#39;&#39;</span>
    <span class="c1"># 1. Parámetros de la &#39;señal&#39; de información (bits)</span>
    <span class="n">N</span> <span class="o">=</span> <span class="nb">len</span><span class="p">(</span><span class="n">bits</span><span class="p">)</span> <span class="c1"># Cantidad de bits</span>

    <span class="c1"># 2. Construyendo un periodo de la señal portadora c(t)</span>
    <span class="n">Tc</span> <span class="o">=</span> <span class="mi">1</span> <span class="o">/</span> <span class="n">fc</span>  <span class="c1"># periodo [s]</span>
    <span class="n">t_periodo</span> <span class="o">=</span> <span class="n">np</span><span class="o">.</span><span class="n">linspace</span><span class="p">(</span><span class="mi">0</span><span class="p">,</span> <span class="n">Tc</span><span class="p">,</span> <span class="n">mpp</span><span class="p">)</span>  <span class="c1"># mpp: muestras por período</span>
    <span class="n">portadora</span> <span class="o">=</span> <span class="n">np</span><span class="o">.</span><span class="n">sin</span><span class="p">(</span><span class="mi">2</span><span class="o">*</span><span class="n">np</span><span class="o">.</span><span class="n">pi</span><span class="o">*</span><span class="n">fc</span><span class="o">*</span><span class="n">t_periodo</span><span class="p">)</span>

    <span class="c1"># 3. Inicializar la señal modulada s(t)</span>
    <span class="n">t_simulacion</span> <span class="o">=</span> <span class="n">np</span><span class="o">.</span><span class="n">linspace</span><span class="p">(</span><span class="mi">0</span><span class="p">,</span> <span class="n">N</span><span class="o">*</span><span class="n">Tc</span><span class="p">,</span> <span class="n">N</span><span class="o">*</span><span class="n">mpp</span><span class="p">)</span> 
    <span class="n">senal_Tx</span> <span class="o">=</span> <span class="n">np</span><span class="o">.</span><span class="n">zeros</span><span class="p">(</span><span class="n">t_simulacion</span><span class="o">.</span><span class="n">shape</span><span class="p">)</span>
    <span class="n">moduladora</span> <span class="o">=</span> <span class="n">np</span><span class="o">.</span><span class="n">zeros</span><span class="p">(</span><span class="n">t_simulacion</span><span class="o">.</span><span class="n">shape</span><span class="p">)</span>  <span class="c1"># (opcional) señal de bits</span>
 
    <span class="c1"># 4. Asignar las formas de onda según los bits (BPSK)</span>
    <span class="k">for</span> <span class="n">i</span><span class="p">,</span> <span class="n">bit</span> <span class="ow">in</span> <span class="nb">enumerate</span><span class="p">(</span><span class="n">bits</span><span class="p">):</span>
        <span class="k">if</span> <span class="n">bit</span> <span class="o">==</span> <span class="mi">1</span><span class="p">:</span>
            <span class="n">senal_Tx</span><span class="p">[</span><span class="n">i</span><span class="o">*</span><span class="n">mpp</span> <span class="p">:</span> <span class="p">(</span><span class="n">i</span><span class="o">+</span><span class="mi">1</span><span class="p">)</span><span class="o">*</span><span class="n">mpp</span><span class="p">]</span> <span class="o">=</span> <span class="n">portadora</span>
            <span class="n">moduladora</span><span class="p">[</span><span class="n">i</span><span class="o">*</span><span class="n">mpp</span> <span class="p">:</span> <span class="p">(</span><span class="n">i</span><span class="o">+</span><span class="mi">1</span><span class="p">)</span><span class="o">*</span><span class="n">mpp</span><span class="p">]</span> <span class="o">=</span> <span class="mi">1</span>
        <span class="k">else</span><span class="p">:</span>
            <span class="n">senal_Tx</span><span class="p">[</span><span class="n">i</span><span class="o">*</span><span class="n">mpp</span> <span class="p">:</span> <span class="p">(</span><span class="n">i</span><span class="o">+</span><span class="mi">1</span><span class="p">)</span><span class="o">*</span><span class="n">mpp</span><span class="p">]</span> <span class="o">=</span> <span class="n">portadora</span> <span class="o">*</span> <span class="o">-</span><span class="mi">1</span>
            <span class="n">moduladora</span><span class="p">[</span><span class="n">i</span><span class="o">*</span><span class="n">mpp</span> <span class="p">:</span> <span class="p">(</span><span class="n">i</span><span class="o">+</span><span class="mi">1</span><span class="p">)</span><span class="o">*</span><span class="n">mpp</span><span class="p">]</span> <span class="o">=</span> <span class="mi">0</span>
    
    <span class="c1"># 5. Calcular la potencia promedio de la señal modulada</span>
    <span class="n">P_senal_Tx</span> <span class="o">=</span> <span class="p">(</span><span class="mi">1</span> <span class="o">/</span> <span class="p">(</span><span class="n">N</span><span class="o">*</span><span class="n">Tc</span><span class="p">))</span> <span class="o">*</span> <span class="n">np</span><span class="o">.</span><span class="n">trapz</span><span class="p">(</span><span class="nb">pow</span><span class="p">(</span><span class="n">senal_Tx</span><span class="p">,</span> <span class="mi">2</span><span class="p">),</span> <span class="n">t_simulacion</span><span class="p">)</span>
    
    <span class="k">return</span> <span class="n">senal_Tx</span><span class="p">,</span> <span class="n">P_senal_Tx</span><span class="p">,</span> <span class="n">portadora</span><span class="p">,</span> <span class="n">moduladora</span>  
</pre></div>

    </div>
</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h4 id="3.1.4.---Construcci&#243;n-de-un-canal-con-ruido-AWGN">3.1.4. - Construcci&#243;n de un canal con ruido AWGN<a class="anchor-link" href="#3.1.4.---Construcci&#243;n-de-un-canal-con-ruido-AWGN">&#182;</a></h4>
</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[19]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="kn">import</span> <span class="nn">numpy</span> <span class="k">as</span> <span class="nn">np</span>

<span class="k">def</span> <span class="nf">canal_ruidoso</span><span class="p">(</span><span class="n">senal_Tx</span><span class="p">,</span> <span class="n">Pm</span><span class="p">,</span> <span class="n">SNR</span><span class="p">):</span>
    <span class="sd">&#39;&#39;&#39;Un bloque que simula un medio de trans-</span>
<span class="sd">    misión no ideal (ruidoso) empleando ruido</span>
<span class="sd">    AWGN. Pide por parámetro un vector con la</span>
<span class="sd">    señal provieniente de un modulador y un</span>
<span class="sd">    valor en decibelios para la relación señal</span>
<span class="sd">    a ruido.</span>

<span class="sd">    :param senal_Tx: El vector del modulador</span>
<span class="sd">    :param Pm: Potencia de la señal modulada</span>
<span class="sd">    :param SNR: Relación señal-a-ruido en dB</span>
<span class="sd">    :return: La señal modulada al dejar el canal</span>
<span class="sd">    &#39;&#39;&#39;</span>
    <span class="c1"># Potencia del ruido generado por el canal</span>
    <span class="n">Pn</span> <span class="o">=</span> <span class="n">Pm</span> <span class="o">/</span> <span class="nb">pow</span><span class="p">(</span><span class="mi">10</span><span class="p">,</span> <span class="n">SNR</span><span class="o">/</span><span class="mi">10</span><span class="p">)</span>

    <span class="c1"># Generando ruido auditivo blanco gaussiano (potencia = varianza)</span>
    <span class="n">ruido</span> <span class="o">=</span> <span class="n">np</span><span class="o">.</span><span class="n">random</span><span class="o">.</span><span class="n">normal</span><span class="p">(</span><span class="mi">0</span><span class="p">,</span> <span class="n">np</span><span class="o">.</span><span class="n">sqrt</span><span class="p">(</span><span class="n">Pn</span><span class="p">),</span> <span class="n">senal_Tx</span><span class="o">.</span><span class="n">shape</span><span class="p">)</span>

    <span class="c1"># Señal distorsionada por el canal ruidoso</span>
    <span class="n">senal_Rx</span> <span class="o">=</span> <span class="n">senal_Tx</span> <span class="o">+</span> <span class="n">ruido</span>

    <span class="k">return</span> <span class="n">senal_Rx</span>
</pre></div>

    </div>
</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h4 id="3.1.5.---Esquema-de-demodulaci&#243;n">3.1.5. - Esquema de demodulaci&#243;n<a class="anchor-link" href="#3.1.5.---Esquema-de-demodulaci&#243;n">&#182;</a></h4>
</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[20]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="kn">import</span> <span class="nn">numpy</span> <span class="k">as</span> <span class="nn">np</span>

<span class="k">def</span> <span class="nf">demodulador</span><span class="p">(</span><span class="n">senal_Rx</span><span class="p">,</span> <span class="n">portadora</span><span class="p">,</span> <span class="n">mpp</span><span class="p">):</span>
    <span class="sd">&#39;&#39;&#39;Un método que simula un bloque demodulador</span>
<span class="sd">    de señales, bajo un esquema BPSK. El criterio</span>
<span class="sd">    de demodulación se basa en decodificación por </span>
<span class="sd">    detección de energía.</span>

<span class="sd">    :param senal_Rx: La señal recibida del canal</span>
<span class="sd">    :param portadora: La onda portadora c(t)</span>
<span class="sd">    :param mpp: Número de muestras por periodo</span>
<span class="sd">    :return: Los bits de la señal demodulada</span>
<span class="sd">    &#39;&#39;&#39;</span>
    <span class="c1"># Cantidad de muestras en senal_Rx</span>
    <span class="n">M</span> <span class="o">=</span> <span class="nb">len</span><span class="p">(</span><span class="n">senal_Rx</span><span class="p">)</span>

    <span class="c1"># Cantidad de bits (símbolos) en transmisión</span>
    <span class="n">N</span> <span class="o">=</span> <span class="nb">int</span><span class="p">(</span><span class="n">M</span> <span class="o">/</span> <span class="n">mpp</span><span class="p">)</span>

    <span class="c1"># Vector para bits obtenidos por la demodulación</span>
    <span class="n">bits_Rx</span> <span class="o">=</span> <span class="n">np</span><span class="o">.</span><span class="n">zeros</span><span class="p">(</span><span class="n">N</span><span class="p">)</span>

    <span class="c1"># Vector para la señal demodulada</span>
    <span class="n">senal_demodulada</span> <span class="o">=</span> <span class="n">np</span><span class="o">.</span><span class="n">zeros</span><span class="p">(</span><span class="n">senal_Rx</span><span class="o">.</span><span class="n">shape</span><span class="p">)</span>

    <span class="c1"># Pseudo-energía de un período de la portadora</span>
    <span class="n">Es</span> <span class="o">=</span> <span class="n">np</span><span class="o">.</span><span class="n">sum</span><span class="p">(</span><span class="n">portadora</span> <span class="o">*</span> <span class="n">portadora</span><span class="p">)</span>

    <span class="c1"># Demodulación</span>
    <span class="k">for</span> <span class="n">i</span> <span class="ow">in</span> <span class="nb">range</span><span class="p">(</span><span class="n">N</span><span class="p">):</span>
        <span class="c1"># Producto interno de dos funciones</span>
        <span class="n">producto</span> <span class="o">=</span> <span class="n">senal_Rx</span><span class="p">[</span><span class="n">i</span><span class="o">*</span><span class="n">mpp</span> <span class="p">:</span> <span class="p">(</span><span class="n">i</span><span class="o">+</span><span class="mi">1</span><span class="p">)</span><span class="o">*</span><span class="n">mpp</span><span class="p">]</span> <span class="o">*</span> <span class="n">portadora</span>
        <span class="n">Ep</span> <span class="o">=</span> <span class="n">np</span><span class="o">.</span><span class="n">sum</span><span class="p">(</span><span class="n">producto</span><span class="p">)</span> 
        <span class="n">senal_demodulada</span><span class="p">[</span><span class="n">i</span><span class="o">*</span><span class="n">mpp</span> <span class="p">:</span> <span class="p">(</span><span class="n">i</span><span class="o">+</span><span class="mi">1</span><span class="p">)</span><span class="o">*</span><span class="n">mpp</span><span class="p">]</span> <span class="o">=</span> <span class="n">producto</span>

        <span class="c1"># Criterio de decisión por detección de energía</span>
        <span class="k">if</span> <span class="n">Ep</span> <span class="o">&gt;</span> <span class="mi">0</span><span class="p">:</span>
            <span class="n">bits_Rx</span><span class="p">[</span><span class="n">i</span><span class="p">]</span> <span class="o">=</span> <span class="mi">1</span>
        <span class="k">else</span><span class="p">:</span>
            <span class="n">bits_Rx</span><span class="p">[</span><span class="n">i</span><span class="p">]</span> <span class="o">=</span> <span class="mi">0</span>

    <span class="k">return</span> <span class="n">bits_Rx</span><span class="o">.</span><span class="n">astype</span><span class="p">(</span><span class="nb">int</span><span class="p">),</span> <span class="n">senal_demodulada</span>
</pre></div>

    </div>
</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h4 id="3.1.6.---Reconstrucci&#243;n-de-la-imagen">3.1.6. - Reconstrucci&#243;n de la imagen<a class="anchor-link" href="#3.1.6.---Reconstrucci&#243;n-de-la-imagen">&#182;</a></h4>
</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[21]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="kn">import</span> <span class="nn">numpy</span> <span class="k">as</span> <span class="nn">np</span>

<span class="k">def</span> <span class="nf">bits_a_rgb</span><span class="p">(</span><span class="n">bits_Rx</span><span class="p">,</span> <span class="n">dimensiones</span><span class="p">):</span>
    <span class="sd">&#39;&#39;&#39;Un blque que decodifica el los bits</span>
<span class="sd">    recuperados en el proceso de demodulación</span>

<span class="sd">    :param: Un vector de bits 1 x k </span>
<span class="sd">    :param dimensiones: Tupla con dimensiones de la img.</span>
<span class="sd">    :return: Un array con los pixeles reconstruidos</span>
<span class="sd">    &#39;&#39;&#39;</span>
    <span class="c1"># Cantidad de bits</span>
    <span class="n">N</span> <span class="o">=</span> <span class="nb">len</span><span class="p">(</span><span class="n">bits_Rx</span><span class="p">)</span>

    <span class="c1"># Se reconstruyen los canales RGB</span>
    <span class="n">bits</span> <span class="o">=</span> <span class="n">np</span><span class="o">.</span><span class="n">split</span><span class="p">(</span><span class="n">bits_Rx</span><span class="p">,</span> <span class="n">N</span> <span class="o">/</span> <span class="mi">8</span><span class="p">)</span>

    <span class="c1"># Se decofican los canales:</span>
    <span class="n">canales</span> <span class="o">=</span> <span class="p">[</span><span class="nb">int</span><span class="p">(</span><span class="s1">&#39;&#39;</span><span class="o">.</span><span class="n">join</span><span class="p">(</span><span class="nb">map</span><span class="p">(</span><span class="nb">str</span><span class="p">,</span> <span class="n">canal</span><span class="p">)),</span> <span class="mi">2</span><span class="p">)</span> <span class="k">for</span> <span class="n">canal</span> <span class="ow">in</span> <span class="n">bits</span><span class="p">]</span>
    <span class="n">pixeles</span> <span class="o">=</span> <span class="n">np</span><span class="o">.</span><span class="n">reshape</span><span class="p">(</span><span class="n">canales</span><span class="p">,</span> <span class="n">dimensiones</span><span class="p">)</span>

    <span class="k">return</span> <span class="n">pixeles</span><span class="o">.</span><span class="n">astype</span><span class="p">(</span><span class="n">np</span><span class="o">.</span><span class="n">uint8</span><span class="p">)</span>
</pre></div>

    </div>
</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h3 id="3.2.---Simulaci&#243;n-del-sistema-de-comunicaciones-con-modulaci&#243;n-BPSK">3.2. - Simulaci&#243;n del sistema de comunicaciones con modulaci&#243;n BPSK<a class="anchor-link" href="#3.2.---Simulaci&#243;n-del-sistema-de-comunicaciones-con-modulaci&#243;n-BPSK">&#182;</a></h3><p><strong>Nota</strong>: esta simulación tarda un poco y quizá hay que hacerla dos veces.</p>

</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[22]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="kn">import</span> <span class="nn">numpy</span> <span class="k">as</span> <span class="nn">np</span>
<span class="kn">import</span> <span class="nn">matplotlib.pyplot</span> <span class="k">as</span> <span class="nn">plt</span>
<span class="kn">import</span> <span class="nn">time</span>

<span class="c1"># Parámetros</span>
<span class="n">fc</span> <span class="o">=</span> <span class="mi">5000</span>  <span class="c1"># frecuencia de la portadora</span>
<span class="n">mpp</span> <span class="o">=</span> <span class="mi">20</span>   <span class="c1"># muestras por periodo de la portadora</span>
<span class="n">SNR</span> <span class="o">=</span> <span class="mi">0</span>   <span class="c1"># relación señal-a-ruido del canal</span>

<span class="c1"># Iniciar medición del tiempo de simulación</span>
<span class="n">inicio</span> <span class="o">=</span> <span class="n">time</span><span class="o">.</span><span class="n">time</span><span class="p">()</span>

<span class="c1"># 1. Importar y convertir la imagen a trasmitir</span>
<span class="n">imagen_Tx</span> <span class="o">=</span> <span class="n">fuente_info</span><span class="p">(</span><span class="s1">&#39;arenal.jpg&#39;</span><span class="p">)</span>
<span class="n">dimensiones</span> <span class="o">=</span> <span class="n">imagen_Tx</span><span class="o">.</span><span class="n">shape</span>

<span class="c1"># 2. Codificar los pixeles de la imagen</span>
<span class="n">bits_Tx</span> <span class="o">=</span> <span class="n">rgb_a_bit</span><span class="p">(</span><span class="n">imagen_Tx</span><span class="p">)</span>

<span class="c1"># 3. Modular la cadena de bits usando el esquema BPSK</span>
<span class="n">senal_Tx</span><span class="p">,</span> <span class="n">Pm</span><span class="p">,</span> <span class="n">portadora</span><span class="p">,</span> <span class="n">moduladora</span> <span class="o">=</span> <span class="n">modulador</span><span class="p">(</span><span class="n">bits_Tx</span><span class="p">,</span> <span class="n">fc</span><span class="p">,</span> <span class="n">mpp</span><span class="p">)</span>

<span class="c1"># 4. Se transmite la señal modulada, por un canal ruidoso</span>
<span class="n">senal_Rx</span> <span class="o">=</span> <span class="n">canal_ruidoso</span><span class="p">(</span><span class="n">senal_Tx</span><span class="p">,</span> <span class="n">Pm</span><span class="p">,</span> <span class="n">SNR</span><span class="p">)</span>

<span class="c1"># 5. Se desmodula la señal recibida del canal</span>
<span class="n">bits_Rx</span><span class="p">,</span> <span class="n">senal_demodulada</span> <span class="o">=</span> <span class="n">demodulador</span><span class="p">(</span><span class="n">senal_Rx</span><span class="p">,</span> <span class="n">portadora</span><span class="p">,</span> <span class="n">mpp</span><span class="p">)</span>

<span class="c1"># 6. Se visualiza la imagen recibida </span>
<span class="n">imagen_Rx</span> <span class="o">=</span> <span class="n">bits_a_rgb</span><span class="p">(</span><span class="n">bits_Rx</span><span class="p">,</span> <span class="n">dimensiones</span><span class="p">)</span>
<span class="n">Fig</span> <span class="o">=</span> <span class="n">plt</span><span class="o">.</span><span class="n">figure</span><span class="p">(</span><span class="n">figsize</span><span class="o">=</span><span class="p">(</span><span class="mi">10</span><span class="p">,</span><span class="mi">6</span><span class="p">))</span>

<span class="c1"># Cálculo del tiempo de simulación</span>
<span class="nb">print</span><span class="p">(</span><span class="s1">&#39;Duración de la simulación: &#39;</span><span class="p">,</span> <span class="n">time</span><span class="o">.</span><span class="n">time</span><span class="p">()</span> <span class="o">-</span> <span class="n">inicio</span><span class="p">)</span>

<span class="c1"># 7. Calcular número de errores</span>
<span class="n">errores</span> <span class="o">=</span> <span class="nb">sum</span><span class="p">(</span><span class="nb">abs</span><span class="p">(</span><span class="n">bits_Tx</span> <span class="o">-</span> <span class="n">bits_Rx</span><span class="p">))</span>
<span class="n">BER</span> <span class="o">=</span> <span class="n">errores</span><span class="o">/</span><span class="nb">len</span><span class="p">(</span><span class="n">bits_Tx</span><span class="p">)</span>
<span class="nb">print</span><span class="p">(</span><span class="s1">&#39;</span><span class="si">{}</span><span class="s1"> errores, para un BER de </span><span class="si">{:0.4f}</span><span class="s1">.&#39;</span><span class="o">.</span><span class="n">format</span><span class="p">(</span><span class="n">errores</span><span class="p">,</span> <span class="n">BER</span><span class="p">))</span>

<span class="c1"># Mostrar imagen transmitida</span>
<span class="n">ax</span> <span class="o">=</span> <span class="n">Fig</span><span class="o">.</span><span class="n">add_subplot</span><span class="p">(</span><span class="mi">1</span><span class="p">,</span> <span class="mi">2</span><span class="p">,</span> <span class="mi">1</span><span class="p">)</span>
<span class="n">imgplot</span> <span class="o">=</span> <span class="n">plt</span><span class="o">.</span><span class="n">imshow</span><span class="p">(</span><span class="n">imagen_Tx</span><span class="p">)</span>
<span class="n">ax</span><span class="o">.</span><span class="n">set_title</span><span class="p">(</span><span class="s1">&#39;Transmitido&#39;</span><span class="p">)</span>

<span class="c1"># Mostrar imagen recuperada</span>
<span class="n">ax</span> <span class="o">=</span> <span class="n">Fig</span><span class="o">.</span><span class="n">add_subplot</span><span class="p">(</span><span class="mi">1</span><span class="p">,</span> <span class="mi">2</span><span class="p">,</span> <span class="mi">2</span><span class="p">)</span>
<span class="n">imgplot</span> <span class="o">=</span> <span class="n">plt</span><span class="o">.</span><span class="n">imshow</span><span class="p">(</span><span class="n">imagen_Rx</span><span class="p">)</span>
<span class="n">ax</span><span class="o">.</span><span class="n">set_title</span><span class="p">(</span><span class="s1">&#39;Recuperado&#39;</span><span class="p">)</span>
<span class="n">Fig</span><span class="o">.</span><span class="n">tight_layout</span><span class="p">()</span>

<span class="n">plt</span><span class="o">.</span><span class="n">imshow</span><span class="p">(</span><span class="n">imagen_Rx</span><span class="p">)</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt"></div>


<div class="output_subarea output_stream output_stdout output_text">
<pre>Duración de la simulación:  5.161305904388428
4 errores, para un BER de 0.0000.
</pre>
</div>
</div>

<div class="output_area">

    <div class="prompt output_prompt">Out[22]:</div>




<div class="output_text output_subarea output_execute_result">
<pre>&lt;matplotlib.image.AxesImage at 0x20a0d0be518&gt;</pre>
</div>

</div>

<div class="output_area">

    <div class="prompt"></div>




<div class="output_png output_subarea ">
<img src="data:image/png;base64,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
"
>
</div>

</div>

</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[23]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="kn">import</span> <span class="nn">matplotlib.pyplot</span> <span class="k">as</span> <span class="nn">plt</span>

<span class="c1"># Visualizar el cambio entre las señales</span>
<span class="n">fig</span><span class="p">,</span> <span class="p">(</span><span class="n">ax1</span><span class="p">,</span> <span class="n">ax2</span><span class="p">,</span> <span class="n">ax3</span><span class="p">,</span> <span class="n">ax4</span><span class="p">)</span> <span class="o">=</span> <span class="n">plt</span><span class="o">.</span><span class="n">subplots</span><span class="p">(</span><span class="n">nrows</span><span class="o">=</span><span class="mi">4</span><span class="p">,</span> <span class="n">sharex</span><span class="o">=</span><span class="kc">True</span><span class="p">,</span> <span class="n">figsize</span><span class="o">=</span><span class="p">(</span><span class="mi">14</span><span class="p">,</span> <span class="mi">7</span><span class="p">))</span>

<span class="c1"># La onda cuadrada moduladora (bits de entrada)</span>
<span class="n">ax1</span><span class="o">.</span><span class="n">plot</span><span class="p">(</span><span class="n">moduladora</span><span class="p">[</span><span class="mi">0</span><span class="p">:</span><span class="mi">600</span><span class="p">],</span> <span class="n">color</span><span class="o">=</span><span class="s1">&#39;r&#39;</span><span class="p">,</span> <span class="n">lw</span><span class="o">=</span><span class="mi">2</span><span class="p">)</span> 
<span class="n">ax1</span><span class="o">.</span><span class="n">set_ylabel</span><span class="p">(</span><span class="s1">&#39;$b(t)$&#39;</span><span class="p">)</span>

<span class="c1"># La señal modulada por BPSK</span>
<span class="n">ax2</span><span class="o">.</span><span class="n">plot</span><span class="p">(</span><span class="n">senal_Tx</span><span class="p">[</span><span class="mi">0</span><span class="p">:</span><span class="mi">600</span><span class="p">],</span> <span class="n">color</span><span class="o">=</span><span class="s1">&#39;g&#39;</span><span class="p">,</span> <span class="n">lw</span><span class="o">=</span><span class="mi">2</span><span class="p">)</span> 
<span class="n">ax2</span><span class="o">.</span><span class="n">set_ylabel</span><span class="p">(</span><span class="s1">&#39;$s(t)$&#39;</span><span class="p">)</span>

<span class="c1"># La señal modulada al dejar el canal</span>
<span class="n">ax3</span><span class="o">.</span><span class="n">plot</span><span class="p">(</span><span class="n">senal_Rx</span><span class="p">[</span><span class="mi">0</span><span class="p">:</span><span class="mi">600</span><span class="p">],</span> <span class="n">color</span><span class="o">=</span><span class="s1">&#39;b&#39;</span><span class="p">,</span> <span class="n">lw</span><span class="o">=</span><span class="mi">2</span><span class="p">)</span> 
<span class="n">ax3</span><span class="o">.</span><span class="n">set_ylabel</span><span class="p">(</span><span class="s1">&#39;$s(t) + n(t)$&#39;</span><span class="p">)</span>

<span class="c1"># La señal demodulada</span>
<span class="n">ax4</span><span class="o">.</span><span class="n">plot</span><span class="p">(</span><span class="n">senal_demodulada</span><span class="p">[</span><span class="mi">0</span><span class="p">:</span><span class="mi">600</span><span class="p">],</span> <span class="n">color</span><span class="o">=</span><span class="s1">&#39;m&#39;</span><span class="p">,</span> <span class="n">lw</span><span class="o">=</span><span class="mi">2</span><span class="p">)</span> 
<span class="n">ax4</span><span class="o">.</span><span class="n">set_ylabel</span><span class="p">(</span><span class="s1">&#39;$b^{\prime}(t)$&#39;</span><span class="p">)</span>
<span class="n">ax4</span><span class="o">.</span><span class="n">set_xlabel</span><span class="p">(</span><span class="s1">&#39;$t$ / milisegundos&#39;</span><span class="p">)</span>
<span class="n">fig</span><span class="o">.</span><span class="n">tight_layout</span><span class="p">()</span>
<span class="n">plt</span><span class="o">.</span><span class="n">show</span><span class="p">()</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt"></div>




<div class="output_png output_subarea ">
<img src="data:image/png;base64,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
"
>
</div>

</div>

</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h3 id="3.3.---Modulaci&#243;n-IQ">3.3. - Modulaci&#243;n IQ<a class="anchor-link" href="#3.3.---Modulaci&#243;n-IQ">&#182;</a></h3><p>Obsérvese que en la modulación BPSK anterior existe una única portadora (<em>carrier</em>) sinusoidal, dada por</p>
$$
c(t) = A_c \sin(2\pi f_c t - \theta_c)
$$<p>La propiedad de la <strong>ortogonalidad</strong> entre las funciones $\sin(\omega t)$ y $\cos(\omega t)$ permite utilizar dos portadoras en lugar de una, de forma tal que es posible crear una señal modulada del tipo:</p>
$$
s(t) = A_1 \cos(2\pi f_c t) + A_2 \sin(2\pi f_c t)
$$<p>Esta señal ocupa el mismo ancho de banda que una sola portadora sinusoidal, pero puede transportar el doble de la información, codificada en $A_1$ y $A_2$. Debido a que las ondas seno y coseno están separadas por un desfase de 90 grados, a este tipo de modulación se le llama "en fase" (<strong>I</strong>, <em>in phase</em>) y "en cuadratura" (<strong>Q</strong>, <em>quadrature</em>), o <strong>modulación IQ</strong>.</p>
<h4 id="3.3.1.---Ortogonalidad">3.3.1. - Ortogonalidad<a class="anchor-link" href="#3.3.1.---Ortogonalidad">&#182;</a></h4><p>La prueba de ortogonalidad de dos funciones del tiempo está dada por el producto interno:</p>
$$
\begin{aligned}
(f * g) (t) &amp; = \langle f(t), g(t)\rangle \\
&amp; = \int f(t) g(t) \, \mathrm{d}t            
\end{aligned}
$$<p>Y en el caso de las dos portadoras sinusoidales:</p>
$$
\begin{aligned}
(f * g) (t) &amp; = \langle f(t), g(t)\rangle \\
&amp; = \int f(t) g(t) \, \mathrm{d}t \\
&amp; = \int \cos(2\pi f_c t) \, \sin(2\pi f_c t) \, \mathrm{d}t \\
&amp; = 0 
\end{aligned}
$$<blockquote><p>Podría decirse, coloquialmente, que las portadoras viajan "juntas pero no revueltas".</p>
</blockquote>
<p>Este resultado es útil para la <em>demodulación coherente (en fase)</em> de señales IQ, porque permite "separar" una portadora de otra.</p>
<h4 id="3.3.2.---Modulaci&#243;n-QPSK">3.3.2. - Modulaci&#243;n QPSK<a class="anchor-link" href="#3.3.2.---Modulaci&#243;n-QPSK">&#182;</a></h4><p>La modulación BPSK tiene dos símbolos posibles (<code>0</code>, <code>1</code>) lo que implica un bit $b$ por símbolo, mientras que la modulación QPSK (<em>Quadrature Phase-Shift Keying</em>) tiene cuatro símbolos posibles (<code>00</code>, <code>01</code>, <code>10</code>, <code>11</code>), con dos bits $b_1 b_2$ por símbolo. La codificación para un símbolo $b_1 b_2$ es ahora:</p>
$$
s(t) = A_1 \cos(2\pi f_c t) + A_2 \sin(2\pi f_c t)
$$<p>donde</p>
$$
A_1 = 
\begin{cases}
             -1, &amp;   \text{si} \quad b_1 = 0 \\
             1, &amp;  \text{si}   \quad b_1 = 1 \\
\end{cases}
$$<p>y</p>
$$
A_2 = 
\begin{cases}
             -1, &amp;   \text{si} \quad b_2 = 0 \\
              1, &amp;   \text{si} \quad b_2 = 1 \\
\end{cases}
$$<p><img src="https://www.analog.com/-/media/analog/en/landing-pages/technical-articles/low-power-iq-modulator-for-digital-communications/iqmodulator.png?h=270&hash=868F3CDB85D7842D27627F7A12099156E9729935&la=en" width="400"></p>
<p>Si se grafica la amplitud $A_1$ y $A_2$ de cada portadora en una gráfica donde el eje $x$ representa al coseno (en fase, $I$) y el eje $y$ al seno (en cuadratura, $Q$), se obtiene lo que se conoce como un "diagrama de constelación" de la modulación:</p>
<p><img src='https://upload.wikimedia.org/wikipedia/commons/thumb/8/8f/QPSK_Gray_Coded.svg/800px-QPSK_Gray_Coded.svg.png' width='200'></p>
<p>Ahí es posible verificar la correspondencia de los bits $b_1 b_2$ (<code>00</code>, <code>01</code>, <code>10</code>, <code>11</code>) con los puntos de la constelación.</p>
<blockquote><p>La modulación QPSK es utilizada en el estándar Wi-Fi IEEE 802.11 (una de sus posibles modulaciones), en comunicaciones satelitales, y en 5G, entre otros.</p>
</blockquote>
<h4 id="3.3.3.---Modulaci&#243;n-8-PSK">3.3.3. - Modulaci&#243;n 8-PSK<a class="anchor-link" href="#3.3.3.---Modulaci&#243;n-8-PSK">&#182;</a></h4><p>La modulación 8-PSK tiene ocho símbolos posibles con tres bits $b_1 b_2 b_3$ por símbolo. La codificación para un símbolo $b_1 b_2 b_3$ es ahora:</p>
$$
s(t) = A_1 \cos(2\pi f_c t) + A_2 \sin(2\pi f_c t)
$$<p>donde</p>
$$
\begin{cases}
    A_1 = 1, &amp; A_2 = 0 &amp; \text{si} \quad b_1 b_2 b_3 = 111 \\
    A_1 = h, &amp; A_2 = h &amp; \text{si} \quad b_1 b_2 b_3 = 110 \\
    A_1 = 0, &amp; A_2 = 1 &amp; \text{si} \quad b_1 b_2 b_3 = 010 \\
    A_1 =-h, &amp; A_2 = h &amp; \text{si} \quad b_1 b_2 b_3 = 011 \\
    A_1 =-1, &amp; A_2 = 0 &amp; \text{si} \quad b_1 b_2 b_3 = 001 \\
    A_1 =-h, &amp; A_2 =-h &amp; \text{si} \quad b_1 b_2 b_3 = 000 \\
    A_1 = 0, &amp; A_2 =-1 &amp; \text{si} \quad b_1 b_2 b_3 = 100 \\
    A_1 = h, &amp; A_2 =-h &amp; \text{si} \quad b_1 b_2 b_3 = 101 \\
\end{cases}
$$<p>donde $h = 1\sin(45^o) = 1\cos(45^o) = \sqrt{2}/2 \approx 0.707$.</p>
<p>El "diagrama de constelación" de la modulación es:</p>
<p><img src="https://upload.wikimedia.org/wikipedia/commons/thumb/1/11/8PSK_Gray_Coded.svg/400px-8PSK_Gray_Coded.svg.png" width="200"></p>
<p>Ahí es posible verificar la correspondencia de los bits $b_1 b_2 b_3$ (<code>000</code>, <code>001</code>, <code>010</code>, <code>011</code>, <code>100</code>, <code>101</code>, <code>110</code>, <code>111</code>) con los puntos de la constelación.</p>
<h4 id="3.3.4.---Modulaci&#243;n-QAM">3.3.4. - Modulaci&#243;n QAM<a class="anchor-link" href="#3.3.4.---Modulaci&#243;n-QAM">&#182;</a></h4><p>La modulación de amplitud en cuadratura (<strong>QAM</strong>, <em>Quadrature Amplitude Modulation</em>) es otro tipo de modulación IQ que ahora utiliza más posibles amplitudes de las dos portadoras para crear una constelación como la siguiente:</p>
<p><img src="https://upload.wikimedia.org/wikipedia/commons/thumb/1/1e/16QAM_Gray_Coded.svg/1280px-16QAM_Gray_Coded.svg.png" width="250"></p>
<p>en donde se aprecian dos valores positivos y dos valores negativos para cada portadora. Este es el caso 16-QAM, en tanto que tiene 16 símbolos de 4 bits cada uno ($2^4 = 16$).</p>
<p>La codificación para un símbolo $b_1 b_2 b_3 b_4$ es:</p>
$$
s(t) = A_1 \cos(2\pi f_c t) + A_2 \sin(2\pi f_c t)
$$<p>donde</p>
$$
A_1 = 
\begin{cases}
             -3, &amp;   \text{si} \quad b_1 b_2 = 00 \\
             -1, &amp;   \text{si} \quad b_1 b_2 = 01 \\
             1, &amp;  \text{si}   \quad b_1 b_2 = 11 \\
             3, &amp;  \text{si}   \quad, b_1 b_2 = 10 \\
\end{cases}
$$<p>y</p>
$$
A_2 = 
\begin{cases}
             3, &amp;   \text{si} \quad b_3 b_4 = 00 \\
             1, &amp;   \text{si} \quad b_3 b_4 = 01 \\
             -1, &amp;  \text{si}   \quad b_3 b_4 = 11 \\
             -3, &amp;  \text{si}   \quad b_3 b_4 = 10 \\
\end{cases}
$$<blockquote><p>La modulación QAM es también utilizada en el estándar Wi-Fi IEEE 802.11 de forma adaptativa, por lo que puede ir desde 16-QAM (4 bits/símbolo) hasta 512-QAM (9 bits/símbolo) cuando las condiciones del canal son óptimas.</p>
</blockquote>

</div>
</div>
</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<hr>
<h2 id="4.---Asignaciones-del-proyecto">4. - Asignaciones del proyecto<a class="anchor-link" href="#4.---Asignaciones-del-proyecto">&#182;</a></h2><h3 id="4.1.---Modulaci&#243;n-8-PSK">4.1. - Modulaci&#243;n 8-PSK<a class="anchor-link" href="#4.1.---Modulaci&#243;n-8-PSK">&#182;</a></h3><ul>
<li>(50%) Realice una simulación del sistema de comunicaciones como en la sección 3.2., pero utilizando una modulación <strong>8-PSK</strong> en lugar de una modulación BPSK. Deben mostrarse las imágenes enviadas y recuperadas y las formas de onda.</li>
</ul>

</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[24]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="c1"># 4.1. - Modulación 8-PSK</span>
<span class="c1"># En este apartado se realiza una simulación del sistema de comunicaciones como en la sección 3.2</span>
<span class="c1"># pero utilizando la modulación </span>
<span class="c1"># Se importan librerías </span>
<span class="c1"># Se debe realizar los pasos para un modulado de 8-PSK</span>

<span class="kn">import</span> <span class="nn">numpy</span> <span class="k">as</span> <span class="nn">np</span>
<span class="kn">import</span> <span class="nn">matplotlib.pyplot</span> <span class="k">as</span> <span class="nn">plt</span>
<span class="kn">import</span> <span class="nn">time</span>
<span class="kn">from</span> <span class="nn">PIL</span> <span class="k">import</span> <span class="n">Image</span>

<span class="k">def</span> <span class="nf">modulador8</span><span class="p">(</span><span class="n">bits</span><span class="p">,</span> <span class="n">fc</span><span class="p">,</span> <span class="n">mpp</span><span class="p">):</span>
    <span class="sd">&#39;&#39;&#39;Un método que simula el esquema de modilación</span>
<span class="sd">    digital 8-PSK</span>
<span class="sd">    :params bits: Vector unidimencional de bits</span>
<span class="sd">    :params fc: Frecuencia de la portadora en Hz</span>
<span class="sd">    :params mpp: Cantidad de muestras por periodo de onda portadora</span>
<span class="sd">    :return: Un vector con la señal modulada </span>
<span class="sd">    :return: Un valor con la potencia promedio [W]</span>
<span class="sd">    :return: onda portadora 1</span>
<span class="sd">    :return: onda portadora 2</span>
<span class="sd">    &#39;&#39;&#39;</span>
    <span class="c1"># 1. Parámetros de la señal de información (bits)</span>
    <span class="c1"># Se determina la cantidad de bits</span>
    <span class="n">N</span> <span class="o">=</span> <span class="nb">len</span><span class="p">(</span><span class="n">bits</span><span class="p">)</span>
    
    <span class="c1"># 2. Contruyendo un periodo de la señal portadora c (t)</span>
    <span class="c1"># Se crea las funciones de las portadoras</span>
    <span class="n">Tc</span> <span class="o">=</span> <span class="mi">1</span> <span class="o">/</span> <span class="n">fc</span> <span class="c1"># periodo en [s]</span>
    <span class="n">t_periodo</span> <span class="o">=</span> <span class="n">np</span><span class="o">.</span><span class="n">linspace</span><span class="p">(</span><span class="mi">0</span><span class="p">,</span> <span class="n">Tc</span><span class="p">,</span> <span class="n">mpp</span><span class="p">)</span> <span class="c1"># Muestras por periodo</span>
    <span class="n">portadora_1</span> <span class="o">=</span> <span class="n">np</span><span class="o">.</span><span class="n">cos</span><span class="p">(</span><span class="mi">2</span><span class="o">*</span><span class="n">np</span><span class="o">.</span><span class="n">pi</span><span class="o">*</span><span class="n">fc</span><span class="o">*</span><span class="n">t_periodo</span><span class="p">)</span>
    <span class="n">portadora_2</span> <span class="o">=</span> <span class="n">np</span><span class="o">.</span><span class="n">sin</span><span class="p">(</span><span class="mi">2</span><span class="o">*</span><span class="n">np</span><span class="o">.</span><span class="n">pi</span><span class="o">*</span><span class="n">fc</span><span class="o">*</span><span class="n">t_periodo</span><span class="p">)</span>
    
    <span class="c1"># 3. Inicializar la señal modulada s(t)</span>
    <span class="n">t_simulacion</span> <span class="o">=</span> <span class="n">np</span><span class="o">.</span><span class="n">linspace</span><span class="p">(</span><span class="mi">0</span><span class="p">,</span> <span class="n">N</span><span class="o">*</span><span class="n">Tc</span><span class="p">,</span> <span class="n">N</span><span class="o">*</span><span class="n">mpp</span><span class="p">)</span> 
    <span class="n">senal_Tx</span> <span class="o">=</span> <span class="n">np</span><span class="o">.</span><span class="n">zeros</span><span class="p">(</span><span class="n">t_simulacion</span><span class="o">.</span><span class="n">shape</span><span class="p">)</span>
    
    <span class="c1"># Se realizará las formas de ondas segun el metodo de los bits de 8-PSK</span>
    <span class="c1"># Asiganr variable h</span>
    <span class="n">h</span> <span class="o">=</span> <span class="mf">0.707</span>
    
    <span class="c1"># Por la condiciones que presenta este método se realiza un &quot;for&quot;</span>
    <span class="c1"># Se estudiará los condicionales de los bits del método de estudio</span>
    
    <span class="k">for</span> <span class="n">i</span> <span class="ow">in</span> <span class="nb">range</span><span class="p">(</span><span class="mi">0</span><span class="p">,</span> <span class="n">N</span><span class="p">,</span> <span class="mi">3</span><span class="p">):</span>
        <span class="k">if</span> <span class="n">bits</span><span class="p">[</span><span class="n">i</span><span class="p">]</span> <span class="o">==</span> <span class="mi">1</span> <span class="ow">and</span> <span class="n">bits</span><span class="p">[</span><span class="n">i</span><span class="o">+</span><span class="mi">1</span><span class="p">]</span> <span class="o">==</span> <span class="mi">0</span> <span class="ow">and</span> <span class="n">bits</span><span class="p">[</span><span class="n">i</span><span class="o">+</span><span class="mi">2</span><span class="p">]</span> <span class="o">==</span> <span class="mi">0</span><span class="p">:</span>
            <span class="n">senal_Tx</span><span class="p">[</span><span class="n">i</span><span class="o">*</span><span class="n">mpp</span><span class="p">:</span> <span class="p">(</span><span class="n">i</span><span class="o">+</span><span class="mi">1</span><span class="p">)</span><span class="o">*</span><span class="n">mpp</span><span class="p">]</span> <span class="o">=</span> <span class="n">portadora_1</span> <span class="o">*</span> <span class="mi">0</span> <span class="o">+</span> <span class="n">portadora_2</span> <span class="o">*</span> <span class="o">-</span><span class="mi">1</span>
            
        <span class="k">elif</span> <span class="n">bits</span><span class="p">[</span><span class="n">i</span><span class="p">]</span> <span class="o">==</span> <span class="mi">1</span> <span class="ow">and</span> <span class="n">bits</span><span class="p">[</span><span class="n">i</span><span class="o">+</span><span class="mi">1</span><span class="p">]</span> <span class="o">==</span> <span class="mi">1</span> <span class="ow">and</span> <span class="n">bits</span><span class="p">[</span><span class="n">i</span><span class="o">+</span><span class="mi">2</span><span class="p">]</span> <span class="o">==</span> <span class="mi">0</span><span class="p">:</span>
            <span class="n">senal_Tx</span><span class="p">[</span><span class="n">i</span><span class="o">*</span><span class="n">mpp</span><span class="p">:</span> <span class="p">(</span><span class="n">i</span><span class="o">+</span><span class="mi">1</span><span class="p">)</span><span class="o">*</span><span class="n">mpp</span><span class="p">]</span> <span class="o">=</span> <span class="n">portadora_1</span> <span class="o">*</span> <span class="n">h</span> <span class="o">+</span> <span class="n">portadora_2</span> <span class="o">*</span> <span class="n">h</span>
        
        <span class="k">elif</span> <span class="n">bits</span><span class="p">[</span><span class="n">i</span><span class="p">]</span> <span class="o">==</span> <span class="mi">0</span> <span class="ow">and</span> <span class="n">bits</span><span class="p">[</span><span class="n">i</span><span class="o">+</span><span class="mi">1</span><span class="p">]</span> <span class="o">==</span> <span class="mi">1</span> <span class="ow">and</span> <span class="n">bits</span><span class="p">[</span><span class="n">i</span><span class="o">+</span><span class="mi">2</span><span class="p">]</span> <span class="o">==</span> <span class="mi">1</span><span class="p">:</span>
            <span class="n">senal_Tx</span><span class="p">[</span><span class="n">i</span><span class="o">*</span><span class="n">mpp</span><span class="p">:</span> <span class="p">(</span><span class="n">i</span><span class="o">+</span><span class="mi">1</span><span class="p">)</span><span class="o">*</span><span class="n">mpp</span><span class="p">]</span> <span class="o">=</span> <span class="n">portadora_1</span> <span class="o">*</span> <span class="o">-</span><span class="n">h</span> <span class="o">+</span> <span class="n">portadora_2</span> <span class="o">*</span> <span class="n">h</span>
        
        <span class="k">elif</span> <span class="n">bits</span><span class="p">[</span><span class="n">i</span><span class="p">]</span> <span class="o">==</span> <span class="mi">0</span> <span class="ow">and</span> <span class="n">bits</span><span class="p">[</span><span class="n">i</span><span class="o">+</span><span class="mi">1</span><span class="p">]</span> <span class="o">==</span> <span class="mi">0</span> <span class="ow">and</span> <span class="n">bits</span><span class="p">[</span><span class="n">i</span><span class="o">+</span><span class="mi">2</span><span class="p">]</span> <span class="o">==</span> <span class="mi">0</span><span class="p">:</span>
            <span class="n">senal_Tx</span><span class="p">[</span><span class="n">i</span><span class="o">*</span><span class="n">mpp</span><span class="p">:</span> <span class="p">(</span><span class="n">i</span><span class="o">+</span><span class="mi">1</span><span class="p">)</span><span class="o">*</span><span class="n">mpp</span><span class="p">]</span> <span class="o">=</span> <span class="n">portadora_1</span> <span class="o">*</span> <span class="o">-</span><span class="n">h</span> <span class="o">+</span> <span class="n">portadora_2</span> <span class="o">*</span> <span class="o">-</span><span class="n">h</span>
        
        <span class="k">elif</span> <span class="n">bits</span><span class="p">[</span><span class="n">i</span><span class="p">]</span> <span class="o">==</span> <span class="mi">0</span> <span class="ow">and</span> <span class="n">bits</span><span class="p">[</span><span class="n">i</span><span class="o">+</span><span class="mi">1</span><span class="p">]</span> <span class="o">==</span> <span class="mi">1</span> <span class="ow">and</span> <span class="n">bits</span><span class="p">[</span><span class="n">i</span><span class="o">+</span><span class="mi">2</span><span class="p">]</span> <span class="o">==</span> <span class="mi">0</span><span class="p">:</span>
            <span class="n">senal_Tx</span><span class="p">[</span><span class="n">i</span><span class="o">*</span><span class="n">mpp</span><span class="p">:</span> <span class="p">(</span><span class="n">i</span><span class="o">+</span><span class="mi">1</span><span class="p">)</span><span class="o">*</span><span class="n">mpp</span><span class="p">]</span> <span class="o">=</span> <span class="n">portadora_1</span> <span class="o">*</span> <span class="mi">0</span> <span class="o">+</span> <span class="n">portadora_2</span> <span class="o">*</span> <span class="mi">1</span>
        
        <span class="k">elif</span> <span class="n">bits</span><span class="p">[</span><span class="n">i</span><span class="p">]</span> <span class="o">==</span> <span class="mi">0</span> <span class="ow">and</span> <span class="n">bits</span><span class="p">[</span><span class="n">i</span><span class="o">+</span><span class="mi">1</span><span class="p">]</span> <span class="o">==</span> <span class="mi">0</span> <span class="ow">and</span> <span class="n">bits</span><span class="p">[</span><span class="n">i</span><span class="o">+</span><span class="mi">2</span><span class="p">]</span> <span class="o">==</span> <span class="mi">1</span><span class="p">:</span>
            <span class="n">senal_Tx</span><span class="p">[</span><span class="n">i</span><span class="o">*</span><span class="n">mpp</span><span class="p">:</span> <span class="p">(</span><span class="n">i</span><span class="o">+</span><span class="mi">1</span><span class="p">)</span><span class="o">*</span><span class="n">mpp</span><span class="p">]</span> <span class="o">=</span> <span class="n">portadora_1</span> <span class="o">*</span> <span class="o">-</span><span class="mi">1</span> <span class="o">+</span> <span class="n">portadora_2</span> <span class="o">*</span> <span class="mi">0</span>

        <span class="k">else</span><span class="p">:</span>
            <span class="n">senal_Tx</span><span class="p">[</span><span class="n">i</span><span class="o">*</span><span class="n">mpp</span><span class="p">:</span> <span class="p">(</span><span class="n">i</span><span class="o">+</span><span class="mi">1</span><span class="p">)</span><span class="o">*</span><span class="n">mpp</span><span class="p">]</span> <span class="o">=</span> <span class="n">portadora_1</span> <span class="o">*</span> <span class="n">h</span> <span class="o">+</span> <span class="n">portadora_2</span> <span class="o">*</span> <span class="o">-</span><span class="n">h</span>

    <span class="c1"># 5. Calcular la potencia promedio de la señal modulada</span>
    <span class="n">Pm</span> <span class="o">=</span> <span class="p">(</span><span class="mi">1</span> <span class="o">/</span> <span class="p">(</span><span class="n">N</span><span class="o">*</span><span class="n">Tc</span><span class="p">))</span> <span class="o">*</span> <span class="n">np</span><span class="o">.</span><span class="n">trapz</span><span class="p">(</span><span class="nb">pow</span><span class="p">(</span><span class="n">senal_Tx</span><span class="p">,</span> <span class="mi">2</span><span class="p">),</span> <span class="n">t_simulacion</span><span class="p">)</span>

    <span class="k">return</span> <span class="n">senal_Tx</span><span class="p">,</span> <span class="n">Pm</span><span class="p">,</span> <span class="n">portadora_1</span><span class="p">,</span> <span class="n">portadora_2</span>
</pre></div>

    </div>
</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[25]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="kn">import</span> <span class="nn">numpy</span> <span class="k">as</span> <span class="nn">np</span>

<span class="k">def</span> <span class="nf">canal_ruidoso</span><span class="p">(</span><span class="n">senal_Tx</span><span class="p">,</span> <span class="n">Pm</span><span class="p">,</span> <span class="n">SNR</span><span class="p">):</span>
    <span class="sd">&#39;&#39;&#39;Un bloque que simula un medio de trans-</span>
<span class="sd">    misión no ideal (ruidoso) empleando ruido</span>
<span class="sd">    AWGN. Pide por parámetro un vector con la</span>
<span class="sd">    señal provieniente de un modulador y un</span>
<span class="sd">    valor en decibelios para la relación señal</span>
<span class="sd">    a ruido.</span>

<span class="sd">    :param senal_Tx: El vector del modulador</span>
<span class="sd">    :param Pm: Potencia de la señal modulada</span>
<span class="sd">    :param SNR: Relación señal-a-ruido en dB</span>
<span class="sd">    :return: La señal modulada al dejar el canal</span>
<span class="sd">    &#39;&#39;&#39;</span>
    <span class="c1"># Potencia del ruido generado por el canal</span>
    <span class="n">Pn</span> <span class="o">=</span> <span class="n">Pm</span> <span class="o">/</span> <span class="nb">pow</span><span class="p">(</span><span class="mi">10</span><span class="p">,</span> <span class="n">SNR</span><span class="o">/</span><span class="mi">10</span><span class="p">)</span>

    <span class="c1"># Generando ruido auditivo blanco gaussiano (potencia = varianza)</span>
    <span class="n">ruido</span> <span class="o">=</span> <span class="n">np</span><span class="o">.</span><span class="n">random</span><span class="o">.</span><span class="n">normal</span><span class="p">(</span><span class="mi">0</span><span class="p">,</span> <span class="n">np</span><span class="o">.</span><span class="n">sqrt</span><span class="p">(</span><span class="n">Pn</span><span class="p">),</span> <span class="n">senal_Tx</span><span class="o">.</span><span class="n">shape</span><span class="p">)</span>

    <span class="c1"># Señal distorsionada por el canal ruidoso</span>
    <span class="n">senal_Rx</span> <span class="o">=</span> <span class="n">senal_Tx</span> <span class="o">+</span> <span class="n">ruido</span>

    <span class="k">return</span> <span class="n">senal_Rx</span>
</pre></div>

    </div>
</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[26]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="c1">############################## demodulador ###############################            </span>
             
<span class="kn">import</span> <span class="nn">numpy</span> <span class="k">as</span> <span class="nn">np</span> 
 
<span class="k">def</span> <span class="nf">demodulador8</span><span class="p">(</span><span class="n">senal_Rx</span><span class="p">,</span> <span class="n">portadora_1</span><span class="p">,</span> <span class="n">portadora_2</span><span class="p">,</span> <span class="n">mpp</span><span class="p">):</span> 
    <span class="sd">&#39;&#39;&#39;Un método que simula un bloque demodulador </span>
<span class="sd">    de señales, bajo un esquema 8-PSK. El criterio </span>
<span class="sd">    de demodulación se basa en decodificación por  </span>
<span class="sd">    detección de energía. </span>
<span class="sd"> </span>
<span class="sd">    :param senal_Rx: La señal recibida del canal </span>
<span class="sd">    :param portadora: La onda portadora c(t) </span>
<span class="sd">    :param mpp: Número de muestras por periodo </span>
<span class="sd">    :return: Los bits de la señal demodulada </span>
<span class="sd">    &#39;&#39;&#39;</span> 
    <span class="c1"># Cantidad de muestras en senal_Rx </span>
    <span class="n">M</span> <span class="o">=</span> <span class="nb">len</span><span class="p">(</span><span class="n">senal_Rx</span><span class="p">)</span> 
 
    <span class="c1"># Cantidad de bits (símbolos) en transmisión </span>
    <span class="n">N</span> <span class="o">=</span> <span class="nb">int</span><span class="p">(</span><span class="n">M</span> <span class="o">/</span> <span class="n">mpp</span><span class="p">)</span> 
 
    <span class="c1"># Vector para bits obtenidos por la demodulación </span>
    <span class="n">bits_Rx</span> <span class="o">=</span> <span class="n">np</span><span class="o">.</span><span class="n">zeros</span><span class="p">(</span><span class="n">N</span><span class="p">)</span> 
 
    <span class="c1"># Vector para la señal demodulada </span>
    <span class="n">senal_demodulada</span> <span class="o">=</span> <span class="n">np</span><span class="o">.</span><span class="n">zeros</span><span class="p">(</span><span class="n">senal_Rx</span><span class="o">.</span><span class="n">shape</span><span class="p">)</span> 
 
    <span class="c1"># Pseudo-Energía de un período de la portadora: </span>
    <span class="n">X</span> <span class="o">=</span> <span class="mi">0</span>

    <span class="k">for</span> <span class="n">i</span> <span class="ow">in</span> <span class="nb">range</span><span class="p">(</span><span class="n">N</span><span class="p">):</span>

        <span class="k">if</span> <span class="n">X</span><span class="o">+</span><span class="mi">3</span> <span class="o">&gt;</span> <span class="n">N</span><span class="p">:</span>  
            <span class="k">break</span>   

    <span class="c1"># Demodulación</span>
     <span class="c1"># Producto interno de dos funciones</span>
        <span class="n">producto_1</span> <span class="o">=</span> <span class="n">senal_Rx</span><span class="p">[</span><span class="n">i</span><span class="o">*</span><span class="n">mpp</span><span class="p">:</span> <span class="p">(</span><span class="n">i</span><span class="o">+</span><span class="mi">1</span><span class="p">)</span><span class="o">*</span><span class="n">mpp</span><span class="p">]</span> <span class="o">*</span> <span class="n">portadora_1</span>
        <span class="n">producto_2</span> <span class="o">=</span> <span class="n">senal_Rx</span><span class="p">[</span><span class="n">i</span><span class="o">*</span><span class="n">mpp</span><span class="p">:</span> <span class="p">(</span><span class="n">i</span><span class="o">+</span><span class="mi">1</span><span class="p">)</span><span class="o">*</span><span class="n">mpp</span><span class="p">]</span> <span class="o">*</span> <span class="n">portadora_2</span>
        <span class="n">senal_demodulada</span><span class="p">[</span><span class="n">i</span><span class="o">*</span><span class="n">mpp</span><span class="p">:</span> <span class="p">(</span><span class="n">i</span><span class="o">+</span><span class="mi">1</span><span class="p">)</span><span class="o">*</span><span class="n">mpp</span><span class="p">]</span> <span class="o">=</span> <span class="n">producto_1</span> <span class="o">+</span> <span class="n">producto_2</span>
    
    <span class="c1">#Secuencia lógica.</span>
        <span class="k">if</span> <span class="n">np</span><span class="o">.</span><span class="n">sum</span><span class="p">(</span><span class="n">producto_1</span><span class="p">)</span> <span class="o">&gt;=</span> <span class="mi">1</span><span class="p">:</span>
            <span class="n">bits_Rx</span><span class="p">[</span><span class="n">X</span><span class="p">]</span> <span class="o">=</span> <span class="mi">1</span> 
            
        <span class="k">if</span> <span class="n">np</span><span class="o">.</span><span class="n">sum</span><span class="p">(</span><span class="n">producto_2</span><span class="p">)</span> <span class="o">==</span> <span class="o">-</span><span class="mi">1</span><span class="p">:</span>
            <span class="n">bits_Rx</span><span class="p">[</span><span class="n">X</span><span class="p">]</span> <span class="o">=</span> <span class="mi">1</span>  <span class="c1"># </span>
     
        <span class="k">if</span> <span class="n">np</span><span class="o">.</span><span class="n">sum</span><span class="p">(</span><span class="n">producto_2</span><span class="p">)</span> <span class="o">&gt;=</span> <span class="mf">0.707</span><span class="p">:</span>
            <span class="n">bits_Rx</span><span class="p">[</span><span class="n">X</span><span class="o">+</span><span class="mi">1</span><span class="p">]</span> <span class="o">=</span> <span class="mi">1</span>  
        
        <span class="k">if</span> <span class="n">np</span><span class="o">.</span><span class="n">sum</span><span class="p">(</span><span class="n">producto_1</span><span class="p">)</span> <span class="o">==</span> <span class="mi">1</span><span class="p">:</span>
            <span class="n">bits_Rx</span><span class="p">[</span><span class="n">X</span><span class="o">+</span><span class="mi">1</span><span class="p">]</span> <span class="o">=</span> <span class="mi">1</span>  

        <span class="k">if</span> <span class="n">np</span><span class="o">.</span><span class="n">sum</span><span class="p">(</span><span class="n">producto_2</span><span class="p">)</span> <span class="o">==</span> <span class="mi">0</span><span class="p">:</span>
            <span class="n">bits_Rx</span><span class="p">[</span><span class="n">X</span><span class="o">+</span><span class="mi">2</span><span class="p">]</span> <span class="o">=</span> <span class="mi">1</span>  <span class="c1">#</span>

        <span class="k">if</span> <span class="n">np</span><span class="o">.</span><span class="n">sum</span><span class="p">(</span><span class="n">producto_2</span><span class="p">)</span> <span class="o">==</span> <span class="mf">0.707</span><span class="p">:</span>
            <span class="n">bits_Rx</span><span class="p">[</span><span class="n">X</span><span class="o">+</span><span class="mi">2</span><span class="p">]</span> <span class="o">=</span> <span class="mi">1</span> 

        <span class="k">if</span> <span class="n">np</span><span class="o">.</span><span class="n">sum</span><span class="p">(</span><span class="n">producto_1</span><span class="p">)</span> <span class="o">==</span> <span class="mf">0.707</span><span class="p">:</span>
            <span class="n">bits_Rx</span><span class="p">[</span><span class="n">X</span><span class="o">+</span><span class="mi">2</span><span class="p">]</span> <span class="o">=</span> <span class="mi">1</span>  
        <span class="n">X</span> <span class="o">+=</span> <span class="mi">3</span>
        
    <span class="k">return</span> <span class="n">bits_Rx</span><span class="o">.</span><span class="n">astype</span><span class="p">(</span><span class="nb">int</span><span class="p">),</span> <span class="n">senal_demodulada</span>
</pre></div>

    </div>
</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[27]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="kn">import</span> <span class="nn">numpy</span> <span class="k">as</span> <span class="nn">np</span>

<span class="k">def</span> <span class="nf">bits_a_rgb</span><span class="p">(</span><span class="n">bits_Rx</span><span class="p">,</span> <span class="n">dimensiones</span><span class="p">):</span>
    <span class="sd">&#39;&#39;&#39;Un blque que decodifica el los bits</span>
<span class="sd">    recuperados en el proceso de demodulación</span>

<span class="sd">    :param: Un vector de bits 1 x k </span>
<span class="sd">    :param dimensiones: Tupla con dimensiones de la img.</span>
<span class="sd">    :return: Un array con los pixeles reconstruidos</span>
<span class="sd">    &#39;&#39;&#39;</span>
    <span class="c1"># Cantidad de bits</span>
    <span class="n">N</span> <span class="o">=</span> <span class="nb">len</span><span class="p">(</span><span class="n">bits_Rx</span><span class="p">)</span>

    <span class="c1"># Se reconstruyen los canales RGB</span>
    <span class="n">bits</span> <span class="o">=</span> <span class="n">np</span><span class="o">.</span><span class="n">split</span><span class="p">(</span><span class="n">bits_Rx</span><span class="p">,</span> <span class="n">N</span> <span class="o">/</span> <span class="mi">8</span><span class="p">)</span>

    <span class="c1"># Se decofican los canales:</span>
    <span class="n">canales</span> <span class="o">=</span> <span class="p">[</span><span class="nb">int</span><span class="p">(</span><span class="s1">&#39;&#39;</span><span class="o">.</span><span class="n">join</span><span class="p">(</span><span class="nb">map</span><span class="p">(</span><span class="nb">str</span><span class="p">,</span> <span class="n">canal</span><span class="p">)),</span> <span class="mi">2</span><span class="p">)</span> <span class="k">for</span> <span class="n">canal</span> <span class="ow">in</span> <span class="n">bits</span><span class="p">]</span>
    <span class="n">pixeles</span> <span class="o">=</span> <span class="n">np</span><span class="o">.</span><span class="n">reshape</span><span class="p">(</span><span class="n">canales</span><span class="p">,</span> <span class="n">dimensiones</span><span class="p">)</span>

    <span class="k">return</span> <span class="n">pixeles</span><span class="o">.</span><span class="n">astype</span><span class="p">(</span><span class="n">np</span><span class="o">.</span><span class="n">uint8</span><span class="p">)</span>
</pre></div>

    </div>
</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[28]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="kn">import</span> <span class="nn">numpy</span> <span class="k">as</span> <span class="nn">np</span>
<span class="kn">import</span> <span class="nn">matplotlib.pyplot</span> <span class="k">as</span> <span class="nn">plt</span>
<span class="kn">import</span> <span class="nn">time</span>

<span class="c1"># Parámetros</span>
<span class="n">fc</span> <span class="o">=</span> <span class="mi">5000</span>  <span class="c1"># frecuencia de la portadora</span>
<span class="n">mpp</span> <span class="o">=</span> <span class="mi">20</span>   <span class="c1"># muestras por periodo de la portadora</span>
<span class="n">SNR</span> <span class="o">=</span> <span class="mi">15</span>   <span class="c1"># relación señal-a-ruido del canal</span>

<span class="c1"># Iniciar medición del tiempo de simulación</span>
<span class="n">inicio</span> <span class="o">=</span> <span class="n">time</span><span class="o">.</span><span class="n">time</span><span class="p">()</span>

<span class="c1"># 1. Importar y convertir la imagen a trasmitir</span>
<span class="n">imagen_Tx</span> <span class="o">=</span> <span class="n">fuente_info</span><span class="p">(</span><span class="s1">&#39;arenal.jpg&#39;</span><span class="p">)</span>
<span class="n">dimensiones</span> <span class="o">=</span> <span class="n">imagen_Tx</span><span class="o">.</span><span class="n">shape</span>

<span class="c1"># 2. Codificar los pixeles de la imagen</span>
<span class="n">bits_Tx</span> <span class="o">=</span> <span class="n">rgb_a_bit</span><span class="p">(</span><span class="n">imagen_Tx</span><span class="p">)</span>

<span class="c1"># 3. Modular la cadena de bits usando el esquema 8-PSK</span>
<span class="n">senal_Tx</span><span class="p">,</span> <span class="n">Pm</span><span class="p">,</span> <span class="n">portadora_1</span><span class="p">,</span> <span class="n">portadora_2</span> <span class="o">=</span> <span class="n">modulador8</span><span class="p">(</span><span class="n">bits_Tx</span><span class="p">,</span> <span class="n">fc</span><span class="p">,</span> <span class="n">mpp</span><span class="p">)</span>

<span class="c1"># 4. Se transmite la señal modulada, por un canal ruidoso</span>
<span class="n">senal_Rx</span> <span class="o">=</span> <span class="n">canal_ruidoso</span><span class="p">(</span><span class="n">senal_Tx</span><span class="p">,</span> <span class="n">Pm</span><span class="p">,</span> <span class="n">SNR</span><span class="p">)</span>

<span class="c1"># 5. Se desmodula la señal recibida del canal</span>
<span class="n">bits_Rx</span><span class="p">,</span> <span class="n">senal_demodulada</span> <span class="o">=</span> <span class="n">demodulador8</span><span class="p">(</span><span class="n">senal_Rx</span><span class="p">,</span> <span class="n">portadora_1</span><span class="p">,</span> <span class="n">portadora_2</span><span class="p">,</span> <span class="n">mpp</span><span class="p">)</span>

<span class="c1"># 6. Se visualiza la imagen recibida </span>
<span class="n">imagen_Rx</span> <span class="o">=</span> <span class="n">bits_a_rgb</span><span class="p">(</span><span class="n">bits_Rx</span><span class="p">,</span> <span class="n">dimensiones</span><span class="p">)</span>
<span class="n">Fig</span> <span class="o">=</span> <span class="n">plt</span><span class="o">.</span><span class="n">figure</span><span class="p">(</span><span class="n">figsize</span><span class="o">=</span><span class="p">(</span><span class="mi">10</span><span class="p">,</span><span class="mi">6</span><span class="p">))</span>

<span class="c1"># Cálculo del tiempo de simulación</span>
<span class="nb">print</span><span class="p">(</span><span class="s1">&#39;Duración de la simulación: &#39;</span><span class="p">,</span> <span class="n">time</span><span class="o">.</span><span class="n">time</span><span class="p">()</span> <span class="o">-</span> <span class="n">inicio</span><span class="p">)</span>

<span class="c1"># 7. Calcular número de errores</span>
<span class="n">errores</span> <span class="o">=</span> <span class="nb">sum</span><span class="p">(</span><span class="nb">abs</span><span class="p">(</span><span class="n">bits_Tx</span> <span class="o">-</span> <span class="n">bits_Rx</span><span class="p">))</span>
<span class="n">BER</span> <span class="o">=</span> <span class="n">errores</span><span class="o">/</span><span class="nb">len</span><span class="p">(</span><span class="n">bits_Tx</span><span class="p">)</span>
<span class="nb">print</span><span class="p">(</span><span class="s1">&#39;</span><span class="si">{}</span><span class="s1"> errores, para un BER de </span><span class="si">{:0.4f}</span><span class="s1">.&#39;</span><span class="o">.</span><span class="n">format</span><span class="p">(</span><span class="n">errores</span><span class="p">,</span> <span class="n">BER</span><span class="p">))</span>

<span class="c1"># Mostrar imagen transmitida</span>
<span class="n">ax</span> <span class="o">=</span> <span class="n">Fig</span><span class="o">.</span><span class="n">add_subplot</span><span class="p">(</span><span class="mi">1</span><span class="p">,</span> <span class="mi">2</span><span class="p">,</span> <span class="mi">1</span><span class="p">)</span>
<span class="n">imgplot</span> <span class="o">=</span> <span class="n">plt</span><span class="o">.</span><span class="n">imshow</span><span class="p">(</span><span class="n">imagen_Tx</span><span class="p">)</span>
<span class="n">ax</span><span class="o">.</span><span class="n">set_title</span><span class="p">(</span><span class="s1">&#39;Transmitido&#39;</span><span class="p">)</span>

<span class="c1"># Mostrar imagen recuperada</span>
<span class="n">ax</span> <span class="o">=</span> <span class="n">Fig</span><span class="o">.</span><span class="n">add_subplot</span><span class="p">(</span><span class="mi">1</span><span class="p">,</span> <span class="mi">2</span><span class="p">,</span> <span class="mi">2</span><span class="p">)</span>
<span class="n">imgplot</span> <span class="o">=</span> <span class="n">plt</span><span class="o">.</span><span class="n">imshow</span><span class="p">(</span><span class="n">imagen_Rx</span><span class="p">)</span>
<span class="n">ax</span><span class="o">.</span><span class="n">set_title</span><span class="p">(</span><span class="s1">&#39;Recuperado&#39;</span><span class="p">)</span>
<span class="n">Fig</span><span class="o">.</span><span class="n">tight_layout</span><span class="p">()</span>

<span class="n">plt</span><span class="o">.</span><span class="n">imshow</span><span class="p">(</span><span class="n">imagen_Rx</span><span class="p">)</span>


<span class="kn">import</span> <span class="nn">matplotlib.pyplot</span> <span class="k">as</span> <span class="nn">plt</span>

<span class="c1"># Visualizar el cambio entre las señales</span>
<span class="n">fig</span><span class="p">,</span> <span class="p">(</span><span class="n">ax1</span><span class="p">,</span> <span class="n">ax2</span><span class="p">,</span> <span class="n">ax3</span><span class="p">,</span> <span class="n">ax4</span><span class="p">)</span> <span class="o">=</span> <span class="n">plt</span><span class="o">.</span><span class="n">subplots</span><span class="p">(</span><span class="n">nrows</span><span class="o">=</span><span class="mi">4</span><span class="p">,</span> <span class="n">sharex</span><span class="o">=</span><span class="kc">True</span><span class="p">,</span> <span class="n">figsize</span><span class="o">=</span><span class="p">(</span><span class="mi">14</span><span class="p">,</span> <span class="mi">7</span><span class="p">))</span>

<span class="c1"># La onda cuadrada moduladora (bits de entrada)</span>
<span class="n">ax1</span><span class="o">.</span><span class="n">plot</span><span class="p">(</span><span class="n">moduladora</span><span class="p">[</span><span class="mi">0</span><span class="p">:</span><span class="mi">600</span><span class="p">],</span> <span class="n">color</span><span class="o">=</span><span class="s1">&#39;r&#39;</span><span class="p">,</span> <span class="n">lw</span><span class="o">=</span><span class="mi">2</span><span class="p">)</span> 
<span class="n">ax1</span><span class="o">.</span><span class="n">set_ylabel</span><span class="p">(</span><span class="s1">&#39;$b(t)$&#39;</span><span class="p">)</span>

<span class="c1"># La señal modulada por BPSK</span>
<span class="n">ax2</span><span class="o">.</span><span class="n">plot</span><span class="p">(</span><span class="n">senal_Tx</span><span class="p">[</span><span class="mi">0</span><span class="p">:</span><span class="mi">600</span><span class="p">],</span> <span class="n">color</span><span class="o">=</span><span class="s1">&#39;g&#39;</span><span class="p">,</span> <span class="n">lw</span><span class="o">=</span><span class="mi">2</span><span class="p">)</span> 
<span class="n">ax2</span><span class="o">.</span><span class="n">set_ylabel</span><span class="p">(</span><span class="s1">&#39;$s(t)$&#39;</span><span class="p">)</span>

<span class="c1"># La señal modulada al dejar el canal</span>
<span class="n">ax3</span><span class="o">.</span><span class="n">plot</span><span class="p">(</span><span class="n">senal_Rx</span><span class="p">[</span><span class="mi">0</span><span class="p">:</span><span class="mi">600</span><span class="p">],</span> <span class="n">color</span><span class="o">=</span><span class="s1">&#39;b&#39;</span><span class="p">,</span> <span class="n">lw</span><span class="o">=</span><span class="mi">2</span><span class="p">)</span> 
<span class="n">ax3</span><span class="o">.</span><span class="n">set_ylabel</span><span class="p">(</span><span class="s1">&#39;$s(t) + n(t)$&#39;</span><span class="p">)</span>

<span class="c1"># La señal demodulada</span>
<span class="n">ax4</span><span class="o">.</span><span class="n">plot</span><span class="p">(</span><span class="n">senal_demodulada</span><span class="p">[</span><span class="mi">0</span><span class="p">:</span><span class="mi">600</span><span class="p">],</span> <span class="n">color</span><span class="o">=</span><span class="s1">&#39;m&#39;</span><span class="p">,</span> <span class="n">lw</span><span class="o">=</span><span class="mi">2</span><span class="p">)</span> 
<span class="n">ax4</span><span class="o">.</span><span class="n">set_ylabel</span><span class="p">(</span><span class="s1">&#39;$b^{\prime}(t)$&#39;</span><span class="p">)</span>
<span class="n">ax4</span><span class="o">.</span><span class="n">set_xlabel</span><span class="p">(</span><span class="s1">&#39;$t$ / milisegundos&#39;</span><span class="p">)</span>
<span class="n">fig</span><span class="o">.</span><span class="n">tight_layout</span><span class="p">()</span>
<span class="n">plt</span><span class="o">.</span><span class="n">show</span><span class="p">()</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt"></div>


<div class="output_subarea output_stream output_stdout output_text">
<pre>Duración de la simulación:  6.527757406234741
220438 errores, para un BER de 0.5212.
</pre>
</div>
</div>

<div class="output_area">

    <div class="prompt"></div>




<div class="output_png output_subarea ">
<img src="data:image/png;base64,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
"
>
</div>

</div>

<div class="output_area">

    <div class="prompt"></div>




<div class="output_png output_subarea ">
<img src="data:image/png;base64,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0CuJUmqnk00BiJZj7FCpGDtUKsYOlYqxQ+Vg/FCpwhQ7AW/rR0RERERERES5MEEnIiIiIiIiWgGYoAfnVtMFoIrF2KFSMXaoVIwdKhVjh8rB+KFShSZ2uAadiIiIiIiIaAXgCDoRERERERHRCsAEnYiIiIiIiGgFYIJOREREREREtAIwQSciIiIiIiJaAZigExEREREREa0ATNCJiIiIiIiIVgAm6EREREREREQrABN0IiIiIiIiohWACToRERERERHRCsAEnYiIiIiIiGgFYIJOREREREREtAJUmS5AOTo7O/WGDRtMF4OIiIiIiIgor127dg1rrbuKva6iE/QNGzZg586dpotBRERERERElJdS6oiT162oKe5KqW8ppQaVUs+bLgsRERERERFRkFZUgg7gDgBvNF0IkmNwehDDM8Omi0GUtWd4D9I6bboYoTCXnDNdhFCbT87j4MhB08UIDcarP3heqVKkdRrxVNx0MWgFWFEJutb6YQAjpstRSR45+gjedufbsP3W7Tg1dcp0cSrK/tP7sfX/bMWFt1yIqfiU6eKEntYa337m27j8m5fj2h9cC6216SKtON966ls492vn4gP/9gGenzKkdRo3P3gzGj/biK8+/lXTxQmtG++5EZu/uhnffPKbpotS0cbmxvD73/19dPx9B3534nemixMaxyeO47LbLsO6L63DS2MvmS4O2Tx85GG89c634rLbLsPg9KDp4qwID730EFZ/YTWuuuMqdtLTykrQnVBK3aSU2qmU2jk0NGS6OEYdGj2E1377tbhn3z3Y1b8Ltz91u+kiVYyp+BSuuesajM2NoX+qH7fuutV0kULvu899Fx/4tw/gseOP4Ycv/BCPn3jcdJFWlEQqgU8//GkAwL8++6/4p8f/yXCJKtfH7v8YPvfI55DSKfzdb/8OyXTSdJFCZ+/wXnz32e8CAP7sZ3/GxLJEiVQCr7njNbj/wP2YSczgi49+0XSRQmFkdgQ7/nkHnjj5BIZnhvGNnd8wXSRasO/0Przu26/DvfvuxRMnn8C/PP0vpotk3G+O/AZXf+dqDEwP4LHjj+HBQw+aLhIZVnEJutb6Vq31dq319q6uopvghdrP9v8M8VQcvY29AIDv7f6e4RJVjtt23YbdQ7vRWd8JAPjH//hHzCfnDZcq3H784o8BAKubVgMAvvc849Xue89/Dy+N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
"
>
</div>

</div>

</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h3 id="4.2.---Estacionaridad-y-ergodicidad">4.2. - Estacionaridad y ergodicidad<a class="anchor-link" href="#4.2.---Estacionaridad-y-ergodicidad">&#182;</a></h3><ul>
<li>(30%) Realice pruebas de estacionaridad y ergodicidad a la señal modulada <code>senal_Tx</code> y obtenga conclusiones sobre estas.</li>
</ul>

</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[29]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="c1">#4.2 Estacionaridad y ergodicidad</span>

<span class="kn">import</span> <span class="nn">numpy</span> <span class="k">as</span> <span class="nn">np</span>

<span class="c1"># Definir los tiempos</span>
<span class="n">T</span> <span class="o">=</span> <span class="mi">100</span>
<span class="n">t1</span> <span class="o">=</span> <span class="mf">0.1</span>
<span class="n">t</span> <span class="o">=</span> <span class="n">np</span><span class="o">.</span><span class="n">linspace</span><span class="p">(</span><span class="mi">0</span><span class="p">,</span> <span class="n">t1</span><span class="p">,</span> <span class="n">T</span><span class="p">)</span>
    
<span class="c1"># Inicialización proceso aleatorio X(t):</span>
<span class="n">A</span> <span class="o">=</span> <span class="p">[</span><span class="o">-</span><span class="mi">1</span><span class="p">,</span> <span class="mi">1</span><span class="p">]</span>            <span class="c1"># Valores para la amplitud</span>
<span class="n">N</span> <span class="o">=</span> <span class="mi">8</span>                      <span class="c1"># Hay 8 posibilidades de la onda </span>
<span class="n">junto</span> <span class="o">=</span> <span class="n">np</span><span class="o">.</span><span class="n">empty</span><span class="p">((</span><span class="n">N</span><span class="p">,</span> <span class="nb">len</span><span class="p">(</span><span class="n">t</span><span class="p">)))</span>    <span class="c1"># N funciones del tiempo x(t) con T puntos</span>

<span class="c1"># Se aplica cada valor de amplitud entre (-1, 1) para la señal</span>
<span class="k">for</span> <span class="n">i</span> <span class="ow">in</span> <span class="n">A</span><span class="p">:</span>
    <span class="n">B</span> <span class="o">=</span> <span class="n">i</span><span class="o">*</span><span class="n">np</span><span class="o">.</span><span class="n">cos</span><span class="p">(</span><span class="mi">2</span><span class="o">*</span><span class="n">np</span><span class="o">.</span><span class="n">pi</span><span class="o">*</span><span class="n">fc</span><span class="o">*</span><span class="n">t</span><span class="p">)</span> <span class="o">+</span> <span class="n">i</span><span class="o">*</span><span class="n">np</span><span class="o">.</span><span class="n">sin</span><span class="p">(</span><span class="mi">2</span><span class="o">*</span><span class="n">np</span><span class="o">.</span><span class="n">pi</span><span class="o">*</span><span class="n">fc</span><span class="o">*</span><span class="n">t</span><span class="p">)</span>
    <span class="n">C</span> <span class="o">=</span> <span class="o">-</span><span class="n">i</span><span class="o">*</span><span class="n">np</span><span class="o">.</span><span class="n">cos</span><span class="p">(</span><span class="mi">2</span><span class="o">*</span><span class="n">np</span><span class="o">.</span><span class="n">pi</span><span class="o">*</span><span class="n">fc</span><span class="o">*</span><span class="n">t</span><span class="p">)</span> <span class="o">+</span> <span class="n">i</span><span class="o">*</span><span class="n">np</span><span class="o">.</span><span class="n">sin</span><span class="p">(</span><span class="mi">2</span><span class="o">*</span><span class="n">np</span><span class="o">.</span><span class="n">pi</span><span class="o">*</span><span class="n">fc</span><span class="o">*</span><span class="n">t</span><span class="p">)</span>
    <span class="n">D</span> <span class="o">=</span> <span class="n">i</span><span class="o">*</span><span class="n">np</span><span class="o">.</span><span class="n">cos</span><span class="p">(</span><span class="mi">2</span><span class="o">*</span><span class="n">np</span><span class="o">.</span><span class="n">pi</span><span class="o">*</span><span class="n">fc</span><span class="o">*</span><span class="n">t</span><span class="p">)</span> <span class="o">+</span> <span class="o">-</span><span class="n">i</span><span class="o">*</span><span class="n">np</span><span class="o">.</span><span class="n">sin</span><span class="p">(</span><span class="mi">2</span><span class="o">*</span><span class="n">np</span><span class="o">.</span><span class="n">pi</span><span class="o">*</span><span class="n">fc</span><span class="o">*</span><span class="n">t</span><span class="p">)</span>
    <span class="n">E</span> <span class="o">=</span> <span class="o">-</span><span class="n">i</span><span class="o">*</span><span class="n">np</span><span class="o">.</span><span class="n">cos</span><span class="p">(</span><span class="mi">2</span><span class="o">*</span><span class="n">np</span><span class="o">.</span><span class="n">pi</span><span class="o">*</span><span class="n">fc</span><span class="o">*</span><span class="n">t</span><span class="p">)</span> <span class="o">+</span> <span class="o">-</span><span class="n">i</span><span class="o">*</span><span class="n">np</span><span class="o">.</span><span class="n">sin</span><span class="p">(</span><span class="mi">2</span><span class="o">*</span><span class="n">np</span><span class="o">.</span><span class="n">pi</span><span class="o">*</span><span class="n">fc</span><span class="o">*</span><span class="n">t</span><span class="p">)</span>
    <span class="n">junto</span><span class="p">[</span><span class="n">i</span><span class="p">,:]</span>   <span class="o">=</span> <span class="n">B</span>
    <span class="n">junto</span><span class="p">[</span><span class="n">i</span><span class="o">+</span><span class="mi">1</span><span class="p">,:]</span> <span class="o">=</span> <span class="n">C</span>
    <span class="n">junto</span><span class="p">[</span><span class="n">i</span><span class="o">+</span><span class="mi">2</span><span class="p">,:]</span> <span class="o">=</span> <span class="n">D</span>
    <span class="n">junto</span><span class="p">[</span><span class="n">i</span><span class="o">+</span><span class="mi">3</span><span class="p">,:]</span> <span class="o">=</span> <span class="n">E</span>
    <span class="n">plt</span><span class="o">.</span><span class="n">plot</span><span class="p">(</span><span class="n">t</span><span class="p">,</span> <span class="n">B</span><span class="p">)</span>
    <span class="n">plt</span><span class="o">.</span><span class="n">plot</span><span class="p">(</span><span class="n">t</span><span class="p">,</span> <span class="n">C</span><span class="p">)</span>
    <span class="n">plt</span><span class="o">.</span><span class="n">plot</span><span class="p">(</span><span class="n">t</span><span class="p">,</span> <span class="n">D</span><span class="p">)</span>
    <span class="n">plt</span><span class="o">.</span><span class="n">plot</span><span class="p">(</span><span class="n">t</span><span class="p">,</span> <span class="n">E</span><span class="p">)</span>

<span class="c1"># Promedio de las N realizaciones por instante</span>

<span class="n">P</span> <span class="o">=</span> <span class="p">[</span><span class="n">np</span><span class="o">.</span><span class="n">mean</span><span class="p">(</span><span class="n">junto</span><span class="p">[:,</span><span class="n">i</span><span class="p">])</span> <span class="k">for</span> <span class="n">i</span> <span class="ow">in</span> <span class="nb">range</span><span class="p">(</span><span class="nb">len</span><span class="p">(</span><span class="n">t</span><span class="p">))]</span>
<span class="n">Rea</span><span class="p">,</span> <span class="o">=</span> <span class="n">plt</span><span class="o">.</span><span class="n">plot</span><span class="p">(</span><span class="n">t</span><span class="p">,</span> <span class="n">P</span><span class="p">,</span> <span class="n">lw</span><span class="o">=</span><span class="mi">6</span><span class="p">,</span> <span class="n">color</span> <span class="o">=</span> <span class="s1">&#39;blue&#39;</span><span class="p">,</span> <span class="n">label</span><span class="o">=</span><span class="s1">&#39;Promedio de realizaciones&#39;</span><span class="p">)</span>

<span class="c1"># Graficar el resultado teórico del valor esperado</span>

<span class="n">E</span> <span class="o">=</span> <span class="n">np</span><span class="o">.</span><span class="n">mean</span><span class="p">(</span><span class="n">senal_Tx</span><span class="p">)</span><span class="o">*</span><span class="n">t</span>
<span class="n">Teo</span><span class="p">,</span> <span class="o">=</span> <span class="n">plt</span><span class="o">.</span><span class="n">plot</span><span class="p">(</span><span class="n">t</span><span class="p">,</span> <span class="n">E</span><span class="p">,</span> <span class="s1">&#39;-.&#39;</span><span class="p">,</span> <span class="n">lw</span><span class="o">=</span><span class="mi">3</span><span class="p">,</span> <span class="n">color</span> <span class="o">=</span> <span class="s1">&#39;r&#39;</span><span class="p">,</span> <span class="n">label</span><span class="o">=</span><span class="s1">&#39;Valor teorico&#39;</span><span class="p">)</span>

<span class="c1"># Muestra las realizaciones y su promedio teórico calculado (teórico)</span>
<span class="n">plt</span><span class="o">.</span><span class="n">title</span><span class="p">(</span><span class="s1">&#39;Realizaciones del proceso aleatorio $X(t)$&#39;</span><span class="p">)</span>
<span class="n">plt</span><span class="o">.</span><span class="n">xlabel</span><span class="p">(</span><span class="s1">&#39;$t$&#39;</span><span class="p">)</span>
<span class="n">plt</span><span class="o">.</span><span class="n">ylabel</span><span class="p">(</span><span class="s1">&#39;$x_i(t)$&#39;</span><span class="p">)</span>
<span class="n">plt</span><span class="o">.</span><span class="n">legend</span><span class="p">([</span><span class="n">Rea</span><span class="p">,</span> <span class="n">Teo</span><span class="p">],</span> <span class="p">[</span><span class="s1">&#39;Promedio de realizaciones&#39;</span><span class="p">,</span> <span class="s1">&#39;Valor teórico&#39;</span><span class="p">])</span>
<span class="n">plt</span><span class="o">.</span><span class="n">show</span><span class="p">()</span>   

<span class="c1">#T valores de desplazamiento en tau</span>
<span class="n">desplazamiento</span> <span class="o">=</span> <span class="n">np</span><span class="o">.</span><span class="n">arange</span><span class="p">(</span><span class="n">T</span><span class="p">)</span>
<span class="n">taus</span> <span class="o">=</span> <span class="n">desplazamiento</span><span class="o">/</span><span class="n">t1</span>

<span class="c1"># Inicialización de matriz de valores de correlación para las N funciones</span>
<span class="n">corr</span> <span class="o">=</span> <span class="n">np</span><span class="o">.</span><span class="n">empty</span><span class="p">((</span><span class="n">N</span><span class="p">,</span> <span class="nb">len</span><span class="p">(</span><span class="n">desplazamiento</span><span class="p">)))</span>

<span class="c1"># Nueva figura autocorrelación:</span>
<span class="n">plt</span><span class="o">.</span><span class="n">figure</span><span class="p">()</span>

<span class="c1"># Correlación para cada valor de tau</span>
<span class="k">for</span> <span class="n">n</span> <span class="ow">in</span> <span class="nb">range</span><span class="p">(</span><span class="n">N</span><span class="p">):</span>
    <span class="k">for</span> <span class="n">i</span><span class="p">,</span> <span class="n">tau</span> <span class="ow">in</span> <span class="nb">enumerate</span><span class="p">(</span><span class="n">desplazamiento</span><span class="p">):</span>
        <span class="n">corr</span><span class="p">[</span><span class="n">n</span><span class="p">,</span> <span class="n">i</span><span class="p">]</span> <span class="o">=</span> <span class="n">np</span><span class="o">.</span><span class="n">correlate</span><span class="p">(</span><span class="n">junto</span><span class="p">[</span><span class="n">n</span><span class="p">,:],</span> <span class="n">np</span><span class="o">.</span><span class="n">roll</span><span class="p">(</span><span class="n">junto</span><span class="p">[</span><span class="n">n</span><span class="p">,:],</span> <span class="n">tau</span><span class="p">))</span><span class="o">/</span><span class="n">T</span>
    <span class="n">plt</span><span class="o">.</span><span class="n">plot</span><span class="p">(</span><span class="n">taus</span><span class="p">,</span> <span class="n">corr</span><span class="p">[</span><span class="n">n</span><span class="p">,:])</span>

<span class="c1"># Valor teórico de correlación</span>
<span class="n">Rxx</span> <span class="o">=</span> <span class="p">(</span><span class="mf">0.5</span> <span class="o">-</span> <span class="n">np</span><span class="o">.</span><span class="n">power</span><span class="p">(</span><span class="mf">0.25</span><span class="p">,</span><span class="mi">2</span><span class="p">))</span> <span class="o">*</span> <span class="n">np</span><span class="o">.</span><span class="n">cos</span><span class="p">(</span><span class="n">np</span><span class="o">.</span><span class="n">pi</span><span class="o">*</span><span class="n">taus</span><span class="p">)</span>

<span class="c1"># Gráficas de correlación para cada realización:</span>
<span class="n">plt</span><span class="o">.</span><span class="n">plot</span><span class="p">(</span><span class="n">taus</span><span class="p">,</span> <span class="n">Rxx</span><span class="p">,</span> <span class="s1">&#39;-.&#39;</span><span class="p">,</span> <span class="n">lw</span><span class="o">=</span><span class="mi">4</span><span class="p">,</span> <span class="n">label</span><span class="o">=</span><span class="s1">&#39;Correlación teórica&#39;</span><span class="p">)</span>
<span class="n">plt</span><span class="o">.</span><span class="n">title</span><span class="p">(</span><span class="s1">&#39;Funciones de autocorrelación en realizaciones del proceso&#39;</span><span class="p">)</span>
<span class="n">plt</span><span class="o">.</span><span class="n">xlabel</span><span class="p">(</span><span class="sa">r</span><span class="s1">&#39;$\tau$&#39;</span><span class="p">)</span>
<span class="n">plt</span><span class="o">.</span><span class="n">ylabel</span><span class="p">(</span><span class="sa">r</span><span class="s1">&#39;$R_</span><span class="si">{WW}</span><span class="s1">(\tau)$&#39;</span><span class="p">)</span>
<span class="n">plt</span><span class="o">.</span><span class="n">legend</span><span class="p">()</span>
<span class="n">plt</span><span class="o">.</span><span class="n">show</span><span class="p">()</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt"></div>




<div class="output_png output_subarea ">
<img src="data:image/png;base64,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Nx0bNmzgvz7/VV59fh0toRYeefJx1j73N9Y88xoYNvfd58zP73znO2zatInt27fz0ksv9S/kZlwtW1YzAkVRKC+r5vrrruG5555i48aNjBs3jptvvjntMzZu3owVi/DpT32SO26/nR07tnP/Q39GVwZ/j7fccguLFi1i+/btfPe73+X6668HQFqCPQf28NzfXmDDxo18+6c/JBYV7Nq2jQcffJDXXnuNrVu3oqoq9913H1u3bqWhoYGdO3eyY8cObrjhhmHPq3QoMBEXOPT0BgytiClLRvZfm3LCeCzVy8Gn1mel7ehuwXskiGf2WFTVcYo787QrsYRk+7oXc9bdcHAPQbWUJbMmAjCyspSwp4Ku5tz2jdBLOwCDonNO77/mHWsTi47G7swuRb31hxcxtGLmnnFc/7UpJ08CoVD3161Zabe9/QbF9VFKl83E5y0C4JorP4+pSg7u2JyVtjcYoefILsL+ESyb5fivX3vuiUT8tYQ6sh9hnSyFFF18gdPfpSdQNr2JaHBiTpvQq3e+gkByyqdOA6BqzkROOlGnRx/Bjt+vyUp77z234A8LTv7IDXh0LyVF5Zxy4434QtDX507X//dCqawALKyeWL+aJRwOs3DhQpYsWcKECRP42Mc+hrQl48aO56TjF1JUW87GjRtZecZKRlWVY1g611xzDS+//DIAHo+H8847D4B58+Zx+umng2UyY/YM6usbAHjhhTU8/MQTnH32hSxbtpSOjg727dvHyy+/zDXXXIOqqowZM4YzzjiDSMwAQFM1hBBs3LiRU049ldrqKgLhGNddd11/3Qm8/fbbTJo0ianjxyOExr9efXV/2d9efZkf3vETFi5ewooVK4hEIhw5ciRlbJYtW8aYcZPRhMWaNWvYvHkzp557BmecfzJrXl7LwYMHAXjooYdYvHgxixYt4q233mLXLmfTJi0bBBT7S532azrSq0LY4HOf+xxnnHEGF198cdpnvLllGwcOHGD06NEsXboUgJqaWjyaQjga62/jq6++yoc//GEAzjjjDDo6OuhqaQEULjj3bLxeLzU1NYwYMYKW9lb+9uyzbN68maVLl7Jw4UJeeOEFDh48yOTJkzl48CCf/exnefbZZykrKxvmjEqPY8bF94OAfa8dRrFqmHbZKf3XJl+0HPVvaziwvpOZ12Smfeb5P6DagiUrBvJHVpbVEBnt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
"
>
</div>

</div>

<div class="output_area">

    <div class="prompt"></div>




<div class="output_png output_subarea ">
<img src="data:image/png;base64,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
"
>
</div>

</div>

</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h3 id="4.3.---Densidad-espectral-de-potencia">4.3. - Densidad espectral de potencia<a class="anchor-link" href="#4.3.---Densidad-espectral-de-potencia">&#182;</a></h3><ul>
<li>(20%) Determine y grafique la densidad espectral de potencia para la señal modulada <code>senal_Tx</code>.</li>
</ul>
\begin{equation}
\displaystyle
\mathcal{S}_{XX}(\omega) = \lim_{T \rightarrow \infty}\frac{E[\vert X_{T}(\omega) \vert^2]}{2T}
\end{equation}
</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[30]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="kn">from</span> <span class="nn">scipy</span> <span class="k">import</span> <span class="n">fft</span>

<span class="c1">#Transformada de Fourier</span>
<span class="n">senal_f</span> <span class="o">=</span> <span class="n">fft</span><span class="p">(</span><span class="n">senal_Tx</span><span class="p">)</span>

<span class="c1">#Muestras de la señal</span>
<span class="n">Nm</span> <span class="o">=</span> <span class="nb">len</span><span class="p">(</span><span class="n">senal_Tx</span><span class="p">)</span>

<span class="c1">#Número de símbolos</span>
<span class="n">Ns</span> <span class="o">=</span> <span class="n">Nm</span><span class="o">//</span><span class="n">mpp</span>

<span class="c1">#Tiempo del símbolo = periódo de la onda portadora</span>
<span class="n">Tc</span> <span class="o">=</span> <span class="mi">1</span> <span class="o">/</span> <span class="n">fc</span>

<span class="c1">#Tiempo entre muestras (periódo de muestreo)</span>
<span class="n">Tm</span> <span class="o">=</span> <span class="n">Tc</span> <span class="o">/</span> <span class="n">mpp</span>

<span class="c1">#Tiempo de la simulación </span>
<span class="n">T</span> <span class="o">=</span> <span class="n">Ns</span> <span class="o">*</span> <span class="n">Tc</span>

<span class="c1">#Espacio de frecuencias</span>
<span class="n">f</span> <span class="o">=</span> <span class="n">np</span><span class="o">.</span><span class="n">linspace</span><span class="p">(</span><span class="mf">0.0</span><span class="p">,</span> <span class="mf">1.0</span><span class="o">/</span><span class="p">(</span><span class="mf">2.0</span><span class="o">*</span><span class="n">Tm</span><span class="p">),</span> <span class="n">Nm</span><span class="o">//</span><span class="mi">2</span><span class="p">)</span>


<span class="c1">#Gráfica</span>
<span class="n">plt</span><span class="o">.</span><span class="n">plot</span><span class="p">(</span><span class="n">f</span><span class="p">,</span> <span class="mf">2.0</span><span class="o">/</span><span class="n">Nm</span> <span class="o">*</span> <span class="n">np</span><span class="o">.</span><span class="n">power</span><span class="p">(</span><span class="n">np</span><span class="o">.</span><span class="n">abs</span><span class="p">(</span><span class="n">senal_f</span><span class="p">[</span><span class="mi">0</span><span class="p">:</span><span class="n">Nm</span><span class="o">//</span><span class="mi">2</span><span class="p">]),</span> <span class="mi">2</span><span class="p">),</span> <span class="n">color</span> <span class="o">=</span> <span class="s1">&#39;red&#39;</span><span class="p">)</span>
<span class="n">plt</span><span class="o">.</span><span class="n">xlim</span><span class="p">(</span><span class="mi">0</span><span class="p">,</span> <span class="mi">20000</span><span class="p">)</span>
<span class="n">plt</span><span class="o">.</span><span class="n">title</span><span class="p">(</span><span class="s1">&#39;Densidad espectral&#39;</span><span class="p">)</span> 
<span class="n">plt</span><span class="o">.</span><span class="n">grid</span><span class="p">()</span>
<span class="n">plt</span><span class="o">.</span><span class="n">xlabel</span><span class="p">(</span><span class="s1">&#39;Frecuencia en Hz&#39;</span><span class="p">)</span>
<span class="n">plt</span><span class="o">.</span><span class="n">ylabel</span><span class="p">(</span><span class="s1">&#39;Densidad espectral de potencia&#39;</span><span class="p">)</span>
<span class="n">plt</span><span class="o">.</span><span class="n">show</span><span class="p">()</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt"></div>




<div class="output_png output_subarea ">
<img src="data:image/png;base64,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
"
>
</div>

</div>

</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<hr>
<h3 id="Universidad-de-Costa-Rica">Universidad de Costa Rica<a class="anchor-link" href="#Universidad-de-Costa-Rica">&#182;</a></h3><h4 id="Facultad-de-Ingenier&#237;a">Facultad de Ingenier&#237;a<a class="anchor-link" href="#Facultad-de-Ingenier&#237;a">&#182;</a></h4><h5 id="Escuela-de-Ingenier&#237;a-El&#233;ctrica">Escuela de Ingenier&#237;a El&#233;ctrica<a class="anchor-link" href="#Escuela-de-Ingenier&#237;a-El&#233;ctrica">&#182;</a></h5><hr>

</div>
</div>
</div>
    </div>
  </div>
</body>

 


</html>
