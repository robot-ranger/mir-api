# GetStatus

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**position** | [**GetStatusPosition**](GetStatusPosition.md) |  | [optional] 
**velocity** | [**GetStatusVelocity**](GetStatusVelocity.md) |  | [optional] 
**battery_time_remaining** | **int** | The approximate time remaining on the battery during normal operation of the robot | [optional] 
**battery_percentage** | **float** | The current charge percentage of the battery | [optional] 
**moved** | **float** |  | [optional] 
**mission_queue_id** | **int** | The id of the current job the robot executes | [optional] 
**mission_queue_url** | **str** | The url to the active mission in queue | [optional] 
**mission_text** | **str** | Status message from mission controller | [optional] 
**distance_to_next_target** | **float** | The distance to the next target of the robot | [optional] 
**robot_name** | **str** | The name of the robot | [optional] 
**robot_model** | **str** | The model of the robot | [optional] 
**serial_number** | **str** | The model of the robot | [optional] 
**session_id** | **str** | The id of the session the robot recides in | [optional] 
**state_id** | **int** | The id of the current state of the robot | [optional] 
**state_text** | **str** | A textual description of the current state of the robot | [optional] 
**mode_id** | **int** | The id of the current mode of the robot | [optional] 
**mode_text** | **str** | A textual description of the current state of the robot | [optional] 
**joystick_web_session_id** | **str** | The id of the web user that has control over the joystick | [optional] 
**map_id** | **str** | The id of the current map the robot recides in | [optional] 
**unloaded_map_changes** | **bool** |  | [optional] 
**safety_system_muted** | **bool** |  | [optional] 
**joystick_low_speed_mode_enabled** | **bool** |  | [optional] 
**mode_key_state** | **str** | A textual description of the position of the mode key | [optional] 
**uptime** | **int** | The uptime of the robot | [optional] 
**errors** | [**list[GetStatusErrors]**](GetStatusErrors.md) | The list of actions executed as part of the mission | [optional] 
**footprint** | **str** | The current footprint of the robot | [optional] 
**hook_status** | [**GetStatusHookStatus**](GetStatusHookStatus.md) |  | [optional] 
**hook_data** | [**GetStatusHookData**](GetStatusHookData.md) |  | [optional] 
**user_prompt** | [**GetStatusUserPrompt**](GetStatusUserPrompt.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


