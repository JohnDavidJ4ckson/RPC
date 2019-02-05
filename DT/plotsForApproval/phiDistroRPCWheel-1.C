void phiDistroRPCWheel-1()
{
//=========Macro generated from canvas: c/Canvas
//=========  (Tue Jan 22 21:37:44 2019) by ROOT version 6.12/04
   TCanvas *c = new TCanvas("c", "Canvas",0,45,800,775);
   c->SetHighLightColor(2);
   c->Range(-84.13314,0.203494,384.4616,1.525523);
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
   multigraph->SetTitle("W-1");
   
   Double_t Graph_fx5[7] = {
   279.488,
   307.3294,
   8.49541,
   63.11011,
   82.89442,
   167.242,
   327.7252};
   Double_t Graph_fy5[7] = {
   3.5,
   6,
   5,
   6,
   4.75,
   3.666667,
   4.666667};
   TGraph *graph = new TGraph(7,Graph_fx5,Graph_fy5);
   graph->SetName("Graph");
   graph->SetTitle("W-1_RB4");
   graph->SetFillStyle(1000);
   graph->SetLineColor(5);
   graph->SetLineWidth(7);
   graph->SetMarkerColor(2);
   graph->SetMarkerStyle(26);
   graph->SetMarkerSize(1.5);
   
   TH1F *Graph_Graph5 = new TH1F("Graph_Graph5","W-1_RB4",100,0,359.6482);
   Graph_Graph5->SetMinimum(3.25);
   Graph_Graph5->SetMaximum(6.25);
   Graph_Graph5->SetDirectory(0);
   Graph_Graph5->SetStats(0);

   Int_t ci;      // for color index setting
   TColor *color; // for color definition with alpha
   ci = TColor::GetColor("#000099");
   Graph_Graph5->SetLineColor(ci);
   Graph_Graph5->GetXaxis()->SetTitle("#phi");
   Graph_Graph5->GetXaxis()->SetLabelFont(42);
   Graph_Graph5->GetXaxis()->SetLabelSize(0.035);
   Graph_Graph5->GetXaxis()->SetTitleSize(0.035);
   Graph_Graph5->GetXaxis()->SetTitleFont(42);
   Graph_Graph5->GetYaxis()->SetTitle("RPC single hit rate (Hz/cm^{2})");
   Graph_Graph5->GetYaxis()->SetLabelFont(42);
   Graph_Graph5->GetYaxis()->SetLabelSize(0.035);
   Graph_Graph5->GetYaxis()->SetTitleSize(0.035);
   Graph_Graph5->GetYaxis()->SetTitleOffset(0);
   Graph_Graph5->GetYaxis()->SetTitleFont(42);
   Graph_Graph5->GetZaxis()->SetLabelFont(42);
   Graph_Graph5->GetZaxis()->SetLabelSize(0.035);
   Graph_Graph5->GetZaxis()->SetTitleSize(0.035);
   Graph_Graph5->GetZaxis()->SetTitleFont(42);
   graph->SetHistogram(Graph_Graph5);
   
   multigraph->Add(graph,"AP");
   
   Double_t Graph_fx6[11] = {
   315.3804,
   276.1186,
   331.4877,
   218.434,
   250.7495,
   40.7495,
   70.74949,
   160.7495,
   186.1186,
   91.48766,
   128.434};
   Double_t Graph_fy6[11] = {
   3,
   7.666667,
   4,
   5,
   3.666667,
   4.666667,
   7.333333,
   6.333333,
   4.333333,
   4.5,
   7.5};
   graph = new TGraph(11,Graph_fx6,Graph_fy6);
   graph->SetName("Graph");
   graph->SetTitle("W-1_RB3");
   graph->SetFillStyle(1000);
   graph->SetLineColor(5);
   graph->SetLineWidth(7);
   graph->SetMarkerColor(2);
   graph->SetMarkerStyle(20);
   graph->SetMarkerSize(1.5);
   
   TH1F *Graph_Graph6 = new TH1F("Graph_Graph6","W-1_RB3",100,11.67569,360.5615);
   Graph_Graph6->SetMinimum(2.533333);
   Graph_Graph6->SetMaximum(8.133333);
   Graph_Graph6->SetDirectory(0);
   Graph_Graph6->SetStats(0);

   ci = TColor::GetColor("#000099");
   Graph_Graph6->SetLineColor(ci);
   Graph_Graph6->GetXaxis()->SetTitle("#phi");
   Graph_Graph6->GetXaxis()->SetLabelFont(42);
   Graph_Graph6->GetXaxis()->SetLabelSize(0.035);
   Graph_Graph6->GetXaxis()->SetTitleSize(0.035);
   Graph_Graph6->GetXaxis()->SetTitleFont(42);
   Graph_Graph6->GetYaxis()->SetTitle("RPC single hit rate (Hz/cm^{2})");
   Graph_Graph6->GetYaxis()->SetLabelFont(42);
   Graph_Graph6->GetYaxis()->SetLabelSize(0.035);
   Graph_Graph6->GetYaxis()->SetTitleSize(0.035);
   Graph_Graph6->GetYaxis()->SetTitleOffset(0);
   Graph_Graph6->GetYaxis()->SetTitleFont(42);
   Graph_Graph6->GetZaxis()->SetLabelFont(42);
   Graph_Graph6->GetZaxis()->SetLabelSize(0.035);
   Graph_Graph6->GetZaxis()->SetTitleSize(0.035);
   Graph_Graph6->GetZaxis()->SetTitleFont(42);
   graph->SetHistogram(Graph_Graph6);
   
   multigraph->Add(graph,"AP");
   
   Double_t Graph_fx7[12] = {
   268.5069,
   298.5069,
   328.5069,
   238.5069,
   221.9349,
   54.03093,
   31.19249,
   2.982877,
   191.9348,
   151.1925,
   114.0309,
   101.9348};
   Double_t Graph_fy7[12] = {
   6.5,
   5.75,
   4.75,
   3.75,
   5.5,
   4.333333,
   4.2,
   6.333333,
   6.666667,
   5.6,
   4.333333,
   8.5};
   graph = new TGraph(12,Graph_fx7,Graph_fy7);
   graph->SetName("Graph");
   graph->SetTitle("W-1_RB2");
   graph->SetFillStyle(1000);
   graph->SetLineColor(5);
   graph->SetLineWidth(7);
   graph->SetMarkerColor(2);
   graph->SetMarkerStyle(25);
   graph->SetMarkerSize(1.5);
   
   TH1F *Graph_Graph7 = new TH1F("Graph_Graph7","W-1_RB2",100,0,361.0593);
   Graph_Graph7->SetMinimum(3.275);
   Graph_Graph7->SetMaximum(8.975);
   Graph_Graph7->SetDirectory(0);
   Graph_Graph7->SetStats(0);

   ci = TColor::GetColor("#000099");
   Graph_Graph7->SetLineColor(ci);
   Graph_Graph7->GetXaxis()->SetTitle("#phi");
   Graph_Graph7->GetXaxis()->SetLabelFont(42);
   Graph_Graph7->GetXaxis()->SetLabelSize(0.035);
   Graph_Graph7->GetXaxis()->SetTitleSize(0.035);
   Graph_Graph7->GetXaxis()->SetTitleFont(42);
   Graph_Graph7->GetYaxis()->SetTitle("RPC single hit rate (Hz/cm^{2})");
   Graph_Graph7->GetYaxis()->SetLabelFont(42);
   Graph_Graph7->GetYaxis()->SetLabelSize(0.035);
   Graph_Graph7->GetYaxis()->SetTitleSize(0.035);
   Graph_Graph7->GetYaxis()->SetTitleOffset(0);
   Graph_Graph7->GetYaxis()->SetTitleFont(42);
   Graph_Graph7->GetZaxis()->SetLabelFont(42);
   Graph_Graph7->GetZaxis()->SetLabelSize(0.035);
   Graph_Graph7->GetZaxis()->SetTitleSize(0.035);
   Graph_Graph7->GetZaxis()->SetTitleFont(42);
   graph->SetHistogram(Graph_Graph7);
   
   multigraph->Add(graph,"AP");
   
   Double_t Graph_fx8[12] = {
   309.5191,
   274.9638,
   210.4085,
   244.9638,
   94.96381,
   124.9638,
   141.2979,
   184.9638,
   4.963811,
   34.9638,
   64.96377,
   339.5191};
   Double_t Graph_fy8[12] = {
   7.333333,
   4.5,
   4.333333,
   6,
   4.5,
   4.25,
   6,
   5.75,
   5.25,
   4,
   5.5,
   4.666667};
   graph = new TGraph(12,Graph_fx8,Graph_fy8);
   graph->SetName("Graph");
   graph->SetTitle("W-1_RB1");
   graph->SetFillStyle(1000);
   graph->SetLineColor(5);
   graph->SetLineWidth(7);
   graph->SetMarkerColor(2);
   graph->SetMarkerStyle(23);
   graph->SetMarkerSize(1.5);
   
   TH1F *Graph_Graph8 = new TH1F("Graph_Graph8","W-1_RB1",100,0,372.9746);
   Graph_Graph8->SetMinimum(3.666667);
   Graph_Graph8->SetMaximum(7.666667);
   Graph_Graph8->SetDirectory(0);
   Graph_Graph8->SetStats(0);

   ci = TColor::GetColor("#000099");
   Graph_Graph8->SetLineColor(ci);
   Graph_Graph8->GetXaxis()->SetTitle("#phi");
   Graph_Graph8->GetXaxis()->SetLabelFont(42);
   Graph_Graph8->GetXaxis()->SetLabelSize(0.035);
   Graph_Graph8->GetXaxis()->SetTitleSize(0.035);
   Graph_Graph8->GetXaxis()->SetTitleFont(42);
   Graph_Graph8->GetYaxis()->SetTitle("RPC single hit rate (Hz/cm^{2})");
   Graph_Graph8->GetYaxis()->SetLabelFont(42);
   Graph_Graph8->GetYaxis()->SetLabelSize(0.035);
   Graph_Graph8->GetYaxis()->SetTitleSize(0.035);
   Graph_Graph8->GetYaxis()->SetTitleOffset(0);
   Graph_Graph8->GetYaxis()->SetTitleFont(42);
   Graph_Graph8->GetZaxis()->SetLabelFont(42);
   Graph_Graph8->GetZaxis()->SetLabelSize(0.035);
   Graph_Graph8->GetZaxis()->SetTitleSize(0.035);
   Graph_Graph8->GetZaxis()->SetTitleFont(42);
   graph->SetHistogram(Graph_Graph8);
   
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
   TText *pt_LaTex = pt->AddText("W-1");
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
