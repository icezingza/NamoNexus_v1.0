import unittest
from unittest.mock import patch, MagicMock
from engine.supervisor import is_healthy, monitor, restart_process

class TestSupervisor(unittest.TestCase):

    @patch('engine.supervisor.requests.get')
    def test_is_healthy_true(self, mock_get):
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_get.return_value = mock_response
        self.assertTrue(is_healthy("http://localhost:8080/health"))

    @patch('engine.supervisor.requests.get')
    def test_is_healthy_false(self, mock_get):
        mock_response = MagicMock()
        mock_response.status_code = 500
        mock_get.return_value = mock_response
        self.assertFalse(is_healthy("http://localhost:8080/health"))

    @patch('engine.supervisor.requests.get')
    def test_is_healthy_exception(self, mock_get):
        mock_get.side_effect = Exception("Connection refused")
        self.assertFalse(is_healthy("http://localhost:8080/health"))

    @patch('engine.supervisor.subprocess.Popen')
    def test_restart_process(self, mock_popen):
        restart_process("Test Process", "echo test")
        mock_popen.assert_called_with("echo test", shell=True)

    @patch('engine.supervisor.time.sleep')
    @patch('engine.supervisor.restart_process')
    @patch('engine.supervisor.is_healthy')
    def test_monitor(self, mock_is_healthy, mock_restart, mock_sleep):
        # Setup mocks to run the loop once then raise StopIteration or similar to break,
        # but since monitor is while True, we can throw an exception to break it

        # Scenario: API Unhealthy, Dash Healthy
        mock_is_healthy.side_effect = [False, True]
        mock_sleep.side_effect = InterruptedError("Break Loop") # To break the while True loop

        try:
            monitor()
        except InterruptedError:
            pass

        mock_restart.assert_called_once()
        args, _ = mock_restart.call_args
        self.assertEqual(args[0], "API Gateway")

if __name__ == '__main__':
    unittest.main()
