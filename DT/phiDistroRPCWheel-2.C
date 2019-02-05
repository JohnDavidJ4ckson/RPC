void phiDistroRPCWheel-2()
{
//=========Macro generated from canvas: c/Canvas
//=========  (Tue Jan 22 21:35:14 2019) by ROOT version 6.12/04
   TCanvas *c = new TCanvas("c", "Canvas",0,45,800,775);
   c->SetHighLightColor(2);
   c->Range(-87.68876,-0.0302516,375.9553,1.519708);
   c->SetFillColor(0);
   c->SetBorderMode(0);
   c->SetBorderSize(2);
   c->SetLogy();
   c->SetGridx();
   c->SetGridy();
   c->SetLeftMargin(0.15);
   c->SetRightMargin(0.06);
   c->SetBottomMargin(0.14);
   c->SetFrameBorderMode(0);
   c->SetFrameBorderMode(0);
   
   TMultiGraph *multigraph = new TMultiGraph();
   multigraph->SetName("");
   multigraph->SetTitle("W-2");
   
   Double_t Graph_fx1[11] = {
   307.3294,
   279.488,
   330.4178,
   217.1706,
   164.7241,
   202.2778,
   101.8656,
   137.242,
   30.41751,
   57.72487,
   8.49541};
   Double_t Graph_fy1[11] = {
   2.5,
   5,
   8,
   5,
   6,
   7.5,
   4.2,
   4.666667,
   6,
   4,
   2};
   TGraph *graph = new TGraph(11,Graph_fx1,Graph_fy1);
   graph->SetName("Graph");
   graph->SetTitle("W-2_RB4");
   graph->SetFillStyle(1000);
   graph->SetLineColor(5);
   graph->SetLineWidth(7);
   graph->SetMarkerColor(2);
   graph->SetMarkerStyle(26);
   graph->SetMarkerSize(1.5);
   
   TH1F *Graph_Graph1 = new TH1F("Graph_Graph1","W-2_RB4",100,0,362.61);
   Graph_Graph1->SetMinimum(1.4);
   Graph_Graph1->SetMaximum(8.6);
   Graph_Graph1->SetDirectory(0);
   Graph_Graph1->SetStats(0);

   Int_t ci;      // for color index setting
   TColor *color; // for color definition with alpha
   ci = TColor::GetColor("#000099");
   Graph_Graph1->SetLineColor(ci);
   Graph_Graph1->GetXaxis()->SetTitle("#phi");
   Graph_Graph1->GetXaxis()->SetLabelFont(42);
   Graph_Graph1->GetXaxis()->SetLabelSize(0.035);
   Graph_Graph1->GetXaxis()->SetTitleSize(0.035);
   Graph_Graph1->GetXaxis()->SetTitleFont(42);
   Graph_Graph1->GetYaxis()->SetTitle("RPC single hit rate (Hz/cm^{2})");
   Graph_Graph1->GetYaxis()->SetLabelFont(42);
   Graph_Graph1->GetYaxis()->SetLabelSize(0.035);
   Graph_Graph1->GetYaxis()->SetTitleSize(0.035);
   Graph_Graph1->GetYaxis()->SetTitleOffset(0);
   Graph_Graph1->GetYaxis()->SetTitleFont(42);
   Graph_Graph1->GetZaxis()->SetLabelFont(42);
   Graph_Graph1->GetZaxis()->SetLabelSize(0.035);
   Graph_Graph1->GetZaxis()->SetTitleSize(0.035);
   Graph_Graph1->GetZaxis()->SetTitleFont(42);
   graph->SetHistogram(Graph_Graph1);
   
   multigraph->Add(graph,"AP");
   
   Double_t Graph_fx2[12] = {
   270.4085,
   304.9638,
   330.4085,
   64.96377,
   39.51911,
   4.963811,
   180.4085,
   159.5191,
   129.5191,
   94.96381,
   231.2979,
   210.4085};
   Double_t Graph_fy2[12] = {
   4.666667,
   7,
   4.333333,
   4,
   7.333333,
   5.25,
   5.666667,
   4.666667,
   4.666667,
   6.5,
   3,
   5.666667};
   graph = new TGraph(12,Graph_fx2,Graph_fy2);
   graph->SetName("Graph");
   graph->SetTitle("W-2_RB1");
   graph->SetFillStyle(1000);
   graph->SetLineColor(5);
   graph->SetLineWidth(7);
   graph->SetMarkerColor(2);
   graph->SetMarkerStyle(20);
   graph->SetMarkerSize(1.5);
   
   TH1F *Graph_Graph2 = new TH1F("Graph_Graph2","W-2_RB1",100,0,362.9529);
   Graph_Graph2->SetMinimum(2.566667);
   Graph_Graph2->SetMaximum(7.766667);
   Graph_Graph2->SetDirectory(0);
   Graph_Graph2->SetStats(0);

   ci = TColor::GetColor("#000099");
   Graph_Graph2->SetLineColor(ci);
   Graph_Graph2->GetXaxis()->SetTitle("#phi");
   Graph_Graph2->GetXaxis()->SetLabelFont(42);
   Graph_Graph2->GetXaxis()->SetLabelSize(0.035);
   Graph_Graph2->GetXaxis()->SetTitleSize(0.035);
   Graph_Graph2->GetXaxis()->SetTitleFont(42);
   Graph_Graph2->GetYaxis()->SetTitle("RPC single hit rate (Hz/cm^{2})");
   Graph_Graph2->GetYaxis()->SetLabelFont(42);
   Graph_Graph2->GetYaxis()->SetLabelSize(0.035);
   Graph_Graph2->GetYaxis()->SetTitleSize(0.035);
   Graph_Graph2->GetYaxis()->SetTitleOffset(0);
   Graph_Graph2->GetYaxis()->SetTitleFont(42);
   Graph_Graph2->GetZaxis()->SetLabelFont(42);
   Graph_Graph2->GetZaxis()->SetLabelSize(0.035);
   Graph_Graph2->GetZaxis()->SetTitleSize(0.035);
   Graph_Graph2->GetZaxis()->SetTitleFont(42);
   graph->SetHistogram(Graph_Graph2);
   
   multigraph->Add(graph,"AP");
   
   Double_t Graph_fx3[12] = {
   325.8213,
   298.5069,
   255.0789,
   81.79292,
   118.5069,
   144.0309,
   178.5069,
   -1.493106,
   32.98288,
   54.03093,
   205.8213,
   234.0309};
   Double_t Graph_fy3[12] = {
   4.4,
   4.25,
   3,
   4.75,
   6.75,
   7.666667,
   4.25,
   3.25,
   4,
   4.666667,
   5.6,
   6.666667};
   graph = new TGraph(12,Graph_fx3,Graph_fy3);
   graph->SetName("Graph");
   graph->SetTitle("W-2_RB2");
   graph->SetFillStyle(1000);
   graph->SetLineColor(5);
   graph->SetLineWidth(7);
   graph->SetMarkerColor(2);
   graph->SetMarkerStyle(25);
   graph->SetMarkerSize(1.5);
   
   TH1F *Graph_Graph3 = new TH1F("Graph_Graph3","W-2_RB2",100,-34.22455,358.5528);
   Graph_Graph3->SetMinimum(2.533333);
   Graph_Graph3->SetMaximum(8.133333);
   Graph_Graph3->SetDirectory(0);
   Graph_Graph3->SetStats(0);

   ci = TColor::GetColor("#000099");
   Graph_Graph3->SetLineColor(ci);
   Graph_Graph3->GetXaxis()->SetTitle("#phi");
   Graph_Graph3->GetXaxis()->SetLabelFont(42);
   Graph_Graph3->GetXaxis()->SetLabelSize(0.035);
   Graph_Graph3->GetXaxis()->SetTitleSize(0.035);
   Graph_Graph3->GetXaxis()->SetTitleFont(42);
   Graph_Graph3->GetYaxis()->SetTitle("RPC single hit rate (Hz/cm^{2})");
   Graph_Graph3->GetYaxis()->SetLabelFont(42);
   Graph_Graph3->GetYaxis()->SetLabelSize(0.035);
   Graph_Graph3->GetYaxis()->SetTitleSize(0.035);
   Graph_Graph3->GetYaxis()->SetTitleOffset(0);
   Graph_Graph3->GetYaxis()->SetTitleFont(42);
   Graph_Graph3->GetZaxis()->SetLabelFont(42);
   Graph_Graph3->GetZaxis()->SetLabelSize(0.035);
   Graph_Graph3->GetZaxis()->SetTitleSize(0.035);
   Graph_Graph3->GetZaxis()->SetTitleFont(42);
   graph->SetHistogram(Graph_Graph3);
   
   multigraph->Add(graph,"AP");
   
   Double_t Graph_fx4[12] = {
   126.1186,
   100.7495,
   188.434,
   156.1186,
   8.434024,
   75.38041,
   31.48767,
   250.7495,
   220.7495,
   331.4877,
   278.434,
   308.434};
   Double_t Graph_fy4[12] = {
   4,
   5.666667,
   8,
   6.666667,
   8,
   5,
   7,
   7.666667,
   7.666667,
   4,
   6.25,
   4};
   graph = new TGraph(12,Graph_fx4,Graph_fy4);
   graph->SetName("Graph");
   graph->SetTitle("W-2_RB3");
   graph->SetFillStyle(1000);
   graph->SetLineColor(5);
   graph->SetLineWidth(7);
   graph->SetMarkerColor(2);
   graph->SetMarkerStyle(23);
   graph->SetMarkerSize(1.5);
   
   TH1F *Graph_Graph4 = new TH1F("Graph_Graph4","W-2_RB3",100,0,363.793);
   Graph_Graph4->SetMinimum(3.6);
   Graph_Graph4->SetMaximum(8.4);
   Graph_Graph4->SetDirectory(0);
   Graph_Graph4->SetStats(0);

   ci = TColor::GetColor("#000099");
   Graph_Graph4->SetLineColor(ci);
   Graph_Graph4->GetXaxis()->SetTitle("#phi");
   Graph_Graph4->GetXaxis()->SetLabelFont(42);
   Graph_Graph4->GetXaxis()->SetLabelSize(0.035);
   Graph_Graph4->GetXaxis()->SetTitleSize(0.035);
   Graph_Graph4->GetXaxis()->SetTitleFont(42);
   Graph_Graph4->GetYaxis()->SetTitle("RPC single hit rate (Hz/cm^{2})");
   Graph_Graph4->GetYaxis()->SetLabelFont(42);
   Graph_Graph4->GetYaxis()->SetLabelSize(0.035);
   Graph_Graph4->GetYaxis()->SetTitleSize(0.035);
   Graph_Graph4->GetYaxis()->SetTitleOffset(0);
   Graph_Graph4->GetYaxis()->SetTitleFont(42);
   Graph_Graph4->GetZaxis()->SetLabelFont(42);
   Graph_Graph4->GetZaxis()->SetLabelSize(0.035);
   Graph_Graph4->GetZaxis()->SetTitleSize(0.035);
   Graph_Graph4->GetZaxis()->SetTitleFont(42);
   graph->SetHistogram(Graph_Graph4);
   
   multigraph->Add(graph,"AP");
   multigraph->Draw("a");
   multigraph->GetXaxis()->SetTitle("#phi");
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
   
   TPaveText *pt = new TPaveText(0.4473935,0.94,0.5526065,0.995,"blNDC");
   pt->SetName("title");
   pt->SetBorderSize(0);
   pt->SetFillColor(0);
   pt->SetFillStyle(0);
   pt->SetTextFont(42);
   TText *pt_LaTex = pt->AddText("W-2");
   pt->Draw();
   
   pt = new TPaveText(0.08,0.94,0.45,0.94,"brNDC");
   pt->SetBorderSize(0);
   pt->SetFillStyle(0);
   pt->SetTextSize(0.04);
   pt_LaTex = pt->AddText("CMS Preliminary");
   pt->Draw();
   
   pt = new TPaveText(0.7,0.94,0.9,0.94,"brNDC");
   pt->SetBorderSize(0);
   pt->SetFillStyle(0);
   pt->SetTextSize(0.03);
   pt_LaTex = pt->AddText("1.5 #times 10^{34} Hz/cm^{2} (13 TeV)");
   pt->Draw();
   
   TLegend *leg = new TLegend(0.25,0.8,0.75,0.85,NULL,"brNDC");
   leg->SetBorderSize(0);
   leg->SetTextSize(0.03);
   leg->SetLineColor(1);
   leg->SetLineStyle(1);
   leg->SetLineWidth(1);
   leg->SetFillColor(0);
   leg->SetFillStyle(1001);
   TLegendEntry *entry=leg->AddEntry("Graph","RB1","p");
   entry->SetLineColor(1);
   entry->SetLineStyle(1);
   entry->SetLineWidth(1);
   entry->SetMarkerColor(2);
   entry->SetMarkerStyle(26);
   entry->SetMarkerSize(1.5);
   entry->SetTextFont(42);
   entry=leg->AddEntry("Graph","RB2","p");
   entry->SetLineColor(1);
   entry->SetLineStyle(1);
   entry->SetLineWidth(1);
   entry->SetMarkerColor(2);
   entry->SetMarkerStyle(20);
   entry->SetMarkerSize(1.5);
   entry->SetTextFont(42);
   entry=leg->AddEntry("Graph","RB3","p");
   entry->SetLineColor(1);
   entry->SetLineStyle(1);
   entry->SetLineWidth(1);
   entry->SetMarkerColor(2);
   entry->SetMarkerStyle(25);
   entry->SetMarkerSize(1.5);
   entry->SetTextFont(42);
   entry=leg->AddEntry("Graph","RB4","p");
   entry->SetLineColor(1);
   entry->SetLineStyle(1);
   entry->SetLineWidth(1);
   entry->SetMarkerColor(2);
   entry->SetMarkerStyle(23);
   entry->SetMarkerSize(1.5);
   entry->SetTextFont(42);
   leg->Draw();
   c->Modified();
   c->cd();
   c->SetSelected(c);
}
