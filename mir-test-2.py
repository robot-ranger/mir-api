import mir
import logging
from uuid import uuid4

# Set up logging configuration
logging.basicConfig(
	level=logging.DEBUG,
	format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
	handlers=[
		logging.StreamHandler(),  # Log to console
		# logging.FileHandler('swagger.log')  # Also log to a file
	]
)
# Get a logger for the current module
logger = logging.getLogger(__name__)

MIR_AUTH = "Basic YWRtaW46OGM2OTc2ZTViNTQxMDQxNWJkZTkwOGJkNGRlZTE1ZGZiMTY3YTljODczZmM0YmI4YTgxZjZmMmFiNDQ4YTkxOA=="

def find_mir_position(api_inst:mir.PositionsApi, search_str:str):
	positions = api_inst.positions_get(MIR_AUTH, accept_language="en_US")
	position_guid = None
	for position in positions:
		if position.name == search_str:
			position_guid = position.guid
	if position_guid:
		logger.info(f'Found {search_str}: {position.guid}')
	else:
		logger.info(f'{search_str} not found. Please check the name. Destination must be present on the current MiR Map')
		exit()
	return position_guid

def find_mir_mission(api_inst:mir.MissionsApi, search_str:str):
	missions = api_inst.missions_get(MIR_AUTH, accept_language="en_US")
	mission_guid = None
	for mission in missions:
		if mission.name == search_str:
			mission_guid = mission.guid
	if mission_guid:
		logger.info(f'Found {search_str}: {mission.guid}')
	else:
		logger.info(f'{search_str} not found. Please check the name.')
		exit()
	return mission_guid



if __name__ == "__main__":
	mir_api_client = mir.ApiClient()
	mir_api_client.configuration.host = "http://192.168.12.20/api/v2.0.0"
	mir_status_api = mir.StatusApi(api_client=mir_api_client)
	mir_positions_api = mir.PositionsApi(api_client=mir_api_client)
	mir_missions_api = mir.MissionsApi(api_client=mir_api_client)
	mir_mission_queue_api = mir.MissionQueueApi(api_client=mir_api_client)

	position_guid = find_mir_position(mir_positions_api, "home-chrg-pen")
	mission_guid = find_mir_mission(mir_missions_api, "pr-er-test")
	mission_queue = mir.PostMissionQueues(mission_id=mission_guid, message="hello world", parameters=[{"id": "destination", "value": position_guid}], priority=0)
	logger.info(mission_queue)
	res = mir_mission_queue_api.mission_queue_post(
		MIR_AUTH,
		accept_language="en_US",
		mission_queues=mission_queue
	)
	logger.info(res)
	status = mir.PutStatus(state_id=3)
	res = mir_status_api.status_put(
		MIR_AUTH,
		accept_language="en_US",
		status=status
	)
	logger.info(res)