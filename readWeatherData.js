var grib2json = require('grib2json')

grib2json('recentWeatherData.grib2', {
    names: true, // (default false): Return descriptive names too
    data: true, // (default false): Return data, not just headers
    category: 2, // Grib2 category number, equals to --fc 1
    parameter: 3, // Grib2 parameter number, equals to --fp 7
    surfaceType: 103, // Grib2 surface type, equals to --fs 103
    surfaceValue: 10, // Grib2 surface value, equals to --fv 10
  }, function (err, json) {
    if (err) return console.error(err)
   
    console.log(json)
  })