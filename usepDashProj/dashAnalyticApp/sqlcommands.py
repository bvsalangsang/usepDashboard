
#universal 
def fetchType():
    sql = ("SELECT * from ref_type WHERE isActive = 'Y'")
    return sql


#analytics
def fetchAnalytics():
    sql = ("SELECT analytics.analId as analId,"
           "anal_program.name as program, "
           "ref_type.description as analType, "
           "analytics.indicator as indicator, "
           "analytics.isActive as isActive "
           "FROM analytics "
           "LEFT JOIN ref_type ON ref_type.typeNo = analytics.typeNo " 
           "LEFT JOIN anal_program ON anal_program.progId = analytics.progId "
           "WHERE analytics.isActive = 'Y'")
    return sql

def fetchAnalProg():
    sql=("SELECT * FROM anal_program WHERE isActive = 'Y'")
    return sql

def insertNewAnal(**analyticsParams):
    sql = ("INSERT INTO analytics " 
           "SET analId = '{0}', "
           "progId = '{1}', "
           "typeNo = '{2}', "
           "indicator = '{3}', "
           "isActive = '{4}'").format(analyticsParams['analId'],
            analyticsParams['progId'],
            analyticsParams['typeNo'],
            analyticsParams['indicator'],
            analyticsParams['isActive'])
    return sql

def updateAnal(**analyticsParams):
    sql = ("UPDATE analytics "
            " SET progId = '{1}', "
            " typeNo = '{2}', "
            " indicator = '{3}', "
            " isActive = '{4}' "
            " WHERE analId  = '{0}' "
            ).format(analyticsParams["analId"],
            analyticsParams["progId"],
            analyticsParams["typeNo"],
            analyticsParams["indicator"],
            analyticsParams["isActive"])
    return sql
   
def deleteAnal(**analyticsParams):
    sql = ("UPDATE analytics "
            "SET isActive = '{1}' " 
            "WHERE analId  = '{0}' "
            ).format(analyticsParams["analId"],
             analyticsParams["isActive"]) 
    return sql

#analytics indicator Board passer
def getAnalInd(**analyticsParams):
    sql = ("SELECT analytics.analId as analId,"
           "anal_program.name as program, "
           "ref_type.description as analType, "
           "analytics.indicator as indicator, "
           "analytics.isActive as isActive "
           "FROM analytics "
           "LEFT JOIN ref_type ON ref_type.typeNo = analytics.typeNo " 
           "LEFT JOIN anal_program ON anal_program.progId = analytics.progId "
           "WHERE analytics.analId = '{0}' AND analytics.isActive = 'Y'").format(analyticsParams['analId'])
    return sql

def fetchBoardPasser():
    sql = ("SELECT anal_board_passers.ctrlNo as ctrlNo, "
           "anal_board_passers.analId AS analId, "
           "analytics.indicator AS indicator, "
           "anal_board_passers.year AS year, "
           "anal_board_passers.noOfTakers AS noOfTakers, "
           "anal_board_passers.noOfPassers AS noOfPassers, "
           "anal_board_passers.percentage AS percentage, "
           "anal_board_passers.isActive AS isActive "
           "FROM anal_board_passers " 
           "LEFT JOIN analytics ON analytics.analId = anal_board_passers.analId " 
           "WHERE anal_board_passers.isActive = 'Y'")
    return sql

def insertNewBoardPasser(**boardPasserParams):
    sql = ("INSERT INTO anal_board_passers " 
           "SET analId = '{0}', "
           "year = '{1}', "
           "noOfTakers = '{2}', "
           "noOfPassers = '{3}', "
           "percentage = '{4}', "
           "isActive = '{5}'").format(boardPasserParams['analId'],
            boardPasserParams['year'],
            boardPasserParams['noOfTakers'],
            boardPasserParams['noOfPassers'],
            boardPasserParams['percentage'],
            boardPasserParams['isActive'])
    return sql

