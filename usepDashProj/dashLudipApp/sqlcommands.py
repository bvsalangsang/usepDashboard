"""
SQL Command for mainApp.

List of CRUD functions for mainApp 
"""

def fetchLudip():
    sql = ("SELECT * FROM ludip WHERE isActive = 'Y'")
    return sql

def insertNewLudip(**ludipParams):
    sql = ("INSERT INTO ludip "
            "SET ludipId  = '{0}', "
            " campus = '{1}', "
            " totalLandArea = '{2}', "
            " landUsed = '{3}', "
            " remainLand = '{4}', "
            " landUsedMap = '{5}', "
            " siteDevPlan = '{6}', "
            " remarks = '{7}', "
            " isActive = '{8}'").format(ludipParams["ludipId"],
            ludipParams["campus"],
            ludipParams["totalLandArea"],
            ludipParams["landUsed"],
            ludipParams["remainLand"], 
            ludipParams["landUsedMap"], 
            ludipParams["siteDevPlan"],
            ludipParams["remarks"],
            ludipParams["isActive"])
    return sql

def updateLudip(**ludipParams):
    sql = ("UPDATE ludip "
            " SET campus = '{1}', "
            " totalLandArea = '{2}', "
            " landUsed = '{3}', "
            " remainLand = '{4}', "
            " landUsedMap = '{5}', "
            " siteDevPlan = '{6}', "
            " remarks = '{7}', "
            " isActive = '{8}'"
             "WHERE ludipId  = '{0}' "
            ).format(ludipParams["ludipId"],
            ludipParams["campus"],
            ludipParams["totalLandArea"],
            ludipParams["landUsed"],
            ludipParams["remainLand"], 
            ludipParams["landUsedMap"], 
            ludipParams["siteDevPlan"],
            ludipParams["remarks"],
            ludipParams["isActive"])
    return sql
     
def deleteLudip(**ludipParams):
    sql = ("UPDATE ludip "
            "SET isActive = '{1}' " 
            "WHERE ludipId  = '{0}' "
            ).format(ludipParams["ludipId"],
             ludipParams["isActive"]) 
    return sql
