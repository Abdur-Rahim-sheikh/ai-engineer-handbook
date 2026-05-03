## Knowledge about MLOps

### Content

1. [How to detect data drift?](#how-to-detect-data-drift)
2. [How PSI (Population Stability Index) works?](#how-psi-population-stability-index-works)

### How to detect data drift?

**Data Drift:** when the distribution of the input data changes over time we call it data drift.
Data drift can be detected using various techniques, including:

- **Statistical Tests**: Use statistical tests like the Kolmogorov-Smirnov test, Chi-Square test and PSI (Population Stability Index) to compare the distributions of the training and current data.
- **Visualization**: Plot histograms, box plots, or scatter plots to visually inspect changes in data distribution.
- **Monitoring Metrics**: Track key metrics such as mean, median, standard deviation, and quantiles over time to identify shifts in data characteristics.

### How PSI (Population Stability Index) works?

PSI is one of the most commonly used techniques to detect data drift. It measures the stability of a population by comparing the distribution of a variable in two different samples (e.g., training data vs. current data). The PSI is calculated as follows:

```
PSI = ∑((Actual% - Expected%) * ln(Actual% / Expected%))
```

Where,

- PSI < 0.1: No significant change
- 0.1 ≤ PSI < 0.25: Moderate change
- PSI ≥ 0.25: Significant change

With example:
Let's say in a coffee shop, different age of customer visit the shop.

- Expected (Last year): 20% teens, 60% adults, 20% seniors
- Actual (This year): 40% teens, 40% adults, 20% seniors

```
PSI(teens) = (0.40 - 0.20) * ln(0.40 / 0.20) = 0.20 * ln(2) ≈ 0.1386
PSI(adults) = (0.40 - 0.60) * ln(0.40 / 0.60) = -0.20 * ln(0.6667) ≈ 0.0811
PSI(seniors) = (0.20 - 0.20) * ln(0.20 / 0.20) = 0
Total PSI = 0.1386 + 0.0811 + 0 = 0.2197
```

So, it's located under moderate change.
