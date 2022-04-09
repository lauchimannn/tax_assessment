import tkinter as tk

class GuiOverlay:
    def __init__(self, parent):
        #create main frames in parent frame
        self.center = tk.Frame(parent)
        #display main frames in parent frame
        self.center.grid(sticky = 'nsew')
        self.home()
        
    def add_sep(self, r, c, widg):
        '''
        create empty label for formatting in grid
        '''
        tk.Label(widg).grid(row=r, column=c)

    def home(self):
        def resetFunction():
            '''
            Function to reset entries
            '''
            #reset radiobutton & entries
            statusVar.set(1)
            selfE.delete(0, 'end')
            spouseE.delete(0, 'end')
            outgoingsExpensesE_self.delete(0, 'end')
            outgoingsExpensesE_self.insert(0, '0')
            outgoingsExpensesE_spouse.delete(0, 'end')
            outgoingsExpensesE_spouse.insert(0, '0')
            selfEduExpensesE_self.delete(0, 'end')
            selfEduExpensesE_self.insert(0, '0')
            selfEduExpensesE_spouse.delete(0, 'end')
            selfEduExpensesE_spouse.insert(0, '0')
            approvedCharitableDonationsE_self.delete(0, 'end')
            approvedCharitableDonationsE_self.insert(0, '0')
            approvedCharitableDonationsE_spouse.delete(0, 'end')
            approvedCharitableDonationsE_spouse.insert(0, '0')
            homeLoanInterestE_self.delete(0, 'end')
            homeLoanInterestE_self.insert(0, '0')
            homeLoanInterestE_spouse.delete(0, 'end')
            homeLoanInterestE_spouse.insert(0, '0')
            amountPaidToResidentialCareHomeE_self.delete(0, 'end')
            amountPaidToResidentialCareHomeE_self.insert(0, '0')
            amountPaidToResidentialCareHomeE_spouse.delete(0, 'end')
            amountPaidToResidentialCareHomeE_spouse.insert(0, '0')
            noOfDependantEligibleVar_self.set(elderlyList[0])
            noOfDependantEligibleVar_spouse.set(elderlyList[0])
            personalDisabilityVar_self.set(personalDisabilityList[0])
            personalDisabilityVar_spouse.set(personalDisabilityList[0])
            
            #clear error messages
            self.errorMsg0.destroy()
            self.errorMsg1.destroy()
        
        def computeFunction(selfVar, spouseVar, outgoingsExpensesVar_self, outgoingsExpensesVar_spouse, selfEduExpensesVar_self, selfEduExpensesVar_spouse, approvedCharitableDonationsVar_self, approvedCharitableDonationsVar_spouse, homeLoanInterestVar_self, homeLoanInterestVar_spouse, noOfDependantEligibleVar_self, noOfDependantEligibleVar_spouse, amountPaidToResidentialCareHomeVar_self, amountPaidToResidentialCareHomeVar_spouse, personalDisabilityVar_self, personalDisabilityVar_spouse):
            '''
            Function to compute result
            '''
            def backFunction():
                '''
                Function to return to home
                '''
                #destroy previous data
                for e in range(self.center.grid_size()[1]):
                    l=list(self.center.grid_slaves(row=e))
                    for w in l:
                        w.destroy()
                        
                self.home()
                
            '''
            error checking
            '''
            #set var
            emptyValid = True
            positiveValid = True
            
            #clear error messages
            self.errorMsg0.destroy()
            self.errorMsg1.destroy()
            
            #single
            if selfVar:
                #income
                if selfVar.isdigit():
                    if int(selfVar) < 0:
                        positiveValid = False
                else:
                    positiveValid = False
                #outgoings and expenses
                if outgoingsExpensesVar_self.isdigit():
                    if int(outgoingsExpensesVar_self) < 0:
                        positiveValid = False
                elif not outgoingsExpensesVar_self:
                    outgoingsExpensesVar_self = 0
                else:
                    positiveValid = False
                #self education expenses
                if selfEduExpensesVar_self.isdigit():
                    if int(selfEduExpensesVar_self) < 0:
                        positiveValid = False
                elif not selfEduExpensesVar_self:
                    selfEduExpensesVar_self = 0
                else:
                    positiveValid = False
                #approved charitable donations
                if approvedCharitableDonationsVar_self.isdigit():
                    if int(approvedCharitableDonationsVar_self) < 0:
                        positiveValid = False
                elif not approvedCharitableDonationsVar_self:
                    approvedCharitableDonationsVar_self = 0
                else:
                    positiveValid = False
                #home loan interest
                if homeLoanInterestVar_self.isdigit():
                    if int(homeLoanInterestVar_self) < 0:
                        positiveValid = False
                elif not homeLoanInterestVar_self:
                    homeLoanInterestVar_self = 0
                else:
                    positiveValid = False
                #amount paid to residential care home
                if amountPaidToResidentialCareHomeVar_self.isdigit():
                    if int(amountPaidToResidentialCareHomeVar_self) < 0:
                        positiveValid = False
                elif not amountPaidToResidentialCareHomeVar_self:
                    amountPaidToResidentialCareHomeVar_self = 0
                else:
                    positiveValid = False
            else:
                emptyValid = False
                
            #married
            if statusVar.get() == 2:
                if selfVar and spouseVar:
                    #income
                    if selfVar.isdigit() and spouseVar.isdigit():
                        if int(selfVar) < 0 or int(spouseVar) < 0:
                            positiveValid = False
                    else:
                        positiveValid = False
                    #outgoings and expenses
                    if outgoingsExpensesVar_spouse.isdigit():
                        if int(outgoingsExpensesVar_spouse) < 0:
                            positiveValid = False
                    elif not outgoingsExpensesVar_spouse:
                        outgoingsExpensesVar_spouse = 0
                    else:
                        positiveValid = False
                    #self education expenses
                    if selfEduExpensesVar_spouse.isdigit():
                        if int(selfEduExpensesVar_spouse) < 0:
                            positiveValid = False
                    elif not selfEduExpensesVar_spouse:
                        selfEduExpensesVar_spouse = 0
                    else:
                        positiveValid = False
                    #approved charitable donations
                    if approvedCharitableDonationsVar_spouse.isdigit():
                        if int(approvedCharitableDonationsVar_spouse) < 0:
                            positiveValid = False
                    elif not approvedCharitableDonationsVar_spouse:
                        approvedCharitableDonationsVar_spouse = 0
                    else:
                        positiveValid = False
                    #home loan interest
                    if homeLoanInterestVar_spouse.isdigit():
                        if int(homeLoanInterestVar_spouse) < 0:
                            positiveValid = False
                    elif not homeLoanInterestVar_spouse:
                        homeLoanInterestVar_spouse = 0
                    else:
                        positiveValid = False
                    #amount paid to residential care home
                    if amountPaidToResidentialCareHomeVar_spouse.isdigit():
                        if int(amountPaidToResidentialCareHomeVar_spouse) < 0:
                            positiveValid = False
                    elif not amountPaidToResidentialCareHomeVar_spouse:
                        amountPaidToResidentialCareHomeVar_spouse = 0
                    else:
                        positiveValid = False
                else:
                    emptyValid = False
            
            #empty value error
            if not emptyValid:
                self.errorMsg0 = tk.Label(self.center, text='Empty value')
                self.errorMsg0.grid(row=15, column=0, columnspan=3)
                self.errorMsg0.config(fg='red')
                
            #input value error
            if not positiveValid:
                self.errorMsg1 = tk.Label(self.center, text='Invalid input')
                self.errorMsg1.grid(row=16, column=0, columnspan=3)
                self.errorMsg1.config(fg='red')
            
            #no error
            if emptyValid and positiveValid:
                #destroy previous data
                for e in range(self.center.grid_size()[1]):
                    l=list(self.center.grid_slaves(row=e))
                    for w in l:
                        w.destroy()
                        
                #titles        
                title0 = tk.Label(self.center, text='Computation of Estimated Salaries Tax Liabilities')
                title1 = tk.Label(self.center, text='Year of assessment 2021/22')
                
                #total income
                totalIncomeL = tk.Label(self.center, text='TOTAL INCOME', borderwidth=1, relief='solid', width=50, anchor='w')
                totalIncomeN_self = tk.Label(self.center, text=selfVar, borderwidth=1, relief='solid', width=30, anchor='e')
                
                #dedections
                deductionsL = tk.Label(self.center, text='DEDUCTIONS:-', borderwidth=1, relief='solid', width=50, anchor='w')
                #outgoings and expenses
                outgoingsExpensesL = tk.Label(self.center, text='   Outgoings and Expenses', borderwidth=1, relief='solid', width=50, anchor='w')
                outgoingsExpensesN_self = tk.Label(self.center, text=outgoingsExpensesVar_self, borderwidth=1, relief='solid', width=30, anchor='e')
                #self education expenses
                selfEduExpensesL = tk.Label(self.center, text='   Self Education Expenses', borderwidth=1, relief='solid', width=50, anchor='w')
                selfEduExpensesN_self = tk.Label(self.center, text=selfEduExpensesVar_self, borderwidth=1, relief='solid', width=30, anchor='e')
                #approved charitable donations
                approvedCharitableDonationsL = tk.Label(self.center, text='   Approved Charitable Donations', borderwidth=1, relief='solid', width=50, anchor='w')
                approvedCharitableDonationsN_self = tk.Label(self.center, text=approvedCharitableDonationsVar_self, borderwidth=1, relief='solid', width=30, anchor='e')
                #MPF
                MPFL = tk.Label(self.center, text='   Tax Deductible MPF Voluntary Contributions', borderwidth=1, relief='solid', width=50, anchor='w')
                if int(selfVar)*0.05 < 18000:
                    MPF_self = int(int(selfVar)*0.05)
                else:
                    MPF_self = 18000
                MPFN_self = tk.Label(self.center, text=MPF_self, borderwidth=1, relief='solid', width=30, anchor='e')
                #home loan interest
                homeLoanInterestL = tk.Label(self.center, text='   Home Loan Interest', borderwidth=1, relief='solid', width=50, anchor='w')
                homeLoanInterestN_self = tk.Label(self.center, text=homeLoanInterestVar_self, borderwidth=1, relief='solid', width=30, anchor='e')
                #amount paid to residential care home
                amountPaidToResidentialCareHomeL = tk.Label(self.center, text='   Amount Paid To Residential Care Home', borderwidth=1, relief='solid', width=50, anchor='w')
                amountPaidToResidentialCareHomeN_self = tk.Label(self.center, text=amountPaidToResidentialCareHomeVar_self, borderwidth=1, relief='solid', width=30, anchor='e')
                
                #net total income
                netTotalIncomeL = tk.Label(self.center, text='NET TOTAL INCOME', borderwidth=1, relief='solid', width=50, anchor='w')
                NTI_self = int(selfVar)-int(outgoingsExpensesVar_self)-int(selfEduExpensesVar_self)-int(approvedCharitableDonationsVar_self)-MPF_self-int(homeLoanInterestVar_self)-int(amountPaidToResidentialCareHomeVar_self)
                if NTI_self < 0:
                    NTI_self = 0
                netTotalIncomeN_self = tk.Label(self.center, text=NTI_self, borderwidth=1, relief='solid', width=30, anchor='e')
                
                #allowances
                allowancesL = tk.Label(self.center, text='ALLOWANCES:-', borderwidth=1, relief='solid', width=50, anchor='w')
                basicL = tk.Label(self.center, text='   Basic', borderwidth=1, relief='solid', width=50, anchor='w')
                allowancesN_self = tk.Label(self.center, text='132,000', borderwidth=1, relief='solid', width=30, anchor='e')
                disableddependantL = tk.Label(self.center, text='   Disabled Dependant(s)', borderwidth=1, relief='solid', width=50, anchor='w')
                disableddependantN_self = tk.Label(self.center, text=int(noOfDependantEligibleVar_self)*75000, borderwidth=1, relief='solid', width=30, anchor='e')
                personalDisabilityL = tk.Label(self.center, text='   Personal Disability', borderwidth=1, relief='solid', width=50, anchor='w')
                if personalDisabilityVar_self == 'Yes':
                    personalDisabilityN_self = tk.Label(self.center, text='75,000', borderwidth=1, relief='solid', width=30, anchor='e')
                    PD_self = 75000
                else:
                    personalDisabilityN_self = tk.Label(self.center, text=0, borderwidth=1, relief='solid', width=30, anchor='e')
                    PD_self = 0
                
                #net chargeable income
                netChargeableIncomeL = tk.Label(self.center, text='NET CHARGEABLE INCOME', borderwidth=1, relief='solid', width=50, anchor='w')
                NCI_self = NTI_self - 132000 - int(noOfDependantEligibleVar_self)*75000 - PD_self
                if NCI_self < 0:
                    NCI_self = 0
                netChargeableIncomeN_self = tk.Label(self.center, text=NCI_self, borderwidth=1, relief='solid', width=30, anchor='e')
                
                #tax payable
                standardRateValid = False
                #calculation
                if NTI_self >= 2022000:
                    TP_self = NTI_self*0.15
                    standardRateValid = True
                elif NCI_self >= 200000:
                    TP_self = 1000+3000+5000+7000+(NCI_self-200000)*0.17
                    taxPayableN_self = tk.Label(self.center, text=str(int(TP_self))+' (17%)', borderwidth=1, relief='solid', width=30, anchor='e')
                elif NCI_self >= 150000:
                    TP_self = 1000+3000+5000+(NCI_self-150000)*0.14
                    taxPayableN_self = tk.Label(self.center, text=str(int(TP_self))+' (14%)', borderwidth=1, relief='solid', width=30, anchor='e')
                elif NCI_self >= 100000:
                    TP_self = 1000+3000+(NCI_self-100000)*0.1
                    taxPayableN_self = tk.Label(self.center, text=str(int(TP_self))+' (10%)', borderwidth=1, relief='solid', width=30, anchor='e')
                elif NCI_self >= 50000:
                    TP_self = 1000+(NCI_self-50000)*0.06
                    taxPayableN_self = tk.Label(self.center, text=str(int(TP_self))+' (6%)', borderwidth=1, relief='solid', width=30, anchor='e')
                elif NCI_self > 0:
                    TP_self = NCI_self*0.02
                    taxPayableN_self = tk.Label(self.center, text=str(int(TP_self))+' (2%)', borderwidth=1, relief='solid', width=30, anchor='e')
                elif NCI_self == 0:
                    TP_self = 0
                    taxPayableN_self = tk.Label(self.center, text=int(TP_self), borderwidth=1, relief='solid', width=30, anchor='e')
                if standardRateValid:
                    taxPayableL = tk.Label(self.center, text='TAX PAYABLE BY YOU (* At Standard Rate)', borderwidth=1, relief='solid', width=50, anchor='w')
                    taxPayableN_self = tk.Label(self.center, text=str(int(TP_self))+' *', borderwidth=1, relief='solid', width=30, anchor='e', fg='red')
                else:
                    taxPayableL = tk.Label(self.center, text='TAX PAYABLE BY YOU', borderwidth=1, relief='solid', width=50, anchor='w')
                
                #back button
                backB = tk.Button(self.center, text='Back', command = lambda: backFunction())
                
                '''
                single
                '''
                if statusVar.get() == 1:
                    #titles
                    title0.grid(row=0, column=0)
                    title1.grid(row=1, column=0)
                    title2 = tk.Label(self.center, text='Based on the information entered, the amount of tax payable by you is computed as follows : -')
                    title2.grid(row=2, column=0, columnspan=2, sticky='w')
                    title3 = tk.Label(self.center, text='HK$')
                    title3.grid(row=3, column=1)
                    totalIncomeL.grid(row=4, column=0, sticky='w')
                    totalIncomeN_self.grid(row=4, column=1, sticky='e')
                    
                    #deductions
                    deductionsL.grid(row=5, column=0, sticky='w')
                    outgoingsExpensesL.grid(row=6, column=0, sticky='w')
                    outgoingsExpensesN_self.grid(row=6, column=1, sticky='e')
                    selfEduExpensesL.grid(row=7, column=0, sticky='w')
                    selfEduExpensesN_self.grid(row=7, column=1, sticky='e')
                    approvedCharitableDonationsL.grid(row=8, column=0, sticky='w')
                    approvedCharitableDonationsN_self.grid(row=8, column=1, sticky='e')
                    MPFL.grid(row=9, column=0, sticky='w')
                    MPFN_self.grid(row=9, column=1, sticky='e')
                    homeLoanInterestL.grid(row=10, column=0, sticky='w')
                    homeLoanInterestN_self.grid(row=10, column=1, sticky='e')
                    amountPaidToResidentialCareHomeL.grid(row=11, column=0, sticky='w')
                    amountPaidToResidentialCareHomeN_self.grid(row=11, column=1, sticky='e')
                    
                    #net total income
                    netTotalIncomeL.grid(row=12, column=0, sticky='w')
                    netTotalIncomeN_self.grid(row=12, column=1, sticky='e')
                    self.add_sep(13, 0, self.center)
                    
                    #allowances
                    allowancesL.grid(row=14, column=0, sticky='w')
                    basicL.grid(row=15, column=0, sticky='w')
                    allowancesN_self.grid(row=15, column=1, sticky='e')
                    disableddependantL.grid(row=16, column=0, sticky='w')
                    disableddependantN_self.grid(row=16, column=1, sticky='e')
                    personalDisabilityL.grid(row=17, column=0, sticky='w')
                    personalDisabilityN_self.grid(row=17, column=1, sticky='e')
                    
                    #net chargeable income
                    netChargeableIncomeL.grid(row=18, column=0, sticky='w')
                    netChargeableIncomeN_self.grid(row=18, column=1, sticky='e')
                    self.add_sep(19, 0, self.center)
                    
                    #tax payable
                    taxPayableL.grid(row=20, column=0, sticky='w')
                    taxPayableN_self.grid(row=20, column=1, sticky='e')
                    
                    #back button
                    backB.grid(row=21, column=1)
                    
                '''
                married
                '''
                if statusVar.get() == 2:
                    #titles
                    title0.grid(row=0, column=1)
                    title1.grid(row=1, column=1)
                    title2 = tk.Label(self.center, text='Based on the information entered, it is advantageous for you and your spouse to be separately taxed. The minimum overall tax liability for you and your spouse under separate taxation')
                    title2.grid(row=2, column=0, sticky='w', columnspan=4)
                    title2_1 = tk.Label(self.center, text='computed below is based on the assumption that the deductions and allowances in accordance with the number of dependant(s) indicated in the brackets are claimed by you and your spouse.')
                    title2_1.grid(row=3, column=0, sticky='w', columnspan=4)
                    title3 = tk.Label(self.center, text='Under Separate Taxation')
                    title3.grid(row=4, column=1, columnspan=2)
                    title4 = tk.Label(self.center, text='''Self
HK$''')
                    title4.grid(row=5, column=1)
                    title5 = tk.Label(self.center, text='''Spouse
HK$''')
                    title5.grid(row=5, column=2)
                    title6 = tk.Label(self.center, text='Under Joint Assessment')
                    title6.grid(row=4, column=3)
                    title7 = tk.Label(self.center, text='HK$')
                    title7.grid(row=5, column=3)
                    
                    #total income
                    totalIncomeL.grid(row=6, column=0, sticky='w')
                    totalIncomeN_self.grid(row=6, column=1, sticky='e')
                    totalIncomeN_sprouse = tk.Label(self.center, text=spouseVar, borderwidth=1, relief='solid', width=30, anchor='e')
                    totalIncomeN_sprouse.grid(row=6, column=2, sticky='e')
                    totalIncomeN_joint = tk.Label(self.center, text=int(selfVar)+int(spouseVar), borderwidth=1, relief='solid', width=30, anchor='e')
                    totalIncomeN_joint.grid(row=6, column=3, sticky='e')
                    
                    #deductions
                    deductionsL.grid(row=7, column=0, sticky='w')
                    outgoingsExpensesL.grid(row=8, column=0, sticky='w')
                    outgoingsExpensesN_self.grid(row=8, column=1, sticky='e')
                    homeLoanInterestN_spouse = tk.Label(self.center, text=homeLoanInterestVar_spouse, borderwidth=1, relief='solid', width=30, anchor='e')
                    homeLoanInterestN_spouse.grid(row=8, column=2, sticky='e')
                    homeLoanInterestN_joint = tk.Label(self.center, text=int(homeLoanInterestVar_self)+int(homeLoanInterestVar_spouse), borderwidth=1, relief='solid', width=30, anchor='e')
                    homeLoanInterestN_joint.grid(row=8, column=3, sticky='e')
                    selfEduExpensesL.grid(row=9, column=0, sticky='w')
                    selfEduExpensesN_self.grid(row=9, column=1, sticky='e')
                    selfEduExpensesN_spouse = tk.Label(self.center, text=selfEduExpensesVar_spouse, borderwidth=1, relief='solid', width=30, anchor='e')
                    selfEduExpensesN_spouse.grid(row=9, column=2, sticky='e')
                    selfEduExpensesN_joint = tk.Label(self.center, text=int(selfEduExpensesVar_self)+int(selfEduExpensesVar_spouse), borderwidth=1, relief='solid', width=30, anchor='e')
                    selfEduExpensesN_joint.grid(row=9, column=3, sticky='e')
                    approvedCharitableDonationsL.grid(row=10, column=0, sticky='w')
                    approvedCharitableDonationsN_self.grid(row=10, column=1, sticky='e')
                    approvedCharitableDonationsN_spouse = tk.Label(self.center, text=approvedCharitableDonationsVar_spouse, borderwidth=1, relief='solid', width=30, anchor='e')
                    approvedCharitableDonationsN_spouse.grid(row=10, column=2, sticky='e')
                    approvedCharitableDonationsN_joint = tk.Label(self.center, text=int(approvedCharitableDonationsVar_self)+int(approvedCharitableDonationsVar_spouse), borderwidth=1, relief='solid', width=30, anchor='e')
                    approvedCharitableDonationsN_joint.grid(row=10, column=3, sticky='e')
                    MPFL.grid(row=11, column=0, sticky='w')
                    MPFN_self.grid(row=11, column=1, sticky='e')
                    if int(spouseVar)*0.05 < 18000:
                        MPF_spouse = int(int(spouseVar)*0.05)
                    else:
                        MPF_spouse = 18000
                    MPFN_spouse = tk.Label(self.center, text=MPF_spouse, borderwidth=1, relief='solid', width=30, anchor='e')
                    MPFN_spouse.grid(row=11, column=2, sticky='e')
                    MPFN_joint = tk.Label(self.center, text=MPF_self+MPF_spouse, borderwidth=1, relief='solid', width=30, anchor='e')
                    MPFN_joint.grid(row=11, column=3, sticky='e')
                    homeLoanInterestL.grid(row=12, column=0, sticky='w')
                    homeLoanInterestN_self.grid(row=12, column=1, sticky='e')
                    homeLoanInterestN_spouse = tk.Label(self.center, text=homeLoanInterestVar_spouse, borderwidth=1, relief='solid', width=30, anchor='e')
                    homeLoanInterestN_spouse.grid(row=12, column=2, sticky='e')
                    homeLoanInterestN_joint = tk.Label(self.center, text=int(homeLoanInterestVar_self)+int(homeLoanInterestVar_spouse), borderwidth=1, relief='solid', width=30, anchor='e')
                    homeLoanInterestN_joint.grid(row=12, column=3, sticky='e')
                    amountPaidToResidentialCareHomeL.grid(row=13, column=0, sticky='w')
                    amountPaidToResidentialCareHomeN_self.grid(row=13, column=1, sticky='e')
                    amountPaidToResidentialCareHomeN_spouse = tk.Label(self.center, text=amountPaidToResidentialCareHomeVar_spouse, borderwidth=1, relief='solid', width=30, anchor='e')
                    amountPaidToResidentialCareHomeN_spouse.grid(row=13, column=2, sticky='e')
                    amountPaidToResidentialCareHomeN_joint = tk.Label(self.center, text=int(amountPaidToResidentialCareHomeVar_self)+int(amountPaidToResidentialCareHomeVar_spouse), borderwidth=1, relief='solid', width=30, anchor='e')
                    amountPaidToResidentialCareHomeN_joint.grid(row=13, column=3, sticky='e')
                    
                    #net total income
                    netTotalIncomeL.grid(row=14, column=0, sticky='w')
                    netTotalIncomeN_self.grid(row=14, column=1, sticky='e')
                    #calculation
                    NTI_spouse = int(spouseVar)-int(outgoingsExpensesVar_spouse)-int(selfEduExpensesVar_spouse)-int(approvedCharitableDonationsVar_spouse)-MPF_spouse-int(homeLoanInterestVar_spouse)-int(amountPaidToResidentialCareHomeVar_spouse)
                    NTI_joint = NTI_self + NTI_spouse
                    netTotalIncomeN_spouse = tk.Label(self.center, text=NTI_spouse, borderwidth=1, relief='solid', width=30, anchor='e')
                    netTotalIncomeN_spouse.grid(row=14, column=2, sticky='e')
                    netTotalIncomeN_joint = tk.Label(self.center, text=NTI_joint, borderwidth=1, relief='solid', width=30, anchor='e')
                    netTotalIncomeN_joint.grid(row=14, column=3, sticky='e')
                    self.add_sep(15, 0, self.center)
                    
                    #allowances
                    allowancesL.grid(row=16, column=0, sticky='w')
                    basicL.grid(row=17, column=0, sticky='w')
                    allowancesN_self.grid(row=17, column=1, sticky='e')
                    allowancesN_spouse = tk.Label(self.center, text='132,000', borderwidth=1, relief='solid', width=30, anchor='e')
                    allowancesN_spouse.grid(row=17, column=2, sticky='e')
                    allowancesN_joint = tk.Label(self.center, text='264,000', borderwidth=1, relief='solid', width=30, anchor='e')
                    allowancesN_joint.grid(row=17, column=3, sticky='e')
                    disableddependantL.grid(row=18, column=0, sticky='w')
                    disableddependantN_self.grid(row=18, column=1, sticky='e')
                    disableddependantN_spouse = tk.Label(self.center, text=int(noOfDependantEligibleVar_spouse)*75000, borderwidth=1, relief='solid', width=30, anchor='e')
                    disableddependantN_spouse.grid(row=18, column=2, sticky='e')
                    disableddependantN_joint = tk.Label(self.center, text=int(noOfDependantEligibleVar_self)*75000+int(noOfDependantEligibleVar_spouse)*75000, borderwidth=1, relief='solid', width=30, anchor='e')
                    disableddependantN_joint.grid(row=18, column=3, sticky='e')
                    personalDisabilityL.grid(row=19, column=0, sticky='w')
                    personalDisabilityN_self.grid(row=19, column=1, sticky='e')
                    if personalDisabilityVar_spouse == 'Yes':
                        personalDisabilityN_spouse = tk.Label(self.center, text='75,000', borderwidth=1, relief='solid', width=30, anchor='e')
                        PD_spouse = 75000
                    else:
                        personalDisabilityN_spouse = tk.Label(self.center, text=0, borderwidth=1, relief='solid', width=30, anchor='e')
                        PD_spouse = 0
                    personalDisabilityN_spouse.grid(row=19, column=2, sticky='e')
                    personalDisabilityN_joint = tk.Label(self.center, text=PD_self+PD_spouse, borderwidth=1, relief='solid', width=30, anchor='e')
                    personalDisabilityN_joint.grid(row=19, column=3, sticky='e')
                    
                    #net chargeable income
                    netChargeableIncomeL.grid(row=20, column=0, sticky='w')
                    netChargeableIncomeN_self.grid(row=20, column=1, sticky='e')
                    NCI_spouse = NTI_spouse - 132000 - int(noOfDependantEligibleVar_spouse)*75000 - PD_spouse
                    if NCI_spouse < 0:
                        NCI_spouse = 0
                    netChargeableIncomeN_spouse = tk.Label(self.center, text=NCI_spouse, borderwidth=1, relief='solid', width=30, anchor='e')
                    netChargeableIncomeN_spouse.grid(row=20, column=2, sticky='e')
                    netChargeableIncomeN_joint = tk.Label(self.center, text=NCI_self+NCI_spouse, borderwidth=1, relief='solid', width=30, anchor='e')
                    netChargeableIncomeN_joint.grid(row=20, column=3, sticky='e')
                    self.add_sep(21, 0, self.center)
                    
                    #tax payable
                    standardRateValid_spouse = False
                    standardRateValid_joint = False
                    #calculation of spouse
                    if NTI_spouse >= 2022000:
                        TP_spouse = NTI_spouse*0.15
                        standardRateValid_spouse = True
                    elif NCI_spouse >= 200000:
                        TP_spouse = 1000+3000+5000+7000+(NCI_spouse-200000)*0.17
                        taxPayableN_spouse = tk.Label(self.center, text=str(int(TP_spouse))+' (17%)', borderwidth=1, relief='solid', width=30, anchor='e')
                    elif NCI_spouse >= 150000:
                        TP_spouse = 1000+3000+5000+(NCI_spouse-150000)*0.14
                        taxPayableN_spouse = tk.Label(self.center, text=str(int(TP_spouse))+' (14%)', borderwidth=1, relief='solid', width=30, anchor='e')
                    elif NCI_spouse >= 100000:
                        TP_spouse = 1000+3000+(NCI_spouse-100000)*0.1
                        taxPayableN_spouse = tk.Label(self.center, text=str(int(TP_spouse))+' (10%)', borderwidth=1, relief='solid', width=30, anchor='e')
                    elif NCI_spouse >= 50000:
                        TP_spouse = 1000+(NCI_spouse-50000)*0.06
                        taxPayableN_spouse = tk.Label(self.center, text=str(int(TP_spouse))+' (6%)', borderwidth=1, relief='solid', width=30, anchor='e')
                    elif NCI_spouse > 0:
                        TP_spouse = NCI_self*0.02
                        taxPayableN_spouse = tk.Label(self.center, text=str(int(TP_spouse))+' (2%)', borderwidth=1, relief='solid', width=30, anchor='e')
                    elif NCI_spouse == 0:
                        TP_spouse = 0
                        taxPayableN_spouse = tk.Label(self.center, text=int(TP_spouse), borderwidth=1, relief='solid', width=30, anchor='e')
                    #calculation of joint
                    NTI_joint_afterAllowance = NTI_joint - 264000
                    if NTI_self + NTI_spouse >= 2022000:
                        TP_joint = (NTI_self + NTI_spouse)*0.15
                        standardRateValid_joint = True
                    elif NTI_joint_afterAllowance >= 200000:
                        TP_joint = 1000+3000+5000+7000+(NTI_joint_afterAllowance-200000)*0.17
                        taxPayableN_joint = tk.Label(self.center, text=str(int(TP_joint))+' (17%)', borderwidth=1, relief='solid', width=30, anchor='e')
                    elif NTI_joint_afterAllowance >= 150000:
                        TP_joint = 1000+3000+5000+(NTI_joint_afterAllowance-150000)*0.14
                        taxPayableN_joint = tk.Label(self.center, text=str(int(TP_joint))+' (14%)', borderwidth=1, relief='solid', width=30, anchor='e')
                    elif NTI_joint_afterAllowance >= 100000:
                        TP_joint = 1000+3000+(NTI_joint_afterAllowance-100000)*0.1
                        taxPayableN_joint = tk.Label(self.center, text=str(int(TP_joint))+' (10%)', borderwidth=1, relief='solid', width=30, anchor='e')
                    elif NTI_joint_afterAllowance >= 50000:
                        TP_joint = 1000+(NTI_joint_afterAllowance-50000)*0.06
                        taxPayableN_joint = tk.Label(self.center, text=str(int(TP_joint))+' (6%)', borderwidth=1, relief='solid', width=30, anchor='e')
                    elif NTI_joint_afterAllowance > 0:
                        TP_joint = NTI_joint_afterAllowance*0.02
                        taxPayableN_joint = tk.Label(self.center, text=str(int(TP_joint))+' (2%)', borderwidth=1, relief='solid', width=30, anchor='e')
                    else:
                        TP_joint = 0
                        taxPayableN_joint = tk.Label(self.center, text=int(TP_joint), borderwidth=1, relief='solid', width=30, anchor='e')
                    if standardRateValid or standardRateValid_spouse or standardRateValid_joint:
                        taxPayableL = tk.Label(self.center, text='TAX PAYABLE (* At Standard Rate)', borderwidth=1, relief='solid', width=50, anchor='w')
                        if standardRateValid_spouse:
                            taxPayableN_spouse = tk.Label(self.center, text=str(int(TP_spouse))+' *', borderwidth=1, relief='solid', width=30, anchor='e', fg='red')
                        if standardRateValid_joint:
                            taxPayableN_joint = tk.Label(self.center, text=str(int(TP_joint))+' *', borderwidth=1, relief='solid', width=30, anchor='e', fg='red')
                    else:
                        taxPayableL = tk.Label(self.center, text='TAX PAYABLE', borderwidth=1, relief='solid', width=50, anchor='w')
                    taxPayableL.grid(row=22, column=0, sticky='w')
                    taxPayableN_self.grid(row=22, column=1, sticky='e')
                    taxPayableN_spouse.grid(row=22, column=2, sticky='e')
                    taxPayableN_joint.grid(row=22, column=3, sticky='e')
                    
                    #total tax payable
                    totalTaxPayableL = tk.Label(self.center, text='TOTAL TAX PAYABLE BY YOU AND YOUR SPOUSE', borderwidth=1, relief='solid', width=50, anchor='w')
                    totalTaxPayableL.grid(row=23, column=0, sticky='w')
                    totalTaxPayableN = tk.Label(self.center, text=int(TP_self+TP_spouse), borderwidth=1, relief='solid', width=61)
                    totalTaxPayableN.grid(row=23, column=1, columnspan=2, sticky='e')
                    totalTaxPayableN_joint = tk.Label(self.center, text=int(TP_joint), borderwidth=1, relief='solid', width=30)
                    totalTaxPayableN_joint.grid(row=23, column=3, sticky='e')
                    
                    #joint assessment recommended
                    jointAssessmentRecommendedL = tk.Label(self.center, text='Joint Assessment Recommended', borderwidth=1, relief='solid', width=50, anchor='w')
                    jointAssessmentRecommendedL.grid(row=24, column=0, sticky='w')
                    #calculation
                    if TP_self + TP_spouse > TP_joint:
                        jointAssessmentRecommendedN = tk.Label(self.center, text='Yes', borderwidth=1, relief='solid', width=92)
                    else:
                        jointAssessmentRecommendedN = tk.Label(self.center, text='No', borderwidth=1, relief='solid', width=92)
                    jointAssessmentRecommendedN.grid(row=24, column= 1, columnspan=3, sticky='e')
                    
                    #back button
                    backB.grid(row=25, column=3)
        #set var
        statusVar = tk.IntVar()
        selfVar = tk.StringVar()
        spouseVar = tk.StringVar()
        self.errorMsg0 = tk.Label()
        self.errorMsg1 = tk.Label()
        
        #titles
        title0 = tk.Label(self.center, text='Salaries Tax Computation')
        title0.grid(row=0, column=1)
        title1 = tk.Label(self.center, text='Year of assessment')
        title1.grid(row=1, column=0, sticky='w')
        title1_1 = tk.Label(self.center, text='2021/22')
        title1_1.grid(row=1, column=1, sticky='w')
        title2 = tk.Label(self.center, text='Marital status')
        title2.grid(row=2, column=0, sticky='w')
        status0 = tk.Radiobutton(self.center, text='Single / Separated / Divorced / Widowed', var=statusVar, value=1)
        status0.grid(row=2, column=1, sticky='w')
        status1 = tk.Radiobutton(self.center, text='Married', var=statusVar, value=2)
        status1.grid(row=2, column=2)
        statusVar.set(1)
        
        '''
        income
        '''
        incomeL = tk.Label(self.center, text='Income for the year of assessment')
        incomeL.grid(row=4, column=0, sticky='w')
        #self
        selfL = tk.Label(self.center, text='''Self
HK$
(Exclude cents)
        ''')
        selfL.grid(row=3, column=1)
        selfE = tk.Entry(self.center, textvariable=selfVar)
        selfE.grid(row=4, column=1)
        #sprouse
        spouseL = tk.Label(self.center, text='''Spouse
HK$
(Exclude cents)
        ''')
        spouseL.grid(row=3, column=2)
        spouseE = tk.Entry(self.center, textvariable=spouseVar)
        spouseE.grid(row=4, column=2)
        
        '''
        deductions
        '''
        #set var
        outgoingsExpensesVar_self = tk.StringVar()
        outgoingsExpensesVar_spouse = tk.StringVar()
        selfEduExpensesVar_self = tk.StringVar()
        selfEduExpensesVar_spouse = tk.StringVar()
        approvedCharitableDonationsVar_self = tk.StringVar()
        approvedCharitableDonationsVar_spouse = tk.StringVar()
        homeLoanInterestVar_self = tk.StringVar()
        homeLoanInterestVar_spouse = tk.StringVar()
        amountPaidToResidentialCareHomeVar_self = tk.StringVar()
        amountPaidToResidentialCareHomeVar_spouse = tk.StringVar()
        elderlyList = (0, 1, 2, 3, 4)
        noOfDependantEligibleVar_self = tk.StringVar()
        noOfDependantEligibleVar_spouse = tk.StringVar()
        personalDisabilityList = ('No', 'Yes')
        personalDisabilityVar_self = tk.StringVar()
        personalDisabilityVar_spouse = tk.StringVar()
        
        #titles
        deductionsL = tk.Label(self.center, text='Deductions')
        deductionsL.grid(row=5, column=0, sticky='w')
        #outgoings and expenses
        outgoingsExpensesL = tk.Label(self.center, text='Outgoings and Expenses')
        outgoingsExpensesL.grid(row=6, column=0, sticky='w')
        outgoingsExpensesE_self = tk.Entry(self.center, textvariable=outgoingsExpensesVar_self)
        outgoingsExpensesE_self.insert(0, '0')
        outgoingsExpensesE_self.grid(row=6, column=1)
        outgoingsExpensesE_spouse = tk.Entry(self.center, textvariable=outgoingsExpensesVar_spouse)
        outgoingsExpensesE_spouse.insert(0, '0')
        outgoingsExpensesE_spouse.grid(row=6, column=2)
        #self education expenses
        selfEduExpensesL = tk.Label(self.center, text='Self Education Expenses')
        selfEduExpensesL.grid(row=7, column=0, sticky='w')
        selfEduExpensesE_self = tk.Entry(self.center, textvariable=selfEduExpensesVar_self)
        selfEduExpensesE_self.insert(0, '0')
        selfEduExpensesE_self.grid(row=7, column=1)
        selfEduExpensesE_spouse = tk.Entry(self.center, textvariable=selfEduExpensesVar_spouse)
        selfEduExpensesE_spouse.insert(0, '0')
        selfEduExpensesE_spouse.grid(row=7, column=2)
        #approved charitable donations
        approvedCharitableDonationsL = tk.Label(self.center, text='Approved Charitable Donations')
        approvedCharitableDonationsL.grid(row=8, column=0, sticky='w')
        approvedCharitableDonationsE_self = tk.Entry(self.center, textvariable=approvedCharitableDonationsVar_self)
        approvedCharitableDonationsE_self.insert(0, '0')
        approvedCharitableDonationsE_self.grid(row=8, column=1)
        approvedCharitableDonationsE_spouse = tk.Entry(self.center, textvariable=approvedCharitableDonationsVar_spouse)
        approvedCharitableDonationsE_spouse.insert(0, '0')
        approvedCharitableDonationsE_spouse.grid(row=8, column=2)
        #home loan interest
        homeLoanInterestL = tk.Label(self.center, text='Home Loan Interest')
        homeLoanInterestL.grid(row=9, column=0, sticky='w')
        homeLoanInterestE_self = tk.Entry(self.center, textvariable=homeLoanInterestVar_self)
        homeLoanInterestE_self.insert(0, '0')
        homeLoanInterestE_self.grid(row=9, column=1)
        homeLoanInterestE_spouse = tk.Entry(self.center, textvariable=homeLoanInterestVar_spouse)
        homeLoanInterestE_spouse.insert(0, '0')
        homeLoanInterestE_spouse.grid(row=9, column=2)
        
        '''
        allowances
        '''
        #elderly residential care expenses
        elderlyResidentialCareExpensesL = tk.Label(self.center, text='Elderly Residential Care Expenses')
        elderlyResidentialCareExpensesL.grid(row=10, column=0, sticky='w')
        #no. of dependant(s) eligible for Disabled Dependant Allowance
        noOfDependantEligibleL = tk.Label(self.center, text=' - No. of dependant(s) eligible for Disabled Dependant Allowance')
        noOfDependantEligibleL.grid(row=11, column=0, sticky='w')
        noOfDependantEligibleVar_self.set(elderlyList[0])
        noOfDependantEligibleMenu_self = tk.OptionMenu(self.center, noOfDependantEligibleVar_self, *elderlyList)
        noOfDependantEligibleMenu_self.grid(row=11, column=1)
        noOfDependantEligibleVar_spouse.set(elderlyList[0])
        noOfDependantEligibleMenu_spouse = tk.OptionMenu(self.center, noOfDependantEligibleVar_spouse, *elderlyList)
        noOfDependantEligibleMenu_spouse.grid(row=11, column=2)
        #amount paid to residential care home
        amountPaidToResidentialCareHomeL = tk.Label(self.center, text=' - Amount Paid To Residential Care Home')
        amountPaidToResidentialCareHomeL.grid(row=12, column=0, sticky='w')
        amountPaidToResidentialCareHomeE_self = tk.Entry(self.center, textvariable=amountPaidToResidentialCareHomeVar_self)
        amountPaidToResidentialCareHomeE_self.insert(0, '0')
        amountPaidToResidentialCareHomeE_self.grid(row=12, column=1)
        amountPaidToResidentialCareHomeE_spouse = tk.Entry(self.center, textvariable=amountPaidToResidentialCareHomeVar_spouse)
        amountPaidToResidentialCareHomeE_spouse.insert(0, '0')
        amountPaidToResidentialCareHomeE_spouse.grid(row=12, column=2)
        #personal disability
        personalDisabilityL = tk.Label(self.center, text='Eligible to claim Personal Disability Allowance')
        personalDisabilityL.grid(row=13, column=0, sticky='w')
        personalDisabilityVar_self.set(personalDisabilityList[0])
        personalDisabilityMenu_self = tk.OptionMenu(self.center, personalDisabilityVar_self, *personalDisabilityList)
        personalDisabilityMenu_self.grid(row=13, column=1)
        personalDisabilityVar_spouse.set(personalDisabilityList[0])
        personalDisabilityMenu_spouse = tk.OptionMenu(self.center, personalDisabilityVar_spouse, *personalDisabilityList)
        personalDisabilityMenu_spouse.grid(row=13, column=2)
        self.add_sep(14, 0, self.center)
        
        '''
        buttons
        '''
        resetB = tk.Button(self.center, text='Reset', command = lambda: resetFunction())
        resetB.grid(row=15, column=1)
        computeB = tk.Button(self.center, text='Compute', command = lambda: computeFunction(selfVar.get(), spouseVar.get(), outgoingsExpensesVar_self.get(), outgoingsExpensesVar_spouse.get(), selfEduExpensesVar_self.get(), selfEduExpensesVar_spouse.get(), approvedCharitableDonationsVar_self.get(), approvedCharitableDonationsVar_spouse.get(), homeLoanInterestVar_self.get(), homeLoanInterestVar_spouse.get(), noOfDependantEligibleVar_self.get(), noOfDependantEligibleVar_spouse.get(), amountPaidToResidentialCareHomeVar_self.get(), amountPaidToResidentialCareHomeVar_spouse.get(), personalDisabilityVar_self.get(), personalDisabilityVar_spouse.get()))
        computeB.grid(row=15, column=2)
        