def updateBoardpasser(**boardPasserParams):
    sql = ("Update anal_board_passers " 
           "SET analId = '{0}', "
           "year = '{1}', "
           "noOfTakers = '{2}', "
           "noOfPassers = '{3}', "
           "percentage = '{4}', "
           "isActive = '{5}' "
           "WHERE ctrlNo = '{6}' ").format(boardPasserParams['analId'],
            boardPasserParams['year'],
            boardPasserParams['noOfTakers'],
            boardPasserParams['noOfPassers'],
            boardPasserParams['percentage'],
            boardPasserParams['isActive'],
            boardPasserParams['ctrlNo'])
    return sql
   
def deleteBoardPasser(**boardPasserParams):
    sql = ("UPDATE anal_board_passers "
            "SET isActive = '{1}' " 
            "WHERE ctrlNo  = '{0}' "
            ).format(boardPasserParams["ctrlNo"],
             boardPasserParams["isActive"]) 
    return sql

#analytics indicator employability
def fetchEmployability():
    sql = ("SELECT anal_employability.ctrlNo as ctrlNo, "
           "anal_employability.analId AS analId, "
           "analytics.indicator AS indicator, "
           "anal_employability.year AS year, "
           "anal_employability.noOfGrads AS noOfGrads, "
           "anal_employability.noOfEmployed AS noOfEmployed, "
           "anal_employability.percentage AS percentage, "
           "anal_employability.isActive AS isActive "
           "FROM anal_employability " 
           "LEFT JOIN analytics ON analytics.analId = anal_employability.analId " 
           "WHERE anal_employability.isActive = 'Y'")
    return sql

def insertNewEmployability(**employabilityParams):
    sql = ("INSERT INTO anal_employability " 
           "SET analId = '{0}', "
           "year = '{1}', "
           "noOfGrads = '{2}', "
           "noOfEmployed = '{3}', "
           "percentage = '{4}', "
           "isActive = '{5}'").format(employabilityParams['analId'],
            employabilityParams['year'],
            employabilityParams['noOfGrads'],
            employabilityParams['noOfEmployed'],
            employabilityParams['percentage'],
            employabilityParams['isActive'])
    return sql

def updateEmployability(**employabilityParams):
    sql = ("Update anal_employability " 
           "SET analId = '{0}', "
           "year = '{1}', "
           "noOfGrads = '{2}', "
           "noOfEmployed = '{3}', "
           "percentage = '{4}', "
           "isActive = '{5}' "
           "WHERE ctrlNo = '{6}' ").format(employabilityParams['analId'],
            employabilityParams['year'],
            employabilityParams['noOfGrads'],
            employabilityParams['noOfEmployed'],
            employabilityParams['percentage'],
            employabilityParams['isActive'],
            employabilityParams['ctrlNo'])
    return sql
   
def deleteEmployability(**employabilityParams):
    sql = ("UPDATE anal_employability "
        "SET isActive = '{1}' " 
        "WHERE ctrlNo  = '{0}' "
        ).format(employabilityParams["ctrlNo"],
            employabilityParams["isActive"]) 
    return sql

#analytics indicator ched rdc identified
def fetchChedRdcIdent():
    sql = ("SELECT anal_ched_rdc.ctrlNo as ctrlNo, "
           "anal_ched_rdc.analId AS analId, "
           "analytics.indicator AS indicator, "
           "anal_ched_rdc.year AS year, "
           "anal_ched_rdc.noOfUnderGrad AS noOfUnderGrad, "
           "anal_ched_rdc.noOfChedRdcIdent AS noOfChedRdcIdent, "
           "anal_ched_rdc.percentage AS percentage, "
           "anal_ched_rdc.isActive AS isActive "
           "FROM anal_ched_rdc " 
           "LEFT JOIN analytics ON analytics.analId = anal_ched_rdc.analId " 
           "WHERE anal_ched_rdc.isActive = 'Y'")
    return sql

