# QuantGaussBinomial

## Description
QuantGaussBinomial is a Python package designed for quantitative developers and data analysts. It provides easy-to-use classes for working with Gaussian and Binomial distributions, allowing for efficient calculations and visualizations. This package is particularly useful in fields like finance, economics, and scientific research where these distributions are commonly applied.

## Features
- **Gaussian Distribution**: Class for calculating and visualizing Gaussian distributions. Features include calculation of mean, standard deviation, and probability density functions (PDF), as well as generating histograms and PDF plots.
- **Binomial Distribution**: Class for working with Binomial distributions, including functionalities for calculating mean, standard deviation, PDF, and generating histograms and PDF plots.


## Usage
### Gaussian Distribution
```python
from QuantGaussBinomial import Gaussian

# Create a Gaussian distribution
gaussian = Gaussian(mu=0, sigma=1)
gaussian.read_data_file('data_file.txt')
gaussian.calculate_mean()
gaussian.calculate_stdev()

# Plotting
gaussian.plot_histogram()
gaussian.plot_histogram_pdf()

from QuantGaussBinomial import Binomial

# Create a Binomial distribution
binomial = Binomial(p=0.5, size=20)
binomial.read_data_file('data_file.txt')
binomial.calculate_mean()
binomial.calculate_stdev()

# Plotting
binomial.plot_bar()
binomial.plot_histogram_pdf()

#Adding Distributions
gaussian_one = Gaussian(25, 3)
        gaussian_two = Gaussian(30, 4)
        gaussian_sum = gaussian_one + gaussian_two
```

## Dependencies
Python 3.x <br>
Matplotlib

## Contributing

Contributions to QuantGaussBinomial are welcome! Please read our contributing guidelines for more details.

## License
This project is licensed under the MIT License - see the LICENSE.md file for details.

## Authors
Richie Sater - Initial work <br>
Andrew Pastor and Udacity Team - Initial work and project set up