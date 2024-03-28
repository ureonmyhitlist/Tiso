from fastapi import APIRouter,Depends
from typing import List
from service.shelter import ShelterService
from schema.response import ShelterInfoSchema, ShelterRespSchema


router=APIRouter(prefix="/shelters",tags=["shelters"])

@router.get("/now", status_code=200)
def get_near_shelter(lat: float, lng: float, shelter_service: ShelterService = Depends()) -> ShelterRespSchema:
        print({lat})
        print({lng})
        user_location = [lng, lat]  # MongoDB는 [경도, 위도] 순서를 사용
        shelter_list = shelter_service.get_near_service(user_location)
        return ShelterRespSchema(data= { "shelterList" : [ShelterInfoSchema.from_odm_to_schema(shelter_info) for shelter_info in shelter_list]} )