def cal_taxPable(income, income_2):
    '''
    calculate tax payable
    '''
    income = str(income)
    if not income:
        print("Empty value")
    elif not income.isdigit():
        print("Invalid value")
    elif income.isdigit():
        if int(income) < 0:
            print("Invalid value")
        else:
            if int(income)*0.05 < 18000:
                MPF = int(income)
            else:
                MPF = 18000
            NTI = int(income) - MPF
            if income_2 == 0:
                NCI = NTI - 132000
            else:
                if int(income_2)*0.05 < 18000:
                    MPF_2 = int(income_2)
                else:
                    MPF_2 = 18000
                NTI_2 = int(income_2) - MPF_2
                NTI = NTI + NTI_2
                NCI = NTI - 264000
                
            if NCI < 0:
                NCI = 0
            if NTI >= 2022000:
                TP = NTI*0.15
            elif NCI >= 200000:
                TP = 1000+3000+5000+7000+(NCI-200000)*0.17
            elif NCI >= 150000:
                TP = 1000+3000+5000+(NCI-150000)*0.14
            elif NCI >= 100000:
                TP = 1000+3000+(NCI-100000)*0.1
            elif NCI >= 50000:
                TP = 1000+(NCI-50000)*0.06
            elif NCI > 0:
                TP = NCI*0.02
            elif NCI == 0:
                TP = 0
                
            return int(TP)

def main():
    root = tk.Tk()
    root.geometry('1100x550')
    root.title('Tax calculator')
    GuiOverlay(root)
    root.mainloop()

if __name__ == '__main__':
    main()
