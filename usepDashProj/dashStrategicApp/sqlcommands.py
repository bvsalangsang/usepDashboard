"""
SQL Command for dashStrategicApp.

List of CRUD functions for dashStrategicApp 
"""

#area
def fetchArea():
    sql = ("SELECT man_strat_area.areaId AS areaId, "
           "man_strat_area.code AS code, "
           "man_strat_area.name AS name, "
           "man_strat_area.isActive AS isActive "
           "FROM man_strat_area "
           "WHERE man_strat_area.isActive = 'Y' ")
    return sql 

def insertNewArea(**stratAreaParams):
    sql = ("INSERT INTO man_strat_area " 
           "SET areaId = '{0}', "
           "code = '{1}', "
           "name = '{2}', "
           "isActive = '{3}'").format(stratAreaParams['areaId'],
            stratAreaParams['code'],
            stratAreaParams['name'],
            stratAreaParams['isActive'])
    return sql

def updateArea(**stratAreaParams):
    sql = ("UPDATE man_strat_area "
            " SET code = '{1}', "
            "  name = '{2}', "
            "  isActive = '{3}' "
            " WHERE areaId  = '{0}' "
            ).format(stratAreaParams["areaId"],
            stratAreaParams["code"],
            stratAreaParams["name"],
            stratAreaParams["isActive"])
    return sql

def deleteArea(**stratAreaParams):
    sql = ("UPDATE man_strat_area "
            "SET isActive = '{1}' " 
            "WHERE areaId  = '{0}' "
            ).format(stratAreaParams["areaId"],
             stratAreaParams["isActive"]) 
    return sql

# Objective
def fetchObj():
    sql = ("SELECT man_strat_objective.objId AS objId, "
           "man_strat_area.areaId AS areaId,"
           "man_strat_area.name AS area, "
           "man_strat_objective.code AS code, "
           "man_strat_objective.description AS description, "
           "man_strat_objective.isActive AS isActive "
           "FROM man_strat_objective "
           "LEFT JOIN man_strat_area ON man_strat_area.areaId = man_strat_objective.areaId "
           "WHERE man_strat_objective.isActive = 'Y' ")
    return sql 

def insertNewObj(**stratObjParams):
    sql = ("INSERT INTO man_strat_objective " 
           "SET objId = '{0}', "
           "areaId = '{1}', "
           "code = '{2}', "
           "description = '{3}', "
           "isActive = '{4}'").format(stratObjParams['objId'],
            stratObjParams['areaId'],
            stratObjParams['code'],
            stratObjParams['description'],
            stratObjParams['isActive'])
    return sql

def updateObj(**stratObjParams):
    sql = ("UPDATE man_strat_objective "
            " SET areaId = '{1}', "
            " code = '{2}', "
            " description = '{3}', "
            " isActive = '{4}' "
            " WHERE objId  = '{0}' "
            ).format(stratObjParams["objId"],
            stratObjParams["areaId"],
            stratObjParams["code"],
            stratObjParams["description"],
            stratObjParams["isActive"])
    return sql

def deleteObj(**stratObjParams):
    sql = ("UPDATE man_strat_objective "
            "SET isActive = '{1}' " 
            "WHERE objId  = '{0}' "
            ).format(stratObjParams["objId"],
             stratObjParams["isActive"]) 
    return sql

# Indicator
def fetchInd():
    sql = ("SELECT man_strat_indicator.indId AS indId, "
           "man_strat_objective.objId AS objId, "
           "man_strat_objective.description AS obj, "
           "ref_type.description AS refType, "
           "man_strat_indicator.code AS code, "
           "man_strat_indicator.description AS description, "
           "man_strat_indicator.isActive AS isActive "
           "FROM man_strat_indicator "
           "LEFT JOIN man_strat_objective ON man_strat_objective.objId = man_strat_indicator.objId "
           "LEFT JOIN ref_type ON ref_type.typeNo = man_strat_indicator.typeNo "
           "WHERE man_strat_indicator.isActive = 'Y' ")
    return sql 

def insertNewInd(**stratIndParams):
    sql = ("INSERT INTO man_strat_indicator " 
           "SET indId = '{0}', "
           "objId = '{1}', "
           "typeNo = '{2}', "
           "code = '{3}', "
           "description = '{4}', "
           "isActive = '{5}'").format(stratIndParams['indId'],
            stratIndParams['objId'],
            stratIndParams['typeNo'],
            stratIndParams['code'],
            stratIndParams['description'],
            stratIndParams['isActive'])
    return sql

def updateInd(**stratIndParams):
    sql = ("UPDATE man_strat_indicator "
            " SET objId = '{1}', "
            " typeNo = '{2}', "
            " code = '{3}', "
            " description = '{4}', "
            " isActive = '{5}' "
            " WHERE indId  = '{0}' "
            ).format(stratIndParams["indId"],
            stratIndParams["objId"],
            stratIndParams["typeNo"],
            stratIndParams["code"],
            stratIndParams["description"],
            stratIndParams["isActive"])
    return sql

