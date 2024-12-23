from collections import OrderedDict

station_map = {"Como Outlet":"1013", 'Curtiss Pond':'1015', 'Victoria Park Pond':'1020', 'TBNS - Magnolia':'1046', 'Alameda Pond':'1055', 'Parkview Filter Bay':'1057', 
               'Arlington-Jackson':'1058', 'Como B5 Outlet | Como B5':'1069', 'Como Zoo Infiltration Basin':'1072', 'Como Zoo Bypass':'1073', 'Como Lake - STA 102':'COMO102', 
               'Como Lake - STA 201':'COMO201', 'Como Lake - STA 202':'COMO202', 'Crosby Lake - STA 201':'CROSBY201', 'St. Anthony Park':'CRWD1', 'Villa Park Outlet':'CRWD10', 
               'Villa Park Inlet':'CRWD11', 'Parkview Center School - System Inlet':'CRWD167', 'Parkview Center School - Filter Bay Inlet':'CRWD168', 
               'Parkview Center School - Filter Bay Outlet':'CRWD169', 'Seminary Pond Outlet':'CRWD170', 'TBNS - Maryland Pond':'CRWD171', 
               'TBNS - Maryland IESF Outlet':'CRWD172', 'TBNS - Magnolia Pond':'CRWD173', 'TBNS - Magnolia IESF Outlet':'CRWD174', 'GC Pond NE IESF Outlet':'CRWD186', 
               'GC Pond SW IESF Outlet':'CRWD187', 'Seminary Pond N IESF Outlet':'CRWD188', 'Seminary Pond S IESF Outlet':'CRWD189', 'Seminary Pond':'CRWD190', 
               'East Kittsondale':'CRWD2', 'Como 3 | Como D':'CRWD21', 'GC Pond IESF Outlet':'CRWD220', 'Como Zoo Inlet':'CRWD222', 'Trout Brook Outlet':'CRWD3', 
               'Willow Reserve - Inlet':'CRWD31', 'Willow Reserve - Outlet':'CRWD32', 'William Street Pond - Pond (WS Pond 3)':'CRWD36', 'William Street Pond - N Filter':'CRWD38', 
               'William Street Pond - S Filter':'CRWD39', 'Trout Brook - West Branch':'CRWD4', 'TBNS - Rose':'CRWD43', 'Phalen Creek':'CRWD5', 'Como 7 | Como B5':'CRWD6', 
               'Willow Reserve':'CRWD63', 'Como Lake':'CRWD66', 'Golf Course Pond':'CRWD70', 'Trout Brook - East Branch':'CRWD8', 'Loeb Lake - STA 201':'LOEB201', 
               'McCarrons Lake - STA 101':'MCCARRONS101'}

station_map = OrderedDict(sorted(station_map.items()))

parameter_map = {"Total Phosphorus": "Total%20Phosphorus",
                 "Dissolved Phosphorus": "Dissolved%20Phosphorus",
                 "Orthophosphate as P": "Orthophosphate%20as%20P",
                 "Total Suspended Solids": "Total%20Suspended%20Solids",
                 "Cadmium": "Cadmium",
                 "Calcium": "Calcium",
                 "Chloride": "Chloride"}