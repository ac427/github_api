from github import Github
import ConfigParser

Config = ConfigParser.ConfigParser()
Config.read("config")
GITHUB_TOKEN=Config.get ("config", "GITHUB_TOKEN")
GITHUB_USERNAME=Config.get ("config", "GITHUB_USERNAME")

org_input = raw_input('What github org you want to update?')

g = Github(base_url="https://github.va.opower.it/api/v3", login_or_token=GITHUB_TOKEN)
org = g.get_organization(org_input)
repos = org.get_repos()
for repo in repos:
  branches = g.get_repo(repo.full_name).get_branches()
  for branch in branches:
    print "updating "+ repo.full_name +" settings"
    update_branch = g.get_repo(repo.full_name).get_branch(branch.name)
    #edit_protection(self, strict=NotSet, contexts=NotSet, enforce_admins=NotSet, dismissal_users=NotSet, dismissal_teams=NotSet, dismiss_stale_reviews=NotSet, require_code_owner_reviews=NotSet, required_approving_review_count=NotSet, user_push_restrictions=NotSet, team_push_restrictions=NotSet)
#    update_branch.edit_protection(True,[],True,[],[],False,True,1,[],[])
#    removing restricut who can push to branch. This allows group with write to merge branches on approval 
    update_branch.edit_protection(True,[],True,[],[],False,True,1)