def insertNewChedRdcIdent(**chedRdcParams):
    sql = ("INSERT INTO anal_ched_rdc " 
           "SET analId = '{0}', "
           "year = '{1}', "
           "noOfUnderGrad = '{2}', "
           "noOfChedRdcIdent = '{3}', "
           "percentage = '{4}', "
           "isActive = '{5}'").format(chedRdcParams['analId'],
            chedRdcParams['year'],
            chedRdcParams['noOfUnderGrad'],
            chedRdcParams['noOfChedRdcIdent'],
            chedRdcParams['percentage'],
            chedRdcParams['isActive'])
    return sql

def updateChedRdcIdent(**chedRdcParams):
    sql = ("Update anal_ched_rdc " 
           "SET analId = '{0}', "
           "year = '{1}', "
           "noOfUnderGrad = '{2}', "
           "noOfChedRdcIdent = '{3}', "
           "percentage = '{4}', "
           "isActive = '{5}' "
           "WHERE ctrlNo = '{6}' ").format(chedRdcParams['analId'],
            chedRdcParams['year'],
            chedRdcParams['noOfUnderGrad'],
            chedRdcParams['noOfChedRdcIdent'],
            chedRdcParams['percentage'],
            chedRdcParams['isActive'],
            chedRdcParams['ctrlNo'])
    return sql
   
def deleteChedRdcIdent(**chedRdcParams):
    sql = ("UPDATE anal_ched_rdc "
        "SET isActive = '{1}' " 
        "WHERE ctrlNo  = '{0}' "
        ).format(chedRdcParams["ctrlNo"],
            chedRdcParams["isActive"]) 
    return sql

#analytics indicator accreditation
def fetchAccred():
    sql = ("SELECT anal_accreditation.ctrlNo as ctrlNo, "
           "anal_accreditation.analId AS analId, "
           "analytics.indicator AS indicator, "
           "anal_accreditation.year AS year, "
           "anal_accreditation.noOfUnderGradProg AS noOfUnderGradProg, "
           "anal_accreditation.noOfUnderGradProgAccred AS noOfUnderGradProgAccred, "
           "anal_accreditation.percentage AS percentage, "
           "anal_accreditation.isActive AS isActive "
           "FROM anal_accreditation " 
           "LEFT JOIN analytics ON analytics.analId = anal_accreditation.analId " 
           "WHERE anal_accreditation.isActive = 'Y'")
    return sql

def insertNewAccred(**accredParams):
    sql = ("INSERT INTO anal_accreditation " 
           "SET analId = '{0}', "
           "year = '{1}', "
           "noOfUnderGradProg = '{2}', "
           "noOfUnderGradProgAccred = '{3}', "
           "percentage = '{4}', "
           "isActive = '{5}'").format(accredParams['analId'],
            accredParams['year'],
            accredParams['noOfUnderGradProg'],
            accredParams['noOfUnderGradProgAccred'],
            accredParams['percentage'],
            accredParams['isActive'])
    return sql

def updateAccred(**accredParams):
    sql = ("Update anal_accreditation " 
           "SET analId = '{0}', "
           "year = '{1}', "
           "noOfUnderGradProg = '{2}', "
           "noOfUnderGradProgAccred = '{3}', "
           "percentage = '{4}', "
           "isActive = '{5}' "
           "WHERE ctrlNo = '{6}' ").format(accredParams['analId'],
            accredParams['year'],
            accredParams['noOfUnderGradProg'],
            accredParams['noOfUnderGradProgAccred'],
            accredParams['percentage'],
            accredParams['isActive'],
            accredParams['ctrlNo'])
    return sql
   
def deleteAccred(**accredParams):
    sql = ("UPDATE anal_accreditation "
        "SET isActive = '{1}' " 
        "WHERE ctrlNo  = '{0}' "
        ).format(accredParams["ctrlNo"],
            accredParams["isActive"]) 
    return sql

