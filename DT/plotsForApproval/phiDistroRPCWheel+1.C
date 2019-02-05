void phiDistroRPCWheel+1()
{
//=========Macro generated from canvas: c/Canvas
//=========  (Tue Jan 22 21:37:47 2019) by ROOT version 6.12/04
   TCanvas *c = new TCanvas("c", "Canvas",0,45,800,775);
   c->SetHighLightColor(2);
   c->Range(-104.9825,0.161229,380.5146,1.50077);
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
   multigraph->SetTitle("W+1");
   
   Double_t Graph_fx13[12] = {
   149.691,
   179.6909,
   89.69093,
   123.951,
   33.95099,
   63.95099,
   3.950962,
   213.951,
   248.211,
   299.691,
   273.951,
   333.951};
   Double_t Graph_fy13[12] = {
   7.333333,
   4,
   6,
   4,
   5.5,
   2.75,
   6.25,
   5.5,
   8,
   6.666667,
   4.5,
   4.5};
   TGraph *graph = new TGraph(12,Graph_fx13,Graph_fy13);
   graph->SetName("Graph");
   graph->SetTitle("W+1_RB1");
   graph->SetFillStyle(1000);
   graph->SetLineColor(5);
   graph->SetLineWidth(7);
   graph->SetMarkerColor(2);
   graph->SetMarkerStyle(26);
   graph->SetMarkerSize(1.5);
   
   TH1F *Graph_Graph13 = new TH1F("Graph_Graph13","W+1_RB1",100,0,366.951);
   Graph_Graph13->SetMinimum(2.225);
   Graph_Graph13->SetMaximum(8.525);
   Graph_Graph13->SetDirectory(0);
   Graph_Graph13->SetStats(0);

   Int_t ci;      // for color index setting
   TColor *color; // for color definition with alpha
   ci = TColor::GetColor("#000099");
   Graph_Graph13->SetLineColor(ci);
   Graph_Graph13->GetXaxis()->SetTitle("#phi");
   Graph_Graph13->GetXaxis()->SetLabelFont(42);
   Graph_Graph13->GetXaxis()->SetLabelSize(0.035);
   Graph_Graph13->GetXaxis()->SetTitleSize(0.035);
   Graph_Graph13->GetXaxis()->SetTitleFont(42);
   Graph_Graph13->GetYaxis()->SetTitle("RPC single hit rate (Hz/cm^{2})");
   Graph_Graph13->GetYaxis()->SetLabelFont(42);
   Graph_Graph13->GetYaxis()->SetLabelSize(0.035);
   Graph_Graph13->GetYaxis()->SetTitleSize(0.035);
   Graph_Graph13->GetYaxis()->SetTitleOffset(0);
   Graph_Graph13->GetYaxis()->SetTitleFont(42);
   Graph_Graph13->GetZaxis()->SetLabelFont(42);
   Graph_Graph13->GetZaxis()->SetLabelSize(0.035);
   Graph_Graph13->GetZaxis()->SetTitleSize(0.035);
   Graph_Graph13->GetZaxis()->SetTitleFont(42);
   graph->SetHistogram(Graph_Graph13);
   
   multigraph->Add(graph,"AP");
   
   Double_t Graph_fx14[12] = {
   324.9678,
   292.6195,
   267.3161,
   204.9679,
   234.9678,
   -5.032163,
   32.0128,
   54.96784,
   82.61953,
   114.9679,
   142.6195,
   172.6195};
   Double_t Graph_fy14[12] = {
   4.75,
   5,
   5,
   5.75,
   7.5,
   5,
   4,
   5,
   5.333333,
   7.75,
   7,
   6};
   graph = new TGraph(12,Graph_fx14,Graph_fy14);
   graph->SetName("Graph");
   graph->SetTitle("W+1_RB3");
   graph->SetFillStyle(1000);
   graph->SetLineColor(5);
   graph->SetLineWidth(7);
   graph->SetMarkerColor(2);
   graph->SetMarkerStyle(20);
   graph->SetMarkerSize(1.5);
   
   TH1F *Graph_Graph14 = new TH1F("Graph_Graph14","W+1_RB3",100,-38.03216,357.9678);
   Graph_Graph14->SetMinimum(3.625);
   Graph_Graph14->SetMaximum(8.125);
   Graph_Graph14->SetDirectory(0);
   Graph_Graph14->SetStats(0);

   ci = TColor::GetColor("#000099");
   Graph_Graph14->SetLineColor(ci);
   Graph_Graph14->GetXaxis()->SetTitle("#phi");
   Graph_Graph14->GetXaxis()->SetLabelFont(42);
   Graph_Graph14->GetXaxis()->SetLabelSize(0.035);
   Graph_Graph14->GetXaxis()->SetTitleSize(0.035);
   Graph_Graph14->GetXaxis()->SetTitleFont(42);
   Graph_Graph14->GetYaxis()->SetTitle("RPC single hit rate (Hz/cm^{2})");
   Graph_Graph14->GetYaxis()->SetLabelFont(42);
   Graph_Graph14->GetYaxis()->SetLabelSize(0.035);
   Graph_Graph14->GetYaxis()->SetTitleSize(0.035);
   Graph_Graph14->GetYaxis()->SetTitleOffset(0);
   Graph_Graph14->GetYaxis()->SetTitleFont(42);
   Graph_Graph14->GetZaxis()->SetLabelFont(42);
   Graph_Graph14->GetZaxis()->SetLabelSize(0.035);
   Graph_Graph14->GetZaxis()->SetTitleSize(0.035);
   Graph_Graph14->GetZaxis()->SetTitleFont(42);
   graph->SetHistogram(Graph_Graph14);
   
   multigraph->Add(graph,"AP");
   
   Double_t Graph_fx15[12] = {
   290.8761,
   24.91773,
   234.9178,
   117.6121,
   207.6121,
   101.0841,
   -9.123835,
   50.87616,
   170.8762,
   140.8762,
   267.6121,
   327.6121};
   Double_t Graph_fy15[12] = {
   4.75,
   5.4,
   4,
   4.75,
   7,
   6,
   6.75,
   4.75,
   6.75,
   5.5,
   4.75,
   4.5};
   graph = new TGraph(12,Graph_fx15,Graph_fy15);
   graph->SetName("Graph");
   graph->SetTitle("W+1_RB2");
   graph->SetFillStyle(1000);
   graph->SetLineColor(5);
   graph->SetLineWidth(7);
   graph->SetMarkerColor(2);
   graph->SetMarkerStyle(25);
   graph->SetMarkerSize(1.5);
   
   TH1F *Graph_Graph15 = new TH1F("Graph_Graph15","W+1_RB2",100,-42.79743,361.2857);
   Graph_Graph15->SetMinimum(3.7);
   Graph_Graph15->SetMaximum(7.3);
   Graph_Graph15->SetDirectory(0);
   Graph_Graph15->SetStats(0);

   ci = TColor::GetColor("#000099");
   Graph_Graph15->SetLineColor(ci);
   Graph_Graph15->GetXaxis()->SetTitle("#phi");
   Graph_Graph15->GetXaxis()->SetLabelFont(42);
   Graph_Graph15->GetXaxis()->SetLabelSize(0.035);
   Graph_Graph15->GetXaxis()->SetTitleSize(0.035);
   Graph_Graph15->GetXaxis()->SetTitleFont(42);
   Graph_Graph15->GetYaxis()->SetTitle("RPC single hit rate (Hz/cm^{2})");
   Graph_Graph15->GetYaxis()->SetLabelFont(42);
   Graph_Graph15->GetYaxis()->SetLabelSize(0.035);
   Graph_Graph15->GetYaxis()->SetTitleSize(0.035);
   Graph_Graph15->GetYaxis()->SetTitleOffset(0);
   Graph_Graph15->GetYaxis()->SetTitleFont(42);
   Graph_Graph15->GetZaxis()->SetLabelFont(42);
   Graph_Graph15->GetZaxis()->SetLabelSize(0.035);
   Graph_Graph15->GetZaxis()->SetTitleSize(0.035);
   Graph_Graph15->GetZaxis()->SetTitleFont(42);
   graph->SetHistogram(Graph_Graph15);
   
   multigraph->Add(graph,"AP");
   
   Double_t Graph_fx16[11] = {
   291.7188,
   -14.72417,
   232.6706,
   212.2748,
   15.27587,
   42.75797,
   179.5825,
   149.5825,
   116.8899,
   260.512,
   318.9822};
   Double_t Graph_fy16[11] = {
   4,
   4.75,
   5.5,
   7.666667,
   6,
   3.666667,
   6.5,
   4.75,
   4.666667,
   5.25,
   7.333333};
   graph = new TGraph(11,Graph_fx16,Graph_fy16);
   graph->SetName("Graph");
   graph->SetTitle("W+1_RB4");
   graph->SetFillStyle(1000);
   graph->SetLineColor(5);
   graph->SetLineWidth(7);
   graph->SetMarkerColor(2);
   graph->SetMarkerStyle(23);
   graph->SetMarkerSize(1.5);
   
   TH1F *Graph_Graph16 = new TH1F("Graph_Graph16","W+1_RB4",100,-48.09481,352.3529);
   Graph_Graph16->SetMinimum(3.266667);
   Graph_Graph16->SetMaximum(8.066667);
   Graph_Graph16->SetDirectory(0);
   Graph_Graph16->SetStats(0);

   ci = TColor::GetColor("#000099");
   Graph_Graph16->SetLineColor(ci);
   Graph_Graph16->GetXaxis()->SetTitle("#phi");
   Graph_Graph16->GetXaxis()->SetLabelFont(42);
   Graph_Graph16->GetXaxis()->SetLabelSize(0.035);
   Graph_Graph16->GetXaxis()->SetTitleSize(0.035);
   Graph_Graph16->GetXaxis()->SetTitleFont(42);
   Graph_Graph16->GetYaxis()->SetTitle("RPC single hit rate (Hz/cm^{2})");
   Graph_Graph16->GetYaxis()->SetLabelFont(42);
   Graph_Graph16->GetYaxis()->SetLabelSize(0.035);
   Graph_Graph16->GetYaxis()->SetTitleSize(0.035);
   Graph_Graph16->GetYaxis()->SetTitleOffset(0);
   Graph_Graph16->GetYaxis()->SetTitleFont(42);
   Graph_Graph16->GetZaxis()->SetLabelFont(42);
   Graph_Graph16->GetZaxis()->SetLabelSize(0.035);
   Graph_Graph16->GetZaxis()->SetTitleSize(0.035);
   Graph_Graph16->GetZaxis()->SetTitleFont(42);
   graph->SetHistogram(Graph_Graph16);
   
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
   TText *pt_LaTex = pt->AddText("W+1");
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
