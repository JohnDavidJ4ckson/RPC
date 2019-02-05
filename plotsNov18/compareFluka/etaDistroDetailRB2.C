void etaDistroDetailRB2()
{
//=========Macro generated from canvas: c1/Canvas
//=========  (Tue Jan 22 23:55:18 2019) by ROOT version 6.12/04
   TCanvas *c1 = new TCanvas("c1", "Canvas",50,45,800,775);
   gStyle->SetOptFit(1);
   gStyle->SetOptStat(0);
   gStyle->SetOptTitle(0);
   c1->SetHighLightColor(2);
   c1->Range(-2.215091,-1.030215,1.886929,3.257248);
   c1->SetFillColor(0);
   c1->SetBorderMode(0);
   c1->SetBorderSize(2);
   c1->SetLogy();
   c1->SetLeftMargin(0.12);
   c1->SetRightMargin(0.04);
   c1->SetTopMargin(0.06);
   c1->SetFrameFillStyle(0);
   c1->SetFrameBorderMode(0);
   c1->SetFrameFillStyle(0);
   c1->SetFrameBorderMode(0);
   
   TMultiGraph *multigraph = new TMultiGraph();
   multigraph->SetName("");
   multigraph->SetTitle("RB1in");
   
   Double_t Graph_fx39[6] = {
   -1.30087,
   -1.418788,
   -1.54149,
   -1.006991,
   -1.088097,
   -1.186697};
   Double_t Graph_fy39[6] = {
   8.67,
   19.02,
   34.95,
   5.015,
   4.12,
   5};
   TGraph *graph = new TGraph(6,Graph_fx39,Graph_fy39);
   graph->SetName("Graph");
   graph->SetTitle("Layer 3 Endcap");
   graph->SetFillStyle(1000);
   graph->SetLineColor(4);
   graph->SetLineWidth(6);
   graph->SetMarkerColor(4);
   graph->SetMarkerStyle(25);
   graph->SetMarkerSize(1.5);
   
   TH1F *Graph_Graph39 = new TH1F("Graph_Graph39","Layer 3 Endcap",100,-1.59494,-0.9535416);
   Graph_Graph39->SetMinimum(1.037);
   Graph_Graph39->SetMaximum(38.033);
   Graph_Graph39->SetDirectory(0);
   Graph_Graph39->SetStats(0);
   Graph_Graph39->SetLineStyle(0);
   Graph_Graph39->SetMarkerStyle(20);
   Graph_Graph39->GetXaxis()->SetTitle("#eta");
   Graph_Graph39->GetXaxis()->SetLabelFont(42);
   Graph_Graph39->GetXaxis()->SetLabelOffset(0.007);
   Graph_Graph39->GetXaxis()->SetLabelSize(0.05);
   Graph_Graph39->GetXaxis()->SetTitleSize(0.06);
   Graph_Graph39->GetXaxis()->SetTitleOffset(0.9);
   Graph_Graph39->GetXaxis()->SetTitleFont(42);
   Graph_Graph39->GetYaxis()->SetTitle("RPC single hit rate (Hz/cm^{2})");
   Graph_Graph39->GetYaxis()->SetLabelFont(42);
   Graph_Graph39->GetYaxis()->SetLabelOffset(0.007);
   Graph_Graph39->GetYaxis()->SetLabelSize(0.05);
   Graph_Graph39->GetYaxis()->SetTitleSize(0.06);
   Graph_Graph39->GetYaxis()->SetTitleOffset(1.25);
   Graph_Graph39->GetYaxis()->SetTitleFont(42);
   Graph_Graph39->GetZaxis()->SetLabelFont(42);
   Graph_Graph39->GetZaxis()->SetLabelOffset(0.007);
   Graph_Graph39->GetZaxis()->SetLabelSize(0.05);
   Graph_Graph39->GetZaxis()->SetTitleSize(0.06);
   Graph_Graph39->GetZaxis()->SetTitleFont(42);
   graph->SetHistogram(Graph_Graph39);
   
   multigraph->Add(graph,"AP");
   
   Double_t Graph_fx40[4] = {
   -0.6402547,
   -0.3577033,
   -0.9968613,
   -0.8309316};
   Double_t Graph_fy40[4] = {
   2.29,
   1.65,
   4.7,
   3.71};
   graph = new TGraph(4,Graph_fx40,Graph_fy40);
   graph->SetName("Graph");
   graph->SetTitle("Layer 3 Wheel");
   graph->SetFillStyle(1000);
   graph->SetLineColor(4);
   graph->SetLineWidth(6);
   graph->SetMarkerColor(4);
   graph->SetMarkerStyle(21);
   graph->SetMarkerSize(1.5);
   
   TH1F *Graph_Graph40 = new TH1F("Graph_Graph40","Layer 3 Wheel",100,-1.060777,-0.2937875);
   Graph_Graph40->SetMinimum(1.345);
   Graph_Graph40->SetMaximum(5.005);
   Graph_Graph40->SetDirectory(0);
   Graph_Graph40->SetStats(0);
   Graph_Graph40->SetLineStyle(0);
   Graph_Graph40->SetMarkerStyle(20);
   Graph_Graph40->GetXaxis()->SetTitle("#eta");
   Graph_Graph40->GetXaxis()->SetLabelFont(42);
   Graph_Graph40->GetXaxis()->SetLabelOffset(0.007);
   Graph_Graph40->GetXaxis()->SetLabelSize(0.05);
   Graph_Graph40->GetXaxis()->SetTitleSize(0.06);
   Graph_Graph40->GetXaxis()->SetTitleOffset(0.9);
   Graph_Graph40->GetXaxis()->SetTitleFont(42);
   Graph_Graph40->GetYaxis()->SetTitle("RPC single hit rate (Hz/cm^{2})");
   Graph_Graph40->GetYaxis()->SetLabelFont(42);
   Graph_Graph40->GetYaxis()->SetLabelOffset(0.007);
   Graph_Graph40->GetYaxis()->SetLabelSize(0.05);
   Graph_Graph40->GetYaxis()->SetTitleSize(0.06);
   Graph_Graph40->GetYaxis()->SetTitleOffset(1.25);
   Graph_Graph40->GetYaxis()->SetTitleFont(42);
   Graph_Graph40->GetZaxis()->SetLabelFont(42);
   Graph_Graph40->GetZaxis()->SetLabelOffset(0.007);
   Graph_Graph40->GetZaxis()->SetLabelSize(0.05);
   Graph_Graph40->GetZaxis()->SetTitleSize(0.06);
   Graph_Graph40->GetZaxis()->SetTitleFont(42);
   graph->SetHistogram(Graph_Graph40);
   
   multigraph->Add(graph,"AP");
   
   Double_t Graph_fx41[6] = {
   1.30087,
   1.418788,
   1.54149,
   1.006991,
   1.088097,
   1.186697};
   Double_t Graph_fy41[6] = {
   7.165,
   16.775,
   29.81,
   4.53,
   4.02,
   4.33};
   graph = new TGraph(6,Graph_fx41,Graph_fy41);
   graph->SetName("Graph");
   graph->SetTitle("Layer 4 Endcap");
   graph->SetFillStyle(1000);
   graph->SetLineColor(5);
   graph->SetLineWidth(7);
   graph->SetMarkerColor(4);
   graph->SetMarkerStyle(25);
   graph->SetMarkerSize(1.5);
   
   TH1F *Graph_Graph41 = new TH1F("Graph_Graph41","Layer 4 Endcap",100,0.9535416,1.59494);
   Graph_Graph41->SetMinimum(1.441);
   Graph_Graph41->SetMaximum(32.389);
   Graph_Graph41->SetDirectory(0);
   Graph_Graph41->SetStats(0);
   Graph_Graph41->SetLineStyle(0);
   Graph_Graph41->SetMarkerStyle(20);
   Graph_Graph41->GetXaxis()->SetTitle("#eta");
   Graph_Graph41->GetXaxis()->SetLabelFont(42);
   Graph_Graph41->GetXaxis()->SetLabelOffset(0.007);
   Graph_Graph41->GetXaxis()->SetLabelSize(0.05);
   Graph_Graph41->GetXaxis()->SetTitleSize(0.06);
   Graph_Graph41->GetXaxis()->SetTitleOffset(0.9);
   Graph_Graph41->GetXaxis()->SetTitleFont(42);
   Graph_Graph41->GetYaxis()->SetTitle("RPC single hit rate (Hz/cm^{2})");
   Graph_Graph41->GetYaxis()->SetLabelFont(42);
   Graph_Graph41->GetYaxis()->SetLabelOffset(0.007);
   Graph_Graph41->GetYaxis()->SetLabelSize(0.05);
   Graph_Graph41->GetYaxis()->SetTitleSize(0.06);
   Graph_Graph41->GetYaxis()->SetTitleOffset(1.25);
   Graph_Graph41->GetYaxis()->SetTitleFont(42);
   Graph_Graph41->GetZaxis()->SetLabelFont(42);
   Graph_Graph41->GetZaxis()->SetLabelOffset(0.007);
   Graph_Graph41->GetZaxis()->SetLabelSize(0.05);
   Graph_Graph41->GetZaxis()->SetTitleSize(0.06);
   Graph_Graph41->GetZaxis()->SetTitleFont(42);
   graph->SetHistogram(Graph_Graph41);
   
   multigraph->Add(graph,"AP");
   
   Double_t Graph_fx42[6] = {
   0.1508182,
   -0.1620493,
   0.6307283,
   0.3519274,
   0.984016,
   0.8194372};
   Double_t Graph_fy42[6] = {
   1.16,
   1,
   3.13,
   1.44,
   4.23,
   3.01};
   graph = new TGraph(6,Graph_fx42,Graph_fy42);
   graph->SetName("Graph");
   graph->SetTitle("Layer 4 Wheel");
   graph->SetFillStyle(1000);
   graph->SetLineColor(5);
   graph->SetLineWidth(7);
   graph->SetMarkerColor(4);
   graph->SetMarkerStyle(21);
   graph->SetMarkerSize(1.5);
   
   TH1F *Graph_Graph42 = new TH1F("Graph_Graph42","Layer 4 Wheel",100,-0.2766558,1.098623);
   Graph_Graph42->SetMinimum(0.677);
   Graph_Graph42->SetMaximum(4.553);
   Graph_Graph42->SetDirectory(0);
   Graph_Graph42->SetStats(0);
   Graph_Graph42->SetLineStyle(0);
   Graph_Graph42->SetMarkerStyle(20);
   Graph_Graph42->GetXaxis()->SetTitle("#eta");
   Graph_Graph42->GetXaxis()->SetLabelFont(42);
   Graph_Graph42->GetXaxis()->SetLabelOffset(0.007);
   Graph_Graph42->GetXaxis()->SetLabelSize(0.05);
   Graph_Graph42->GetXaxis()->SetTitleSize(0.06);
   Graph_Graph42->GetXaxis()->SetTitleOffset(0.9);
   Graph_Graph42->GetXaxis()->SetTitleFont(42);
   Graph_Graph42->GetYaxis()->SetTitle("RPC single hit rate (Hz/cm^{2})");
   Graph_Graph42->GetYaxis()->SetLabelFont(42);
   Graph_Graph42->GetYaxis()->SetLabelOffset(0.007);
   Graph_Graph42->GetYaxis()->SetLabelSize(0.05);
   Graph_Graph42->GetYaxis()->SetTitleSize(0.06);
   Graph_Graph42->GetYaxis()->SetTitleOffset(1.25);
   Graph_Graph42->GetYaxis()->SetTitleFont(42);
   Graph_Graph42->GetZaxis()->SetLabelFont(42);
   Graph_Graph42->GetZaxis()->SetLabelOffset(0.007);
   Graph_Graph42->GetZaxis()->SetLabelSize(0.05);
   Graph_Graph42->GetZaxis()->SetTitleSize(0.06);
   Graph_Graph42->GetZaxis()->SetTitleFont(42);
   graph->SetHistogram(Graph_Graph42);
   
   multigraph->Add(graph,"AP");
   
   Double_t Graph_fx43[4] = {
   -0.5647852,
   -0.3653146,
   -0.961078,
   -0.7492043};
   Double_t Graph_fy43[4] = {
   1.81,
   1.31,
   4.33,
   3.37};
   graph = new TGraph(4,Graph_fx43,Graph_fy43);
   graph->SetName("Graph");
   graph->SetTitle("Layer 4 Wheel");
   graph->SetFillStyle(1000);
   graph->SetLineColor(5);
   graph->SetLineWidth(7);
   graph->SetMarkerColor(4);
   graph->SetMarkerStyle(23);
   graph->SetMarkerSize(1.5);
   
   TH1F *Graph_Graph43 = new TH1F("Graph_Graph43","Layer 4 Wheel",100,-1.020654,-0.3057383);
   Graph_Graph43->SetMinimum(1.008);
   Graph_Graph43->SetMaximum(4.632);
   Graph_Graph43->SetDirectory(0);
   Graph_Graph43->SetStats(0);
   Graph_Graph43->SetLineStyle(0);
   Graph_Graph43->SetMarkerStyle(20);
   Graph_Graph43->GetXaxis()->SetTitle("#eta");
   Graph_Graph43->GetXaxis()->SetLabelFont(42);
   Graph_Graph43->GetXaxis()->SetLabelOffset(0.007);
   Graph_Graph43->GetXaxis()->SetLabelSize(0.05);
   Graph_Graph43->GetXaxis()->SetTitleSize(0.06);
   Graph_Graph43->GetXaxis()->SetTitleOffset(0.9);
   Graph_Graph43->GetXaxis()->SetTitleFont(42);
   Graph_Graph43->GetYaxis()->SetTitle("RPC single hit rate (Hz/cm^{2})");
   Graph_Graph43->GetYaxis()->SetLabelFont(42);
   Graph_Graph43->GetYaxis()->SetLabelOffset(0.007);
   Graph_Graph43->GetYaxis()->SetLabelSize(0.05);
   Graph_Graph43->GetYaxis()->SetTitleSize(0.06);
   Graph_Graph43->GetYaxis()->SetTitleOffset(1.25);
   Graph_Graph43->GetYaxis()->SetTitleFont(42);
   Graph_Graph43->GetZaxis()->SetLabelFont(42);
   Graph_Graph43->GetZaxis()->SetLabelOffset(0.007);
   Graph_Graph43->GetZaxis()->SetLabelSize(0.05);
   Graph_Graph43->GetZaxis()->SetTitleSize(0.06);
   Graph_Graph43->GetZaxis()->SetTitleFont(42);
   graph->SetHistogram(Graph_Graph43);
   
   multigraph->Add(graph,"AP");
   
   Double_t Graph_fx44[6] = {
   0.1070081,
   -0.1177723,
   0.5727437,
   0.3707642,
   0.9726389,
   0.759068};
   Double_t Graph_fy44[6] = {
   0.99,
   1.15,
   2.05,
   1.43,
   3.51,
   3.57};
   graph = new TGraph(6,Graph_fx44,Graph_fy44);
   graph->SetName("Graph");
   graph->SetTitle("Layer 4 Wheel");
   graph->SetFillStyle(1000);
   graph->SetLineColor(5);
   graph->SetLineWidth(7);
   graph->SetMarkerColor(4);
   graph->SetMarkerStyle(23);
   graph->SetMarkerSize(1.5);
   
   TH1F *Graph_Graph44 = new TH1F("Graph_Graph44","Layer 4 Wheel",100,-0.2268135,1.08168);
   Graph_Graph44->SetMinimum(0.732);
   Graph_Graph44->SetMaximum(3.828);
   Graph_Graph44->SetDirectory(0);
   Graph_Graph44->SetStats(0);
   Graph_Graph44->SetLineStyle(0);
   Graph_Graph44->SetMarkerStyle(20);
   Graph_Graph44->GetXaxis()->SetTitle("#eta");
   Graph_Graph44->GetXaxis()->SetLabelFont(42);
   Graph_Graph44->GetXaxis()->SetLabelOffset(0.007);
   Graph_Graph44->GetXaxis()->SetLabelSize(0.05);
   Graph_Graph44->GetXaxis()->SetTitleSize(0.06);
   Graph_Graph44->GetXaxis()->SetTitleOffset(0.9);
   Graph_Graph44->GetXaxis()->SetTitleFont(42);
   Graph_Graph44->GetYaxis()->SetTitle("RPC single hit rate (Hz/cm^{2})");
   Graph_Graph44->GetYaxis()->SetLabelFont(42);
   Graph_Graph44->GetYaxis()->SetLabelOffset(0.007);
   Graph_Graph44->GetYaxis()->SetLabelSize(0.05);
   Graph_Graph44->GetYaxis()->SetTitleSize(0.06);
   Graph_Graph44->GetYaxis()->SetTitleOffset(1.25);
   Graph_Graph44->GetYaxis()->SetTitleFont(42);
   Graph_Graph44->GetZaxis()->SetLabelFont(42);
   Graph_Graph44->GetZaxis()->SetLabelOffset(0.007);
   Graph_Graph44->GetZaxis()->SetLabelSize(0.05);
   Graph_Graph44->GetZaxis()->SetTitleSize(0.06);
   Graph_Graph44->GetZaxis()->SetTitleFont(42);
   graph->SetHistogram(Graph_Graph44);
   
   multigraph->Add(graph,"AP");
   
   Double_t RB2_fx45[133] = {
   -1.053586,
   -1.041572,
   -1.029445,
   -1.017204,
   -1.004846,
   -0.99237,
   -0.9797751,
   -0.9670596,
   -0.9542222,
   -0.9412613,
   -0.9281756,
   -0.9149638,
   -0.9016245,
   -0.8881564,
   -0.8745581,
   -0.8608285,
   -0.8469663,
   -0.8329703,
   -0.8188394,
   -0.8045725,
   -0.7901687,
   -0.775627,
   -0.7609464,
   -0.7461263,
   -0.7311659,
   -0.7160645,
   -0.7008217,
   -0.6854371,
   -0.6699104,
   -0.6542413,
   -0.6384299,
   -0.6224763,
   -0.6063808,
   -0.5901437,
   -0.5737657,
   -0.5572475,
   -0.5405901,
   -0.5237947,
   -0.5068627,
   -0.4897955,
   -0.4725951,
   -0.4552634,
   -0.4378027,
   -0.4202156,
   -0.4025048,
   -0.3846734,
   -0.3667246,
   -0.348662,
   -0.3304893,
   -0.3122108,
   -0.2938306,
   -0.2753534,
   -0.2567841,
   -0.2381277,
   -0.2193897,
   -0.2005755,
   -0.181691,
   -0.1627422,
   -0.1437353,
   -0.1246767,
   -0.105573,
   -0.08643081,
   -0.06725697,
   -0.04805842,
   -0.02884215,
   -0.009615236,
   0.009615236,
   0.02884215,
   0.04805842,
   0.06725697,
   0.08643081,
   0.105573,
   0.1246767,
   0.1437353,
   0.1627422,
   0.181691,
   0.2005755,
   0.2193897,
   0.2381277,
   0.2567841,
   0.2753534,
   0.2938306,
   0.3122108,
   0.3304893,
   0.348662,
   0.3667246,
   0.3846734,
   0.4025048,
   0.4202156,
   0.4378027,
   0.4552634,
   0.4725951,
   0.4897955,
   0.5068627,
   0.5237947,
   0.5405901,
   0.5572475,
   0.5737657,
   0.5901437,
   0.6063808,
   0.6224763,
   0.6384299,
   0.6542413,
   0.6699104,
   0.6854371,
   0.7008217,
   0.7160645,
   0.7311659,
   0.7461263,
   0.7609464,
   0.775627,
   0.7901687,
   0.8045725,
   0.8188394,
   0.8329703,
   0.8469663,
   0.8608285,
   0.8745581,
   0.8881564,
   0.9016245,
   0.9149638,
   0.9281756,
   0.9412613,
   0.9542222,
   0.9670596,
   0.9797751,
   0.99237,
   1.004846,
   1.017204,
   1.029445,
   1.041572,
   1.053586,
   1.05955};
   Double_t RB2_fy45[133] = {
   4.950819,
   4.082847,
   4.379541,
   4.192521,
   2.890888,
   2.779551,
   4.355912,
   3.906284,
   3.303673,
   3.516265,
   4.429874,
   3.950556,
   3.756268,
   4.781566,
   4.435534,
   3.60508,
   3.226103,
   3.632962,
   3.726844,
   3.328402,
   3.826613,
   3.104588,
   3.870109,
   3.907393,
   3.537681,
   4.976782,
   3.865738,
   3.734548,
   2.103979,
   2.746458,
   2.269922,
   1.90278,
   2.452552,
   2.289008,
   1.782161,
   1.731592,
   1.664412,
   1.678247,
   2.44758,
   1.485556,
   1.236816,
   1.281414,
   1.465145,
   1.31448,
   1.379153,
   1.433508,
   1.430996,
   1.595432,
   2.480766,
   0.8610658,
   0.8700705,
   1.267476,
   0.7710968,
   1.235885,
   1.43728,
   0.8376313,
   0.624521,
   1.098268,
   0.8676181,
   0.8350705,
   0.9221045,
   0.8584674,
   0.9234652,
   0.5706072,
   0.8185985,
   1.330582,
   0.9238179,
   0.4577248,
   0.5462736,
   0.9089574,
   0.7329358,
   0.8428642,
   1.480666,
   0.6973135,
   0.9583901,
   0.7860167,
   1.244142,
   1.042401,
   0.9031688,
   1.1054,
   0.8490499,
   0.9506145,
   0.6810743,
   1.339425,
   0.9825973,
   0.9319505,
   1.255415,
   1.444849,
   1.41887,
   1.816463,
   1.834513,
   1.997987,
   1.628084,
   1.630536,
   1.825103,
   2.219164,
   1.893135,
   2.550726,
   2.641983,
   3.412588,
   2.899261,
   2.473698,
   2.786409,
   2.783766,
   3.729856,
   3.841024,
   2.405039,
   2.674264,
   2.821922,
   4.425625,
   3.520978,
   3.510097,
   3.561911,
   4.333319,
   4.422379,
   4.158473,
   3.82943,
   4.348824,
   5.050042,
   4.752982,
   4.910605,
   5.3536,
   4.937577,
   3.725598,
   4.911318,
   3.690507,
   3.863682,
   5.158178,
   4.335991,
   4.077626,
   4.781146,
   4.557869,
   4.557869};
   graph = new TGraph(133,RB2_fx45,RB2_fy45);
   graph->SetName("RB2");
   graph->SetTitle("");
   graph->SetFillColor(1);
   graph->SetLineColor(2);
   graph->SetLineWidth(4);
   graph->SetMarkerColor(2);
   graph->SetMarkerStyle(20);
   
   TH1F *Graph_Graph_RB21745 = new TH1F("Graph_Graph_RB21745","",133,-1.264899,1.270864);
   Graph_Graph_RB21745->SetMinimum(0.4119523);
   Graph_Graph_RB21745->SetMaximum(5.843188);
   Graph_Graph_RB21745->SetDirectory(0);
   Graph_Graph_RB21745->SetStats(0);
   Graph_Graph_RB21745->SetLineStyle(0);
   Graph_Graph_RB21745->SetMarkerStyle(20);
   Graph_Graph_RB21745->GetXaxis()->SetLabelFont(42);
   Graph_Graph_RB21745->GetXaxis()->SetLabelOffset(0.007);
   Graph_Graph_RB21745->GetXaxis()->SetLabelSize(0.05);
   Graph_Graph_RB21745->GetXaxis()->SetTitleSize(0.06);
   Graph_Graph_RB21745->GetXaxis()->SetTitleOffset(0.9);
   Graph_Graph_RB21745->GetXaxis()->SetTitleFont(42);
   Graph_Graph_RB21745->GetYaxis()->SetLabelFont(42);
   Graph_Graph_RB21745->GetYaxis()->SetLabelOffset(0.007);
   Graph_Graph_RB21745->GetYaxis()->SetLabelSize(0.05);
   Graph_Graph_RB21745->GetYaxis()->SetTitleSize(0.06);
   Graph_Graph_RB21745->GetYaxis()->SetTitleOffset(1.25);
   Graph_Graph_RB21745->GetYaxis()->SetTitleFont(42);
   Graph_Graph_RB21745->GetZaxis()->SetLabelFont(42);
   Graph_Graph_RB21745->GetZaxis()->SetLabelOffset(0.007);
   Graph_Graph_RB21745->GetZaxis()->SetLabelSize(0.05);
   Graph_Graph_RB21745->GetZaxis()->SetTitleSize(0.06);
   Graph_Graph_RB21745->GetZaxis()->SetTitleFont(42);
   graph->SetHistogram(Graph_Graph_RB21745);
   
   multigraph->Add(graph,"AP");
   
   Double_t RE2_fx46[74] = {
   -1.566226,
   -1.540101,
   -1.514823,
   -1.490345,
   -1.466629,
   -1.443635,
   -1.42133,
   -1.399681,
   -1.378656,
   -1.358229,
   -1.338373,
   -1.319062,
   -1.300275,
   -1.281989,
   -1.264184,
   -1.24684,
   -1.22994,
   -1.213466,
   -1.197402,
   -1.181733,
   -1.166444,
   -1.151522,
   -1.136953,
   -1.122725,
   -1.108827,
   -1.095246,
   -1.081973,
   -1.068997,
   -1.056309,
   -1.043899,
   -1.031757,
   -1.019877,
   -1.008249,
   -0.9968656,
   -0.9857197,
   -0.974804,
   -0.9694303,
   1.566226,
   1.540101,
   1.514823,
   1.490345,
   1.466629,
   1.443635,
   1.42133,
   1.399681,
   1.378656,
   1.358229,
   1.338373,
   1.319062,
   1.300275,
   1.281989,
   1.264184,
   1.24684,
   1.22994,
   1.213466,
   1.197402,
   1.181733,
   1.166444,
   1.151522,
   1.136953,
   1.122725,
   1.108827,
   1.095246,
   1.081973,
   1.068997,
   1.056309,
   1.043899,
   1.031757,
   1.019877,
   1.008249,
   0.9968656,
   0.9857197,
   0.974804,
   0.9694303};
   Double_t RE2_fy46[74] = {
   49.72748,
   43.19698,
   42.77219,
   37.94842,
   35.29684,
   31.72164,
   27.74867,
   25.76675,
   23.48924,
   22.16387,
   20.81307,
   20.42428,
   19.58233,
   19.82947,
   16.72208,
   18.68909,
   16.50878,
   18.15923,
   15.73543,
   18.37732,
   13.69642,
   13.70736,
   14.3006,
   14.1987,
   13.58849,
   13.63352,
   14.96923,
   14.15163,
   15.28388,
   16.83189,
   17.9305,
   18.10663,
   19.47646,
   23.66026,
   26.4489,
   30.8136,
   30.8136,
   49.75708,
   42.08487,
   44.50194,
   36.74236,
   34.14095,
   31.78911,
   29.93908,
   26.58785,
   26.35778,
   25.40924,
   23.21831,
   24.04648,
   21.61685,
   20.97253,
   19.76371,
   18.93973,
   15.10765,
   15.90398,
   15.16688,
   16.71751,
   15.44307,
   14.06592,
   14.89581,
   14.41405,
   15.65192,
   15.21405,
   15.31271,
   18.44787,
   20.06036,
   16.52838,
   18.72799,
   20.50735,
   21.32087,
   24.50685,
   28.48316,
   37.66272,
   37.66272};
   graph = new TGraph(74,RE2_fx46,RE2_fy46);
   graph->SetName("RE2");
   graph->SetTitle("");
   graph->SetFillColor(1);
   graph->SetLineColor(2);
   graph->SetLineWidth(4);
   graph->SetMarkerColor(2);
   graph->SetMarkerStyle(4);
   
   TH1F *Graph_Graph_RE21846 = new TH1F("Graph_Graph_RE21846","",100,-1.879471,1.879471);
   Graph_Graph_RE21846->SetMinimum(9.971632);
   Graph_Graph_RE21846->SetMaximum(53.37394);
   Graph_Graph_RE21846->SetDirectory(0);
   Graph_Graph_RE21846->SetStats(0);

   Int_t ci;      // for color index setting
   TColor *color; // for color definition with alpha
   ci = TColor::GetColor("#000099");
   Graph_Graph_RE21846->SetLineColor(ci);
   Graph_Graph_RE21846->GetXaxis()->SetTitle("#eta");
   Graph_Graph_RE21846->GetXaxis()->SetLabelFont(42);
   Graph_Graph_RE21846->GetXaxis()->SetLabelSize(0.035);
   Graph_Graph_RE21846->GetXaxis()->SetTitleSize(0.035);
   Graph_Graph_RE21846->GetXaxis()->SetTitleFont(42);
   Graph_Graph_RE21846->GetYaxis()->SetTitle("Particle Flux");
   Graph_Graph_RE21846->GetYaxis()->SetLabelFont(42);
   Graph_Graph_RE21846->GetYaxis()->SetLabelSize(0.035);
   Graph_Graph_RE21846->GetYaxis()->SetTitleSize(0.035);
   Graph_Graph_RE21846->GetYaxis()->SetTitleFont(42);
   Graph_Graph_RE21846->GetZaxis()->SetLabelFont(42);
   Graph_Graph_RE21846->GetZaxis()->SetLabelSize(0.035);
   Graph_Graph_RE21846->GetZaxis()->SetTitleSize(0.035);
   Graph_Graph_RE21846->GetZaxis()->SetTitleFont(42);
   graph->SetHistogram(Graph_Graph_RE21846);
   
   multigraph->Add(graph,"AP");
   multigraph->Draw("a");
   multigraph->GetXaxis()->SetTitle("#eta");
   multigraph->GetXaxis()->SetLabelFont(42);
   multigraph->GetXaxis()->SetLabelOffset(0.007);
   multigraph->GetXaxis()->SetLabelSize(0.043);
   multigraph->GetXaxis()->SetTitleSize(0.05);
   multigraph->GetXaxis()->SetTitleOffset(1.06);
   multigraph->GetXaxis()->SetTitleFont(42);
   multigraph->GetYaxis()->SetTitle("RPC single hit rate (Hz/cm^{2})");
   multigraph->GetYaxis()->SetLabelFont(42);
   multigraph->GetYaxis()->SetLabelOffset(0.008);
   multigraph->GetYaxis()->SetLabelSize(0.05);
   multigraph->GetYaxis()->SetTitleSize(0.06);
   multigraph->GetYaxis()->SetTitleOffset(0.87);
   multigraph->GetYaxis()->SetTitleFont(42);
   
   TPaveText *pt = new TPaveText(0.1,0.97,0.55,0.97,"brNDC");
   pt->SetBorderSize(0);
   pt->SetFillStyle(0);
   pt->SetTextSize(0.03);
   TText *pt_LaTex = pt->AddText("CMS Preliminary");
   pt->Draw();
   
   pt = new TPaveText(0.7,0.97,0.9,0.97,"brNDC");
   pt->SetBorderSize(0);
   pt->SetFillStyle(0);
   pt->SetTextSize(0.03);
   pt_LaTex = pt->AddText("1.5 #times 10^{34} Hz/cm^{2} (13 TeV)");
   pt->Draw();
   
   TLegend *leg = new TLegend(0.4,0.6,0.7,0.8,NULL,"brNDC");
   leg->SetTextFont(62);
   leg->SetTextSize(0.05);
   leg->SetLineColor(1);
   leg->SetLineStyle(1);
   leg->SetLineWidth(1);
   leg->SetFillColor(0);
   leg->SetFillStyle(1001);
   TLegendEntry *entry=leg->AddEntry("Graph","RE2","p");
   entry->SetLineColor(1);
   entry->SetLineStyle(1);
   entry->SetLineWidth(1);
   entry->SetMarkerColor(4);
   entry->SetMarkerStyle(25);
   entry->SetMarkerSize(1.5);
   entry->SetTextFont(62);
   entry=leg->AddEntry("Graph","RB2in","p");
   entry->SetLineColor(1);
   entry->SetLineStyle(1);
   entry->SetLineWidth(1);
   entry->SetMarkerColor(4);
   entry->SetMarkerStyle(21);
   entry->SetMarkerSize(1.5);
   entry->SetTextFont(62);
   entry=leg->AddEntry("Graph","RB2out","p");
   entry->SetLineColor(1);
   entry->SetLineStyle(1);
   entry->SetLineWidth(1);
   entry->SetMarkerColor(4);
   entry->SetMarkerStyle(23);
   entry->SetMarkerSize(1.5);
   entry->SetTextFont(62);
   entry=leg->AddEntry("RB2","Fluka Simulation","p");
   entry->SetLineColor(1);
   entry->SetLineStyle(1);
   entry->SetLineWidth(1);
   entry->SetMarkerColor(2);
   entry->SetMarkerStyle(20);
   entry->SetMarkerSize(1);
   entry->SetTextFont(62);
   leg->Draw();
   c1->Modified();
   c1->cd();
   c1->SetSelected(c1);
}
