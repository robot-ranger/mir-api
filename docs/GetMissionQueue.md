# GetMissionQueue

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | The id of the mission queue entry | [optional] 
**mission_id** | **str** | The global id of the mission that was executed | [optional] 
**mission** | **str** | The url to the mission that mission that was executed | [optional] 
**state** | **str** | The end state after the mission was executed | [optional] 
**message** | **str** | The last message produced by the actions in the mission list | [optional] 
**ordered** | **datetime** | The date end time when the mission was queued | [optional] 
**started** | **datetime** | The date and time when the missin was started | [optional] 
**finished** | **datetime** | The date and time when the mission was finished | [optional] 
**priority** | **int** | The id of the action | [optional] 
**actions** | **str** | The list of parameters this mission queue entry accepts | [optional] 
**created_by_id** | **str** | The global id of the user who created this entry | [optional] 
**created_by** | **str** | The url to the description of the type of this element | [optional] 
**control_state** | **int** | Mission control state. a value above zero indicates that the robot needs an external input in order to continue | [optional] 
**control_posid** | **str** | Global id of position used during control states | [optional] 
**parameters** | **str** |  | [optional] 
**description** | **str** | Inerited from mission description, when item was queued | [optional] 
**fleet_schedule_guid** | **str** | The guid of the mission scheduler element this mission queue element corresponds to on the fleet | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


