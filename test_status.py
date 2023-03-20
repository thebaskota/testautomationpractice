import test_logger

log = test_logger.test_logger()


def assert_true(result, result_message):
    """
    call this for a Positive hard assert in the test

    :param result: result of a test, should be true or false
    :param result_message: the message to be logged
    :return: None
    """
    if result:
        log.info(f"### VERIFICATION SUCCESSFUL :: {result_message}")
        assert True
    else:
        log.error(f"### VERIFICATION FAILED :: {result_message}")
        assert False


def assert_false(result, result_message):
    """
    call this for a negative hard assert in the test

    :param result: result of a test, should be true or false
    :param result_message: the message to be logged
    :return: None
    """
    if result is False:
        log.info(f"### VERIFICATION SUCCESSFUL :: {result_message}")
        assert True
    else:
        log.error(f"### VERIFICATION FAILED :: {result_message}")
        assert False
