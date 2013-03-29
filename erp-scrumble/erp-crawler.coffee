cheerio = require "cheerio"
request = require "request"
mongo = require "baio-mongo"
async = require "async"

mongo.setConfig uri : "mongodb://baio:123@ds033487.mongolab.com:33487/erp"

req = (i, done) ->
  console.log i
  request "http://www.erpr.ru/ob/all_ob.aspx?page=#{i}", (err, response, body) ->
    if !err
      $ = cheerio.load body
      items = ($(j).text() for j in $("#ctl00_ContentPlaceHolder1_gvAllAnnouncements strong"))
      if items[0] == "В этом разделе организации отсутствуют"
        done "complete"
      else

        items = items.map (m) -> _id : m
        mongo.insert "catalog", items, false, (err) ->
            done if err and  err.code != 11000 then err else null
    else
      done null

count = 1
async.whilst((-> true), ((ck) -> req count++, ck), ((err) -> console.log err))