def deleteInd(**stratIndParams):
    sql = ("UPDATE man_strat_indicator "
            "SET isActive = '{1}' " 
            "WHERE indId  = '{0}' "
            ).format(stratIndParams["indId"],
             stratIndParams["isActive"]) 
    return sql

#reference
def fetchRef():
    sql =("""
            SELECT ref_strat_reference.refNo AS refNo,
            ref_strat_reference.refName AS refName,
            ref_strat_reference.description AS description,
            ref_strat_reference.isActive AS isActive
            FROM ref_strat_reference
            WHERE ref_strat_reference.isActive = 'Y'
        """)

    return sql

def saveUpdateReference(**stratRefParams):
    sql = ("""
            INSERT INTO ref_strat_reference
            SET refNo = '{0}',
            refName = '{1}',
            description = '{2}',
            isActive = '{3}'
            ON DUPLICATE KEY UPDATE 
            refName = '{1}',
            description = '{2}',
            isActive = '{3}'
          """).format(stratRefParams['refNo'],
                    stratRefParams['refName'], 
                    stratRefParams['description'], 
                    stratRefParams['isActive'])
    
    return sql

def deleteRef(**stratRefParams):
    sql = ("UPDATE ref_strat_reference "
            "SET isActive = '{1}' " 
            "WHERE refNo  = '{0}' "
            ).format(stratRefParams["refNo"],
             stratRefParams["isActive"]) 
    return sql


#matrices
def stratAnnualTargets():
    sql = ("SELECT area.areaId as AreaId, "
          "area.code AS areaCode, "
          "area.name AS areaName, "
          "area.isActive AS areaIsActive, "
          "obj.objId  AS objId, "
          "obj.code AS objCode, "
          "obj.description AS objDesc, "
          "obj.isActive AS objIsActive, "  
          "ind.indId  AS indId, "
          "rtype.description AS typeDesc, "
          "ind.code AS indCode, "
          "ind.description AS indDesc, "
          "ind.isActive AS indIsActive, "  
          "strat.reference AS reference, "
          "strat.blineData AS baseLine, "
          "strat.targetPlan AS targetPlan, "
          "strat.yr2022 AS yr2022, "
          "strat.yr2023 AS yr2023, "
          "strat.yr2024 AS yr2024, "
          "strat.yr2025 AS yr2025, "
          "strat.yr2026 AS yr2024, "
          "strat.yr2027 AS yr2025, "
          "strat.isActive AS stratIsActive, "
          "strat.ctrlNo AS ctrlNo "
          "FROM man_strat_area area "
          "LEFT JOIN man_strat_objective obj ON area.areaId = obj.areaId "
          "LEFT JOIN man_strat_indicator ind ON obj.objId = ind.objId "
          "LEFT JOIN ref_type rtype ON rtype.typeNo = ind.typeNo "
          "LEFT JOIN strat_plan_matices strat ON strat.indId = ind.indId "
            )
    return sql 

def insertMartrices(**matricesParams):
    sql = ("""
        INSERT INTO strat_plan_matices
        SET indId = '{0}', 
            reference = '{1}',
            blineData = '{2}', 
            targetPlan = '{3}',
            yr2022 = '{4}', 
            yr2023 = '{5}', 
            yr2024 = '{6}', 
            yr2025 = '{7}', 
            yr2026 = '{8}', 
            yr2027 = '{9}',
            isActive = '{10}',
            ctrlNo = '{11}' 
            ON DUPLICATE KEY UPDATE
            indId = '{0}', 
            reference = '{1}',
            blineData = '{2}', 
            targetPlan = '{3}',
            yr2022 = '{4}', 
            yr2023 = '{5}', 
            yr2024 = '{6}', 
            yr2025 = '{7}', 
            yr2026 = '{8}', 
            yr2027 = '{9}',
           isActive = '{10}'
           """).format(matricesParams['indId'],
                       matricesParams['reference'],
                       matricesParams['blineData'],
                       matricesParams['targetPlan'],
                       matricesParams['yr2022'],
                       matricesParams['yr2023'],
                       matricesParams['yr2024'],
                       matricesParams['yr2025'],
                       matricesParams['yr2026'],
                       matricesParams['yr2027'],
                      matricesParams['isActive'],
                      matricesParams['ctrlNo'])
    return sql

#scorecards
def stratScorecards(**scorecardParams):
    sql = ("""SELECT 
    area.areaId AS AreaId, 
    area.code AS areaCode, 
    area.name AS areaName, 
    area.isActive AS areaIsActive, 
    obj.objId AS objId, 
    obj.code AS objCode, 
    obj.description AS objDesc, 
    obj.isActive AS objIsActive, 
    ind.indId AS indId, 
    rtype.description AS typeDesc, 
    ind.code AS indCode, 
    ind.description AS indDesc, 
    ind.isActive AS indIsActive,   
    scard.reference AS reference,
    scard.targetyear AS year, 
    scard.target AS target, 
    scard.actual AS actual, 
    scard.variance AS variance, 
    scard.percentage AS percentage, 
    scard.isActive AS scActive, 
    scard.ctrlNo AS ctrlNo 
    FROM man_strat_area area 
    LEFT JOIN man_strat_objective obj ON area.areaId = obj.areaId 
    LEFT JOIN man_strat_indicator ind ON obj.objId = ind.objId 
    LEFT JOIN ref_type rtype ON rtype.typeNo = ind.typeNo 
    LEFT JOIN strat_yearly_scorecard scard ON scard.indId = ind.indId 
    WHERE scard.targetyear IS NULL OR scard.targetyear = '{0}'
    ORDER BY area.areaId, obj.objId, ind.indId;
    """).format(scorecardParams['targetyear'])
    return sql 

