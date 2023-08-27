from sqlalchemy import text

class EndpointDao:
    def __init__(self, database):
        self.db = database
        
    def selectEndpointAll(self):
        rows = self.db.execute(text("""
            SELECT *
            FROM TBENDLIST """)
        ).fetchall()
        return [{
            'GROUPID' : row['GROUPID'],
            'TYPEID' : row['TYPEID'],
            'TYPEDESC' : row['TYPEDESC'],
            'DEVICEDESC' : row['DEVICEDESC'],
            'REGIDATE' : row['REGIDATE'],
            'OWNER' : row['OWNER'],
            'USEYN' : row['USEYN']
        } for row in rows]
    
    def selectEndpointInfo(self, group_id, device_id):
        row = self.db.execute(text("""
            SELECT *
            FROM TBENDLIST 
            WHERE GROUPID = :group_id
            AND DEVICEID = :device_id
            """), {
                'group_id' : group_id,
                'device_id' : device_id
            }).fetchone()
        return {
            'GROUPID' : row['GROUPID'],
            'TYPEID' : row['TYPEID'],
            'TYPEDESC' : row['TYPEDESC'],
            'DEVICEDESC' : row['DEVICEDESC'],
            'REGIDATE' : row['REGIDATE'],
            'OWNER' : row['OWNER'],
            'URL' : row['URL'],
            'USEYN' : row['USEYN'],
            'LATITUDE' : row['LATITUDE'],
            'LONGITUDE' : row['LONGITUDE']
        } if row else None
    
    def selectEndpointUrl(self, group_id):
        row = self.db.execute(text("""
            SELECT URL
            FROM TBENDLIST 
            WHERE GROUPID = :group_id
            """), {
                'group_id' : group_id
            }).fetchone()
        return {
            'URL' : row['URL']
        } if row else None

    def updateEndpointLocation(self, group_id, endpoint_response):
        return self.db.execute(text("""
            UPDATE TBENDLIST SET
            latitude = :latitude
            longitude = :longitude
            WHERE group_id = :group_id
            """), {
                'group_id'     : group_id,
                'latitude'      : endpoint_response.latitude,
                'longitude'     : endpoint_response.longitude
            }).rowcount