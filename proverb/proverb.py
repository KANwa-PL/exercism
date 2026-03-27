def proverb(*args, qualifier):
    result = [f"For want of a {i} the {k} was lost." for i, k in zip(args,args[1:])]
    if qualifier is not None:
        result.append(f"And all for the want of a {qualifier} {args[0]}.")
    elif len(args) > 0:
        result.append(f"And all for the want of a {args[0]}.")
    return result


print(proverb("nail", "shoe", "horse", qualifier="iron"))