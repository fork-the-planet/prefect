import { ActionChangeFlowRunStateFields } from "./action-change-flow-run-state-fields";
import type { ActionsSchema } from "./action-type-schemas";

type ActionTypeAdditionalFieldsProps = {
	actionType: ActionsSchema["type"];
};

export const ActionTypeAdditionalFields = ({
	actionType,
}: ActionTypeAdditionalFieldsProps) => {
	switch (actionType) {
		case "change-flow-run-state":
			return <ActionChangeFlowRunStateFields />;
		case "run-deployment":
		case "pause-deployment":
		case "resume-deployment":
			return <div>TODO Deployment</div>;
		case "pause-work-queue":
		case "resume-work-queue":
			return <div>TODO Work Queue</div>;
		case "pause-work-pool":
		case "resume-work-pool":
			return <div>TODO Work pool</div>;
		case "pause-automation":
		case "resume-automation":
			return <div>TODO Automation</div>;
		case "send-notification":
			return <div>TODO send notification</div>;
		case "cancel-flow-run":
		case "suspend-flow-run":
		case "resume-flow-run":
		default:
			return null;
	}
};