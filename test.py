# Databricks notebook source
files = dbutils.fs.ls('/databricks-datasets/')

display(files)
