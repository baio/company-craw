// Generated by CoffeeScript 1.3.3
(function() {
  var async, cheerio, count, mongo, req, request;

  cheerio = require("cheerio");

  request = require("request");

  mongo = require("baio-mongo");

  async = require("async");

  mongo.setConfig({
    uri: "mongodb://baio:123@ds033487.mongolab.com:33487/erp"
  });

  req = function(i, done) {
    console.log(i);
    return request("http://www.erpr.ru/ob/all_ob.aspx?page=" + i, function(err, response, body) {
      var $, items, j;
      if (!err) {
        $ = cheerio.load(body);
        items = (function() {
          var _i, _len, _ref, _results;
          _ref = $("#ctl00_ContentPlaceHolder1_gvAllAnnouncements strong");
          _results = [];
          for (_i = 0, _len = _ref.length; _i < _len; _i++) {
            j = _ref[_i];
            _results.push($(j).text());
          }
          return _results;
        })();
        if (items[0] === "В этом разделе организации отсутствуют") {
          return done("complete");
        } else {
          items = items.map(function(m) {
            return {
              _id: m
            };
          });
          return mongo.insert("catalog", items, false, function(err) {
            return done(err && err.code !== 11000 ? err : null);
          });
        }
      } else {
        return done(null);
      }
    });
  };

  count = 1;

  async.whilst((function() {
    return true;
  }), (function(ck) {
    return req(count++, ck);
  }), (function(err) {
    return console.log(err);
  }));

}).call(this);