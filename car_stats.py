#!/usr/bin/env python3

import json
import locale
import sys
import operator
from reports import generate as report
from emails import generate as email_generate
from emails import send as email_send

def load_data(filename):
  """Loads the contents of filename as a JSON file."""
  locale.setlocale(locale.LC_ALL, 'en_US.UTF8')
  with open(filename) as json_file:
    new_data = json.load(json_file)
    data = sorted(new_data, key=lambda i: i['total_sales'])
  return data


def format_car(car):
  """Given a car dictionary, returns a nicely formatted name."""
  return "{} {} ({})".format(
      car["car_make"], car["car_model"], car["car_year"])
def process_data(data):
  """Analyzes the data, looking for maximums.

  Returns a list of lines that summarize the information.
  """
  max_revenue = {"revenue": 0}
  max_sales = {"total_sales": 0}
  car_year = {}
  for item in data:
    # Calculate the revenue generated by this model (price * total_sales)
    # We need to convert the price from "$1234.56" to 1234.56
    item_price = locale.atof(item["price"].strip("$"))
    item_revenue = item["total_sales"] * item_price
    if item_revenue > max_revenue["revenue"]:
      item["revenue"] = item_revenue
      max_revenue = item
    # TODO: also handle max sales
    if item["total_sales"] > max_sales["total_sales"]:
        max_sales = item
    # TODO: also handle most popular car_year
    current_car_year = item["car"]["car_year"]
    if current_car_year in car_year.keys():
       car_year[current_car_year] += item['total_sales'] 
    else:
      car_year[current_car_year] =  item["total_sales"]
  year_more_sales=max(car_year.items(), key=operator.itemgetter(1))[0]  
  max_sales_year=car_year[year_more_sales]  
  summary = [
    "The {} generated the most revenue: ${}".format(
      format_car(max_revenue["car"]), max_revenue["revenue"]),
    "The {} had the most sales: {}".format(
      format_car(max_sales["car"]), max_sales["total_sales"]),
    "The most popular year was {} with {} sales.".format(year_more_sales,max_sales_year),
        ]

  return summary


def cars_dict_to_table(car_data):
  """Turns the data in car_data into a list of lists."""
  table_data = [["ID", "Car", "Price", "Total Sales"]]
  for item in car_data:
    table_data.append([item["id"], format_car(item["car"]), item["price"], item["Total Sales"]])
  return table_data


def main(argv):
  """Process the JSON data and generate a full report out of it."""
  data = load_data("car_sales.json")
  summary = process_data(data)
  new_summary = '<br/>'.join(summary)
  print(summary)
  # TODO: turn this into a PDF report
  report('/tmp/care.pdf', "Cars report", new_summary, cars_dict_to_table(data))
  # TODO: send the PDF report as an email attachment
  msg = email_generate("automation@example.com", "student-03-72acbed1de6a@example.com", "Sales sumary for last month", new_summary  , "/tmp/cars.pdf")
  email_send(msg)


if __name__ == "__main__":
    main(sys.argv)
