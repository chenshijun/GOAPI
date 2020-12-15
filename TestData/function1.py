def get_url():
    return ["deepexi-system-digital-retail-mobile-service/api/v1/promotion/activity/couponLogger/userAbleUse"]


def get_data():
    return [
        {
            "desc": "测试一个api1",
            "data": {
                "appId": "1196271598647115865",
                "activityInfoQueryList": [{
                    "skuInfoList": [{
                        "detailPrice": "10.00",
                        "brandId": 358,
                        "categoryId": 312,
                        "skuId": 5198,
                        "tradeType": 1,
                        "skuAmount": 1
                    }],
                    "shopId": 14,
                    "skuIdList": [5198]
                }],
                "selectedCouponLoggerIdList": [],
                "tenantId": "bbf981fd0e654f7c90470bc865d83690"
            }
        },
        {
            "desc": "测试一个api2",
            "data": {
                "appId": "1196271598647115865",
                "activityInfoQueryList": [{
                    "skuInfoList": [{
                        "detailPrice": "10.00",
                        "brandId": 358,
                        "categoryId": 312,
                        "skuId": 5198,
                        "tradeType": 1,
                        "skuAmount": 1
                    }],
                    "shopId": 14,
                    "skuIdList": [5198]
                }],
                "selectedCouponLoggerIdList": [],
                "tenantId": "bbf981fd0e654f7c90470bc865d83690"
            }
        }

    ]
