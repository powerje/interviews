__author__ = 'jep'

import unittest
from python.water_histogram import hydrohisto


class TestHistogram(unittest.TestCase):

  def test_flat_histogram(self):
    histogram = [0, 0, 0, 0]
    self.assertEqual(0, hydrohisto.calculate_volume_for_histogram(histogram))

  def test_flat_histogram_at_height(self):
    histogram = [1, 1, 1, 1]
    self.assertEqual(0, hydrohisto.calculate_volume_for_histogram(histogram))

  def test_flat_histogram_with_negatives(self):
      histogram = [-1, -1, -1, -1]
      self.assertEqual(4, hydrohisto.calculate_volume_for_histogram(histogram))

  def test_empty_histogram(self):
    histogram = []
    self.assertEqual(0, hydrohisto.calculate_volume_for_histogram(histogram))

  # Known histogram with volume of 10
  def test_closed_histogram(self):
    histogram = [1, 2, 1, 4, 2, 2, 3, 5, 1, 8]
    self.assertEqual(10, hydrohisto.calculate_volume_for_histogram(histogram))

  def test_open_histogram(self):
    histogram = [0, 2, 1, 4, 2, 2, 3, 5, 1, 0]
    self.assertEqual(6, hydrohisto.calculate_volume_for_histogram(histogram))

  def test_open_histogram2(self):
      histogram = [0, 2, 1, 0, 4, 2, 2, 3, 5, 1, 0]
      self.assertEqual(8, hydrohisto.calculate_volume_for_histogram(histogram))

  def test_tall_middle_histogram(self):
      histogram = [0, 2, 1, 4, 2, 10, 3, 5, 1, 0]
      self.assertEqual(5, hydrohisto.calculate_volume_for_histogram(histogram))

  def test_tall_middle_histogram2(self):
      histogram = [0, 10, 3, 5, 0]
      self.assertEqual(2, hydrohisto.calculate_volume_for_histogram(histogram))

  def test_tiny_histogram(self):
    histogram = [1, 4, 2]
    self.assertEqual(0, hydrohisto.calculate_volume_for_histogram(histogram))

  def test_tiny_histogram2(self):
      histogram = [0, 1, 0]
      self.assertEqual(0, hydrohisto.calculate_volume_for_histogram(histogram))

  def test_tiny_histogram3(self):
      histogram = [0, 1, 0, 1, 0, 1]
      self.assertEqual(2, hydrohisto.calculate_volume_for_histogram(histogram))

  def test_tiny_histogram_with_negatives(self):
    histogram = [0, 1, -2, 1, 0, 1]
    self.assertEqual(4, hydrohisto.calculate_volume_for_histogram(histogram))

