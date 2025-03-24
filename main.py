from utils.helper_functions import read_vcf, plot_genetic_markers

# Specify the path to your VCF file
vcf_file_path = 'genome_files/55001703461679.vcf'

# Define the maximum number of records to read (if chunking is enabled)
max_records = 1000

# Toggle use_max_records to control whether to read the entire file or a chunk
use_max_records = True  # Set this to False to read the entire file

# Read the VCF file with the specified chunking settings
variants = read_vcf(vcf_file_path, max_records, use_max_records)

# Plot the genetic markers from the VCF data
plot_genetic_markers(variants)