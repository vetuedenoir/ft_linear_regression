def read_in_file(name: str):
    """
    Reads precomputed parameters (theta0 and theta1) from a file and validates the content.

    Args:
        name (str): The name of the file to read (e.g., "theta.txt").

    Returns:
        tuple: A tuple containing two float values, theta0 and theta1.

    Raises:
        AssertionError: If the file content is incomplete or improperly formatted.
        Exception: If there is an error during file operations.
    """
    try:
        f = open("theta.txt", 'r')
        l1 = f.readline()
        l2 = f.readline()
        f.close()

        assert len(l1) != 0 or len(l2) != 0, \
            "Error: File theta.txt not complete"
        assert l1[:9] == "theta0 = " and l2[:9] == "theta1 = ", \
            "Error: theta not found in file theta.txt"

        theta0 = float(l1[9:])
        theta1 = float(l2[9:])
        return theta0, theta1

    except AssertionError as e:
        print(e)
        exit(1)

    except Exception as e:
        print("Error:", e)
        exit(1)
