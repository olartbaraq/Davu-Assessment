from flask import render_template, request, jsonify, Blueprint
import logging


bp = Blueprint("main", __name__, url_prefix="/api/experimental/dags")

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def initiate_dag(dag_id, dag_run_id, conf):
    dags = {}
    if dag_id not in dags:
        dags[dag_id] = []

    dag_run = {"dag_run_id": dag_run_id, "dag_id": dag_id, "conf": conf}
    dags[dag_id].append(dag_run)

    logger.info(f"Successfully created DAG run ID :{dag_run_id} for DAG ID: {dag_id}")
    return (
        jsonify(
            {
                "dag_run_id": dag_run_id,
                "message": f"Created DAG Run for {dag_id}",
                "conf": conf,
            }
        ),
        201,
    )


@bp.route("/", methods=["GET"])
def index():
    return render_template("index.html")


@bp.route("/create_dag", methods=["POST"])
def create_dag():
    data = request.json
    dag_id = data.get("dag_id")
    dag_run_id = data.get("dag_run_id")
    conf = data.get("conf", {})

    if not dag_id or not dag_run_id:
        return jsonify({"error": "Missing dag_id or dag_run_id"}), 400

    response, status_code = initiate_dag(dag_id, dag_run_id, conf)
    return response, status_code
