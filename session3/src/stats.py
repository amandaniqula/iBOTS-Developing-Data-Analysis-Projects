def calculate_mean(numbers):
    return sum(numbers) / len(numbers)

def calculate_variance(numbers):
    mean = calculate_mean(numbers)
    variance = sum([(x - mean) ** 2 for x in numbers]) / len(numbers)
    return variance

def calculate_std(numbers):
    std = calculate_variance(numbers) ** .5
    return std

def calculate_median(numbers):
    numbers.sort()
    n = len(numbers)
    mid = n // 2
    if n % 2 == 0:
        median = (numbers[mid - 1] + numbers[mid]) / 2
    else:
        median = numbers[mid]
    return median

def compute_stat(data, kind="calculate_mean"):
    return kind(data)

def plot_histogram(data, nbins):
    figure, ax = plt.subplots(ncols=1, nrows=1)
    ax.hist(data, bins=nbins);