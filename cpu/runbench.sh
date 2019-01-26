#!/bin/bash

###################################################################################
# Exectue speccpu2006 int test
###################################################################################


function 400_test() {

echo '400'
cd 400.perlbench/
#40
time taskset -c 3 ./perlbench_base.gcc43-64bit -I./lib checkspam.pl 2500 5 25 11 150 1 1 1 1 > checkspam.2500.5.25.11.150.1.1.1.1.out 2> checkspam.2500.5.25.11.150.1.1.1.1.err
# Starting run for copy #0
time taskset -c 3 ./perlbench_base.gcc43-64bit -I./lib diffmail.pl 4 800 10 17 19 300 > diffmail.4.800.10.17.19.300.out 2> diffmail.4.800.10.17.19.300.err
# Starting run for copy #0
time taskset -c 3 ./perlbench_base.gcc43-64bit -I./lib splitmail.pl 1600 12 26 16 4500 > splitmail.1600.12.26.16.4500.out 2> splitmail.1600.12.26.16.4500.err
}


function 401_test() {
echo '401'
cd ../401.bzip2/
#401
# Starting run for copy #0
time taskset -c 3 ./bzip2_base.gcc43-64bit input.source 280 > input.source.out 2> input.source.err
# Starting run for copy #0
time taskset -c 3 ./bzip2_base.gcc43-64bit chicken.jpg 30 > chicken.jpg.out 2> chicken.jpg.err
# Starting run for copy #0
time taskset -c 3 ./bzip2_base.gcc43-64bit liberty.jpg 30 > liberty.jpg.out 2> liberty.jpg.err
# Starting run for copy #0
time taskset -c 3 ./bzip2_base.gcc43-64bit input.program 280 > input.program.out 2> input.program.err
# Starting run for copy #0
time taskset -c 3 ./bzip2_base.gcc43-64bit text.html 280 > text.html.out 2> text.html.err
# Starting run for copy #0
time taskset -c 3 ./bzip2_base.gcc43-64bit input.combined 200 > input.combined.out 2> input.combined.err
}


function 403_test() {
echo '403'
cd ../403.gcc/
#403
# Starting run for copy #0
time taskset -c 3 ./gcc_base.gcc43-64bit 166.in -o 166.s > 166.out 2> 166.err
# Starting run for copy #0
time taskset -c 3 ./gcc_base.gcc43-64bit 200.in -o 200.s > 200.out 2> 200.err
# Starting run for copy #0
time taskset -c 3 ./gcc_base.gcc43-64bit c-typeck.in -o c-typeck.s > c-typeck.out 2> c-typeck.err
# Starting run for copy #0
time taskset -c 3 ./gcc_base.gcc43-64bit cp-decl.in -o cp-decl.s > cp-decl.out 2> cp-decl.err
# Starting run for copy #0
time taskset -c 3 ./gcc_base.gcc43-64bit expr.in -o expr.s > expr.out 2> expr.err
# Starting run for copy #0
time taskset -c 3 ./gcc_base.gcc43-64bit expr2.in -o expr2.s > expr2.out 2> expr2.err
# Starting run for copy #0
time taskset -c 3 ./gcc_base.gcc43-64bit g23.in -o g23.s > g23.out 2> g23.err
# Starting run for copy #0
time taskset -c 3 ./gcc_base.gcc43-64bit s04.in -o s04.s > s04.out 2> s04.err
# Starting run for copy #0
time taskset -c 3 ./gcc_base.gcc43-64bit scilab.in -o scilab.s > scilab.out 2> scilab.err
}

function 429_test() {
echo '429'
cd ../429.mcf/
#429
# Starting run for copy #0
time taskset -c 3 ./mcf_base.gcc43-64bit inp.in > inp.out 2> inp.err
}


