from flask import Blueprint, jsonify

bp = Blueprint("main", __name__)


@bp.get("/health")
def health():
    return jsonify({"status": "ok"})


@bp.get("/items")
def list_items():
    items = [
        {"id": 1, "name": "Widget"},
        {"id": 2, "name": "Gadget"},
        {"id": 3, "name": "Doohickey"},
    ]
    return jsonify(items)


@bp.get("/items/<int:item_id>")
def get_item(item_id: int):
    items = {
        1: {"id": 1, "name": "Widget"},
        2: {"id": 2, "name": "Gadget"},
        3: {"id": 3, "name": "Doohickey"},
    }
    item = items.get(item_id)
    if item is None:
        return jsonify({"error": "not found"}), 404
    return jsonify(item)