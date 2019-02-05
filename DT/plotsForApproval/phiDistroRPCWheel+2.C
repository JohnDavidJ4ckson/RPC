void phiDistroRPCWheel+2()
{
//=========Macro generated from canvas: c/Canvas
//=========  (Tue Jan 22 21:37:48 2019) by ROOT version 6.12/04
   TCanvas *c = new TCanvas("c", "Canvas",0,45,800,775);
   c->SetHighLightColor(2);
   c->Range(-109.2549,-0.0302516,385.6797,1.519708);
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
   multigraph->SetTitle("W+2");
   
   Double_t Graph_fx17[12] = {
   300.3065,
   267.6121,
   -2.387865,
   152.1028,
   184.3481,
   94.34811,
   117.6121,
   23.12147,
   60.30654,
   323.1215,
   207.6121,
   240.3065};
   Double_t Graph_fy17[12] = {
   6.8,
   3,
   7,
   5.333333,
   5.25,
   7.5,
   4,
   7.333333,
   6,
   7.666667,
   6,
   4.8};
   TGraph *graph = new TGraph(12,Graph_fx17,Graph_fy17);
   graph->SetName("Graph");
   graph->SetTitle("W+2_RB2");
   graph->SetFillStyle(1000);
   graph->SetLineColor(5);
   graph->SetLineWidth(7);
   graph->SetMarkerColor(2);
   graph->SetMarkerStyle(26);
   graph->SetMarkerSize(1.5);
   
   TH1F *Graph_Graph17 = new TH1F("Graph_Graph17","W+2_RB2",100,-34.9388,355.6724);
   Graph_Graph17->SetMinimum(2.533333);
   Graph_Graph17->SetMaximum(8.133333);
   Graph_Graph17->SetDirectory(0);
   Graph_Graph17->SetStats(0);

   Int_t ci;      // for color index setting
   TColor *color; // for color definition with alpha
   ci = TColor::GetColor("#000099");
   Graph_Graph17->SetLineColor(ci);
   Graph_Graph17->GetXaxis()->SetTitle("#phi");
   Graph_Graph17->GetXaxis()->SetLabelFont(42);
   Graph_Graph17->GetXaxis()->SetLabelSize(0.035);
   Graph_Graph17->GetXaxis()->SetTitleSize(0.035);
   Graph_Graph17->GetXaxis()->SetTitleFont(42);
   Graph_Graph17->GetYaxis()->SetTitle("RPC single hit rate (Hz/cm^{2})");
   Graph_Graph17->GetYaxis()->SetLabelFont(42);
   Graph_Graph17->GetYaxis()->SetLabelSize(0.035);
   Graph_Graph17->GetYaxis()->SetTitleSize(0.035);
   Graph_Graph17->GetYaxis()->SetTitleOffset(0);
   Graph_Graph17->GetYaxis()->SetTitleFont(42);
   Graph_Graph17->GetZaxis()->SetLabelFont(42);
   Graph_Graph17->GetZaxis()->SetLabelSize(0.035);
   Graph_Graph17->GetZaxis()->SetTitleSize(0.035);
   Graph_Graph17->GetZaxis()->SetTitleFont(42);
   graph->SetHistogram(Graph_Graph17);
   
   multigraph->Add(graph,"AP");
   
   Double_t Graph_fx18[12] = {
   303.951,
   8.21099,
   63.95099,
   33.95099,
   119.691,
   188.211,
   243.951,
   213.951,
   269.6909,
   89.69093,
   153.951,
   338.211};
   Double_t Graph_fy18[12] = {
   6.25,
   7,
   6,
   5.75,
   6,
   4,
   5.25,
   3.75,
   5,
   4,
   6,
   6};
   graph = new TGraph(12,Graph_fx18,Graph_fy18);
   graph->SetName("Graph");
   graph->SetTitle("W+2_RB1");
   graph->SetFillStyle(1000);
   graph->SetLineColor(5);
   graph->SetLineWidth(7);
   graph->SetMarkerColor(2);
   graph->SetMarkerStyle(20);
   graph->SetMarkerSize(1.5);
   
   TH1F *Graph_Graph18 = new TH1F("Graph_Graph18","W+2_RB1",100,0,371.211);
   Graph_Graph18->SetMinimum(3.425);
   Graph_Graph18->SetMaximum(7.325);
   Graph_Graph18->SetDirectory(0);
   Graph_Graph18->SetStats(0);

   ci = TColor::GetColor("#000099");
   Graph_Graph18->SetLineColor(ci);
   Graph_Graph18->GetXaxis()->SetTitle("#phi");
   Graph_Graph18->GetXaxis()->SetLabelFont(42);
   Graph_Graph18->GetXaxis()->SetLabelSize(0.035);
   Graph_Graph18->GetXaxis()->SetTitleSize(0.035);
   Graph_Graph18->GetXaxis()->SetTitleFont(42);
   Graph_Graph18->GetYaxis()->SetTitle("RPC single hit rate (Hz/cm^{2})");
   Graph_Graph18->GetYaxis()->SetLabelFont(42);
   Graph_Graph18->GetYaxis()->SetLabelSize(0.035);
   Graph_Graph18->GetYaxis()->SetTitleSize(0.035);
   Graph_Graph18->GetYaxis()->SetTitleOffset(0);
   Graph_Graph18->GetYaxis()->SetTitleFont(42);
   Graph_Graph18->GetZaxis()->SetLabelFont(42);
   Graph_Graph18->GetZaxis()->SetLabelSize(0.035);
   Graph_Graph18->GetZaxis()->SetTitleSize(0.035);
   Graph_Graph18->GetZaxis()->SetTitleFont(42);
   graph->SetHistogram(Graph_Graph18);
   
   multigraph->Add(graph,"AP");
   
   Double_t Graph_fx19[12] = {
   302.0128,
   264.9678,
   232.6195,
   204.9679,
   114.9679,
   57.31615,
   24.96786,
   -5.032163,
   332.0128,
   174.9678,
   152.0128,
   87.31615};
   Double_t Graph_fy19[12] = {
   8,
   6.5,
   4,
   4.5,
   6.5,
   8,
   6.25,
   5.5,
   5.5,
   5.5,
   6,
   6};
   graph = new TGraph(12,Graph_fx19,Graph_fy19);
   graph->SetName("Graph");
   graph->SetTitle("W+2_RB3");
   graph->SetFillStyle(1000);
   graph->SetLineColor(5);
   graph->SetLineWidth(7);
   graph->SetMarkerColor(2);
   graph->SetMarkerStyle(25);
   graph->SetMarkerSize(1.5);
   
   TH1F *Graph_Graph19 = new TH1F("Graph_Graph19","W+2_RB3",100,-38.73666,365.7173);
   Graph_Graph19->SetMinimum(3.6);
   Graph_Graph19->SetMaximum(8.4);
   Graph_Graph19->SetDirectory(0);
   Graph_Graph19->SetStats(0);

   ci = TColor::GetColor("#000099");
   Graph_Graph19->SetLineColor(ci);
   Graph_Graph19->GetXaxis()->SetTitle("#phi");
   Graph_Graph19->GetXaxis()->SetLabelFont(42);
   Graph_Graph19->GetXaxis()->SetLabelSize(0.035);
   Graph_Graph19->GetXaxis()->SetTitleSize(0.035);
   Graph_Graph19->GetXaxis()->SetTitleFont(42);
   Graph_Graph19->GetYaxis()->SetTitle("RPC single hit rate (Hz/cm^{2})");
   Graph_Graph19->GetYaxis()->SetLabelFont(42);
   Graph_Graph19->GetYaxis()->SetLabelSize(0.035);
   Graph_Graph19->GetYaxis()->SetTitleSize(0.035);
   Graph_Graph19->GetYaxis()->SetTitleOffset(0);
   Graph_Graph19->GetYaxis()->SetTitleFont(42);
   Graph_Graph19->GetZaxis()->SetLabelFont(42);
   Graph_Graph19->GetZaxis()->SetLabelSize(0.035);
   Graph_Graph19->GetZaxis()->SetTitleSize(0.035);
   Graph_Graph19->GetZaxis()->SetTitleFont(42);
   graph->SetHistogram(Graph_Graph19);
   
   multigraph->Add(graph,"AP");
   
   Double_t Graph_fx20[10] = {
   17.79374,
   232.6706,
   318.9822,
   84.50074,
   127.6604,
   149.5825,
   179.5825,
   -17.24204,
   45.27584,
   257.0032};
   Double_t Graph_fy20[10] = {
   4.333333,
   2,
   7,
   4.875,
   3.5,
   5,
   5.5,
   5,
   3.5,
   7};
   graph = new TGraph(10,Graph_fx20,Graph_fy20);
   graph->SetName("Graph");
   graph->SetTitle("W+2_RB4");
   graph->SetFillStyle(1000);
   graph->SetLineColor(5);
   graph->SetLineWidth(7);
   graph->SetMarkerColor(2);
   graph->SetMarkerStyle(23);
   graph->SetMarkerSize(1.5);
   
   TH1F *Graph_Graph20 = new TH1F("Graph_Graph20","W+2_RB4",100,-50.86447,352.6047);
   Graph_Graph20->SetMinimum(1.5);
   Graph_Graph20->SetMaximum(7.5);
   Graph_Graph20->SetDirectory(0);
   Graph_Graph20->SetStats(0);

   ci = TColor::GetColor("#000099");
   Graph_Graph20->SetLineColor(ci);
   Graph_Graph20->GetXaxis()->SetTitle("#phi");
   Graph_Graph20->GetXaxis()->SetLabelFont(42);
   Graph_Graph20->GetXaxis()->SetLabelSize(0.035);
   Graph_Graph20->GetXaxis()->SetTitleSize(0.035);
   Graph_Graph20->GetXaxis()->SetTitleFont(42);
   Graph_Graph20->GetYaxis()->SetTitle("RPC single hit rate (Hz/cm^{2})");
   Graph_Graph20->GetYaxis()->SetLabelFont(42);
   Graph_Graph20->GetYaxis()->SetLabelSize(0.035);
   Graph_Graph20->GetYaxis()->SetTitleSize(0.035);
   Graph_Graph20->GetYaxis()->SetTitleOffset(0);
   Graph_Graph20->GetYaxis()->SetTitleFont(42);
   Graph_Graph20->GetZaxis()->SetLabelFont(42);
   Graph_Graph20->GetZaxis()->SetLabelSize(0.035);
   Graph_Graph20->GetZaxis()->SetTitleSize(0.035);
   Graph_Graph20->GetZaxis()->SetTitleFont(42);
   graph->SetHistogram(Graph_Graph20);
   
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
   
   TPaveText *pt = new TPaveText(0.4405013,0.94,0.5594987,0.995,"blNDC");
   pt->SetName("title");
   pt->SetBorderSize(0);
   pt->SetFillColor(0);
   pt->SetFillStyle(0);
   pt->SetTextFont(42);
   TText *pt_LaTex = pt->AddText("W+2");
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