#analytics indicator faculty research
def fetchGradRes():
    sql = ("SELECT anal_grad_research.ctrlNo as ctrlNo, "
           "anal_grad_research.analId AS analId, "
           "analytics.indicator AS indicator, "
           "anal_grad_research.year AS year, "
           "anal_grad_research.noOfGradFac AS noOfGradFac, "
           "anal_grad_research.noOfGradFacRes AS noOfGradFacRes, "
           "anal_grad_research.percentage AS percentage, "
           "anal_grad_research.isActive AS isActive "
           "FROM anal_grad_research " 
           "LEFT JOIN analytics ON analytics.analId = anal_grad_research.analId " 
           "WHERE anal_grad_research.isActive = 'Y'")
    return sql

def insertNewGradRes(**gradresParams):
    sql = ("INSERT INTO anal_grad_research " 
           "SET analId = '{0}', "
           "year = '{1}', "
           "noOfGradFac = '{2}', "
           "noOfGradFacRes = '{3}', "
           "percentage = '{4}', "
           "isActive = '{5}'").format(gradresParams['analId'],
            gradresParams['year'],
            gradresParams['noOfGradFac'],
            gradresParams['noOfGradFacRes'],
            gradresParams['percentage'],
            gradresParams['isActive'])
    return sql

def updateGradRes(**gradresParams):
    sql = ("Update anal_grad_research " 
           "SET analId = '{0}', "
           "year = '{1}', "
           "noOfGradFac = '{2}', "
           "noOfGradFacRes = '{3}', "
           "percentage = '{4}', "
           "isActive = '{5}' "
           "WHERE ctrlNo = '{6}' ").format(gradresParams['analId'],
            gradresParams['year'],
            gradresParams['noOfGradFac'],
            gradresParams['noOfGradFacRes'],
            gradresParams['percentage'],
            gradresParams['isActive'],
            gradresParams['ctrlNo'])
    return sql
      
def deleteGradRes(**gradresParams):
    sql = ("UPDATE anal_grad_research "
        "SET isActive = '{1}' " 
        "WHERE ctrlNo  = '{0}' "
        ).format(gradresParams["ctrlNo"],
            gradresParams["isActive"]) 
    return sql

#analytics indicator research degree
def fetchResDeg():
    sql = ("SELECT anal_res_degree.ctrlNo as ctrlNo, "
           "anal_res_degree.analId AS analId, "
           "analytics.indicator AS indicator, "
           "anal_res_degree.year AS year, "
           "anal_res_degree.noOfGrad AS noOfGrad, "
           "anal_res_degree.noOfGradResDeg AS noOfGradResDeg, "
           "anal_res_degree.percentage AS percentage, "
           "anal_res_degree.isActive AS isActive "
           "FROM anal_res_degree " 
           "LEFT JOIN analytics ON analytics.analId = anal_res_degree.analId " 
           "WHERE anal_res_degree.isActive = 'Y'")
    return sql

def insertNewResDeg(**resDegParams):
    sql = ("INSERT INTO anal_res_degree " 
           "SET analId = '{0}', "
           "year = '{1}', "
           "noOfGrad = '{2}', "
           "noOfGradResDeg = '{3}', "
           "percentage = '{4}', "
           "isActive = '{5}'").format(resDegParams['analId'],
            resDegParams['year'],
            resDegParams['noOfGrad'],
            resDegParams['noOfGradResDeg'],
            resDegParams['percentage'],
            resDegParams['isActive'])
    return sql

def updateResDeg(**resDegParams):
    sql = ("Update anal_res_degree " 
           "SET analId = '{0}', "
           "year = '{1}', "
           "noOfGrad = '{2}', "
           "noOfGradResDeg = '{3}', "
           "percentage = '{4}', "
           "isActive = '{5}' "
           "WHERE ctrlNo = '{6}' ").format(resDegParams['analId'],
            resDegParams['year'],
            resDegParams['noOfGrad'],
            resDegParams['noOfGradResDeg'],
            resDegParams['percentage'],
            resDegParams['isActive'],
            resDegParams['ctrlNo'])
    return sql
      
def deleteResDeg(**resDegParams):
    sql = ("UPDATE anal_res_degree "
        "SET isActive = '{1}' " 
        "WHERE ctrlNo  = '{0}' "
        ).format(resDegParams["ctrlNo"],
            resDegParams["isActive"]) 
    return sql

