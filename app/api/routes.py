from app.api import bp, controllers


@bp.route("/test", methods=["GET"])
def create_test():
    return controllers.create_test_controller()


@bp.route("/users", methods=["POST"])
def create_user():
    return controllers.create_user_controller()
