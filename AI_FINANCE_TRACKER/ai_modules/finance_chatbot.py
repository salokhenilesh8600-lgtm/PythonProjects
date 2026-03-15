def chat(df, question):

    food = df[df["category"]=="Food"]["amount"].sum()
    total = df["amount"].sum()

    if "save" in question:
        return "Reduce food spending and subscriptions."

    if "food" in question:
        return f"You spent ₹{food} on food."

    if "budget" in question:
        return f"Total spending so far ₹{total}"

    return "Track expenses daily to improve savings."