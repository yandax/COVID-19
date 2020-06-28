import sys

countries = ['US', 'Italy', 'Brazil', 'Russia', 'Mexico', 'Japan', 'Canada', 'Colombia', 'Peru', 'Spain', 'India', 'United Kingdom', 'China', 'Chile', 'Netherlands', 'Australia', 'Pakistan', 'Germany', 'Sweden', 'Ukraine', 'Denmark', 'France', 'Afghanistan', 'Albania', 'Algeria', 'Andorra', 'Angola', 'Antigua and Barbuda', 'Argentina', 'Armenia', 'Austria', 'Azerbaijan', 'Bahamas', 'Bahrain', 'Bangladesh', 'Barbados', 'Belarus', 'Belgium', 'Belize', 'Benin', 'Bhutan', 'Bolivia', 'Bosnia and Herzegovina', 'Botswana', 'Brunei', 'Bulgaria', 'Burkina Faso', 'Burma', 'Burundi', 'Cabo Verde', 'Cambodia', 'Cameroon', 'Central African Republic', 'Chad', 'Comoros', 'Congo (Brazzaville)', 'Congo (Kinshasa)', 'Costa Rica', "Cote d'Ivoire", 'Croatia', 'Cuba', 'Cyprus', 'Czechia', 'Diamond Princess', 'Djibouti', 'Dominica', 'Dominican Republic', 'Ecuador', 'Egypt', 'El Salvador', 'Equatorial Guinea', 'Eritrea', 'Estonia', 'Eswatini', 'Ethiopia', 'Fiji', 'Finland', 'Gabon', 'Gambia', 'Georgia', 'Ghana', 'Greece', 'Grenada', 'Guatemala', 'Guinea', 'Guinea-Bissau', 'Guyana', 'Haiti', 'Holy See', 'Honduras', 'Hungary', 'Iceland', 'Indonesia', 'Iran', 'Iraq', 'Ireland', 'Israel', 'Jamaica', 'Jordan', 'Kazakhstan', 'Kenya', 'Korea, South', 'Kosovo', 'Kuwait', 'Kyrgyzstan', 'Laos', 'Latvia', 'Lebanon', 'Lesotho', 'Liberia', 'Libya', 'Liechtenstein', 'Lithuania', 'Luxembourg', 'MS Zaandam', 'Madagascar', 'Malawi', 'Malaysia', 'Maldives', 'Mali', 'Malta', 'Mauritania', 'Mauritius', 'Moldova', 'Monaco', 'Mongolia', 'Montenegro', 'Morocco', 'Mozambique', 'Namibia', 'Nepal', 'New Zealand', 'Nicaragua', 'Niger', 'Nigeria', 'North Macedonia', 'Norway', 'Oman', 'Panama', 'Papua New Guinea', 'Paraguay', 'Philippines', 'Poland', 'Portugal', 'Qatar', 'Romania', 'Rwanda', 'Saint Kitts and Nevis', 'Saint Lucia', 'Saint Vincent and the Grenadines', 'San Marino', 'Sao Tome and Principe', 'Saudi Arabia', 'Senegal', 'Serbia', 'Seychelles', 'Sierra Leone', 'Singapore', 'Slovakia', 'Slovenia', 'Somalia', 'South Africa', 'South Sudan', 'Sri Lanka', 'Sudan', 'Suriname', 'Switzerland', 'Syria', 'Taiwan', 'Tajikistan', 'Tanzania', 'Thailand', 'Timor-Leste', 'Togo', 'Trinidad and Tobago', 'Tunisia', 'Turkey', 'Uganda', 'United Arab Emirates', 'Uruguay', 'Uzbekistan', 'Venezuela', 'Vietnam', 'West Bank and Gaza', 'Western Sahara', 'Yemen', 'Zambia', 'Zimbabwe']

