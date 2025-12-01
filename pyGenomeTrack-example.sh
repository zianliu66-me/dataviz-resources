#!/bin/bash
# pyGenomeTrack-example.sh
# A way to visualize a genome that uses the Python ecosystem


flag_maketracks=1
bw_files_0='out/igg/outs/atac_cut_sites.bigwig'
bw_files_1='out/exp/outs/atac_cut_sites.bigwig'
genes_ref="refdata-cellranger-arc-mm10-2020-A-2.0.0/genes/genes.gtf.gz"
ini_output='out/pygt-example.ini'
regions_bed='out/plotting-example.bed'
out_plotprefix='out/trackexample-'

if [ $flag_maketracks ]; then
	make_tracks_file \
    		--trackFiles \
    			"$bw_files_0" \
    			"$bw_files_1" \
        		"$genes_ref" \
    		-o "$ini_output"
fi

# Make tracks. Easier to use the bash-native loop here
while IFS=$'\t' read -r -a genomicArr; do
    region_name="${genomicArr[0]}:${genomicArr[1]}-${genomicArr[2]}"
    plot_title="${genomicArr[3]}"
    pyGenomeTracks \
        --tracks "$ini_output" \
        --region "$region_name" \
        -o "$out_plotprefix""$plot_title"'.pdf'
done < "$regions_bed"

