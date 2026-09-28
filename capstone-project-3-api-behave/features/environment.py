def after_scenario(context, scenario):
    client = getattr(context, "client", None)
    if client is None:
        return

    if getattr(context, "user_created", False) and not getattr(
        context, "user_deleted", False
    ):
        try:
            client.delete_user(
                context.user["email"], context.user["password"]
            )
        except Exception as exc:
            print(f"Temporary account cleanup failed: {exc}")

    client.close()