function 445_test() {
echo '445'
cd ../445.gobmk/
#445
# Use another -n on the command line to see chdir commands and env dump
# Starting run for copy #0
time taskset -c 3 ./gobmk_base.gcc43-64bit --quiet --mode gtp < 13x13.tst > 13x13.out 2> 13x13.err
# Starting run for copy #0
time taskset -c 3 ./gobmk_base.gcc43-64bit --quiet --mode gtp < nngs.tst > nngs.out 2> nngs.err
# Starting run for copy #0
time taskset -c 3 ./gobmk_base.gcc43-64bit --quiet --mode gtp < score2.tst > score2.out 2> score2.err
# Starting run for copy #0
time taskset -c 3 ./gobmk_base.gcc43-64bit --quiet --mode gtp < trevorc.tst > trevorc.out 2> trevorc.err
# Starting run for copy #0
time taskset -c 3 ./gobmk_base.gcc43-64bit --quiet --mode gtp < trevord.tst > trevord.out 2> trevord.err
}


function 456_test() {
echo '456'
cd ../456.hmmer/
#456
# Starting run for copy #0
time taskset -c 3 ./hmmer_base.gcc43-64bit nph3.hmm swiss41 > nph3.out 2> nph3.err
# Starting run for copy #0
time taskset -c 3 ./hmmer_base.gcc43-64bit --fixed 0 --mean 500 --num 500000 --sd 350 --seed 0 retro.hmm > retro.out 2> retro.err
}


function 458_test() {
echo '458'
cd ../458.sjeng/
#458
# Starting run for copy #0
time taskset -c 3 ./sjeng_base.gcc43-64bit ref.txt > ref.out 2> ref.err
}


function 462_test() {
echo '462'
cd ../462.libquantum/
#462
# Starting run for copy #0
time taskset -c 3 ./libquantum_base.gcc43-64bit 1397 8 > ref.out 2> ref.err
}


function 464_test() {
echo '464'
cd ../464.h264ref/
#464
# Starting run for copy #0
time taskset -c 3 ./h264ref_base.gcc43-64bit -d foreman_ref_encoder_baseline.cfg > foreman_ref_baseline_encodelog.out 2> foreman_ref_baseline_encodelog.err
# Starting run for copy #0
time taskset -c 3 ./h264ref_base.gcc43-64bit -d foreman_ref_encoder_main.cfg > foreman_ref_main_encodelog.out 2> foreman_ref_main_encodelog.err
# Starting run for copy #0
time taskset -c 3 ./h264ref_base.gcc43-64bit -d sss_encoder_main.cfg > sss_main_encodelog.out 2> sss_main_encodelog.err
}


function 471_test() {
echo '471'
cd ../471.omnetpp/
#471
time taskset -c 3 ./omnetpp_base.gcc43-64bit  omnetpp.ini > omnetpp.log 2> omnetpp.err
}


function 473_test() {
echo '473'
cd ../473.astar/
#473
# Starting run for copy #0
time taskset -c 3 ./astar_base.gcc43-64bit BigLakes2048.cfg > BigLakes2048.out 2> BigLakes2048.err
# Starting run for copy #0
time taskset -c 3 ./astar_base.gcc43-64bit rivers.cfg > rivers.out 2> rivers.err
}


function 483_test() {
echo '483'
cd ../483.xalancbmk/
#483
time taskset -c 3 ./Xalan_base.gcc43-64bit -v t5.xml xalanc.xsl > ref.out 2> ref.err
}

###################################################################################
# Exectue speccpu2006 fp test
###################################################################################

function 410_test() {
echo '410'
cd ../410.bwaves/
#410
# Starting run for copy #0
(time ${fix_core} ./bwaves_base.gcc43-64bit) 2>> ${result_csv}

}

function 416_test() {
echo '416'
cd ../416.gamess/
#416
# Starting run for copy #0
(time ${fix_core} ./gamess_base.gcc43-64bit < cytosine.2.config > cytosine.2.out) 2>> ${result_csv}
# Starting run for copy #0
(time ${fix_core} ./gamess_base.gcc43-64bit < h2ocu2+.gradient.config > h2ocu2+.gradient.out) 2>> ${result_csv}
# Starting run for copy #0
(time ${fix_core} ./gamess_base.gcc43-64bit < triazolium.config > triazolium.out) 2>> ${result_csv}
#eof
}

function 433_test() {
echo '433'
cd ../433.milc/
#433
# Starting run for copy #0
(time ${fix_core} ./milc_base.gcc43-64bit < su3imp.in > su3imp.out) 2>> ${result_csv}
#eof
}

function 434_test() {
echo '434'
cd ../434.zeusmp/
#434
# Starting run for copy #0
(time ${fix_core} ./zeusmp_base.gcc43-64bit > zeusmp.stdout) 2>> ${result_csv}
}


