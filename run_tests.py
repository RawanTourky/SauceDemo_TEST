import pytest
import os
from datetime import datetime
import webbrowser


def run_tests():
    if not os.path.exists('reports'):
        os.makedirs('reports')

    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    report_name = f"reports/report_{timestamp}.html"

    pytest_args = [
        "-v",
        "--html=" + report_name,
        "--self-contained-html",
        "-s",
        "--capture=tee-sys"
    ]

    # Run the tests
    pytest.main(pytest_args)

    # Get absolute path of report
    report_path = os.path.abspath(report_name)
    print(f"\nReport generated: {report_path}")

    # Open report in Edge browser
    try:
        webbrowser.get('edge').open('file://' + report_path)
    except Exception as e:
        print(f"Could not open report automatically: {e}")
        print("Please open the report manually from the reports directory")


if __name__ == "__main__":
    run_tests()