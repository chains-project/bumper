```java
import com.jcabi.aspects.Tv;
import org.mockito.Mockito;

public class MkGithub {

  private final Tv tv;

  public MkGithub(Tv tv) {
    this.tv = tv;
  }

  public void addIssue(String repo, String user, String title, String body) {
    Mockito.when(tv.issue(repo, user, title, body)).thenReturn(Mockito.mock(Issue.class));
  }

  public void addPull(String repo, String user, String title, String body) {
    Mockito.when(tv.pull(repo, user, title, body)).thenReturn(Mockito.mock(Pull.class));
  }

  public void addComment(String repo, String issue, String user, String body) {
    Mockito.when(tv.comment(repo, issue, user, body)).thenReturn(Mockito.mock(Comment.class));
  }

  public void addLabel(String repo, String issue, String label) {
    Mockito.when(tv.label(repo, issue, label)).thenReturn(Mockito.mock(Label.class));
  }

  public void addAssignee(String repo, String issue, String assignee) {
    Mockito.when(tv.assignee(repo, issue, assignee)).thenReturn(Mockito.mock(Assignee.class));
  }

  public void addMilestone(String repo, String title, String description, String dueDate) {
    Mockito.when(tv.milestone(repo, title, description, dueDate)).thenReturn(Mockito.mock(Milestone.class));
  }

  public void addCommit(String repo, String branch, String message, String sha) {
    Mockito.when(tv.commit(repo, branch, message, sha)).thenReturn(Mockito.mock(Commit.class));
  }

  public void addTag(String repo, String name, String message, String sha) {
    Mockito.when(tv.tag(repo, name, message, sha)).thenReturn(Mockito.mock(Tag.class));
  }

  public void addRelease(String repo, String tag, String name, String body) {
    Mockito.when(tv.release(repo, tag, name, body)).thenReturn(Mockito.mock(Release.class));
  }

  public void addStatus(String repo, String sha, String state, String description, String targetUrl) {
    Mockito.when(tv.status(repo, sha, state, description, targetUrl)).thenReturn(Mockito.mock(Status.class));
  }

  public void addHook(String repo, String name, String config) {
    Mockito.when(tv.hook(repo, name, config)).thenReturn(Mockito.mock(Hook.class));
  }

  public void addDeploy(String repo, String ref, String environment, String description, String state) {
    Mockito.when(tv.deploy(repo, ref, environment, description, state)).thenReturn(Mockito.mock(Deploy.class));
  }

  public void addPage(String repo, String name, String sha) {
    Mockito.when(tv.page(repo, name, sha)).thenReturn(Mockito.mock(Page.class));
  }

  public void addBlob(String repo, String sha, String content) {
    Mockito.when(tv.blob(repo, sha, content)).thenReturn(Mockito.mock(Blob.class));
  }

  public void addTree(String repo, String sha, String baseTree, String path) {
    Mockito.when(tv.tree(repo, sha, baseTree, path)).thenReturn(Mockito.mock(Tree.class));
  }

  public void addCommitComment(String repo, String sha, String body) {
    Mockito.when(tv.commitComment(repo, sha, body)).thenReturn(Mockito.mock(CommitComment.class));
  }

  public void addGist(String description) {
    Mockito.when(tv.gist(description)).thenReturn(Mockito.mock(Gist.class));
  }

  public void addGistFile(String gist, String name, String content) {
    Mockito.when(tv.gistFile(gist, name, content)).thenReturn(Mockito.mock(GistFile.class));
  }

  public void addOrg(String login) {
    Mockito.when(tv.org(login)).thenReturn(Mockito.mock(Org.class));
  }

  public void addRepo(String org, String name) {
    Mockito.when(tv.repo(org, name)).thenReturn(Mockito.mock(Repo.class));
  }

  public void addUser(String login) {
    Mockito.when(tv.user(login)).thenReturn(Mockito.mock(User.class));
  }

  public void addTeam(String org, String name) {
    Mockito.when(tv.team(org, name)).thenReturn(Mockito.mock(Team.class));
  }

  public void addMembership(String org, String user, String role) {
    Mockito.when(tv.membership(org, user, role)).thenReturn(Mockito.mock(Membership.class));
  }

  public void addEvent(String repo, String event, String action, String issue, String comment, String pull, String commit, String push, String pages, String release, String deployment, String status, String gist, String gollum, String issueComment, String member, String public, String team, String watch) {
    Mockito.when(tv.event(repo, event, action, issue, comment, pull, commit, push, pages, release, deployment, status, gist, gollum, issueComment, member, public, team, watch)).thenReturn(Mockito.mock(Event.class));
  }

  public void addHookDelivery(String id, String code, String status) {
    Mockito.when(tv.hookDelivery(id, code, status)).thenReturn(Mockito.mock(HookDelivery.class));
  }

  public void addIntegration(String installation, String repo, String event, String action, String issue, String comment, String pull, String commit, String push, String pages, String release, String deployment, String status, String gist, String gollum, String issueComment, String member, String public, String team, String watch) {
    Mockito.when(tv.integration(installation, repo, event, action, issue, comment, pull, commit, push, pages, release, deployment, status, gist, gollum, issueComment, member, public, team, watch)).thenReturn(Mockito.mock(Integration.class));
  }

  public void addMarketplacePurchase(String account, String plan, String status) {
    Mockito.when(tv.marketplacePurchase(account, plan, status)).thenReturn(Mockito.mock(MarketplacePurchase.class));
  }

  public void addMarketplaceStub(String owner, String repo, String plan, String status) {
    Mockito.when(tv.marketplaceStub(owner, repo, plan, status)).thenReturn(Mockito.mock(MarketplaceStub.class));
  }

  public void addMeta(String key, String value) {
    Mockito.when(tv.meta(key, value)).thenReturn(Mockito.mock(Meta.class));
  }

  public void addNotification(String repo, String subject, String reason, String unread) {
    Mockito.when(tv.notification(repo, subject, reason, unread)).thenReturn(Mockito.mock(Notification.class));
  }

  public void addPing(String hook) {
    Mockito.when(tv.ping(hook)).thenReturn(Mockito.mock(Ping.class));
  }

  public void addRepoPush(String repo, String ref, String sha, String head, String before, String size, String distinctSize, String commit) {
    Mockito.when(tv.repoPush(repo, ref, sha, head, before, size, distinctSize, commit)).thenReturn(Mockito.mock(RepoPush.class));
  }

  public void addRepoStatus(String repo, String sha, String state, String targetUrl, String description, String context) {
    Mockito.when(tv.repoStatus(repo, sha, state, targetUrl, description, context)).thenReturn(Mockito.mock(RepoStatus.class));
  }

  public void addUserBlock(String username, String reason) {
    Mockito.when(tv.userBlock(username, reason)).thenReturn(Mockito.mock(UserBlock.class));
  }

  public void addUserEmail(String username, String email) {
    Mockito.when(tv.userEmail(username, email)).thenReturn(Mockito.mock(UserEmail.class));
  }

  public void addUserKey(String username, String title, String key) {
    Mockito.when(tv.userKey(username, title, key)).thenReturn(Mockito.mock(UserKey.class));
  }

  public void addUserSsh(String username, String title, String key) {
    Mockito.when(tv.userSsh(username, title, key)).thenReturn(Mockito.mock(UserSsh.class));
  }

  public void addVerification(String payload, String signature) {
    Mockito.when(tv.verification(payload, signature)).thenReturn(Mockito.mock(Verification.class));
  }

  public void addWebhook(String id, String name, String config, String events, String active) {
    Mockito.when(tv.webhook(id, name, config, events, active)).thenReturn(Mockito.mock(Webhook.class));
  }

}
```