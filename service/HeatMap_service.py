class HeatMapService:
    def __init__(self, HeatMapDao):
        self.HeatMapDao = HeatMapDao

    def gradeCountHumidList(self, group_id):
        lv1 = self.HeatMapDao.selectGradeCountHumid('0', '50',group_id)
        lv2 = self.HeatMapDao.selectGradeCountHumid('51', '70',group_id)
        lv3 = self.HeatMapDao.selectGradeCountHumid('71', '80',group_id)
        lv4 = self.HeatMapDao.selectGradeCountHumid('81', '90',group_id)
        lv5 = self.HeatMapDao.selectGradeCountHumid('91', '100',group_id)
        lv1['level'] = 'lv1'
        lv2['level'] = 'lv2'
        lv3['level'] = 'lv3'
        lv4['level'] = 'lv4'
        lv5['level'] = 'lv5'
        issueCountTuple = (lv1, lv2, lv3, lv4, lv5)
        # print(issueCountTuple)
        return issueCountTuple

    # def gradeCountAcidList(self, group_id):
    #     lv1 = self.HeatMapDao.selectGradeCountAcid('0', '6.0',group_id)
    #     lv2 = self.HeatMapDao.selectGradeCountAcid('6.0', '6.4',group_id)
    #     lv3 = self.HeatMapDao.selectGradeCountAcid('6.4', '6.7',group_id)
    #     lv4 = self.HeatMapDao.selectGradeCountAcid('6.7', '7.0',group_id)
    #     lv5 = self.HeatMapDao.selectGradeCountAcid('7.0', '7.5',group_id)
    #     lv6 = self.HeatMapDao.selectGradeCountAcid('7.5', '100',group_id)
    #     lv1['level'] = 'lv1'
    #     lv2['level'] = 'lv2'
    #     lv3['level'] = 'lv3'
    #     lv4['level'] = 'lv4'
    #     lv5['level'] = 'lv5'
    #     lv6['level'] = 'lv6'
    #     issueCountTuple = (lv1, lv2, lv3, lv4, lv5, lv6)
    #     # print(issueCountTuple)
    #     return issueCountTuple
    
    def gradeCountTemperList(self, group_id):
        lv1 = self.HeatMapDao.selectGradeCountTemper('0', '10',group_id)
        lv2 = self.HeatMapDao.selectGradeCountTemper('10.1', '20',group_id)
        lv3 = self.HeatMapDao.selectGradeCountTemper('20.1', '25',group_id)
        lv4 = self.HeatMapDao.selectGradeCountTemper('25.1', '30',group_id)
        lv5 = self.HeatMapDao.selectGradeCountTemper('30.1', '35',group_id)
        lv6 = self.HeatMapDao.selectGradeCountTemper('35.1', '40',group_id)
        lv1['level'] = 'lv1'
        lv2['level'] = 'lv2'
        lv3['level'] = 'lv3'
        lv4['level'] = 'lv4'
        lv5['level'] = 'lv5'
        lv6['level'] = 'lv6'
        issueCountTuple = (lv1, lv2, lv3, lv4, lv5, lv6)
        # print(issueCountTuple)
        return issueCountTuple
    
    def soilDataDetail(self, group_id, device_id):
        resultMap = self.HeatMapDao.selectSoilData(group_id, device_id)
        return resultMap
    
    def soilDataCountFind(self, group_id):
        resultMap = self.HeatMapDao.selectSoilDataCount(group_id)
        return resultMap
    
    def maxGeoXFind(self, group_id):
        resultMap = self.HeatMapDao.selectMaxGeoX(group_id)
        return resultMap
    
    def maxGeoYFind(self, group_id):
        resultMap = self.HeatMapDao.selectMaxGeoY(group_id)
        return resultMap

        




