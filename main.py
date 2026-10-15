import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from pathlib import Path
from itertools import combinations
from scipy.stats import shapiro, pearsonr
from astropy.cosmology import FlatLambdaCDM
from astropy.coordinates import SkyCoord
from astropy import units as u


# Load datasets
folder = Path(__file__).resolve().parent

groups = pd.read_csv(
    folder / "groups.tsv",
    delimiter="\t"
)

coordinates = pd.read_csv(
    folder / "galaxies_coordinates.tsv",
    delimiter="\t"
)

# Remove missing values
groups = groups.dropna()
coordinates = coordinates.dropna()


# Initialize the cosmological model
cosmo = FlatLambdaCDM(H0=67.74, Om0=0.3089)

# Calculate angular diameter distances in kiloparsecs
groups["d_A"] = cosmo.angular_diameter_distance(
    groups["z"].to_numpy()
).to(u.kpc).value


# Calculate median angular separation for each galaxy group
results = []

for group_name, group_data in coordinates.groupby("Group"):

    galaxies = SkyCoord(
        ra=group_data["RA"].to_numpy() * u.degree,
        dec=group_data["DEC"].to_numpy() * u.degree,
        frame="fk5"
    )

    separations = []

    # Calculate angular separation for every possible galaxy pair
    for i, j in combinations(range(len(galaxies)), 2):
        angle = galaxies[i].separation(galaxies[j])
        separations.append(angle.to(u.rad).value)

    if separations:
        median_angle = np.median(separations)

        results.append({
            "Group": group_name,
            "median_angle": median_angle
        })


# Create a DataFrame with median angular separations
separation_df = pd.DataFrame(results)

# Merge galaxy group information
df = pd.merge(
    groups,
    separation_df,
    on="Group",
    how="inner"
)

# Calculate projected median separation in kiloparsecs
df["median_separation"] = df["median_angle"] * df["d_A"]

# Remove missing values
df = df.dropna()


# Visualize the relationship between separation and brightness
plt.scatter(
    df["median_separation"],
    df["mean_mu"]
)

plt.xlabel("Projected median separation (kpc)")
plt.ylabel("IGL mean surface brightness")

# Invert the magnitude axis
plt.gca().invert_yaxis()

plt.show()


# Perform Shapiro-Wilk normality tests
_, p_separation = shapiro(df["median_separation"])
_, p_mu = shapiro(df["mean_mu"])


# Calculate Pearson correlation
correlation, p_pearson = pearsonr(
    df["median_separation"],
    df["mean_mu"]
)


# Get the projected median separation for HCG 2
hcg2 = df.loc[
    df["Group"] == "HCG 2",
    "median_separation"
].iloc[0]


# Print statistical results
print(hcg2, p_separation, p_mu, p_pearson)
