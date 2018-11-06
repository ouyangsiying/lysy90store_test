{
  "actions":
  [
    {
      "action": [
        {
          "api": "login",
          "data": "login"
        },
        {
          "api": "place_order",
          "data": "place_order"
        }
      ]
    }
  ],
  "data": {
    "login": {
      "check": 0,
      "test_datas": [
        {
          "Interface_description":"登录的测试数据",
          "input": {
            "user_name": "person111",
            "password": "111111"
          },
          "output": {
          }
        }
      ]
    },
    "place_order": {
      "check": 2,
      "test_datas": [
        {
          "Interface_description":"提交正常的订单信息",
          "input": {
            "is_cart": 0,
            "is_custom": 0,
            "receiving_id": 16,
            "shipping_id": 0,
            "invoice_belong": 1,
            "goods_list": "[{'sku':'QY-SK-C17S201AAZ1-THIN-B-S','goods_count':1}]"
          },
          "output": {
            "errno": 0,
            "result": {
              "order_id": 1693
            }
          }
        }
      ]
    }
  }
}