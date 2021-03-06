import ROOT
import sys
argv = sys.argv
sys.argv = argv[:1]
import optparse

if __name__ == '__main__':
    
    sys.argv = argv

    usage = 'usage: %prog [options]'
    parser = optparse.OptionParser(usage)

    parser.add_option('--cut'       , dest='cut'        , help='type of cut'            , default='jv')
    parser.add_option('--dynamic'   , dest='dynamic'    , help='dynamic cut variable'   , default='mjj')

    (opt, args) = parser.parse_args()
    
    print ''
    print '                 cut =', opt.cut
    print '             dynamic =', opt.dynamic
    print ''
    
    f = ROOT.TFile('latino_WpWpJJ_EWK.root')
    t = f.Get('latino')

    presel = '(abs(std_vector_jet_eta[1])<5 && abs(std_vector_jet_eta[0])<5 \
    && metPfType1 > 30 \
    && std_vector_jet_pt[0]>30 && std_vector_jet_pt[1]>30 \
    && (abs((std_vector_lepton_eta[0] - (std_vector_jet_eta[0]+std_vector_jet_eta[1])/2)/detajj) < 0.5) \
    && (abs((std_vector_lepton_eta[1] - (std_vector_jet_eta[0]+std_vector_jet_eta[1])/2)/detajj) < 0.5) \
    && (std_vector_lepton_flavour[0] * std_vector_lepton_flavour[1]) > 0 \
    && veto_EMTFBug)'

    weights = '(baseW*GEN_weight_SM/abs(GEN_weight_SM)*puW*effTrigW \
    *bPogSF_CSVM*std_vector_lepton_recoW[0]*std_vector_lepton_recoW[1] \
    *std_vector_lepton_idisoWcut_WP_Tight80X[0]*std_vector_lepton_idisoWcut_WP_Tight80X[1] \
    *std_vector_lepton_promptgenmatched[0]*std_vector_lepton_promptgenmatched[1]*(std_vector_trigger_special[0] \
    *std_vector_trigger_special[1]*std_vector_trigger_special[2]*std_vector_trigger_special[3] \
    *std_vector_trigger_special[5])*(((std_vector_trigger_special[8]==-2.)*(std_vector_trigger_special[6] \
    *std_vector_trigger_special[7])) || ((! (std_vector_trigger_special[8]==-2.))*(std_vector_trigger_special[8] \
    *std_vector_trigger_special[9])))*((std_vector_lepton_flavour[0] * std_vector_lepton_flavour[1])>0)*1.067466)'
    
    ptcond = '(std_vector_jet_pt[2]>=20)'

    hN = ROOT.TH1F('hN', '', 3, -0.5, 2.5)
    hD = ROOT.TH1F('hD', '', 3, -0.5, 2.5)
    efficiencies = ROOT.TGraphAsymmErrors()
    efficiencies.SetName('efficiencies')
    efficiencies_norm = ROOT.TGraphAsymmErrors()
    efficiencies_norm.SetName('efficiencies_norm')
    numerator0 = ROOT.TGraph()
    numerator0.SetName('numerator0')
    denominator0 = ROOT.TGraph()
    denominator0.SetName('denominator0')
    numerator1 = ROOT.TGraph()
    numerator1.SetName('numerator1')
    denominator1 = ROOT.TGraph()
    denominator1.SetName('denominator1')
    numerator2 = ROOT.TGraph()
    numerator2.SetName('numerator2')
    denominator2 = ROOT.TGraph()
    denominator2.SetName('denominator2')
    numerator3 = ROOT.TGraph()
    numerator3.SetName('numerator3')
    denominator3 = ROOT.TGraph()
    denominator3.SetName('denominator3')
    numerator4 = ROOT.TGraph()
    numerator4.SetName('numerator4')
    denominator4 = ROOT.TGraph()
    denominator4.SetName('denominator4')
    numerator6 = ROOT.TGraph()
    numerator6.SetName('numerator6')
    denominator6 = ROOT.TGraph()
    denominator6.SetName('denominator6')
    numerator8 = ROOT.TGraph()
    numerator8.SetName('numerator8')
    denominator8 = ROOT.TGraph()
    denominator8.SetName('denominator8')
    
    if (opt.cut == 'jv') or (opt.cut == 'cjv'):
        start = 21
    else:
        start = 0
    #if opt.cut == 'dcjv':
        #end = 115
    #else:
        #end = 100
    if (opt.cut == 'djv') or (opt.cut == 'dcjv'):
        start = 10
    end = 100
                
    for i in range (start,end):
        if opt.cut == 'jv':
            x_cut = i
            cut = '(std_vector_jet_pt[2]<{})'.format(x_cut)
        elif opt.cut == 'cjv':
            x_cut = i
            cut = '(std_vector_jet_pt[2]<{} || (std_vector_jet_pt[2]>={} \
            && std_vector_jet_eta[2] <  \
            ((std_vector_jet_eta[0]<std_vector_jet_eta[1])*std_vector_jet_eta[0]+(std_vector_jet_eta[0]>= \
            std_vector_jet_eta[1])*std_vector_jet_eta[1]) || std_vector_jet_eta[2] > \
            ((std_vector_jet_eta[0]<std_vector_jet_eta[1])*std_vector_jet_eta[1]+(std_vector_jet_eta[0]>= \
            std_vector_jet_eta[1])*std_vector_jet_eta[0]) ))'.format(x_cut,x_cut)
        elif opt.cut == 'djv' and opt.dynamic == 'mjj':
            x_cut = i*0.002
            cut = '(std_vector_jet_pt[2]<{}*{})'.format(x_cut,opt.dynamic)
        elif opt.cut == 'djv' and opt.dynamic != 'mjj':
            x_cut = i*0.01
            cut = '(std_vector_jet_pt[2]<{}*{})'.format(x_cut,opt.dynamic)
        elif opt.cut == 'dcjv' and opt.dynamic == 'mjj':
            #if i <= 25:
                #x_cut = i*0.0008
            #else:
                #x_cut = 0.02+(i-25)*0.002
            x_cut = i*0.002
            cut = '(std_vector_jet_pt[2]<{}*{} || (std_vector_jet_pt[2]>={}*{} \
            && std_vector_jet_eta[2] < \
            ((std_vector_jet_eta[0]<std_vector_jet_eta[1])*std_vector_jet_eta[0]+(std_vector_jet_eta[0]>= \
            std_vector_jet_eta[1])*std_vector_jet_eta[1]) || std_vector_jet_eta[2] > \
            ((std_vector_jet_eta[0]<std_vector_jet_eta[1])*std_vector_jet_eta[1]+(std_vector_jet_eta[0]>= \
            std_vector_jet_eta[1])*std_vector_jet_eta[0])))'.format(x_cut,opt.dynamic,x_cut,opt.dynamic)
        elif opt.cut == 'dcjv' and opt.dynamic != 'mjj':
            x_cut = i*0.0086
            cut = '(std_vector_jet_pt[2]<{}*{} || (std_vector_jet_pt[2]>={}*{} \
            && std_vector_jet_eta[2] < \
            ((std_vector_jet_eta[0]<std_vector_jet_eta[1])*std_vector_jet_eta[0]+(std_vector_jet_eta[0]>= \
            std_vector_jet_eta[1])*std_vector_jet_eta[1]) || std_vector_jet_eta[2] > \
            ((std_vector_jet_eta[0]<std_vector_jet_eta[1])*std_vector_jet_eta[1]+(std_vector_jet_eta[0]>= \
            std_vector_jet_eta[1])*std_vector_jet_eta[0])))'.format(x_cut,opt.dynamic,x_cut,opt.dynamic)

        for j in range(0,9):
            if opt.cut == 'djv':
                t.Draw('1 >> hN', presel+'*'+weights+'*'+cut+'*(std_vector_LHE_weight[{}]/std_vector_LHE_weight[0])'.format(j))
                t.Draw('1 >> hD', presel+'*'+weights +'*(std_vector_LHE_weight[{}]/std_vector_LHE_weight[0])'.format(j))
            else:
                t.Draw('1 >> hN', presel+'*'+weights+'*'+cut+'*'+ptcond+'*(std_vector_LHE_weight[{}]/std_vector_LHE_weight[0])'.format(j))
                t.Draw('1 >> hD', presel+'*'+weights +'*'+ptcond+'*(std_vector_LHE_weight[{}]/std_vector_LHE_weight[0])'.format(j))
            efficiency = hN.Integral() / hD.Integral()
            if j == 0:
                eff = efficiency
                effmax = efficiency
                effmin = efficiency
                numerator0.SetPoint(i-start, x_cut, hN.Integral())
                denominator0.SetPoint(i-start, x_cut, hD.Integral())
            elif j == 1:
                numerator1.SetPoint(i-start, x_cut, hN.Integral())
                denominator1.SetPoint(i-start, x_cut, hD.Integral())
            elif j == 2:
                numerator2.SetPoint(i-start, x_cut, hN.Integral())
                denominator2.SetPoint(i-start, x_cut, hD.Integral())
            elif j == 3:
                numerator3.SetPoint(i-start, x_cut, hN.Integral())
                denominator3.SetPoint(i-start, x_cut, hD.Integral())
            elif j == 4:
                numerator4.SetPoint(i-start, x_cut, hN.Integral())
                denominator4.SetPoint(i-start, x_cut, hD.Integral())
            elif j == 6:
                numerator6.SetPoint(i-start, x_cut, hN.Integral())
                denominator6.SetPoint(i-start, x_cut, hD.Integral())
            elif j == 8:
                numerator8.SetPoint(i-start, x_cut, hN.Integral())
                denominator8.SetPoint(i-start, x_cut, hD.Integral())
            if efficiency > effmax:
                effmax = efficiency
            if efficiency < effmin:
                effmin = efficiency
 
        efficiencies.SetPoint(i-start, x_cut, eff)
        efficiencies.SetPointEYlow(i-start, eff-effmin)
        efficiencies.SetPointEYhigh(i-start, effmax-eff)
        efficiencies_norm.SetPoint(i-start, x_cut, 1)
        efficiencies_norm.SetPointEYlow(i-start, (eff-effmin)/eff)
        efficiencies_norm.SetPointEYhigh(i-start, (effmax-eff)/eff)        
        print 'punto #', i-start, '--', eff, effmin, effmax
        if (x_cut < 31 and x_cut > 24) or (x_cut < 0.041 and x_cut > 0.03):
            print 'cut =', x_cut, 'efficiency =', eff, 'error =', 100*max(eff-effmin, effmax-eff)/eff

        
    if opt.cut == 'jv':
        efficiencies.SetFillColor(ROOT.kBlue+2)
        efficiencies_norm.SetLineColor(ROOT.kBlue)
        efficiencies_norm.SetFillColor(ROOT.kBlue+2)
        efficiencies.GetXaxis().SetTitle('p_{t} jet 3 [GeV]')
        efficiencies_norm.GetXaxis().SetTitle('p_{t} jet 3 [GeV]')
    elif opt.cut == 'cjv':
        efficiencies.SetFillColor(ROOT.kRed+1)
        efficiencies_norm.SetLineColor(ROOT.kRed)
        efficiencies_norm.SetFillColor(ROOT.kRed+1)
        efficiencies.GetXaxis().SetTitle('p_{t} jet 3 [GeV]')
        efficiencies_norm.GetXaxis().SetTitle('p_{t} jet 3 [GeV]')
    elif opt.cut == 'djv':
        efficiencies.SetFillColor(ROOT.kGreen+2)
        efficiencies_norm.SetLineColor(ROOT.kGreen)
        efficiencies_norm.SetFillColor(ROOT.kGreen+2)
        efficiencies.GetXaxis().SetTitle('k')
        efficiencies_norm.GetXaxis().SetTitle('k')
    elif opt.cut == 'dcjv':
        efficiencies.SetFillColor(ROOT.kPink-9)
        efficiencies_norm.SetLineColor(ROOT.kPink-8)
        efficiencies_norm.SetFillColor(ROOT.kPink-9)
        efficiencies.GetXaxis().SetTitle('k_{d}')
        efficiencies_norm.GetXaxis().SetTitle('k_{d}')
    
    efficiencies_norm.GetYaxis().SetTitle('Normalized #varepsilon')
    efficiencies.GetXaxis().SetTitleSize(0.04)
    efficiencies_norm.GetXaxis().SetTitleSize(0.04)
    efficiencies_norm.GetYaxis().SetTitleSize(0.045)
    efficiencies.GetYaxis().SetTitle('#varepsilon')
    efficiencies.GetYaxis().SetTitleSize(0.045)
    efficiencies.GetYaxis().SetTitleOffset(0.8)
    efficiencies_norm.SetFillStyle(3001)
    efficiencies_norm.SetLineWidth(2)
    #efficiencies.SetMarkerStyle(20)
    #efficiencies.SetMarkerColor(ROOT.kRed)
    #efficiencies_norm.SetMarkerStyle(20)
    #efficiencies_norm.SetMarkerColor(ROOT.kRed)

    outfile = ROOT.TFile('{}_eff.root'.format(opt.cut), 'RECREATE')
    
    efficiencies.Write()
    efficiencies_norm.Write()
    numerator0.Write()
    denominator0.Write()
    numerator1.Write()
    denominator1.Write()
    numerator2.Write()
    denominator2.Write()
    numerator3.Write()
    denominator3.Write()
    numerator4.Write()
    denominator4.Write()
    numerator6.Write()
    denominator6.Write()
    numerator8.Write()
    denominator8.Write()
         
    canva = ROOT.TCanvas('canva', "", 100, 200, 700, 500)
    canva.cd()
    efficiencies.Draw('AP4C')
    canva.SaveAs('{}_eff.png'.format(opt.cut))
    canva.SaveAs('CANVA{}_eff.root'.format(opt.cut))
    
    canva_norm = ROOT.TCanvas('canva_norm', "", 100, 200, 700, 500)
    canva_norm.cd()
    if (opt.cut=='jv') or (opt.cut=='djv'):
        efficiencies_norm.GetYaxis().SetRangeUser(0.885,1.115)
    elif (opt.cut=='cjv') or (opt.cut=='dcjv'):
        efficiencies_norm.GetYaxis().SetRangeUser(0.9915,1.0085)
    efficiencies_norm.Draw('AP4C')
    canva_norm.SaveAs('{}_eff_norm.png'.format(opt.cut))
    canva_norm.SaveAs('CANVA{}_eff_norm.root'.format(opt.cut))
