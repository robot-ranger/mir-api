# GetPosition

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**guid** | **str** | The global id unique across robots that identifies this position | [optional] 
**name** | **str** | The name of the position | [optional] 
**pos_x** | **float** | The x-coordinate of the position relative to origo of the underlying map | [optional] 
**pos_y** | **float** | The y-coordinate of the position relative to origo of the underlying map | [optional] 
**orientation** | **float** | The orientation of the position in degrees relative to origo of the underlying map | [optional] 
**type_id** | **int** | The type of position. see the general description above | [optional] 
**type** | **str** | The url to the description of the type of this position | [optional] 
**map_id** | **str** | The global id of the map this positions belongs to | [optional] 
**parent_id** | **str** | The global id of the possible parent position of the current position. a parent position is a position related to the current position, for instance the parent position of a trolley left entry position is the actual trolley position. if the position does not have a parent position then this field is empty | [optional] 
**parent** | **str** | The url to the possible parent position. if the position does not have a parent position then this field is empty | [optional] 
**docking_offsets** | **str** | The url to the possible docking offset. if the position does not have a docking offset then this field is empty | [optional] 
**map** | **str** | The url to the map this position belongs to | [optional] 
**created_by_id** | **str** | The global id of the user who created this entry | [optional] 
**created_by** | **str** | The url to the description of the type of this position | [optional] 
**help_positions** | **str** |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