#analytics indicator Accredited Graduate Program
def fetchAccGradProg():
    sql = ("SELECT anal_accr_grad_prog.ctrlNo as ctrlNo, "
           "anal_accr_grad_prog.analId AS analId, "
           "analytics.indicator AS indicator, "
           "anal_accr_grad_prog.year AS year, "
           "anal_accr_grad_prog.noOfGradProg AS noOfGradProg, "
           "anal_accr_grad_prog.noOfAccrGradProg AS noOfAccrGradProg, "
           "anal_accr_grad_prog.percentage AS percentage, "
           "anal_accr_grad_prog.isActive AS isActive "
           "FROM anal_accr_grad_prog " 
           "LEFT JOIN analytics ON analytics.analId = anal_accr_grad_prog.analId " 
           "WHERE anal_accr_grad_prog.isActive = 'Y'")
    return sql

def insertNewAccrGradProg(**accrGradProgParams):
    sql = ("INSERT INTO anal_accr_grad_prog " 
           "SET analId = '{0}', "
           "year = '{1}', "
           "noOfGradProg = '{2}', "
           "noOfAccrGradProg = '{3}', "
           "percentage = '{4}', "
           "isActive = '{5}'").format(accrGradProgParams['analId'],
            accrGradProgParams['year'],
            accrGradProgParams['noOfGradProg'],
            accrGradProgParams['noOfAccrGradProg'],
            accrGradProgParams['percentage'],
            accrGradProgParams['isActive'])
    return sql

def updateAccrGradProg(**accrGradProgParams):
    sql = ("Update anal_accr_grad_prog " 
           "SET analId = '{0}', "
           "year = '{1}', "
           "noOfGradProg = '{2}', "
           "noOfAccrGradProg = '{3}', "
           "percentage = '{4}', "
           "isActive = '{5}' "
           "WHERE ctrlNo = '{6}' ").format(accrGradProgParams['analId'],
            accrGradProgParams['year'],
            accrGradProgParams['noOfGradProg'],
            accrGradProgParams['noOfAccrGradProg'],
            accrGradProgParams['percentage'],
            accrGradProgParams['isActive'],
            accrGradProgParams['ctrlNo'])
    return sql
      
def deleteAccrGradProg(**accrGradProgParams):
    sql = ("UPDATE anal_accr_grad_prog "
        "SET isActive = '{1}' " 
        "WHERE ctrlNo  = '{0}' "
        ).format(accrGradProgParams["ctrlNo"],
            accrGradProgParams["isActive"]) 
    return sql

#analytics indicator Research Output
def fetchResOutput():
    sql = ("SELECT anal_res_output.ctrlNo as ctrlNo, "
           "anal_res_output.analId AS analId, "
           "analytics.indicator AS indicator, "
           "anal_res_output.year AS year, "
           "anal_res_output.noOfResOutput AS noOfResOutput, "
           "anal_res_output.isActive AS isActive "
           "FROM anal_res_output " 
           "LEFT JOIN analytics ON analytics.analId = anal_res_output.analId " 
           "WHERE anal_res_output.isActive = 'Y'")
    return sql

def insertNewResOutput(**resOutputParams):
    sql = ("INSERT INTO anal_res_output " 
           "SET analId = '{0}', "
           "year = '{1}', "
           "noOfResOutput = '{2}', "
           "isActive = '{3}'").format(resOutputParams['analId'],
            resOutputParams['year'],
            resOutputParams['noOfResOutput'],
            resOutputParams['isActive'])
    return sql

def updateResOutput(**resOutputParams):
    sql = ("Update anal_res_output " 
           "SET analId = '{0}', "
           "year = '{1}', "
           "noOfResOutput = '{2}', "
           "isActive = '{3}' "
           "WHERE ctrlNo = '{4}' ").format(resOutputParams['analId'],
            resOutputParams['year'],
            resOutputParams['noOfResOutput'],
            resOutputParams['isActive'],
            resOutputParams['ctrlNo'])
    return sql
      
