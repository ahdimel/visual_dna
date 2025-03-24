import vcfpy
import matplotlib.pyplot as plt

def read_vcf(file_path, max_records=1000, use_max_records=True):
    """
    Read a VCF file and return a limited number of variant data.
    If use_max_records is False, it reads the entire file.
    """
    variants = []
    vcf_reader = vcfpy.Reader.from_path(file_path)
    for i, record in enumerate(vcf_reader):
        if use_max_records and i >= max_records:
            break
        variants.append(record)
    return variants

def plot_genetic_markers(variants):
    """
    Plot genetic markers from the VCF file.
    """
    positions = [variant.POS for variant in variants]
    quality_scores = [variant.QUAL for variant in variants]

    plt.figure(figsize=(10, 6))
    plt.scatter(positions, quality_scores, marker='o', color='b')
    plt.title('Genetic Marker Quality Scores')
    plt.xlabel('Genomic Position')
    plt.ylabel('Quality Score')
    plt.show()