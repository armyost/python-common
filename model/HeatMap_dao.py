from sqlalchemy import text

class HeatMapDao:
    def __init__(self, database):
        self.db = database

    def selectGradeCountTemper(self, min_value, max_value, group_id):
        row = self.db.execute(text("""
            SELECT COUNT(*) AS DATACOUNT
            FROM TBSOILDATA 
            WHERE
            GROUPID = :group_id
            AND TEMPERATURE BETWEEN :min_value AND :max_value """),
            {'min_value' : min_value, 
             'max_value' : max_value,
             'group_id' : group_id }
        ).fetchone()
        return {
            'count'      : row['DATACOUNT']
        } if row else None
    
    def selectGradeCountHumid(self, min_value, max_value, group_id):
        row = self.db.execute(text("""
            SELECT COUNT(*) AS DATACOUNT
            FROM TBSOILDATA 
            WHERE 
            GROUPID = :group_id
            AND HUMIDITY BETWEEN :min_value AND :max_value """),
            {'min_value' : min_value, 
             'max_value' : max_value,
             'group_id' : group_id }
        ).fetchone()
        return {
            'count'      : row['DATACOUNT']
        } if row else None
    
    
    # def selectGradeCountAcid(self, min_value, max_value, group_id):
    #     row = self.db.execute(text("""
    #         SELECT COUNT(*) AS DATACOUNT
    #         FROM TBSOILDATA 
    #         WHERE 
    #         GROUPID = :group_id
    #         AND ACIDDATA BETWEEN :min_value AND :max_value """),
    #         {'min_value' : min_value, 
    #          'max_value' : max_value,
    #          'group_id' : group_id }
    #     ).fetchone()
    #     return {
    #         'count'      : row['DATACOUNT']
    #     } if row else None
    
    def selectSoilData(self, group_id, device_id):
        row = self.db.execute(text("""
            SELECT GEOX,
                GEOY,
                HUMIDITY,
                TEMPERATURE,
                REGIDATE
            FROM TBSOILDATA 
            WHERE 
            GROUPID = :group_id
            AND DEVICEID = :device_id
            """), {'device_id' : device_id,
              'group_id' : group_id}
        ).fetchone()
        return {
            'GEOX'      : row['GEOX'],
            'GEOY'      : row['GEOY'],
            'HUMIDITY'   : row['HUMIDITY'],
            'TEMPERATURE'   : row['TEMPERATURE'],
            'REGIDATE' : row['REGIDATE']
        } if row else None

    def selectSoilDataCount(self, group_id):
        row = self.db.execute(text("""
            SELECT count(*) as DATACOUNT
            FROM TBSOILDATA 
            WHERE GROUPID = :group_id
            """),{'group_id' : group_id}
            ).fetchone()
        return {
            'count'      : row['DATACOUNT']
        } if row else None
    
    def selectMaxGeoX(self, group_id):
        row = self.db.execute(text("""
            SELECT GEOX
            FROM TBSOILDATA
            WHERE GROUPID = :group_id
            ORDER BY GEOX DESC
            """),{'group_id' : group_id}
            ).fetchone()
        return {
            'GEOX'      : row['GEOX']
        } if row else None

    def selectMaxGeoY(self, group_id):
        row = self.db.execute(text("""
            SELECT GEOY
            FROM TBSOILDATA
            WHERE GROUPID = :group_id
            ORDER BY GEOY DESC
            """),{'group_id' : group_id}
            ).fetchone()
        return {
            'GEOY'      : row['GEOY']
        } if row else None