def deleteResOutput(**resOutputParams):
    sql = ("UPDATE anal_res_output "
        "SET isActive = '{1}' " 
        "WHERE ctrlNo  = '{0}' "
        ).format(resOutputParams["ctrlNo"],
            resOutputParams["isActive"]) 
    return sql

#analytics indicator Research Output Complete
def fetchResComplete():
    sql = ("SELECT anal_res_complete.ctrlNo as ctrlNo, "
           "anal_res_complete.analId AS analId, "
           "analytics.indicator AS indicator, "
           "anal_res_complete.year AS year, "
           "anal_res_complete.noOfResComplete AS noOfResComplete, "
           "anal_res_complete.isActive AS isActive "
           "FROM anal_res_complete " 
           "LEFT JOIN analytics ON analytics.analId = anal_res_complete.analId " 
           "WHERE anal_res_complete.isActive = 'Y'")
    return sql

def insertNewResComplete(**resCompleteParams):
    sql = ("INSERT INTO anal_res_complete " 
           "SET analId = '{0}', "
           "year = '{1}', "
           "noOfResComplete = '{2}', "
           "isActive = '{3}'").format(resCompleteParams['analId'],
            resCompleteParams['year'],
            resCompleteParams['noOfResComplete'],
            resCompleteParams['isActive'])
    return sql

def updateResComplete(**resCompleteParams):
    sql = ("Update anal_res_complete " 
           "SET analId = '{0}', "
           "year = '{1}', "
           "noOfResComplete = '{2}', "
           "isActive = '{3}' "
           "WHERE ctrlNo = '{4}' ").format(resCompleteParams['analId'],
            resCompleteParams['year'],
            resCompleteParams['noOfResComplete'],
            resCompleteParams['isActive'],
            resCompleteParams['ctrlNo'])
    return sql
      
def deleteResComplete(**resCompleteParams):
    sql = ("UPDATE anal_res_complete "
        "SET isActive = '{1}' " 
        "WHERE ctrlNo  = '{0}' "
        ).format(resCompleteParams["ctrlNo"],
            resCompleteParams["isActive"]) 
    return sql

#analytics indicator Research Output Published
def fetchResPublished():
    sql = ("SELECT anal_res_published.ctrlNo as ctrlNo, "
           "anal_res_published.analId AS analId, "
           "analytics.indicator AS indicator, "
           "anal_res_published.year AS year, "
           "anal_res_published.noOfResOutput AS noOfResOutput, "
           "anal_res_published.noOfResPublished AS noOfResPublished, "
           "anal_res_published.percentage AS percentage, "
           "anal_res_published.isActive AS isActive "
           "FROM anal_res_published " 
           "LEFT JOIN analytics ON analytics.analId = anal_res_published.analId " 
           "WHERE anal_res_published.isActive = 'Y'")
    return sql

def insertNewResPublished(**resPublishedParams):
    sql = ("INSERT INTO anal_res_published " 
           "SET analId = '{0}', "
           "year = '{1}', "
           "noOfResOutput = '{2}', "
           "noOfResPublished = '{3}', "
           "percentage = '{4}', "
           "isActive = '{5}'").format(resPublishedParams['analId'],
            resPublishedParams['year'],
            resPublishedParams['noOfResOutput'],
            resPublishedParams['noOfResPublished'],
            resPublishedParams['percentage'],
            resPublishedParams['isActive'])
    return sql

def updateResPublished(**resPublishedParams):
    sql = ("Update anal_res_published " 
           "SET analId = '{0}', "
           "year = '{1}', "
           "noOfResOutput = '{2}', "
           "noOfResPublished = '{3}', "
           "percentage = '{4}', "
           "isActive = '{5}' "
           "WHERE ctrlNo = '{6}' ").format(resPublishedParams['analId'],
            resPublishedParams['year'],
            resPublishedParams['noOfResOutput'],
            resPublishedParams['noOfResPublished'],
            resPublishedParams['percentage'],
            resPublishedParams['isActive'],
            resPublishedParams['ctrlNo'])
    return sql
      
