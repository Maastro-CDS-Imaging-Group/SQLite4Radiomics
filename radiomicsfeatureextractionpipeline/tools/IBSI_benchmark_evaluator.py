import pandas as pd
import argparse


def main(args):
    try:
        pipeline_df = pd.read_csv(args.pipeline_csv_file)
        benchmark_df = pd.read_csv(args.benchmark_csv_file)
        mapping_df = pd.read_csv(args.mapping_csv_file)

    except:
        print("Error in reading csv files.")
        exit()

    tags_of_interest = []

    benchmark_df["pyradiomics_tag"] = benchmark_df["tag"]


    for f_ibsi, f_pyradiomics in zip(mapping_df["IBSIName"], mapping_df["PyradiomicsFeature"]):
        f_ibsi = f_ibsi.lstrip("F").replace(".", "_")
        match_condition = benchmark_df['tag'].str.contains(f_ibsi)

        benchmark_df.loc[match_condition, 'your_result'] = pipeline_df[f_pyradiomics].values[0]

        benchmark_df.loc[match_condition, 'pyradiomics_tag'] = f_pyradiomics

        tags_of_interest.append(benchmark_df[match_condition & benchmark_df['benchmark_value'].notnull()])


    matched_df = pd.concat(tags_of_interest)

    matched_df["difference"] = (matched_df["your_result"] - matched_df["benchmark_value"]).abs()
    matched_df["check"] = matched_df["difference"] <= matched_df["tolerance"] 
 
    matched_df.to_csv(args.save_csv)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--pipeline_csv_file", help="Path to the pipeline generated CSV file")
    parser.add_argument("--benchmark_csv_file", help="Path to CSV file provided by IBSI for benchmarking", default='IBSI-1-configA.csv')
    parser.add_argument("--mapping_csv_file", help="Mapping file with correspondences between tags of IBSI and pyradiomics", default='Pyradiomics2IBSIFeatures.csv')
    parser.add_argument("--save_csv", help="Output csv file path", default="out.csv")

    args = parser.parse_args()
    main(args)