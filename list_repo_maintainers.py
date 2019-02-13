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
  print "For repo - " + repo.full_name
  for teams in repo.get_teams():
  #https://developer.github.com/v3/teams/members/#list-team-members
    print "Maintainer Teams Members" 
    for member in teams.get_members('maintainer'):
        print teams.name + "  " + member.name
  print "Collaborators and their permissions"
  for user in repo.get_collaborators():
    print user.login + "--> " +repo.get_collaborator_permission(user)
