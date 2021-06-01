from velocloud.models import error


class TestError(object):
    def test_error(self):
        e = error.Error(
            code=5,
            message='VCO Test Error',
            data=error.ErrorData(
                valid=True,
                error=list(error.ValidationErrorDetails(
                    code='Fake error code',
                    message='Fake error message',
                    path='Fake error path'
                ))
            )
        )


class TestWarning(object):
    def test_warning(self):
        e = error.Error(
            code=5,
            message='VCO Test Error',
            data=error.ErrorData(
                valid=True,
                warning=list(error.ValidationErrorDetails(
                    code='Fake warning code',
                    message='Fake warning message',
                    path='Fake warning path'
                ))
            )
        )
