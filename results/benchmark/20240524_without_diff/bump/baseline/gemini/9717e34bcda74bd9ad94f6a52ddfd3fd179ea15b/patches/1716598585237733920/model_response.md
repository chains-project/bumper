```java
  import com.jcabi.aspects.Tv;
  import com.jcabi.aspects.Tv.TvException;

  public class MkGithub {

    private final Tv tv;

    public MkGithub(Tv tv) {
      this.tv = tv;
    }

    public void createRepo(String owner, String name) throws TvException {
      tv.play(owner, name);
    }

    public void deleteRepo(String owner, String name) throws TvException {
      tv.stop(owner, name);
    }

    public void commit(String owner, String name, String message) throws TvException {
      tv.record(owner, name, message);
    }

    public void push(String owner, String name, String branch) throws TvException {
      tv.rewind(owner, name, branch);
    }

    public void pull(String owner, String name, String branch) throws TvException {
      tv.forward(owner, name, branch);
    }

    public void branch(String owner, String name, String branch) throws TvException {
      tv.pause(owner, name, branch);
    }

    public void tag(String owner, String name, String tag) throws TvException {
      tv.mute(owner, name, tag);
    }

    public void release(String owner, String name, String tag) throws TvException {
      tv.unmute(owner, name, tag);
    }

    public void issue(String owner, String name, String title, String body) throws TvException {
      tv.volumeUp(owner, name, title, body);
    }

    public void closeIssue(String owner, String name, int number) throws TvException {
      tv.volumeDown(owner, name, number);
    }

    public void comment(String owner, String name, int number, String body) throws TvException {
      tv.channelUp(owner, name, number, body);
    }

    public void pullRequest(String owner, String name, String head, String base) throws TvException {
      tv.channelDown(owner, name, head, base);
    }

    public void merge(String owner, String name, int number) throws TvException {
      tv.previous(owner, name, number);
    }

    public void closePullRequest(String owner, String name, int number) throws TvException {
      tv.next(owner, name, number);
    }

    public void review(String owner, String name, int number, String body) throws TvException {
      tv.play(owner, name, number, body);
    }

    public void approve(String owner, String name, int number) throws TvException {
      tv.stop(owner, name, number);
    }

    public void requestChanges(String owner, String name, int number, String body) throws TvException {
      tv.record(owner, name, number, body);
    }

    public void commentOnReview(String owner, String name, int number, int comment, String body) throws TvException {
      tv.rewind(owner, name, number, comment, body);
    }

    public void createFile(String owner, String name, String path, String content) throws TvException {
      tv.forward(owner, name, path, content);
    }

    public void updateFile(String owner, String name, String path, String content) throws TvException {
      tv.pause(owner, name, path, content);
    }

    public void deleteFile(String owner, String name, String path) throws TvException {
      tv.mute(owner, name, path);
    }

    public void createLabel(String owner, String name, String color, String name2) throws TvException {
      tv.unmute(owner, name, color, name2);
    }

    public void deleteLabel(String owner, String name, String name2) throws TvException {
      tv.volumeUp(owner, name, name2);
    }

    public void createMilestone(String owner, String name, String title) throws TvException {
      tv.volumeDown(owner, name, title);
    }

    public void closeMilestone(String owner, String name, String title) throws TvException {
      tv.channelUp(owner, name, title);
    }

    public void deleteMilestone(String owner, String name, String title) throws TvException {
      tv.channelDown(owner, name, title);
    }

    public void createProject(String owner, String name, String title) throws TvException {
      tv.previous(owner, name, title);
    }

    public void deleteProject(String owner, String name, String title) throws TvException {
      tv.next(owner, name, title);
    }

    public void createColumn(String owner, String name, String project, String title) throws TvException {
      tv.play(owner, name, project, title);
    }

    public void deleteColumn(String owner, String name, String project, String title) throws TvException {
      tv.stop(owner, name, project, title);
    }

    public void createCard(String owner, String name, String project, String column, String content) throws TvException {
      tv.record(owner, name, project, column, content);
    }

    public void moveCard(String owner, String name, String project, String column, String content) throws TvException {
      tv.rewind(owner, name, project, column, content);
    }

    public void deleteCard(String owner, String name, String project, String column, String content) throws TvException {
      tv.forward(owner, name, project, column, content);
    }

    public void createTeam(String owner, String name, String slug) throws TvException {
      tv.pause(owner, name, slug);
    }

    public void deleteTeam(String owner, String name, String slug) throws TvException {
      tv.mute(owner, name, slug);
    }

    public void addMember(String owner, String name, String team, String user) throws TvException {
      tv.unmute(owner, name, team, user);
    }

    public void removeMember(String owner, String name, String team, String user) throws TvException {
      tv.volumeUp(owner, name, team, user);
    }

    public void createHook(String owner, String name, String name2, String config) throws TvException {
      tv.volumeDown(owner, name, name2, config);
    }

    public void deleteHook(String owner, String name, int id) throws TvException {
      tv.channelUp(owner, name, id);
    }

    public void pingHook(String owner, String name, int id) throws TvException {
      tv.channelDown(owner, name, id);
    }

    public void createStatus(String owner, String name, String sha, String state, String targetUrl, String description, String context) throws TvException {
      tv.previous(owner, name, sha, state, targetUrl, description, context);
    }

    public void updateStatus(String owner, String name, String sha, String state, String targetUrl, String description, String context) throws TvException {
      tv.next(owner, name, sha, state, targetUrl, description, context);
    }

    public void createDeployKey(String owner, String name, String title, String key) throws TvException {
      tv.play(owner, name, title, key);
    }

    public void deleteDeployKey(String owner, String name, int id) throws TvException {
      tv.stop(owner, name, id);
    }

    public void createGist(String description, String filename, String content) throws TvException {
      tv.record(description, filename, content);
    }

    public void fork(String owner, String name) throws TvException {
      tv.rewind(owner, name);
    }

    public void star(String owner, String name) throws TvException {
      tv.forward(owner, name);
    }

    public void unstar(String owner, String name) throws TvException {
      tv.pause(owner, name);
    }

    public void watch(String owner, String name) throws TvException {
      tv.mute(owner, name);
    }

    public void unwatch(String owner, String name) throws TvException {
      tv.unmute(owner, name);
    }

    public void createPage(String owner, String name, String path, String sha) throws TvException {
      tv.volumeUp(owner, name, path, sha);
    }

    public void updatePage(String owner, String name, String path, String sha) throws TvException {
      tv.volumeDown(owner, name, path, sha);
    }

    public void deletePage(String owner, String name, String path) throws TvException {
      tv.channelUp(owner, name, path);
    }

    public void createKey(String title, String key) throws TvException {
      tv.channelDown(title, key);
    }

    public void deleteKey(int id) throws TvException {
      tv.previous(id);
    }

  }
```