function 435_test() {
echo '435'
cd ../435.gromacs/
#435
# Starting run for copy #0
(time ${fix_core} ./gromacs_base.gcc43-64bit -silent -deffnm gromacs -nice 0) 2>> ${result_csv}
}

function 436_test() {
echo '436'
cd ../436.cactusADM/
#436
# Starting run for copy #0
(time ${fix_core} ./cactusADM_base.gcc43-64bit benchADM.par > benchADM.out) 2>> ${result_csv}
}

function 437_test() {
echo '437'
cd ../437.leslie3d/
#437
# Starting run for copy #0
(time ${fix_core} ./leslie3d_base.gcc43-64bit < leslie3d.in > leslie3d.stdout) 2>> ${result_csv}
}

function 444_test() {
echo '444'
cd ../444.namd/
#444
# Starting run for copy #0
(time ${fix_core} ./namd_base.gcc43-64bit --input namd.input --iterations 38 --output namd.out > namd.stdout) 2>> ${result_csv}
}

function 447_test() {
echo '447'
cd ../447.dealII/
#447
# Starting run for copy #0
(time ${fix_core} ./dealII_base.gcc43-64bit 23 > log) 2>> ${result_csv}
}

function 450_test() {
echo '450'
cd ../450.soplex/
#450
# Starting run for copy #0
(time ${fix_core} ./soplex_base.gcc43-64bit -s1 -e -m45000 pds-50.mps > pds-50.mps.out) 2>> ${result_csv}
# Starting run for copy #0
(time ${fix_core} ./soplex_base.gcc43-64bit -m3500 ref.mps > ref.out) 2>> ${result_csv}
}

function 453_test() {
echo '453'
cd ../453.povray/
#453
# Starting run for copy #0
(time ${fix_core} ./povray_base.gcc43-64bit SPEC-benchmark-ref.ini > SPEC-benchmark-ref.stdout) 2>> ${result_csv}
}

function 454_test() {
echo '454'
cd ../454.calculix/
#454
(time ${fix_core} ./calculix_base.gcc43-64bit -i  hyperviscoplastic > hyperviscoplastic.log) 2>> ${result_csv}
}

function 459_test() {
echo '459'
cd ../459.GemsFDTD/
#459
(time ${fix_core} ./GemsFDTD_base.gcc43-64bit > ref.log) 2>> ${result_csv}
}

function 465_test() {
echo '465'
cd ../465.tonto/
#465
(time ${fix_core} ./tonto_base.gcc43-64bit > tonto.out) 2>> ${result_csv}
}

function 470_test() {
#eof
echo '470'
cd ../470.lbm/
#470
(time ${fix_core} ./lbm_base.gcc43-64bit 3000 reference.dat 0 0 100_100_130_ldc.of > lbm.out) 2>> ${result_csv}
#:<<eof
}

function 481_test() {
echo '481'
cd ../481.wrf/
#481
(time ${fix_core} ./wrf_base.gcc43-64bit > rsl.out.0000) 2>> ${result_csv}
}

function 482_test() {
echo '482'
cd ../482.sphinx3/
#482
(time ${fix_core} ./sphinx_livepretend_base.gcc43-64bit ctlfile . args.an4 > an4.log) 2>> ${result_csv}
}

function int_test() {
    for item in 400 401 403 429 445 456 458 462 464 471 473 483
      $item_test 
}

function fp_test() {

    for i in 410 416 433 434 435 436 437 444 447 450 453 454 459 465 470 481 482
      $item_test


}

function all_test() {

     int_test
     fp_test 
}


###################################################################################
# Exectue speccpu2006 test
###################################################################################

show_usage="args: [-t -r]\
                  [--test_type=, --rate=]"

#获取参数
while [ -n "$1" ]
do
        case "$1" in
                -t |--test_type) opt_test=$2; shift 2;;
                -r |--rate) opt_rate=$2; shift 2;;
                --) break ;;
                *) echo $1,$2,$show_usage; break ;;
        esac
done

if [[ -z $opt_test || -z $opt_rate ]]; then
        echo $show_usage
        echo "test_type: $opt_test , rate: $opt_rate"
        exit 0
fi













