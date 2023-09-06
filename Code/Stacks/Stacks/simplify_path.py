def simply_path(spath):
    # Initialize a stack
    stack = []

    # Split the input string on "/" as the delimiter
    # and process each portion one by one
    for portion in spath.split("/"):

        # If the current component is a "..", then
        # we pop an entry from the stack if it's non-empty
        if portion == "..":
            if stack:
                stack.pop()
        elif portion == "." or not portion:
                # A no-op for a "." or an empty string
            continue
        else:
                # Finally, a legitimate directory name, so we add it
                # to our stack
            stack.append(portion)

    # Stich together all the directory names together
    final_str = "/" + "/".join(stack)
    return final_str

spath = "/a/./b/../../c/"
spath = "/../"
ans = simply_path(spath)
print("The original path is: ",spath)
print("The canonical path is: ",ans)