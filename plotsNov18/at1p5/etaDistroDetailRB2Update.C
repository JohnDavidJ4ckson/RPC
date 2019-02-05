void etaDistroDetailRB2()
{
//=========Macro generated from canvas: c1/Canvas
//=========  (Fri Jan 18 17:33:33 2019) by ROOT version 6.12/04
   TCanvas *c1 = new TCanvas("c1", "Canvas",50,45,800,775);
   gStyle->SetOptFit(1);
   gStyle->SetOptStat(0);
   gStyle->SetOptTitle(0);
   c1->SetHighLightColor(2);
   c1->Range(-2.180107,-0.597762,1.857128,3.229644);
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
   
   Double_t Graph_fx27[6] = {
   -1.30087,
   -1.418788,
   -1.54149,
   -1.006991,
   -1.088097,
   -1.186697};
   Double_t Graph_fy27[6] = {
   8.67,
   19.02,
   34.95,
   5.015,
   4.12,
   5};
   TGraph *graph = new TGraph(6,Graph_fx27,Graph_fy27);
   graph->SetName("Graph");
   graph->SetTitle("Layer 3 Endcap");
   graph->SetFillStyle(1000);
   graph->SetLineColor(4);
   graph->SetLineWidth(6);

   Int_t ci;      // for color index setting
   TColor *color; // for color definition with alpha
   ci = TColor::GetColor("#ff0000");
   graph->SetMarkerColor(ci);
   graph->SetMarkerStyle(25);
   graph->SetMarkerSize(1.5);
   
   TH1F *Graph_Graph27 = new TH1F("Graph_Graph27","Layer 3 Endcap",100,-1.59494,-0.9535416);
   Graph_Graph27->SetMinimum(1.037);
   Graph_Graph27->SetMaximum(38.033);
   Graph_Graph27->SetDirectory(0);
   Graph_Graph27->SetStats(0);
   Graph_Graph27->SetLineStyle(0);
   Graph_Graph27->SetMarkerStyle(20);
   Graph_Graph27->GetXaxis()->SetTitle("#eta");
   Graph_Graph27->GetXaxis()->SetLabelFont(42);
   Graph_Graph27->GetXaxis()->SetLabelOffset(0.007);
   Graph_Graph27->GetXaxis()->SetLabelSize(0.05);
   Graph_Graph27->GetXaxis()->SetTitleSize(0.06);
   Graph_Graph27->GetXaxis()->SetTitleOffset(0.9);
   Graph_Graph27->GetXaxis()->SetTitleFont(42);
   Graph_Graph27->GetYaxis()->SetTitle("RPC single hit rate (Hz/cm^{2})");
   Graph_Graph27->GetYaxis()->SetLabelFont(42);
   Graph_Graph27->GetYaxis()->SetLabelOffset(0.007);
   Graph_Graph27->GetYaxis()->SetLabelSize(0.05);
   Graph_Graph27->GetYaxis()->SetTitleSize(0.06);
   Graph_Graph27->GetYaxis()->SetTitleOffset(1.25);
   Graph_Graph27->GetYaxis()->SetTitleFont(42);
   Graph_Graph27->GetZaxis()->SetLabelFont(42);
   Graph_Graph27->GetZaxis()->SetLabelOffset(0.007);
   Graph_Graph27->GetZaxis()->SetLabelSize(0.05);
   Graph_Graph27->GetZaxis()->SetTitleSize(0.06);
   Graph_Graph27->GetZaxis()->SetTitleFont(42);
   graph->SetHistogram(Graph_Graph27);
   
   multigraph->Add(graph,"AP");
   
   Double_t Graph_fx28[4] = {
   -0.6402547,
   -0.3577033,
   -0.9968613,
   -0.8309316};
   Double_t Graph_fy28[4] = {
   2.29,
   1.65,
   4.7,
   3.71};
   graph = new TGraph(4,Graph_fx28,Graph_fy28);
   graph->SetName("Graph");
   graph->SetTitle("Layer 3 Wheel");
   graph->SetFillStyle(1000);
   graph->SetLineColor(4);
   graph->SetLineWidth(6);

   ci = TColor::GetColor("#ff0000");
   graph->SetMarkerColor(ci);
   graph->SetMarkerStyle(21);
   graph->SetMarkerSize(1.5);
   
   TH1F *Graph_Graph28 = new TH1F("Graph_Graph28","Layer 3 Wheel",100,-1.060777,-0.2937875);
   Graph_Graph28->SetMinimum(1.345);
   Graph_Graph28->SetMaximum(5.005);
   Graph_Graph28->SetDirectory(0);
   Graph_Graph28->SetStats(0);
   Graph_Graph28->SetLineStyle(0);
   Graph_Graph28->SetMarkerStyle(20);
   Graph_Graph28->GetXaxis()->SetTitle("#eta");
   Graph_Graph28->GetXaxis()->SetLabelFont(42);
   Graph_Graph28->GetXaxis()->SetLabelOffset(0.007);
   Graph_Graph28->GetXaxis()->SetLabelSize(0.05);
   Graph_Graph28->GetXaxis()->SetTitleSize(0.06);
   Graph_Graph28->GetXaxis()->SetTitleOffset(0.9);
   Graph_Graph28->GetXaxis()->SetTitleFont(42);
   Graph_Graph28->GetYaxis()->SetTitle("RPC single hit rate (Hz/cm^{2})");
   Graph_Graph28->GetYaxis()->SetLabelFont(42);
   Graph_Graph28->GetYaxis()->SetLabelOffset(0.007);
   Graph_Graph28->GetYaxis()->SetLabelSize(0.05);
   Graph_Graph28->GetYaxis()->SetTitleSize(0.06);
   Graph_Graph28->GetYaxis()->SetTitleOffset(1.25);
   Graph_Graph28->GetYaxis()->SetTitleFont(42);
   Graph_Graph28->GetZaxis()->SetLabelFont(42);
   Graph_Graph28->GetZaxis()->SetLabelOffset(0.007);
   Graph_Graph28->GetZaxis()->SetLabelSize(0.05);
   Graph_Graph28->GetZaxis()->SetTitleSize(0.06);
   Graph_Graph28->GetZaxis()->SetTitleFont(42);
   graph->SetHistogram(Graph_Graph28);
   
   multigraph->Add(graph,"AP");
   
   Double_t Graph_fx29[6] = {
   1.30087,
   1.418788,
   1.54149,
   1.006991,
   1.088097,
   1.186697};
   Double_t Graph_fy29[6] = {
   7.165,
   16.775,
   29.81,
   4.53,
   4.02,
   4.33};
   graph = new TGraph(6,Graph_fx29,Graph_fy29);
   graph->SetName("Graph");
   graph->SetTitle("Layer 4 Endcap");
   graph->SetFillStyle(1000);
   graph->SetLineColor(5);
   graph->SetLineWidth(7);

   ci = TColor::GetColor("#ff0000");
   graph->SetMarkerColor(ci);
   graph->SetMarkerStyle(25);
   graph->SetMarkerSize(1.5);
   
   TH1F *Graph_Graph29 = new TH1F("Graph_Graph29","Layer 4 Endcap",100,0.9535416,1.59494);
   Graph_Graph29->SetMinimum(1.441);
   Graph_Graph29->SetMaximum(32.389);
   Graph_Graph29->SetDirectory(0);
   Graph_Graph29->SetStats(0);
   Graph_Graph29->SetLineStyle(0);
   Graph_Graph29->SetMarkerStyle(20);
   Graph_Graph29->GetXaxis()->SetTitle("#eta");
   Graph_Graph29->GetXaxis()->SetLabelFont(42);
   Graph_Graph29->GetXaxis()->SetLabelOffset(0.007);
   Graph_Graph29->GetXaxis()->SetLabelSize(0.05);
   Graph_Graph29->GetXaxis()->SetTitleSize(0.06);
   Graph_Graph29->GetXaxis()->SetTitleOffset(0.9);
   Graph_Graph29->GetXaxis()->SetTitleFont(42);
   Graph_Graph29->GetYaxis()->SetTitle("RPC single hit rate (Hz/cm^{2})");
   Graph_Graph29->GetYaxis()->SetLabelFont(42);
   Graph_Graph29->GetYaxis()->SetLabelOffset(0.007);
   Graph_Graph29->GetYaxis()->SetLabelSize(0.05);
   Graph_Graph29->GetYaxis()->SetTitleSize(0.06);
   Graph_Graph29->GetYaxis()->SetTitleOffset(1.25);
   Graph_Graph29->GetYaxis()->SetTitleFont(42);
   Graph_Graph29->GetZaxis()->SetLabelFont(42);
   Graph_Graph29->GetZaxis()->SetLabelOffset(0.007);
   Graph_Graph29->GetZaxis()->SetLabelSize(0.05);
   Graph_Graph29->GetZaxis()->SetTitleSize(0.06);
   Graph_Graph29->GetZaxis()->SetTitleFont(42);
   graph->SetHistogram(Graph_Graph29);
   
   multigraph->Add(graph,"AP");
   
   Double_t Graph_fx30[6] = {
   0.1508182,
   -0.1620493,
   0.6307283,
   0.3519274,
   0.984016,
   0.8194372};
   Double_t Graph_fy30[6] = {
   1.16,
   1,
   3.13,
   1.44,
   4.23,
   3.01};
   graph = new TGraph(6,Graph_fx30,Graph_fy30);
   graph->SetName("Graph");
   graph->SetTitle("Layer 4 Wheel");
   graph->SetFillStyle(1000);
   graph->SetLineColor(5);
   graph->SetLineWidth(7);

   ci = TColor::GetColor("#ff0000");
   graph->SetMarkerColor(ci);
   graph->SetMarkerStyle(21);
   graph->SetMarkerSize(1.5);
   
   TH1F *Graph_Graph30 = new TH1F("Graph_Graph30","Layer 4 Wheel",100,-0.2766558,1.098623);
   Graph_Graph30->SetMinimum(0.677);
   Graph_Graph30->SetMaximum(4.553);
   Graph_Graph30->SetDirectory(0);
   Graph_Graph30->SetStats(0);
   Graph_Graph30->SetLineStyle(0);
   Graph_Graph30->SetMarkerStyle(20);
   Graph_Graph30->GetXaxis()->SetTitle("#eta");
   Graph_Graph30->GetXaxis()->SetLabelFont(42);
   Graph_Graph30->GetXaxis()->SetLabelOffset(0.007);
   Graph_Graph30->GetXaxis()->SetLabelSize(0.05);
   Graph_Graph30->GetXaxis()->SetTitleSize(0.06);
   Graph_Graph30->GetXaxis()->SetTitleOffset(0.9);
   Graph_Graph30->GetXaxis()->SetTitleFont(42);
   Graph_Graph30->GetYaxis()->SetTitle("RPC single hit rate (Hz/cm^{2})");
   Graph_Graph30->GetYaxis()->SetLabelFont(42);
   Graph_Graph30->GetYaxis()->SetLabelOffset(0.007);
   Graph_Graph30->GetYaxis()->SetLabelSize(0.05);
   Graph_Graph30->GetYaxis()->SetTitleSize(0.06);
   Graph_Graph30->GetYaxis()->SetTitleOffset(1.25);
   Graph_Graph30->GetYaxis()->SetTitleFont(42);
   Graph_Graph30->GetZaxis()->SetLabelFont(42);
   Graph_Graph30->GetZaxis()->SetLabelOffset(0.007);
   Graph_Graph30->GetZaxis()->SetLabelSize(0.05);
   Graph_Graph30->GetZaxis()->SetTitleSize(0.06);
   Graph_Graph30->GetZaxis()->SetTitleFont(42);
   graph->SetHistogram(Graph_Graph30);
   
   multigraph->Add(graph,"AP");
   
   Double_t Graph_fx31[4] = {
   -0.5647852,
   -0.3653146,
   -0.961078,
   -0.7492043};
   Double_t Graph_fy31[4] = {
   1.81,
   1.31,
   4.33,
   3.37};
   graph = new TGraph(4,Graph_fx31,Graph_fy31);
   graph->SetName("Graph");
   graph->SetTitle("Layer 4 Wheel");
   graph->SetFillStyle(1000);
   graph->SetLineColor(5);
   graph->SetLineWidth(7);

   ci = TColor::GetColor("#0000ff");
   graph->SetMarkerColor(ci);
   graph->SetMarkerStyle(23);
   graph->SetMarkerSize(1.5);
   
   TH1F *Graph_Graph31 = new TH1F("Graph_Graph31","Layer 4 Wheel",100,-1.020654,-0.3057383);
   Graph_Graph31->SetMinimum(1.008);
   Graph_Graph31->SetMaximum(4.632);
   Graph_Graph31->SetDirectory(0);
   Graph_Graph31->SetStats(0);
   Graph_Graph31->SetLineStyle(0);
   Graph_Graph31->SetMarkerStyle(20);
   Graph_Graph31->GetXaxis()->SetTitle("#eta");
   Graph_Graph31->GetXaxis()->SetLabelFont(42);
   Graph_Graph31->GetXaxis()->SetLabelOffset(0.007);
   Graph_Graph31->GetXaxis()->SetLabelSize(0.05);
   Graph_Graph31->GetXaxis()->SetTitleSize(0.06);
   Graph_Graph31->GetXaxis()->SetTitleOffset(0.9);
   Graph_Graph31->GetXaxis()->SetTitleFont(42);
   Graph_Graph31->GetYaxis()->SetTitle("RPC single hit rate (Hz/cm^{2})");
   Graph_Graph31->GetYaxis()->SetLabelFont(42);
   Graph_Graph31->GetYaxis()->SetLabelOffset(0.007);
   Graph_Graph31->GetYaxis()->SetLabelSize(0.05);
   Graph_Graph31->GetYaxis()->SetTitleSize(0.06);
   Graph_Graph31->GetYaxis()->SetTitleOffset(1.25);
   Graph_Graph31->GetYaxis()->SetTitleFont(42);
   Graph_Graph31->GetZaxis()->SetLabelFont(42);
   Graph_Graph31->GetZaxis()->SetLabelOffset(0.007);
   Graph_Graph31->GetZaxis()->SetLabelSize(0.05);
   Graph_Graph31->GetZaxis()->SetTitleSize(0.06);
   Graph_Graph31->GetZaxis()->SetTitleFont(42);
   graph->SetHistogram(Graph_Graph31);
   
   multigraph->Add(graph,"AP");
   
   Double_t Graph_fx32[6] = {
   0.1070081,
   -0.1177723,
   0.5727437,
   0.3707642,
   0.9726389,
   0.759068};
   Double_t Graph_fy32[6] = {
   0.99,
   1.15,
   2.05,
   1.43,
   3.51,
   3.57};
   graph = new TGraph(6,Graph_fx32,Graph_fy32);
   graph->SetName("Graph");
   graph->SetTitle("Layer 4 Wheel");
   graph->SetFillStyle(1000);
   graph->SetLineColor(5);
   graph->SetLineWidth(7);

   ci = TColor::GetColor("#0000ff");
   graph->SetMarkerColor(ci);
   graph->SetMarkerStyle(23);
   graph->SetMarkerSize(1.5);
   
   TH1F *Graph_Graph32 = new TH1F("Graph_Graph32","Layer 4 Wheel",100,-0.2268135,1.08168);
   Graph_Graph32->SetMinimum(0.732);
   Graph_Graph32->SetMaximum(3.828);
   Graph_Graph32->SetDirectory(0);
   Graph_Graph32->SetStats(0);
   Graph_Graph32->SetLineStyle(0);
   Graph_Graph32->SetMarkerStyle(20);
   Graph_Graph32->GetXaxis()->SetTitle("#eta");
   Graph_Graph32->GetXaxis()->SetLabelFont(42);
   Graph_Graph32->GetXaxis()->SetLabelOffset(0.007);
   Graph_Graph32->GetXaxis()->SetLabelSize(0.05);
   Graph_Graph32->GetXaxis()->SetTitleSize(0.06);
   Graph_Graph32->GetXaxis()->SetTitleOffset(0.9);
   Graph_Graph32->GetXaxis()->SetTitleFont(42);
   Graph_Graph32->GetYaxis()->SetTitle("RPC single hit rate (Hz/cm^{2})");
   Graph_Graph32->GetYaxis()->SetLabelFont(42);
   Graph_Graph32->GetYaxis()->SetLabelOffset(0.007);
   Graph_Graph32->GetYaxis()->SetLabelSize(0.05);
   Graph_Graph32->GetYaxis()->SetTitleSize(0.06);
   Graph_Graph32->GetYaxis()->SetTitleOffset(1.25);
   Graph_Graph32->GetYaxis()->SetTitleFont(42);
   Graph_Graph32->GetZaxis()->SetLabelFont(42);
   Graph_Graph32->GetZaxis()->SetLabelOffset(0.007);
   Graph_Graph32->GetZaxis()->SetLabelSize(0.05);
   Graph_Graph32->GetZaxis()->SetTitleSize(0.06);
   Graph_Graph32->GetZaxis()->SetTitleFont(42);
   graph->SetHistogram(Graph_Graph32);
   
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

   ci = TColor::GetColor("#ff0000");
   entry->SetMarkerColor(ci);
   entry->SetMarkerStyle(25);
   entry->SetMarkerSize(1.5);
   entry->SetTextFont(62);
   entry=leg->AddEntry("Graph","RB2in","p");
   entry->SetLineColor(1);
   entry->SetLineStyle(1);
   entry->SetLineWidth(1);

   ci = TColor::GetColor("#ff0000");
   entry->SetMarkerColor(ci);
   entry->SetMarkerStyle(21);
   entry->SetMarkerSize(1.5);
   entry->SetTextFont(62);
   entry=leg->AddEntry("Graph","RB2out","p");
   entry->SetLineColor(1);
   entry->SetLineStyle(1);
   entry->SetLineWidth(1);

   ci = TColor::GetColor("#0000ff");
   entry->SetMarkerColor(ci);
   entry->SetMarkerStyle(23);
   entry->SetMarkerSize(1.5);
   entry->SetTextFont(62);
   leg->Draw();
   c1->Modified();
   c1->cd();
   c1->SetSelected(c1);
}
