import io
import sys

from approvaltests import verify
from texttest_fixture import main


# E2E test
def test_gilded_rose_approvals():
    orig_sysout = sys.stdout
    try:
        fake_stdout = io.StringIO()
        sys.stdout = fake_stdout
        sys.argv = ["texttest_fixture.py"]
        main(30)
        answer = fake_stdout.getvalue()
    finally:
        sys.stdout = orig_sysout

    verify(answer, reporter=None)


if __name__ == "__main__":
    test_gilded_rose_approvals()
