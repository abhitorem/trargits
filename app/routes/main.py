import json
from pathlib import Path

from flask import Blueprint, abort, render_template

main_bp = Blueprint("main", __name__)


_CONTENT_PATH = Path(__file__).resolve().parent.parent / "content" / "pages.json"


def _load_page_tree() -> dict:
    with _CONTENT_PATH.open("r", encoding="utf-8") as content_file:
        return json.load(content_file)


def _flatten_nodes(nodes: list[dict]) -> dict[str, dict]:
    result: dict[str, dict] = {}

    for node in nodes:
        slug = node.get("slug")
        if slug:
            result[slug] = node

        children = node.get("children", [])
        result.update(_flatten_nodes(children))

    return result


@main_bp.context_processor
def nav_context() -> dict:
    tree = _load_page_tree()
    return {"tree": tree, "tabs": tree.get("tabs", [])}


@main_bp.get("/")
def home():
    tree = _load_page_tree()
    return render_template("pages/home.html", title="Home", tree=tree)


@main_bp.get("/about")
def about():
    return render_template("pages/about.html", title="About")


@main_bp.get("/services")
def services():
    tree = _load_page_tree()
    services_nodes = tree.get("components", [])
    return render_template("pages/services.html", title="Services", services_nodes=services_nodes)


@main_bp.get("/contact")
def contact():
    return render_template("pages/contact.html", title="Contact")


@main_bp.get("/components/<slug>")
def component_detail(slug: str):
    tree = _load_page_tree()
    all_nodes = _flatten_nodes(tree.get("components", []))
    node = all_nodes.get(slug)
    if not node:
        abort(404)

    return render_template("pages/component.html", title=node.get("label", "Component"), node=node)
