#!/usr/bin/env python3


'''
Viết script tìm 50 quán bia / quán nhậu / quán bar / nhà hàng quanh toạ độ của lớp học (lên google map để lấy) với bán kính 2KM.
Ghi kết quả theo định dạng JSON vào file pymi_beer.geojson

Sử dụng Google Map API
https://developers.google.com/places/web-service/

Chú ý: phải tạo "token" để có thể truy cập API.

Chú ý: giữa mỗi trang kết quả phải đợi để lấy tiếp.

- Kết quả trả về lưu theo format JSON, với mỗi điểm là một GeoJSON point (https://leafletjs.com/examples/geojson/), up file này lên GitHub để xem bản đồ kết quả.

- Xem mẫu GEOJSON https://github.com/tung491/make_boba_map

'''

path = '/Users/laiminhduy/pyfml/exercises/beerspot_api.txt'

with open(path) as f:
    api_key = f.readline()
    f.close

print(api_key)

api = 'AIzaSyCmlzFlcbG-b8QtfNBM7EBbBn_CmKvybhQ'