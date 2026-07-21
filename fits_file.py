from astropy.io import fits

# Open the FITS file
hdul = fits.open("example.fits")

# Inspect the Header Data Units (HDUs)
hdul.info()

# Access the primary HDU header metadata
primary_hdu = hdul[0]
print("\nPrimary Header Metadata:")
print(primary_hdu.header)

# Close the file handler after reading
hdul.close()