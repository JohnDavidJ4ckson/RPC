void etaDistroDetailRB1()
{
//=========Macro generated from canvas: c1/Canvas
//=========  (Fri Jan 18 17:33:32 2019) by ROOT version 6.12/04
   TCanvas *c1 = new TCanvas("c1", "Canvas",50,45,800,775);
   gStyle->SetOptFit(1);
   gStyle->SetOptStat(0);
   gStyle->SetOptTitle(0);
   c1->SetHighLightColor(2);
   c1->Range(-2.194995,-0.3140046,1.851362,3.211532);
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
   
   Double_t Graph_fx21[6] = {
   -1.269543,
   -1.38083,
   -1.554935,
   -0.9430065,
   -1.01269,
   -1.104428};
   Double_t Graph_fy21[6] = {
   4.93,
   7.92,
   14.07,
   2.11,
   1.595,
   1.975};
   TGraph *graph = new TGraph(6,Graph_fx21,Graph_fy21);
   graph->SetName("Graph");
   graph->SetTitle("Layer 1 Endcap");
   graph->SetFillStyle(1000);
   graph->SetLineColor(2);
   graph->SetLineWidth(4);

   Int_t ci;      // for color index setting
   TColor *color; // for color definition with alpha
   ci = TColor::GetColor("#ff0000");
   graph->SetMarkerColor(ci);
   graph->SetMarkerStyle(24);
   graph->SetMarkerSize(1.5);
   
   TH1F *Graph_Graph_Graph121 = new TH1F("Graph_Graph_Graph121","Layer 1 Endcap",100,-1.616128,-0.8818137);
   Graph_Graph_Graph121->SetMinimum(0.3475);
   Graph_Graph_Graph121->SetMaximum(15.3175);
   Graph_Graph_Graph121->SetDirectory(0);
   Graph_Graph_Graph121->SetStats(0);
   Graph_Graph_Graph121->SetLineStyle(0);
   Graph_Graph_Graph121->SetMarkerStyle(20);
   Graph_Graph_Graph121->GetXaxis()->SetTitle("#eta");
   Graph_Graph_Graph121->GetXaxis()->SetLabelFont(42);
   Graph_Graph_Graph121->GetXaxis()->SetLabelOffset(0.007);
   Graph_Graph_Graph121->GetXaxis()->SetLabelSize(0.05);
   Graph_Graph_Graph121->GetXaxis()->SetTitleSize(0.06);
   Graph_Graph_Graph121->GetXaxis()->SetTitleOffset(0.9);
   Graph_Graph_Graph121->GetXaxis()->SetTitleFont(42);
   Graph_Graph_Graph121->GetYaxis()->SetTitle("RPC single hit rate (Hz/cm^{2})");
   Graph_Graph_Graph121->GetYaxis()->SetLabelFont(42);
   Graph_Graph_Graph121->GetYaxis()->SetLabelOffset(0.007);
   Graph_Graph_Graph121->GetYaxis()->SetLabelSize(0.05);
   Graph_Graph_Graph121->GetYaxis()->SetTitleSize(0.06);
   Graph_Graph_Graph121->GetYaxis()->SetTitleOffset(1.25);
   Graph_Graph_Graph121->GetYaxis()->SetTitleFont(42);
   Graph_Graph_Graph121->GetZaxis()->SetLabelFont(42);
   Graph_Graph_Graph121->GetZaxis()->SetLabelOffset(0.007);
   Graph_Graph_Graph121->GetZaxis()->SetLabelSize(0.05);
   Graph_Graph_Graph121->GetZaxis()->SetTitleSize(0.06);
   Graph_Graph_Graph121->GetZaxis()->SetTitleFont(42);
   graph->SetHistogram(Graph_Graph_Graph121);
   
   multigraph->Add(graph,"AP");
   
   Double_t Graph_fx22[4] = {
   -0.6914756,
   -0.4535393,
   -1.112329,
   -0.9352334};
   Double_t Graph_fy22[4] = {
   11.21,
   7.22,
   17.11,
   15.98};
   graph = new TGraph(4,Graph_fx22,Graph_fy22);
   graph->SetName("Graph");
   graph->SetTitle("RB1 in");
   graph->SetFillStyle(1000);

   ci = TColor::GetColor("#ff0000");
   graph->SetMarkerColor(ci);
   graph->SetMarkerStyle(20);
   graph->SetMarkerSize(1.5);
   
   TH1F *Graph_Graph_Graph222 = new TH1F("Graph_Graph_Graph222","RB1 in",100,-1.178207,-0.3876603);
   Graph_Graph_Graph222->SetMinimum(6.231);
   Graph_Graph_Graph222->SetMaximum(18.099);
   Graph_Graph_Graph222->SetDirectory(0);
   Graph_Graph_Graph222->SetStats(0);
   Graph_Graph_Graph222->SetLineStyle(0);
   Graph_Graph_Graph222->SetMarkerStyle(20);
   Graph_Graph_Graph222->GetXaxis()->SetTitle("#eta");
   Graph_Graph_Graph222->GetXaxis()->SetLabelFont(42);
   Graph_Graph_Graph222->GetXaxis()->SetLabelOffset(0.007);
   Graph_Graph_Graph222->GetXaxis()->SetLabelSize(0.05);
   Graph_Graph_Graph222->GetXaxis()->SetTitleSize(0.06);
   Graph_Graph_Graph222->GetXaxis()->SetTitleOffset(0.9);
   Graph_Graph_Graph222->GetXaxis()->SetTitleFont(42);
   Graph_Graph_Graph222->GetYaxis()->SetTitle("RPC single hit rate (Hz/cm^{2})");
   Graph_Graph_Graph222->GetYaxis()->SetLabelFont(42);
   Graph_Graph_Graph222->GetYaxis()->SetLabelOffset(0.007);
   Graph_Graph_Graph222->GetYaxis()->SetLabelSize(0.05);
   Graph_Graph_Graph222->GetYaxis()->SetTitleSize(0.06);
   Graph_Graph_Graph222->GetYaxis()->SetTitleOffset(1.25);
   Graph_Graph_Graph222->GetYaxis()->SetTitleFont(42);
   Graph_Graph_Graph222->GetZaxis()->SetLabelFont(42);
   Graph_Graph_Graph222->GetZaxis()->SetLabelOffset(0.007);
   Graph_Graph_Graph222->GetZaxis()->SetLabelSize(0.05);
   Graph_Graph_Graph222->GetZaxis()->SetTitleSize(0.06);
   Graph_Graph_Graph222->GetZaxis()->SetTitleFont(42);
   graph->SetHistogram(Graph_Graph_Graph222);
   
   multigraph->Add(graph,"AP");
   
   Double_t Graph_fx23[6] = {
   1.25092,
   1.36161,
   1.53501,
   0.940752,
   1.01269,
   1.104428};
   Double_t Graph_fy23[6] = {
   5.01,
   8.4,
   13.75,
   2.865,
   1.9,
   2.115};
   graph = new TGraph(6,Graph_fx23,Graph_fy23);
   graph->SetName("Graph");
   graph->SetTitle("Layer 3 Endcap");
   graph->SetFillStyle(1000);
   graph->SetLineColor(4);
   graph->SetLineWidth(6);

   ci = TColor::GetColor("#ff0000");
   graph->SetMarkerColor(ci);
   graph->SetMarkerStyle(24);
   graph->SetMarkerSize(1.5);
   
   TH1F *Graph_Graph_Graph323 = new TH1F("Graph_Graph_Graph323","Layer 3 Endcap",100,0.8813262,1.594436);
   Graph_Graph_Graph323->SetMinimum(0.715);
   Graph_Graph_Graph323->SetMaximum(14.935);
   Graph_Graph_Graph323->SetDirectory(0);
   Graph_Graph_Graph323->SetStats(0);
   Graph_Graph_Graph323->SetLineStyle(0);
   Graph_Graph_Graph323->SetMarkerStyle(20);
   Graph_Graph_Graph323->GetXaxis()->SetTitle("#eta");
   Graph_Graph_Graph323->GetXaxis()->SetLabelFont(42);
   Graph_Graph_Graph323->GetXaxis()->SetLabelOffset(0.007);
   Graph_Graph_Graph323->GetXaxis()->SetLabelSize(0.05);
   Graph_Graph_Graph323->GetXaxis()->SetTitleSize(0.06);
   Graph_Graph_Graph323->GetXaxis()->SetTitleOffset(0.9);
   Graph_Graph_Graph323->GetXaxis()->SetTitleFont(42);
   Graph_Graph_Graph323->GetYaxis()->SetTitle("RPC single hit rate (Hz/cm^{2})");
   Graph_Graph_Graph323->GetYaxis()->SetLabelFont(42);
   Graph_Graph_Graph323->GetYaxis()->SetLabelOffset(0.007);
   Graph_Graph_Graph323->GetYaxis()->SetLabelSize(0.05);
   Graph_Graph_Graph323->GetYaxis()->SetTitleSize(0.06);
   Graph_Graph_Graph323->GetYaxis()->SetTitleOffset(1.25);
   Graph_Graph_Graph323->GetYaxis()->SetTitleFont(42);
   Graph_Graph_Graph323->GetZaxis()->SetLabelFont(42);
   Graph_Graph_Graph323->GetZaxis()->SetLabelOffset(0.007);
   Graph_Graph_Graph323->GetZaxis()->SetLabelSize(0.05);
   Graph_Graph_Graph323->GetZaxis()->SetTitleSize(0.06);
   Graph_Graph_Graph323->GetZaxis()->SetTitleFont(42);
   graph->SetHistogram(Graph_Graph_Graph323);
   
   multigraph->Add(graph,"AP");
   
   Double_t Graph_fx24[6] = {
   0.1378691,
   -0.1516978,
   0.7169072,
   0.4716459,
   1.146298,
   0.966242};
   Double_t Graph_fy24[6] = {
   3.14,
   2.8,
   11.12,
   5.88,
   23.37,
   22.4};
   graph = new TGraph(6,Graph_fx24,Graph_fy24);
   graph->SetName("Graph");
   graph->SetTitle("Layer 3 Wheel");
   graph->SetFillStyle(1000);
   graph->SetLineColor(4);
   graph->SetLineWidth(6);

   ci = TColor::GetColor("#ff0000");
   graph->SetMarkerColor(ci);
   graph->SetMarkerStyle(20);
   graph->SetMarkerSize(1.5);
   
   TH1F *Graph_Graph_Graph424 = new TH1F("Graph_Graph_Graph424","Layer 3 Wheel",100,-0.2814974,1.276098);
   Graph_Graph_Graph424->SetMinimum(0.743);
   Graph_Graph_Graph424->SetMaximum(25.427);
   Graph_Graph_Graph424->SetDirectory(0);
   Graph_Graph_Graph424->SetStats(0);
   Graph_Graph_Graph424->SetLineStyle(0);
   Graph_Graph_Graph424->SetMarkerStyle(20);
   Graph_Graph_Graph424->GetXaxis()->SetTitle("#eta");
   Graph_Graph_Graph424->GetXaxis()->SetLabelFont(42);
   Graph_Graph_Graph424->GetXaxis()->SetLabelOffset(0.007);
   Graph_Graph_Graph424->GetXaxis()->SetLabelSize(0.05);
   Graph_Graph_Graph424->GetXaxis()->SetTitleSize(0.06);
   Graph_Graph_Graph424->GetXaxis()->SetTitleOffset(0.9);
   Graph_Graph_Graph424->GetXaxis()->SetTitleFont(42);
   Graph_Graph_Graph424->GetYaxis()->SetTitle("RPC single hit rate (Hz/cm^{2})");
   Graph_Graph_Graph424->GetYaxis()->SetLabelFont(42);
   Graph_Graph_Graph424->GetYaxis()->SetLabelOffset(0.007);
   Graph_Graph_Graph424->GetYaxis()->SetLabelSize(0.05);
   Graph_Graph_Graph424->GetYaxis()->SetTitleSize(0.06);
   Graph_Graph_Graph424->GetYaxis()->SetTitleOffset(1.25);
   Graph_Graph_Graph424->GetYaxis()->SetTitleFont(42);
   Graph_Graph_Graph424->GetZaxis()->SetLabelFont(42);
   Graph_Graph_Graph424->GetZaxis()->SetLabelOffset(0.007);
   Graph_Graph_Graph424->GetZaxis()->SetLabelSize(0.05);
   Graph_Graph_Graph424->GetZaxis()->SetTitleSize(0.06);
   Graph_Graph_Graph424->GetZaxis()->SetTitleFont(42);
   graph->SetHistogram(Graph_Graph_Graph424);
   
   multigraph->Add(graph,"AP");
   
   Double_t Graph_fx25[4] = {
   -0.6684232,
   -0.4372446,
   -1.081175,
   -0.9069221};
   Double_t Graph_fy25[4] = {
   8.42,
   6.03,
   12.68,
   12.44};
   graph = new TGraph(4,Graph_fx25,Graph_fy25);
   graph->SetName("Graph");
   graph->SetTitle("Layer 1 Wheel");
   graph->SetFillStyle(1000);
   graph->SetLineColor(2);
   graph->SetLineWidth(4);

   ci = TColor::GetColor("#0000ff");
   graph->SetMarkerColor(ci);
   graph->SetMarkerStyle(29);
   graph->SetMarkerSize(1.7);
   
   TH1F *Graph_Graph_Graph625 = new TH1F("Graph_Graph_Graph625","Layer 1 Wheel",100,-1.145568,-0.3728516);
   Graph_Graph_Graph625->SetMinimum(5.365);
   Graph_Graph_Graph625->SetMaximum(13.345);
   Graph_Graph_Graph625->SetDirectory(0);
   Graph_Graph_Graph625->SetStats(0);
   Graph_Graph_Graph625->SetLineStyle(0);
   Graph_Graph_Graph625->SetMarkerStyle(20);
   Graph_Graph_Graph625->GetXaxis()->SetTitle("#eta");
   Graph_Graph_Graph625->GetXaxis()->SetLabelFont(42);
   Graph_Graph_Graph625->GetXaxis()->SetLabelOffset(0.007);
   Graph_Graph_Graph625->GetXaxis()->SetLabelSize(0.05);
   Graph_Graph_Graph625->GetXaxis()->SetTitleSize(0.06);
   Graph_Graph_Graph625->GetXaxis()->SetTitleOffset(0.9);
   Graph_Graph_Graph625->GetXaxis()->SetTitleFont(42);
   Graph_Graph_Graph625->GetYaxis()->SetTitle("RPC single hit rate (Hz/cm^{2})");
   Graph_Graph_Graph625->GetYaxis()->SetLabelFont(42);
   Graph_Graph_Graph625->GetYaxis()->SetLabelOffset(0.007);
   Graph_Graph_Graph625->GetYaxis()->SetLabelSize(0.05);
   Graph_Graph_Graph625->GetYaxis()->SetTitleSize(0.06);
   Graph_Graph_Graph625->GetYaxis()->SetTitleOffset(1.25);
   Graph_Graph_Graph625->GetYaxis()->SetTitleFont(42);
   Graph_Graph_Graph625->GetZaxis()->SetLabelFont(42);
   Graph_Graph_Graph625->GetZaxis()->SetLabelOffset(0.007);
   Graph_Graph_Graph625->GetZaxis()->SetLabelSize(0.05);
   Graph_Graph_Graph625->GetZaxis()->SetTitleSize(0.06);
   Graph_Graph_Graph625->GetZaxis()->SetTitleFont(42);
   graph->SetHistogram(Graph_Graph_Graph625);
   
   multigraph->Add(graph,"AP");
   
   Double_t Graph_fx26[6] = {
   0.1232712,
   -0.1356536,
   0.6501188,
   0.4243846,
   1.056183,
   0.8843007};
   Double_t Graph_fy26[6] = {
   3.05,
   2.89,
   7.54,
   5.77,
   14.6,
   13.21};
   graph = new TGraph(6,Graph_fx26,Graph_fy26);
   graph->SetName("Graph");
   graph->SetTitle("Layer 4 Wheel");
   graph->SetFillStyle(1000);
   graph->SetLineColor(5);
   graph->SetLineWidth(7);

   ci = TColor::GetColor("#0000ff");
   graph->SetMarkerColor(ci);
   graph->SetMarkerStyle(29);
   graph->SetMarkerSize(1.5);
   
   TH1F *Graph_Graph_Graph826 = new TH1F("Graph_Graph_Graph826","Layer 4 Wheel",100,-0.2548373,1.175367);
   Graph_Graph_Graph826->SetMinimum(1.719);
   Graph_Graph_Graph826->SetMaximum(15.771);
   Graph_Graph_Graph826->SetDirectory(0);
   Graph_Graph_Graph826->SetStats(0);
   Graph_Graph_Graph826->SetLineStyle(0);
   Graph_Graph_Graph826->SetMarkerStyle(20);
   Graph_Graph_Graph826->GetXaxis()->SetTitle("#eta");
   Graph_Graph_Graph826->GetXaxis()->SetLabelFont(42);
   Graph_Graph_Graph826->GetXaxis()->SetLabelOffset(0.007);
   Graph_Graph_Graph826->GetXaxis()->SetLabelSize(0.05);
   Graph_Graph_Graph826->GetXaxis()->SetTitleSize(0.06);
   Graph_Graph_Graph826->GetXaxis()->SetTitleOffset(0.9);
   Graph_Graph_Graph826->GetXaxis()->SetTitleFont(42);
   Graph_Graph_Graph826->GetYaxis()->SetTitle("RPC single hit rate (Hz/cm^{2})");
   Graph_Graph_Graph826->GetYaxis()->SetLabelFont(42);
   Graph_Graph_Graph826->GetYaxis()->SetLabelOffset(0.007);
   Graph_Graph_Graph826->GetYaxis()->SetLabelSize(0.05);
   Graph_Graph_Graph826->GetYaxis()->SetTitleSize(0.06);
   Graph_Graph_Graph826->GetYaxis()->SetTitleOffset(1.25);
   Graph_Graph_Graph826->GetYaxis()->SetTitleFont(42);
   Graph_Graph_Graph826->GetZaxis()->SetLabelFont(42);
   Graph_Graph_Graph826->GetZaxis()->SetLabelOffset(0.007);
   Graph_Graph_Graph826->GetZaxis()->SetLabelSize(0.05);
   Graph_Graph_Graph826->GetZaxis()->SetTitleSize(0.06);
   Graph_Graph_Graph826->GetZaxis()->SetTitleFont(42);
   graph->SetHistogram(Graph_Graph_Graph826);
   
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

   ci = TColor::GetColor("#ff0000");
   entry->SetMarkerColor(ci);
   entry->SetMarkerStyle(24);
   entry->SetMarkerSize(1.5);
   entry->SetTextFont(62);
   entry=leg->AddEntry("Graph","RB1in","p");
   entry->SetLineColor(1);
   entry->SetLineStyle(1);
   entry->SetLineWidth(1);

   ci = TColor::GetColor("#ff0000");
   entry->SetMarkerColor(ci);
   entry->SetMarkerStyle(20);
   entry->SetMarkerSize(1.5);
   entry->SetTextFont(62);
   entry=leg->AddEntry("Graph","RB1out","p");
   entry->SetLineColor(1);
   entry->SetLineStyle(1);
   entry->SetLineWidth(1);

   ci = TColor::GetColor("#0000ff");
   entry->SetMarkerColor(ci);
   entry->SetMarkerStyle(29);
   entry->SetMarkerSize(1.7);
   entry->SetTextFont(62);
   leg->Draw();
   c1->Modified();
   c1->cd();
   c1->SetSelected(c1);
}