for country in countries:
    fileout = open(country + ".html", "w")
    fileout.write('''<html>

    <head>

        <title>COVID-19 Dashboard</title>

        <script src="allcountrydata.js"></script> <!--change daily-->

        <script>
            currentdate = "06-27-2020"; // change daily
            countryname = "''' + country + '''";
        </script>

        <!-- Compiled and minified CSS -->
        <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/materialize/1.0.0/css/materialize.min.css">

        <!-- Compiled and minified JavaScript -->
        <script src="https://cdnjs.cloudflare.com/ajax/libs/materialize/1.0.0/js/materialize.min.js"></script>

        <link href="https://fonts.googleapis.com/icon?family=Material+Icons" rel="stylesheet">

        <link rel="stylesheet" href="https://unpkg.com/leaflet@1.6.0/dist/leaflet.css"
              integrity="sha512-xwE/Az9zrjBIphAcBb3F6JVqxf46+CDLwfLMHloNu6KEQCAWi6HcDUbeOfBIptF7tcCzusKFjFw2yuvEpDL9wQ=="
              crossorigin=""/>
        <script src="https://unpkg.com/leaflet@1.6.0/dist/leaflet.js"
                integrity="sha512-gZwIG9x3wUXg2hdXF6+rVkLF/0Vi9U8D2Ntg4Ga5I5BZpVkVxlJWbSQtXPSiUTtC0TjtGOmxa1AJPuV0CPthew=="
                crossorigin=""></script>

        <script src="https://cdn.jsdelivr.net/npm/chart.js@2.9.3/dist/Chart.min.js"></script>

        <script src="https://cdnjs.cloudflare.com/ajax/libs/Chart.js/2.9.3/Chart.js" integrity="sha256-nZaxPHA2uAaquixjSDX19TmIlbRNCOrf5HO1oHl5p70=" crossorigin="anonymous"></script>

        <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/Chart.js/2.9.3/Chart.css" integrity="sha256-IvM9nJf/b5l2RoebiFno92E5ONttVyaEEsdemDC6iQA=" crossorigin="anonymous" />

        <script src="https://cdnjs.cloudflare.com/ajax/libs/jquery/3.5.1/jquery.min.js" integrity="sha256-9/aliU8dGd2tb6OSsuzixeV4y/faTqgFtohetphbbj0=" crossorigin="anonymous"></script>

        <script src="https://cdnjs.cloudflare.com/ajax/libs/datatables/1.10.20/js/jquery.dataTables.js" integrity="sha256-Q0cguHZIfvl0zzk68PF1dGCY3pW2y6xvHx4GHLQ/lg4=" crossorigin="anonymous"></script>

        <style>
            nav ul li:hover {
                background-color: orange;
            }
            .nav-wrapper {
                z-index: 1000000;
                padding-left: 20px;
            }
            .nav-wrapper :hover {
                color: black;
            }
            footer ul li a:hover {
                color: black;
            }
            table.highlight>tbody>tr:hover {
                background-color: #4db6ac66;
            }
            tbody {
                display: block;
                height: 559px;
                position: static;
                overflow: auto;
            }
            thead, tbody tr {
                display: table;
                width: 100%;
                table-layout: fixed;
            }
            thead {
                width: calc( 100% - 1em )
            }
            table {
                width:100%;
            }
            .globalcases {
                color: #f8f540;
                display: inline;
                font-weight: bold;
            }
            .globaldeaths {
                color: #f65164;
                display: inline;
                font-weight: bold;
            }
            .globalactive {
                color: #ff9d00;
                display: inline;
                font-weight: bold;
            }
            .globalrecovered {
                color: #65dd9b;
                display: inline;
                font-weight: bold;
            }
            .leaflet-container {
                z-index: 10;
            }
            .leaflet-popup-content-wrapper {
                background-color: #546e7a;
            }
            .leaflet-popup-tip {
                background-color: #546e7a;
            }
            .flag {
                width: 70px;
                position: absolute;
                overflow: hidden;
                left: 15px;
                border: 1px solid #021a40;
                display: inline-block;
                top: 15px;
            }

            div.material-table {
                padding: 0;
            }

            div.material-table .hiddensearch {
                padding: 0 14px 0 24px;
                border-bottom: solid 1px #DDDDDD;
                display: none;
            }

            div.material-table .hiddensearch input {
                margin: 0;
                border: transparent 0 !important;
                height: 48px;
                color: rgba(0, 0, 0, .84);
            }

            div.material-table .hiddensearch input:active {
                border: transparent 0 !important;
            }

            div.material-table table {
                table-layout: fixed;
            }

            div.material-table .table-header {
                height: 64px;
                padding-left: 24px;
                padding-right: 14px;
                -webkit-align-items: center;
                -ms-flex-align: center;
                align-items: center;
                display: flex;
                -webkit-display: flex;
                border-bottom: solid 1px #DDDDDD;
            }

            div.material-table .table-header .actions {
                display: -webkit-flex;
                margin-left: auto;
            }

            div.material-table .table-header .btn-flat {
                min-width: 36px;
                padding: 0 8px;
            }

            div.material-table .table-header input {
                margin: 0;
                height: auto;
            }

            div.material-table .table-header i {
                color: rgba(0, 0, 0, 0.54);
                font-size: 24px;
            }

            div.material-table .table-footer {
                height: 56px;
                padding-left: 24px;
                padding-right: 14px;
                display: -webkit-flex;
                display: flex;
                -webkit-flex-direction: row;
                flex-direction: row;
                -webkit-justify-content: flex-end;
                justify-content: flex-end;
                -webkit-align-items: center;
                align-items: center;
                font-size: 12px !important;
                color: rgba(0, 0, 0, 0.54);
            }

            div.material-table .table-footer .dataTables_length {
                display: -webkit-flex;
                display: flex;
            }

            div.material-table .table-footer label {
                font-size: 12px;
                color: rgba(0, 0, 0, 0.54);
                display: -webkit-flex;
                display: flex;
                -webkit-flex-direction: row
                    /* works with row or column */

                    flex-direction: row;
                -webkit-align-items: center;
                align-items: center;
                -webkit-justify-content: center;
                justify-content: center;
            }

            div.material-table .table-footer .select-wrapper {
                display: -webkit-flex;
                display: flex;
                -webkit-flex-direction: row
                    /* works with row or column */

                    flex-direction: row;
                -webkit-align-items: center;
                align-items: center;
                -webkit-justify-content: center;
                justify-content: center;
            }

            div.material-table .table-footer .dataTables_info,
            div.material-table .table-footer .dataTables_length {
                margin-right: 32px;
            }

            div.material-table .table-footer .material-pagination {
                display: flex;
                -webkit-display: flex;
                margin: 0;
            }

            div.material-table .table-footer .material-pagination li:first-child {
                margin-right: 24px;
            }

            div.material-table .table-footer .material-pagination li a {
                color: rgba(0, 0, 0, 0.54);
            }

            div.material-table .table-footer .select-wrapper input.select-dropdown {
                margin: 0;
                border-bottom: none;
                height: auto;
                line-height: normal;
                font-size: 12px;
                width: 40px;
                text-align: right;
            }

            div.material-table .table-footer select {
                background-color: transparent;
                width: auto;
                padding: 0;
                border: 0;
                border-radius: 0;
                height: auto;
                margin-left: 20px;
            }

            div.material-table .table-title {
                font-size: 20px;
                color: #000;
            }

            div.material-table table tr td {
                padding: 0 0 0 56px;
                height: 48px;
                font-size: 14px;
                color: rgba(0, 0, 0, 0.87);
                border-bottom: solid 1px #DDDDDD;
                white-space: nowrap;
                overflow: hidden;
                text-overflow: ellipsis;
            }

            div.material-table table tr td a {
                color: inherit;
            }

            div.material-table table tr td a i {
                font-size: 18px;
                color: rgba(0, 0, 0, 0.54);
            }

            div.material-table table th {
                font-weight: 500;
                color: #757575;
                cursor: pointer;
                white-space: nowrap;
                padding: 0;
                height: 56px;
                padding-left: 56px;
                vertical-align: middle;
                outline: none !important;
            }

            div.material-table table th.sorting_asc,
            div.material-table table th.sorting_desc {
                color: rgba(0, 0, 0, 0.87);
            }

            div.material-table table th.sorting:after,
            div.material-table table th.sorting_asc:after,
            div.material-table table th.sorting_desc:after {
                font-family: 'Material Icons';
                font-weight: normal;
                font-style: normal;
                font-size: 16px;
                line-height: 1;
                letter-spacing: normal;
                text-transform: none;
                display: inline-block;
                word-wrap: normal;
                -webkit-font-feature-settings: 'liga';
                -webkit-font-smoothing: antialiased;
                content: "arrow_back";
                -webkit-transform: rotate(90deg);
                display: none;
                vertical-align: middle;
            }

            div.material-table table th.sorting:hover:after,
            div.material-table table th.sorting_asc:after,
            div.material-table table th.sorting_desc:after {
                display: inline-block;
            }

            div.material-table table th.sorting_desc:after {
                content: "arrow_forward";
            }

            div.material-table table tbody tr:hover {
                background-color: #EEE;
            }

            div.material-table table th:first-child,
            div.material-table table td:first-child {
                padding: 0 0 0 24px;
            }

            div.material-table table th:last-child,
            div.material-table table td:last-child {
                padding: 0 14px 0 0;
            }

            div.dt-button-info {
                position: fixed;
                top: 50%;
                left: 50%;
                width: 400px;
                margin-top: -100px;
                margin-left: -200px;
                text-align: center;
                z-index: 21;
                color: rgba(0, 0, 0, 0.6);
            }

        </style>

    </head>

    <body>
        <div class="navbar-fixed">
            <nav>
                <div class="nav-wrapper teal">
                    <a href=../index.html class="brand-logo"><i class="large material-icons">home</i></a>
                    <ul id="nav-mobile" class="right hide-on-med-and-down">
                        <li><a href=../countries.html>Countries</a></li>
                        <li><a href=../timeline.html>Timeline</a></li>
                        <li><a href="https://github.com/CSSEGISandData/COVID-19/tree/master/csse_covid_19_data/csse_covid_19_daily_reports">JHU Data</a></li>
                        <li><a href="https://materializecss.com/">Materialize</a></li>
                        <li><a href="https://leafletjs.com/">Leaflet</a></li>
                        <li class="github"><a href="https://github.com/yandax/COVID-19">GitHub&nbsp;&nbsp;<img src="../GitHub-Mark-120px-plus.png" width="20" style="vertical-align: middle;"></a></li>
                    </ul>
                </div>
            </nav>
        </div>

        <h1 class="center" id="pagetitle">COVID-19 Dashboard - </h1>
        <script>
            document.getElementById('pagetitle').innerHTML += countryname;
        </script>
        <br>

        <div class="row">
            <div class="col s12 m6 l6">
                <canvas id="casechart"></canvas>
            </div>
            <script>
                var ctx = document.getElementById('casechart');
                dates = [];
                cases = [];
                for(var i in data) {
                    dates.unshift(i);
                    conf = 0;
                    for(j=0; j<data[i].length; j++) {
                        if(data[i][j]["name"] == countryname) {
                            conf = data[i][j]["conf"];
                        }
                    }
                    cases.unshift(conf);
                }
                var myChart = new Chart(ctx, {
                    type: 'line',
                    data: {
                        labels: dates,
                        datasets: [{
                            label: 'Total Cases',
                            data: cases,
                            fill: false,
                            borderColor: "#ff9d00",
                            lineTension: 0.1
                        }]
                    },
                    options: {
                        legend: {
                            display: false
                        },
                        title: {
                            display: true,
                            text: 'Total Cases'
                        },
                        "scales":{
                            "xAxes":[{"ticks":{"beginAtZero":true}}]
                        },
                        tooltips: {
                            callbacks: {
                                label: function(tooltipItem, data) {
                                    return "Total Cases: " + data["datasets"][0]["data"][tooltipItem["index"]].toString().replace(/\B(?=(\d{3})+(?!\d))/g, ",");
                                }
                            }
                        }
                    }
                });
            </script>
            <div class="col s12 m6 l6">
                <canvas id="deathchart"></canvas>
            </div>
            <script>
                var ctx = document.getElementById('deathchart');
                dates = [];
                deaths = [];
                for(var i in data) {
                    dates.unshift(i);
                    dead = 0;
                    for(j=0; j<data[i].length; j++) {
                        if(data[i][j]["name"] == countryname) {
                            dead = data[i][j]["dead"];
                        }
                    }
                    deaths.unshift(dead);
                }
                var myChart = new Chart(ctx, {
                    type: 'line',
                    data: {
                        labels: dates,
                        datasets: [{
                            label: 'Total Dead',
                            data: deaths,
                            fill: false,
                            borderColor: "#f65164",
                            lineTension: 0.1
                        }]
                    },
                    options: {
                        legend: {
                            display: false
                        },
                        title: {
                            display: true,
                            text: 'Total Dead'
                        },
                        "scales":{
                            "xAxes":[{"ticks":{"beginAtZero":true}}]
                        },
                        tooltips: {
                            callbacks: {
                                label: function(tooltipItem, data) {
                                    return "Total Deaths: " + data["datasets"][0]["data"][tooltipItem["index"]].toString().replace(/\B(?=(\d{3})+(?!\d))/g, ",");
                                }
                            }
                        }
                    }
                });
            </script>
        </div>

        <div class="row">
            <div class="col s12 m6 l6">
                <canvas id="dailycasechart"></canvas>
            </div>
            <script>
                var ctx = document.getElementById('dailycasechart');
                dates = [];
                dailycases = [];
                var keys = Object.keys(data);
                for(i=0; i<keys.length-1; i++) {
                    dates.unshift(keys[i]);
                    final = 0;
                    for(j=0; j<data[keys[i]].length; j++) {
                        if(data[keys[i]][j]["name"] == countryname) {
                            final = data[keys[i]][j]["conf"];
                        }
                    }
                    initial = 0;
                    for(j=0; j<data[keys[i+1]].length; j++) {
                        if(data[keys[i+1]][j]["name"] == countryname) {
                            initial = data[keys[i+1]][j]["conf"];
                        }
                    }
                    dailycases.unshift(final-initial);
                }
                var myChart = new Chart(ctx, {
                    type: 'line',
                    data: {
                        labels: dates,
                        datasets: [{
                            label: 'Daily Cases',
                            data: dailycases,
                            fill: false,
                            borderColor: "#ff9d00",
                            lineTension: 0.1
                        }]
                    },
                    options: {
                        legend: {
                            display: false
                        },
                        title: {
                            display: true,
                            text: 'Daily Cases'
                        },
                        "scales":{
                            "xAxes":[{"ticks":{"beginAtZero":true}}]
                        },
                        tooltips: {
                            callbacks: {
                                label: function(tooltipItem, data) {
                                    return "Daily Cases: " + data["datasets"][0]["data"][tooltipItem["index"]].toString().replace(/\B(?=(\d{3})+(?!\d))/g, ",");
                                }
                            }
                        }
                    }
                });
            </script>
            <div class="col s12 m6 l6">
                <canvas id="dailydeathchart"></canvas>
            </div>
            <script>
                var ctx = document.getElementById('dailydeathchart');
                dates = [];
                dailydeaths = [];
                var keys = Object.keys(data);
                for(i=0; i<keys.length-1; i++) {
                    dates.unshift(keys[i]);
                    final = 0;
                    for(j=0; j<data[keys[i]].length; j++) {
                        if(data[keys[i]][j]["name"] == countryname) {
                            final = data[keys[i]][j]["dead"];
                        }
                    }
                    initial = 0;
                    for(j=0; j<data[keys[i+1]].length; j++) {
                        if(data[keys[i+1]][j]["name"] == countryname) {
                            initial = data[keys[i+1]][j]["dead"];
                        }
                    }
                    dailydeaths.unshift(final-initial);
                }
                var myChart = new Chart(ctx, {
                    type: 'line',
                    data: {
                        labels: dates,
                        datasets: [{
                            label: 'Daily Deaths',
                            data: dailydeaths,
                            fill: false,
                            borderColor: "#f65164",
                            lineTension: 0.1
                        }]
                    },
                    options: {
                        legend: {
                            display: false
                        },
                        title: {
                            display: true,
                            text: 'Daily Deaths'
                        },
                        "scales":{
                            "xAxes":[{"ticks":{"beginAtZero":true}}]
                        },
                        tooltips: {
                            callbacks: {
                                label: function(tooltipItem, data) {
                                    return "Daily Deaths: " + data["datasets"][0]["data"][tooltipItem["index"]].toString().replace(/\B(?=(\d{3})+(?!\d))/g, ",");
                                }
                            }
                        }
                    }
                });
            </script>
        </div>

        <!--
<div class="row">
<div class="col s12 m6 l6 center">
<div>
<canvas id="chartjs-2"></canvas>
</div>
</div>
</div>
-->

        <div class="row">
            <div class="col l3">
                <div class="card blue-grey darken-1">
                    <div class="card-content white-text">
                        <span class="card-title center"><h4><b>Total Confirmed</b></h4></span>
                        <p class="globalcases" style="text-align: center;" id="globalcases"></p>
                        <br>
                        <span class="card-title center"><h4><b>Total Deceased</b></h4></span>
                        <p class="globaldeaths" style="text-align: center;" id="globaldeaths"></p>
                        <br>
                        <span class="card-title center"><h4><b>Total Active</b></h4></span>
                        <p class="globalactive" style="text-align: center;" id="globalactive"></p>
                        <br>
                        <span class="card-title center"><h4><b>Total Recovered</b></h4></span>
                        <p class="globalrecovered" style="text-align: center;" id="globalrecovered"></p>
                    </div>
                </div>
            </div>

            <div class="col s12 m12 l9" id="countrytable">
                <div class="card material-table">
                    <div class="table-header">
                        <span class="table-title" id="tabletitle"></span>
                        <script>
                            document.getElementById("tabletitle").innerHTML = countryname + " Database";
                        </script>
                        <div class="actions">
                            <a class="search-toggle waves-effect btn-flat nopadding"><i class="material-icons">search</i></a>
                        </div>
                    </div>
                    <table class="centered" id="datatable">
                        <thead>
                            <tr>
                                <th>Date</th>
                                <th>Confirmed Cases</th>
                                <th>Deaths</th>
                                <th>Recovered</th>
                            </tr>
                        </thead>

                        <tbody id="fulllist"></tbody>
                    </table>
                    <script>
                        (function(window, document, undefined) {

                            var factory = function($, DataTable) {

                                "use strict";

                                $('.search-toggle').click(function() {
                                    if ($('.hiddensearch').css('display') == 'none')
                                        $('.hiddensearch').slideDown();
                                    else
                                        $('.hiddensearch').slideUp();
                                });

                                /* Set the defaults for DataTables initialisation */
                                $.extend(true, DataTable.defaults, {
                                    dom: "<'hiddensearch'f'>" +
                                    "tr"+
                                    "<'table-footer'Blip'>",
                                    renderer: 'material'
                                });
                                /* Default class modification */
                                $.extend(DataTable.ext.classes, {
                                    sWrapper: "dataTables_wrapper",
                                    sFilterInput: "form-control input-sm",
                                    sLengthSelect: "form-control input-sm"
                                });

                                /* Bootstrap paging button renderer */
                                DataTable.ext.renderer.pageButton.material = function(settings, host, idx, buttons, page, pages) {
                                    var api = new DataTable.Api(settings);
                                    var classes = settings.oClasses;
                                    var lang = settings.oLanguage.oPaginate;
                                    var btnDisplay, btnClass, counter = 0;

                                    var attach = function(container, buttons) {
                                        var i, ien, node, button;
                                        var clickHandler = function(e) {
                                            e.preventDefault();
                                            if (!$(e.currentTarget).hasClass('disabled')) {
                                                api.page(e.data.action).draw(false);
                                            }
                                        };

                                        for (i = 0, ien = buttons.length; i < ien; i++) {
                                            button = buttons[i];

                                            if ($.isArray(button)) {
                                                attach(container, button);
                                            } else {
                                                btnDisplay = '';
                                                btnClass = '';

                                                switch (button) {

                                                    case 'first':
                                                        btnDisplay = lang.sFirst;
                                                        btnClass = button + (page > 0 ?
                                                                             '' : ' disabled');
                                                        break;

                                                    case 'previous':
                                                        btnDisplay = '<i class="material-icons">chevron_left</i>';
                                                        btnClass = button + (page > 0 ?
                                                                             '' : ' disabled');
                                                        break;

                                                    case 'next':
                                                        btnDisplay = '<i class="material-icons">chevron_right</i>';
                                                        btnClass = button + (page < pages - 1 ?
                                                                             '' : ' disabled');
                                                        break;

                                                    case 'last':
                                                        btnDisplay = lang.sLast;
                                                        btnClass = button + (page < pages - 1 ?
                                                                             '' : ' disabled');
                                                        break;

                                                }

                                                if (btnDisplay) {
                                                    node = $('<li>', {
                                                        'class': classes.sPageButton + ' ' + btnClass,
                                                        'id': idx === 0 && typeof button === 'string' ?
                                                        settings.sTableId + '_' + button : null
                                                    })
                                                        .append($('<a>', {
                                                        'href': '#',
                                                        'aria-controls': settings.sTableId,
                                                        'data-dt-idx': counter,
                                                        'tabindex': settings.iTabIndex
                                                    })
                                                                .html(btnDisplay)
                                                               )
                                                        .appendTo(container);

                                                    settings.oApi._fnBindAction(
                                                        node, {
                                                            action: button
                                                        }, clickHandler
                                                    );

                                                    counter++;
                                                }
                                            }
                                        }
                                    };

                                    // IE9 throws an 'unknown error' if document.activeElement is used
                                    // inside an iframe or frame.
                                    var activeEl;

                                    try {
                                        // Because this approach is destroying and recreating the paging
                                        // elements, focus is lost on the select button which is bad for
                                        // accessibility. So we want to restore focus once the draw has
                                        // completed
                                        activeEl = $(document.activeElement).data('dt-idx');
                                    } catch (e) {}

                                    attach(
                                        $(host).empty().html('<ul class="material-pagination"/>').children('ul'),
                                        buttons
                                    );

                                    if (activeEl) {
                                        $(host).find('[data-dt-idx=' + activeEl + ']').focus();
                                    }
                                };

                                if (DataTable.TableTools) {
                                    // Set the classes that TableTools uses to something suitable for Bootstrap
                                    $.extend(true, DataTable.TableTools.classes, {
                                        "container": "DTTT btn-group",
                                        "buttons": {
                                            "normal": "btn btn-default",
                                            "disabled": "disabled"
                                        },
                                        "collection": {
                                            "container": "DTTT_dropdown dropdown-menu",
                                            "buttons": {
                                                "normal": "",
                                                "disabled": "disabled"
                                            }
                                        },
                                        "select": {
                                            "row": "active"
                                        }
                                    });

                                    // Have the collection use a material compatible drop down
                                    $.extend(true, DataTable.TableTools.DEFAULTS.oTags, {
                                        "collection": {
                                            "container": "ul",
                                            "button": "li",
                                            "liner": "a"
                                        }
                                    });
                                }

                            }; // /factory

                            // Define as an AMD module if possible
                            if (typeof define === 'function' && define.amd) {
                                define(['jquery', 'datatables'], factory);
                            } else if (typeof exports === 'object') {
                                // Node/CommonJS
                                factory(require('jquery'), require('datatables'));
                            } else if (jQuery) {
                                // Otherwise simply initialise as normal, stopping multiple evaluation
                                factory(jQuery, jQuery.fn.dataTable);
                            }

                        })(window, document);


                        $(document).ready(function() {
                            var t = $('#datatable').DataTable({
                                "order": [[ 0, 'desc' ]],
                                "pageLength": 20,
                                "oLanguage": {
                                    "sSearch": "",
                                    "sSearchPlaceholder": "Search",
                                    "sInfo": "_START_ -_END_ of _TOTAL_",
                                    "sLengthMenu": '<span>Rows per page:</span><select class="browser-default">' +
                                    '<option value="20">20</option>' +
                                    '<option value="50">50</option>' +
                                    '<option value="-1">All</option>' +
                                    '</select></div>'
                                },
                                bAutoWidth: false,
                            });
                        });
                    </script>
                </div>
            </div>
        </div>

        <footer class="page-footer teal">
            <div class="container">
                <div class="row">
                    <div class="col l6 s12">
                        <h5 class="white-text">COVID-19 Dashbord</h5>
                        <p class="grey-text text-lighten-4">This website is intended to be a dashboard to track COVID-19 statistics across the world. Data is updated roughly every day.</p>
                    </div>
                    <div class="col l4 offset-l2 s12">
                        <h5 class="white-text">Links</h5>
                        <ul>
                            <li><a class="grey-text text-lighten-3" href="../index.html">All Data</a></li>
                            <li><a class="grey-text text-lighten-3" href="../countries.html">Countries</a></li>
                            <li><a class="grey-text text-lighten-3" href="../timeline.html">Timeline</a></li>
                            <li><a class="grey-text text-lighten-3" href="https://github.com/CSSEGISandData/COVID-19/tree/master/csse_covid_19_data/csse_covid_19_daily_reports">JHU Data</a></li>
                            <li><a class="grey-text text-lighten-3" href="https://github.com/yandax/COVID-19">GitHub</a></li>
                        </ul>
                    </div>
                </div>
            </div>
            <div class="footer-copyright">
                <div class="container">
                    © 2020 Copyright Daniel Yang
                </div>
            </div>
        </footer>

    </body>

    <script>

        function fulllist() {

            fulllist = document.getElementById("fulllist");

            myhtml = "";
            for(var i in data) {
                myhtml += "<tr>";
                hasdata = false;
                for(j=0; j<data[i].length; j++) {
                    if(data[i][j]["name"] == countryname) {
                        hasdata = true;
                        myhtml += "<td>" + i + "</td>";
                        myhtml += "<td>" + data[i][j]["conf"].toString().replace(/\B(?=(\d{3})+(?!\d))/g, ",") + "</td>";
                        myhtml += "<td>" + data[i][j]["dead"].toString().replace(/\B(?=(\d{3})+(?!\d))/g, ",") + "</td>";
                        myhtml += "<td>" + data[i][j]["recv"].toString().replace(/\B(?=(\d{3})+(?!\d))/g, ",") + "</td></tr>";
                        break;
                    }
                }
                if(!hasdata) {
                    myhtml += "<td>" + i + "</td>";
                    myhtml += "<td>0</td>";
                    myhtml += "<td>0</td>";
                    myhtml += "<td>0</td></tr>";
                }
            }

            fulllist.innerHTML += myhtml;

        }

        function global(){

            globalcases = document.getElementById("globalcases");

            total = 0;

            for(i=0; i<data[currentdate].length; i++){
                if(data[currentdate][i]["name"] == countryname) {
                    total += data[currentdate][i]["conf"];
                }
            }

            globalcases.innerHTML = "<h3><b>" + total.toString().replace(/\B(?=(\d{3})+(?!\d))/g, ",") + "</b></h3>";

            globaldeaths = document.getElementById("globaldeaths");

            total = 0;
            for(i=0; i<data[currentdate].length; i++){
                if(data[currentdate][i]["name"] == countryname) {
                    total += data[currentdate][i]["dead"];
                }
            }

            globaldeaths.innerHTML = "<h3><b>" + total.toString().replace(/\B(?=(\d{3})+(?!\d))/g, ",") + "</b></h3>";

            globalactive = document.getElementById("globalactive");

            total = 0;
            for(i=0; i<data[currentdate].length; i++){
                if(data[currentdate][i]["name"] == countryname) {
                    total += data[currentdate][i]["active"];
                }
            }

            globalactive.innerHTML = "<h3><b>" + total.toString().replace(/\B(?=(\d{3})+(?!\d))/g, ",") + "</b></h3>";

            globalrecovered = document.getElementById("globalrecovered");

            total = 0;
            for(i=0; i<data[currentdate].length; i++){
                if(data[currentdate][i]["name"] == countryname) {
                    total += data[currentdate][i]["recv"];
                }
            }

            globalrecovered.innerHTML = "<h3><b>" + total.toString().replace(/\B(?=(\d{3})+(?!\d))/g, ",") + "</b></h3>";

        }

        fulllist();
        global();

    </script>

</html>''')