def insertNewScorecards(**scorecardParams):
    sql = ("""
        INSERT INTO strat_yearly_scorecard
        SET indId = '{0}', 
            reference = '{1}',
            targetyear = '{2}', 
            target = '{3}',
            actual = '{4}', 
            variance = '{5}', 
            percentage = '{6}', 
            isActive = '{7}',
            ctrlNo = '{8}'
            ON DUPLICATE KEY UPDATE
            indId = '{0}', 
            reference = '{1}',
            targetyear = '{2}', 
            target = '{3}',
            actual = '{4}', 
            variance = '{5}', 
            percentage = '{6}', 
            isActive = '{7}' 
           """).format(scorecardParams['indId'],
                       scorecardParams['reference'],
                       scorecardParams['targetyear'],
                       scorecardParams['target'],
                       scorecardParams['actual'],
                       scorecardParams['variance'],
                       scorecardParams['percentage'],
                       scorecardParams['isActive'],
                       scorecardParams['ctrlNo'] )
    return sql

#strat template
def fetchTemplate():
  
    sql = ("""
            SELECT tempId, tempName, createdBy, createdDate, isActive
            FROM  strat_template 
            WHERE isActive = 'Y' 
        """)
    
    return sql

def rawStratItems():
    sql = ("""SELECT 
    area.areaId AS AreaId, 
    area.code AS areaCode, 
    area.name AS areaName, 
    area.isActive AS areaIsActive, 
    obj.objId AS objId, 
    obj.code AS objCode, 
    obj.description AS objDesc, 
    obj.isActive AS objIsActive, 
    ind.indId AS indId, 
    rtype.description AS typeDesc, 
    ind.code AS indCode, 
    ind.description AS indDesc, 
    ind.isActive AS indIsActive 
    FROM man_strat_area area 
    LEFT JOIN man_strat_objective obj ON area.areaId = obj.areaId 
    LEFT JOIN man_strat_indicator ind ON obj.objId = ind.objId 
    LEFT JOIN ref_type rtype ON rtype.typeNo = ind.typeNo 
     """)
    return sql 

def tempStratItems(**stratTempDetParams):
    sql = ("""SELECT 
    area.areaId AS AreaId, 
    area.code AS areaCode, 
    area.name AS areaName, 
    area.isActive AS areaIsActive, 
    obj.objId AS objId, 
    obj.code AS objCode, 
    obj.description AS objDesc, 
    obj.isActive AS objIsActive, 
    ind.indId AS indId, 
    rtype.description AS typeDesc, 
    ind.code AS indCode, 
    ind.description AS indDesc, 
    temp.reference AS reference,
    temp.target AS target,
    temp.isActive AS tempIsActive,
    temp.ctrlNo as ctrlNo
    FROM man_strat_area area 
    LEFT JOIN man_strat_objective obj ON area.areaId = obj.areaId 
    LEFT JOIN man_strat_indicator ind ON obj.objId = ind.objId 
    LEFT JOIN strat_template_det temp ON ind.indId = temp.indId
    LEFT JOIN ref_type rtype ON rtype.typeNo = ind.typeNo 
    WHERE temp.tempId = '{0}' AND temp.isActive = '{1}'
     """).format(stratTempDetParams['tempId'],
                 stratTempDetParams['isActive'])
    return sql 

def insertStratTemp(**stratTempParams):
    sql = ("""
            INSERT INTO strat_template
            SET tempId = '{0}',
            tempName = '{1}',
            createdBy = '{2}',
            createdDate = '{3}',
            isActive = '{4}'
            ON DUPLICATE KEY UPDATE
            tempName = '{1}',
            createdBy = '{2}',
            createdDate = '{3}',
            isActive = '{4}'
         """).format(stratTempParams['tempId'],
                     stratTempParams['tempName'],
                     stratTempParams['createdBy'],
                     stratTempParams['createdDate'],
                     stratTempParams['isActive'])
    return sql 

def insertStratTempDet(**stratTempDetParams):
    sql = ("""
            INSERT INTO strat_template_det 
            set tempId = '{0}',
            indId = '{1}', 
            reference = '{2}',
            target = '{3}',
            isActive = '{4}'
          """).format(stratTempDetParams['tempId'],
                      stratTempDetParams['indId'],
                      stratTempDetParams['reference'],
                      stratTempDetParams['target'],
                      stratTempDetParams['isActive'])
    return sql