def deleteResPublished(**resPublishedParams):
    sql = ("UPDATE anal_res_published "
        "SET isActive = '{1}' " 
        "WHERE ctrlNo  = '{0}' "
        ).format(resPublishedParams["ctrlNo"],
            resPublishedParams["isActive"]) 
    return sql

#analytics indicator Active partnership
def fetchActPartner():
    sql = ("SELECT anal_active_partner.ctrlNo as ctrlNo, "
           "anal_active_partner.analId AS analId, "
           "analytics.indicator AS indicator, "
           "anal_active_partner.year AS year, "
           "anal_active_partner.noOfActPart AS noOfActPart, "
           "anal_active_partner.isActive AS isActive "
           "FROM anal_active_partner " 
           "LEFT JOIN analytics ON analytics.analId = anal_active_partner.analId " 
           "WHERE anal_active_partner.isActive = 'Y'")
    return sql

def insertNewActPartner(**actPartnerParams):
    sql = ("INSERT INTO anal_active_partner " 
           "SET analId = '{0}', "
           "year = '{1}', "
           "noOfActPart = '{2}', "
           "isActive = '{3}'").format(actPartnerParams['analId'],
            actPartnerParams['year'],
            actPartnerParams['noOfActPart'],
            actPartnerParams['isActive'])
    return sql

def updateActPartner(**actPartnerParams):
    sql = ("Update anal_active_partner " 
           "SET analId = '{0}', "
           "year = '{1}', "
           "noOfActPart = '{2}', "
           "isActive = '{3}' "
           "WHERE ctrlNo = '{4}' ").format(actPartnerParams['analId'],
            actPartnerParams['year'],
            actPartnerParams['noOfActPart'],
            actPartnerParams['isActive'],
            actPartnerParams['ctrlNo'])
    return sql
      
def deleteActPartner(**actPartnerParams):
    sql = ("UPDATE anal_active_partner "
        "SET isActive = '{1}' " 
        "WHERE ctrlNo  = '{0}' "
        ).format(actPartnerParams["ctrlNo"],
            actPartnerParams["isActive"]) 
    return sql


#analytics indicator Number of Trainees
def fetchTrainees():
    sql = ("SELECT anal_num_trainees.ctrlNo as ctrlNo, "
           "anal_num_trainees.analId AS analId, "
           "analytics.indicator AS indicator, "
           "anal_num_trainees.year AS year, "
           "anal_num_trainees.noOfTrainees AS noOfTrainees, "
           "anal_num_trainees.isActive AS isActive "
           "FROM anal_num_trainees " 
           "LEFT JOIN analytics ON analytics.analId = anal_num_trainees.analId " 
           "WHERE anal_num_trainees.isActive = 'Y'")
    return sql

def insertNewTrainees(**traineesParams):
    sql = ("INSERT INTO anal_num_trainees " 
           "SET analId = '{0}', "
           "year = '{1}', "
           "noOfTrainees = '{2}', "
           "isActive = '{3}'").format(traineesParams['analId'],
            traineesParams['year'],
            traineesParams['noOfTrainees'],
            traineesParams['isActive'])
    return sql

def updateTrainees(**traineesParams):
    sql = ("Update anal_num_trainees " 
           "SET analId = '{0}', "
           "year = '{1}', "
           "noOfTrainees = '{2}', "
           "isActive = '{3}' "
           "WHERE ctrlNo = '{4}' ").format(traineesParams['analId'],
            traineesParams['year'],
            traineesParams['noOfTrainees'],
            traineesParams['isActive'],
            traineesParams['ctrlNo'])
    return sql
      
def deleteTrainees(**traineesParams):
    sql = ("UPDATE anal_num_trainees "
        "SET isActive = '{1}' " 
        "WHERE ctrlNo  = '{0}' "
        ).format(traineesParams["ctrlNo"],
            traineesParams["isActive"]) 
    return sql

