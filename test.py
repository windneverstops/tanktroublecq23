dct = {
    "deleted_objects": [],
    "updated_objects": {
        "tank-2": {
            "type": 1,
            "position": [
                1019.15,
                490.0
            ],
            "velocity": [
                -141.42,
                0.0
            ],
            "hp": 5,
            "powerups": []
        },
        "closing_boundary-1": {
            "type": 6,
            "position": [
                [
                    13.17,
                    986.83
                ],
                [
                    13.17,
                    13.17
                ],
                [
                    1786.83,
                    13.17
                ],
                [
                    1786.83,
                    986.83
                ]
            ],
            "velocity": [
                [
                    10.0,
                    0.0
                ],
                [
                    0.0,
                    10.0
                ],
                [
                    -10.0,
                    0.0
                ],
                [
                    0.0,
                    -10.0
                ]
            ]
        },
        "bullet-1": {
            "type": 2,
            "tank_id": "tank-2",
            "position": [
                669.86,
                490.0
            ],
            "velocity": [
                -450.0,
                0.0
            ],
            "damage": 1
        },
        "bullet-2": {
            "type": 2,
            "tank_id": "tank-2",
            "position": [
                824.15,
                490.0
            ],
            "velocity": [
                -450.0,
                0.0
            ],
            "damage": 1
        },
        "bullet-3": {
            "type": 2,
            "tank_id": "tank-2",
            "position": [
                978.44,
                490.0
            ],
            "velocity": [
                -450.0,
                0.0
            ],
            "damage": 1
        }
    },
    "path_indicators": [
        [
            1150.0,
            490.0
        ],
        [
            1130.0,
            490.0
        ],
        [
            1110.0,
            490.0
        ],
        [
            1090.0,
            490.0
        ],
        [
            1070.0,
            490.0
        ],
        [
            1050.0,
            490.0
        ],
        [
            1030.0,
            490.0
        ],
        [
            1010.0,
            490.0
        ],
        [
            990.0,
            490.0
        ],
        [
            970.0,
            490.0
        ],
        [
            950.0,
            490.0
        ],
        [
            930.0,
            490.0
        ],
        [
            910.0,
            490.0
        ],
        [
            890.0,
            510.0
        ]
    ]
}


for obj_key, obj_data in dct["updated_objects"].items():
    # Check if the "type" property of the current object is equal to 2
    if obj_data.get("type") == 2:
        # If it is, add the object to the list
        print(obj_data)