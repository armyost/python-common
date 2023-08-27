from flask      import request, jsonify, current_app, Response, g
from flask.json import JSONEncoder
from threading  import Thread


def create_endpoints(app, services):
    app.json_encoder = JSONEncoder

    @app.route("/ping", methods=['GET'])
    def ping():
        return "pong"

    @app.route('/listTopic', methods=['GET'])
    def listTopic():
        dataList    = services.KafkaCollectorService.topicList()
        return dataList
            
    @app.route('/listEndpoint', methods=['GET'])
    def listEndpoint():
        return jsonify({'devices' : services.EndpointService.endpointList()})
    
    @app.route('/detailEndpointGroup/<group_id>', methods=['GET'])
    def detailEndpoint(group_id):
        return jsonify({'device_info' : services.EndpointService.endpointInfoDetail(group_id, 1)})
        
    ## 미완성    
    @app.route("/modifyEndpointInfo/<group_id>", methods=['GET'])
    def modifyEndpointInfo(group_id):
        endpoint_url = services.EndpointService.endpointUrlFind(group_id)
        endpoint_response = services.EndpointService.endpointInfoApiDetail(endpoint_url)
        services.EndpointService.endpointInfoModify(group_id, endpoint_response)
        return endpoint_response

    @app.route('/listConsumerGroup', methods=['GET'])
    def listConsumerGroup():
        targetList  = services.KafkaCollectorService.consumerGroupList()
        return targetList

    @app.route('/detailSoilData/<group_id>/<device_id>', methods=['GET'])
    def detailSoilData(group_id, device_id):
        dataTuple  = services.HeatMapService.soilDataDetail(group_id, device_id)
        return jsonify(dataTuple)
    
    @app.route('/findSoilDataCount/<group_id>', methods=['GET'])
    def findSoilDataCount(group_id):
        dataTuple  = services.HeatMapService.soilDataCountFind(group_id)
        return jsonify(dataTuple)
    
    @app.route('/findMaxGeoX/<group_id>', methods=['GET'])
    def findMaxGeoX(group_id):
        dataTuple  = services.HeatMapService.maxGeoXFind(group_id)
        return jsonify(dataTuple)
    
    @app.route('/findMaxGeoY/<group_id>', methods=['GET'])
    def findMaxGeoY(group_id):
        dataTuple  = services.HeatMapService.maxGeoYFind(group_id)
        return jsonify(dataTuple)

    @app.route('/listGradeCount/humid/<group_id>', methods=['GET'])
    def listGradeCountHumid(group_id):
        dataTuple  = services.HeatMapService.gradeCountHumidList(group_id)
        return jsonify(dataTuple)
    
    @app.route('/listGradeCount/temper/<group_id>', methods=['GET'])
    def listGradeCountTemper(group_id):
        dataTuple  = services.HeatMapService.gradeCountTemperList(group_id)
        return jsonify(dataTuple)
    
    # @app.route('/listGradeCount/acid/<group_id>', methods=['GET'])
    # def listGradeCountAcid(group_id):
    #     dataTuple  = services.HeatMapService.gradeCountAcidList(group_id)
    #     return jsonify(dataTuple)

    @app.route('/subscribSoilData', methods=['GET'])
    def subscribSoilData():
        thread = Thread(target=services.KafkaCollectorService.SoilDataSubscribeAndModify)
        thread.daemon = True
        thread.start()
        return jsonify({'thread_name': str(thread.name), 'started': True})
