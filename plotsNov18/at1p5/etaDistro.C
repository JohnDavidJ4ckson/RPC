void etaDistro()
{
//=========Macro generated from canvas: c1/Canvas
//=========  (Tue Jan 22 21:57:04 2019) by ROOT version 6.12/04
   TCanvas *c1 = new TCanvas("c1", "Canvas",0,45,1440,775);
   gStyle->SetOptFit(1);
   gStyle->SetOptStat(0);
   gStyle->SetOptTitle(0);
   c1->SetHighLightColor(2);
   c1->Range(0,0,1,1);
   c1->SetFillColor(0);
   c1->SetBorderMode(0);
   c1->SetBorderSize(2);
   c1->SetLeftMargin(0.06);
   c1->SetRightMargin(0.02);
   c1->SetTopMargin(0.06);
   c1->SetFrameFillStyle(0);
   c1->SetFrameBorderMode(0);
  
// ------------>Primitives in pad: c1_1
   TPad *c1_1 = new TPad("c1_1", "c1_1",0.001,0.501,0.3323333,0.999);
   c1_1->Draw();
   c1_1->cd();
   c1_1->Range(-2.37264,-0.4717938,1.772408,3.182726);
   c1_1->SetFillColor(0);
   c1_1->SetBorderMode(0);
   c1_1->SetBorderSize(2);
   c1_1->SetLogy();
   c1_1->SetTickx(1);
   c1_1->SetTicky(1);
   c1_1->SetLeftMargin(0.16);
   c1_1->SetRightMargin(0.02);
   c1_1->SetTopMargin(0.05);
   c1_1->SetBottomMargin(0.13);
   c1_1->SetFrameFillStyle(0);
   c1_1->SetFrameBorderMode(0);
   c1_1->SetFrameFillStyle(0);
   c1_1->SetFrameBorderMode(0);
   
   TMultiGraph *multigraph = new TMultiGraph();
   multigraph->SetName("");
   multigraph->SetTitle("RB1in");
   
   Double_t Graph_fx1[6] = {
   -1.269543,
   -1.38083,
   -1.554935,
   -0.9430065,
   -1.01269,
   -1.104428};
   Double_t Graph_fy1[6] = {
   4.93,
   7.92,
   14.07,
   2.11,
   1.595,
   1.975};
   TGraph *graph = new TGraph(6,Graph_fx1,Graph_fy1);
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
   
   TH1F *Graph_Graph1 = new TH1F("Graph_Graph1","Layer 1 Endcap",100,-1.616128,-0.8818137);
   Graph_Graph1->SetMinimum(0.3475);
   Graph_Graph1->SetMaximum(15.3175);
   Graph_Graph1->SetDirectory(0);
   Graph_Graph1->SetStats(0);
   Graph_Graph1->SetLineStyle(0);
   Graph_Graph1->SetMarkerStyle(20);
   Graph_Graph1->GetXaxis()->SetTitle("#eta");
   Graph_Graph1->GetXaxis()->SetLabelFont(42);
   Graph_Graph1->GetXaxis()->SetLabelOffset(0.007);
   Graph_Graph1->GetXaxis()->SetLabelSize(0.05);
   Graph_Graph1->GetXaxis()->SetTitleSize(0.06);
   Graph_Graph1->GetXaxis()->SetTitleOffset(0.9);
   Graph_Graph1->GetXaxis()->SetTitleFont(42);
   Graph_Graph1->GetYaxis()->SetTitle("RPC single hit rate (Hz/cm^{2})");
   Graph_Graph1->GetYaxis()->SetLabelFont(42);
   Graph_Graph1->GetYaxis()->SetLabelOffset(0.007);
   Graph_Graph1->GetYaxis()->SetLabelSize(0.05);
   Graph_Graph1->GetYaxis()->SetTitleSize(0.06);
   Graph_Graph1->GetYaxis()->SetTitleOffset(1.25);
   Graph_Graph1->GetYaxis()->SetTitleFont(42);
   Graph_Graph1->GetZaxis()->SetLabelFont(42);
   Graph_Graph1->GetZaxis()->SetLabelOffset(0.007);
   Graph_Graph1->GetZaxis()->SetLabelSize(0.05);
   Graph_Graph1->GetZaxis()->SetTitleSize(0.06);
   Graph_Graph1->GetZaxis()->SetTitleFont(42);
   graph->SetHistogram(Graph_Graph1);
   
   multigraph->Add(graph,"AP");
   
   Double_t Graph_fx2[4] = {
   -0.6914756,
   -0.4535393,
   -1.112329,
   -0.9352334};
   Double_t Graph_fy2[4] = {
   11.21,
   7.22,
   17.11,
   15.98};
   graph = new TGraph(4,Graph_fx2,Graph_fy2);
   graph->SetName("Graph");
   graph->SetTitle("RB1 in");
   graph->SetFillStyle(1000);

   ci = TColor::GetColor("#ff0000");
   graph->SetMarkerColor(ci);
   graph->SetMarkerStyle(20);
   graph->SetMarkerSize(1.5);
   
   TH1F *Graph_Graph2 = new TH1F("Graph_Graph2","RB1 in",100,-1.178207,-0.3876603);
   Graph_Graph2->SetMinimum(6.231);
   Graph_Graph2->SetMaximum(18.099);
   Graph_Graph2->SetDirectory(0);
   Graph_Graph2->SetStats(0);
   Graph_Graph2->SetLineStyle(0);
   Graph_Graph2->SetMarkerStyle(20);
   Graph_Graph2->GetXaxis()->SetTitle("#eta");
   Graph_Graph2->GetXaxis()->SetLabelFont(42);
   Graph_Graph2->GetXaxis()->SetLabelOffset(0.007);
   Graph_Graph2->GetXaxis()->SetLabelSize(0.05);
   Graph_Graph2->GetXaxis()->SetTitleSize(0.06);
   Graph_Graph2->GetXaxis()->SetTitleOffset(0.9);
   Graph_Graph2->GetXaxis()->SetTitleFont(42);
   Graph_Graph2->GetYaxis()->SetTitle("RPC single hit rate (Hz/cm^{2})");
   Graph_Graph2->GetYaxis()->SetLabelFont(42);
   Graph_Graph2->GetYaxis()->SetLabelOffset(0.007);
   Graph_Graph2->GetYaxis()->SetLabelSize(0.05);
   Graph_Graph2->GetYaxis()->SetTitleSize(0.06);
   Graph_Graph2->GetYaxis()->SetTitleOffset(1.25);
   Graph_Graph2->GetYaxis()->SetTitleFont(42);
   Graph_Graph2->GetZaxis()->SetLabelFont(42);
   Graph_Graph2->GetZaxis()->SetLabelOffset(0.007);
   Graph_Graph2->GetZaxis()->SetLabelSize(0.05);
   Graph_Graph2->GetZaxis()->SetTitleSize(0.06);
   Graph_Graph2->GetZaxis()->SetTitleFont(42);
   graph->SetHistogram(Graph_Graph2);
   
   multigraph->Add(graph,"AP");
   
   Double_t Graph_fx3[6] = {
   1.25092,
   1.36161,
   1.53501,
   0.940752,
   1.01269,
   1.104428};
   Double_t Graph_fy3[6] = {
   5.01,
   8.4,
   13.75,
   2.865,
   1.9,
   2.115};
   graph = new TGraph(6,Graph_fx3,Graph_fy3);
   graph->SetName("Graph");
   graph->SetTitle("Layer 3 Endcap");
   graph->SetFillStyle(1000);
   graph->SetLineColor(4);
   graph->SetLineWidth(6);

   ci = TColor::GetColor("#ff0000");
   graph->SetMarkerColor(ci);
   graph->SetMarkerStyle(24);
   graph->SetMarkerSize(1.5);
   
   TH1F *Graph_Graph3 = new TH1F("Graph_Graph3","Layer 3 Endcap",100,0.8813262,1.594436);
   Graph_Graph3->SetMinimum(0.715);
   Graph_Graph3->SetMaximum(14.935);
   Graph_Graph3->SetDirectory(0);
   Graph_Graph3->SetStats(0);
   Graph_Graph3->SetLineStyle(0);
   Graph_Graph3->SetMarkerStyle(20);
   Graph_Graph3->GetXaxis()->SetTitle("#eta");
   Graph_Graph3->GetXaxis()->SetLabelFont(42);
   Graph_Graph3->GetXaxis()->SetLabelOffset(0.007);
   Graph_Graph3->GetXaxis()->SetLabelSize(0.05);
   Graph_Graph3->GetXaxis()->SetTitleSize(0.06);
   Graph_Graph3->GetXaxis()->SetTitleOffset(0.9);
   Graph_Graph3->GetXaxis()->SetTitleFont(42);
   Graph_Graph3->GetYaxis()->SetTitle("RPC single hit rate (Hz/cm^{2})");
   Graph_Graph3->GetYaxis()->SetLabelFont(42);
   Graph_Graph3->GetYaxis()->SetLabelOffset(0.007);
   Graph_Graph3->GetYaxis()->SetLabelSize(0.05);
   Graph_Graph3->GetYaxis()->SetTitleSize(0.06);
   Graph_Graph3->GetYaxis()->SetTitleOffset(1.25);
   Graph_Graph3->GetYaxis()->SetTitleFont(42);
   Graph_Graph3->GetZaxis()->SetLabelFont(42);
   Graph_Graph3->GetZaxis()->SetLabelOffset(0.007);
   Graph_Graph3->GetZaxis()->SetLabelSize(0.05);
   Graph_Graph3->GetZaxis()->SetTitleSize(0.06);
   Graph_Graph3->GetZaxis()->SetTitleFont(42);
   graph->SetHistogram(Graph_Graph3);
   
   multigraph->Add(graph,"AP");
   
   Double_t Graph_fx4[6] = {
   0.1378691,
   -0.1516978,
   0.7169072,
   0.4716459,
   1.146298,
   0.966242};
   Double_t Graph_fy4[6] = {
   3.14,
   2.8,
   11.12,
   5.88,
   23.37,
   22.4};
   graph = new TGraph(6,Graph_fx4,Graph_fy4);
   graph->SetName("Graph");
   graph->SetTitle("Layer 3 Wheel");
   graph->SetFillStyle(1000);
   graph->SetLineColor(4);
   graph->SetLineWidth(6);

   ci = TColor::GetColor("#ff0000");
   graph->SetMarkerColor(ci);
   graph->SetMarkerStyle(20);
   graph->SetMarkerSize(1.5);
   
   TH1F *Graph_Graph4 = new TH1F("Graph_Graph4","Layer 3 Wheel",100,-0.2814974,1.276098);
   Graph_Graph4->SetMinimum(0.743);
   Graph_Graph4->SetMaximum(25.427);
   Graph_Graph4->SetDirectory(0);
   Graph_Graph4->SetStats(0);
   Graph_Graph4->SetLineStyle(0);
   Graph_Graph4->SetMarkerStyle(20);
   Graph_Graph4->GetXaxis()->SetTitle("#eta");
   Graph_Graph4->GetXaxis()->SetLabelFont(42);
   Graph_Graph4->GetXaxis()->SetLabelOffset(0.007);
   Graph_Graph4->GetXaxis()->SetLabelSize(0.05);
   Graph_Graph4->GetXaxis()->SetTitleSize(0.06);
   Graph_Graph4->GetXaxis()->SetTitleOffset(0.9);
   Graph_Graph4->GetXaxis()->SetTitleFont(42);
   Graph_Graph4->GetYaxis()->SetTitle("RPC single hit rate (Hz/cm^{2})");
   Graph_Graph4->GetYaxis()->SetLabelFont(42);
   Graph_Graph4->GetYaxis()->SetLabelOffset(0.007);
   Graph_Graph4->GetYaxis()->SetLabelSize(0.05);
   Graph_Graph4->GetYaxis()->SetTitleSize(0.06);
   Graph_Graph4->GetYaxis()->SetTitleOffset(1.25);
   Graph_Graph4->GetYaxis()->SetTitleFont(42);
   Graph_Graph4->GetZaxis()->SetLabelFont(42);
   Graph_Graph4->GetZaxis()->SetLabelOffset(0.007);
   Graph_Graph4->GetZaxis()->SetLabelSize(0.05);
   Graph_Graph4->GetZaxis()->SetTitleSize(0.06);
   Graph_Graph4->GetZaxis()->SetTitleFont(42);
   graph->SetHistogram(Graph_Graph4);
   
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
   c1_1->Modified();
   c1->cd();
  
// ------------>Primitives in pad: c1_2
   TPad *c1_2 = new TPad("c1_2", "c1_2",0.3343333,0.501,0.6656667,0.999);
   c1_2->Draw();
   c1_2->cd();
   c1_2->Range(0,0,1,1);
   c1_2->SetFillColor(0);
   c1_2->SetBorderMode(0);
   c1_2->SetBorderSize(2);
   c1_2->SetLogy();
   c1_2->SetTickx(1);
   c1_2->SetTicky(1);
   c1_2->SetLeftMargin(0.16);
   c1_2->SetRightMargin(0.02);
   c1_2->SetTopMargin(0.05);
   c1_2->SetBottomMargin(0.13);
   c1_2->SetFrameFillStyle(0);
   c1_2->SetFrameBorderMode(0);
   
   TLegend *leg = new TLegend(0.2,0.7,0.8,0.9,NULL,"brNDC");
   leg->SetTextFont(62);
   leg->SetLineColor(1);
   leg->SetLineStyle(1);
   leg->SetLineWidth(1);
   leg->SetFillColor(0);
   leg->SetFillStyle(1001);
   TLegendEntry *entry=leg->AddEntry("","Barrel","p");
   entry->SetLineColor(1);
   entry->SetLineStyle(1);
   entry->SetLineWidth(1);
   entry->SetMarkerColor(1);
   entry->SetMarkerStyle(20);
   entry->SetMarkerSize(1.5);
   entry->SetTextFont(62);
   entry=leg->AddEntry("","Endcaps","p");
   entry->SetLineColor(1);
   entry->SetLineStyle(1);
   entry->SetLineWidth(1);
   entry->SetMarkerColor(1);
   entry->SetMarkerStyle(24);
   entry->SetMarkerSize(1.5);
   entry->SetTextFont(62);
   leg->Draw();
   
   leg = new TLegend(0.2,0.2,0.8,0.6,NULL,"brNDC");
   leg->SetTextFont(62);
   leg->SetTextSize(0.05);
   leg->SetLineColor(1);
   leg->SetLineStyle(1);
   leg->SetLineWidth(1);
   leg->SetFillColor(0);
   leg->SetFillStyle(1001);
   entry=leg->AddEntry("Graph","RB1in  + RE1","p");
   entry->SetLineColor(1);
   entry->SetLineStyle(1);
   entry->SetLineWidth(1);

   ci = TColor::GetColor("#ff0000");
   entry->SetMarkerColor(ci);
   entry->SetMarkerStyle(20);
   entry->SetMarkerSize(1.5);
   entry->SetTextFont(62);
   entry=leg->AddEntry("Graph","RB1out + RE1","p");
   entry->SetLineColor(1);
   entry->SetLineStyle(1);
   entry->SetLineWidth(1);

   ci = TColor::GetColor("#0000ff");
   entry->SetMarkerColor(ci);
   entry->SetMarkerStyle(29);
   entry->SetMarkerSize(1.5);
   entry->SetTextFont(62);
   entry=leg->AddEntry("Graph","RB2 + RE2","p");
   entry->SetLineColor(1);
   entry->SetLineStyle(1);
   entry->SetLineWidth(1);

   ci = TColor::GetColor("#990000");
   entry->SetMarkerColor(ci);
   entry->SetMarkerStyle(21);
   entry->SetMarkerSize(1.5);
   entry->SetTextFont(62);
   entry=leg->AddEntry("Graph","RB3 + RE3","p");
   entry->SetLineColor(1);
   entry->SetLineStyle(1);
   entry->SetLineWidth(1);
   entry->SetMarkerColor(6);
   entry->SetMarkerStyle(22);
   entry->SetMarkerSize(1.5);
   entry->SetTextFont(62);
   entry=leg->AddEntry("Graph","RB4 + RE4","p");
   entry->SetLineColor(1);
   entry->SetLineStyle(1);
   entry->SetLineWidth(1);
   entry->SetMarkerColor(28);
   entry->SetMarkerStyle(23);
   entry->SetMarkerSize(1.5);
   entry->SetTextFont(62);
   leg->Draw();
   c1_2->Modified();
   c1->cd();
  
// ------------>Primitives in pad: c1_3
   TPad *c1_3 = new TPad("c1_3", "c1_3",0.6676667,0.501,0.999,0.999);
   c1_3->Draw();
   c1_3->cd();
   c1_3->Range(-2.37264,-0.4382291,1.772408,3.180959);
   c1_3->SetFillColor(0);
   c1_3->SetBorderMode(0);
   c1_3->SetBorderSize(2);
   c1_3->SetLogy();
   c1_3->SetTickx(1);
   c1_3->SetTicky(1);
   c1_3->SetLeftMargin(0.16);
   c1_3->SetRightMargin(0.02);
   c1_3->SetTopMargin(0.05);
   c1_3->SetBottomMargin(0.13);
   c1_3->SetFrameFillStyle(0);
   c1_3->SetFrameBorderMode(0);
   c1_3->SetFrameFillStyle(0);
   c1_3->SetFrameBorderMode(0);
   
   multigraph = new TMultiGraph();
   multigraph->SetName("");
   multigraph->SetTitle("RB1out");
   
   Double_t Graph_fx5[6] = {
   -1.269543,
   -1.38083,
   -1.554935,
   -0.9430065,
   -1.01269,
   -1.104428};
   Double_t Graph_fy5[6] = {
   4.93,
   7.92,
   14.07,
   2.11,
   1.595,
   1.975};
   graph = new TGraph(6,Graph_fx5,Graph_fy5);
   graph->SetName("Graph");
   graph->SetTitle("Layer 1 Endcap");
   graph->SetFillStyle(1000);
   graph->SetLineColor(2);
   graph->SetLineWidth(4);

   ci = TColor::GetColor("#0000ff");
   graph->SetMarkerColor(ci);
   graph->SetMarkerStyle(30);
   graph->SetMarkerSize(1.5);
   
   TH1F *Graph_Graph5 = new TH1F("Graph_Graph5","Layer 1 Endcap",100,-1.616128,-0.8818137);
   Graph_Graph5->SetMinimum(0.3475);
   Graph_Graph5->SetMaximum(15.3175);
   Graph_Graph5->SetDirectory(0);
   Graph_Graph5->SetStats(0);
   Graph_Graph5->SetLineStyle(0);
   Graph_Graph5->SetMarkerStyle(20);
   Graph_Graph5->GetXaxis()->SetTitle("#eta");
   Graph_Graph5->GetXaxis()->SetLabelFont(42);
   Graph_Graph5->GetXaxis()->SetLabelOffset(0.007);
   Graph_Graph5->GetXaxis()->SetLabelSize(0.05);
   Graph_Graph5->GetXaxis()->SetTitleSize(0.06);
   Graph_Graph5->GetXaxis()->SetTitleOffset(0.9);
   Graph_Graph5->GetXaxis()->SetTitleFont(42);
   Graph_Graph5->GetYaxis()->SetTitle("RPC single hit rate (Hz/cm^{2})");
   Graph_Graph5->GetYaxis()->SetLabelFont(42);
   Graph_Graph5->GetYaxis()->SetLabelOffset(0.007);
   Graph_Graph5->GetYaxis()->SetLabelSize(0.05);
   Graph_Graph5->GetYaxis()->SetTitleSize(0.06);
   Graph_Graph5->GetYaxis()->SetTitleOffset(1.25);
   Graph_Graph5->GetYaxis()->SetTitleFont(42);
   Graph_Graph5->GetZaxis()->SetLabelFont(42);
   Graph_Graph5->GetZaxis()->SetLabelOffset(0.007);
   Graph_Graph5->GetZaxis()->SetLabelSize(0.05);
   Graph_Graph5->GetZaxis()->SetTitleSize(0.06);
   Graph_Graph5->GetZaxis()->SetTitleFont(42);
   graph->SetHistogram(Graph_Graph5);
   
   multigraph->Add(graph,"AP");
   
   Double_t Graph_fx6[4] = {
   -0.6684232,
   -0.4372446,
   -1.081175,
   -0.9069221};
   Double_t Graph_fy6[4] = {
   8.42,
   6.03,
   12.68,
   12.44};
   graph = new TGraph(4,Graph_fx6,Graph_fy6);
   graph->SetName("Graph");
   graph->SetTitle("Layer 1 Wheel");
   graph->SetFillStyle(1000);
   graph->SetLineColor(2);
   graph->SetLineWidth(4);

   ci = TColor::GetColor("#0000ff");
   graph->SetMarkerColor(ci);
   graph->SetMarkerStyle(29);
   graph->SetMarkerSize(1.7);
   
   TH1F *Graph_Graph6 = new TH1F("Graph_Graph6","Layer 1 Wheel",100,-1.145568,-0.3728516);
   Graph_Graph6->SetMinimum(5.365);
   Graph_Graph6->SetMaximum(13.345);
   Graph_Graph6->SetDirectory(0);
   Graph_Graph6->SetStats(0);
   Graph_Graph6->SetLineStyle(0);
   Graph_Graph6->SetMarkerStyle(20);
   Graph_Graph6->GetXaxis()->SetTitle("#eta");
   Graph_Graph6->GetXaxis()->SetLabelFont(42);
   Graph_Graph6->GetXaxis()->SetLabelOffset(0.007);
   Graph_Graph6->GetXaxis()->SetLabelSize(0.05);
   Graph_Graph6->GetXaxis()->SetTitleSize(0.06);
   Graph_Graph6->GetXaxis()->SetTitleOffset(0.9);
   Graph_Graph6->GetXaxis()->SetTitleFont(42);
   Graph_Graph6->GetYaxis()->SetTitle("RPC single hit rate (Hz/cm^{2})");
   Graph_Graph6->GetYaxis()->SetLabelFont(42);
   Graph_Graph6->GetYaxis()->SetLabelOffset(0.007);
   Graph_Graph6->GetYaxis()->SetLabelSize(0.05);
   Graph_Graph6->GetYaxis()->SetTitleSize(0.06);
   Graph_Graph6->GetYaxis()->SetTitleOffset(1.25);
   Graph_Graph6->GetYaxis()->SetTitleFont(42);
   Graph_Graph6->GetZaxis()->SetLabelFont(42);
   Graph_Graph6->GetZaxis()->SetLabelOffset(0.007);
   Graph_Graph6->GetZaxis()->SetLabelSize(0.05);
   Graph_Graph6->GetZaxis()->SetTitleSize(0.06);
   Graph_Graph6->GetZaxis()->SetTitleFont(42);
   graph->SetHistogram(Graph_Graph6);
   
   multigraph->Add(graph,"AP");
   
   Double_t Graph_fx7[6] = {
   1.25092,
   1.36161,
   1.53501,
   0.940752,
   1.01269,
   1.104428};
   Double_t Graph_fy7[6] = {
   5.01,
   8.4,
   13.75,
   2.865,
   1.9,
   2.115};
   graph = new TGraph(6,Graph_fx7,Graph_fy7);
   graph->SetName("Graph");
   graph->SetTitle("Layer 4 Endcap");
   graph->SetFillStyle(1000);
   graph->SetLineColor(5);
   graph->SetLineWidth(7);

   ci = TColor::GetColor("#0000ff");
   graph->SetMarkerColor(ci);
   graph->SetMarkerStyle(30);
   graph->SetMarkerSize(1.5);
   
   TH1F *Graph_Graph7 = new TH1F("Graph_Graph7","Layer 4 Endcap",100,0.8813262,1.594436);
   Graph_Graph7->SetMinimum(0.715);
   Graph_Graph7->SetMaximum(14.935);
   Graph_Graph7->SetDirectory(0);
   Graph_Graph7->SetStats(0);
   Graph_Graph7->SetLineStyle(0);
   Graph_Graph7->SetMarkerStyle(20);
   Graph_Graph7->GetXaxis()->SetTitle("#eta");
   Graph_Graph7->GetXaxis()->SetLabelFont(42);
   Graph_Graph7->GetXaxis()->SetLabelOffset(0.007);
   Graph_Graph7->GetXaxis()->SetLabelSize(0.05);
   Graph_Graph7->GetXaxis()->SetTitleSize(0.06);
   Graph_Graph7->GetXaxis()->SetTitleOffset(0.9);
   Graph_Graph7->GetXaxis()->SetTitleFont(42);
   Graph_Graph7->GetYaxis()->SetTitle("RPC single hit rate (Hz/cm^{2})");
   Graph_Graph7->GetYaxis()->SetLabelFont(42);
   Graph_Graph7->GetYaxis()->SetLabelOffset(0.007);
   Graph_Graph7->GetYaxis()->SetLabelSize(0.05);
   Graph_Graph7->GetYaxis()->SetTitleSize(0.06);
   Graph_Graph7->GetYaxis()->SetTitleOffset(1.25);
   Graph_Graph7->GetYaxis()->SetTitleFont(42);
   Graph_Graph7->GetZaxis()->SetLabelFont(42);
   Graph_Graph7->GetZaxis()->SetLabelOffset(0.007);
   Graph_Graph7->GetZaxis()->SetLabelSize(0.05);
   Graph_Graph7->GetZaxis()->SetTitleSize(0.06);
   Graph_Graph7->GetZaxis()->SetTitleFont(42);
   graph->SetHistogram(Graph_Graph7);
   
   multigraph->Add(graph,"AP");
   
   Double_t Graph_fx8[6] = {
   0.1232712,
   -0.1356536,
   0.6501188,
   0.4243846,
   1.056183,
   0.8843007};
   Double_t Graph_fy8[6] = {
   3.05,
   2.89,
   7.54,
   5.77,
   14.6,
   13.21};
   graph = new TGraph(6,Graph_fx8,Graph_fy8);
   graph->SetName("Graph");
   graph->SetTitle("Layer 4 Wheel");
   graph->SetFillStyle(1000);
   graph->SetLineColor(5);
   graph->SetLineWidth(7);

   ci = TColor::GetColor("#0000ff");
   graph->SetMarkerColor(ci);
   graph->SetMarkerStyle(29);
   graph->SetMarkerSize(1.5);
   
   TH1F *Graph_Graph8 = new TH1F("Graph_Graph8","Layer 4 Wheel",100,-0.2548373,1.175367);
   Graph_Graph8->SetMinimum(1.719);
   Graph_Graph8->SetMaximum(15.771);
   Graph_Graph8->SetDirectory(0);
   Graph_Graph8->SetStats(0);
   Graph_Graph8->SetLineStyle(0);
   Graph_Graph8->SetMarkerStyle(20);
   Graph_Graph8->GetXaxis()->SetTitle("#eta");
   Graph_Graph8->GetXaxis()->SetLabelFont(42);
   Graph_Graph8->GetXaxis()->SetLabelOffset(0.007);
   Graph_Graph8->GetXaxis()->SetLabelSize(0.05);
   Graph_Graph8->GetXaxis()->SetTitleSize(0.06);
   Graph_Graph8->GetXaxis()->SetTitleOffset(0.9);
   Graph_Graph8->GetXaxis()->SetTitleFont(42);
   Graph_Graph8->GetYaxis()->SetTitle("RPC single hit rate (Hz/cm^{2})");
   Graph_Graph8->GetYaxis()->SetLabelFont(42);
   Graph_Graph8->GetYaxis()->SetLabelOffset(0.007);
   Graph_Graph8->GetYaxis()->SetLabelSize(0.05);
   Graph_Graph8->GetYaxis()->SetTitleSize(0.06);
   Graph_Graph8->GetYaxis()->SetTitleOffset(1.25);
   Graph_Graph8->GetYaxis()->SetTitleFont(42);
   Graph_Graph8->GetZaxis()->SetLabelFont(42);
   Graph_Graph8->GetZaxis()->SetLabelOffset(0.007);
   Graph_Graph8->GetZaxis()->SetLabelSize(0.05);
   Graph_Graph8->GetZaxis()->SetTitleSize(0.06);
   Graph_Graph8->GetZaxis()->SetTitleFont(42);
   graph->SetHistogram(Graph_Graph8);
   
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
   
   pt = new TPaveText(0.1,0.97,0.55,0.97,"brNDC");
   pt->SetBorderSize(0);
   pt->SetFillStyle(0);
   pt->SetTextSize(0.03);
   pt_LaTex = pt->AddText("CMS Preliminary");
   pt->Draw();
   
   pt = new TPaveText(0.7,0.97,0.9,0.97,"brNDC");
   pt->SetBorderSize(0);
   pt->SetFillStyle(0);
   pt->SetTextSize(0.03);
   pt_LaTex = pt->AddText("1.5 #times 10^{34} Hz/cm^{2} (13 TeV)");
   pt->Draw();
   c1_3->Modified();
   c1->cd();
  
// ------------>Primitives in pad: c1_4
   TPad *c1_4 = new TPad("c1_4", "c1_4",0.001,0.001,0.3323333,0.499);
   c1_4->Draw();
   c1_4->cd();
   c1_4->Range(-2.357352,-0.7690617,1.778353,3.198372);
   c1_4->SetFillColor(0);
   c1_4->SetBorderMode(0);
   c1_4->SetBorderSize(2);
   c1_4->SetLogy();
   c1_4->SetTickx(1);
   c1_4->SetTicky(1);
   c1_4->SetLeftMargin(0.16);
   c1_4->SetRightMargin(0.02);
   c1_4->SetTopMargin(0.05);
   c1_4->SetBottomMargin(0.13);
   c1_4->SetFrameFillStyle(0);
   c1_4->SetFrameBorderMode(0);
   c1_4->SetFrameFillStyle(0);
   c1_4->SetFrameBorderMode(0);
   
   multigraph = new TMultiGraph();
   multigraph->SetName("");
   multigraph->SetTitle("RB2");
   
   Double_t Graph_fx9[6] = {
   -1.30087,
   -1.418788,
   -1.54149,
   -1.006991,
   -1.088097,
   -1.186697};
   Double_t Graph_fy9[6] = {
   8.67,
   19.02,
   34.95,
   5.015,
   4.12,
   5};
   graph = new TGraph(6,Graph_fx9,Graph_fy9);
   graph->SetName("Graph");
   graph->SetTitle("Layer 2 Endcap");
   graph->SetFillStyle(1000);
   graph->SetLineColor(3);
   graph->SetLineWidth(5);

   ci = TColor::GetColor("#990000");
   graph->SetMarkerColor(ci);
   graph->SetMarkerStyle(25);
   graph->SetMarkerSize(1.5);
   
   TH1F *Graph_Graph9 = new TH1F("Graph_Graph9","Layer 2 Endcap",100,-1.59494,-0.9535416);
   Graph_Graph9->SetMinimum(1.037);
   Graph_Graph9->SetMaximum(38.033);
   Graph_Graph9->SetDirectory(0);
   Graph_Graph9->SetStats(0);
   Graph_Graph9->SetLineStyle(0);
   Graph_Graph9->SetMarkerStyle(20);
   Graph_Graph9->GetXaxis()->SetTitle("#eta");
   Graph_Graph9->GetXaxis()->SetLabelFont(42);
   Graph_Graph9->GetXaxis()->SetLabelOffset(0.007);
   Graph_Graph9->GetXaxis()->SetLabelSize(0.05);
   Graph_Graph9->GetXaxis()->SetTitleSize(0.06);
   Graph_Graph9->GetXaxis()->SetTitleOffset(0.9);
   Graph_Graph9->GetXaxis()->SetTitleFont(42);
   Graph_Graph9->GetYaxis()->SetTitle("RPC single hit rate (Hz/cm^{2})");
   Graph_Graph9->GetYaxis()->SetLabelFont(42);
   Graph_Graph9->GetYaxis()->SetLabelOffset(0.007);
   Graph_Graph9->GetYaxis()->SetLabelSize(0.05);
   Graph_Graph9->GetYaxis()->SetTitleSize(0.06);
   Graph_Graph9->GetYaxis()->SetTitleOffset(1.25);
   Graph_Graph9->GetYaxis()->SetTitleFont(42);
   Graph_Graph9->GetZaxis()->SetLabelFont(42);
   Graph_Graph9->GetZaxis()->SetLabelOffset(0.007);
   Graph_Graph9->GetZaxis()->SetLabelSize(0.05);
   Graph_Graph9->GetZaxis()->SetTitleSize(0.06);
   Graph_Graph9->GetZaxis()->SetTitleFont(42);
   graph->SetHistogram(Graph_Graph9);
   
   multigraph->Add(graph,"AP");
   
   Double_t Graph_fx10[8] = {
   -0.6402547,
   -0.3577033,
   -0.5647852,
   -0.3653146,
   -0.9968613,
   -0.8309316,
   -0.961078,
   -0.7492043};
   Double_t Graph_fy10[8] = {
   2.29,
   1.65,
   1.81,
   1.31,
   4.7,
   3.71,
   4.33,
   3.37};
   graph = new TGraph(8,Graph_fx10,Graph_fy10);
   graph->SetName("Graph");
   graph->SetTitle("Layer 2 Wheel");
   graph->SetFillStyle(1000);
   graph->SetLineColor(3);
   graph->SetLineWidth(5);

   ci = TColor::GetColor("#990000");
   graph->SetMarkerColor(ci);
   graph->SetMarkerStyle(21);
   graph->SetMarkerSize(1.5);
   
   TH1F *Graph_Graph10 = new TH1F("Graph_Graph10","Layer 2 Wheel",100,-1.060777,-0.2937875);
   Graph_Graph10->SetMinimum(0.971);
   Graph_Graph10->SetMaximum(5.039);
   Graph_Graph10->SetDirectory(0);
   Graph_Graph10->SetStats(0);
   Graph_Graph10->SetLineStyle(0);
   Graph_Graph10->SetMarkerStyle(20);
   Graph_Graph10->GetXaxis()->SetTitle("#eta");
   Graph_Graph10->GetXaxis()->SetLabelFont(42);
   Graph_Graph10->GetXaxis()->SetLabelOffset(0.007);
   Graph_Graph10->GetXaxis()->SetLabelSize(0.05);
   Graph_Graph10->GetXaxis()->SetTitleSize(0.06);
   Graph_Graph10->GetXaxis()->SetTitleOffset(0.9);
   Graph_Graph10->GetXaxis()->SetTitleFont(42);
   Graph_Graph10->GetYaxis()->SetTitle("RPC single hit rate (Hz/cm^{2})");
   Graph_Graph10->GetYaxis()->SetLabelFont(42);
   Graph_Graph10->GetYaxis()->SetLabelOffset(0.007);
   Graph_Graph10->GetYaxis()->SetLabelSize(0.05);
   Graph_Graph10->GetYaxis()->SetTitleSize(0.06);
   Graph_Graph10->GetYaxis()->SetTitleOffset(1.25);
   Graph_Graph10->GetYaxis()->SetTitleFont(42);
   Graph_Graph10->GetZaxis()->SetLabelFont(42);
   Graph_Graph10->GetZaxis()->SetLabelOffset(0.007);
   Graph_Graph10->GetZaxis()->SetLabelSize(0.05);
   Graph_Graph10->GetZaxis()->SetTitleSize(0.06);
   Graph_Graph10->GetZaxis()->SetTitleFont(42);
   graph->SetHistogram(Graph_Graph10);
   
   multigraph->Add(graph,"AP");
   
   Double_t Graph_fx11[6] = {
   1.30087,
   1.418788,
   1.54149,
   1.006991,
   1.088097,
   1.186697};
   Double_t Graph_fy11[6] = {
   7.165,
   16.775,
   29.81,
   4.53,
   4.02,
   4.33};
   graph = new TGraph(6,Graph_fx11,Graph_fy11);
   graph->SetName("Graph");
   graph->SetTitle("Layer 4 Endcap");
   graph->SetFillStyle(1000);
   graph->SetLineColor(5);
   graph->SetLineWidth(7);

   ci = TColor::GetColor("#990000");
   graph->SetMarkerColor(ci);
   graph->SetMarkerStyle(25);
   graph->SetMarkerSize(1.5);
   
   TH1F *Graph_Graph11 = new TH1F("Graph_Graph11","Layer 4 Endcap",100,0.9535416,1.59494);
   Graph_Graph11->SetMinimum(1.441);
   Graph_Graph11->SetMaximum(32.389);
   Graph_Graph11->SetDirectory(0);
   Graph_Graph11->SetStats(0);
   Graph_Graph11->SetLineStyle(0);
   Graph_Graph11->SetMarkerStyle(20);
   Graph_Graph11->GetXaxis()->SetTitle("#eta");
   Graph_Graph11->GetXaxis()->SetLabelFont(42);
   Graph_Graph11->GetXaxis()->SetLabelOffset(0.007);
   Graph_Graph11->GetXaxis()->SetLabelSize(0.05);
   Graph_Graph11->GetXaxis()->SetTitleSize(0.06);
   Graph_Graph11->GetXaxis()->SetTitleOffset(0.9);
   Graph_Graph11->GetXaxis()->SetTitleFont(42);
   Graph_Graph11->GetYaxis()->SetTitle("RPC single hit rate (Hz/cm^{2})");
   Graph_Graph11->GetYaxis()->SetLabelFont(42);
   Graph_Graph11->GetYaxis()->SetLabelOffset(0.007);
   Graph_Graph11->GetYaxis()->SetLabelSize(0.05);
   Graph_Graph11->GetYaxis()->SetTitleSize(0.06);
   Graph_Graph11->GetYaxis()->SetTitleOffset(1.25);
   Graph_Graph11->GetYaxis()->SetTitleFont(42);
   Graph_Graph11->GetZaxis()->SetLabelFont(42);
   Graph_Graph11->GetZaxis()->SetLabelOffset(0.007);
   Graph_Graph11->GetZaxis()->SetLabelSize(0.05);
   Graph_Graph11->GetZaxis()->SetTitleSize(0.06);
   Graph_Graph11->GetZaxis()->SetTitleFont(42);
   graph->SetHistogram(Graph_Graph11);
   
   multigraph->Add(graph,"AP");
   
   Double_t Graph_fx12[12] = {
   0.1508182,
   -0.1620493,
   0.1070081,
   -0.1177723,
   0.6307283,
   0.3519274,
   0.5727437,
   0.3707642,
   0.984016,
   0.8194372,
   0.9726389,
   0.759068};
   Double_t Graph_fy12[12] = {
   1.16,
   1,
   0.99,
   1.15,
   3.13,
   1.44,
   2.05,
   1.43,
   4.23,
   3.01,
   3.51,
   3.57};
   graph = new TGraph(12,Graph_fx12,Graph_fy12);
   graph->SetName("Graph");
   graph->SetTitle("Layer 4 Wheel");
   graph->SetFillStyle(1000);
   graph->SetLineColor(5);
   graph->SetLineWidth(7);

   ci = TColor::GetColor("#990000");
   graph->SetMarkerColor(ci);
   graph->SetMarkerStyle(21);
   graph->SetMarkerSize(1.5);
   
   TH1F *Graph_Graph12 = new TH1F("Graph_Graph12","Layer 4 Wheel",100,-0.2766558,1.098623);
   Graph_Graph12->SetMinimum(0.666);
   Graph_Graph12->SetMaximum(4.554);
   Graph_Graph12->SetDirectory(0);
   Graph_Graph12->SetStats(0);
   Graph_Graph12->SetLineStyle(0);
   Graph_Graph12->SetMarkerStyle(20);
   Graph_Graph12->GetXaxis()->SetTitle("#eta");
   Graph_Graph12->GetXaxis()->SetLabelFont(42);
   Graph_Graph12->GetXaxis()->SetLabelOffset(0.007);
   Graph_Graph12->GetXaxis()->SetLabelSize(0.05);
   Graph_Graph12->GetXaxis()->SetTitleSize(0.06);
   Graph_Graph12->GetXaxis()->SetTitleOffset(0.9);
   Graph_Graph12->GetXaxis()->SetTitleFont(42);
   Graph_Graph12->GetYaxis()->SetTitle("RPC single hit rate (Hz/cm^{2})");
   Graph_Graph12->GetYaxis()->SetLabelFont(42);
   Graph_Graph12->GetYaxis()->SetLabelOffset(0.007);
   Graph_Graph12->GetYaxis()->SetLabelSize(0.05);
   Graph_Graph12->GetYaxis()->SetTitleSize(0.06);
   Graph_Graph12->GetYaxis()->SetTitleOffset(1.25);
   Graph_Graph12->GetYaxis()->SetTitleFont(42);
   Graph_Graph12->GetZaxis()->SetLabelFont(42);
   Graph_Graph12->GetZaxis()->SetLabelOffset(0.007);
   Graph_Graph12->GetZaxis()->SetLabelSize(0.05);
   Graph_Graph12->GetZaxis()->SetTitleSize(0.06);
   Graph_Graph12->GetZaxis()->SetTitleFont(42);
   graph->SetHistogram(Graph_Graph12);
   
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
   
   pt = new TPaveText(0.1,0.97,0.55,0.97,"brNDC");
   pt->SetBorderSize(0);
   pt->SetFillStyle(0);
   pt->SetTextSize(0.03);
   pt_LaTex = pt->AddText("CMS Preliminary");
   pt->Draw();
   
   pt = new TPaveText(0.7,0.97,0.9,0.97,"brNDC");
   pt->SetBorderSize(0);
   pt->SetFillStyle(0);
   pt->SetTextSize(0.03);
   pt_LaTex = pt->AddText("1.5 #times 10^{34} Hz/cm^{2} (13 TeV)");
   pt->Draw();
   c1_4->Modified();
   c1->cd();
  
// ------------>Primitives in pad: c1_5
   TPad *c1_5 = new TPad("c1_5", "c1_5",0.3343333,0.001,0.6656667,0.499);
   c1_5->Draw();
   c1_5->cd();
   c1_5->Range(-2.650646,-1.344903,1.99961,3.228679);
   c1_5->SetFillColor(0);
   c1_5->SetBorderMode(0);
   c1_5->SetBorderSize(2);
   c1_5->SetLogy();
   c1_5->SetTickx(1);
   c1_5->SetTicky(1);
   c1_5->SetLeftMargin(0.16);
   c1_5->SetRightMargin(0.02);
   c1_5->SetTopMargin(0.05);
   c1_5->SetBottomMargin(0.13);
   c1_5->SetFrameFillStyle(0);
   c1_5->SetFrameBorderMode(0);
   c1_5->SetFrameFillStyle(0);
   c1_5->SetFrameBorderMode(0);
   
   multigraph = new TMultiGraph();
   multigraph->SetName("");
   multigraph->SetTitle("RB3");
   
   Double_t Graph_fx13[6] = {
   -1.483583,
   -1.60646,
   -1.733277,
   -1.17169,
   -1.258672,
   -1.363507};
   Double_t Graph_fy13[6] = {
   8.96,
   18.45,
   30.105,
   6.695,
   6.275,
   6.045};
   graph = new TGraph(6,Graph_fx13,Graph_fy13);
   graph->SetName("Graph");
   graph->SetTitle("Layer 1 Endcap");
   graph->SetFillStyle(1000);
   graph->SetLineColor(2);
   graph->SetLineWidth(4);
   graph->SetMarkerColor(6);
   graph->SetMarkerStyle(26);
   graph->SetMarkerSize(1.5);
   
   TH1F *Graph_Graph13 = new TH1F("Graph_Graph13","Layer 1 Endcap",100,-1.789436,-1.115531);
   Graph_Graph13->SetMinimum(3.639);
   Graph_Graph13->SetMaximum(32.511);
   Graph_Graph13->SetDirectory(0);
   Graph_Graph13->SetStats(0);
   Graph_Graph13->SetLineStyle(0);
   Graph_Graph13->SetMarkerStyle(20);
   Graph_Graph13->GetXaxis()->SetTitle("#eta");
   Graph_Graph13->GetXaxis()->SetLabelFont(42);
   Graph_Graph13->GetXaxis()->SetLabelOffset(0.007);
   Graph_Graph13->GetXaxis()->SetLabelSize(0.05);
   Graph_Graph13->GetXaxis()->SetTitleSize(0.06);
   Graph_Graph13->GetXaxis()->SetTitleOffset(0.9);
   Graph_Graph13->GetXaxis()->SetTitleFont(42);
   Graph_Graph13->GetYaxis()->SetTitle("RPC single hit rate (Hz/cm^{2})");
   Graph_Graph13->GetYaxis()->SetLabelFont(42);
   Graph_Graph13->GetYaxis()->SetLabelOffset(0.007);
   Graph_Graph13->GetYaxis()->SetLabelSize(0.05);
   Graph_Graph13->GetYaxis()->SetTitleSize(0.06);
   Graph_Graph13->GetYaxis()->SetTitleOffset(1.25);
   Graph_Graph13->GetYaxis()->SetTitleFont(42);
   Graph_Graph13->GetZaxis()->SetLabelFont(42);
   Graph_Graph13->GetZaxis()->SetLabelOffset(0.007);
   Graph_Graph13->GetZaxis()->SetLabelSize(0.05);
   Graph_Graph13->GetZaxis()->SetTitleSize(0.06);
   Graph_Graph13->GetZaxis()->SetTitleFont(42);
   graph->SetHistogram(Graph_Graph13);
   
   multigraph->Add(graph,"AP");
   
   Double_t Graph_fx14[8] = {
   -0.5015153,
   -0.3223997,
   -0.518495,
   -0.333847,
   -0.84419,
   -0.6957875,
   -0.8692863,
   -0.7177791};
   Double_t Graph_fy14[8] = {
   0.5,
   0.42,
   0.45,
   0.47,
   0.67,
   0.5,
   0.7,
   0.49};
   graph = new TGraph(8,Graph_fx14,Graph_fy14);
   graph->SetName("Graph");
   graph->SetTitle("Layer 1 Wheel");
   graph->SetFillStyle(1000);
   graph->SetLineColor(2);
   graph->SetLineWidth(4);
   graph->SetMarkerColor(6);
   graph->SetMarkerStyle(22);
   graph->SetMarkerSize(1.5);
   
   TH1F *Graph_Graph14 = new TH1F("Graph_Graph14","Layer 1 Wheel",100,-0.9239749,-0.267711);
   Graph_Graph14->SetMinimum(0.392);
   Graph_Graph14->SetMaximum(0.728);
   Graph_Graph14->SetDirectory(0);
   Graph_Graph14->SetStats(0);
   Graph_Graph14->SetLineStyle(0);
   Graph_Graph14->SetMarkerStyle(20);
   Graph_Graph14->GetXaxis()->SetTitle("#eta");
   Graph_Graph14->GetXaxis()->SetLabelFont(42);
   Graph_Graph14->GetXaxis()->SetLabelOffset(0.007);
   Graph_Graph14->GetXaxis()->SetLabelSize(0.05);
   Graph_Graph14->GetXaxis()->SetTitleSize(0.06);
   Graph_Graph14->GetXaxis()->SetTitleOffset(0.9);
   Graph_Graph14->GetXaxis()->SetTitleFont(42);
   Graph_Graph14->GetYaxis()->SetTitle("RPC single hit rate (Hz/cm^{2})");
   Graph_Graph14->GetYaxis()->SetLabelFont(42);
   Graph_Graph14->GetYaxis()->SetLabelOffset(0.007);
   Graph_Graph14->GetYaxis()->SetLabelSize(0.05);
   Graph_Graph14->GetYaxis()->SetTitleSize(0.06);
   Graph_Graph14->GetYaxis()->SetTitleOffset(1.25);
   Graph_Graph14->GetYaxis()->SetTitleFont(42);
   Graph_Graph14->GetZaxis()->SetLabelFont(42);
   Graph_Graph14->GetZaxis()->SetLabelOffset(0.007);
   Graph_Graph14->GetZaxis()->SetLabelSize(0.05);
   Graph_Graph14->GetZaxis()->SetTitleSize(0.06);
   Graph_Graph14->GetZaxis()->SetTitleFont(42);
   graph->SetHistogram(Graph_Graph14);
   
   multigraph->Add(graph,"AP");
   
   Double_t Graph_fx15[6] = {
   1.483583,
   1.60646,
   1.733277,
   1.17169,
   1.258672,
   1.363507};
   Double_t Graph_fy15[6] = {
   9.81,
   19.21,
   30.445,
   7.805,
   6.565,
   7.11};
   graph = new TGraph(6,Graph_fx15,Graph_fy15);
   graph->SetName("Graph");
   graph->SetTitle("Layer 4 Endcap");
   graph->SetFillStyle(1000);
   graph->SetLineColor(5);
   graph->SetLineWidth(7);
   graph->SetMarkerColor(6);
   graph->SetMarkerStyle(26);
   graph->SetMarkerSize(1.5);
   
   TH1F *Graph_Graph15 = new TH1F("Graph_Graph15","Layer 4 Endcap",100,1.115531,1.789436);
   Graph_Graph15->SetMinimum(4.177);
   Graph_Graph15->SetMaximum(32.833);
   Graph_Graph15->SetDirectory(0);
   Graph_Graph15->SetStats(0);
   Graph_Graph15->SetLineStyle(0);
   Graph_Graph15->SetMarkerStyle(20);
   Graph_Graph15->GetXaxis()->SetTitle("#eta");
   Graph_Graph15->GetXaxis()->SetLabelFont(42);
   Graph_Graph15->GetXaxis()->SetLabelOffset(0.007);
   Graph_Graph15->GetXaxis()->SetLabelSize(0.05);
   Graph_Graph15->GetXaxis()->SetTitleSize(0.06);
   Graph_Graph15->GetXaxis()->SetTitleOffset(0.9);
   Graph_Graph15->GetXaxis()->SetTitleFont(42);
   Graph_Graph15->GetYaxis()->SetTitle("RPC single hit rate (Hz/cm^{2})");
   Graph_Graph15->GetYaxis()->SetLabelFont(42);
   Graph_Graph15->GetYaxis()->SetLabelOffset(0.007);
   Graph_Graph15->GetYaxis()->SetLabelSize(0.05);
   Graph_Graph15->GetYaxis()->SetTitleSize(0.06);
   Graph_Graph15->GetYaxis()->SetTitleOffset(1.25);
   Graph_Graph15->GetYaxis()->SetTitleFont(42);
   Graph_Graph15->GetZaxis()->SetLabelFont(42);
   Graph_Graph15->GetZaxis()->SetLabelOffset(0.007);
   Graph_Graph15->GetZaxis()->SetLabelSize(0.05);
   Graph_Graph15->GetZaxis()->SetTitleSize(0.06);
   Graph_Graph15->GetZaxis()->SetTitleFont(42);
   graph->SetHistogram(Graph_Graph15);
   
   multigraph->Add(graph,"AP");
   
   Double_t Graph_fx16[12] = {
   0.09594883,
   -0.1056089,
   0.09388923,
   -0.1033433,
   0.5183615,
   0.3337568,
   0.5080792,
   0.326819,
   0.8690899,
   0.7176067,
   0.8539197,
   0.704303};
   Double_t Graph_fy16[12] = {
   0.5,
   0.45,
   0.35,
   0.38,
   0.59,
   0.49,
   0.64,
   0.57,
   0.88,
   0.66,
   0.9,
   0.795};
   graph = new TGraph(12,Graph_fx16,Graph_fy16);
   graph->SetName("Graph");
   graph->SetTitle("Layer 4 Wheel");
   graph->SetFillStyle(1000);
   graph->SetLineColor(5);
   graph->SetLineWidth(7);
   graph->SetMarkerColor(6);
   graph->SetMarkerStyle(22);
   graph->SetMarkerSize(1.5);
   
   TH1F *Graph_Graph16 = new TH1F("Graph_Graph16","Layer 4 Wheel",100,-0.2030788,0.9665598);
   Graph_Graph16->SetMinimum(0.295);
   Graph_Graph16->SetMaximum(0.955);
   Graph_Graph16->SetDirectory(0);
   Graph_Graph16->SetStats(0);
   Graph_Graph16->SetLineStyle(0);
   Graph_Graph16->SetMarkerStyle(20);
   Graph_Graph16->GetXaxis()->SetTitle("#eta");
   Graph_Graph16->GetXaxis()->SetLabelFont(42);
   Graph_Graph16->GetXaxis()->SetLabelOffset(0.007);
   Graph_Graph16->GetXaxis()->SetLabelSize(0.05);
   Graph_Graph16->GetXaxis()->SetTitleSize(0.06);
   Graph_Graph16->GetXaxis()->SetTitleOffset(0.9);
   Graph_Graph16->GetXaxis()->SetTitleFont(42);
   Graph_Graph16->GetYaxis()->SetTitle("RPC single hit rate (Hz/cm^{2})");
   Graph_Graph16->GetYaxis()->SetLabelFont(42);
   Graph_Graph16->GetYaxis()->SetLabelOffset(0.007);
   Graph_Graph16->GetYaxis()->SetLabelSize(0.05);
   Graph_Graph16->GetYaxis()->SetTitleSize(0.06);
   Graph_Graph16->GetYaxis()->SetTitleOffset(1.25);
   Graph_Graph16->GetYaxis()->SetTitleFont(42);
   Graph_Graph16->GetZaxis()->SetLabelFont(42);
   Graph_Graph16->GetZaxis()->SetLabelOffset(0.007);
   Graph_Graph16->GetZaxis()->SetLabelSize(0.05);
   Graph_Graph16->GetZaxis()->SetTitleSize(0.06);
   Graph_Graph16->GetZaxis()->SetTitleFont(42);
   graph->SetHistogram(Graph_Graph16);
   
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
   
   pt = new TPaveText(0.1,0.97,0.55,0.97,"brNDC");
   pt->SetBorderSize(0);
   pt->SetFillStyle(0);
   pt->SetTextSize(0.03);
   pt_LaTex = pt->AddText("CMS Preliminary");
   pt->Draw();
   
   pt = new TPaveText(0.7,0.97,0.9,0.97,"brNDC");
   pt->SetBorderSize(0);
   pt->SetFillStyle(0);
   pt->SetTextSize(0.03);
   pt_LaTex = pt->AddText("1.5 #times 10^{34} Hz/cm^{2} (13 TeV)");
   pt->Draw();
   c1_5->Modified();
   c1->cd();
  
// ------------>Primitives in pad: c1_6
   TPad *c1_6 = new TPad("c1_6", "c1_6",0.6676667,0.001,0.999,0.499);
   c1_6->Draw();
   c1_6->cd();
   c1_6->Range(-2.779513,0.06893769,2.098545,3.154266);
   c1_6->SetFillColor(0);
   c1_6->SetBorderMode(0);
   c1_6->SetBorderSize(2);
   c1_6->SetLogy();
   c1_6->SetTickx(1);
   c1_6->SetTicky(1);
   c1_6->SetLeftMargin(0.16);
   c1_6->SetRightMargin(0.02);
   c1_6->SetTopMargin(0.05);
   c1_6->SetBottomMargin(0.13);
   c1_6->SetFrameFillStyle(0);
   c1_6->SetFrameBorderMode(0);
   c1_6->SetFrameFillStyle(0);
   c1_6->SetFrameBorderMode(0);
   
   multigraph = new TMultiGraph();
   multigraph->SetName("");
   multigraph->SetTitle("RB4");
   
   Double_t Graph_fx17[6] = {
   -1.564398,
   -1.688988,
   -1.817205,
   -1.24603,
   -1.33517,
   -1.442247};
   Double_t Graph_fy17[6] = {
   22.105,
   31.31,
   39.28,
   20.68,
   19.685,
   20.695};
   graph = new TGraph(6,Graph_fx17,Graph_fy17);
   graph->SetName("Graph");
   graph->SetTitle("Layer 2 Endcap");
   graph->SetFillStyle(1000);
   graph->SetLineColor(3);
   graph->SetLineWidth(5);
   graph->SetMarkerColor(28);
   graph->SetMarkerStyle(32);
   graph->SetMarkerSize(1.5);
   
   TH1F *Graph_Graph17 = new TH1F("Graph_Graph17","Layer 2 Endcap",100,-1.874322,-1.188913);
   Graph_Graph17->SetMinimum(17.7255);
   Graph_Graph17->SetMaximum(41.2395);
   Graph_Graph17->SetDirectory(0);
   Graph_Graph17->SetStats(0);
   Graph_Graph17->SetLineStyle(0);
   Graph_Graph17->SetMarkerStyle(20);
   Graph_Graph17->GetXaxis()->SetTitle("#eta");
   Graph_Graph17->GetXaxis()->SetLabelFont(42);
   Graph_Graph17->GetXaxis()->SetLabelOffset(0.007);
   Graph_Graph17->GetXaxis()->SetLabelSize(0.05);
   Graph_Graph17->GetXaxis()->SetTitleSize(0.06);
   Graph_Graph17->GetXaxis()->SetTitleOffset(0.9);
   Graph_Graph17->GetXaxis()->SetTitleFont(42);
   Graph_Graph17->GetYaxis()->SetTitle("RPC single hit rate (Hz/cm^{2})");
   Graph_Graph17->GetYaxis()->SetLabelFont(42);
   Graph_Graph17->GetYaxis()->SetLabelOffset(0.007);
   Graph_Graph17->GetYaxis()->SetLabelSize(0.05);
   Graph_Graph17->GetYaxis()->SetTitleSize(0.06);
   Graph_Graph17->GetYaxis()->SetTitleOffset(1.25);
   Graph_Graph17->GetYaxis()->SetTitleFont(42);
   Graph_Graph17->GetZaxis()->SetLabelFont(42);
   Graph_Graph17->GetZaxis()->SetLabelOffset(0.007);
   Graph_Graph17->GetZaxis()->SetLabelSize(0.05);
   Graph_Graph17->GetZaxis()->SetTitleSize(0.06);
   Graph_Graph17->GetZaxis()->SetTitleFont(42);
   graph->SetHistogram(Graph_Graph17);
   
   multigraph->Add(graph,"AP");
   
   Double_t Graph_fx18[8] = {
   -0.4436355,
   -0.2837401,
   -0.4465736,
   -0.2856898,
   -0.7406925,
   -0.6060548,
   -0.7588612,
   -0.6213755};
   Double_t Graph_fy18[8] = {
   12.82,
   12.53,
   7.545,
   9.585,
   13.66,
   15.985,
   4.38,
   7.22};
   graph = new TGraph(8,Graph_fx18,Graph_fy18);
   graph->SetName("Graph");
   graph->SetTitle("Layer 2 Wheel");
   graph->SetFillStyle(1000);
   graph->SetLineColor(3);
   graph->SetLineWidth(5);
   graph->SetMarkerColor(28);
   graph->SetMarkerStyle(23);
   graph->SetMarkerSize(1.7);
   
   TH1F *Graph_Graph18 = new TH1F("Graph_Graph18","Layer 2 Wheel",100,-0.8063733,-0.236228);
   Graph_Graph18->SetMinimum(3.2195);
   Graph_Graph18->SetMaximum(17.1455);
   Graph_Graph18->SetDirectory(0);
   Graph_Graph18->SetStats(0);
   Graph_Graph18->SetLineStyle(0);
   Graph_Graph18->SetMarkerStyle(20);
   Graph_Graph18->GetXaxis()->SetTitle("#eta");
   Graph_Graph18->GetXaxis()->SetLabelFont(42);
   Graph_Graph18->GetXaxis()->SetLabelOffset(0.007);
   Graph_Graph18->GetXaxis()->SetLabelSize(0.05);
   Graph_Graph18->GetXaxis()->SetTitleSize(0.06);
   Graph_Graph18->GetXaxis()->SetTitleOffset(0.9);
   Graph_Graph18->GetXaxis()->SetTitleFont(42);
   Graph_Graph18->GetYaxis()->SetTitle("RPC single hit rate (Hz/cm^{2})");
   Graph_Graph18->GetYaxis()->SetLabelFont(42);
   Graph_Graph18->GetYaxis()->SetLabelOffset(0.007);
   Graph_Graph18->GetYaxis()->SetLabelSize(0.05);
   Graph_Graph18->GetYaxis()->SetTitleSize(0.06);
   Graph_Graph18->GetYaxis()->SetTitleOffset(1.25);
   Graph_Graph18->GetYaxis()->SetTitleFont(42);
   Graph_Graph18->GetZaxis()->SetLabelFont(42);
   Graph_Graph18->GetZaxis()->SetLabelOffset(0.007);
   Graph_Graph18->GetZaxis()->SetLabelSize(0.05);
   Graph_Graph18->GetZaxis()->SetTitleSize(0.06);
   Graph_Graph18->GetZaxis()->SetTitleFont(42);
   graph->SetHistogram(Graph_Graph18);
   
   multigraph->Add(graph,"AP");
   
   Double_t Graph_fx19[6] = {
   1.56629,
   1.69092,
   1.819165,
   1.24603,
   1.33517,
   1.442247};
   Double_t Graph_fy19[6] = {
   21.57,
   33.02,
   40.695,
   22.6,
   20.07,
   20.395};
   graph = new TGraph(6,Graph_fx19,Graph_fy19);
   graph->SetName("Graph");
   graph->SetTitle("Layer 4 Endcap");
   graph->SetFillStyle(1000);
   graph->SetLineColor(5);
   graph->SetLineWidth(7);
   graph->SetMarkerColor(28);
   graph->SetMarkerStyle(32);
   graph->SetMarkerSize(1.5);
   
   TH1F *Graph_Graph19 = new TH1F("Graph_Graph19","Layer 4 Endcap",100,1.188716,1.876478);
   Graph_Graph19->SetMinimum(18.0075);
   Graph_Graph19->SetMaximum(42.7575);
   Graph_Graph19->SetDirectory(0);
   Graph_Graph19->SetStats(0);
   Graph_Graph19->SetLineStyle(0);
   Graph_Graph19->SetMarkerStyle(20);
   Graph_Graph19->GetXaxis()->SetTitle("#eta");
   Graph_Graph19->GetXaxis()->SetLabelFont(42);
   Graph_Graph19->GetXaxis()->SetLabelOffset(0.007);
   Graph_Graph19->GetXaxis()->SetLabelSize(0.05);
   Graph_Graph19->GetXaxis()->SetTitleSize(0.06);
   Graph_Graph19->GetXaxis()->SetTitleOffset(0.9);
   Graph_Graph19->GetXaxis()->SetTitleFont(42);
   Graph_Graph19->GetYaxis()->SetTitle("RPC single hit rate (Hz/cm^{2})");
   Graph_Graph19->GetYaxis()->SetLabelFont(42);
   Graph_Graph19->GetYaxis()->SetLabelOffset(0.007);
   Graph_Graph19->GetYaxis()->SetLabelSize(0.05);
   Graph_Graph19->GetYaxis()->SetTitleSize(0.06);
   Graph_Graph19->GetYaxis()->SetTitleOffset(1.25);
   Graph_Graph19->GetYaxis()->SetTitleFont(42);
   Graph_Graph19->GetZaxis()->SetLabelFont(42);
   Graph_Graph19->GetZaxis()->SetLabelOffset(0.007);
   Graph_Graph19->GetZaxis()->SetLabelSize(0.05);
   Graph_Graph19->GetZaxis()->SetTitleSize(0.06);
   Graph_Graph19->GetZaxis()->SetTitleFont(42);
   graph->SetHistogram(Graph_Graph19);
   
   multigraph->Add(graph,"AP");
   
   Double_t Graph_fx20[12] = {
   0.002692048,
   -0.08955609,
   0.07597283,
   -0.0836318,
   0.4449627,
   0.2846205,
   0.4259257,
   0.2720173,
   0.7588613,
   0.6216822,
   0.7295206,
   0.5964391};
   Double_t Graph_fy20[12] = {
   10.12,
   8.25,
   7.61,
   8.04,
   14.29,
   17.56,
   16.04,
   16.95,
   16.07,
   17.685,
   17.85,
   22.82};
   graph = new TGraph(12,Graph_fx20,Graph_fy20);
   graph->SetName("Graph");
   graph->SetTitle("Layer 4 Wheel");
   graph->SetFillStyle(1000);
   graph->SetLineColor(5);
   graph->SetLineWidth(7);
   graph->SetMarkerColor(28);
   graph->SetMarkerStyle(23);
   graph->SetMarkerSize(1.5);
   
   TH1F *Graph_Graph20 = new TH1F("Graph_Graph20","Layer 4 Wheel",100,-0.1743978,0.843703);
   Graph_Graph20->SetMinimum(6.089);
   Graph_Graph20->SetMaximum(24.341);
   Graph_Graph20->SetDirectory(0);
   Graph_Graph20->SetStats(0);
   Graph_Graph20->SetLineStyle(0);
   Graph_Graph20->SetMarkerStyle(20);
   Graph_Graph20->GetXaxis()->SetTitle("#eta");
   Graph_Graph20->GetXaxis()->SetLabelFont(42);
   Graph_Graph20->GetXaxis()->SetLabelOffset(0.007);
   Graph_Graph20->GetXaxis()->SetLabelSize(0.05);
   Graph_Graph20->GetXaxis()->SetTitleSize(0.06);
   Graph_Graph20->GetXaxis()->SetTitleOffset(0.9);
   Graph_Graph20->GetXaxis()->SetTitleFont(42);
   Graph_Graph20->GetYaxis()->SetTitle("RPC single hit rate (Hz/cm^{2})");
   Graph_Graph20->GetYaxis()->SetLabelFont(42);
   Graph_Graph20->GetYaxis()->SetLabelOffset(0.007);
   Graph_Graph20->GetYaxis()->SetLabelSize(0.05);
   Graph_Graph20->GetYaxis()->SetTitleSize(0.06);
   Graph_Graph20->GetYaxis()->SetTitleOffset(1.25);
   Graph_Graph20->GetYaxis()->SetTitleFont(42);
   Graph_Graph20->GetZaxis()->SetLabelFont(42);
   Graph_Graph20->GetZaxis()->SetLabelOffset(0.007);
   Graph_Graph20->GetZaxis()->SetLabelSize(0.05);
   Graph_Graph20->GetZaxis()->SetTitleSize(0.06);
   Graph_Graph20->GetZaxis()->SetTitleFont(42);
   graph->SetHistogram(Graph_Graph20);
   
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
   
   pt = new TPaveText(0.1,0.97,0.55,0.97,"brNDC");
   pt->SetBorderSize(0);
   pt->SetFillStyle(0);
   pt->SetTextSize(0.03);
   pt_LaTex = pt->AddText("CMS Preliminary");
   pt->Draw();
   
   pt = new TPaveText(0.7,0.97,0.9,0.97,"brNDC");
   pt->SetBorderSize(0);
   pt->SetFillStyle(0);
   pt->SetTextSize(0.03);
   pt_LaTex = pt->AddText("1.5 #times 10^{34} Hz/cm^{2} (13 TeV)");
   pt->Draw();
   c1_6->Modified();
   c1->cd();
   TLatex *   tex = new TLatex(0.98,0.952,"13 TeV");
tex->SetNDC();
   tex->SetTextAlign(31);
   tex->SetTextFont(42);
   tex->SetTextSize(0.036);
   tex->SetLineWidth(2);
   tex->Draw();
      tex = new TLatex(0.1014,0.91025,"CMS");
tex->SetNDC();
   tex->SetTextAlign(13);
   tex->SetTextFont(61);
   tex->SetTextSize(0.045);
   tex->SetLineWidth(2);
   tex->Draw();
      tex = new TLatex(0.1014,0.85625,"Preliminary");
tex->SetNDC();
   tex->SetTextAlign(13);
   tex->SetTextFont(52);
   tex->SetTextSize(0.0342);
   tex->SetLineWidth(2);
   tex->Draw();
      tex = new TLatex(0.1014,0.80765,"2018 pp data");
tex->SetNDC();
   tex->SetTextAlign(13);
   tex->SetTextFont(52);
   tex->SetTextSize(0.0342);
   tex->SetLineWidth(2);
   tex->Draw();
      tex = new TLatex(0.06,0.952,"title");
tex->SetNDC();
   tex->SetTextFont(42);
   tex->SetTextSize(0.036);
   tex->SetLineWidth(2);
   tex->Draw();
   c1->Modified();
   c1->cd();
   c1->SetSelected(c1);
}
