__author__ = 'jep'

def calculate_volume_for_histogram(histogram):
  maxFromLeft = _maxes_at_each_index_for_array(histogram)
  maxFromRight = _maxes_at_each_index_for_array(histogram[::-1])[::-1]

  v = 0
  for i in range(len(histogram)):
    lMax = maxFromLeft[i]
    rMax = maxFromRight[i]
    minimum = min(lMax, rMax)
    v += minimum - histogram[i]

  return max(v, 0)


def _maxes_at_each_index_for_array(arr):
    ret = []
    max = 0
    for i in range(len(arr)):
      if arr[i] > max:
        max = arr[i]
      ret.append(max)

    return ret

if __name__ == '__main__':
  histogram = [1, 2, 1, 4, 2, 2, 3, 5, 1, 8]
  print('volume: {0}'.format(calculate_volume_for_histogram(histogram)))
