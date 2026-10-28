import unittest
from intelliterminal.catalog import match_request, find_command, BUNDLES
from intelliterminal.safety import classify_risk, is_allowed_to_run
class Tests(unittest.TestCase):
 def test_hinglish(self): self.assertEqual(match_request("Mujhe ek naya folder banao")["id"],"mkdir")
 def test_git_status(self): self.assertEqual(match_request("please git status check karo")["id"],"git-status")
 def test_branch(self): self.assertEqual(match_request("show current branch")["id"],"git-branch")
 def test_unknown(self): self.assertIsNone(match_request("make me a sandwich"))
 def test_lookup(self): self.assertEqual(find_command("git status")["id"],"git-status")
 def test_bundle(self): self.assertIn("git-summary",BUNDLES)
 def test_risk(self): self.assertIn("HIGH",classify_risk("rm -rf folder"))
 def test_allowlist(self):
  self.assertTrue(is_allowed_to_run(find_command("git status")))
  self.assertFalse(is_allowed_to_run(find_command("df -h")))
if __name__=="__main__": unittest.main()
