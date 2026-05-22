from pydantic import BaseModel, Field
from typing import Annotated, Literal

class IncomePredictionRequest(BaseModel):
    age: Annotated[
        int,
        Field(..., gt=0, lt=120, description="Age of the individual")
    ]
    workclass: Annotated[
        Literal[
            'Private', 'Local-gov', 'Self-emp-not-inc', 'Federal-gov', 'State-gov', 'Self-emp-inc', 'Without-pay', 'Never-worked'
        ], 
        Field(..., description="Type of employment sector of the individual")
    ]
    fnlwgt: Annotated[
        int,
        Field(..., description="Final weight assigned by census (statistical weight)")
    ]
    education: Annotated[
        Literal[
            '11th', 'HS-grad', 'Assoc-acdm', 'Some-college', '10th',
            'Prof-school', '7th-8th', 'Bachelors', 'Masters', 'Doctorate',
            '5th-6th', 'Assoc-voc', '9th', '12th', '1st-4th', 'Preschool'
        ],
        Field(..., description="Highest education level")
    ]
    educational_num: Annotated[
        int,
        Field(..., alias="educational-num", ge=1, description="Number of years of education") 
    ]
    marital_status: Annotated[
        Literal[
            'Never-married', 'Married-civ-spouse', 'Widowed', 'Divorced',
            'Separated', 'Married-spouse-absent', 'Married-AF-spouse'
        ],
        Field(..., alias="marital-status", description="Marital status of the individual")
    ]
    occupation: Annotated[
        str,
        Field(..., description="Occupation type")
    ]
    relationship: Annotated[
        Literal[
            'Own-child', 'Husband', 'Not-in-family', 'Unmarried', 'Wife',
            'Other-relative'
        ],
        Field(..., description="Relationship status in family")
    ]
    race: Annotated[
        str,
        Field(..., description="Race of the individual")
    ]
    gender: Annotated[
        Literal[
            'Male', 'Female'
        ],
        Field(..., description="Gender of the individual")
    ]
    capital_gain: Annotated[
        int,
        Field(..., alias="capital-gain", ge=0, description="Capital gain")
    ]
    capital_loss: Annotated[
        int,
        Field(..., alias="capital-loss", description="Capital Loss")
    ]
    hours_per_week: Annotated[
        int,
        Field(..., alias="hours-per-week", ge=1, le=100, description="Working hours per week")
    ]
    native_country: Annotated[
        str,
        Field(..., alias="native-country", description="Country of origin")
    ]
    