#analytics indicator Number of Extension Program
def fetchExtProgram():
    sql = ("SELECT anal_ext_program.ctrlNo as ctrlNo, "
           "anal_ext_program.analId AS analId, "
           "analytics.indicator AS indicator, "
           "anal_ext_program.year AS year, "
           "anal_ext_program.noOfExtProgram AS noOfExtProgram, "
           "anal_ext_program.isActive AS isActive "
           "FROM anal_ext_program " 
           "LEFT JOIN analytics ON analytics.analId = anal_ext_program.analId " 
           "WHERE anal_ext_program.isActive = 'Y'")
    return sql

def insertNewExtProgram(**extProgramParams):
    sql = ("INSERT INTO anal_ext_program " 
           "SET analId = '{0}', "
           "year = '{1}', "
           "noOfExtProgram = '{2}', "
           "isActive = '{3}'").format(extProgramParams['analId'],
            extProgramParams['year'],
            extProgramParams['noOfExtProgram'],
            extProgramParams['isActive'])
    return sql

def updateExtProgram(**extProgramParams):
    sql = ("Update anal_ext_program " 
           "SET analId = '{0}', "
           "year = '{1}', "
           "noOfExtProgram = '{2}', "
           "isActive = '{3}' "
           "WHERE ctrlNo = '{4}' ").format(extProgramParams['analId'],
            extProgramParams['year'],
            extProgramParams['noOfExtProgram'],
            extProgramParams['isActive'],
            extProgramParams['ctrlNo'])
    return sql
      
def deleteExtProgram(**extProgramParams):
    sql = ("UPDATE anal_ext_program "
        "SET isActive = '{1}' " 
        "WHERE ctrlNo  = '{0}' "
        ).format(extProgramParams["ctrlNo"],
            extProgramParams["isActive"]) 
    return sql

#analytics indicator Beneficiaries
def fetchBeneficiary():
    sql = ("SELECT anal_beneficiaries.ctrlNo as ctrlNo, "
           "anal_beneficiaries.analId AS analId, "
           "analytics.indicator AS indicator, "
           "anal_beneficiaries.year AS year, "
           "anal_beneficiaries.noOfBenef AS noOfBenef, "
           "anal_beneficiaries.noOfBenef AS noOfBenef, "
           "anal_beneficiaries.percentage AS percentage, "
           "anal_beneficiaries.isActive AS isActive "
           "FROM anal_beneficiaries " 
           "LEFT JOIN analytics ON analytics.analId = anal_beneficiaries.analId " 
           "WHERE anal_beneficiaries.isActive = 'Y'")
    return sql

def insertNewBeneficiary(**benefParams):
    sql = ("INSERT INTO anal_beneficiaries " 
           "SET analId = '{0}', "
           "year = '{1}', "
           "noOfBenef = '{2}', "
           "noOfBenefRate = '{3}', "
           "percentage = '{4}', "
           "isActive = '{5}'").format(benefParams['analId'],
            benefParams['year'],
            benefParams['noOfBenef'],
            benefParams['noOfBenefRate'],
            benefParams['percentage'],
            benefParams['isActive'])
    return sql

def updateBeneficiary(**benefParams):
    sql = ("Update anal_beneficiaries " 
           "SET analId = '{0}', "
           "year = '{1}', "
           "noOfBenef = '{2}', "
           "noOfBenefRate = '{3}', "
           "percentage = '{4}', "
           "isActive = '{5}' "
           "WHERE ctrlNo = '{6}' ").format(benefParams['analId'],
            benefParams['year'],
            benefParams['noOfBenef'],
            benefParams['noOfBenefRate'],
            benefParams['percentage'],
            benefParams['isActive'],
            benefParams['ctrlNo'])
    return sql
      
def deleteBeneficiary(**benefParams):
    sql = ("UPDATE anal_beneficiaries "
        "SET isActive = '{1}' " 
        "WHERE ctrlNo  = '{0}' "
        ).format(benefParams["ctrlNo"],
            benefParams["isActive"]) 
    return sql