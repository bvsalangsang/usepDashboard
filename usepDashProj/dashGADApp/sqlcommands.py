"""
SQL Command for dashGadApp.

List of CRUD functions for dashGadApp 
"""

#campus
def fetchCampus():
    sql =("""
        SELECT * from man_campus 
        WHERE  isActive  = 'Y'
        """)
    return sql 
    
# add/update Campus
def insertUpdateCampus(**gadCampusParams):
    sql = ("""
        INSERT INTO man_campus
        SET campId = '{0}',
        name = '{1}',
        isActive  = '{2}'
        ON DUPLICATE KEY UPDATE 
        name = '{1}',
        isActive  = '{2}'
        """).format(gadCampusParams['campId'],
                    gadCampusParams['name'],
                    gadCampusParams['isActive'])
    
    return sql 

#delete campus
def deleteCampus(**gadCampusParams):
    sql = ("""
        UPDATE man_campus 
           SET isActive = '{1}'
           WHERE campId = '{0}'
        """).format(gadCampusParams['campId'],
                    gadCampusParams['isActive'])

    return sql

#division
def fetchDivision():
    sql =("""
        SELECT divis.divId as divId,
               camp.name AS campusName,
               divis.name AS divName,
               divis.IsActive AS divActive
               from man_division divis 
               LEFT JOIN man_campus camp ON camp.campId = divis.campId
               WHERE divis.isActive  = 'Y'
        """)
    return sql 
    
# add/update division
def insertUpdateDivision(**gadDivisionParams):
    sql = ("""
        INSERT INTO man_division
        SET divId = '{0}',
        campId = '{1}',
        name = '{2}',
        isActive  = '{3}'
        ON DUPLICATE KEY UPDATE 
        campId = '{1}',
        name = '{2}',
        isActive  = '{3}'
        """).format(gadDivisionParams['divId'],
                    gadDivisionParams['campId'],
                    gadDivisionParams['name'],
                    gadDivisionParams['isActive'])
    
    return sql 

#delete campus
def deleteDivision(**gadDivisionParams):
    sql = ("""
        UPDATE man_division 
           SET isActive = '{1}'
           WHERE divId = '{0}'
        """).format(gadDivisionParams['divId'],
                    gadDivisionParams['isActive'])

    return sql

#component
def fetchComponent():
    sql = ("""
        SELECT comp.compId AS compId,
           divis.name AS divName,
           comp.description AS compDesc,
           comp.isActive AS compIsActive
           FROM man_component comp 
           LEFT JOIN man_division divis ON divis.divId = comp.divId
           WHERE comp.isActive = 'Y'
        """)
    
    return sql

def getComponent(**gadDivisionParams):
    
    sql = ("""
        SELECT comp.compId AS compId,
           divis.name AS divName,
           comp.description AS compDesc,
           comp.isActive AS compIsActive
           FROM man_component comp 
           LEFT JOIN man_division divis ON divis.divId = comp.divId
           WHERE comp.isActive = 'Y' AND divis.divId = '{0}'
        """).format(gadDivisionParams['divId'])
    
    return sql


# add/update component
def insertUpdateComponent(**gadComponentParams):
    sql = ("""
        INSERT INTO man_component
        SET compId = '{0}',
        divId = '{1}',
        description = '{2}',
        isActive  = '{3}'
        ON DUPLICATE KEY UPDATE 
        divId = '{1}',
        description = '{2}',
        isActive  = '{3}'
        """).format(gadComponentParams['compId'],
                    gadComponentParams['divId'],
                    gadComponentParams['description'],
                    gadComponentParams['isActive'])
    
    return sql 

def deleteComponent(**gadComponentParams):
    sql = ("""
        UPDATE man_component 
           SET isActive = '{1}'
           WHERE compId = '{0}'
        """).format(gadComponentParams['compId'],
                    gadComponentParams['isActive'])

    return sql


# gad details
def fetchGad():
    sql =("""
            SELECT gad.gadId AS gadId,
            camp.name AS campName,
            divis.name AS divName,
            comp.description AS description,
            gad.series AS series,
            gad.program AS program,
            gad.female AS female,
            gad.male AS male,
            gad.total AS total,
            gad.isActive as gadIsActive
            FROM gad
            LEFT JOIN man_campus camp ON camp.campId = gad.campId
            LEFT JOIN man_component comp ON comp.compId = gad.compId
            LEFT JOIN man_division divis ON comp.divId = divis.divId
            WHERE gad.isActive = 'Y'
            ORDER BY divis.name
        """)
    
    return sql

def insertUpdateGadDetails(**gadDetParams):
    sql = ("""
        INSERT INTO gad 
            SET gadId = '{0}',
            campId = '{1}',
            compId = '{2}',
            series = '{3}',
            program = '{4}',
            female = '{5}',
            male = '{6}',
            total = '{7}',
            isActive = '{8}'
         ON DUPLICATE KEY UPDATE
            campId = '{1}',
            compId = '{2}',
            series = '{3}',
            program = '{4}',
            female ='{5}',
            male = '{6}',
            total = '{7}',
            isActive = '{8}'
        """).format(gadDetParams['gadId'],
                    gadDetParams['campId'],
                    gadDetParams['compId'],
                    gadDetParams['series'],
                    gadDetParams['program'],
                    gadDetParams['female'],
                    gadDetParams['male'],
                    gadDetParams['total'],
                    gadDetParams['isActive'])
    return sql       

def deleteGad(**gadDetParams):
    sql = ("""
        UPDATE gad 
           SET isActive = '{1}'
           WHERE gadId = '{0}'
        """).format(gadDetParams['gadId'],
                    gadDetParams['isActive'])

    return sql

# def getGad(**gadDetParams):
#     sql=("""


#         """)