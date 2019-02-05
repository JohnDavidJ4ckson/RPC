void etaDistroDetailRB1()
{
//=========Macro generated from canvas: c1/Canvas
//=========  (Tue Jan 22 23:55:16 2019) by ROOT version 6.12/04
   TCanvas *c1 = new TCanvas("c1", "Canvas",50,45,800,775);
   gStyle->SetOptFit(1);
   gStyle->SetOptStat(0);
   gStyle->SetOptTitle(0);
   c1->SetHighLightColor(2);
   c1->Range(-2.324873,-0.3463775,1.980447,3.213599);
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
   
   Double_t Graph_fx31[6] = {
   -1.269543,
   -1.38083,
   -1.554935,
   -0.9430065,
   -1.01269,
   -1.104428};
   Double_t Graph_fy31[6] = {
   4.93,
   7.92,
   14.07,
   2.11,
   1.595,
   1.975};
   TGraph *graph = new TGraph(6,Graph_fx31,Graph_fy31);
   graph->SetName("Graph");
   graph->SetTitle("Layer 1 Endcap");
   graph->SetFillStyle(1000);
   graph->SetLineColor(2);
   graph->SetLineWidth(4);
   graph->SetMarkerColor(4);
   graph->SetMarkerStyle(24);
   graph->SetMarkerSize(1.5);
   
   TH1F *Graph_Graph_Graph131 = new TH1F("Graph_Graph_Graph131","Layer 1 Endcap",100,-1.616128,-0.8818137);
   Graph_Graph_Graph131->SetMinimum(0.3475);
   Graph_Graph_Graph131->SetMaximum(15.3175);
   Graph_Graph_Graph131->SetDirectory(0);
   Graph_Graph_Graph131->SetStats(0);
   Graph_Graph_Graph131->SetLineStyle(0);
   Graph_Graph_Graph131->SetMarkerStyle(20);
   Graph_Graph_Graph131->GetXaxis()->SetTitle("#eta");
   Graph_Graph_Graph131->GetXaxis()->SetLabelFont(42);
   Graph_Graph_Graph131->GetXaxis()->SetLabelOffset(0.007);
   Graph_Graph_Graph131->GetXaxis()->SetLabelSize(0.05);
   Graph_Graph_Graph131->GetXaxis()->SetTitleSize(0.06);
   Graph_Graph_Graph131->GetXaxis()->SetTitleOffset(0.9);
   Graph_Graph_Graph131->GetXaxis()->SetTitleFont(42);
   Graph_Graph_Graph131->GetYaxis()->SetTitle("RPC single hit rate (Hz/cm^{2})");
   Graph_Graph_Graph131->GetYaxis()->SetLabelFont(42);
   Graph_Graph_Graph131->GetYaxis()->SetLabelOffset(0.007);
   Graph_Graph_Graph131->GetYaxis()->SetLabelSize(0.05);
   Graph_Graph_Graph131->GetYaxis()->SetTitleSize(0.06);
   Graph_Graph_Graph131->GetYaxis()->SetTitleOffset(1.25);
   Graph_Graph_Graph131->GetYaxis()->SetTitleFont(42);
   Graph_Graph_Graph131->GetZaxis()->SetLabelFont(42);
   Graph_Graph_Graph131->GetZaxis()->SetLabelOffset(0.007);
   Graph_Graph_Graph131->GetZaxis()->SetLabelSize(0.05);
   Graph_Graph_Graph131->GetZaxis()->SetTitleSize(0.06);
   Graph_Graph_Graph131->GetZaxis()->SetTitleFont(42);
   graph->SetHistogram(Graph_Graph_Graph131);
   
   multigraph->Add(graph,"AP");
   
   Double_t Graph_fx32[4] = {
   -0.6914756,
   -0.4535393,
   -1.112329,
   -0.9352334};
   Double_t Graph_fy32[4] = {
   11.21,
   7.22,
   17.11,
   15.98};
   graph = new TGraph(4,Graph_fx32,Graph_fy32);
   graph->SetName("Graph");
   graph->SetTitle("RB1 in");
   graph->SetFillStyle(1000);
   graph->SetMarkerColor(4);
   graph->SetMarkerStyle(20);
   graph->SetMarkerSize(1.5);
   
   TH1F *Graph_Graph_Graph232 = new TH1F("Graph_Graph_Graph232","RB1 in",100,-1.178207,-0.3876603);
   Graph_Graph_Graph232->SetMinimum(6.231);
   Graph_Graph_Graph232->SetMaximum(18.099);
   Graph_Graph_Graph232->SetDirectory(0);
   Graph_Graph_Graph232->SetStats(0);
   Graph_Graph_Graph232->SetLineStyle(0);
   Graph_Graph_Graph232->SetMarkerStyle(20);
   Graph_Graph_Graph232->GetXaxis()->SetTitle("#eta");
   Graph_Graph_Graph232->GetXaxis()->SetLabelFont(42);
   Graph_Graph_Graph232->GetXaxis()->SetLabelOffset(0.007);
   Graph_Graph_Graph232->GetXaxis()->SetLabelSize(0.05);
   Graph_Graph_Graph232->GetXaxis()->SetTitleSize(0.06);
   Graph_Graph_Graph232->GetXaxis()->SetTitleOffset(0.9);
   Graph_Graph_Graph232->GetXaxis()->SetTitleFont(42);
   Graph_Graph_Graph232->GetYaxis()->SetTitle("RPC single hit rate (Hz/cm^{2})");
   Graph_Graph_Graph232->GetYaxis()->SetLabelFont(42);
   Graph_Graph_Graph232->GetYaxis()->SetLabelOffset(0.007);
   Graph_Graph_Graph232->GetYaxis()->SetLabelSize(0.05);
   Graph_Graph_Graph232->GetYaxis()->SetTitleSize(0.06);
   Graph_Graph_Graph232->GetYaxis()->SetTitleOffset(1.25);
   Graph_Graph_Graph232->GetYaxis()->SetTitleFont(42);
   Graph_Graph_Graph232->GetZaxis()->SetLabelFont(42);
   Graph_Graph_Graph232->GetZaxis()->SetLabelOffset(0.007);
   Graph_Graph_Graph232->GetZaxis()->SetLabelSize(0.05);
   Graph_Graph_Graph232->GetZaxis()->SetTitleSize(0.06);
   Graph_Graph_Graph232->GetZaxis()->SetTitleFont(42);
   graph->SetHistogram(Graph_Graph_Graph232);
   
   multigraph->Add(graph,"AP");
   
   Double_t Graph_fx33[6] = {
   1.25092,
   1.36161,
   1.53501,
   0.940752,
   1.01269,
   1.104428};
   Double_t Graph_fy33[6] = {
   5.01,
   8.4,
   13.75,
   2.865,
   1.9,
   2.115};
   graph = new TGraph(6,Graph_fx33,Graph_fy33);
   graph->SetName("Graph");
   graph->SetTitle("Layer 3 Endcap");
   graph->SetFillStyle(1000);
   graph->SetLineColor(4);
   graph->SetLineWidth(6);
   graph->SetMarkerColor(4);
   graph->SetMarkerStyle(24);
   graph->SetMarkerSize(1.5);
   
   TH1F *Graph_Graph_Graph333 = new TH1F("Graph_Graph_Graph333","Layer 3 Endcap",100,0.8813262,1.594436);
   Graph_Graph_Graph333->SetMinimum(0.715);
   Graph_Graph_Graph333->SetMaximum(14.935);
   Graph_Graph_Graph333->SetDirectory(0);
   Graph_Graph_Graph333->SetStats(0);
   Graph_Graph_Graph333->SetLineStyle(0);
   Graph_Graph_Graph333->SetMarkerStyle(20);
   Graph_Graph_Graph333->GetXaxis()->SetTitle("#eta");
   Graph_Graph_Graph333->GetXaxis()->SetLabelFont(42);
   Graph_Graph_Graph333->GetXaxis()->SetLabelOffset(0.007);
   Graph_Graph_Graph333->GetXaxis()->SetLabelSize(0.05);
   Graph_Graph_Graph333->GetXaxis()->SetTitleSize(0.06);
   Graph_Graph_Graph333->GetXaxis()->SetTitleOffset(0.9);
   Graph_Graph_Graph333->GetXaxis()->SetTitleFont(42);
   Graph_Graph_Graph333->GetYaxis()->SetTitle("RPC single hit rate (Hz/cm^{2})");
   Graph_Graph_Graph333->GetYaxis()->SetLabelFont(42);
   Graph_Graph_Graph333->GetYaxis()->SetLabelOffset(0.007);
   Graph_Graph_Graph333->GetYaxis()->SetLabelSize(0.05);
   Graph_Graph_Graph333->GetYaxis()->SetTitleSize(0.06);
   Graph_Graph_Graph333->GetYaxis()->SetTitleOffset(1.25);
   Graph_Graph_Graph333->GetYaxis()->SetTitleFont(42);
   Graph_Graph_Graph333->GetZaxis()->SetLabelFont(42);
   Graph_Graph_Graph333->GetZaxis()->SetLabelOffset(0.007);
   Graph_Graph_Graph333->GetZaxis()->SetLabelSize(0.05);
   Graph_Graph_Graph333->GetZaxis()->SetTitleSize(0.06);
   Graph_Graph_Graph333->GetZaxis()->SetTitleFont(42);
   graph->SetHistogram(Graph_Graph_Graph333);
   
   multigraph->Add(graph,"AP");
   
   Double_t Graph_fx34[6] = {
   0.1378691,
   -0.1516978,
   0.7169072,
   0.4716459,
   1.146298,
   0.966242};
   Double_t Graph_fy34[6] = {
   3.14,
   2.8,
   11.12,
   5.88,
   23.37,
   22.4};
   graph = new TGraph(6,Graph_fx34,Graph_fy34);
   graph->SetName("Graph");
   graph->SetTitle("Layer 3 Wheel");
   graph->SetFillStyle(1000);
   graph->SetLineColor(4);
   graph->SetLineWidth(6);
   graph->SetMarkerColor(4);
   graph->SetMarkerStyle(20);
   graph->SetMarkerSize(1.5);
   
   TH1F *Graph_Graph_Graph434 = new TH1F("Graph_Graph_Graph434","Layer 3 Wheel",100,-0.2814974,1.276098);
   Graph_Graph_Graph434->SetMinimum(0.743);
   Graph_Graph_Graph434->SetMaximum(25.427);
   Graph_Graph_Graph434->SetDirectory(0);
   Graph_Graph_Graph434->SetStats(0);
   Graph_Graph_Graph434->SetLineStyle(0);
   Graph_Graph_Graph434->SetMarkerStyle(20);
   Graph_Graph_Graph434->GetXaxis()->SetTitle("#eta");
   Graph_Graph_Graph434->GetXaxis()->SetLabelFont(42);
   Graph_Graph_Graph434->GetXaxis()->SetLabelOffset(0.007);
   Graph_Graph_Graph434->GetXaxis()->SetLabelSize(0.05);
   Graph_Graph_Graph434->GetXaxis()->SetTitleSize(0.06);
   Graph_Graph_Graph434->GetXaxis()->SetTitleOffset(0.9);
   Graph_Graph_Graph434->GetXaxis()->SetTitleFont(42);
   Graph_Graph_Graph434->GetYaxis()->SetTitle("RPC single hit rate (Hz/cm^{2})");
   Graph_Graph_Graph434->GetYaxis()->SetLabelFont(42);
   Graph_Graph_Graph434->GetYaxis()->SetLabelOffset(0.007);
   Graph_Graph_Graph434->GetYaxis()->SetLabelSize(0.05);
   Graph_Graph_Graph434->GetYaxis()->SetTitleSize(0.06);
   Graph_Graph_Graph434->GetYaxis()->SetTitleOffset(1.25);
   Graph_Graph_Graph434->GetYaxis()->SetTitleFont(42);
   Graph_Graph_Graph434->GetZaxis()->SetLabelFont(42);
   Graph_Graph_Graph434->GetZaxis()->SetLabelOffset(0.007);
   Graph_Graph_Graph434->GetZaxis()->SetLabelSize(0.05);
   Graph_Graph_Graph434->GetZaxis()->SetTitleSize(0.06);
   Graph_Graph_Graph434->GetZaxis()->SetTitleFont(42);
   graph->SetHistogram(Graph_Graph_Graph434);
   
   multigraph->Add(graph,"AP");
   
   Double_t Graph_fx35[4] = {
   -0.6684232,
   -0.4372446,
   -1.081175,
   -0.9069221};
   Double_t Graph_fy35[4] = {
   8.42,
   6.03,
   12.68,
   12.44};
   graph = new TGraph(4,Graph_fx35,Graph_fy35);
   graph->SetName("Graph");
   graph->SetTitle("Layer 1 Wheel");
   graph->SetFillStyle(1000);
   graph->SetLineColor(2);
   graph->SetLineWidth(4);
   graph->SetMarkerColor(4);
   graph->SetMarkerStyle(29);
   graph->SetMarkerSize(1.7);
   
   TH1F *Graph_Graph_Graph835 = new TH1F("Graph_Graph_Graph835","Layer 1 Wheel",100,-1.145568,-0.3728516);
   Graph_Graph_Graph835->SetMinimum(5.365);
   Graph_Graph_Graph835->SetMaximum(13.345);
   Graph_Graph_Graph835->SetDirectory(0);
   Graph_Graph_Graph835->SetStats(0);
   Graph_Graph_Graph835->SetLineStyle(0);
   Graph_Graph_Graph835->SetMarkerStyle(20);
   Graph_Graph_Graph835->GetXaxis()->SetTitle("#eta");
   Graph_Graph_Graph835->GetXaxis()->SetLabelFont(42);
   Graph_Graph_Graph835->GetXaxis()->SetLabelOffset(0.007);
   Graph_Graph_Graph835->GetXaxis()->SetLabelSize(0.05);
   Graph_Graph_Graph835->GetXaxis()->SetTitleSize(0.06);
   Graph_Graph_Graph835->GetXaxis()->SetTitleOffset(0.9);
   Graph_Graph_Graph835->GetXaxis()->SetTitleFont(42);
   Graph_Graph_Graph835->GetYaxis()->SetTitle("RPC single hit rate (Hz/cm^{2})");
   Graph_Graph_Graph835->GetYaxis()->SetLabelFont(42);
   Graph_Graph_Graph835->GetYaxis()->SetLabelOffset(0.007);
   Graph_Graph_Graph835->GetYaxis()->SetLabelSize(0.05);
   Graph_Graph_Graph835->GetYaxis()->SetTitleSize(0.06);
   Graph_Graph_Graph835->GetYaxis()->SetTitleOffset(1.25);
   Graph_Graph_Graph835->GetYaxis()->SetTitleFont(42);
   Graph_Graph_Graph835->GetZaxis()->SetLabelFont(42);
   Graph_Graph_Graph835->GetZaxis()->SetLabelOffset(0.007);
   Graph_Graph_Graph835->GetZaxis()->SetLabelSize(0.05);
   Graph_Graph_Graph835->GetZaxis()->SetTitleSize(0.06);
   Graph_Graph_Graph835->GetZaxis()->SetTitleFont(42);
   graph->SetHistogram(Graph_Graph_Graph835);
   
   multigraph->Add(graph,"AP");
   
   Double_t Graph_fx36[6] = {
   0.1232712,
   -0.1356536,
   0.6501188,
   0.4243846,
   1.056183,
   0.8843007};
   Double_t Graph_fy36[6] = {
   3.05,
   2.89,
   7.54,
   5.77,
   14.6,
   13.21};
   graph = new TGraph(6,Graph_fx36,Graph_fy36);
   graph->SetName("Graph");
   graph->SetTitle("Layer 4 Wheel");
   graph->SetFillStyle(1000);
   graph->SetLineColor(5);
   graph->SetLineWidth(7);
   graph->SetMarkerColor(4);
   graph->SetMarkerStyle(29);
   graph->SetMarkerSize(1.5);
   
   TH1F *Graph_Graph_Graph1036 = new TH1F("Graph_Graph_Graph1036","Layer 4 Wheel",100,-0.2548373,1.175367);
   Graph_Graph_Graph1036->SetMinimum(1.719);
   Graph_Graph_Graph1036->SetMaximum(15.771);
   Graph_Graph_Graph1036->SetDirectory(0);
   Graph_Graph_Graph1036->SetStats(0);
   Graph_Graph_Graph1036->SetLineStyle(0);
   Graph_Graph_Graph1036->SetMarkerStyle(20);
   Graph_Graph_Graph1036->GetXaxis()->SetTitle("#eta");
   Graph_Graph_Graph1036->GetXaxis()->SetLabelFont(42);
   Graph_Graph_Graph1036->GetXaxis()->SetLabelOffset(0.007);
   Graph_Graph_Graph1036->GetXaxis()->SetLabelSize(0.05);
   Graph_Graph_Graph1036->GetXaxis()->SetTitleSize(0.06);
   Graph_Graph_Graph1036->GetXaxis()->SetTitleOffset(0.9);
   Graph_Graph_Graph1036->GetXaxis()->SetTitleFont(42);
   Graph_Graph_Graph1036->GetYaxis()->SetTitle("RPC single hit rate (Hz/cm^{2})");
   Graph_Graph_Graph1036->GetYaxis()->SetLabelFont(42);
   Graph_Graph_Graph1036->GetYaxis()->SetLabelOffset(0.007);
   Graph_Graph_Graph1036->GetYaxis()->SetLabelSize(0.05);
   Graph_Graph_Graph1036->GetYaxis()->SetTitleSize(0.06);
   Graph_Graph_Graph1036->GetYaxis()->SetTitleOffset(1.25);
   Graph_Graph_Graph1036->GetYaxis()->SetTitleFont(42);
   Graph_Graph_Graph1036->GetZaxis()->SetLabelFont(42);
   Graph_Graph_Graph1036->GetZaxis()->SetLabelOffset(0.007);
   Graph_Graph_Graph1036->GetZaxis()->SetLabelSize(0.05);
   Graph_Graph_Graph1036->GetZaxis()->SetTitleSize(0.06);
   Graph_Graph_Graph1036->GetZaxis()->SetTitleFont(42);
   graph->SetHistogram(Graph_Graph_Graph1036);
   
   multigraph->Add(graph,"AP");
   
   Double_t RB1_fx37[133] = {
   -1.217389,
   -1.204512,
   -1.191496,
   -1.178337,
   -1.165033,
   -1.151583,
   -1.137982,
   -1.124229,
   -1.110322,
   -1.096257,
   -1.082033,
   -1.067645,
   -1.053093,
   -1.038373,
   -1.023483,
   -1.00842,
   -0.9931808,
   -0.9777637,
   -0.9621657,
   -0.9463842,
   -0.9304168,
   -0.9142608,
   -0.8979139,
   -0.8813736,
   -0.8646375,
   -0.8477035,
   -0.8305693,
   -0.8132329,
   -0.7956923,
   -0.7779458,
   -0.7599917,
   -0.7418286,
   -0.7234552,
   -0.7048704,
   -0.6860734,
   -0.6670637,
   -0.6478409,
   -0.6284051,
   -0.6087566,
   -0.5888962,
   -0.5688249,
   -0.5485442,
   -0.528056,
   -0.5073626,
   -0.486467,
   -0.4653724,
   -0.4440827,
   -0.4226024,
   -0.4009363,
   -0.37909,
   -0.3570697,
   -0.334882,
   -0.3125342,
   -0.2900342,
   -0.2673905,
   -0.2446121,
   -0.2217086,
   -0.1986901,
   -0.1755673,
   -0.1523511,
   -0.1290532,
   -0.1056855,
   -0.08226014,
   -0.05878966,
   -0.03528679,
   -0.01176443,
   0.01176443,
   0.03528679,
   0.05878966,
   0.08226014,
   0.1056855,
   0.1290532,
   0.1523511,
   0.1755673,
   0.1986901,
   0.2217086,
   0.2446121,
   0.2673905,
   0.2900342,
   0.3125342,
   0.334882,
   0.3570697,
   0.37909,
   0.4009363,
   0.4226024,
   0.4440827,
   0.4653724,
   0.486467,
   0.5073626,
   0.528056,
   0.5485442,
   0.5688249,
   0.5888962,
   0.6087566,
   0.6284051,
   0.6478409,
   0.6670637,
   0.6860734,
   0.7048704,
   0.7234552,
   0.7418286,
   0.7599917,
   0.7779458,
   0.7956923,
   0.8132329,
   0.8305693,
   0.8477035,
   0.8646375,
   0.8813736,
   0.8979139,
   0.9142608,
   0.9304168,
   0.9463842,
   0.9621657,
   0.9777637,
   0.9931808,
   1.00842,
   1.023483,
   1.038373,
   1.053093,
   1.067645,
   1.082033,
   1.096257,
   1.110322,
   1.124229,
   1.137982,
   1.151583,
   1.165033,
   1.178337,
   1.191496,
   1.204512,
   1.217389,
   1.223775};
   Double_t RB1_fy37[133] = {
   14.35587,
   17.04314,
   14.00669,
   20.75583,
   18.87226,
   20.29945,
   20.9028,
   18.78981,
   19.48845,
   38.85177,
   21.49524,
   35.12606,
   21.24412,
   19.2741,
   23.28979,
   26.68679,
   24.36488,
   28.67566,
   24.2919,
   23.22084,
   20.07011,
   20.50949,
   19.74358,
   18.84393,
   16.13341,
   15.58126,
   18.00668,
   15.8139,
   18.42738,
   15.25207,
   13.82394,
   16.5676,
   13.66563,
   12.9871,
   15.67038,
   15.09239,
   13.07929,
   11.60308,
   11.75712,
   9.466366,
   9.969821,
   9.632773,
   8.518782,
   10.43695,
   8.28745,
   11.72638,
   13.92105,
   12.25865,
   9.050624,
   9.245236,
   10.00097,
   6.829585,
   5.763368,
   8.62826,
   8.550679,
   5.355077,
   5.121437,
   5.288715,
   4.133575,
   4.460507,
   4.826904,
   5.339343,
   5.965509,
   5.11343,
   5.076316,
   4.472533,
   4.898827,
   4.472917,
   5.642775,
   3.992347,
   4.483537,
   5.416802,
   3.609136,
   4.39775,
   4.448063,
   4.673975,
   4.536643,
   5.739515,
   7.142173,
   7.85153,
   7.731059,
   8.98611,
   7.035293,
   7.270968,
   6.969673,
   7.950385,
   8.824398,
   11.52714,
   10.25254,
   7.759439,
   12.03995,
   8.978055,
   10.17909,
   10.79639,
   11.90513,
   11.09492,
   10.71764,
   11.12856,
   14.28275,
   13.15499,
   12.88957,
   14.46974,
   14.3689,
   14.19652,
   16.04975,
   18.36733,
   15.15213,
   17.25865,
   18.71487,
   20.13484,
   20.32613,
   23.16743,
   22.37122,
   24.33465,
   22.29591,
   23.24682,
   27.00186,
   24.85142,
   21.09602,
   20.9623,
   21.62863,
   23.16478,
   21.05564,
   35.01475,
   20.1187,
   20.41947,
   19.81513,
   18.67501,
   17.75633,
   24.52921,
   15.72721,
   13.29749,
   13.29749};
   graph = new TGraph(133,RB1_fx37,RB1_fy37);
   graph->SetName("RB1");
   graph->SetTitle("");
   graph->SetFillColor(1);
   graph->SetLineColor(2);
   graph->SetLineWidth(4);
   graph->SetMarkerColor(2);
   graph->SetMarkerStyle(20);
   
   TH1F *Graph_Graph_Graph_RB151137 = new TH1F("Graph_Graph_Graph_RB151137","",133,-1.461505,1.467892);
   Graph_Graph_Graph_RB151137->SetMinimum(0.0848724);
   Graph_Graph_Graph_RB151137->SetMaximum(42.37603);
   Graph_Graph_Graph_RB151137->SetDirectory(0);
   Graph_Graph_Graph_RB151137->SetStats(0);

   Int_t ci;      // for color index setting
   TColor *color; // for color definition with alpha
   ci = TColor::GetColor("#000099");
   Graph_Graph_Graph_RB151137->SetLineColor(ci);
   Graph_Graph_Graph_RB151137->GetXaxis()->SetTitle("#eta");
   Graph_Graph_Graph_RB151137->GetXaxis()->SetLabelFont(42);
   Graph_Graph_Graph_RB151137->GetXaxis()->SetLabelSize(0.035);
   Graph_Graph_Graph_RB151137->GetXaxis()->SetTitleSize(0.035);
   Graph_Graph_Graph_RB151137->GetXaxis()->SetTitleFont(42);
   Graph_Graph_Graph_RB151137->GetYaxis()->SetTitle("Particle Flux");
   Graph_Graph_Graph_RB151137->GetYaxis()->SetLabelFont(42);
   Graph_Graph_Graph_RB151137->GetYaxis()->SetLabelSize(0.035);
   Graph_Graph_Graph_RB151137->GetYaxis()->SetTitleSize(0.035);
   Graph_Graph_Graph_RB151137->GetYaxis()->SetTitleFont(42);
   Graph_Graph_Graph_RB151137->GetZaxis()->SetLabelFont(42);
   Graph_Graph_Graph_RB151137->GetZaxis()->SetLabelSize(0.035);
   Graph_Graph_Graph_RB151137->GetZaxis()->SetTitleSize(0.035);
   Graph_Graph_Graph_RB151137->GetZaxis()->SetTitleFont(42);
   graph->SetHistogram(Graph_Graph_Graph_RB151137);
   
   multigraph->Add(graph,"AP");
   
   Double_t RE1_fx38[88] = {
   -1.64385,
   -1.610787,
   -1.579029,
   -1.548492,
   -1.519101,
   -1.490785,
   -1.463482,
   -1.437135,
   -1.411691,
   -1.3871,
   -1.363318,
   -1.340305,
   -1.318021,
   -1.29643,
   -1.275501,
   -1.255202,
   -1.235504,
   -1.216381,
   -1.197807,
   -1.179759,
   -1.162214,
   -1.145152,
   -1.128552,
   -1.112397,
   -1.096669,
   -1.081351,
   -1.066428,
   -1.051884,
   -1.037706,
   -1.023881,
   -1.010394,
   -0.9972357,
   -0.984393,
   -0.9718553,
   -0.9596121,
   -0.9476536,
   -0.93597,
   -0.9245525,
   -0.9133922,
   -0.9024809,
   -0.8918105,
   -0.8813736,
   -0.8711627,
   -0.8661398,
   1.64385,
   1.610787,
   1.579029,
   1.548492,
   1.519101,
   1.490785,
   1.463482,
   1.437135,
   1.411691,
   1.3871,
   1.363318,
   1.340305,
   1.318021,
   1.29643,
   1.275501,
   1.255202,
   1.235504,
   1.216381,
   1.197807,
   1.179759,
   1.162214,
   1.145152,
   1.128552,
   1.112397,
   1.096669,
   1.081351,
   1.066428,
   1.051884,
   1.037706,
   1.023881,
   1.010394,
   0.9972357,
   0.984393,
   0.9718553,
   0.9596121,
   0.9476536,
   0.93597,
   0.9245525,
   0.9133922,
   0.9024809,
   0.8918105,
   0.8813736,
   0.8711627,
   0.8661398};
   Double_t RE1_fy38[88] = {
   32.11991,
   33.5322,
   34.55772,
   27.71721,
   27.83259,
   23.97492,
   28.61762,
   25.66029,
   19.29823,
   22.41841,
   19.74444,
   19.87311,
   23.44681,
   18.37057,
   15.25069,
   18.82816,
   18.35203,
   12.90901,
   13.45268,
   11.23683,
   8.242119,
   9.219868,
   10.96681,
   8.524131,
   8.036029,
   8.140464,
   8.628419,
   7.692684,
   9.002812,
   7.103019,
   7.819879,
   7.679058,
   10.38284,
   8.396053,
   7.727733,
   10.47913,
   11.85229,
   14.98457,
   18.12015,
   22.69014,
   25.75011,
   24.47215,
   24.72251,
   24.72251,
   30.72206,
   38.63645,
   30.92221,
   29.30057,
   26.45369,
   31.15161,
   24.28481,
   23.78302,
   25.02385,
   19.92068,
   22.44595,
   20.16444,
   16.40243,
   17.95867,
   23.37209,
   23.69401,
   23.1886,
   16.68589,
   13.18479,
   13.81451,
   12.53761,
   10.77974,
   10.89971,
   10.05369,
   9.792868,
   10.07204,
   10.26933,
   8.190818,
   8.43545,
   10.39116,
   11.39468,
   10.9817,
   11.87317,
   14.1379,
   11.31579,
   14.43205,
   20.68057,
   20.85462,
   19.38402,
   23.01924,
   24.5388,
   30.61799,
   31.67509,
   31.67509};
   graph = new TGraph(88,RE1_fx38,RE1_fy38);
   graph->SetName("RE1");
   graph->SetTitle("");
   graph->SetFillColor(1);
   graph->SetLineColor(2);
   graph->SetLineWidth(4);
   graph->SetMarkerColor(2);
   graph->SetMarkerStyle(4);
   
   TH1F *Graph_Graph_Graph_RE161238 = new TH1F("Graph_Graph_Graph_RE161238","",100,-1.972619,1.972619);
   Graph_Graph_Graph_RE161238->SetMinimum(3.949676);
   Graph_Graph_Graph_RE161238->SetMaximum(41.78979);
   Graph_Graph_Graph_RE161238->SetDirectory(0);
   Graph_Graph_Graph_RE161238->SetStats(0);

   ci = TColor::GetColor("#000099");
   Graph_Graph_Graph_RE161238->SetLineColor(ci);
   Graph_Graph_Graph_RE161238->GetXaxis()->SetTitle("#eta");
   Graph_Graph_Graph_RE161238->GetXaxis()->SetLabelFont(42);
   Graph_Graph_Graph_RE161238->GetXaxis()->SetLabelSize(0.035);
   Graph_Graph_Graph_RE161238->GetXaxis()->SetTitleSize(0.035);
   Graph_Graph_Graph_RE161238->GetXaxis()->SetTitleFont(42);
   Graph_Graph_Graph_RE161238->GetYaxis()->SetTitle("Particle Flux");
   Graph_Graph_Graph_RE161238->GetYaxis()->SetLabelFont(42);
   Graph_Graph_Graph_RE161238->GetYaxis()->SetLabelSize(0.035);
   Graph_Graph_Graph_RE161238->GetYaxis()->SetTitleSize(0.035);
   Graph_Graph_Graph_RE161238->GetYaxis()->SetTitleFont(42);
   Graph_Graph_Graph_RE161238->GetZaxis()->SetLabelFont(42);
   Graph_Graph_Graph_RE161238->GetZaxis()->SetLabelSize(0.035);
   Graph_Graph_Graph_RE161238->GetZaxis()->SetTitleSize(0.035);
   Graph_Graph_Graph_RE161238->GetZaxis()->SetTitleFont(42);
   graph->SetHistogram(Graph_Graph_Graph_RE161238);
   
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
   
   TLegend *leg = new TLegend(0.4,0.7,0.7,0.9,NULL,"brNDC");
   leg->SetTextFont(62);
   leg->SetTextSize(0.05);
   leg->SetLineColor(1);
   leg->SetLineStyle(1);
   leg->SetLineWidth(1);
   leg->SetFillColor(0);
   leg->SetFillStyle(1001);
   TLegendEntry *entry=leg->AddEntry("Graph","RE1","p");
   entry->SetLineColor(1);
   entry->SetLineStyle(1);
   entry->SetLineWidth(1);
   entry->SetMarkerColor(4);
   entry->SetMarkerStyle(24);
   entry->SetMarkerSize(1.5);
   entry->SetTextFont(62);
   entry=leg->AddEntry("Graph","RB1in","p");
   entry->SetLineColor(1);
   entry->SetLineStyle(1);
   entry->SetLineWidth(1);
   entry->SetMarkerColor(4);
   entry->SetMarkerStyle(20);
   entry->SetMarkerSize(1.5);
   entry->SetTextFont(62);
   entry=leg->AddEntry("Graph","RB1out","p");
   entry->SetLineColor(1);
   entry->SetLineStyle(1);
   entry->SetLineWidth(1);
   entry->SetMarkerColor(4);
   entry->SetMarkerStyle(29);
   entry->SetMarkerSize(1.7);
   entry->SetTextFont(62);
   entry=leg->AddEntry("RB1","Fluka Simulation","p");
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
